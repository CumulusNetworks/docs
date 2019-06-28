---
title: Install NetQ
author: Cumulus Networks
weight: 65
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=10456317
pageID: 10456317
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
Installing NetQ can be accomplished in one of three ways:

  - If you have purchased a NetQ Appliance, the only installation
    required is to load the NetQ Agent on any host you want to monitor.

  - If you already have a Cumulus Linux switch (running version 3.3.0 or
    later) and you want to add NetQ functionality to it, installation
    involves three steps:
    
      - Verify your server meets the hardware and software requirements.
    
      - Load the software onto the switch.
    
      - Load the NetQ Agent onto the hosts.

  - If you upgrading from a prior version of NetQ, please follow the
    instructions in the relevant upgrade topic, rather than the
    instructions here.

## <span>Prerequisites</span>

### <span id="src-10456317_InstallNetQ-hwspec" class="confluence-anchor-link"></span><span>Hardware Requirements</span>

NetQ is supported on the NetQ Appliance and a variety of other hardware.

{{%notice note%}}

**IMPORTANT**

You must meet these hardware requirements to install the VM and have it
run properly.

{{%/notice%}}

In all cases, the NetQ software requires a server with the following:

| Requirement             | Description                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Processing power        | Eight (8) virtual CPUs                                                                                                         |
| Memory                  | 64 GB RAM                                                                                                                      |
| Local disk storage      | 256 GB SSD (**Note**: This must be an SSD; use of other storage options can lead to system instability and are not supported.) |
| Network interface speed | 1 G NIC or higher                                                                                                              |

If you are *not* using the NetQ Appliance, you must open the following
ports on the NetQ server to use the NetQ software:

| Port  | Component Access         |
| ----- | ------------------------ |
| 31980 | NetQ Platform            |
| 32708 | API Gateway              |
| 32666 | Web-based User Interface |

{{%notice info%}}

These ports have changed from NetQ 1.4 and earlier.

{{%/notice%}}

### <span>Operating System Requirements</span>

NetQ 2.1.0 is supported on the following operating systems:

  - Cumulus Linux 3.3.0 and later

  - Ubuntu 16.04

  - Red Hat<sup>®</sup> Enterprise Linux (RHEL) 7.1

  - CentOS 7

### <span>NetQ Application Support</span>

  - NetQ CLI is supported on NetQ 1.0 and later.

  - NetQ UI is supported on NetQ 2.1.0.

  - RESTful API is supported on NetQ 2.1.0.

## <span>Install Workflow</span>

Installation of NetQ involves installing the NetQ Platform, and
installing and configuring the NetQ Agents. Additional steps are needed
to <span style="color: #ff0000;"> [Integrate NetQ with Event
Notification
Applications](/cumulus-netq/Cumulus_NetQ_Deployment_Guide/Integrate_with_Third-party_Software_and_Hardware)
</span> . This flow chart shows the required steps to install and setup
NetQ to start validating your network and the optional steps of
integrating with event notification applications and monitoring hosts.

{{% imgOld 0 %}}

## <span>Install the NetQ Platform</span>

If you *are* *not* using the NetQ Appliance, you must install the NetQ
Platform on your selected hardware. If you have deployed the NetQ
Appliance, you can skip to [Install NetQ
Agent](#src-10456317_InstallNetQ-agent).

The NetQ Platform is comprised of the following components:

  - **NetQ application**: network monitoring and analytics functionality

  - **NetQ CLI**: command line user interface for monitoring network and
    administering NetQ through a terminal session

  - **NetQ UI**: graphical interface for monitoring network and
    administering NetQ

  - **NetQ API**: Restful application programming interface for
    accessing NetQ data and integrating with third-party tools

  - **Authorization**: secure access functionality

The server is available in one of two formats:

  - Virtual:
    
      - VMware ESXi™ 6.5 virtual machine (VM)
    
      - KVM/QCOW (QEMU Copy on Write) image for use on CentOS, Ubuntu
        and RedHat hosts

  - Physical:
    
      - NetQ Appliance (software pre-installed)

{{%notice info%}}

**Best Practice**

Cumulus Networks recommends you install the NetQ software on a server
that is part of an out-of-band management network to ensure it can
monitor in-band network issues without being affected itself. You should
run the software on a separate, powerful server to ensure proper
operation and for maximum usability and performance. Refer to [Hardware
Requirements](#src-10456317_InstallNetQ-hwspec) for specifics.

{{%/notice%}}

### <span>Install Using VM</span>

To install the NetQ Platform using a VM image:

1.  **IMPORTANT**: Confirm that your server hardware meets the
    requirements set out [here](#src-10456317_InstallNetQ-hwspec).

2.  Download the NetQ Platform image.
    
    1.  On the [Cumulus
        Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.
    
    2.  Click *2.1* from the **Version** list box, and then select
        *2.1.0* from the submenu.
    
    3.  Optionally, select the hypervisor you wish to use from the
        **Hypervisor/Platform** list box.
        
        {{% imgOld 1 %}}
    
    4.  Scroll down to review the images that match your selection
        criteria, and click **Download** for the image you want.
        
        {{% imgOld 2 %}}

3.  Open your hypervisor and set up your VM.  
    The following example show this process using an OVA file with
    VMware ESXi. You can use this for reference or use your own
    hypervisor instructions.

Click here to show example...

1.  Enter the address of the hardware in your browser.

2.  Log in to VMware using credentials with root access.  
    
    {{% imgOld 3 %}}

3.  Click **Create/Register VM** at the top of the right pane.
    
    {{% imgOld 4 %}}

4.  Select **Deploy a virtual machine from and OVF or OVA file**, and
    click **Next**.  
    
    {{% imgOld 5 %}}

5.  Provide a name for the VM, for example *Cumulus NetQ*.

6.  Drag and drop the NetQ Platform image file you downloaded in Step 1
    above.

7.  Click **Next**.
    
    {{% imgOld 6 %}}

8.  Select the storage type and data store for the image to use, then
    click **Next**. In this example, only one is available.
    
    {{% imgOld 7 %}}

9.  Accept the default deployment options or modify them according to
    your network needs. Click **Next** when you are finished.
    
    {{% imgOld 8 %}}

10. Review the configuration summary. Click **Back** to change any of
    the settings, or click **Finish** to continue with the creation of
    the VM.
    
    {{% imgOld 9 %}}
    
    The progress of the request is shown in the Recent Tasks window at
    the bottom of the application. This may take some time, so continue
    with your other work until the upload finishes.

11. Once completed, view the full details of the VM and hardware.
    
    {{% imgOld 10 %}}

### <span>Verify the Installation</span>

1.  Verify you can access the NetQ CLI.
    
    1.  From a terminal window, log in to the switch using the default
        credentials (*cumulus/CumulusLinux\!*).
        
            <computer>:~<username>$ ssh cumulus@<switch-ipaddress>
            Warning: Permanently added 'netq-appliance,10.0.0.167' (ECDSA) to the list of known hosts.
            cumulus@netq-appliance's password: <enter CumulusLinux! here>
             
            Welcome to Cumulus (R) Linux (R)
             
            For support and online technical documentation, visit
            http://www.cumulusnetworks.com/support
             
            The registered trademark Linux (R) is used pursuant to a sublicense from LMI,
            the exclusive licensee of Linus Torvalds, owner of the mark on a world-wide
            basis.
             
            cumulus@switch:~$ 
    
    2.  Run some NetQ commands.
        
            cumulus@switch:~$ netq show lldp
            cumulus@switch:~$ netq check ntp

2.  Verify that NTP is configured and running. NTP operation is critical
    to proper operation of NetQ. Refer to [Setting Date and
    Time](/display/NETQ/Setting+Date+and+Time) in the *Cumulus Linux
    User Guide* for details and instructions.

3.  Continue the NetQ installation by loading the NetQ Agent on each
    switch or host you want to monitor. Refer to the next section for
    instructions.

## <span id="src-10456317_InstallNetQ-agent" class="confluence-anchor-link"></span><span>Install the NetQ Agent</span>

Whether using the NetQ Appliance or your own hardware, the NetQ Agent
must be installed on each node you want to monitor. The node can be a:

  - Switch running Cumulus Linux version 3.7.0 or later

  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7

  - Linux virtual machine running any of the above Linux operating
    systems

To install the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

<span style="color: #000000;"> Instructions for installing the meta
package on each node type are included here: </span>

  - [Install NetQ Agent on a Cumulus Linux
    Switch](#src-10456317_InstallNetQ-AgentCL)

  - [Install NetQ Agent on an Ubuntu
    Server](#src-10456317_InstallNetQ-AgentUbuntu)

  - [Install NetQ Agent on a Red Hat or CentOS
    Server](#src-10456317_InstallNetQ-AgentRHC)

{{%notice info%}}

<span style="color: #000000;"> If your network uses a proxy server for
external connections, you should first <span style="color: #339966;">
[<span style="color: #339966;"> configure a global proxy
</span>](/display/NETQ/Configuring+a+Global+Proxy) </span> so `apt-get`
</span> <span style="color: #000000;"> can access the meta package on
the Cumulus Networks repository </span> .

{{%/notice%}}

### <span id="src-10456317_InstallNetQ-AgentCL" class="confluence-anchor-link"></span><span>Install NetQ Agent on a Cumulus Linux Switch</span>

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the
    <span style="color: #000000;"> repository for Cumulus NetQ. **Note**
    that NetQ has a separate repository from Cumulus Linux. </span>
    
        cumulus@switch:~$ sudo nano /etc/apt/sources.list
        ...
        deb http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-2.1
        ...
    
    {{%notice tip%}}
    
    The repository `deb http://apps3.cumulusnetworks.com/repos/deb
    CumulusLinux-3 netq-latest` can be used if you want to always
    retrieve the latest posted version of NetQ.
    
    {{%/notice%}}

2.  Update the local `apt` repository, then install the NetQ meta
    package on the switch.
    
        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install cumulus-netq

Repeat these steps for each Cumulus switch, or use an automation tool to
install NetQ Agent on multiple Cumulus Linux switches.

### <span id="src-10456317_InstallNetQ-AgentUbuntu" class="confluence-anchor-link"></span><span>Install NetQ Agent on an Ubuntu Server (Optional)</span>

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all

  - iproute2 4.3.0-1ubuntu3 amd64

  - lldpd 0.7.19-1 amd64

  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64
    
    {{%notice info%}}
    
    Make sure you are running lldp**d**, not lldp**ad**. Ubuntu does not
    include `lldpd` by default, which is required for the installation.
    To install this package, run the following commands:
    
        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install lldpd
        root@ubuntu:~# systemctl enable lldpd.service
        root@ubuntu:~# systemctl start lldpd.service
    
    {{%/notice%}}

To install the NetQ Agent on an Ubuntu server:

1.  If you are upgrading from a prior version of NetQ, first purge the
    current NetQ Agent and application software from your switch or
    host; otherwise skip to Step 3.
    
        root@ubuntu:~# sudo systemctl stop netq-agent
        root@ubuntu:~# sudo systemctl stop netqd
        root@ubuntu:~# yum remove netq-agent netq-apps

2.  Verify you have removed all older NetQ packages. You should not see
    any older version files.
    
        root@ubuntu:~# dpkg -l | grep netq

3.  Reference and update the local `apt` repository.
    
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

4.  Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following lines:
    
        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    
    {{%notice note%}}
    
    The use of `netq-latest` in this example means that a `get` to the
    repository always retrieves the lastest version of NetQ, even in the
    case where a major version update has been made. If you want to keep
    the repository on a specific version — such as `netq-2.1` — use that
    instead.
    
    {{%/notice%}}

5.  Install NTP on the server.
    
        root@ubuntu:~# sudo apt-get install ntp

6.  Configure the NTP server.
    
    1.  Open the `/etc/ntp.conf` file in your text editor of choice.
    
    2.  Under the Server section, specify the NTP server IP address or
        hostname.

7.  Enable and start the NTP service.
    
        root@ubuntu:~# sudo systemctl enable ntp.service
        root@ubuntu:~# sudo systemctl start ntp.service

8.  Verify NTP is operating correctly. Look for an asterisk (\*) or a
    plus sign (+) that indicates the clock is synchronized.
    
        root@ubuntu:~# ntpq -pn
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
        +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
         2a00:7600::41   .STEP.          16 u    - 1024    0    0.000    0.000   0.000
        *129.250.35.250  249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

9.  Install the meta package on the server.
    
        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install cumulus-netq

10. Restart the NetQ daemon.
    
        root@ubuntu:~# systemctl enable netqd
        root@ubuntu:~# systemctl restart netqd

### <span id="src-10456317_InstallNetQ-AgentRHC" class="confluence-anchor-link"></span><span>Install NetQ Agent on a Red Hat or CentOS Server (Optional)</span>

Before you install the NetQ Agent on a Red Hat or CentOS server, make
sure the following packages are installed and running these minimum
versions:

  - iproute-3.10.0-54.el7\_2.1.x86\_64

  - lldpd-0.9.7-5.el7.x86\_64
    
    {{%notice info%}}
    
    Make sure you are running lldp**d**, not lldp**ad**.
    
    CentOS does not include `lldpd` by default, nor does it include
    `wget`, which is required for the installation. To install this
    package, run the following commands:
    
        root@centos:~# yum -y install epel-release
        root@centos:~# yum -y install lldpd
        root@centos:~# systemctl enable lldpd.service
        root@centos:~# systemctl start lldpd.service
        root@centos:~# yum install wget
    
    {{%/notice%}}

  - ntp-4.2.6p5-25.el7.centos.2.x86\_64

  - ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

To install the NetQ Agent on a Red Hat or CentOS server:

1.  If you are upgrading from a prior version of NetQ, first purge the
    current NetQ Agent and application software from your switch or
    host; otherwise skip to Step 3.
    
        root@rhel7:~# sudo systemctl stop netq-agent
        root@rhel7:~# sudo systemctl stop netqd
        root@rhel7:~# apt-get purge --auto-remove cumulus-netq netq-agent netq-apps

2.  Verify you have removed all older NetQ packages. You should not see
    any older version files.
    
        root@rhel7:~# dpkg -l | grep netq

3.  Reference and update the local `yum` repository.
    
        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
        root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

4.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1`
    flag for the two NetQ repositories.
    
        root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
        ... 
        [cumulus-arch-netq-2.1]
        name=Cumulus netq packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.1/$basearch 
        gpgcheck=1
        enabled=1
        [cumulus-noarch-netq-2.1]
        name=Cumulus netq architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-2.1/noarch
        gpgcheck=1
        enabled=1
        ...

5.  Install NTP on the server.
    
        root@rhel7:~# yum install ntp

6.  Configure the NTP server.
    
    1.  Open the `/etc/ntp.conf` file in your text editor of choice.
    
    2.  Under the Server section, specify the NTP server IP address or
        hostname.

7.  Enable and start the NTP service.
    
        root@rhel7:~# sudo systemctl enable ntpd.service
        root@rhel7:~# sudo systemctl start ntpd.service

8.  Verify NTP is operating correctly. Look for an asterisk (\*) or a
    plus sign (+) that indicates the clock is synchronized.
    
        root@rhel7:~# ntpq -pn
             remote           refid      st t when poll reach   delay   offset  jitter
        ==============================================================================
        +173.255.206.154 132.163.96.3     2 u   86  128  377   41.354    2.834   0.602
        +12.167.151.2    198.148.79.209   3 u  103  128  377   13.395   -4.025   0.198
         2a00:7600::41   .STEP.          16 u    - 1024    0    0.000    0.000   0.000
        *129.250.35.250  249.224.99.213   2 u  101  128  377   14.588   -0.299   0.243

9.  Install the Bash completion and NetQ meta packages on the server.
    
        root@rhel7:~# yum -y install bash-completion
        root@rhel7:~# yum install cumulus-netq

10. Restart the NetQ daemon.
    
        root@rhel7:~# systemctl enable netqd ; systemctl restart netqd

## <span>Set Up the NetQ Agents</span>

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. Depending on your deployment, follow the
relevant additional instructions after the basic configuration steps:

  - [Basic
    Configuration](https://docs.cumulusnetworks.com/display/NETQ140DRAFT/Cumulus+NetQ+1.4+Installation+Guide#CumulusNetQ1.4InstallationGuide-BasicConfig)

  - [Configuring the Agent to Use a
    VRF](#src-10456317_InstallNetQ-AgentVRF)

  - [Configuring the Agent to Communicate over a Specific
    Port](#src-10456317_InstallNetQ-port)

### <span>Basic Configuration </span>

This is the minimum configuration required to properly monitor your
nodes.

1.  Verify that [NTP](/display/NETQ/Setting+Date+and+Time) is running on
    the host node. Nodes must be in time synchronization with the NetQ
    Platform to enable useful statistical analysis.
    
        cumulus@switch:~$ sudo systemctl status ntp
        [sudo] password for cumulus:
        ● ntp.service - LSB: Start NTP daemon
           Loaded: loaded (/etc/init.d/ntp; bad; vendor preset: enabled)
           Active: active (running) since Fri 2018-06-01 13:49:11 EDT; 2 weeks 6 days ago
             Docs: man:systemd-sysv-generator(8)
           CGroup: /system.slice/ntp.service
                   └─2873 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -c /var/lib/ntp/ntp.conf.dhcp -u 109:114

2.  Restart `rsyslog` so log files are sent to the correct destination.
    
        cumulus@switch:~$ sudo systemctl restart rsyslog.service

3.  Link the node to the NetQ Platform you configured above.  
    You must configure both the agent server and the cli server to link
    to the NetQ Platform. **Note:** If you intend to use VRF, skip to
    [Configure the Agent to Use
    VRF](#src-10456317_InstallNetQ-AgentVRF). If you intend to specify a
    port for communication, skip to [Configure the Agent to Communicate
    over a Specific Port](#src-10456317_InstallNetQ-port).In this
    example, the IP address for the agent and cli servers is
    *192.168.1.254*.
    
        cumulus@switch:~$ netq config add agent server 192.168.1.254
        cumulus@switch:~$ netq config add cli server 192.168.1.254
    
    This command updates the configuration in the `/etc/netq/netq.yml`
    file and enables the NetQ CLI.

4.  Restart NetQ Agent and CLI.
    
        cumulus@switch:~$ netq config restart agent
        cumulus@switch:~$ netq config restart cli

### <span id="src-10456317_InstallNetQ-AgentVRF" class="confluence-anchor-link"></span><span>Configure the Agent to Use a VRF (Optional)</span>

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/display/NETQ/Virtual+Routing+and+Forwarding+-+VRF), including a
[management VRF](/display/NETQ/Management+VRF). To do so, you need to
specify the VRF name when configuring the NetQ Agent. For example, if
the management VRF is configured and you want the agent to communicate
with the NetQ Platform over it, configure the agent like this:
<span style="color: #222222;"> </span>

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
    cumulus@leaf01:~$ netq config add cli server 192.168.254 vrf mgmt

You then restart the agent: <span style="color: #222222;"> </span>

    cumulus@leaf01:~$ netq config restart agent
    cumulus@leaf01:~$ netq config restart cli

### <span id="src-10456317_InstallNetQ-port" class="confluence-anchor-link"></span><span>Configure the Agent to Communicate over a Specific Port (Optional)</span>

By default, NetQ uses port 8981 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent: <span style="color: #222222;"> </span>

    cumulus@leaf01:~$ netq config restart agent

## <span>Integrate with Event Notification Tools</span>

If you want to proactively monitor events in your network, you can
integrate NetQ with the PagerDuty or Slack notification tools. To do so
you need to configure both the notification application itself to
receive the messages, and NetQ with what messages to send and where to
send them. Refer to [Integrate NetQ with Event Notification
Applications](/cumulus-netq/Cumulus_NetQ_Deployment_Guide/Integrate_with_Third-party_Software_and_Hardware)
to use the CLI for configuration.

## <span>Set Up Security</span>

<span style="color: #ff0000;"> <span style="color: #000000;"> When you
set up and configured your Cumulus Linux switches, you likely configured
a number of the security features available. Cumulus recommends the same
security measures be followed for the NetQ Platform in the
out-of-band-network. Refer to the </span> [Securing Cumulus Linux white
paper](https://cumulusnetworks.com/learn/web-scale-networking-resources/white-papers/securing-cumulus-linux/)
<span style="color: #000000;"> for details. </span> </span>

<span style="color: #ff0000;"> <span style="color: #000000;"> Your
Cumulus Linux switches have a number of ports open by default. A few
additional ports must be opened to run the NetQ software (refer to
[Default Open Ports in Cumulus Linux and
NetQ](https://support.cumulusnetworks.com/hc/en-us/articles/228281808-Default-Open-Ports-in-Cumulus-Linux-and-NetQ)
article). </span> </span>

<span style="color: #ff0000;">  
</span>
