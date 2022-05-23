---
title: Install NetQ Agents
author: NVIDIA
weight: 280
toc: 4
---

After installing your {{<link url="Install-NetQ" text="NetQ software">}}, you should install the NetQ {{<version>}} Agents on each switch you want to monitor. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.12 and later
- SONiC 202012 and later
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04

## Prepare for NetQ Agent Installation

For switches running Cumulus Linux and SONiC, you need to:

- Install and configure NTP, if needed
- Obtain NetQ software packages

For servers running RHEL, CentOS, or Ubuntu, you need to:

- Verify you installed the minimum package versions
- Verify the server is running `lldpd`
- Install and configure NTP, if needed
- Obtain NetQ software packages

{{<notice note>}}
If your network uses a proxy server for external connections, you should first {{<kb_link latest="cl" url="System-Configuration/Configuring-a-Global-Proxy.md" text="configure a global proxy">}} so <code>apt-get</code> can access the software package in the NVIDIA networking repository.
{{</notice>}}

{{<tabs "Prepare Agent Install">}}

{{<tab "Cumulus Linux">}}

<!-- vale off -->
### Verify NTP Is Installed and Configured
<!-- vale on -->

Verify that {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} is running on the switch. The switch must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

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

To install the NetQ Agent you need to install `netq-agent` on each switch or host. This is available from the NVIDIA networking repository.

To obtain the NetQ Agent package:

Edit the `/etc/apt/sources.list` file to add the repository for NetQ.

*Note that NetQ has a separate repository from Cumulus Linux.*

{{<tabs "Get Agent Package" >}}

{{<tab "Cumulus Linux 3.7" >}}

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-{{<version>}}
...
```

{{<notice tip>}}
You  can use the <code>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-latest</code> repository if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

{{</tab>}}

{{<tab "Cumulus Linux 4.0 and later">}}

Cumulus Linux 4.4 and later includes the `netq-agent` package by default.

To add the repository, uncomment or add the following line in `/etc/apt/sources.list`:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-{{<version>}}
...
```

{{<notice tip>}}
You can use the <code>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest</code> repository if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

Add the `apps3.cumulusnetworks.com` authentication key to Cumulus Linux:

```
cumulus@switch:~$ wget -qO - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -
```

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "SONiC">}}

<!-- vale off -->
### Verify NTP Is Installed and Configured
<!-- vale on -->

Verify that {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} is running on the switch. The switch must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

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

1. Install the `wget` utility so you can install the GPG keys in step 3.

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

Make sure you are running lldp**d**, not lldp**ad**. CentOS does not include `lldpd` by default, nor does it include `wget`; however,the installation requires it.

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

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

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

If NTP is not already installed and configured, follow these steps:

1. Install {{<kb_link latest="cl" url="System-Configuration/Date-and-Time/Network-Time-Protocol-NTP.md" text="NTP">}} on the server, if not already installed. Servers must be in time synchronization with the NetQ Platform or NetQ Appliance to enable useful statistical analysis.

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

          root@ubuntu:~# sudo apt install chrony

   2. Start the chrony service.

          root@ubuntu:~# sudo /usr/local/sbin/chronyd

   3. Verify it installed successfully.

          root@ubuntu:~# chronyc activity
          200 OK
          8 sources online
          0 sources offline
          0 sources doing burst (return to online)
          0 sources doing burst (return to offline)
          0 sources with unknown address

   4. View the time servers chrony is using.

          root@ubuntu:~# chronyc sources
          210 Number of sources = 8

          MS Name/IP address         Stratum Poll Reach LastRx Last sample
          ===============================================================================
          ^+ golem.canonical.com           2   6   377    39  -1135us[-1135us] +/-   98ms
          ^* clock.xmission.com            2   6   377    41  -4641ns[ +144us] +/-   41ms
          ^+ ntp.ubuntu.net              2   7   377   106   -746us[ -573us] +/-   41ms
          ...

      Open the *chrony.conf* configuration file (by default at */etc/chrony/*) and edit if needed.

      Example with individual servers specified:

          server golem.canonical.com iburst
          server clock.xmission.com iburst
          server ntp.ubuntu.com iburst
          driftfile /var/lib/chrony/drift
          makestep 1.0 3
          rtcsync

      Example when using a pool of servers:

          pool pool.ntp.org iburst
          driftfile /var/lib/chrony/drift
          makestep 1.0 3
          rtcsync

   5. View the server chrony is currently tracking.

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

{{</tabs>}}

    {{<notice note>}}
The use of <code>netq-latest</code> in these examples means that a <code>get</code> to the repository always retrieves the latest version of NetQ, even for a major version update. If you want to keep the repository on a specific version &mdash; such as <code>netq-4.2</code> &mdash; use that instead.
    {{</notice>}}

{{</tab>}}

{{</tabs>}}

## Install NetQ Agent

After completing the preparation steps, you can successfully install the agent onto your switch or host.

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

    {{<netq-install/agent-version version="4.2.0" opsys="cl">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

    ```
    cumulus@switch:~$ sudo systemctl restart rsyslog.service
    ```

4. Continue with NetQ Agent configuration in the next section.

{{</tab>}}

{{<tab "SONiC">}}

To install the NetQ Agent (this example uses Cumulus Linux but the steps are the same for SONiC):

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

4. Continue with NetQ Agent configuration in the next section.

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
    root@rhel7:~# rpm -q -netq-agent
    ```

    {{<netq-install/agent-version version="4.2.0" opsys="rh">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

    ```
    root@rhel7:~# sudo systemctl restart rsyslog
    ```

4. Continue with NetQ Agent Configuration in the next section.

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

    {{<netq-install/agent-version version="4.2.0" opsys="ub">}}

3. Restart `rsyslog` so it sends log files to the correct destination.

```
root@ubuntu:~# sudo systemctl restart rsyslog.service
```

4. Continue with NetQ Agent Configuration in the next section.

{{</tab>}}

{{</tabs>}}

## Configure NetQ Agent

After you install the NetQ Agents on the switches you want to monitor, you must configure them to obtain useful and relevant data.

{{%notice note%}}
The NetQ Agent is aware of and communicates through the designated VRF. If you do not specify one, it uses the default VRF (named *default*). If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.
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
    - server: IP address of the NetQ Appliance or VM where the agent should send its collected data
    - vrf: default (or one that you specify)

    Your configuration should be similar to this:

    ```
    netq-agent:
        port: 31980
        server: 127.0.0.1
        vrf: mgmt
    ```

### Configure NetQ Agents Using the NetQ CLI

If you configured the NetQ CLI, you can use it to configure the NetQ Agent to send telemetry data to the NetQ Appliance or VM. To configure the NetQ CLI, refer to {{<link title="Install NetQ CLI">}}.

{{<notice info>}}
If you intend to use a VRF for agent communication (recommended), refer to {{<link url="#configure-the-agent-to-use-a-vrf" text="Configure the Agent to Use VRF">}}. If you intend to specify a port for communication, refer to {{<link url="#configure-the-agent-to-communicate-over-a-specific-port" text="Configure the Agent to Communicate over a Specific Port">}}.
{{</notice>}}

Use the following command to configure the NetQ Agent:

```
netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
```

This example uses an IP address of *192.168.1.254* and the default port and VRF for the NetQ Appliance or VM.

```
sudo netq config add agent server 192.168.1.254
Updated agent server 192.168.1.254 vrf default. Please restart netq-agent (netq config restart agent).
sudo netq config restart agent
```

## Configure Advanced NetQ Agent Settings

A couple of additional options are available for configuring the NetQ Agent. If you are using VRFs, you can configure the agent to communicate over a specific VRF. You can also configure the agent to use a particular port.

### Configure the Agent to Use a VRF

<!-- vale off -->
By default, NetQ uses the *default* VRF for communication between the NetQ Appliance or VM and NetQ Agents. While optional, NVIDIA strongly recommends that you configure NetQ Agents to communicate with the NetQ Appliance or VM only via a {{<kb_link latest="cl" url="Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF.md" text="VRF">}}, including a {{<kb_link latest="cl" url="Layer-3/VRFs/Management-VRF.md" text="management VRF">}}. To do so, you need to specify the VRF name when configuring the NetQ Agent. For example, if you configured the management VRF and you want the agent to communicate with the NetQ Appliance or VM over it, configure the agent like this:
<!-- vale on -->

```
sudo netq config add agent server 192.168.1.254 vrf mgmt
sudo netq config restart agent
```

{{%notice info%}}
If you later change the VRF configured for the NetQ Agent (using a lifecycle management configuration profile, for example), you might cause the NetQ Agent to lose communication.
{{%/notice%}}

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 31980 for communication between the NetQ Appliance or VM and NetQ Agents. If you want the NetQ Agent to communicate with the NetQ Appliance or VM via a different port, you need to specify the port number when configuring the NetQ Agent, like this:

```
sudo netq config add agent server 192.168.1.254 port 7379
sudo netq config restart agent
```

## Configure the On-switch OPTA

{{<notice note>}}
On-switch OPTA functionality is an Early Access feature, and it does not support Flow Analysis or LCM. 
{{</notice>}}

On-switch OPTA is intended for use in small NetQ Cloud deployments where a dedicated OPTA might not be necessary. If you need help assessing the correct OPTA configuration for your deployment, {{<exlink url="https://www.nvidia.com/en-us/contact/sales/" text="contact your NVIDIA">}} sales team.

Instead of installing a {{<link title="Install NetQ as a Remote Deployment" text="dedicated OPTA appliance">}}, you can enable the OPTA service on every switch in your environment that will send data to the NetQ Cloud. To configure a switch for OPTA functionality, install the `netq-opta` package.

```
sudo apt-get update
sudo apt-get install netq-opta
```

Once the `netq-opta` package is installed, add your OPTA configuration key. Run the following command with the `config-key` obtained from the email you received from NVIDIA titled _NetQ Access Link_. You can also obtain the configuration key through the NetQ UI in the premise management configuration. For more information, see {{<link title="Access the NetQ UI#log-in-to-netq" text="First Time Log In - NetQ Cloud">}}.

```
netq config add opta config-key <config_key> [vrf <vrf_name>] [proxy-host <text-proxy-host> proxy-port <text-proxy-port>] 
```

The VRF name should be the VRF used to communicate with the NetQ Cloud. Specifying a proxy host and port is optional. For example:

```
netq config add opta config-key tHkSI2d3LmRldjMubmV0cWRldi5jdW11bHVasdf29ya3MuY29tGLsDIiwzeUpNc3BwK1IyUjVXY2p2dDdPL3JHS3ZrZ1dDUkpFY2JkMVlQOGJZUW84PTIEZGV2MzoHbmV0cWRldr vrf mgmt
```

You can also add a proxy host separately with the following command:

```
netq config add opta proxy-host <text-proxy-host> proxy-port <text-proxy-port>
```

The final steps is configuring the local NetQ agent on the switch to connect to the local OPTA service. Configure the agent on the switch to connect to `localhost` with the following command:

```
netq config add agent server localhost vrf mgmt
```