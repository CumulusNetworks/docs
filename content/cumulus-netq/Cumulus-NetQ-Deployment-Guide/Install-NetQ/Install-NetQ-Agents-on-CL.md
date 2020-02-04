---
title: Install and Configure the NetQ Agent on Cumulus Linux Switches
author: Cumulus Networks
weight: 419
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
draft: true
---
After installing your Cumulus NetQ software, you should install the  NetQ 2.4.0 Agents on each switch you want to monitor. NetQ 2.4 Agents can be installed on switches running:

- Cumulus Linux version 3.3.2-3.7.x
- Cumulus Linux version 4.0.0 and later

This topic describes how to install and configure the NetQ Agent and CLI on switches running Cumulus Linux OS.

## Prepare for Installation

To install the NetQ Agent and CLI you need to install `netq-agent` and `netq-apps` on each switch. These are available from the Cumulus Networks repository.

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/) so `apt-get` can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Add NetQ Debian Repository

Edit the `/etc/apt/sources.list` file to add the repository for Cumulus NetQ.

*Note that NetQ has a separate repository from Cumulus Linux.*

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-2.4
...
```

{{%notice tip%}}
The repository `deb http://apps3.cumulusnetworks.com/repos/deb     CumulusLinux-4 netq-latest` can be used if you want to always retrieve the latest posted version of NetQ.
{{%/notice%}}

## Install NetQ Agent on Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1. Verify that [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) is running on the switch. Switches must be in time synchronization with the NetQ Platform to enable useful statistical analysis.

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

2. Update the local `apt` repository, then install the NetQ software on the switch.

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get install netq-agent
```

3. Verify you have the correct version of the Agent.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

    You should see version 2.4.0 and update 25 in the results. For example:

    - Cumulus Linux 3.3.2-3.7.x
      - netq-agent_**2.4.0**-cl3u**25**~1579642196.aeb67d8_armel.deb
      - netq-agent_**2.4.0**-cl3u**25**~1579642196.aeb67d8_amd64.deb

    - Cumulus Linux 4.0.0
      - netq-agent_**2.4.0**-cl4u**25**~1579822727.aeb67d82_amd64.deb 
    
4. Restart `rsyslog` so log files are sent to the correct destination.

```
cumulus@switch:~$ sudo systemctl restart rsyslog.service
```

5. Continue with [NetQ Agent configuration](#configure-your-netq-agents) or install the NetQ CLI in the next section.

## Install NetQ CLI on Cumulus Linux Switch

A simple process installs the NetQ CLI on a Cumulus switch.

1. Update the local `apt` repository, then install the CLI software on the switch.

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get install netq-apps
```

4. Verify you have the correct version of the CLI.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-apps
```

    You should see version 2.4.0 and update 25 in the results. For example:

    - Cumulus Linux 3.3.2-3.7.x
      - netq-apps_**2.4.0**-cl3u**25**~1579642196.aeb67d8_armel.deb
      - netq-apps_**2.4.0**-cl3u**25**~1579642196.aeb67d8_amd64.deb
    - For Cumulus Linux 4.0.0
      - netq-apps_**2.4.0**-cl4u**25**~1579822727.aeb67d82_amd64.deb 

5. Continue with configuration in the next section.

## Configure the NetQ CLI

Two methods are available for configuring the NetQ CLI on a switch:

- Use the NetQ CLI; refer to the next section
- Edit the configuration file on the switch; refer to [Configure NetQ CLI Using a Configuration File](#configure-netq-cli-using-a-configuration-file)

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment.

<details><summary>Configuring the CLI for On-premises Deployments</summary>

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

This example uses an IP address of 192.168.1.0 and the default port and VRF.

```
cumulus@switch:~$ sudo netq config add cli server 192.168.1.0
cumulus@switch:~$ sudo netq config restart cli
```

{{%notice tip%}}
If you have a server cluster deployed, use the IP address of the master server.
{{%/notice%}}

</details>
<details><summary>Configuring the CLI for Cloud Deployments</summary>
Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>] [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

<details><summary>For Switches with Internet Access</summary>

To configure the CLI for switches with Internet access in cloud deployments, you need your access keys (refer to [Generate Access Keys]()) or a keys file, and the premises name you want to query.  You must specify the premises whether you have only one premises or multiple premises.

#### Create a Keys File

In version 2.2.1 and later, you can save your access keys to a YAML file for easy reference, and to avoid having to type or copy the key values. You can:

- Store the file wherever you like; for example, in */home/cumulus/* or */etc/netq*
- Name the file whatever you like; for example, credentials.yml, creds.yml, or keys.yml
- BUT, the file must have the following format:

  ```
  access-key: <user-access-key-value-here>
  secret-key: <user-secret-key-value-here>
  ```

#### Configure CLI Using Access Keys

This example configures the CLI to access the NetQ Cloud service, *api.netq.cumulusnetworks.com*, the *datacenterwest* premises, the default port and VRF, and uses sample access keys.

*Be sure to use your own access keys and premises name when you run this command.*

```
cumulus@switch:~$ sudo netq config add cli server api.netq.cumulusnetworks.com access-key b409b135792850a1726f55534279dd3c8b3ec55e8b25144d4739abcdebe8149e secret-key /vAGywae2E4xVZg8F+HtS6h12378ZbBP6HXa3JLdJWc= premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

#### Configure CLI Using a Keys File

This example configures the CLI to access the NetQ Cloud service, *api.netq.cumulusnetworks.com*, the *datacenterwest* premises, the *netqcreds.yml* key file, and the default port and VRF.

*Be sure to include the full path the to key file and specify your own premises name when you run this command.*

```
cumulus@switch:~$ netq config add cli server api.netq.cumulusnetworks.com cli-keys-file //home/cumulus/netqcreds.yml> premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

#### View Data for a Different Premises

If you have multiple premises and want to query data from a different premises than you originally configured, rerun the `netq config add cli server` command with the desired premises name. You can only view the data for one premises at a time with the CLI.

</details>
<details><summary>For Switches without Internet Access</summary>

You can use the CLI proxy that is part of the NetQ Cloud Server or Appliance with NetQ 2.2.2 and later to manage CLI access on your switches. To configure the proxy, run the following commands, using the IP address and port of your proxy server:

```
netq xxx proxy-host <text-proxy-host> proxy-port <text-proxy-port>
```

Then configure the CLi in the same way as for switches with Internet access.
</details>
</details>

### Configure NetQ CLI Using a Configuration File

You can configure the NetQ CLI in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice.
2. Locate the *netq-cli* section, or add it.
3. Set the parameters for the CLI as follows:
    - port: 32708 (default configuration)
    - server: IP address of the NetQ server or NetQ Appliance
    - premises: Name of the premises to view

Your configuration should be similar to this:

```
netq-cli:
  port: 443
  premises: datacenterwest
  server: api.netq.cumulusnetworks.com
```

## Configure Your NetQ Agents

Once the NetQ Agents have been installed on the network switches you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the switch, or
- Use the NetQ CLI.

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

Now that the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Server or Appliance.

{{%notice info%}}
If you intend to use VRF, refer to [Configure the Agent to Use VRF](#configure-the-agent-to-use-a-vrf). If you intend to specify a port for communication, refer to [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port).
{{%/notice%}}

This example uses an IP address of *192.168.1.254* for the NetQ hardware.

```
cumulus@switch:~$ netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
cumulus@switch:~$ netq config restart agent
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