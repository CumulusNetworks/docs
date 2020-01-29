---
title: Install and Configure the NetQ Agent and CLI on Cumulus Linux Switches
author: Cumulus Networks
weight: 419
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After installing your Cumulus NetQ software, you should install the corresponding version of the NetQ Agents on each node you want to monitor. NetQ 2.4 Agents can be installed and run on switches running Cumulus Linux version 3.3.2-4.0.x.

This topic describes how to install and configure the NetQ Agent and CLI on Cumulus Linux switches.

{{%notice note%}}
You only need to install the NetQ Agent on switches running Cumulus Linux 3.3.2-3.3.x, or on switches running Cumulus Linux 4.0.x that have version 2.3.1 of the Agent pre-installed.

Check the version of the NetQ Agent running on your switch using the `dpkg-query -W -f '${Package}\t${Version}\n' netq-agent` command. If the version installed is:

- 2.3.1-xxx, then you need to install the 2.4.0 Agent
- 2.4.0-cl3u<24 or less>~xxx *or* 2.4.0-cl4u<24 or less>~xxx, then you need to install an updated 2.4.0 Agent. Follow the instructions in [Upgrade the NetQ Agent on Cumulus Linux Switches](../../Upgrade-NetQ/Upgrade-NetQ-Agents-on-Cumulus-Linux-Switches/), then return here to follow the configuration steps.
- 2.4.0-cl3u<25 or greater>~xxx *or* 2.4.0-cl4u<25 or greater>~xxx, then you are running the latest version. There is no need to update the NetQ 2.4.0 Agent and you can skip to [Configure Your NetQ Agents](#configure-your-netq-agents).
{{%/notice%}}

## Prepare for Installation

To install the NetQ Agent you need to install `netq-agent` on each switch. To install the NetQ CLI you need to install `netq-apps` on each switch.

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/) so `apt-get` can access the software package on the Cumulus Networks repository.
{{%/notice%}}

### Add NetQ Debian Repository

Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.

*Note that NetQ has a separate repository from Cumulus Linux.*

<details><summary>Cumulus Linux 3.x</summary>
```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb     CumulusLinux-3 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}
</details>

<details><summary>Cumulus Linux 4.x</summary>
```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb     CumulusLinux-4 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}
</details>

### Add the Apt Repository Key (Cumulus Linux 4.0 Only)

Add the `apps3.cumulusnetworks.com` authentication key to Cumulus Linux.

    cumulus@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -

## Install NetQ Agent and CLI

A simple process installs the NetQ Agent and CLI on a Cumulus switch.

1.  Update the local `apt` repository, then install the NetQ meta
    package on the switch.

        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install netq-agent netq-apps

2.  Verify that [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/)
    is running on the host node. Nodes must be in time synchronization with the
    NetQ Platform to enable useful statistical analysis.

        cumulus@switch:~$ sudo systemctl status ntp
        [sudo] password for cumulus:
        ● ntp.service - LSB: Start NTP daemon
           Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
           Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
             Docs: man:systemd-sysv-generator(8)
           CGroup: /system.slice/ntp.service
                   └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114

3.  Restart `rsyslog` so log files are sent to the correct destination.

        cumulus@switch:~$ sudo systemctl restart rsyslog.service

<!-- 4. Continue with [Configure Your NetQ Agents](#configure-your-netq-agents). -->

## Configure the NetQ CLI

Two methods are available for configuring the NetQ CLI on a switch:

- Edit the configuration file on the switch, or
- Configure and run NetQ CLI commands on the switch.

*Note that the steps to install the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment.*

<details><summary>Configure NetQ CLI for on-premises deployments</summary>

Configuring the CLI for *on-premises* deployments requires only two commands:

```
netq config add cli server <ip-address-of-netq-server-or-appliance>
netq config restart cli
```
</details>

<details><summary>Configure NetQ CLI for cloud deployments</summary>

Configuring the CLI for *cloud* deployments also only requires two commands; however, there are a couple of additional options that you can apply:

- In NetQ 2.2.2 and later, if your nodes do not have Internet access, you can use the CLI proxy that is available on the NetQ cloud server or NetQ Cloud Appliance.
- In NetQ 2.2.1 and later, you can:
    - save your access credentials in a file and reference that file here to simplify the configuration commands
    - specify which premises you want to query


<details><summary>For Switches with Internet Access</summary>

Run the following commands, being sure to replace the key values with your generated keys. Refer to [Generate Access Keys](../Prepare-NetQ-Cloud/#generate-access-keys) if needed.

```
$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name>
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```

Or, if you have created a keys file as noted in the installation procedures for the NetQ Cloud server or Appliance, run the following commands. Be sure to include the *full path* the to file.

```
$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file </full-path/credentials-filename.yml> premises text-premises-name>
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```

If you have multiple premises, be sure to include which premises you want to query. Rerun this command to query a different premises.

```
$ netq config add cli server api.netq.cumulusnetworks.com access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name>
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```
</details>

<details><summary>For Switches without Internet Access</summary>

You can use the CLI proxy that is part of the NetQ Cloud Server or Appliance with NetQ 2.2.2 and later to manage CLI access on your nodes. To make use of the proxy, you must point each switch or host to the NetQ Cloud Server or Appliance. Run the following commands, using the IP address of the proxy:

```
$ netq config add cli server <proxy-ip-addr>
Updated cli server <proxy-ip-addr> vrf default port 443. Please restart netqd (netq config restart cli)

$ netq config restart cli
Restarting NetQ CLI... Success!
```
</details>
</details>

## Configure Your NetQ Agents

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the device, or
- Configure and run NetQ CLI commands on the device.

### Configure NetQ Agents Using a Configuration File

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice.
2. Locate the *netq-agent* section, or add it.
3. Set the parameters for the agent as follows:
    - port: 31980 (default configuration)
    - server: IP address of the NetQ server or NetQ Appliance where the agent should send its collected data

Your configuration should be similar to this:

```
netq-agent:
  port: 31980
  server: 127.0.0.1
```

### Configure NetQ Agents Using the NetQ CLI

The NetQ CLI was installed when you installed the NetQ Agent; however, to use it to configure your NetQ Agents, you must first configure the CLI to communicate with your NetQ server or appliance.

{{%notice info%}}

If you intend to use VRF, refer to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, refer to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).

{{%/notice%}}

This example uses an IP address of *192.168.1.254* for the NetQ hardware.

```
$ netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
$ netq config restart agent
```

## Configure Advanced NetQ Agent Settings

### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a
[management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:

```
cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
cumulus@leaf01:~$ netq config restart agent
```

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

```
cumulus@leaf01:~$ netq config add agent server 192.168.1.254 port 7379
cumulus@leaf01:~$ netq config restart agent
```

<!-- ## Configure Advanced NetQ CLI Settings

proxy -->
