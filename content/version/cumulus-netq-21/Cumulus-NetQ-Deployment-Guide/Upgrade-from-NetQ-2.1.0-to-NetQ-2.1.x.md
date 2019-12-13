---
title: Upgrade from NetQ 2.1.0 to NetQ 2.1.x
author: Cumulus Networks
weight: 39
aliases:
 - /display/NETQ21/Upgrade+from+NetQ+2.1.0+to+NetQ+2.1.x
 - /pages/viewpage.action?pageId=10464065
pageID: 10464065
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq-21
siteSlug: cumulus-netq-21
---
This document describes the steps required to upgrade from NetQ 2.1.0 to
NetQ 2.1.1 or later.

{{%notice note%}}

Cumulus Networks recommends only upgrading NetQ during a network
maintenance window.

Any data you have collected while using NetQ 2.1.0 is maintained during
this upgrade process.

{{%/notice%}}

{{%notice note%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the agents re-sync with
the current state of the Host or Cumulus Linux switch with the NetQ
Platform.

{{%/notice%}}

To upgrade from NetQ 1.x to NetQ 2.1.x, please follow the instructions
[here](../Upgrade-from-NetQ-1.x-to-NetQ-2.1.x/).
Instructions for installing NetQ 2.1.x for the first time can be found
[here](../Install-NetQ/).

## Prerequisites

Before you begin the upgrade process, please note the following:

  - The minimum supported Cumulus Linux version for NetQ 2.1.x is 3.3.0.
  - You must upgrade your NetQ Agents as well as the NetQ Platform.
  - You can upgrade to NetQ 2.1.x without upgrading Cumulus Linux.
  - The NetQ installer pod `netq-installer` should be up in either the
    *Containercreating* or *Running* state. The `netq-installer` pod
    state could also be *ContainerCreating*, in which case the host is
    initializing with the SSH keys.

## Upgrade the NetQ Platform or NetQ Appliance

To upgrade the NetQ Platform:

1.  Download the NetQ Platform or Appliance upgrade image
    (NetQ-2.1.x.tgz).
    
    1.  On the [Cumulus
        Downloads](https://cumulusnetworks.com/downloads/) page, select
        *NetQ* from the **Product** list box.
    
    2.  Click *2.1* from the **Version** list box, and then select
        *2.1.x* from the submenu.
        
        {{% imgOld 0 %}}
    
    3.  Scroll down to review the images that match your selection
        criteria.
        
        {{% imgOld 1 %}}
    
    4.  Click **Upgrade** for the relevant version (VMware or KVM for
        NetQ Platform, Appliance for NetQ Appliance).

2.  From a terminal window, log in to the NetQ Platform or Appliance
    using your login credentials. This example uses the default
    *cumulus/CumulusLinux\!* credentials and is run on the NetQ
    Appliance.
    
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

5.  Copy the NetQ-2.1.x.tgz file into your new directory.
    
        root@netq-appliance:~# cd /mnt/installables/
        root@netq-appliance:/mnt/installables# cp /home/usr/dir/NetQ-2.1.x.tgz ./ 

6.  Export the installer script.
    
        root@netq-appliance:/mnt/installables# tar -xvf NetQ-2.1.x.tgz ./netq-install.sh

7.  Verify the contents of the directory. You should have the
    NetQ-2.1.x.tgz file and the `netq-install.sh` script.
    
        root@netq-appliance:/mnt/installables# ls -l
        total 9607744
        -rw-r--r-- 1 cumulus cumulus 5911383922 Apr 23 11:13 NetQ-2.1.x.tgz
        -rwxr-xr-x 1 _lldpd _lldpd 4309 Apr 23 10:34 netq-install.sh
        root@netq-appliance:/mnt/installables#

8.  Configure SSH access.
    
    {{%notice note%}}
    
If you perform the upgrade more than once, you can skip this step
after performing it once.
    
If you have an existing SSH key, skip to step 8c.
    
    {{%/notice%}}
    
    1.  Generate the SSH key to enable you to run the script.
        
        {{%notice note%}}
        
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
        
            root@netq-appliance:/mnt/installables/# ./netq-install.sh --usekey ~/.ssh/id_rsa
            [Fri 22 Mar 2019 06:34:47 AM UTC] - This Script can only be invoked by user: root
            [Fri 22 Mar 2019 06:34:47 AM UTC] - The logged in user is root
            [Fri 22 Mar 2019 06:34:47 AM UTC] - Install directory /mnt/installables exists on system.
            [Fri 22 Mar 2019 06:34:47 AM UTC] - File /root/.ssh/id_rsa exists on system...
            [Fri 22 Mar 2019 06:34:47 AM UTC] - checking the presence of existing instaler-ssh-keys secret/instaler-ssh-keys created
            [Fri 22 Mar 2019 06:34:48 AM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
            [Fri 22 Mar 2019 06:34:58 AM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
            [Fri 22 Mar 2019 06:35:08 AM UTC] - Able to find the netq-installer up and running...

9.  Upgrade the NetQ software. This example show an upgrade to version
    2.1.2.
    
        root@netq-appliance:/mnt/installables# ./netq-install.sh  --installbundle  /mnt/installables/NetQ-2.1.2.tgz --updateapps
        [Wed 05 Jun 2019 08:18:37 PM UTC] - File /mnt/installables/NetQ-2.1.2.tgz exists on system for updating netq-installer ...
        [Wed 05 Jun 2019 08:18:37 PM UTC] - Check the netq-installer is up and running to process requests ....
        [Wed 05 Jun 2019 08:18:37 PM UTC] - Checking the Status of netq-installer ....
        [Wed 05 Jun 2019 08:18:37 PM UTC] - The netq-installer is up and running ...
        [Wed 05 Jun 2019 08:18:37 PM UTC] - Updating the netq-installer ...
        [Wed 05 Jun 2019 08:18:37 PM UTC] - Able to execute the command for updating netq-installer ...
        [Wed 05 Jun 2019 08:18:37 PM UTC] - Checking initialization of netq-installer update ...
        [Wed 05 Jun 2019 08:18:37 PM UTC] - Update of netq-installer is in progress ...
        ******************************0
        [Wed 05 Jun 2019 08:28:39 PM UTC] - Successfully updated netq installer....
        0,/mnt/installables/NetQ-2.1.2.tgz
        [Wed 05 Jun 2019 08:28:39 PM UTC] - File /mnt/installables/NetQ-2.1.2.tgz exists on system for updating netq apps...
        [Wed 05 Jun 2019 08:28:39 PM UTC] - User selected to update netq-apps ...
        [Wed 05 Jun 2019 08:28:39 PM UTC] - Checking the Status of netq-installer ....
        [Wed 05 Jun 2019 08:28:41 PM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
        [Wed 05 Jun 2019 08:28:52 PM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
        [Wed 05 Jun 2019 08:29:03 PM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
        [Wed 05 Jun 2019 08:29:14 PM UTC] - Unable to find netq-installer up and running. Sleeping for 10 seconds ...
        [Wed 05 Jun 2019 08:29:24 PM UTC] - The netq-installer is up and running ...
        [Wed 05 Jun 2019 08:29:24 PM UTC] - Able to execute the command for netq apps updates ...
        [Wed 05 Jun 2019 08:29:24 PM UTC] - Checking initialization of apps update ...
        [Wed 05 Jun 2019 08:29:29 PM UTC] - netq apps update is in progress ...
        ************************************************************************************************************************************    ******************************************************************************************************************************************************************************
        0
        [Wed 05 Jun 2019 09:20:31 PM UTC] - Successfully updated netq apps ....
        root@netq-appliance:/mnt/installables#
    
    {{%notice info%}}
    
Please allow about an hour for the upgrade to complete.
    
    {{%/notice%}}

You are now running NetQ 2.1.x.

## Upgrade the NetQ Agents

Whether using the NetQ Appliance or your own hardware, the NetQ Agent
should be upgraded on each of the existing nodes you want to monitor.
The node can be a:

  - Switch running Cumulus Linux version 3.7.0 or later
  - Server running Red Hat RHEL 7.1, Ubuntu 16.04 or CentOS 7
  - Linux virtual machine running any of the above Linux operating
    systems

To upgrade the NetQ Agent you need to install the OS-specific meta
package, `cumulus-netq`, on each switch. Optionally, you can install it
on hosts. The meta package contains the NetQ Agent, the NetQ command
line interface (CLI), and the NetQ library. The library contains modules
used by both the NetQ Agent and the CLI.

- [Upgrade NetQ Agent on a Cumulus Linux Switch](#upgrade-netq-agent-on-a-cumulus-linux-switch)
- [Upgrade NetQ Agent on an Ubuntu Server](#upgrade-netq-agent-on-an-ubuntu-server)
- [Upgrade NetQ Agent on a Red Hat or CentOS Server](#upgrade-net-agent-on-a-red-hat-or-centos-server)

{{%notice note%}}

If your network uses a proxy server for external connections, you should
first [configure a global proxy](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Configuring-a-Global-Proxy/), so `apt-get` can access the meta package on the Cumulus Networks repository.

{{%/notice%}}

### Upgrade NetQ Agent on a Cumulus Linux Switch

A simple process installs the NetQ Agent on a Cumulus switch.

1.  Edit the `/etc/apt/sources.list` file to add the repository for
    Cumulus NetQ. **Note** that NetQ has a separate repository from
    Cumulus Linux.*
    
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

3.  Verify the upgrade.
    
        cumulus@switch:~$ dpkg -l | grep netq
        ii  cumulus-netq                      2.1.2-cl3u17~1557345432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.1.2-cl3u17~1559681411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.1.2-cl3u17~1559681411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

4.  Repeat these steps for each Cumulus switch, or use an automation
    tool to install NetQ Agent on multiple Cumulus Linux switches.

### Upgrade NetQ Agent on an Ubuntu Server

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository.
    
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

2.  In `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list`, verify
    the following repository is included:
    
        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
        ...
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        ...
    
    {{%notice note%}}
    
The use of `netq-latest` in this example means that a `get` to the
repository always retrieves the latest version of NetQ, even in the
case where a major version update has been made. If you want to keep
the repository on a specific version — such as `netq-2.1` — use that
instead.
    
    {{%/notice%}}

3.  Install the meta package on the server.
    
        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install cumulus-netq

4.  Verify the upgrade.
    
        root@ubuntu:~$ dpkg -l | grep netq
        ii  cumulus-netq                      2.1.2-cl3u17~1557345432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.1.2-cl3u17~1559681411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.1.2-cl3u17~1559681411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

5.  Repeat these steps for each switch/host running Ubuntu, or use an
    automation tool to install NetQ Agent on multiple switches/hosts.

### Upgrade NetQ Agent on a Red Hat or CentOS Server

To install the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository.
    
        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
        root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1`
    flag for the two NetQ repositories.
    
        [cumulus@firewall-2 ~]$ cat /etc/yum.repos.d/cumulus-host-el.repo 
        [cumulus-arch-netq-2.0]
        name=Cumulus netq packages
        baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/$basearch
        gpgcheck=1
        enabled=1
         
        [cumulus-noarch-netq-2.0]
        name=Cumulus netq architecture-independent packages
        baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/noarch
        gpgcheck=1
        enabled=1
         
        [cumulus-src-netq-2.0]
        name=Cumulus netq source packages
        baseurl=http://rohbuild03.mvlab.cumulusnetworks.com/dev/rpm/el/7/netq-latest/src
        gpgcheck=1
        enabled=1

3.  Update the NetQ meta packages on the server.
    
        root@rhel7:~# yum update cumulus-netq.x86_64

4.  Verify the upgrade.
    
        root@ubuntu:~$ yum list installed | grep netq
        ii  cumulus-netq                      2.1.2-cl3u17~1557345432.a60ec9a    all          This meta-package provides installation of Cumulus NetQ packages.
        ii  netq-agent                        2.1.2-cl3u17~1559681411.2bba220    amd64        Cumulus NetQ Telemetry Agent for Cumulus Linux
        ii  netq-apps                         2.1.2-cl3u17~1559681411.2bba220    amd64        Cumulus NetQ Fabric Validation Application for Cumulus Linux

5.  Repeat these steps for each switch/host running Ubuntu, or use an
    automation tool to install NetQ Agent on multiple switches/hosts.

## Configure Optional NetQ Agent Settings

Once the NetQ Agents have been installed on the network nodes you want
to monitor, the NetQ Agents must be configured to obtain useful and
relevant data. The code examples shown in this section illustrate how to
configure the NetQ Agent on a Cumulus switch, but it is exactly the same
for the other type of nodes. If you have already configured these
settings, you do not need to do so again.

- [Configure the Agent to Use a VRF](#configure-the-agent-to-use-a-vrf)
- [Configure the Agent to Communicate over a Specific Port](#configure-the-agent-to-communicate-over-a-specific-port)

### Configure the Agent to Use a VRF

While optional, Cumulus strongly recommends that you configure NetQ
Agents to communicate with the NetQ Platform only via a
[VRF](/cumulus-linux/Layer-3/Virtual-Routing-and-Forwarding-VRF/),
including a [management VRF](/cumulus-linux/Layer-3/Management-VRF/).
To do so, you need to specify the VRF name when configuring the NetQ
Agent. For example, if the management VRF is configured and you want the
agent to communicate with the NetQ Platform over it, configure the agent
like this:

    cumulus@leaf01:~$ netq config add agent server 192.168.1.254 vrf mgmt
    cumulus@leaf01:~$ netq config add cli server 192.168.254 vrf mgmt

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent
    cumulus@leaf01:~$ netq config restart cli

### Configure the Agent to Communicate over a Specific Port

By default, NetQ uses port 8981 for communication between the NetQ
Platform and NetQ Agents. If you want the NetQ Agent to communicate with
the NetQ Platform via a different port, you need to specify the port
number when configuring the NetQ Agent like this:

    cumulus@switch:~$ netq config add agent server 192.168.1.254 port 7379

You then restart the agent:

    cumulus@leaf01:~$ netq config restart agent

## Upgrade Tips

After you have upgraded NetQ, if you find that some issues remain,
review these commonly encountered scenarios. If NetQ is still not
operating as expected, please open a [support
ticket](https://cumulusnetworks.com/support/file-a-ticket/) with a
detailed description of your issues.

### Scenario 1: NetQ Appliance IP Address Was Changed

The NetQ Appliance came with a pre-configured IP address, which has
since been changed. How do I recover the system?

 You must remove and reconfigure the
Kubernetes configuration. Follow these steps:

1.  Locate the Kubernetes pods.
    
        cumulus@switch:~$ kubectl get pods

2.  Reset all Kubernetes administrative settings. Run the command twice
    to make sure all directories and files have been reset.
    
        cumulus@switch:~$ sudo kudeadm reset -f 
        cumulus@switch:~$ sudo kudeadm reset -f

3.  Remove the Kubernetes configuration.
    
        cumulus@switch:~$ sudo rm /home/cumulus/.kube/config

4.  Reset the NetQ Appliance install daemon.
    
        cumulus@switch:~$ sudo systemctl reset-failed

5.  Reset the Kubernetes service.
    
        cumulus@switch:~$ sudo systemctl restart cts-kubectl-config 
    
    {{%notice note%}}
    
Allow 15 minutes for the prompt to return.
    
    {{%/notice%}}

### Scenario 2: No IP Address Assigned to the NetQ Appliance on Boot

A user did not configure an IP address when the system was first booted.
Later the user assigned an IP address to eth0, but the NetQ appliance
does not appear to be functioning.

You must reset the install daemon and restart the Kubernetes service.
Follow these steps:

1.  Reset the NetQ Appliance install daemon.
    
        cumulus@switch:~$ sudo systemctl reset-failed

2.  Restart the Kubernetes service.
    
        cumulus@switch:~$ sudo systemctl restart cts-kubectl-config
