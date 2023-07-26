---
title: Use netconsole with syslog on Cumulus Linux Switches
author: NVIDIA
weight: 380
toc: 4
---

`{{<exlink url="https://www.kernel.org/doc/Documentation/networking/netconsole.txt" text="netconsole">}}` is a Linux feature that allows you to redirect kernel messages output from `dmesg` to a location across the network using UDP. You can capture and store these messages on a `syslog` server to investigate issues on the Cumulus Linux switch that is generating the `dmesg` output. This is useful where a physical console is not connected and you need to debug kernel events, such as system crashes and unexpected reboots.

`netconsole` is not a replacement for a physical console. It does not provide an interactive console to the switch; it is a remote logging service only. `netconsole` is also not available until the network has initialized on boot. Log data from early in the boot cycle is not captured. Use `netconsole` whenever a physical console is not available to log data.

## Configure the netconsole Module

{{%notice note %}}
You must reboot the switch at the end of this process to apply the changes.
{{%/notice%}}

To configure the `netconsole` module on your Cumulus Linux switch:

1. Set up the `netconsole` kernel module to load on boot:

   ```
   cumulus@switch:~$ echo netconsole | sudo tee /etc/modules-load.d/netconsole.conf
   ```

2. Configure the `netconsole` kernel module options to point to your `syslog` server.

   ```
   cumulus@switch:~$ echo 'options netconsole netconsole=[...]' | sudo tee /etc/modprobe.d/netconsole.conf
   ```

   In the above command, replace `[...]` with the desired configuration. The format for the options is as follows (with default values in parentheses):

   ```
   netconsole=[+][src-port]@[src-ip]/[<dev>],[tgt-port]@<tgt-ip>/[tgt-macaddr]
      where
            +            if present, enable extended console support
            src-port     source UDP port (6665)
            src-ip       source IP address (<dev> interface address)
            dev          network interface (eth0)
            tgt-port     UDP port of the syslog server (6666)
            tgt-ip       IP address of the syslog server
            tgt-macaddr  Ethernet MAC address of the next hop to the syslog server (broadcast)
   ```

    - The `netconsole` module requires only the `tgt-ip` parameter; other parameters use their default value if unspecified.
    - Because the `netconsole` module might get loaded before you configure `dev`, you must specify `src-ip`.
    - If the `syslog` server is not on the same Ethernet segment as the source device, you must specify `tgt-macaddr`.
    - It is more efficient to specify `tgt-macaddr` than to use the default, which is an Ethernet broadcast.

    To determine the values `dev` and `tgt-macaddr`, use the following procedure. When running the commands, replace the values between angle brackets (< >) to match your configuration.

    1. Use `ip route get` to determine the interface and IP address of the next hop to the `syslog` server.

       If the `syslog` server is reachable through a front port, run:

       ```
       cumulus@switch:~$ ip route get <tgt-ip>
       ```

       If the `syslog` server is reachable through the management port (mgmt VRF), run:

       ```
       cumulus@switch:~$ ip route get <tgt-ip> vrf mgmt
       ```
       <!-- vale off -->
       Look at the output of the `ip route get` command. If it is in the following format (without a `via` keyword), the `syslog` server is on the same Ethernet segment. The value to use for the `dev` parameter is the `dev` value reported in the output, `eth0` in this example. The _nexthop ip_ is the first field.
       <!-- vale on -->
       ```
       10.230.130.20 dev eth0 table mgmt src 10.230.130.211 uid 1000
       ```
       <!-- vale off -->
       If the output of the `ip route get` command is in the following format (with a `via` keyword), you reached the `syslog` server through a gateway. The value to use for the `dev` parameter is the `dev` value reported in the output, `eth0` in this example. The _nexthop ip_ is the `via` value, 10.230.130.1 in this example.
       <!-- vale on -->
       ```
       10.230.15.31 via 10.230.130.1 dev eth0 table mgmt src 10.230.130.211 uid 1000
       ```

    1. Use the `arping` command to determine the next hop MAC address:

       ```
       cumulus@switch:~$ sudo arping -i <dev> -c1 -r <nexthop ip>
       ```

       The value to use for the `tgt-macaddr` parameter is the output of the previous command.

       For example, to configure a switch with `netconsole` logging to a `syslog` server reachable at IP address 10.230.15.31 and port 514, run the following commands:

       ```
       cumulus@switch:~$ ip route get 10.230.15.31 vrf mgmt
       10.230.15.31 via 10.230.130.1 dev eth0 table mgmt src 10.230.130.211 uid 0
           cache
       cumulus@switch:~$ sudo arping -i eth0 -c1 -r 10.230.130.1
       d8:c4:97:b5:be:b7
       cumulus@switch:~$ ip -4 addr show dev eth0
       2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq master mgmt state UP group default qlen 1000
           inet 10.230.130.211/24 brd 10.230.130.255 scope global dynamic eth0
              valid_lft 6855sec preferred_lft 6855sec
       cumulus@switch:~$ echo netconsole > /etc/modules-load.d/netconsole.conf
       cumulus@switch:~$ echo 'options netconsole netconsole=@10.230.130.211/eth0,514@10.230.15.31/d8:c4:97:b5:be:b7' > /etc/modprobe.d/netconsole.conf
       cumulus@switch:~$ sudo reboot
       ```

3.  You can increase or decrease the amount of data you want to log.

      - To increase the amount of data the kernel logs (see {{<exlink url="https://linuxconfig.org/introduction-to-the-linux-kernel-log-levels" text="Introduction to the Linux kernel log levels at linuxconfig.org">}}), adjust the log level. By default, a Cumulus Linux switch logs kernel data at level 3 (KERN\_ERR). It might be useful to log all the data when trying to debug an issue. To do this, increase the kernel `printk` value to *7* in the `/etc/systctl.d/99-sysctl.conf` file:

      ```
      $ echo 'kernel.printk = 7 4 1 7' | sudo tee -a /etc/sysctl.d/99-sysctl.conf
      ```

      - To limit the data to just kernel panic logs, set the kernel module option `oops_only` to *1* by appending `oops_only=1` to the `options netconsole` line you used in `/etc/modprobe.d/netconsole.conf`.

        ``` 
        cumulus@switch:~$ echo 'options netconsole netconsole=@10.230.130.211/eth0,514@10.230.15.31/d8:c4:97:b5:be:b7 oops_only=1' | sudo tee /etc/modprobe.d/netconsole.conf
        ```

4.  Reboot the switch. The boot sequence applies the settings.

    ```
    cumulus@switch:~$ sudo reboot
    ```

### Create a Running Configuration

The following procedure only impacts the running kernel (otherwise known as a non-persistent configuration) on the switch. After the switch reboots, you lose these settings.

To create a running configuration on a Cumulus Linux switch:

1.  Increase the kernel logging level (optional).

    ```
    cumulus@switch:~$ sudo dmesg -n 7
    ```

2.  Load the `netconsole` kernel module with the appropriate options.

    {{%notice note%}}
If the `syslog` server is reachable through the management VRF, when loading the `netconsole` module at runtime, &lt;dev> must be the name of the management VRF interface, _mgmt_.
{{%/notice%}}

    ```
    cumulus@switch:~$ sudo modprobe netconsole netconsole=@10.20.30.40/eth0,6666@10.20.30.255/00:22:33:aa:bb:cc
    ```

    Using the same configuration as above:

    ```
    cumulus@switch:~$ sudo modprobe netconsole netconsole=@10.230.130.211/mgmt,514@10.230.15.31/d8:c4:97:b5:be:b7
    ```

    To use the `oops_only` setting, append this option to the `modprobe` command:

    ```
    cumulus@switch:~$ sudo modprobe netconsole netconsole=@10.230.130.211/mgmt,514@10.230.15.31/d8:c4:97:b5:be:b7 oops_only=1
    ```

### Configure an rsyslog Server to Receive Console Log Data

The following steps show how to configure an `rsyslog` server to receive UDP traffic on port 6666 from two devices and create separate log files for each. You can add this to your existing `rsyslog` configuration.

{{%notice note %}}
You must be the root (super) user on your server to perform these steps.
{{%/notice%}}

1. Create a specific configuration file with your favorite editor:

   ```
   cumulus@switch:~$ sudo vi /etc/rsyslog.d/remote-netconsole.conf
   ```

2. Add the following content to the file. Change the IP addresses to match the IP addresses of your switches and the appropriate destination log files.

    ``` 
    $ModLoad imudp

    $RuleSet remote
    # Modify the following template according to the devices on which you want to
    # store logs. Change the IP address and subdirectory name on each
    # line. Add or remove "else if" lines according to the number of your
    # devices.
    if $fromhost-ip=='10.20.30.40' then /var/log/remote/spineswitch1/console.log
    else if $fromhost-ip=='10.20.30.41' then /var/log/remote/leafswitch1/console.log
    else if $fromhost-ip=='10.20.30.42' then /var/log/remote/leafswitch2/console.log
    else /var/log/remote/other/console.log
    & stop

    $InputUDPServerBindRuleset remote
    $UDPServerRun 6666

    $RuleSet RSYSLOG_DefaultRuleset
    ```

2.  Create a directory to store the log files. The following example creates a directory called `/var/log/remote`.

    ```
    # mkdir /var/log/remote
    ```

3.  Restart `rsyslog`.

    ```
    # systemctl restart rsyslog.service
    ```

## Test the Setup

You can test this setup in one of two ways:

- Append data to the kernel log
- Intentionally crash the switch (which causes a catastrophic failure of the switch)

### Append Data to the Kernel Log

To create a new kernel log message and verify that the `syslog` server recorded it, run the following command on the switch configured with `netconsole`:

```
cumulus@switch:~$ echo "<0>test message $(date +%s)" | sudo tee /dev/kmsg
```

Confirm that the same message output by this command is also recorded on the `syslog` server.

### Crash a Switch

{{%notice warning%}}
This causes a catastrophic failure of the switch and results in an immediate reboot. Ensure your network is ready for this to occur and you understand the consequences.
{{%/notice%}}

To invoke a kernel panic to test the process, log in to the switch you want to crash and run the following command:

```
cumulus@switch:~$ echo c | sudo tee /proc/sysrq-trigger
```

If the process is working correctly, you see log data sent to the `rsyslog` server.

### Log File Sample Output

Here is some sample output from the `rsyslog` server:

   ```
   May 12 17:13:59 leafswitch1.network.com [17593.272492] sysrq: SysRq :
   May 12 17:13:59 Trigger a crash
   May 12 17:13:59 leafswitch1.network.com [17593.277181] BUG: unable to handle kernel
   May 12 17:13:59 NULL pointer dereference
   May 12 17:13:59 leafswitch1.network.com  at           (null)
   May 12 17:13:59 leafswitch1.network.com [17593.285951] IP:
   May 12 17:13:59 leafswitch1.network.com  [<ffffffff81496256>] sysrq_handle_crash+0x16/0x20
   May 12 17:13:59 leafswitch1.network.com [17593.292773] PGD 4cb06067
   May 12 17:13:59 PUD 4ca44067
   May 12 17:13:59 PMD 0
   May 12 17:13:59 leafswitch1.network.com
   May 12 17:13:59 leafswitch1.network.com [17593.297566] Oops: 0002 [#1]
   May 12 17:13:59 SMP
   ...
   ```
