---
title: Install and Configure the NetQ Agent on RHEL and CentOS Servers
author: Cumulus Networks
weight: 310
toc: 5
---
After installing your Cumulus NetQ software, you should install the NetQ 3.2.1 Agents on each server you want to monitor. NetQ Agents can be installed on servers running:

- Red Hat RHEL 7.1
- CentOS 7

## Prepare for NetQ Agent Installation on a RHEL or CentOS Server

For servers running RHEL or CentOS, you need to:

- Verify the minimum package versions are installed
- Verify the server is running lldpd
- Install and configure NTP, if needed
- Obtain NetQ software packages

{{%notice note%}}
If your network uses a proxy server for external connections, you should first [configure a global proxy]({{<ref "/cumulus-linux-43/System-Configuration/Configuring-a-Global-Proxy" >}}) so `apt-get` can access the software package in the Cumulus Networks repository.
{{%/notice%}}

### Verify Service Package Versions

Before you install the NetQ Agent on a Red Hat or CentOS server, make sure the following packages are installed and running these minimum versions:

- iproute-3.10.0-54.el7\_2.1.x86\_64
- lldpd-0.9.7-5.el7.x86\_64
- ntp-4.2.6p5-25.el7.centos.2.x86\_64
- ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

### Verify the Server is Running lldpd and wget

Make sure you are running lldp**d**, not lldp**ad**. CentOS does not include `lldpd` by default, nor does it include `wget`, which is required for the installation.

To install this package, run the following commands:

```
root@rhel7:~# sudo yum -y install epel-release
root@rhel7:~# sudo yum -y install lldpd
root@rhel7:~# sudo systemctl enable lldpd.service
root@rhel7:~# sudo systemctl start lldpd.service
root@rhel7:~# sudo yum install wget
```

### Install and Configure NTP

If NTP is not already installed and configured, follow these steps:

1. Install [NTP]({{<ref "/cumulus-linux-43/System-Configuration/Setting-Date-and-Time" >}}) on the server. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

    ```
    root@rhel7:~# sudo yum install ntp
    ```

2. Configure the NTP server.

    1.  Open the `/etc/ntp.conf` file in your text editor of choice.

    2.  Under the *Server* section, specify the NTP server IP address or hostname.

3. Enable and start the NTP service.

    ```
    root@rhel7:~# sudo systemctl enable ntp
    root@rhel7:~# sudo systemctl start ntp
    ```

   {{%notice tip%}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (`ntp@<vrf-name>` versus just `ntp`) in the above commands.
   {{%/notice%}}

4.  Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock is synchronized.

    ```
    root@rhel7:~# ntpq -pn
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

1.  Reference and update the local `yum` repository.

    ```
    root@rhel7:~# sudo rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
    root@rhel7:~# sudo wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo
    ```

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1` flag for the two NetQ repositories.

    ```
    root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
    ...
    [cumulus-arch-netq-3.2]
    name=Cumulus netq packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-3.2/$basearch
    gpgcheck=1
    enabled=1
    [cumulus-noarch-netq-3.2]
    name=Cumulus netq architecture-independent packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-3.2/noarch
    gpgcheck=1
    enabled=1
    ...
    ```

## Install NetQ Agent on a RHEL or CentOS Server

After completing the preparation steps, you can successfully install the agent software onto your server.

To install the NetQ Agent:

1.  Install the Bash completion and NetQ packages on the server.

    ```
    root@rhel7:~# sudo yum -y install bash-completion
    root@rhel7:~# sudo yum install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    root@rhel7:~# rpm -qa | grep -i netq
    ```

    {{<netq-install/agent-version version="3.2.1" opsys="rh">}}

3. Restart `rsyslog` so log files are sent to the correct destination.

    ```
    root@rhel7:~# sudo systemctl restart rsyslog
    ```

4.  Continue with NetQ Agent Configuration in the next section.

## Configure the NetQ Agent on a RHEL or CentOS Server

After the NetQ Agent and CLI have been installed on the servers you want to monitor, the NetQ Agents must be configured to obtain useful and relevant data.

{{%notice note%}}
The NetQ Agent is aware of and communicates through the designated VRF. If you do not specify one, the default VRF (named *default*) is used. If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.
{{%/notice%}}

Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the device, or
- Use the NetQ CLI.

### Configure the NetQ Agents Using a Configuration File

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

If the CLI is configured, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Server or Appliance. If it is not configured, refer to {{<link title="Install and Configure the NetQ CLI on RHEL and CentOS Servers#configure-the-netq-cli-on-a-rhel-or-centos-server" text="Configure the NetQ CLI on a RHEL or CentOS Server">}} and then return here.

{{%notice info%}}
If you intend to use VRF, skip to {{<link url="#configure-the-netq-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, skip to {{<link url="#configure-the-netq-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.

{{%/notice%}}

Use the following command to configure the NetQ Agent:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
```

This example uses an IP address of *192.168.1.254* and the default port and VRF for the NetQ hardware.

```
root@rhel7:~# sudo netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
root@rhel7:~# sudo netq config restart agent
```

## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRF, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the NetQ Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ Agents to communicate with the NetQ Platform only via a [VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF" >}}), including a [management VRF]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Management-VRF" >}}). To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if the management VRF is configured and you want the agent to communicate with the NetQ Platform over it, configure the agent like this:

```
root@rhel7:~# sudo netq config add agent server 192.168.1.254 vrf mgmt
root@rhel7:~# sudo netq config restart agent
```

### Configure the NetQ Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ Platform and NetQ Agents. If you want the NetQ Agent to communicate with the NetQ Platform via a different port, you need to specify the port number when configuring the NetQ Agent like this:

```
root@rhel7:~# sudo netq config add agent server 192.168.1.254 port 7379
root@rhel7:~# sudo netq config restart agent
```
