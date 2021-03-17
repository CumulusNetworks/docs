---
title: Getting Started with SONiC
author: Cumulus Networks
weight: 30
product: SONiC
version: 4.0
siteSlug: sonic
---

## Configuring the Switch for the First Time

The procedures described in this page assume that you have already installed and powered on your switch according to the instructions in the Hardware Installation Guide, which was shipped with the product.

### Using the RJ-45 Console

1. Connect the host PC to the console (RJ-45) port of the switch system using the supplied cable.

   Make sure to connect to the console RJ-45 port of the switch and not to the MGT port.
2. Configure a serial terminal with the settings described below:

   Baud Rate might be different based on BIOS/ONIE.

   | Parameter | Setting |
   | --------- | ------- |
   | Baud Rate | 115200 |
   | Data bits | 8 |
   | Flow Control | None |
   | Parity | None |
   | Stop bits | 1 |

### Via the Management IP

DHCP is enabled by default over the MGT port. Therefore, if you have configured your DHCP server and connected an RJ-45 cable to the MGT port, simply log in using the designated IP address.

## Installing SONiC Image

The switch may be received with ONIE or another OS pre-installed. In order to install SONiC on it, the prerequisites below must be applied prior to installing the SONiC software.

### Prerequisites

Using older platforms prior to 201811 might require BIOS and ONIE versions upgrade. For instructions, please contact Mellanox Support.

1. Verify your model is supported. See https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms.
2. Connect to the switch via the serial console.
3. If the switch has NOS installed, uninstall the existing NOS first before installing SONiC. To do so, simply boot into ONIE and select 'Uninstall OS':

       GNU GRUB version 2.02-beta3
       +-----------------------------------
       | ONIE: Install OS
       | ONIE: Rescue
       | *ONIE: Uninstall OS
       | ONIE: Update ONIE
       | ONIE: Embed ONIE

4. Reboot the switch into ONIE and select 'Install OS'
5. A discovery process starts automatically, trying to search for the OS to install. Stop the ONIE discovery by running:

       onie-stop
6. Verify SMIBIOS params by running:

       dmidecode -t1 -t2 | grep "Product Name"
       Product Name: MSN2700
       Product Name: VMOD0001

If the output is like the example below, please contact Mellanox Support to correct the settings.

Product Name: Mellanox switch

Product Name: Mellanox x86 SFF board

### Installing SONiC

1. Reboot the switch into ONIE and select 'Install OS':

       GNU GRUB version 2.02-beta3
       +-----------------------------------
       | *ONIE: Install OS
       | ONIE: Rescue
       | ONIE: Uninstall OS
       | ONIE: Update ONIE
       | ONIE: Embed ONIE

2. Download the latest SONiC image from LatestSuccessfulBuild.

   The latest successful build might not be fully tested.

   It is recommended to contact Mellanox Support to receive the latest approved hash for production.

   - If a specific image is required, download it from here
   - Check the installation process suitable for you from the list described here.<br />For example: Copying the image to the switch and running 'onie-nos-install <PATH/sonic-mellanox.bin>'.

   When NOS installation is completed, the switch will reboot into SONiC by default as shown in the example below:

       GNU GRUB version 2.02-beta3
       +----------------------------------
       |*SONiC-05-HEAD.517-6045235
       |ONIE

3. Log into SONiC. First time credentials:

   - Use username: admin
   - Password: YourPaSsWoRd

4. Verify the current image version.

       switch:~$ show version
       SONIC Software Version: SONiC-05-HEAD.517-6045235 
       Distribution: Debian 8.10
       Kernel: 3.16.0-5-amd64
       BLAU commit: fcbbb8a
       Build date: Fri Apr 13 08:47:39 UTC 2018 
       Built by johnar@jenkins-worker-3

5. Verify the platform type.

       switch:~$ show platform summary
       Platform: x86_64-mlnx_msn2700-r0
       HWSKU: ACS-MSN2700
       ASIC: mellanox

6. Verify that all the Docker Containers are running.

   The list in the example below is basic and more containers can be loaded based on the user system's configuration.

   It might take up to 2 minutes for the full list of running containers and interfaces to show up.

       admin@arc-switch1004:~$ docker ps
       CONTAINER ID    IMAGE               COMMAND         CREATED       STATUS       PORTS        NAMES
       a3a07e51496a    docker-snmp-sv2:latest      "/usr/bin/supervisord"  2 days ago     Up 31 hours               snmp
       ae43e4647d75    docker-sonic-telemetry:latest   "/usr/bin/supervisord"  2 days ago     Up 31 hours               telemetry
       b17ee8a690d3    docker-sflow:latest        "/usr/bin/supervisord"  2 days ago     Up 31 hours               sflow
       b42f3b285b11    docker-dhcp-relay:latest     "/usr/bin/docker_ini…"  2 days ago     Up 31 hours               dhcp_relay
       40c86af713ff    docker-router-advertiser:latest  "/usr/bin/supervisord"  2 days ago     Up 31 hours               radv
       53144ca433b5    docker-lldp-sv2:latest      "/usr/bin/docker-lld…"  2 days ago     Up 31 hours               lldp
       5b712bdcb50f    docker-nat:latest         "/usr/bin/supervisord"  2 days ago     Up 31 hours               nat
       41accfbb0e8d    docker-platform-monitor:latest  "/usr/bin/docker_ini…"  2 days ago     Up 31 hours               pmon
       39e692bb8de4    docker-syncd-mlnx:latest     "/usr/bin/supervisord"  2 days ago     Up 31 hours               syncd
       715e3dc0eff1    docker-teamd:latest        "/usr/bin/supervisord"  2 days ago     Up 31 hours               teamd
       3098d062178c    docker-orchagent:latest      "/usr/bin/supervisord"  2 days ago     Up 31 hours               swss
       4ce804c17fa4    docker-fpm-frr:latest       "/usr/bin/supervisord"  2 days ago     Up 31 hours               bgp
       918e27ea0f9b    docker-database:latest      "/usr/local/bin/dock…"  2 days ago     Up 31 hours               database

7. Verify the interfaces status.

       admin@arc-switch1004:~$ show interfaces status
       Interface      Lanes  Speed  MTU  Alias       Vlan  Oper  Admin       Type  Asym PFC
       --------------- --------------- ------- ----- ------- --------------- ------ ------- --------------- ----------
       Ethernet0       0,1   50G  9100  etp1a PortChannel0002   up    up  QSFP+ or later     off
       Ethernet2       2,3   50G  9100  etp1b PortChannel0002   up    up  QSFP+ or later     off
       Ethernet4       4,5   50G  9100  etp2a PortChannel0005   up    up  QSFP+ or later     off
       Ethernet6       6,7   50G  9100  etp2b PortChannel0005   up    up  QSFP+ or later     off
       Ethernet8       8,9   50G  9100  etp3a PortChannel0008   up    up  QSFP+ or later     off
       Ethernet10      10,11   50G  9100  etp3b PortChannel0008   up    up  QSFP+ or later     off
       Ethernet12      12,13   50G  9100  etp4a PortChannel0011   up    up  QSFP+ or later     off
       Ethernet14      14,15   50G  9100  etp4b PortChannel0011   up    up  QSFP+ or later     off
       Ethernet16      16,17   50G  9100  etp5a PortChannel0014   up    up  QSFP+ or later     off
       Ethernet18      18,19   50G  9100  etp5b PortChannel0014   up    up  QSFP+ or later     off
       Ethernet20      20,21   50G  9100  etp6a PortChannel0017   up    up  QSFP+ or later     off
       Ethernet22      22,23   50G  9100  etp6b PortChannel0017   up    up  QSFP+ or later     off
       Ethernet24   24,25,26,27   100G  9100   etp7 PortChannel0020   up    up  QSFP+ or later     off
       Ethernet28   28,29,30,31   100G  9100   etp8 PortChannel0020   up    up  QSFP+ or later     off

By default, all physical ports (etpXX) should be shown. The number of ports depends on the system you are using.

- For SN2700 32 ports (etp1-etp32) are expected
- For SN2100 16 ports (etp1-etp16) are expected

If the SKU includes split ports, the {a/b/c/d} will be added to the physical port name (for example: Splitting etp12 to 2, instead of etp12 the ports will be etp12a and etp12b).

If NO interfaces are showing, it might indicate missing/wrong `/etc/sonic/config_db.json`, an issue with the syncd container or failure to process `port_config.ini/minigraph/config_db.json/etc`.
