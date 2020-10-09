---
title: Use netconsole with syslog on Cumulus Linux Switches
author: Cumulus Networks
weight: 380
toc: 4
---

`{{<exlink url="https://www.kernel.org/doc/Documentation/networking/netconsole.txt" text="netconsole">}}` is a feature of Linux that allows you to redirect kernel messages output from `dmesg` to a location across the network using UDP. These messages can be captured and stored on a `syslog` server for investigating issues on a Cumulus Linux switch where the `dmesg` output was generated. This is particularly useful in situations where a physical console is not connected and you need to debug kernel events such as system crashes and unexpected reboots.

`netconsole` is not a replacement for a physical console. It does not provide an interactive console to the switch; it is a remote logging service only. `netconsole` is also limited in that it is not available until the network has initialized on boot. Log data from early in the boot cycle does not get captured. That does not mean you should avoid using `netconsole`. It is a great tool to use whenever a physical console is not available to log data.

## Configure the netconsole Module on Your Cumulus Linux Switch

{{%notice note %}}

You must reboot the switch at the end of this process to apply the changes.

{{%/notice%}}

1.  Set up the `netconsole` kernel module to load on boot:

        cumulus@switch:~$ echo netconsole | sudo tee /etc/modules-load.d/netconsole.conf

2.  Configure the `netconsole` kernel module options to point to your `syslog` server.

    ```
    cumulus@switch:~$ echo 'options netconsole netconsole=[...]' | sudo tee /etc/modprobe.d/netconsole.conf
    ```

    In the above command, "[...]" must be replaced with the desired configuration. The format for the options is as follows (default values are shown in parentheses):

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

    Only the &lt;tgt-ip> parameter is required by the `netconsole` module; other parameters use their default value if unspecified. In practice, since the `netconsole` module may be loaded before &lt;dev> is configured, &lt;src-ip> must be specified. &lt;tgt-macaddr> must be specified if the `syslog` server is not on the same Ethernet segment as the source device. In any case, it is more efficient to specify &lt;tgt-macaddr> than to use the default which is an Ethernet broadcast.

    To determine the values for &lt;dev> and &lt;tgt-macaddr>, use the following procedure. When running the commands, replace the values between angle brackets ("<>") to match your configuration.

    1. Determine the interface and IP address of the next hop to the `syslog` server, using `ip route get`. If the `syslog` server is reachable through a front port, run:

           cumulus@switch:~$ ip route get <tgt-ip>

       If the `syslog` server is reachable through the management port ("mgmt" VRF), run:

           cumulus@switch:~$ ip route get <tgt-ip> vrf mgmt

       Looking at the output of the previous command, if it is of the following form (without a "via" keyword):

           10.230.130.20 dev eth0 table mgmt src 10.230.130.211 uid 1000

       then the `syslog` server is on the same Ethernet segment. The value to use for the <dev> parameter is the "dev" value reported in the output, "eth0" in this example. The _nexthop ip_ is the first field.

       If the output of the `ip rou get` command is of the following form (with a "via" keyword):

           10.230.15.31 via 10.230.130.1 dev eth0 table mgmt src 10.230.130.211 uid 1000

       then the `syslog` server is reached through a gateway. The value to use for the &lt;dev> parameter is the "dev" value reported in the output, "eth0" in this example. The _nexthop ip_ is the "via" value, "10.230.130.1" in this example.

    1. Next, determine the next hop MAC address using the `arping` command. Run:

           cumulus@switch:~$ sudo arping -i <dev> -c1 -r <nexthop ip>

       The value to use for the &lt;tgt-macaddr> parameter is the output of the previous command.

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

      - To increase the amount of data being logged by the kernel (see {{<exlink url="https://linuxconfig.org/introduction-to-the-linux-kernel-log-levels" text="Introduction to the Linux kernel log levels at linuxconfig.org">}}), adjust the log level. By default, a Cumulus Linux switch logs kernel data at level 3 (KERN\_ERR). It may be useful to log all the data when trying to debug an issue. To do this, increase the kernel `printk` value to *7* in the `/etc/systctl.d/99-sysctl.conf` file:

            $ echo 'kernel.printk = 7 4 1 7' | sudo tee -a /etc/sysctl.d/99-sysctl.conf

      - To limit the data to just kernel panic logs, set the kernel module option `oops_only` to *1* by appending `oops_only=1` to the `options netconsole` line you used in `/etc/modprobe.d/netconsole.conf`.

        ``` 
        cumulus@switch:~$ echo 'options netconsole netconsole=@10.230.130.211/eth0,514@10.230.15.31/d8:c4:97:b5:be:b7 oops_only=1' | sudo tee /etc/modprobe.d/netconsole.conf
        ```

4.  Reboot the switch. The settings are applied during the boot sequence.

        cumulus@switch:~$ sudo reboot

### Create a Running Configuration on a Cumulus Linux Switch

The following procedure only impacts the running kernel on the switch; this is known as a non-persistent configuration. Once the switch reboots, these settings are lost.

1.  Increase the kernel logging level (optional).

        cumulus@switch:~$ sudo dmesg -n 7

2.  Load the `netconsole` kernel module with the appropriate options.

    {{%notice note%}}

If the `syslog` server is reachable via the management VRF, when loading the `netconsole` module at runtime, &lt;dev> must be the name of the management VRF interface, _mgmt_.

{{%/notice%}}

        cumulus@switch:~$ sudo modprobe netconsole netconsole=@10.20.30.40/eth0,6666@10.20.30.255/00:22:33:aa:bb:cc

    Using the same configuration as above:

        cumulus@switch:~$ sudo modprobe netconsole netconsole=@10.230.130.211/mgmt,514@10.230.15.31/d8:c4:97:b5:be:b7

    To use the `oops_only` setting, append this option to the `modprobe` command:

        cumulus@switch:~$ sudo modprobe netconsole netconsole=@10.230.130.211/mgmt,514@10.230.15.31/d8:c4:97:b5:be:b7 oops_only=1

### Configure an rsyslog Server to Receive the Console Log Data

The following steps show how to configure an `rsyslog` server to receive UDP traffic on port 6666 from 2 devices and create separate log files for each. You can add this to your existing `rsyslog` configuration. These steps must be performed by the root (super) user on your server.

1.  Create a specific configuration file with your favorite editor:

        cumulus@switch:~$ sudo vi /etc/rsyslog.d/remote-netconsole.conf

    The file should contain:

    ``` 
    $ModLoad imudp
    $RuleSet remote

    # For each IP address that you want to store logs from,
    # add and modify the following two (!) lines:
    if $fromhost-ip=='10.20.30.40' then /var/log/remote/leafswitch1/console.log
    if $fromhost-ip=='10.20.30.41' then /var/log/remote/spineswitch2/console.log
    & stop

    $InputUDPServerBindRuleset remote
    $UDPServerRun 6666

    $RuleSet RSYSLOG_DefaultRuleset

    ```

    {{%notice note %}}

The highlighted text should be changed to match the IP  addresses of your switches and appropriate destination log files.

{{%/notice%}}

2.  Create a directory called `/var/log/remote` (or use a directory of your choice) to store the log files:

        # mkdir /var/log/remote

3.  Restart `rsyslog`.

        # systemctl restart rsyslog.service

## Test the Setup

You can test this setup in one of two ways:

- Appending data to the kernel log
- Intentionally crashing the switch (which causes a catastrophic failure of the switch &mdash; see below)

### Append Data to the Kernel Log

You can create a new kernel log message and verify that it is recorded on the `syslog` server.

Run the following command on the switch device that has been configured with `netconsole`:

    cumulus@switch:~$ echo "<0>test message $(date +%s)" | sudo tee /dev/kmsg

Confirm that the same message output by this command is also recorded on the `syslog` server.

### Intentionally Crashing a Switch

You can invoke a kernel panic to test the process.

{{%notice warning%}}

This causes a catastrophic failure of the switch and results in an immediate reboot. Please ensure your network is prepared for this to occur and you understand the consequences.

{{%/notice%}}

Log in to the switch you want to crash and run the following command:

    $ echo c | sudo tee /proc/sysrq-trigger

If the process is working correctly, you should see log data sent to the `rsyslog` server.

### Log File Sample Output

Here is some sample output from the `rsyslog` server:

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
