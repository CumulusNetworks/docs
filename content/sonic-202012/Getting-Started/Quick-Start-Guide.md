---
title: Quick Start Guide
author: NVIDIA
weight: 110
product: SONiC
version: 202012
siteSlug: sonic
---

This topic assumes you are configuring SONiC for the first time and have already installed and powered on your switch according to the instructions in the hardware installation guide that shipped with the switch.

## Install SONiC

1. Reboot the switch into ONIE and select **ONIE: Install OS**:

       GNU GRUB version 2.02-beta3
       +-----------------------------------
       | *ONIE: Install OS
       | ONIE: Rescue
       | ONIE: Uninstall OS
       | ONIE: Update ONIE
       | ONIE: Embed ONIE

1. Download the SONiC disk image. If you want an NVIDIA Mellanox version of SONiC, download it from the {{<exlink url="https://sonic-jenkins.westus2.cloudapp.azure.com/job/mellanox/job/buildimage-mlnx-all/" text="Azure website">}}.

1. Decide which installation process to follow from the list described in {{<link url="Installation-Management">}}. For example, copying the image to the switch and running `onie-nos-install <PATH/sonic-mellanox.bin>`.

   When the NOS installation completes, the switch reboots into SONiC by default, as shown here:

       GNU GRUB version 2.02-beta3
       +----------------------------------
       |*SONiC-05-HEAD.517-6045235
       |ONIE

1. Log into SONiC. The {{<link url="#default-credentials" text="default login credentials">}} are:

   - Username: *admin*
   - Password: *YourPaSsWoRd*

1. Verify the current image version.

       admin@switch:~$ show version

       SONiC Software Version: SONiC.202012.15-cb79de1b
       Distribution: Debian 10.7
       Kernel: 4.19.0-9-2-amd64
       Build commit: cb79de1b
       Build date: Sat Jan 30 11:14:42 UTC 2021
       Built by: johnar@jenkins-worker-11

       Platform: x86_64-mlnx_msn2700-r0
       HWSKU: ACS-MSN2700
       ASIC: mellanox
       Serial Number: 000000
       Uptime: 04:14:22 up 1 day,  2:25,  1 user,  load average: 2.05, 2.96, 3.33

1. Verify the platform type.

       switch:~$ show platform summary
       Platform: x86_64-mlnx_msn2700-r0
       HWSKU: ACS-MSN2700
       ASIC: mellanox

1. Verify that all the Docker containers are running.

   The list in the example below is the default. More containers can be loaded based on the user system's configuration.

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

1. Verify the status of the interfaces.

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

By default, all physical ports (Ethernet##) should appear. The number of ports depends on the system you are using.

{{%notice tip%}}

If the SKU includes split ports, then a lowercase letter (*a*, *b*, *c*, *d*) is appended to the physical port alias. For example, if port Ethernet12 is broken out to two ports, the resulting ports are named *fortyGigE0/12a* and *fortyGigE0/12b*.

{{%/notice%}}

If no interfaces are showing, it might indicate one of the following:

- The `/etc/sonic/config_db.json` file is missing or was misconfigured.
- There is an issue with the `syncd` container.
- There was an error processing a configuration file such as `port_config.ini` or `config_db.json`.

## Default Credentials

All SONiC switches support both serial console-based login and SSH-based login by default. The default credentials to log in (if you did not modify when you built the SONiC image) is *admin*/*YourPaSsWoRd*.

For SSH login, you can log in to the management interface (eth0) IP address after configuring the it using the serial console. Refer the next section for configuring the IP address for management interface.

You can add new users with the Linux `useradd` command. You manage passwords with the Linux `passwd` command.

## Configure Using CLI or JSON

You configure SONiC in one of two ways:

- Using the SONiC CLI. SONiC includes a broad range of `config` commands that configure almost every feature in the operating system. Changes made using the CLI are applied to a running configuration that does not persist after you reboot the switch, unless you save the configuration with `config save`. The Azure GitHub documentation contains a {{<exlink url="https://github.com/Azure/sonic-utilities/blob/master/doc/Command-Reference.md" text="command reference">}}, and you can also run `config ?` to list all the configuration commands available:

  {{<expand "config ? Output">}}

  ```
  admin@ibm-2700-01:~$ sudo config ?
  Usage: config [OPTIONS] COMMAND [ARGS]...

    SONiC command line - 'config' command

  Options:
    -?, -h, --help  Show this message and exit.

  Commands:
    aaa                    AAA command line
    acl                    ACL-related configuration tasks
    bgp                    BGP-related configuration tasks
    buffer                 Configure buffer_profile
    chassis-modules        Configure chassis-modules options
    console                Console-related configuration tasks
    dropcounters           Drop counter related configuration tasks
    ecn                    ECN-related configuration tasks
    feature                Configure features
    hostname               Change device hostname without impacting the...
    interface              Interface-related configuration tasks
    interface_naming_mode  Modify interface naming mode for interacting with...
    kdump                  Configure kdump
    kubernetes             kubernetes command line
    load                   Import a previous saved config DB dump file.
    load_mgmt_config       Reconfigure hostname and mgmt interface based on...
    load_minigraph         Reconfigure based on minigraph.
    loopback               Loopback-related configuration tasks
    mirror_session
    muxcable               SONiC command line - 'show muxcable' command
    nat                    NAT-related configuration tasks
    ntp                    NTP server configuration tasks
    pfcwd                  Configure pfc watchdog
    platform               Platform-related configuration tasks
    portchannel
    qos                    QoS-related configuration tasks
    reload                 Clear current configuration and import a previous...
    route                  route-related configuration tasks
    save                   Export current config DB to a file on disk.
    sflow                  sFlow-related configuration tasks
    snmpagentaddress       SNMP agent listening IP address, port, vrf...
    snmptrap               SNMP Trap server configuration to send traps
    synchronous_mode       Enable or disable synchronous mode between...
    syslog                 Syslog server configuration tasks
    tacacs                 TACACS+ server configuration
    vlan                   VLAN-related configuration tasks
    vrf                    VRF-related configuration tasks
    vxlan
    warm_restart           warm_restart-related configuration tasks
    watermark              Configure watermark
    ztp                    Configure Zero Touch Provisioning
  ```
  {{</expand>}}
- Editing the SONiC CONFIG_DB JSON configuration file `config_db.json` directly. To apply your changes, reload the configuration with `config reload`.

### Show the Running Configuration

A *running configuration* is a combination of the startup configuration that loads when you boot the switch, plus any updates that are made to the configuration that are not committed to CONFIG_DB (that is, they're not saved to the configuration with `config save`).

The `show runningconfiguration all` command shows the current running state of the `config_db.json` file.

{{<expand "Show Running Configuration">}}

```
admin@switch:~$ show runningconfiguration all
{
    "ACL_TABLE": {
        "L3_INGRESS_1": {
            "policy_desc": "L3 ingress rule",
            "ports": [
                "Ethernet0",
                "Ethernet124",
                "PortChannel0001"
            ],
            "stage": "ingress",
            "type": "L3"
        }
    },
    "BGP_NEIGHBOR": {
        "10.0.0.1": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.0",
            "name": "ARISTA01T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.3": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.2",
            "name": "ARISTA02T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.5": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.4",
            "name": "ARISTA03T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.7": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.6",
            "name": "ARISTA04T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.9": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.8",
            "name": "ARISTA05T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.11": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.10",
            "name": "ARISTA06T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.13": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.12",
            "name": "ARISTA07T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.15": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.14",
            "name": "ARISTA08T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.17": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.16",
            "name": "ARISTA09T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.19": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.18",
            "name": "ARISTA10T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.21": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.20",
            "name": "ARISTA11T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.23": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.22",
            "name": "ARISTA12T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.25": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.24",
            "name": "ARISTA13T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.27": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.26",
            "name": "ARISTA14T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.29": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.28",
            "name": "ARISTA15T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.31": {
            "asn": "65200",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.30",
            "name": "ARISTA16T2",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.33": {
            "asn": "64001",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.32",
            "name": "ARISTA01T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.35": {
            "asn": "64002",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.34",
            "name": "ARISTA02T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.37": {
            "asn": "64003",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.36",
            "name": "ARISTA03T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.39": {
            "asn": "64004",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.38",
            "name": "ARISTA04T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.41": {
            "asn": "64005",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.40",
            "name": "ARISTA05T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.43": {
            "asn": "64006",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.42",
            "name": "ARISTA06T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.45": {
            "asn": "64007",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.44",
            "name": "ARISTA07T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.47": {
            "asn": "64008",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.46",
            "name": "ARISTA08T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.49": {
            "asn": "64009",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.48",
            "name": "ARISTA09T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.51": {
            "asn": "64010",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.50",
            "name": "ARISTA10T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.53": {
            "asn": "64011",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.52",
            "name": "ARISTA11T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.55": {
            "asn": "64012",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.54",
            "name": "ARISTA12T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.57": {
            "asn": "64013",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.56",
            "name": "ARISTA13T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.59": {
            "asn": "64014",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.58",
            "name": "ARISTA14T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.61": {
            "asn": "64015",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.60",
            "name": "ARISTA15T0",
            "nhopself": "0",
            "rrclient": "0"
        },
        "10.0.0.63": {
            "asn": "64016",
            "holdtime": "180",
            "keepalive": "60",
            "local_addr": "10.0.0.62",
            "name": "ARISTA16T0",
            "nhopself": "0",
            "rrclient": "0"
        }
    },
    "CRM": {
        "Config": {
            "acl_counter_high_threshold": "85",
            "acl_counter_low_threshold": "70",
            "acl_counter_threshold_type": "percentage",
            "acl_entry_high_threshold": "85",
            "acl_entry_low_threshold": "70",
            "acl_entry_threshold_type": "percentage",
            "acl_group_high_threshold": "85",
            "acl_group_low_threshold": "70",
            "acl_group_threshold_type": "percentage",
            "acl_table_high_threshold": "85",
            "acl_table_low_threshold": "70",
            "acl_table_threshold_type": "percentage",
            "fdb_entry_high_threshold": "85",
            "fdb_entry_low_threshold": "70",
            "fdb_entry_threshold_type": "percentage",
            "ipv4_neighbor_high_threshold": "85",
            "ipv4_neighbor_low_threshold": "70",
            "ipv4_neighbor_threshold_type": "percentage",
            "ipv4_nexthop_high_threshold": "85",
            "ipv4_nexthop_low_threshold": "70",
            "ipv4_nexthop_threshold_type": "percentage",
            "ipv4_route_high_threshold": "85",
            "ipv4_route_low_threshold": "70",
            "ipv4_route_threshold_type": "percentage",
            "ipv6_neighbor_high_threshold": "85",
            "ipv6_neighbor_low_threshold": "70",
            "ipv6_neighbor_threshold_type": "percentage",
            "ipv6_nexthop_high_threshold": "85",
            "ipv6_nexthop_low_threshold": "70",
            "ipv6_nexthop_threshold_type": "percentage",
            "ipv6_route_high_threshold": "85",
            "ipv6_route_low_threshold": "70",
            "ipv6_route_threshold_type": "percentage",
            "nexthop_group_high_threshold": "85",
            "nexthop_group_low_threshold": "70",
            "nexthop_group_member_high_threshold": "85",
            "nexthop_group_member_low_threshold": "70",
            "nexthop_group_member_threshold_type": "percentage",
            "nexthop_group_threshold_type": "percentage",
            "polling_interval": "300"
        }
    },
    "DEVICE_METADATA": {
        "localhost": {
            "bgp_asn": "65100",
            "default_bgp_status": "up",
            "default_pfcwd_status": "disable",
            "hostname": "sonic",
            "hwsku": "Force10-S6000",
            "mac": "52:54:00:12:34:56",
            "platform": "x86_64-kvm_x86_64-r0",
            "type": "LeafRouter"
        }
    },
    "FEATURE": {
        "bgp": {
            "auto_restart": "enabled",
            "has_global_scope": "False",
            "has_per_asic_scope": "True",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "database": {
            "auto_restart": "disabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "True",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "dhcp_relay": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "lldp": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "True",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "mgmt-framework": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "True",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "nat": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "disabled"
        },
        "pmon": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "radv": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "sflow": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "disabled"
        },
        "snmp": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "True",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "swss": {
            "auto_restart": "enabled",
            "has_global_scope": "False",
            "has_per_asic_scope": "True",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "syncd": {
            "auto_restart": "enabled",
            "has_global_scope": "False",
            "has_per_asic_scope": "True",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "teamd": {
            "auto_restart": "enabled",
            "has_global_scope": "False",
            "has_per_asic_scope": "True",
            "has_timer": "False",
            "high_mem_alert": "disabled",
            "state": "enabled"
        },
        "telemetry": {
            "auto_restart": "enabled",
            "has_global_scope": "True",
            "has_per_asic_scope": "False",
            "has_timer": "True",
            "high_mem_alert": "disabled",
            "state": "enabled"
        }
    },
    "FLEX_COUNTER_TABLE": {
        "BUFFER_POOL_WATERMARK": {
            "FLEX_COUNTER_STATUS": "enable"
        },
        "PFCWD": {
            "FLEX_COUNTER_STATUS": "enable"
        },
        "PG_WATERMARK": {
            "FLEX_COUNTER_STATUS": "enable"
        },
        "PORT": {
            "FLEX_COUNTER_STATUS": "enable"
        },
        "PORT_BUFFER_DROP": {
            "FLEX_COUNTER_STATUS": "enable"
        },
        "QUEUE": {
            "FLEX_COUNTER_STATUS": "enable"
        },
        "QUEUE_WATERMARK": {
            "FLEX_COUNTER_STATUS": "enable"
        }
    },
    "INTERFACE": {
        "Ethernet0": {},
        "Ethernet4": {},
        "Ethernet8": {},
        "Ethernet12": {},
        "Ethernet16": {},
        "Ethernet20": {},
        "Ethernet24": {
            "vrf_name": "VrfHedgehog"
        },
        "Ethernet28": {},
        "Ethernet32": {},
        "Ethernet36": {},
        "Ethernet40": {},
        "Ethernet44": {},
        "Ethernet48": {},
        "Ethernet52": {},
        "Ethernet56": {},
        "Ethernet60": {},
        "Ethernet64": {},
        "Ethernet68": {},
        "Ethernet72": {},
        "Ethernet76": {},
        "Ethernet80": {},
        "Ethernet84": {},
        "Ethernet88": {},
        "Ethernet92": {},
        "Ethernet96": {},
        "Ethernet100": {},
        "Ethernet104": {},
        "Ethernet108": {},
        "Ethernet112": {},
        "Ethernet116": {},
        "Ethernet120": {},
        "Ethernet124": {},
        "Ethernet0|10.0.0.0/31": {},
        "Ethernet4|10.0.0.2/31": {},
        "Ethernet4|10.255.255.4/32": {},
        "Ethernet4|2001:DB8::4/32": {},
        "Ethernet8|10.0.0.4/31": {},
        "Ethernet12|10.0.0.6/31": {},
        "Ethernet12|10.0.1.1/31": {},
        "Ethernet16|10.0.0.8/31": {},
        "Ethernet20|10.0.0.10/31": {},
        "Ethernet28|10.0.0.14/31": {},
        "Ethernet32|10.0.0.16/31": {},
        "Ethernet36|10.0.0.18/31": {},
        "Ethernet40|10.0.0.20/31": {},
        "Ethernet44|10.0.0.22/31": {},
        "Ethernet48|10.0.0.24/31": {},
        "Ethernet52|10.0.0.26/31": {},
        "Ethernet56|10.0.0.28/31": {},
        "Ethernet60|10.0.0.30/31": {},
        "Ethernet64|10.0.0.32/31": {},
        "Ethernet68|10.0.0.34/31": {},
        "Ethernet72|10.0.0.36/31": {},
        "Ethernet76|10.0.0.38/31": {},
        "Ethernet80|10.0.0.40/31": {},
        "Ethernet84|10.0.0.42/31": {},
        "Ethernet88|10.0.0.44/31": {},
        "Ethernet92|10.0.0.46/31": {},
        "Ethernet96|10.0.0.48/31": {},
        "Ethernet100|10.0.0.50/31": {},
        "Ethernet104|10.0.0.52/31": {},
        "Ethernet108|10.0.0.54/31": {},
        "Ethernet112|10.0.0.56/31": {},
        "Ethernet116|10.0.0.58/31": {},
        "Ethernet120|10.0.0.60/31": {},
        "Ethernet124|10.0.0.62/31": {}
    },
    "LOOPBACK_INTERFACE": {
        "Loopback0": {},
        "Loopback01": {},
        "Loopback0|10.1.0.1/32": {},
        "Loopback0|10.10.10.1/32": {},
        "Loopback0|10.255.255.1/32": {},
        "Loopback01|10.255.255.1/32": {}
    },
    "MGMT_VRF_CONFIG": {
        "vrf_global": {
            "mgmtVrfEnabled": "true"
        }
    },
    "PORT": {
        "Ethernet0": {
            "admin_status": "up",
            "alias": "fortyGigE0/0",
            "index": "0",
            "lanes": "25,26,27,28",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet4": {
            "admin_status": "up",
            "alias": "fortyGigE0/4",
            "fec": "fc",
            "index": "1",
            "lanes": "29,30,31,32",
            "mtu": "1500",
            "pfc_asym": "on",
            "speed": "100000000"
        },
        "Ethernet8": {
            "admin_status": "up",
            "alias": "fortyGigE0/8",
            "index": "2",
            "lanes": "33,34,35,36",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet12": {
            "admin_status": "up",
            "alias": "fortyGigE0/12",
            "index": "3",
            "lanes": "37,38,39,40",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet16": {
            "admin_status": "up",
            "alias": "fortyGigE0/16",
            "index": "4",
            "lanes": "45,46,47,48",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet20": {
            "admin_status": "up",
            "alias": "fortyGigE0/20",
            "index": "5",
            "lanes": "41,42,43,44",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet24": {
            "admin_status": "up",
            "alias": "fortyGigE0/24",
            "index": "6",
            "lanes": "1,2,3,4",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet28": {
            "admin_status": "up",
            "alias": "fortyGigE0/28",
            "index": "7",
            "lanes": "5,6,7,8",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet32": {
            "admin_status": "up",
            "alias": "fortyGigE0/32",
            "index": "8",
            "lanes": "13,14,15,16",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet36": {
            "admin_status": "up",
            "alias": "fortyGigE0/36",
            "index": "9",
            "lanes": "9,10,11,12",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet40": {
            "admin_status": "up",
            "alias": "fortyGigE0/40",
            "index": "10",
            "lanes": "17,18,19,20",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet44": {
            "admin_status": "up",
            "alias": "fortyGigE0/44",
            "index": "11",
            "lanes": "21,22,23,24",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet48": {
            "admin_status": "up",
            "alias": "fortyGigE0/48",
            "index": "12",
            "lanes": "53,54,55,56",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet52": {
            "admin_status": "up",
            "alias": "fortyGigE0/52",
            "index": "13",
            "lanes": "49,50,51,52",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet56": {
            "admin_status": "up",
            "alias": "fortyGigE0/56",
            "index": "14",
            "lanes": "57,58,59,60",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet60": {
            "admin_status": "up",
            "alias": "fortyGigE0/60",
            "index": "15",
            "lanes": "61,62,63,64",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet64": {
            "admin_status": "up",
            "alias": "fortyGigE0/64",
            "index": "16",
            "lanes": "69,70,71,72",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet68": {
            "admin_status": "up",
            "alias": "fortyGigE0/68",
            "index": "17",
            "lanes": "65,66,67,68",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet72": {
            "admin_status": "up",
            "alias": "fortyGigE0/72",
            "index": "18",
            "lanes": "73,74,75,76",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet76": {
            "admin_status": "up",
            "alias": "fortyGigE0/76",
            "index": "19",
            "lanes": "77,78,79,80",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet80": {
            "admin_status": "up",
            "alias": "fortyGigE0/80",
            "index": "20",
            "lanes": "109,110,111,112",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet84": {
            "admin_status": "up",
            "alias": "fortyGigE0/84",
            "index": "21",
            "lanes": "105,106,107,108",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet88": {
            "admin_status": "up",
            "alias": "fortyGigE0/88",
            "index": "22",
            "lanes": "113,114,115,116",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet92": {
            "admin_status": "up",
            "alias": "fortyGigE0/92",
            "index": "23",
            "lanes": "117,118,119,120",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet96": {
            "admin_status": "up",
            "alias": "fortyGigE0/96",
            "index": "24",
            "lanes": "125,126,127,128",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet100": {
            "admin_status": "up",
            "alias": "fortyGigE0/100",
            "index": "25",
            "lanes": "121,122,123,124",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet104": {
            "admin_status": "up",
            "alias": "fortyGigE0/104",
            "index": "26",
            "lanes": "81,82,83,84",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet108": {
            "admin_status": "up",
            "alias": "fortyGigE0/108",
            "index": "27",
            "lanes": "85,86,87,88",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet112": {
            "admin_status": "up",
            "alias": "fortyGigE0/112",
            "index": "28",
            "lanes": "93,94,95,96",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet116": {
            "admin_status": "up",
            "alias": "fortyGigE0/116",
            "index": "29",
            "lanes": "89,90,91,92",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet120": {
            "admin_status": "up",
            "alias": "fortyGigE0/120",
            "index": "30",
            "lanes": "101,102,103,104",
            "mtu": "9100",
            "speed": "40000"
        },
        "Ethernet124": {
            "admin_status": "up",
            "alias": "fortyGigE0/124",
            "index": "31",
            "lanes": "97,98,99,100",
            "mtu": "9100",
            "speed": "40000"
        }
    },
    "PORTCHANNEL": {
        "?": {
            "admin_status": "up",
            "mtu": "9100"
        },
        "PortChannel0008": {
            "admin_status": "up",
            "mtu": "9100"
        }
    },
    "PORTCHANNEL_MEMBER": {
        "PortChannel0008|Ethernet8": {},
        "PortChannel0008|Ethernet12": {}
    },
    "TELEMETRY": {
        "gnmi": {
            "port": "8080"
        }
    },
    "VERSIONS": {
        "DATABASE": {
            "VERSION": "version_1_0_4"
        }
    },
    "VLAN": {
        "Vlan100": {
            "vlanid": "100"
        }
    },
    "VRF": {
        "VrfHedgehog": {}
    }
}
```

{{</expand>}}

You can filter the configuration to only show the running configuration for ACLs, BGP, interfaces, NTP, ports, SNMP or `syslog`.

```
admin@switch:~$ show runningconfiguration ntp
NTP Servers
-------------
10.10.249.30
```
