---
title: Install and Configure the NetQ Agent on Cumulus Linux Switches
author: Cumulus Networks
weight: 118
toc: 5
---
After installing your Cumulus NetQ software, you should install the  NetQ 2.4.1 Agents on each switch you want to monitor. NetQ 2.4 Agents can be installed on switches running:

- Cumulus Linux version 3.3.2-3.7.x
- Cumulus Linux version 4.0.0 and later

## Prepare for NetQ Agent Installation on a Cumulus Linux Switch

For servers running Cumulus Linux, you need to:

- Install and configure NTP, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so `apt-get` can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Verify NTP is Installed and Configured

Verify that [NTP]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}}) is running on the switch. The switch must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

```
cumulus@switch:~$ sudo systemctl status ntp
[sudo] password for cumulus:
● ntp.service - LSB: Start NTP daemon
        Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
        Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
          Docs: man:systemd-sysv-generator(8)
        CGroup: /system.slice/ntp.service
                └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114
```

If NTP is not installed, install and configure it before continuing.  

If NTP is not running:

- verify the IP address or hostname of the NTP server in the `/etc/ntp.conf` file, and then
- reenable and start the NTP service using the `systemctl [enable|start] ntp` commands.

{{%notice tip%}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (`ntp@<vrf-name>` versus just `ntp`) in the above commands.
{{%/notice%}}

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each switch or host. This is available from the Cumulus Networks repository.

To obtain the NetQ Agent package:

Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.

*Note that NetQ has a separate repository from Cumulus Linux.*

{{< tabs "TabID0" >}}

{{< tab "Cumulus Linux 3.x" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}

{{< /tab >}}

{{< tab "Cumulus Linux 4.x" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

### Add the Apt Repository Key (Cumulus Linux 4.0 Only)

Add the `apps3.cumulusnetworks.com` authentication key to Cumulus Linux.

```
cumulus@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -
```

## Install the NetQ Agent on Cumulus Linux Switch

After completing the preparation steps, you can successfully install the agent onto your switch.

To install the NetQ Agent:

1. Update the local `apt` repository, then install the NetQ software on the switch.

    ```
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    You should see version 2.4.1 and update 26 or later in the results. For example:

    - Cumulus Linux 3.3.2-3.7.x
      - netq-agent_**2.4.1**-cl3u**26**~1581350572.c5ec3e5_armel.deb
      - netq-agent_**2.4.1**-cl3u**26**~1581350238.c5ec3e5a_amd64.deb

    - Cumulus Linux 4.0.0
      - netq-agent_**2.4.1**-cl4u**26**~1581350349.c5ec3e5a_armel.deb
      - netq-agent_**2.4.1**-cl3u**26**~1581350537.c5ec3e5_amd64.deb

3. Restart `rsyslog` so log files are sent to the correct destination.

    ```
    cumulus@switch:~$ sudo systemctl restart rsyslog.service
    ```

4. Continue with NetQ Agent configuration in the next section.

## Configure the NetQ Agent on a Cumulus Linux Switch

After the NetQ Agents have been installed on the switches you want to monitor, the NetQ Agents must be configured to obtain useful and relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the switch, or
- Use the NetQ CLI.

### Configure NetQ Agents Using a Configuration File

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    root@rhel7:~# sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-agent* section, or add it.

3. Set the parameters for the agent as follows:
    - port: 31980 (default configuration)
    - server: IP address of the NetQ Platform or NetQ Appliance where the agent should send its collected data
    - vrf: default (default) or one that you specify

    Your configuration should be similar to this:

    ```
    netq-agent:
    port: 31980
    server: 127.0.0.1
    vrf: default
    ```

### Configure NetQ Agents Using the NetQ CLI

If the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Platform or NetQ Appliance. To configure the NetQ CLI, refer to {{<link title="Install and Configure the NetQ CLI on Cumulus Linux Switches#install-the-netq-cli-installation-on-a-cumulus-linux-switch">}}.

{{%notice info%}}
If you intend to use VRF, refer to {{<link url="#configure-the-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, refer to {{<link url="#configure-the-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.
{{%/notice%}}

Use the following command to configure the NetQ Agent:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
```

This example uses an IP address of *192.168.1.254* and the default port and VRF for the NetQ hardware.

```
cumulus@switch:~$ sudo netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
cumulus@switch:~$ sudo netq config restart agent
```

## Configure Advanced NetQ Agent Settings on a Cumulus Linux Switch

A couple of additional options are available for configuring the NetQ Agent. If you are using VRF, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ Agents to communicate with the NetQ Platform only via a [VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF" >}}), including a [management VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Management-VRF" >}}). To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if the management VRF is configured and you want the agent to communicate with the NetQ Platform over it, configure the agent like this:

```
cumulus@leaf01:~$ sudo netq config add agent server 192.168.1.254 vrf mgmt
cumulus@leaf01:~$ sudo netq config restart agent
```

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ Platform and NetQ Agents. If you want the NetQ Agent to communicate with the NetQ Platform via a different port, you need to specify the port number when configuring the NetQ Agent like this:

```
cumulus@leaf01:~$ sudo netq config add agent server 192.168.1.254 port 7379
cumulus@leaf01:~$ sudo netq config restart agent
```
