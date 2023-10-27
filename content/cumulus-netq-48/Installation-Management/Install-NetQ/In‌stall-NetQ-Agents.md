---
title: Install NetQ Agents
author: NVIDIA
weight: 280
toc: 4
---

After installing the NetQ software, you should install the NetQ Agents on each switch you want to monitor. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 4.3.0 and 4.3.1 (Broadcom switches)
- Cumulus Linux 5.0.0 and above (Spectrum switches)
- SONiC 202012
- CentOS 7
- RHEL 7.1
- Ubuntu 20.04

## Prepare for NetQ Agent Installation

For switches running Cumulus Linux and SONiC, you need to:

- Install and configure NTP or PTP, if needed
- Obtain NetQ software packages

For servers running RHEL, CentOS, or Ubuntu, you need to:

- Verify you installed the minimum package versions
- Verify the server is running `lldpd`
- Install and configure NTP or PTP, if needed
- Obtain NetQ software packages

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NVIDIA networking repository.
{{</notice>}}

{{<tabs "Prepare Agent Install">}}

{{<tab "Cumulus Linux">}}

<!-- vale off -->
### Verify NTP Is Installed and Configured
<!-- vale on -->

Verify that {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} is running on the switch as outlined in the steps below. The switch system clock must be synchronized with the NetQ appliance to enable useful statistical analysis. Alternatively, you can configure {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Precision Time Protocol-PTP.md" text="PTP">}} for time synchronization.

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

- Verify the IP address or hostname of the NTP server in the `/etc/ntp.conf` file, and then
- Reenable and start the NTP service using the `systemctl [enable|start] ntp` commands

   {{<notice tip>}}
If you are running NTP in your out-of-band management network with VRF, specify the VRF (<code>ntp@&lt;vrf-name&gt;</code> versus just <code>ntp</code>) in the above commands.
   {{</notice>}}
### Obtain NetQ Agent Software Package

Cumulus Linux 4.4 and later includes the `netq-agent` package by default. To upgrade the NetQ Agent to the latest version: 

1. Add the repository by uncommenting or adding the following line in `/etc/apt/sources.list`:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest
...
```

{{<notice tip>}}
You can specify a NetQ Agent version in the repository configuration. The following example shows the repository configuration to retrieve NetQ Agent 4.3: <pre>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-4.3</pre>
{{</notice>}}

2. Add the `apps3.cumulusnetworks.com` authentication key to Cumulus Linux:

```
cumulus@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -
```

{{</tab>}}

{{<tab "SONiC">}}

<!-- vale off -->
### Verify NTP Is Installed and Configured
<!-- vale on -->

Verify that {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} is running on the switch as outlined in the steps below. The switch must be synchronized with the NetQ appliance to enable useful statistical analysis. Alternatively, you can configure {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Precision Time Protocol-PTP.md" text="PTP">}} for time synchronization.

```
admin@switch:~$ sudo systemctl status ntp
● ntp.service - Network Time Service
     Loaded: loaded (/lib/systemd/system/ntp.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2021-06-08 14:56:16 UTC; 2min 18s ago
       Docs: man:ntpd(8)
    Process: 1444909 ExecStart=/usr/lib/ntp/ntp-systemd-wrapper (code=exited, status=0/SUCCESS)
   Main PID: 1444921 (ntpd)
      Tasks: 2 (limit: 9485)
     Memory: 1.9M
     CGroup: /system.slice/ntp.service
             └─1444921 /usr/sbin/ntpd -p /var/run/ntpd.pid -x -u 106:112
```

If NTP is not installed, install and configure it before continuing.  

If NTP is not running:

- Verify the IP address or hostname of the NTP server in the `/etc/sonic/config_db.json` file, and then
- Reenable and start the NTP service using the `sudo config reload -n` command

Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock synchronized with NTP.

```
admin@switch:~$ show ntp
MGMT_VRF_CONFIG is not present.
synchronised to NTP server (104.194.8.227) at stratum 3
   time correct to within 2014 ms
   polling server every 64 s
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
-144.172.118.20  139.78.97.128    2 u   26   64  377   47.023  -1798.1 120.803
+208.67.75.242   128.227.205.3    2 u   32   64  377   72.050  -1939.3  97.869
+216.229.4.66    69.89.207.99     2 u  160   64  374   41.223  -1965.9  83.585
*104.194.8.227   164.67.62.212    2 u   33   64  377    9.180  -1934.4  97.376
```

### Obtain NetQ Agent Software Package

To install the NetQ Agent you need to install `netq-agent` on each switch or host. This is available from the NVIDIA networking repository.

*Note that NetQ has a separate repository from SONiC.*

To obtain the NetQ Agent package:

1. Install the `wget` utility so that you can install the GPG keys in step 3.

       admin@switch:~$ sudo apt-get update
       admin@switch:~$ sudo apt-get install wget -y
1. Edit the `/etc/apt/sources.list` file to add the SONiC repository:

       admin@switch:~$ sudo vi /etc/apt/sources.list
       ...
       deb https://apps3.cumulusnetworks.com/repos/deb buster netq-latest
       ...
1. Add the SONiC repo key:

       admin@switch:~$ sudo wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -

{{</tab>}}

{{<tab "RHEL 7 or CentOS">}}

### Verify Service Package Versions

Before you install the NetQ Agent on a Red Hat or CentOS server, make sure you install and run at least the minimum versions of the following packages:

- iproute-3.10.0-54.el7\_2.1.x86\_64
- lldpd-0.9.7-5.el7.x86\_64
- ntp-4.2.6p5-25.el7.centos.2.x86\_64
- ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

### Verify the Server is Running lldpd and wget

Make sure you are running lldp**d**, not lldp**ad**. CentOS does not include `lldpd` by default, nor does it include `wget`; however, the installation requires it.

To install this package, run the following commands:

```
root@rhel7:~# sudo yum -y install epel-release
root@rhel7:~# sudo yum -y install lldpd
root@rhel7:~# sudo systemctl enable lldpd.service
root@rhel7:~# sudo systemctl start lldpd.service
root@rhel7:~# sudo yum install wget
```

### Install and Configure NTP

If NTP is not already installed and configured, follow the steps outlined below. Alternatively, you can configure {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Precision Time Protocol-PTP.md" text="PTP">}} for time synchronization.

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server. Servers must be synchronized with the NetQ appliance to enable useful statistical analysis.

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

4.  Verify NTP is operating correctly. Look for an asterisk (\*) or a plus sign (+) that indicates the clock synchronized with NTP.

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

To install the NetQ Agent you need to install `netq-agent` on each switch or host. This is available from the NVIDIA networking repository.

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
    [cumulus-arch-netq-4.0]
    name=Cumulus netq packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-4.0/$basearch
    gpgcheck=1
    enabled=1
    [cumulus-noarch-netq-4.0]
    name=Cumulus netq architecture-independent packages
    baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-4.0/noarch
    gpgcheck=1
    enabled=1
    ...
    ```

{{</tab>}}

{{<tab "Ubuntu">}}

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

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server, if not already installed. Servers must be synchronized with the NetQ appliance to enable useful statistical analysis.

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

   {{<tab "Use Chrony (Ubuntu 18.04 only)" >}}

   1. Install chrony if needed.
```
root@ubuntu:~# sudo apt install chrony
```
   2. Start the chrony service.
```
root@ubuntu:~# sudo /usr/local/sbin/chronyd
```
   3. Verify it installed successfully.
```
root@ubuntu:~# chronyc activity
200 OK
8 sources online
0 sources offline
0 sources doing burst (return to online)
0 sources doing burst (return to offline)
0 sources with unknown address
```
   4. View the time servers which chrony is using.
```
root@ubuntu:~# chronyc sources
210 Number of sources = 8
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^+ golem.canonical.com           2   6   377    39  -1135us[-1135us] +/-   98ms
^* clock.xmission.com            2   6   377    41  -4641ns[ +144us] +/-   41ms
^+ ntp.ubuntu.net              2   7   377   106   -746us[ -573us] +/-   41ms
...
```
Open the *chrony.conf* configuration file (by default at */etc/chrony/*) and edit if needed.

Example with individual servers specified:
```
server golem.canonical.com iburst
server clock.xmission.com iburst
server ntp.ubuntu.com iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
```
Example when using a pool of servers:
```
pool pool.ntp.org iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
```
   5. View the server  chrony is currently tracking.
```
root@ubuntu:~# chronyc tracking
Reference ID    : 5BBD59C7 (golem.canonical.com)
Stratum         : 3
Ref time (UTC)  : Mon Feb 10 14:35:18 2020
System time     : 0.0000046340 seconds slow of NTP time
Last offset     : -0.000123459 seconds
RMS offset      : 0.007654410 seconds
Frequency       : 8.342 ppm slow
Residual freq   : -0.000 ppm
Skew            : 26.846 ppm
Root delay      : 0.031207654 seconds
Root dispersion : 0.001234590 seconds
Update interval : 115.2 seconds
Leap status     : Normal
```
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

    {{<tabs "Get NetQ Agent Package" >}}

{{<tab "Ubuntu 18.04" >}}

Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-bionic.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-bionic.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb bionic netq-latest
...
```

{{</tab>}}
        
{{<tab "Ubuntu 20.04" >}}

Create the file `/etc/apt/sources.list.d/cumulus-host-ubuntu-focal.list` and add the following line:

```
root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-focal.list
...
deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb focal netq-latest
...
```

{{</tab>}}

{{</tabs>}}

    {{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even for a major version update. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.4</code> &mdash; use that instead.
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
    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    {{<netq-install/agent-version version="4.7.0" opsys="cl">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

    ```
    cumulus@switch:~$ sudo systemctl restart rsyslog.service
    ```

4. Configure the NetQ Agent, as described in the next section.

{{</tab>}}

{{<tab "SONiC">}}

To install the NetQ Agent (the following example uses Cumulus Linux but the steps are the same for SONiC):

1. Update the local `apt` repository, then install the NetQ software on the switch.

    ```
    admin@switch:~$ sudo apt-get update
    admin@switch:~$ sudo apt-get install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    admin@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

3. Restart `rsyslog` so it sends log files to the correct destination.

    ```
    admin@switch:~$ sudo systemctl restart rsyslog.service
    ```

4. Configure the NetQ Agent, as described in the next section.

{{</tab>}}

{{<tab "RHEL7 or CentOS">}}

To install the NetQ Agent:

1. Install the Bash completion and NetQ packages on the server.

    ```
    root@rhel7:~# sudo yum -y install bash-completion
    root@rhel7:~# sudo yum install netq-agent
    ```

2. Verify you have the correct version of the Agent.

    ```
    root@rhel7:~# rpm -qa | grep -i netq
    ```

    {{<netq-install/agent-version version="4.7.0" opsys="rh">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

    ```
    root@rhel7:~# sudo systemctl restart rsyslog
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

2. Verify you have the correct version of the Agent.

    ```
    root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
    ```

    {{<netq-install/agent-version version="4.7.0" opsys="ub">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

```
root@ubuntu:~# sudo systemctl restart rsyslog.service
```

4. Configure the NetQ Agent, as described in the next section.

{{</tab>}}

{{</tabs>}}

## Configure NetQ Agent

After you install the NetQ Agents on the switches you want to monitor, you must configure them to obtain useful and relevant data.

{{%notice note%}}
The NetQ Agent is aware of and communicates through the designated VRF. If you do not specify one, it uses the default VRF (named *default*). If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.

If you configure the NetQ Agent to communicate in a VRF that is not *default* or *mgmt*, the following line must be added to `/etc/netq/netq.yml` in the `netq-agent` section:

```
netq-agent:
  netq_stream_address: 0.0.0.0
```
{{%/notice%}}

Two methods are available for configuring a NetQ Agent:

- Edit the configuration file on the switch, or
- Use the NetQ CLI

### Configure NetQ Agents Using a Configuration File

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

    For in-band deployments:
    ```
    netq-agent:
        inband-interface: swp1
        port: 31980
        server: 192.168.1.254
        vrf: default
    ```


### Configure NetQ Agents Using the NetQ CLI

If you configured the NetQ CLI, you can use it to configure the NetQ Agent to send telemetry data to the NetQ appliance or VM. To configure the NetQ CLI, refer to {{<link title="Install NetQ CLI">}}.

{{<notice info>}}
If you intend to use a VRF for agent communication (recommended), refer to {{<link url="#configure-the-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, refer to {{<link url="#configure-the-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.
{{</notice>}}

Use the following command to configure the NetQ Agent:

```
sudo netq config add agent server <text-opta-ip> [port <text-opta-port>] [ssl true | ssl false] [ssl-cert <text-ssl-cert-file> | ssl-cert download] [vrf <text-vrf-name>] [inband-interface <interface-name>]
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


## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRFs, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the Agent to Use a VRF

<!-- vale off -->
By default, NetQ uses the *default* VRF for communication between the NetQ appliance or VM and NetQ Agents. While optional, NVIDIA strongly recommends that you configure NetQ Agents to communicate with the NetQ appliance or VM only via a {{<kb_link latest="cl" url="Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF.md" text="VRF">}}, including a {{<kb_link latest="cl" url="Layer-3/VRFs/Management-VRF.md" text="management VRF">}}. To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if you configured the management VRF and you want the agent to communicate with the NetQ appliance or VM over it, configure the agent like this:
<!-- vale on -->

```
sudo netq config add agent server 192.168.1.254 vrf mgmt
sudo netq config restart agent
```

{{%notice info%}}
If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.
{{%/notice%}}

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ server and NetQ Agents for on-premises deployments and port 443 for cloud deployments. If you want the NetQ Agent to communicate with the NetQ sever via a different port, you need to specify the port number when configuring the NetQ Agent, like this:

```
sudo netq config add agent server 192.168.1.254 port 7379
sudo netq config restart agent
```
## Related Information
- {{<link title="Manage NetQ Agents">}}