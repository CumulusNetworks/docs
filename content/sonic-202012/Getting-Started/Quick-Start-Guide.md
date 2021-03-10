---
title: Quick Start Guide
author: Cumulus Networks
weight: 110
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

This topic assumes you are configuring SONiC for the first time and have already installed and powered on your switch according to the instructions in the hardware installation guide that shipped with the switch.

## Prepare to Install the SONiC Image

The switch may already have ONIE or another network operating system installed. In order to install SONiC on it, follow the preparatory steps below before you start installing SONiC.

Using a SONiC release earlier than 201811 might require upgrades to the BIOS and ONIE. For instructions, please contact your switch manufacturer.

1. Verify your switch model is {{<exlink url="https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms" text="supported">}}.
1. Connect to the switch via the serial console.
1. If the switch has a network operating system installed, uninstall the existing NOS first before installing SONiC. To do so, simply boot into ONIE and select **Uninstall OS**:

       GNU GRUB version 2.02-beta3
       +-----------------------------------
       | ONIE: Install OS
       | ONIE: Rescue
       | *ONIE: Uninstall OS
       | ONIE: Update ONIE
       | ONIE: Embed ONIE

1. Reboot the switch into ONIE and select **Install OS**.
1. A discovery process starts automatically, searching for the OS to install. Stop the ONIE discovery by running:

       $ onie-stop
1. Verify SMIBIOS parameters by running:

       $ dmidecode -t1 -t2 | grep "Product Name"
       Product Name: MSN2700
       Product Name: VMOD0001

### Install Using the RJ-45 Console

1. Connect the host PC to the console (RJ-45) port of the switch system using the supplied cable.

   {{%notice info%}}

   Make sure to connect to the console RJ-45 port of the switch and not to the management port.

   {{%/notice%}}

2. Configure a serial terminal with the settings described below:

   The baud rate might be different based on the BIOS or ONIE version.

   | Parameter | Setting |
   | --------- | ------- |
   | Baud Rate | 115200 |
   | Data bits | 8 |
   | Flow Control | None |
   | Parity | None |
   | Stop bits | 1 |

### Install Using the Management IP

DHCP is enabled by default over the management port. Therefore, if you configured your DHCP server and connected an RJ-45 cable to the management port, you can log in using the designated IP address.

## Install SONiC

1. Reboot the switch into ONIE and select **Install OS**:

       GNU GRUB version 2.02-beta3
       +-----------------------------------
       | *ONIE: Install OS
       | ONIE: Rescue
       | ONIE: Uninstall OS
       | ONIE: Update ONIE
       | ONIE: Embed ONIE

2. Download the latest SONiC image from the {{<exlink url="https://sonic-jenkins.westus2.cloudapp.azure.com/job/mellanox/job/buildimage-mlnx-all/lastSuccessfulBuild/artifact/target/sonic-mellanox.bin" text="Last Successful Build">}} page.

   {{%notice info%}}

   The latest successful build might not be fully tested.

   It is recommended to contact your switch manufacturer's support team to receive the latest approved hash for production.

   {{%/notice%}}

   - If you need a different version than the latest, download it from {{<exlink url="https://sonic-jenkins.westus2.cloudapp.azure.com/job/mellanox/job/buildimage-mlnx-all/" text="here">}}.
   - Decide which installation process to follow from the list described on the {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html" text="ONIE website">}}. For example, copying the image to the switch and running `onie-nos-install <PATH/sonic-mellanox.bin>`.

   When the NOS installation completes, the switch reboots into SONiC by default, as shown here:

       GNU GRUB version 2.02-beta3
       +----------------------------------
       |*SONiC-05-HEAD.517-6045235
       |ONIE

3. Log into SONiC. The default login credentials are:

   - Username: *admin*
   - Password: *YourPaSsWoRd*

4. Verify the current image version.

       admin@leaf01:~$ show version

       SONiC Software Version: SONiC.201911.202-c453381a
       Distribution: Debian 9.13
       Kernel: 4.9.0-11-2-amd64
       Build commit: c453381a
       Build date: Tue Nov 10 07:40:20 UTC 2020
       Built by: johnar@jenkins-worker-7

       Platform: x86_64-mlnx_msn2700-r0
       HWSKU: ACS-MSN2700
       ASIC: mellanox
       Serial Number: 000000
       Uptime: 04:14:22 up 1 day,  2:25,  1 user,  load average: 2.05, 2.96, 3.33

5. Verify the platform type.

       switch:~$ show platform summary
       Platform: x86_64-mlnx_msn2700-r0
       HWSKU: ACS-MSN2700
       ASIC: mellanox

6. Verify that all the Docker containers are running.

   The list in the example below is basic and more containers can be loaded based on the user system's configuration.

   It might take up to 2 minutes for the full list of running containers and interfaces to appear.

       admin@leaf01:~$ docker ps
       CONTAINER ID        IMAGE                             COMMAND                  CREATED             STATUS              PORTS               NAMES
       7693970157e4        docker-sonic-telemetry:latest     "/usr/bin/supervisord"   26 hours ago        Up 26 hours                             telemetry
       1346bf47d5aa        docker-snmp-sv2:latest            "/usr/bin/supervisord"   26 hours ago        Up 26 hours                             snmp
       b4927925be4a        docker-router-advertiser:latest   "/usr/bin/docker-ini…"   26 hours ago        Up 26 hours                             radv
       fd4006a177d1        docker-dhcp-relay:latest          "/usr/bin/docker_ini…"   26 hours ago        Up 26 hours                             dhcp_relay
       d90bf65d463f        docker-lldp-sv2:latest            "/usr/bin/docker-lld…"   26 hours ago        Up 26 hours                             lldp
       7e1c5217eff3        docker-syncd-vs:latest            "/usr/bin/supervisord"   4 days ago          Up 26 hours                             syncd
       dcede1ab4ac0        docker-teamd:latest               "/usr/bin/supervisord"   4 days ago          Up 26 hours                             teamd
       8e3c153cafdb        docker-orchagent:latest           "/usr/bin/docker-ini…"   4 days ago          Up 26 hours                             swss
       cdeb016623c5        docker-fpm-frr:latest             "/usr/bin/supervisord"   7 days ago          Up 26 hours                             bgp
       2f6ac855e3e1        docker-platform-monitor:latest    "/usr/bin/docker_ini…"   7 days ago          Up 26 hours                             pmon
       77917d9efb8a        docker-database:latest            "/usr/local/bin/dock…"   7 days ago          Up 26 hours                             database

7. Verify the status of the interfaces.

       admin@leaf01:~$ show interfaces status
         Interface            Lanes    Speed    MTU    FEC           Alias    Vlan    Oper    Admin    Type    Asym PFC
       -----------  ---------------  -------  -----  -----  --------------  ------  ------  -------  ------  ----------
         Ethernet0      25,26,27,28      40G   9216    N/A    fortyGigE0/0   trunk      up       up     N/A         N/A
         Ethernet4      29,30,31,32      40G   9216    N/A    fortyGigE0/4   trunk      up       up     N/A         N/A
         Ethernet8      33,34,35,36      40G   9216    N/A    fortyGigE0/8   trunk      up       up     N/A         N/A
        Ethernet12      37,38,39,40      40G   9216    N/A   fortyGigE0/12  routed      up       up     N/A         N/A
        Ethernet16      45,46,47,48      40G   9216    N/A   fortyGigE0/16  routed      up       up     N/A         N/A
        Ethernet20      41,42,43,44      40G   9216    N/A   fortyGigE0/20  routed      up       up     N/A         N/A
        Ethernet24          1,2,3,4      40G   9216    N/A   fortyGigE0/24  routed      up       up     N/A         N/A
        Ethernet28          5,6,7,8      40G   9216    N/A   fortyGigE0/28  routed      up       up     N/A         N/A
        Ethernet32      13,14,15,16      40G   9216    N/A   fortyGigE0/32  routed      up       up     N/A         N/A
        Ethernet36       9,10,11,12      40G   9216    N/A   fortyGigE0/36  routed    down       up     N/A         N/A
        Ethernet40      17,18,19,20      40G   9216    N/A   fortyGigE0/40  routed    down       up     N/A         N/A
        Ethernet44      21,22,23,24      40G   9216    N/A   fortyGigE0/44  routed    down       up     N/A         N/A
        Ethernet48      53,54,55,56      40G   9216    N/A   fortyGigE0/48  routed    down       up     N/A         N/A
        Ethernet52      49,50,51,52      40G   9216    N/A   fortyGigE0/52  routed    down       up     N/A         N/A
        Ethernet56      57,58,59,60      40G   9216    N/A   fortyGigE0/56  routed    down       up     N/A         N/A
        Ethernet60      61,62,63,64      40G   9216    N/A   fortyGigE0/60  routed    down       up     N/A         N/A
        Ethernet64      69,70,71,72      40G   9216    N/A   fortyGigE0/64  routed    down       up     N/A         N/A
        Ethernet68      65,66,67,68      40G   9216    N/A   fortyGigE0/68  routed    down       up     N/A         N/A
        Ethernet72      73,74,75,76      40G   9216    N/A   fortyGigE0/72  routed    down       up     N/A         N/A
        Ethernet76      77,78,79,80      40G   9216    N/A   fortyGigE0/76  routed    down       up     N/A         N/A
        Ethernet80  109,110,111,112      40G   9216    N/A   fortyGigE0/80  routed    down       up     N/A         N/A
        Ethernet84  105,106,107,108      40G   9216    N/A   fortyGigE0/84  routed    down       up     N/A         N/A
        Ethernet88  113,114,115,116      40G   9216    N/A   fortyGigE0/88  routed    down       up     N/A         N/A
        Ethernet92  117,118,119,120      40G   9216    N/A   fortyGigE0/92  routed    down       up     N/A         N/A
        Ethernet96  125,126,127,128      40G   9216    N/A   fortyGigE0/96  routed    down       up     N/A         N/A
       Ethernet100  121,122,123,124      40G   9216    N/A  fortyGigE0/100  routed    down       up     N/A         N/A
       Ethernet104      81,82,83,84      40G   9216    N/A  fortyGigE0/104  routed    down       up     N/A         N/A
       Ethernet108      85,86,87,88      40G   9216    N/A  fortyGigE0/108  routed    down       up     N/A         N/A
       Ethernet112      93,94,95,96      40G   9216    N/A  fortyGigE0/112  routed    down       up     N/A         N/A
       Ethernet116      89,90,91,92      40G   9216    N/A  fortyGigE0/116  routed    down       up     N/A         N/A
       Ethernet120  101,102,103,104      40G   9216    N/A  fortyGigE0/120  routed    down       up     N/A         N/A
       Ethernet124     97,98,99,100      40G   9216    N/A  fortyGigE0/124  routed    down       up     N/A         N/A

By default, all physical ports (etpXX) should be shown. The number of ports depends on the system you are using.

{{%notice tip%}}

If the SKU includes split ports, then a lowercase letter (*a*, *b*, *c*, *d*) is appended to the physical port alias. For example, if port etp12 is split in two, the resulting ports are named *etp12a* and *etp12b*.

{{%/notice%}}

If no interfaces are showing, it might indicate one of the following:

- The `/etc/sonic/config_db.json` file is missing or was misconfigured.
- There is an issue with the `syncd` container.
- There was a failure to process `port_config.ini/minigraph/config_db.json/etc`.
