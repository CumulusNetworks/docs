---
title: Upgrading NetQ
author: Cumulus Networks
weight: 49
aliases:
 - /display/NETQ121/Upgrading-NetQ
 - /pages/viewpage.action?pageId=8356543
pageID: 8356543
product: Cumulus NetQ
version: 1.2.1
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
This section covers the process for upgrading NetQ. The upgrade process
involves upgrading each of the various components of NetQ (the NetQ
Telemetry Server, and both the host and Cumulus Linux agents), and then
connecting the upgraded NetQ Telemetry Server to the network.

{{%notice info%}}

Cumulus Networks recommends only upgrading NetQ during a network
maintenance window.

{{%/notice%}}

{{%notice warning%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the agents will re-sync
with the current state of the Host or Cumulus Linux switch with the
Telemetry server.

{{%/notice%}}

Before upgrading NetQ, consider the following:

  - The minimum supported Cumulus Linux version for NetQ 1.2 is 3.3.2.

  - You can upgrade to NetQ 1.2 without upgrading Cumulus Linux.

## <span>Upgrade the NetQ Telemetry Server</span>

{{%notice note%}}

To install a new instance of NetQ, refer to the [Getting Started with
NetQ](/version/cumulus-netq-121/Getting-Started-with-NetQ/) chapter.

{{%/notice%}}

1.  Back up the current NetQ Telemetry Server data. For instructions,
    refer to the [NetQ
    backup](/version/cumulus-netq-121/Restoring-from-Backups-with-NetQ)
    chapter.

2.  Shut down the connectivity from the agents to the current NetQ
    Telemetry Server.
    
    {{%notice warning%}}
    
    This step is required to ensure agents don't attempt to communicate
    with the Telemetry Server during the maintenance window.
    
    {{%/notice%}}

3.  Shut down the current NetQ Telemetry Server.

4.  Start the new NetQ Telemetry Server.

5.  Restore the data to the new NetQ Telemetry Server. For instructions,
    refer to the [NetQ
    backup](/version/cumulus-netq-121/Restoring-from-Backups-with-NetQ)
    chapter.
    
    {{%notice info%}}
    
    This step can be skipped, if there is no desire to retain the
    previous data. NetQ agents will re-populate the current data once
    they connect to the new NetQ Telemetry Server.
    
    {{%/notice%}}

6.  Validate that the telemetry server is up and running:
    
        cumulus@switch:~$ cat /etc/app-release
        APPLIANCE_VERSION=1.2.0

{{%notice note%}}

Cumulus Networks recommends that the NetQ Agents remain disconnected
from the NetQ Telemetry Server until they have been upgraded to the
current version of NetQ as well.

{{%/notice%}}

## <span>Upgrade the NetQ Agents</span>

Follow the steps for the relevant OS below to upgrade the NetQ Agents:

### <span>Cumulus Linux</span>

1.  Open the `/etc/apt/sources.list` file in a text editor.

2.  Add the following line, and save the file:
    
        cumulus@switch:~$ deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-1.2

3.  Install the `cumulus-netq` metapack and its components:
    
        cumulus@switch:~$ sudo apt-get update && apt-get install cumulus-netq

### <span>Ubuntu 16.04</span>

1.  Use the `wget` tool to retrieve the public key:
    
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-host-ubuntu.pubkey | apt-key add

2.  Open the `/etc/apt/sources.list` file in a text editor.

3.  Add the following line, and save the file:
    
        root@ubuntu:~# deb https://apps3.cumulusnetworks.com/repos/deb xenial netq-1.2

4.  Install the `cumulus-netq` metapack and its components:
    
        root@ubuntu:~# sudo apt-get update && apt-get install cumulus-netq
    
    When you see the following prompt, type *N* to keep your current
    version:
    
        Configuration file '/etc/netq/netq.yml'
         ==> File on system created by you or by a script.
         ==> File also in package provided by package maintainer.
           What would you like to do about it ?  Your options are:
            Y or I  : install the package maintainer's version
            N or O  : keep your currently-installed version
              D     : show the differences between the versions
              Z     : start a shell to examine the situation

### <span>Red Hat Enterprise Linux 7 / CentOS 7</span>

{{%notice warning%}}

If you are upgrading from NetQ 1.1 to 1.2 only, you must remove the
Cumulus NetQ packages before installing the new version.

    root@rhel7:~# yum remove netq-apps netq-agent cumulus-netq

{{%/notice%}}

To install the NetQ Agent on a Red Hat or CentOS host, do the following:

1.  Import the public key:
    
        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-host-el.pubkey

2.  Open `/etc/yum.repos.d/cumulus-host-el.repo` in a text editor.

3.  Define the repository source, and save the file:
    
        [cumulus-arch]
        name=Cumulus Packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.2/$basearch
        gpgcheck=1
        enabled=1
         
        [cumulus-noarch]
        name=Architecture-independent Cumulus packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.2/noarch
        gpgcheck=1
        enabled=1
         
        [cumulus-src]
        name=Cumulus source packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.2/src
        gpgcheck=1
        enabled=1

4.  Install the `cumulus-netq` metapack and its components:
    
        root@rhel7:~# yum install cumulus-netq

## <span>Connect the NetQ Telemetry Server to the Network</span>

1.  Once the NetQ Telemetry Server and NetQ agents have been upgraded,
    connect the NetQ Telemetry Server to the network. For more
    information, refer to the [Getting Started with
    NetQ](/version/cumulus-netq-121/Getting-Started-with-NetQ/) chapter.

2.  Verify the NetQ Agents are OK, and running NetQ 1.2. The output
    should show the version as `1.2-cl3u5` for NetQ 1.2:
    
        cumulus@switch:~$ netq show agents

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
