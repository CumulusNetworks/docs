---
title: Install NetQ Agents
author: NVIDIA
weight: 220
toc: 4
---

After installing the NetQ software, you should install the NetQ Agents on each switch you want to monitor. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 5.15, 5.14, 5.11.3, 5.9.4
- Ubuntu 24.04, 22.04

## Prepare for NetQ Agent Installation

For switches running *Cumulus Linux*, you need to:

- Install and configure NTP or PTP, if needed
- Obtain NetQ software packages

For servers running *Ubuntu*, you need to:

- Verify you installed the minimum package versions
- Verify the server is running `lldpd`
- Install and configure NTP or PTP, if needed
- Obtain NetQ software packages

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NVIDIA networking repository.
{{</notice>}}

{{<tabs "Prepare Agent Install">}}
{{<tab "Cumulus Linux 5.9.0 or later">}}

<!-- vale off -->
### Verify NTP Is Installed and Configured
<!-- vale on -->

Verify that {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} is running on the switch as outlined in the steps below. The switch system clock must be synchronized with NetQ to enable useful statistical analysis. Alternatively, you can configure {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Precision Time Protocol-PTP.md" text="PTP">}} for time synchronization.

```
nvidia@switch:~$ sudo systemctl status ntp
[sudo] password for nvidia:
● ntp.service - LSB: Start NTP daemon
        Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
        Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
          Docs: man:systemd-sysv-generator(8)
        CGroup: /system.slice/ntp.service
                └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114
```

If NTP is not installed, install and configure it before continuing.  

If NTP is not running:

- Verify the IP address or hostname of the NTP server in the `/etc/ntp.conf` file, and then
- Reenable and start the NTP service using the `systemctl [enable|start] ntp` commands

   {{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
   {{</notice>}}
### Obtain NetQ Agent Software Package

Cumulus Linux 4.4 and later includes the `netq-agent` package by default. To upgrade the NetQ Agent to the latest version: 

1. Add the repository by uncommenting or adding the following line in `/etc/apt/sources.list`:

```
nvidia@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-d12 netq-latest
...
```

{{<notice tip>}}
You can specify a NetQ Agent version in the repository configuration. The following example shows the repository configuration to retrieve NetQ Agent 4.15: <pre>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-d12 netq-4.15</pre>
{{</notice>}}

2. Add the `apps3.cumulusnetworks.com` authentication key to Cumulus Linux:

```
nvidia@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -
```

{{</tab>}}

{{<tab "Ubuntu 24.04">}}

### Verify Service Package Versions

Before you install the NetQ Agent on an Ubuntu server, make sure you install and run at least the minimum versions of the following packages:

<!-- vale off -->
- iproute 1:4.3.0-1ubuntu3.16.04.1 all
- iproute2 4.3.0-1ubuntu3 amd64
- lldpd 0.7.19-1 amd64
- ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64
<!-- vale on -->

### Verify the Server is Running lldpd

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default; however, the installation requires it.

To install this package, run the following commands:

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install lldpd
root@ubuntu:~# sudo systemctl enable lldpd.service
root@ubuntu:~# sudo systemctl start lldpd.service
```

### Install and Configure Network Time Server

If NTP is not already installed and configured, follow the steps below. Alternatively, you can configure {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Precision Time Protocol-PTP.md" text="PTP">}} for time synchronization.

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server, if not already installed. Servers must be synchronized with NetQ to enable useful statistical analysis.

    ```
    root@ubuntu:~# sudo apt-get install ntp
    ```

2. Configure the network time server.

{{<tabs "TabID124" >}}

{{<tab "Use NTP Configuration File" >}}

   1. Open the `/etc/ntp.conf` file in your text editor of choice.

   2. Under the *Server* section, specify the NTP server IP address or hostname.

   3. Enable and start the NTP service.

          root@ubuntu:~# sudo systemctl enable ntp
          root@ubuntu:~# sudo systemctl start ntp

   {{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
   {{</notice>}}

   4. Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock synchronized with NTP.

          root@ubuntu:~# ntpq -pn
          remote           refid            st t when poll reach   delay   offset  jitter
          ==============================================================================
          +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
          +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
          2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
          \*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

{{</tab>}}

{{</tabs>}}

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each server. This is available from the NVIDIA networking repository.

To obtain the NetQ Agent package:

1. Reference and update the local `apt` repository.

```
root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
```

2. Add the Ubuntu repository:


Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-noble.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-noble.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb noble netq-latest
...
```
    {{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even for a major version update. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.9</code> &mdash; use that instead.
    {{</notice>}}

{{</tab>}}

{{<tab "Ubuntu 22.04">}}

### Verify Service Package Versions

Before you install the NetQ Agent on an Ubuntu server, make sure you install and run at least the minimum versions of the following packages:

<!-- vale off -->
- iproute 1:4.3.0-1ubuntu3.16.04.1 all
- iproute2 4.3.0-1ubuntu3 amd64
- lldpd 0.7.19-1 amd64
- ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64
<!-- vale on -->

### Verify the Server is Running lldpd

Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not include `lldpd` by default; however, the installation requires it.

To install this package, run the following commands:

```
root@ubuntu:~# sudo apt-get update
root@ubuntu:~# sudo apt-get install lldpd
root@ubuntu:~# sudo systemctl enable lldpd.service
root@ubuntu:~# sudo systemctl start lldpd.service
```

### Install and Configure Network Time Server

If NTP is not already installed and configured, follow the steps below. Alternatively, you can configure {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Precision Time Protocol-PTP.md" text="PTP">}} for time synchronization.

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server, if not already installed. Servers must be synchronized with NetQ to enable useful statistical analysis.

    ```
    root@ubuntu:~# sudo apt-get install ntp
    ```

2. Configure the network time server.

{{<tabs "TabID0" >}}

{{<tab "Use NTP Configuration File" >}}

   1. Open the `/etc/ntp.conf` file in your text editor of choice.

   2. Under the *Server* section, specify the NTP server IP address or hostname.

   3. Enable and start the NTP service.

          root@ubuntu:~# sudo systemctl enable ntp
          root@ubuntu:~# sudo systemctl start ntp

   {{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
   {{</notice>}}

   4. Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock synchronized with NTP.

          root@ubuntu:~# ntpq -pn
          remote           refid            st t when poll reach   delay   offset  jitter
          ==============================================================================
          +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
          +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
          2a00:7600::41    .STEP.          16 u    - 1024    0    0.000    0.000   0.000
          \*129.250.35.250 249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

   {{</tab>}}

{{</tabs>}}

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each server. This is available from the NVIDIA networking repository.

To obtain the NetQ Agent package:

1. Reference and update the local `apt` repository.

```
root@ubuntu:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -
```

2. Add the Ubuntu repository:


Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-jammy.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-jammy.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb jammy netq-latest
...
```
    {{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even for a major version update. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.9</code> &mdash; use that instead.
    {{</notice>}}

{{</tab>}}

{{</tabs>}}


## Install NetQ Agent

After completing the preparation steps, install the agent on your switch or host.

{{<tabs "Install NetQ Agent">}}

{{<tab "Cumulus Linux">}}

Cumulus Linux 4.4 and later includes the `netq-agent` package by default. To install the NetQ Agent on earlier versions of Cumulus Linux:

1. Update the local `apt` repository, then install the NetQ software on the switch.

    ```
    nvidia@switch:~$ sudo apt-get update
    nvidia@switch:~$ sudo apt-get install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    nvidia@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    {{<netq-install/agent-version version="4.15.0" opsys="cl">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

    ```
    nvidia@switch:~$ sudo systemctl restart rsyslog.service
    ```

4. Configure the NetQ Agent, as described in the next section.

{{</tab>}}

{{<tab "Ubuntu">}}

To install the NetQ Agent:

1. Install the software packages on the server.

    ```
    root@ubuntu:~# sudo apt-get update
    root@ubuntu:~# sudo apt-get install netq-agent
    ```

2. Verify that you have the correct agent version.

    ```
    root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    {{<netq-install/agent-version version="4.15.0" opsys="ub">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

```
root@ubuntu:~# sudo systemctl restart rsyslog.service
```

4. Configure the NetQ Agent, as described in the next section.

{{</tab>}}

{{</tabs>}}

## Configure NetQ Agents

After you install the NetQ Agents on the switches you want to monitor, you must configure them to obtain useful and relevant data.

{{%notice note%}}
The NetQ Agent is aware of and communicates through the designated VRF. If you do not specify one, it uses the default VRF (named *default*). If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.<br><br> If you configure the NetQ Agent to communicate in a VRF that is not *default* or *mgmt*, add the following line to `/etc/netq/netq.yml` in the `netq-agent` section:

```
netq-agent:
  netq_stream_address: 0.0.0.0
```
{{%/notice%}}

Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the switch, or
- Use the NetQ CLI

{{<tabs "TabID298" >}}


{{<tab "Standalone Deployments" >}}

{{<tabs "TabID318" >}}

{{<tab "NetQ CLI" >}}

If you {{<link title="Install NetQ CLI" text="configured the NetQ CLI">}}, you can use it to configure the NetQ Agent to send telemetry data to the NetQ VM.

{{<notice info>}}
If you intend to use a VRF for agent communication (recommended), refer to {{<link url="#configure-the-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, refer to {{<link url="#configure-the-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.
{{</notice>}}

Use the following command to configure the NetQ Agent:

```
sudo netq config add agent server <text-opta-ip> 
    [port <text-opta-port>] 
    [ssl true | ssl false] 
    [ssl-cert <text-ssl-cert-file> | ssl-cert download] 
    [vrf <text-vrf-name>] 
    [inband-interface <interface-name>]
```

This example uses a NetQ server IP address of *192.168.1.254*, the default port, and the `mgmt` VRF for a switch managed through an out-of-band connection:

```
sudo netq config add agent server 192.168.1.254 vrf mgmt
Updated agent server 192.168.1.254 vrf mgmt. Please restart netq-agent (netq config restart agent).
sudo netq config restart agent
```

This example uses a NetQ server IP address of *192.168.1.254*, the default port, and the `default` VRF for a switch managed through an in-band connection on interface `swp1`:

```
sudo netq config add agent server 192.168.1.254 vrf default inband-interface swp1
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
sudo netq config restart agent
```

{{</tab>}}

{{<tab "Configuration Files" >}}

You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-agent* section, or add it.

3. Set the parameters for the agent as follows:
    - port: 31980 (default configuration)
    - server: IP address of the NetQ server where the agent should send its collected data
    - vrf: default (or one that you specify)
    - inband-interface: the interface used to reach your NetQ server and used by lifecycle management to connect to the switch (for deployments where switches are managed through an in-band interface)

    Your configuration should be similar to this:

    ```
    netq-agent:
        port: 31980
        server: 192.168.1.254
        vrf: mgmt
    ```

    For in-band deployments, using the `default` VRF:
    ```
    netq-agent:
        inband-interface: swp1
        port: 31980
        server: 192.168.1.254
        vrf: default
    ```


{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "Cluster Deployments" >}}

{{<tabs "TabID302" >}}

{{<tab "NetQ CLI" >}}

If you have a high-availability server cluster arrangement, you should configure the NetQ Agent to distribute data across all servers in the cluster. For {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster" text="scale cluster deployments">}}, configure the agent with the IP address of the `master-ip` and each `ha-node`. For 5-node deployments, you do not need to specify the `worker-nodes`.

To configure the agent to send data to the servers in your cluster, run:

```
sudo netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
```

You must separate the list of IP addresses by commas (not spaces). You can optionally specify a port or VRF.

This example configures the NetQ Agent on a switch to send the data to three servers located at *10.0.0.21*, *10.0.0.22*, and *10.0.0.23* using the *mgmt* VRF.

```
nvidia@switch:~$ sudo netq config add agent cluster-servers 10.0.0.21,10.0.0.22,10.0.0.23 vrf mgmt
```

To stop a NetQ Agent from sending data to a server cluster, run:

```
nvidia@switch:~$ sudo netq config del agent cluster-servers
```


{{</tab>}}

{{<tab "Configuration Files" >}}


You can configure the NetQ Agent in the `netq.yml` configuration file contained in the `/etc/netq/` directory.

1. Open the `netq.yml` file using your text editor of choice. For example:

    ```
    sudo nano /etc/netq/netq.yml
    ```

2. Locate the *netq-agent* section, or add it.

3. Set the parameters for the agent as follows:
    - port: 31980 (default configuration)
    - cluster-servers: IP addresses of all NetQ servers in your cluster. For {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster" text="scale cluster deployments">}}, configure the agent with the IP address of the `master-ip` and each `ha-node`. For 5-node deployments, you do not need to specify the `worker-nodes`.
    - vrf: default (or one that you specify)
    - inband-interface: the interface used to reach your NetQ server and used by lifecycle management to connect to the switch (for deployments where switches are managed through an in-band interface)

    Your configuration should be similar to this:

    ```
    netq-agent:
        cluster-servers: 10.0.0.21,10.0.0.22,10.0.0.23
        port: 31980
        vrf: mgmt
    ```

    For in-band deployments, using the `default` VRF:
    ```
    netq-agent:
        inband-interface: swp1
        cluster-servers: 10.0.0.21,10.0.0.22,10.0.0.23
        port: 31980
        vrf: mgmt
    ```

{{</tab>}}

{{</tabs>}}

{{</tab>}}
   
{{</tabs>}}


## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRFs, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the Agent to Use a VRF

<!-- vale off -->
By default, NetQ uses the *default* VRF for communication between the NetQ VM and NetQ Agents. While optional, NVIDIA strongly recommends that you configure NetQ Agents to communicate with the NetQ VM only via a {{<kb_link latest="cl" url="Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF.md" text="VRF">}}, including a {{<kb_link latest="cl" url="Layer-3/VRFs/Management-VRF.md" text="management VRF">}}. To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if you configured the management VRF and you want the agent to communicate over the management VRF with the NetQ VM, configure the agent like this:
<!-- vale on -->

```
sudo netq config add agent server 192.168.1.254 vrf mgmt
sudo netq config restart agent
```

{{%notice info%}}
If you reconfigure the VRF used for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.
{{%/notice%}}

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ server and NetQ Agents for on-premises deployments and port 443 for cloud deployments. If you want the NetQ Agent to communicate with the NetQ sever via a different port, you need to specify the port number when configuring the NetQ Agent, like this:

```
sudo netq config add agent server 192.168.1.254 port 7379
sudo netq config restart agent
```
## Related Information
- {{<link title="Manage NetQ Agents">}}
