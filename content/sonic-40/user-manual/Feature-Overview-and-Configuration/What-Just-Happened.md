---
title: What Just Happened
author: Cumulus Networks
weight: 54
product: SONiC
version: 4.0
siteSlug: sonic
---

What-Just-Happened feature is distributed as a Debian package that can be installed on SONiC system on the fly. Please contact Mellanox Support to get a Debian package to be installed on your SONiC switch. 

{{%notice info%}}

Before the installation make sure you do not have configuration changes in running config that you do not want to persist after reboot.

{{%/notice%}}

To install WJH:

1. Download the package on running SONiC system. Contact Mellanox Support to receive the package. 

       admin@sonic:~$ sudo curl http://arc-build-server/sonic/what-just-happened_1.0.1_amd64.deb -o what-just-happened_1.0.1_amd64.deb
       % Total % Received % Xferd Average Speed Time Time Time Current
       Dload Upload Total Spent Left Speed
       100 91.2M 100 91.2M 0 0 109M 0 --:--:-- --:--:-- --:--:-- 109M
2. Install the downloaded package using dpkg utility:

       admin@sonic:~$ sudo dpkg -i what-just-happened_1.0.1_amd64.deb 
       Selecting previously unselected package what-just-happened.
       (Reading database ... 27045 files and directories currently installed.)
       Preparing to unpack what-just-happened_1.0.1_amd64.deb ...
       Unpacking what-just-happened (1.0.1) ...
       Setting up what-just-happened (1.0.1) ...
       Loading what-just-happened docker image...
       Setting up default configuration to CONFIG DB...
       OK
       OK
       OK
       NOTE: config will be saved.
       Running command: /usr/local/bin/sonic-cfggen -d --print-data > /etc/sonic/config_db.json
       Reloading systemd configuration...
       Done!!!

Once this is done, you will see a new docker image installed on the SONiC system, you can verify it by running show version SONiC command:

```
admin@sonic:~$ show version
 
SONiC Software Version: SONiC.201911.105-a693f023
Distribution: Debian 9.12
Kernel: 4.9.0-11-2-amd64
Build commit: a693f023
Build date: Tue Jun  2 04:34:50 UTC 2020
Built by: johnar@jenkins-worker-8
 
Platform: x86_64-mlnx_msn2700-r0
HwSKU: ACS-MSN2700
ASIC: mellanox
Serial Number: MT1749X10061
Uptime: 11:13:31 up 13 min,  1 user,  load average: 1.23, 1.27, 0.94
 
Docker images:
REPOSITORY                    TAG                   IMAGE ID            SIZE
docker-wjh                    latest                98c3552e0656        314MB
docker-wjh                    master.0-5f20758      98c3552e0656        314MB
docker-syncd-mlnx             201911.105-a693f023   98fca07c66f8        385MB
docker-syncd-mlnx             latest                98fca07c66f8        385MB
docker-router-advertiser      201911.105-a693f023   7cfa270f720e        285MB
docker-router-advertiser      latest                7cfa270f720e        285MB
docker-sonic-mgmt-framework   201911.105-a693f023   e4de082a4d57        425MB
docker-sonic-mgmt-framework   latest                e4de082a4d57        425MB
docker-platform-monitor       201911.105-a693f023   47225d051c25        631MB
docker-platform-monitor       latest                47225d051c25        631MB
docker-fpm-frr                201911.105-a693f023   35f7b0e37293        330MB
docker-fpm-frr                latest                35f7b0e37293        330MB
docker-sflow                  201911.105-a693f023   1881f652abc6        310MB
docker-sflow                  latest                1881f652abc6        310MB
docker-lldp-sv2               201911.105-a693f023   68b65649a34c        307MB
docker-lldp-sv2               latest                68b65649a34c        307MB
docker-dhcp-relay             201911.105-a693f023   9ad2cf038e18        295MB
docker-dhcp-relay             latest                9ad2cf038e18        295MB
docker-database               201911.105-a693f023   eb5aa74a87c1        285MB
docker-database               latest                eb5aa74a87c1        285MB
docker-teamd                  201911.105-a693f023   1e58c8013eb7        310MB
docker-teamd                  latest                1e58c8013eb7        310MB
docker-snmp-sv2               201911.105-a693f023   9be7e0014c74        343MB
docker-snmp-sv2               latest                9be7e0014c74        343MB
docker-orchagent              201911.105-a693f023   cfd095aa48d4        328MB
docker-orchagent              latest                cfd095aa48d4        328MB
docker-nat                    201911.105-a693f023   b4b59b10cd72        311MB
docker-nat                    latest                b4b59b10cd72        311MB
docker-sonic-telemetry        201911.105-a693f023   63aee702a3ed        349MB
docker-sonic-telemetry        latest                63aee702a3ed        349MB
```

{{%notice info%}}

During the installation, a default configuration required for What Just Happened to run will be pushed to CONFIG DB following a config save operation. No changes to the existing configuration will be made, only the new configuration will be inserted.

{{%/notice%}}

## Integrating What Just Happened with SONiC

Once installed, a new docker image will be treated as another SONiC optional feature, thus any feature operation can be applied to What Just Happened as well. You can run the following command to verify it:

```
admin@sonic:~$ show feature status
Feature             State     AutoRestart
------------------  --------  -------------
bgp                 enabled   enabled
database            enabled   disabled
dhcp_relay          enabled   enabled
lldp                enabled   enabled
mgmt-framework      enabled   enabled
nat                 disabled  enabled
pmon                enabled   enabled
radv                enabled   enabled
sflow               disabled  enabled
snmp                enabled   enabled
swss                enabled   enabled
syncd               enabled   enabled
teamd               enabled   enabled
telemetry           enabled   enabled
what-just-happened  enabled   disabled 
```

After installation, What Just Happened is in disabled state by default.

To enable WJH:
1. Run:

       sudo config feature state what-just-happened enabled
2. Save the configuration to make changes persistent across reboots.

   If further configuration changes are required, follow the instruction in this link: https://github.com/Azure/SONiC/blob/2ac24d2e216ee1187ed68f13a7b6c2e198c71a80/doc/database/multi_database_instances.md.

Any user configuration to CONTAINER_FEATURE table is also applied to the What Just Happened container.  Thus, you can configure an auto restart of the container or a high memory alert in the same way as it is done for any other SONiC docker container. The output below shows the defaults:

```
admin@sonic:~$ redis-cli -n 4 hgetall "CONTAINER_FEATURE|what-just-happened"
1) "auto_restart"
2) "disabled"
3) "high_mem_alert"
4) "disabled"
```

Once enabled, you can see a new docker container running in the system:

```
admin@sonic:~$ docker ps 
CONTAINER ID        IMAGE                             COMMAND                  CREATED              STATUS              PORTS               NAMES
f3484abb2d69        docker-wjh:latest                 "/usr/bin/supervisord"   About a minute ago   Up About a minute                       what-just-happened
a45fb0c5b4b9        docker-snmp-sv2:latest            "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             snmp
cb93b1f3e9d9        docker-sonic-telemetry:latest     "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             telemetry
6c3619d37a8a        docker-router-advertiser:latest   "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             radv
54d4463a62a0        docker-lldp-sv2:latest            "/usr/bin/docker-lld…"   13 hours ago         Up 12 hours                             lldp
716ce0c84a5f        docker-nat:latest                 "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             nat
e21843c92b81        docker-dhcp-relay:latest          "/usr/bin/docker_ini…"   13 hours ago         Up 12 hours                             dhcp_relay
83048cd4e43c        docker-sflow:latest               "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             sflow
ac887f2319b5        docker-platform-monitor:latest    "/usr/bin/docker_ini…"   13 hours ago         Up 12 hours                             pmon
9052457251f7        docker-syncd-mlnx:latest          "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             syncd
46463fb559ca        docker-teamd:latest               "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             teamd
025864af2a73        docker-orchagent:latest           "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             swss
2c1d59da4117        docker-fpm-frr:latest             "/usr/bin/supervisord"   13 hours ago         Up 12 hours                             bgp
b2d1e2ea041a        docker-database:latest            "/usr/local/bin/dock…"   13 hours ago         Up 12 hours                             database
```

### Integrating "What Just Happened" with SONiC systemd

What Just Happened container is managed by systemd in the same way as any other component in SONiC, thus any systemctl command can be applied to What Just Happened. To see the status of the service after What Just Happened is enabled:

```
admin@sonic:~$ sudo systemctl status what-just-happened.service 
what-just-happened.service - Service providing "What-Just-Happened" feature functionality
   Loaded: loaded (/etc/systemd/system/what-just-happened.service; static; vendor preset: enabled)
   Active: active (running) since Wed 2020-06-03 10:48:49 UTC; 15s ago
  Process: 31918 ExecStartPre=/usr/bin/what-just-happened.sh start (code=exited, status=0/SUCCESS)
 Main PID: 31987 (what-just-happe)
    Tasks: 10 (limit: 4915)
   Memory: 20.6M
      CPU: 1.284s
   CGroup: /system.slice/what-just-happened.service
           ├─31987 /bin/bash /usr/bin/what-just-happened.sh wait
           └─31989 docker wait what-just-happened
 
Jun 03 10:48:48 r-boxer-sw01 systemd[1]: Starting Service providing "What-Just-Happened" feature functionality...
Jun 03 10:48:49 r-boxer-sw01 what-just-happened.sh[31918]: Creating new what-just-happened container with HWSKU ACS-MSN2010
Jun 03 10:48:49 r-boxer-sw01 what-just-happened.sh[31918]: f3484abb2d69a48549309150160fff9851b8ea178324332bbc18ed90a35cb960
Jun 03 10:48:49 r-boxer-sw01 what-just-happened.sh[31918]: what-just-happened
Jun 03 10:48:49 r-boxer-sw01 systemd[1]: Started Service providing "What-Just-Happened" feature functionality.
```

### Integrating "What Just Happened" with SONiC CLI

After installation, a new subcommand in show CLI group named what-just-happened will be available. This command is a root subcommand for any What Just Happened specific operation.

### Upgrading SONiC-to-SONiC

Currently What Just Happened package does not support SONiC-to-SONiC upgrade scenario. After SONiC-to-SONiC upgrade procedure, installed What Just Happened feature will be lost.

#### Upgrading the WJH Package

To upgrade to another version of the WJH package, user the installation command:

Please make sure the new WJH Debian has the proper SDK version integrated into the image.  If the version is not the latest, remove the WJH Debian image BEFORE rebooting to the next image. 

For the latest SDK version, refer to the SONiC Release Notes.

```
admin@sonic:~$ sudo dpkg -i what-just-happened-201911_1.2.0_amd64.deb 
(Reading database ... 28024 files and directories currently installed.)
Preparing to unpack what-just-happened-201911_1.2.0_amd64.deb ...
Stopping what-just-happened service...
what-just-happened
Removing installed docker what-just-happened images...
Untagged: docker-wjh:201911.master.0-dirty-20200812.172321
Untagged: docker-wjh:latest
Deleted: sha256:1ea0e2cf882b7bbd203834d77c9acd525a13f33bdd1d2c9698e957d2c8bf9b11
Deleted: sha256:91e7c1eec5f25417c1564f30d5d160755fef7bef37870488f451fe90493c23cb
Deleted: sha256:bbad6712a05452e1d65fd27b5ee3fdc1c84a53fb95f19214310a37e2aa95df47
Deleted: sha256:5fd624d90e10c62bac699b7c6f7f1fdb5a9e8ee15c9e5c4d3b74cd61f021d757
Deleted: sha256:8d33945a98c5c3d73fec4026326be6688f4898e0e2561b109de35dab13567a6a
Deleted: sha256:a56bc738c6fbc4d639cab9e37592484ca03930721bb84321eb8e51f7407eb6ac
Deleted: sha256:777e5954c4715cabbddcc1b0852ca80be4e03c7d595e1bdcccc671416297a351
Deleted: sha256:dd1f3612aceb8e0b1531a4c0301e5bfcb4179116f8bf45716e3eb2a9add0ba84
Deleted: sha256:e5316eeb03482087f37dea3f372d2cb03a8c2f70a2b733caa435ce5f040c2996
Deleted: sha256:aa3d24abfff4185f86a56ae98a9b42c96e375006c1852972d619ad567118d53d
Deleted: sha256:2353ed83bbcb58826508211cc2bdbf36ad718b360a7f843046b8f6caf10073d0
Deleted: sha256:bfad98fd76d3c5b4af05b876f37d36000f3096f798fd99d053a760ca88e350a2
Deleted: sha256:f01bc7215c6d590a460f080e50b7723cb6cb6166f3ab399ab826b39f7f53e42c
Deleted: sha256:e84b9d651af1e09084ecfe6e776b17dd1b2f1ada0122369537d4a01da854c303
Removing feature from FEATURE table...
Removing what-just-happened configuration tables...
NOTE: config will be saved.
Running command: /usr/local/bin/sonic-cfggen -d --print-data > /etc/sonic/config_db.json
Done!!!
Unpacking what-just-happened-201911 (1.2.0) over (1.2.0) ...
Setting up what-just-happened-201911 (1.2.0) ...
Loading what-just-happened docker image...
Writing default what-just-happened configuration...
NOTE: config will be saved...
Running command: /usr/local/bin/sonic-cfggen -d --print-data > /etc/sonic/config_db.json
Installing what-just-happened CLI...
Reloading systemd configuration...
Done!!!
```

## Configuring What Just Happened

### Global Configuration

```
"WJH": {
    "global": {
        "mode": "debug", 
        "nice_level": "1", 
        "pci_bandwidth": "50"
    }
}
```

- **mode** - defines the operation mode for What Just Happened. Can be either debug or streaming, currently only debug is available. In debug mode user is able to view packets locally on the system using CLI command, while in streaming mode the CLI is available to the user and dropped packets are streamed to a remote collector.
- **nice_level** - a nice value of the What Just Happened application process in Linux. User may tweak this parameter to control how "nice" the What Just Happened application will be to other processes in terms of CPU usage. In order to give more CPU resources to other running processes, you may increase this value. A valid range is from -20 to 19. nice_level can be changed in runtime while What Just Happened container is running.
- **pci_bandwidth** - controls how much of the PCI What Just Happened is allowed to use in percents. Valid range is from 0 to 100. Changing this value will require What Just Happened service restart.

We recommend keep the default values for Global configuration.

### Channels Configuration

A channel is an entity from which dropped packets are read. Same as a trap group that has a list of traps, a channel has a list of drop categories:

```
"WJH_CHANNEL": {
     "forwarding": {
        "drop_category_list": "L2,L3,Tunnel", 
        "type": "raw_and_aggregated"
     }
}
```

The type defines a type of data returned by What Just Happened, one of:

- **raw** - provides raw packets as well as metadata about the dropped packet, such as timestamp, drop reason, drop category and recommended action.
- **aggregated** - provides aggregated counter which shows how many packets of a flow has been dropped as well as metadata about the dropped packets. Aggregation is done based on tuple of Source and Destination MAC addresses, Source and Destination IP addresses and Ports, ingress port, VLAN, protocol and drop reason.
- **raw_and_aggregated** - combined type, provides both raw and aggregated information.

This configuration is default and in current What Just Happened release it cannot be changed by the user.

#### Changing Drop Reason and Recommended Action Messages

What Just Happened uses an XML formatted file for configuring messages displayed in the CLI, as shown in the example below:

```
<reason-info>
  <reason-id>204</reason-id>
  <reason>Ingress VLAN filtering</reason>
  <severity>Error</severity>
  <description>Validate the VLAN membership configuration on both ends of the link</description>
</reason-info>
```

User can modify the severity, reason and description fields. Upon start, What Just-Happened will try to load /etc/sonic/wjh/wjh.xml file that can be provided by the user. If this file does not exist, a default provided by What Just-Happened SDK library will be used. You can use the file inside What Just-Happened container as a reference for creating your own:

    admin@sonic:~$ docker exec -it what-just-happened less /usr/etc/wjh_lib_conf.xml

Once custom /etc/sonic/wjh/wjh.xml file is created, What Just-Happened service needs to be restarted to load the new XML file.

## Command Line User Interface

What Just Happened provides a new CLI subcommand in show utility.

|  Show WJH Help | Description |
| ---- | ------------ |
| show what-just-happened --help | Shows what-just-happened [OPTIONS] COMMAND [ARGS]... |
| Options | -?, -h, --help: Show this message and exit. |
| Commands | poll*: Poll what-just-happened user channel<br />configuration: show what-just-happened configuration<br />dump: Dump what-just-happened debug information |
| Example | <pre>admin@sonic:~$ show what-just-happened --help<br />Usage: show what-just-happened [OPTIONS] COMMAND [ARGS]...<br /><br />"show what-just-happened" command group<br /><br />Options:<br />  -?, -h, --help  Show this message and exit.<br /><br />Commands:<br />  poll*          Poll what-just-happened user channel<br />  configuration  show what-just-happened configuration<br />  dump           Dump what-just-happened debug information |

| Show WJH Config | Description |
| ---- | ------------ |
| show what-just-happened configuration | Shows what-just-happened configuration [OPTIONS] COMMAND [ARGS]... |
| Options | -?, -h, --help: Show this message and exit. |
| Commands | channels: show what-just-happened channel configuration<br />global: show global what-just-happened configuration |
| Example | <pre>admin@sonic:~$ show what-just-happened configuration<br />Usage: show what-just-happened configuration [OPTIONS] COMMAND [ARGS]...<br /><br />  show what-just-happened configuration<br /><br />Options: -?, -h, --help  Show this message and exit.<br /><br />Commands:<br />  channels  show what-just-happened channel configuration<br />  global    show global what-just-happened configuration</pre> |

| Show WJH Config Global | Description |
| ---- | ------------ |
| show what-just-happened configuration global | Shows what-just-happened global configuration. |
| Example | <pre>admin@sonic:~$ show what-just-happened configuration global<br />Mode      PCI Bandwidth (%)    Nice Level<br />------  -------------------  ------------<br />debug                    50             1</pre>

| Show WJH Config Channels | Description |
| ---- | ------------ |
| show what-just-happened configuration channels | Shows what-just-happened channel configuration. |
| Example | <pre>admin@sonic:~$ show what-just-happened configuration channels<br />Channel     Type                Polling Interval (s)    Drop Groups<br />----------  ------------------  ----------------------  -------------<br />forwarding  raw_and_aggregated  N/A                     L2,L3,Tunnel</pre>
| Notes | This command can be used only for a channel that has a type of raw or raw_and_aggregated.<br /><br />A raw or raw_and_aggregated channel has a circular buffer for storing dropped packets, the default capacity of the buffer is 1024 and cannot be changed by the user, thus the maximum number of packets displayed per channel is 1024. If the new packet gets dropped the oldest drop is discarded.<br /><br />For further information, refer to Channels Configuration. |

| Show WJH Poll | Description |
| ---- | ------------ |
| show what-just-happened poll --help | Shows what-just-happened poll [OPTIONS] [CHANNELS]... |
| Options | --aggregate: Dump aggregated counters<br />--export: Save dropped packets into pcap file<br />-?, -h, --help: Show this message and exit. |
| Example | <pre>admin@sonic:~$ show what-just-happened poll --help<br />Usage: show what-just-happened poll [OPTIONS] [CHANNELS]...<br /><br />Poll what-just-happened user channel<br /><br />Options:<br />  --aggregate     Dump aggregated counters<br />  --export        Save droped packets into pcap file<br />  -?, -h, --help  Show this message and exit.</pre> |
| Notes | To poll the channel, you can use either "show what-just-happened poll [OPTIONS] [CHANNELS]" or just use a root subcommand directly "show what-just-happened [OPTIONS] [CHANNELS]" |

| Show WJH Forwarding | Description |
| ---- | ------------ |
| show what-just-happened forwarding | Displays dropped packets. |
| Example | <pre>admin@sonic:~$ show what-just-happened forwarding<br />#  Timestamp              sPort      dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action<br />                                                                                        Group<br />-- ---------------------- ---------- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- ---------------------------------------------------<br />1  20/06/03 10:51:29.892  Ethernet0  N/A    N/A   e4:1d:2d:a5:f1:4a  33:33:00:00:00:16  IPv6     ::           ff02::16     ip        L3     Error     Source IP is unspecified - Bad packet was received<br />                                                                                                                                                      from the peer<br />2  20/06/03 10:51:29.892  Ethernet0  N/A    N/A   e4:1d:2d:a5:f1:4a  33:33:00:00:00:16  IPv6     ::           ff02::16     ip        L3     Error     Source IP is unspecified - Bad packet was received<br />                                                                                                                                                      from the peer</pre> |
| Notes | This command can be used only for a channel that has a type of raw or raw_and_aggregated.<br /><br />A raw or raw_and_aggregated channel has a circular buffer for storing dropped packets, the default capacity of the buffer is 1024 and cannot be changed by the user, thus the maximum number of packets displayed per channel is 1024. If the new packet gets dropped the oldest drop is discarded.<br /><br />Once drops are read from the channel, they are gone and will not be displayed by subsequent executions of show what-just-happened. To save information you have few options. In case of raw or aggregated or raw_and_aggregated channel you can save the CLI output to a file, in case of raw or raw_and_aggregated channel you can use --export option described below to save dropped packets into PCAP persistently.<br /><br />The user must remove any unused saved pcap file to prevent storage consumption. |

| Show WJH Forwarding Aggregate | Description |
| ---- | ------------ |
| show what-just-happened forwarding --aggregate | Displays aggregated counters. |
| Example | <pre>admin@sonic:~$ show what-just-happened forwarding --aggregate<br />#  sPort      VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action<br />-- ---------- ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -------------------------------------------------<br />1  Ethernet4  N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1:0  127.0.0.1:0  ip        100    Error     Unicast destination IP but multicast destination<br />                                                                                                                        MAC - Bad packet was received from the peer</pre> |
| Notes | This command can be used only for a channel that has a type of aggregated or raw_and_aggregated.<br /><br />An aggregated or raw_and_aggregated channel has a buffer for storing dropped packets, the default capacity of the buffer is 1024 and cannot be changed by the user, thus the maximum number of unique tuples of source, destination MAC, source destination IP and port, ingress port, vlan, protocol and drop reason is 1024, thus the maximum number of rows in aggregated table view per channel is 1024.<br /><br />Since, aggregation currently is done in software, on high drop rates the Count column may not reflect the actual number of dropped packets. |

| Show WJH Forwarding Export | Description |
| ---- | ------------ |
| show what-just-happened forwarding --export | Saves dropped packets into PCAP. |
| Example | <pre>admin@sonic:~$ show what-just-happened forwarding --export<br /><br />PCAP file path : /var/log/mellanox/wjh/wjh_user_2020_06_03_10_55_34.pcap<br /><br />#   Timestamp              sPort      dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action<br />                                                                                                                                      Group<br />--- ---------------------- ---------- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -------------------------------------------------<br />1   20/06/03 10:55:32.249  Ethernet4  N/A    N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1    127.0.0.1    ip        L3     Error     Unicast destination IP but multicast destination<br />                                                                                                                                                       MAC - Bad packet was received from the peer<br />2   20/06/03 10:55:32.249  Ethernet4  N/A    N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1    127.0.0.1    ip        L3     Error     Unicast destination IP but multicast destination<br />                                                                                                                                                       MAC - Bad packet was received from the peer</pre> |
| Notes | This command can be used only for a channel that has a type of raw or raw_and_aggregated.<br /><br />PCAP files are saved into /var/log/mellanox/wjh/ folder and named in the following format: wjh_user_YYYY_MM_DD_hh_mm_ss.pcap. Those files are not rotated or automatically cleaned. The user is required to manage the content of /var/log/mellanox/wjh/ and make sure created files will not take all space on the drive. After SONiC-to-SONiC upgrade, /var/log/mellanox/wjh/ will still contain dumps created by the user. As in case of raw table view, the maximum number of packets stored in PCAP file per channel is 1024.<br /><br />If type of the channel is raw_and_aggregated the user can view aggregated information and store packets into PCAP file at the same time.<br /><pre>admin@sonic:~$ show what-just-happened --aggregate --export<br /><br />PCAP file path : /var/log/mellanox/wjh/wjh_user_2020_06_03_10_58_31.pcap<br /><br />#  sPort      VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action<br />-- ---------- ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -------------------------------------------------<br />1  Ethernet4  N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1:0  127.0.0.1:0  ip        20     Error     Unicast destination IP but multicast destination<br />                                                                                                                        MAC - Bad packet was received from the peer</pre> |

| Docker Exec WJH | Description |
| --------------- | ----------- |
| docker exec -it what-just-happened supervisorctl status all | Checks whether or not services are running inside docker container. |
| Example | <pre>admin@sonic:~$ docker exec -it what-just-happened supervisorctl status all<br />rsyslogd                         RUNNING   pid 14, uptime 0:00:15<br />start.sh                         EXITED    Jun 03 10:57 AM<br />supervisor-proc-exit-listener    RUNNING   pid 8, uptime 0:00:16<br />wjhd                             RUNNING   pid 19, uptime 0:00:14</pre> |

| Show WJH Dump | Description |
| ------------- | ----------- |
| show what-just-happened dump | Dumps What Just-Happened library to stdout. |
| Example | <pre>admin@sonic:~$ show what-just-happened dump<br />######## Init params #########<br />force           : 1<br />max_bw_percent  : 50<br />conf_xml_path   : (null)<br />dbg_file_path   : (null)<br />ingress_info_type       : if_index<br />######## User Channel #########<br />channel id[0], channel type[3].</pre> |
