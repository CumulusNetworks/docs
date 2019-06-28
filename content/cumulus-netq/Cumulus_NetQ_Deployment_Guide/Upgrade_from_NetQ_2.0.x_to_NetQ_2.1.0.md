---
title: Upgrade from NetQ 2.0.x to NetQ 2.1.0
author: Cumulus Networks
weight: 69
aliases:
 - /display/NETQ/Upgrade+from+NetQ+2.0.x+to+NetQ+2.1.0
 - /pages/viewpage.action?pageId=10456364
pageID: 10456364
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
This document describes the steps required to upgrade from NetQ 2.0.x to
NetQ 2.1.0.

{{%notice info%}}

Cumulus Networks recommends only upgrading NetQ during a network
maintenance window.

Any data you have collected while using NetQ 2.0.x is maintained during
this upgrade process.

{{%/notice%}}

{{%notice note%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the agents re-sync with
the current state of the Host or Cumulus Linux switch with the NetQ
Platform.

{{%/notice%}}

To upgrade from NetQ 1.x to NetQ 2.1.0, please follow the instructions
in
[here](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=10456300).
Instructions for installing NetQ 2.1.0 for the first time can be found
in
[here](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=10456209).

## <span>Prerequisites</span>

Before you begin the upgrade process, please note the following:

  - The minimum supported Cumulus Linux version for NetQ 2.0.1 is 3.3.0.

  - You must upgrade your NetQ Agents as well as the NetQ Platform.

  - You can upgrade to NetQ 2.1.0 without upgrading Cumulus Linux.

  - The NetQ installer pod `netq-installer` should be up in either the
    *Containercreating* or *Running* state. The `netq-installer` pod
    state could also be *ContainerCreating*, in which case the host's
    kubelet is looking to initialize SSH keys.

## <span>Upgrade the NetQ Platform</span>

To upgrade the NetQ Platform:

1.  Obtain the NetQ-2.1.0.tgz and NetQ-2.1.0-installer.tgz files from
    your sales engineer.

2.  From a terminal window, log in to the NetQ Platform
    (*netq-appliance*) using your login credentials. This example uses
    the default *cumulus/CumulusLinux\!* credentials.
    
        <computer>:~<username>$ ssh cumulus@netq-appliance
        cumulus@netq-appliance's password: 
        cumulus@netq-appliance:~$ 

3.  Change to the root user.
    
        cumulus@netq-appliance:~$ sudo -i
        [sudo] password for cumulus:
        root@netq-appliance:~#

4.  Create an *installables* subdirectory in the mount directory.
    
        root@netq-appliance:~# mkdir -p /mnt/installables/
        root@netq-appliance:~#

5.  Copy the NetQ-2.1.0.tgz and NetQ-2.1.0-installer.tgz files into your
    new directory.
    
        root@netq-appliance:~# cd /mnt/installables/
        root@netq-appliance:/mnt/installables# cp /home/usr/dir/{NetQ-2.1.0.tgz,NetQ-2.1.0-installer.tgz} ./ 

6.  Export the installer script.
    
        root@netq-appliance:/mnt/installables#tar -xvf NetQ-2.1.0.tgz ./netq-install.sh

7.  Verify the contents of the directory. You should have the two TGZ
    files and the `netq-install.sh` script.
    
        root@netq-appliance:/mnt/installables# ls -l
        total 9607744
        -rw-r--r-- 1 cumulus cumulus  253283595 Apr 23 20:36 NetQ-2.1.0-installer.tgz
        -rw-r--r-- 1 cumulus cumulus 5911383922 Apr 23 11:13 NetQ-2.1.0.tgz
        -rwxr-xr-x 1 _lldpd _lldpd 4309 Apr 23 10:34 netq-install.sh
        root@netq-appliance:/mnt/installables#

8.  Configure SSH access.
    
    {{%notice info%}}
    
    If you perform the upgrade more than once, skip to step 8c.
    
    {{%/notice%}}
    
    1.  Generate the SSH key to enable you to run the script.
        
        {{%notice info%}}
        
        Leave the passphrase blank to simplify running the script.
        
        {{%/notice%}}
        
            root@netq-appliance:/mnt/installables# ssh-keygen -t rsa -b 4096
            Generating public/private rsa key pair.
            Enter file in which to save the key (/root/.ssh/id_rsa):
            Created directory '/root/.ssh'.
            Enter passphrase (empty for no passphrase): 
            Enter same passphrase again:
            Your identification has been saved in /root/.ssh/id_rsa.
            Your public key has been saved in /root/.ssh/id_rsa.pub.
    
    2.  Copy the key to the `authorized_keys` directory.
        
            root@netq-appliance:/mnt/installables# cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
            root@netq-appliance:/mnt/installables# chmod 0600 ~/.ssh/authorized_keys
            root@netq-appliance:/mnt/installables#
    
    3.  Associate the key with the installer.
        
            root@netq-appliance:~#/mnt/installables/./netq-install.sh --usekey ~/.ssh/id_rsa
            [Fri 22 Mar 2019 06:34:47 AM UTC] - This Script can only be invoked by user: root
            [Fri 22 Mar 2019 06:34:47 AM UTC] - The logged in user is root
            [Fri 22 Mar 2019 06:34:47 AM UTC] - Install directory /mnt/installables exists on system.
            [Fri 22 Mar 2019 06:34:47 AM UTC] - File /root/.ssh/id_rsa exists on system...
            [Fri 22 Mar 2019 06:34:47 AM UTC] - checking the presence of existing instaler-ssh-keys secret/instaler-ssh-keys created
            [Fri 22 Mar 2019 06:34:48 AM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
            [Fri 22 Mar 2019 06:34:58 AM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
            [Fri 22 Mar 2019 06:35:08 AM UTC] - Able to find the netq-installer up and running...

9.  Upgrade the netq-installer pod to the 2.1.0 version.*_  
    _*
    
        root@netq-appliance:/mnt/installables# ./netq-install.sh --installbundle /mnt/installables/NetQ-2.1.0-installer.tgz
        [Tue Apr 23 02:55:52 2019] - File /mnt/installables/NetQ-2.1.0-installer.tgz exists on system for updating netq installer ... 
        [Tue Apr 23 02:55:52 2019] - Updating the netq installer ... 
        [Tue Apr 23 02:55:52 2019] - Able to execute the command for updating netq installer ... 
        [Tue Apr 23 02:55:52 2019] - Checking initialization of installer update ... 
        [Tue Apr 23 02:55:57 2019] - Update of netq installer is in progress ... 
        ******[Tue Apr 23 02:58:57 2019] - Finished updating the netq-installer 
        [Tue Apr 23 02:58:57 2019] - Finishshed updating netq installer ! 
        0,/mnt/installables/NetQ-2.1.0-installer.tgz
        cumulus@sm-telem-02:/mnt/installables$
    
    {{%notice info%}}
    
    Please allow 3-4 minutes for the installer upgrade to complete.
    
    {{%/notice%}}

10. Confirm the netq-installer has been upgraded to the 2.1.0 version.
    
        root@netq-appliance:~# kubectl get pod -l app=netq-installer -o=jsonpath={.items[0].status.containerStatuses[0].image}
        netq-installer:2.1.0

11. Upgrade the NetQ software.
    
        root@netq-appliance:/mnt/installables/# ./netq-install.sh --updateapps /mnt/installables/NetQ-2.1.0.tgz
        [Tue Apr 23 02:55:52 2019] - File /mnt/installables/NetQ-2.1.0-installer.tgz exists on system for updating netq installer ... 
        [Tue Apr 23 02:55:52 2019] - Updating the netq installer ... 
        [Tue Apr 23 02:55:52 2019] - Able to execute the command for updating netq installer ... 
        [Tue Apr 23 02:55:52 2019] - Checking initialization of installer update ... 
        [Tue Apr 23 02:55:57 2019] - Update of netq installer is in progress ... 
        ******[Tue Apr 23 02:58:57 2019] - Finished updating the netq-installer 
        [Tue Apr 23 02:58:57 2019] - Finishshed updating netq installer ! 
        0,/mnt/installables/NetQ-2.1.0-installer.tgz
        cumulus@sm-telem-02:/mnt/installables$ sudo /mnt/installables/./netq-install.sh --updateapps /mnt/installables/NetQ-2.1.0.tgz
        [Tue Apr 23 03:01:13 2019] - File /mnt/installables/NetQ-2.1.0.tgz exists on system for updating netq apps... 
        [Tue Apr 23 03:01:13 2019] - User selected to update netq-apps ... 
        [Tue Apr 23 03:04:13 2019] - Able to execute the command for netq apps updates ... 
        [Tue Apr 23 03:04:13 2019] - Checking initialization of apps update ... 
        [Tue Apr 23 03:04:18 2019] - netq apps update is in progress ... 
        ******************************************************************[Tue Apr 23 03:37:18 2019] - Finished updating the netq apps ... 
        [Tue Apr 23 03:37:18 2019] - Finished updating apps .... 
    
    {{%notice info%}}
    
    Please allow about an hour for the upgrade to complete.
    
    {{%/notice%}}

You are now running NetQ 2.1.0.

## <span>Upgrade the NetQ Agents</span>

Whether using the NetQ Appliance or your own hardware, the NetQ Agent
must be upgraded on each node you want to monitor. The node can be a:

  - Switch running Cumulus Linux version 3.7.0 or later

  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7

  - Linux virtual machine running any of the above Linux operating
    systems

To upgrade the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

<span style="color: #000000;"> Instructions for installing the meta
package on each node type are included here: </span>

  - [Upgrade NetQ Agent on a Cumulus Linux
    Switch](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentCL)

  - [Upgrade NetQ Agent on an Ubuntu
    Server](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentUbuntu)

  - [Upgrade NetQ Agent on a Red Hat or CentOS
    Server](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentRHC)

{{%notice info%}}

<span style="color: #000000;"> If your network uses a proxy server for
external connections, you should first <span style="color: #339966;">
[<span style="color: #339966;"> configure a global proxy
</span>](/display/NETQ/Configuring+a+Global+Proxy) </span> so `apt-get`
</span> <span style="color: #000000;"> can access the meta package on
the Cumulus Networks repository </span> .

{{%/notice%}}

### <span id="src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentCL" class="confluence-anchor-link"></span><span>Upgrade NetQ Agent on a Cumulus Linux Switch</span>

A simple process upgrades the NetQ Agent on a Cumulus switch.

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

### <span id="src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentUbuntu" class="confluence-anchor-link"></span><span>Upgrade NetQ Agent on an Ubuntu Server (Optional)</span>

Before you upgrade the NetQ Agent on an Ubuntu server, make sure the
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

To upgrade the NetQ Agent on an Ubuntu server:

1.  Remove the current NetQ Agent and application software from your
    switch or host.
    
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

### <span id="src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentRHC" class="confluence-anchor-link"></span><span>Upgrade NetQ Agent on a Red Hat or CentOS Server (Optional)</span>

Before you upgrade the NetQ Agent on a Red Hat or CentOS server, make
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

To upgrade the NetQ Agent on a Red Hat or CentOS server:

1.  Remove the current NetQ Agent and application software from your
    switch or host.
    
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
    VRF](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentVRF)

  - [Configuring the Agent to Communicate over a Specific
    Port](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-port)

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
    VRF](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentVRF). If you
    intend to specify a port for communication, skip to [Configure the
    Agent to Communicate over a Specific
    Port](#src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-port).In this
    example, the IP address for the agent and cli servers is
    *192.168.1.254*.
    
        cumulus@switch:~$ netq config add agent server 192.168.1.254
        cumulus@switch:~$ netq config add cli server 192.168.1.254
    
    This command updates the configuration in the `/etc/netq/netq.yml`
    file and enables the NetQ CLI.

4.  Restart NetQ Agent and CLI.
    
        cumulus@switch:~$ netq config restart agent
        cumulus@switch:~$ netq config restart cli

### <span id="src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-AgentVRF" class="confluence-anchor-link"></span><span>Configure the Agent to Use a VRF (Optional)</span>

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

### <span id="src-10456364_UpgradefromNetQ2.0.xtoNetQ2.1.0-port" class="confluence-anchor-link"></span><span>Configure the Agent to Communicate over a Specific Port (Optional)</span>

By default, NetQ uses port 8981 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent: <span style="color: #222222;"> </span>

    cumulus@leaf01:~$ netq config restart agent

## <span>Upgrade Tips</span>

After your installation is complete, the following scenarios may be
encountered.

### <span>Scenario 1: NetQ Appliance IP Address Was Changed</span>

The NetQ Appliance came with a pre-configured IP address, which has
since been changed. How do I recover the system?

<span style="color: #222222;"> You must remove and reconfigure the
Kubernetes configuration. Follow these steps: </span>

1.  Locate the Kubernetes pods.  
    `cumulus@switch:~$ kubectl get pods`

2.  Reset all Kubernetes administrative settings. Run the command twice
    to make sure all directories and files have been reset.  
    `cumulus@switch:~$ sudo kudeadm reset -f cumulus@switch:~$ sudo
    kudeadm reset -f`

3.  Remove the Kubernetes configuration.  
    `cumulus@switch:~$ sudo rm /home/cumulus/.kube/config`

4.  Reset <span style="color: #000000;"> the NetQ Appliance install
    daemon. </span>  
    `cumulus@switch:~$ sudo systemctl reset-failed`

5.  Reset the Kubernetes service.  
    `cumulus@switch:~$ sudo systemctl restart cts-kubectl-config`  
    **Note**: Allow 15 minutes for the prompt to return.

### <span>Scenario 2: No IP Address Assigned to the NetQ Appliance on Boot</span>

A user did not configure an IP address when the system was first booted.
Later the user assigned an IP address to eth0, but the NetQ appliance
does not appear to be functioning.

<span style="color: #222222;"> You must reset </span>
<span style="color: #000000;"> the install daemon </span>
<span style="color: #222222;"> and restart the Kubernetes service.
Follow these steps: </span>

1.  Reset <span style="color: #000000;"> the NetQ Appliance install
    daemon. </span>  
    `cumulus@switch:~$ sudo systemctl reset-failed`

2.  Restart the Kubernetes service.  
    `cumulus@switch:~$ sudo systemctl restart cts-kubectl-config`
