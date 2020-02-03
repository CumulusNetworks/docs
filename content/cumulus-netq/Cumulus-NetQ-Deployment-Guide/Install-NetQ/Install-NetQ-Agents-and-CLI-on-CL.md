---
title: Install and Configure the NetQ Agent and CLI on Cumulus Linux Switches
author: Cumulus Networks
weight: 419
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After installing your Cumulus NetQ software, you should install the  NetQ 2.4.0 Agents on each switch you want to monitor. NetQ 2.4 Agents can be installed on switches running:

- Cumulus Linux version 3.3.2-3.7.x
- Cumulus Linux version 4.0.0 and later

This topic describes how to install and configure the NetQ Agent and CLI on Cumulus Linux switches.

## Prepare for NetQ Agent Installation on a Cumulus Linux Switch

For servers running Cumulus Linux, you need to:

- Install and configure NTP, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/) so `apt-get` can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Verify NTP is Installed and Configured

Verify that [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) is running on the switch. The switch must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

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
- re-enable and start the NTP service using the `systemctl [enable|start] ntp` commands.

{{%notice tip%}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (`ntp@<vrf-name>` versus just `ntp`) in the above commands.
{{%/notice%}}

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each switch or host. This is available from the Cumulus Networks repository.

To obtain the NetQ Agent package:

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

```
cumulus@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -
```

## Install NetQ Agent on a Cumulus Linux Switch

After completing the preparation steps, you can successfully install the agent onto your switch.

To install the NetQ Agent:

1. Update the local `apt` repository and install the software on the switch.

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get install netq-agent
```

2. Verify you have the correct version of the Agent.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

    You should see version 2.4.0 and update 25 in the results. For example:

    - For Cumulus Linux 3.3.2-3.7.x:  
      - netq-agent_**2.4.0**-cl3u**25**~1579642196.aeb67d8_armel.deb
      - netq-agent_**2.4.0**-cl3u**25**~1579642196.aeb67d8_amd64.deb
    - For Cumulus Linux 4.0.0:
      -   netq-agent_**2.4.0**-cl4u**25**~1579822727.aeb67d82_amd64.deb 

3. Restart `rsyslog` so log files are sent to the correct destination.

```
cumulus@switch:~$ sudo systemctl restart rsyslog
```

4. Continue with [NetQ Agent Configuration](#configure-your-netq-agents), or if you want to use the NetQ CLI to configure the agent, go to the next section.

## Install NetQ CLI on a Cumulus Linux Switch

A simple process installs the NetQ CLI on a Cumulus Linux switch.

To install the NetQ Agent you need to install `netq-apps` on each switch or host. This is available from the Cumulus Networks repository.

To obtain the NetQ Agent package:

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

2. Update the local `apt` repository and install the software on the switch.

```
cumulus@switch:~$ sudo apt-get update
cumulus@switch:~$ sudo apt-get install netq-apps
```

3. Verify you have the correct version of the CLI.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

    You should see version 2.4.0 and update 25 in the results. For example:

    - For Cumulus Linux 3.3.2-3.7.x:  
      - netq-apps_**2.4.0**-cl3u**25**~1579642196.aeb67d8_armel.deb
      - netq-apps_**2.4.0**-cl3u**25**~1579642196.aeb67d8_amd64.deb
    - For Cumulus Linux 4.0.0:
      -   netq-apps_**2.4.0**-cl4u**25**~1579822727.aeb67d82_amd64.deb 

4. Continue with the next section.

## Configure the NetQ CLI on a Cumulus Linux Switch

Two methods are available for configuring the NetQ CLI on a switch:

- Run NetQ CLI commands on the switch; refer to the next section
- Edit the configuration file on the switch; refer to [Configure CLI Using File](#configure-netq-cli-using-configuration-file)

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment. Follow the instructions for your deployment type.

<details><summary>Configuring the CLI for On-premises Deployments</summary>

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [vrf <text-vrf-name>] [port <text-gateway-port>]
```
</details>
<details><summary>Configure NetQ CLI for cloud deployments</summary>

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

Refer to [Generate Access Keys](../../Install-NetQ/Prepare-NetQ-Cloud/#generate-access-keys) if you have not already created your access keys.

This example uses the individual access key, a premises of *datacenterwest*,  and the default Cloud address, port and VRF.  **Be sure to replace the key values with your generated keys if you are using this example on your server.**

```
cumulus@switch:~$ sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ sudo netq config restart cli
Restarting NetQ CLI... Success!
```

This example uses an optional keys file. Refer to [Generate Access Keys](../../Install-NetQ/Prepare-NetQ-Cloud/#generate-access-keys) for information about creating this file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

```
cumulus@switch:~$ sudo netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

cumulus@switch:~$ netq config restart cli
Restarting NetQ CLI... Success!
```

{{%notice tip%}}
Rerun this command if you have multiple premises and want to query a different premises.
{{%/notice%}}

</details>

### Configure NetQ CLI Using Configuration File

You can configure the NetQ CLI in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

```
root@rhel7:~# sudo nano /etc/netq/netq.yml
```

2. Locate the *netq-cli* section, or add it.

3. Set the parameters for the CLI as follows:

| Parameter | On-premises | Cloud |
| ----| ---- | ---- |
| netq-user | User who can access the CLI | User who can access the CLI |
| server | IP address of the NetQ server or NetQ Appliance | api.netq.cumulusnetworks.com |
| port (default) | 32708 | 443 |
| premises | NA | Name of premises you want to query |

An on-premises configuration should be similar to this:

```
netq-cli:
  netq-user: admin@company.com
  port: 32708
  server: 192.168.0.254
  ```

A cloud configuration should be similar to this:

```
netq-cli:
  netq-user: admin@company.com
  port: 443
  premises: datacenterwest
  server: api.netq.cumulusnetworks.com
```
</details>
</details>

## Configure the NetQ Agent on a Cumulus Linux Server

After the NetQ Agents have been installed on the switches you want to monitor, the NetQ Agents must be configured to obtain useful and relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the device, or
- Use the NetQ CLI.

### Configure NetQ Agents Using a Configuration File

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

```
root@rhel7:~# sudo nano /etc/netq/netq.yml
```

2. Locate the *netq-agent* section, or add it.

3. Set the parameters for the agent as follows:
  - port: 31980 (default) or one that you specify
  - server: IP address of the NetQ server or appliance where the agent should send its collected data
  - vrf: default (default) or one that you specify

Your configuration should be similar to this:

```
netq-agent:
  port: 31980
  server: 127.0.0.1
  vrf: default
```

### Configure NetQ Agents Using the NetQ CLI

If the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Server or Appliance. If it is not configured, refer to [Configure the NetQ CLI](#configure-the -netq-cli-on-a-rhel-or-centos-server) and then return here.

{{%notice info%}}
If you intend to use VRF, refer to [Configure the Agent to Use VRF](#configure-the-netq-agent-to-use-a-vrf). If you intend to specify a port for communication, refer to [Configure the Agent to Communicate over a Specific Port](#configure-the-netq-agent-to-communicate-over-a-specific-port).
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

## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRF, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the NetQ Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ Agents to communicate with the NetQ Platform only via a [VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a [management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if the management VRF is configured and you want the agent to communicate with the NetQ Platform over it, configure the agent like this:

```
cumulus@leaf01:~$ sudo netq config add agent server 192.168.1.254 vrf mgmt
cumulus@leaf01:~$ sudo netq config restart agent
```

### Configure the NetQ Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ Platform and NetQ Agents. If you want the NetQ Agent to communicate with the NetQ Platform via a different port, you need to specify the port number when configuring the NetQ Agent like this:

```
cumulus@leaf01:~$ sudo netq config add agent server 192.168.1.254 port 7379
cumulus@leaf01:~$ sudo netq config restart agent
```
