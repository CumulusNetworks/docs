---
title: Upgrading NetQ
author: Cumulus Networks
weight: 47
aliases:
 - /display/NETQ110/Upgrading-NetQ
 - /pages/viewpage.action?pageId=7111302
pageID: 7111302
product: Cumulus NetQ
version: 1.1.0
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
---
This section covers the process for upgrading NetQ. The upgrade process
involves upgrading each of the various components of NetQ (the NetQ
Telemetry Server, and both the Host and Cumulus Linux Agents), and then
connecting the upgraded NetQ Telemetry Server to the network.

{{%notice info%}}

Cumulus Networks recommends only upgrading NetQ during a maintenance
window.

{{%/notice%}}

{{%notice warning%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the agents will re-sync
with the current state of the Host or Cumulus Linux switch with the
Telemetry server.

{{%/notice%}}

Before upgrading NetQ, consider the following information:

  - The minimum supported Cumulus Linux version for NetQ 1.1 is 3.3.0.

  - NetQ 1.0 can be upgraded to NetQ 1.1 without upgrading Cumulus
    Linux.

{{%notice note%}}

NetQ 1.1 will be supported on Cumulus Linux 3.4.0 and future releases
until the next NetQ version is released.

{{%/notice%}}

## <span>Upgrade the NetQ Telemetry Server</span>

{{%notice note%}}

To install a new instance of NetQ, refer to the [Getting Started with NetQ](/version/cumulus-netq-110/Getting-Started-with-NetQ/)
documentation.

{{%/notice%}}

1.  Back up the current NetQ Telemetry Server data. For instructions,
    refer to the [NetQ Backup](/version/cumulus-netq-110/Restoring-from-Backups-with-NetQ/)
    documentation.

2.  Shutdown the connectivity from the agents to the current NetQ
    Telemetry Server.

    {{%notice warning%}}

    This step is required to ensure agents don't attempt to communicate
    with the Telemetry Server during the maintenance window.

    {{%/notice%}}

3.  Shutdown the current NetQ Telemetry Server.

4.  Start the new NetQ Telemetry Server.

5.  Restore the data to the new NetQ Telemetry Server. For instructions,
    refer to the [NetQ Backup](/version/cumulus-netq-110/Restoring-from-Backups-with-NetQ/)
    documentation.

    {{%notice info%}}

    This step can be skipped, if there is no desire to retain the
    previous data. NetQ agents will re-populate the current data once
    they connect to the new NetQ Telemetry Server.

    {{%/notice%}}

6.  Validate that the telemetry server is up and running:

        cumulus@switch:~$ cat /etc/app-release
        APPLIANCE_VERSION=1.1.0

{{%notice note%}}

Cumulus Networks recommends that the NetQ Agents remain disconnected
from the NetQ Telemetry Server until they have been upgraded to NetQ 1.1
as well.

{{%/notice%}}

{{%notice warning%}}

The NetQ Notifier configuration syntax has changed between versions 1.0
and 1.1. Examples of the new syntax are in the [getting started guide](/version/cumulus-netq-110/Getting-Started-with-NetQ/).

{{%/notice%}}

## <span>Upgrade the NetQ Agents</span>

Follow the steps for the relevant OS below to upgrade the NetQ Agents:

### <span>Cumulus Linux</span>

1.  Open the `/etc/apt/sources.list` file in a text editor.

2.  Add the following line, and save the file:

        deb     https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-1.1

3.  Install the `cumulus-netq` metapack and its components:

        cumulus@switch:~$ sudo apt-get update && apt-get install cumulus-netq

### <span>Ubuntu 16.04</span>

1.  Use the `wget` tool to retrieve the public key:

        cumulus@switch:~$ wget -O - https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | sudo apt-key add -

2.  Open the `/etc/apt/sources.list` file in a text editor.

3.  Add the following line, and save the file:

        deb     https://apps3.cumulusnetworks.com/repos/deb xenial netq-1.1

4.  Install the `cumulus-netq` metapack and its components:

        cumulus@switch:~$ sudo apt-get update && apt-get install cumulus-netq

### <span>Red Hat Enterprise Linux 7 / CentOS 7</span>

1.  Import the public key:

        cumulus@switch:~$ sudo rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-host-el.pubkey

2.  Open `/etc/yum.repos.d/cumulus-host-el.repo` in a text editor.

3.  Define the repository source, and save the file:

        [cumulus-arch]
        name=Cumulus Packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.1/$basearch
        gpgcheck=1
        enabled=1
         
         
        [cumulus-noarch]
        name=Architecture-independent Cumulus packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.1/noarch
        gpgcheck=1
        enabled=1
         
        [cumulus-src]
        name=Cumulus source packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.1/src
        gpgcheck=1
        enabled=1

4.  Install the `cumulus-netq` metapack and its components:

        cumulus@switch:~$ sudo yum install cumulus-netq

## <span>Connect the NetQ Telemetry Server to the Network</span>

1.  Once the NetQ Telemetry Server and NetQ agents have been upgraded,
    connect the NetQ Telemetry Server to the network. For more
    information, refer to the [Getting Started](/version/cumulus-netq-110/Getting-Started-with-NetQ/)
    documentation.

2.  Verify the NetQ Agents are OK, and running NetQ 1.1. The output
    should show the version as `1.1-cl3u5` for NetQ 1.1:

        cumulus@switch:~$ netq show agents
