---
title: Install and Configure the NetQ Agent and CLI on Ubuntu Servers
author: Cumulus Networks
weight: 420
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
After installing your Cumulus NetQ software, you should install the  NetQ 2.4.0 Agents on each switch you want to monitor. NetQ 2.4 Agents can be installed on servers running:

- Ubuntu 16.04
- Ubuntu 18.04 (NetQ 2.2.2 and later)

This topic describes how to install and configure the NetQ Agent and CLI on switches running Ubuntu OS.

## Prepare for NetQ Agent Installation on an Ubuntu Server

For servers running Ubuntu OS, you need to:

- Verify the minimum service packages versions are installed
- Verify the server is running lldpd
- Install and configure NTP, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy](/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/) so `apt-get` can access the agent package on the Cumulus Networks repository.
{{%/notice%}}

### Verify Service Package Versions

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all
  - iproute2 4.3.0-1ubuntu3 amd64
  - lldpd 0.7.19-1 amd64
  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64

### Verify the Server is Running lldpd

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default, which is required for the installation.

To install this package, run the following commands:

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install lldpd
root@ubuntu:~# sudo systemctl enable lldpd.service
root@ubuntu:~# sudo systemctl start lldpd.service
```

### Install and Configure NTP

If NTP is not already installed an configured, follow these steps:

1.  Install [NTP](/cumulus-linux/System-Configuration/Setting-Date-and-Time/) on the server, if not already installed. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

```
root@ubuntu:~# sudo apt-get install ntp
```

2.  Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.

    2.  Under the *Server* section, specify the NTP server IP address or hostname.

3.  Enable and start the NTP service.

```
root@ubuntu:~# sudo systemctl enable ntp
root@ubuntu:~# sudo systemctl start ntp
```

    {{%notice tip%}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (`ntp@<vrf-name>` versus just `ntp`) in the above commands.
    {{%/notice%}}

4.  Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock is synchronized.

```
root@ubuntu:~# ntpq -pn
remote           refid            st t when poll reach   delay   offset  jitter
==============================================================================
+173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
+12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
\*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243
```

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each switch or host. This is available from the Cumulus Networks repository.

To obtain the NetQ Agent package:

1.  Reference and update the local `apt` repository.

 ```
 root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
 ```

2. Add the Ubuntu repository:

    <details><summary>Ubuntu 16.04</summary>
    Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    </details>
    <details><summary>Ubuntu 18.04</summary>
    Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
    </details>

    {{%notice note%}}
The use of `netq-latest` in these examples means that a `get` to the repository always retrieves the latest version of NetQ, even in the case where a major version update has been made. If you want to keep the repository on a specific version - such as `netq-2.3` - use that instead.
    {{%/notice%}}

## Install NetQ Agent on an Ubuntu Server

After completing the preparation steps, you can successfully install the agent software onto your server.

To install the NetQ Agent:

1.  Install the software packages on the server.

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install netq-agent
```

2. Verify you have the correct version of the Agent.

```
root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

    You should see version 2.4.0 and update 25 in the results. For example:

    - netq-agent_**2.4.0**-ub18.04u**25**~1579642196.aeb67d8_amd64.deb
    - netq-agent_**2.4.0**-ub16.04u**25**~1579714730.aeb67d8_amd64.deb, or

3. Restart `rsyslog` so log files are sent to the correct destination.

```
root@ubuntu:~# sudo systemctl restart rsyslog.service
```

4.  Continue with [NetQ Agent Configuration](#configure-your-netq-agents), or if you want to use the NetQ CLI to configure the agent, go to the next section.

## Install NetQ CLI on an Ubuntu Server

A simple process installs the NetQ CLI on an Ubuntu server.

1.  Reference and update the local `apt` repository and key.

 ```
 root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
 ```

2. Add the Ubuntu repository:

    <details><summary>Ubuntu 16.04</summary>
    Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    </details>
    <details><summary>Ubuntu 18.04</summary>
    Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add the following line:

        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
        ...
    </details>

    {{%notice note%}}
The use of `netq-latest` in this example means that a `get` to the repository always retrieves the latest version of NetQ, even in the case where a major version update has been made. If you want to keep the repository on a specific version - such as `netq-2.3` - use that instead.
    {{%/notice%}}

3.  Install the CLI software on the server.

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install netq-apps
```

4. Verify you have the correct version of the CLI.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-apps
```

    You should see version 2.4.0 and update 25 in the results. For example:

    - netq-apps_**2.4.0**-ub18.04u**25**~1579642196.aeb67d8_amd64.deb, or
    - netq-apps_**2.4.0**-ub16.04u**25**~1579714730.aeb67d8_amd64.deb5. 

5. Continue with the next section.

## Configure the NetQ CLI on an Ubuntu Server

Two methods are available for configuring the NetQ CLI on a switch:

- Run NetQ CLI commands on the switch; refer to the next section
- Edit the configuration file on the switch; refer to [Configure CLI Using File](#configure-netq-cli-using-configuration-file)

### Configure NetQ CLI Using the CLI

The steps to configure the CLI are different depending on whether the NetQ software has been installed for an on-premises or cloud deployment. Follow the instruction for your deployment type.

<details><summary>Configuring the CLI for On-premises Deployments</summary>

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

This example uses an IP address of 192.168.1.0 and the default port and VRF.

```
root@ubuntu:~# sudo netq config add cli server 192.168.1.0
root@ubuntu:~# sudo netq config restart cli
```

{{%notice tip%}}
If you have a server cluster deployed, use the IP address of the master server.
{{%/notice%}}

</details>
<details><summary> Configuring the CLI for Cloud Deployments</summary>

Use the following command to configure the CLI:

```
netq config add cli server <text-gateway-dest> [access-key <text-access-key> secret-key <text-secret-key> premises <text-premises-name> | cli-keys-file <text-key-file> premises <text-premises-name>] [vrf <text-vrf-name>] [port <text-gateway-port>]
```

Restart the CLI afterward to activate the configuration.

Refer to [Generate Access Keys](../../Install-NetQ/Prepare-NetQ-Cloud/#generate-access-keys) if you have not already created your access keys.

This example uses the individual access key, a premises of *datacenterwest*,  and the default Cloud address, port and VRF.  **Be sure to replace the key values with your generated keys if you are using this example on your server.**

```
root@ubuntu:~# sudo netq config add cli server api.netq.cumulusnetworks.com access-key 123452d9bc2850a1726f55534279dd3c8b3ec55e8b25144d4739dfddabe8149e secret-key /vAGywae2E4xVZg8F+HtS6h6yHliZbBP6HXU3J98765= premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

root@ubuntu:~# sudo netq config restart cli
Restarting NetQ CLI... Success!
```

This example uses an optional keys file. Refer to [Generate Access Keys](../../Install-NetQ/Prepare-NetQ-Cloud/#generate-access-keys) for information about creating this file. **Be sure to replace the keys filename and path with the *full path* and name of your keys file, and the *datacenterwest* premises name with your premises name if you are using this example on your server.**

```
root@ubuntu:~# sudo netq config add cli server api.netq.cumulusnetworks.com cli-keys-file /home/netq/nq-cld-creds.yml premises datacenterwest
Successfully logged into NetQ cloud at api.netq.cumulusnetworks.com:443
Updated cli server api.netq.cumulusnetworks.com vrf default port 443. Please restart netqd (netq config restart cli)

root@ubuntu:~# sudo netq config restart cli
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
root@ubuntu:~# sudo nano /etc/netq/netq.yml
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

## Configure the NetQ Agent on an Ubuntu Server

After the NetQ Agents have been installed on the servers you want to monitor, the NetQ Agents must be configured to obtain useful and relevant data. Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the device, or
- Use the NetQ CLI.

### Configure the NetQ Agents Using a Configuration File

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

```
root@ubuntu:~# sudo nano /etc/netq/netq.yml
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

If the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Server or Appliance. If it is not configured, refer to [Configure the NetQ CLI](#configure-the -netq-cli-on-an-ubuntu-server) and then return here.

{{%notice info%}}
If you intend to use VRF, skip to [Configure the Agent to Use VRF] (#configure-the-netq-agent-to-use-a-vrf). If you intend to specify a port for communication, skip to [Configure the Agent to Communicate over a Specific Port](#configure-the-netq-agent-to-communicate-over-a-specific-port).
{{%/notice%}}

Use the following command to configure the NetQ Agent:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
```

This example uses an IP address of *192.168.1.254* and the default port and VRF for the NetQ hardware.

```
root@ubuntu:~# sudo netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
root@ubuntu:~# sudo netq config restart agent
```

## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRF, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the NetQ Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/), including a
[management VRF](/cumulus-linux/Layer-3/Management-VRF/). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:

```
root@ubuntu:~# sudo netq config add agent server 192.168.1.254 vrf mgmt
root@ubuntu:~# sudo netq config restart agent
```

### Configure the NetQ Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

```
root@ubuntu:~# sudo netq config add agent server 192.168.1.254 port 7379
root@ubuntu:~# sudo netq config restart agent
```
