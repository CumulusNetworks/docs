---
title: What Just Happened
author: NVIDIA
weight: 620
product: SONiC
version: 202012
siteSlug: sonic
---

*What Just Happened* (WJH) is a troubleshooting feature that streams detailed and contextual telemetry data for analysis. It provides real-time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, and ACL or layer 1 problems.

**WJH available on NVIDIA Spectrum switches only.** It distributed as a Debian package that you can install on a SONiC switch. Please contact Mellanox Support to get the WJH Debian package.

## Install WJH

{{%notice info%}}

Before you install, make sure you do not have changes in the running configuration that you want to persist after reboot.

{{%/notice%}}

To install WJH:

1. Download the Debian package you received from Mellanox Support onto the SONiC switch.

       admin@switch:~$ sudo curl http://&lt;Mellanox-file-server>/sonic/what-just-happened_1.0.1_amd64.deb -o what-just-happened_1.0.1_amd64.deb
       % Total % Received % Xferd Average Speed Time Time Time Current
       Dload Upload Total Spent Left Speed
       100 91.2M 100 91.2M 0 0 109M 0 --:--:-- --:--:-- --:--:-- 109M
2. Install the downloaded package using `dpkg`:

       admin@switch:~$ sudo dpkg -i what-just-happened_1.0.1_amd64.deb 
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

When the installation finishes, a new Docker image appears as installed on the switch. You can verify it by running `show version`:

```
admin@switch:~$ show version
 
SONiC Software Version: SONiC.202012.15-cb79de1b
Distribution: Debian 10.7
Kernel: 4.19.0-9-2-amd64
Build commit: cb79de1b
Build date: Sat Jan 30 11:14:42 UTC 2021
Built by: johnar@jenkins-worker-11

Platform: x86_64-mlnx_msn2700-r0
HwSKU: ACS-MSN2700
ASIC: mellanox
ASIC Count: 1
Serial Number: MT1552X12041
Uptime: 19:19:08 up 15 days, 22:56,  1 user,  load average: 6.67, 6.37, 6.05
 
Docker images:
REPOSITORY                    TAG                   IMAGE ID            SIZE
docker-wjh                    latest                98c3552e0656        314MB
docker-wjh                    master.0-5f20758      98c3552e0656        314MB
docker-syncd-mlnx             202012.15-cb79de1b   10691c29472b        540MB
docker-syncd-mlnx             latest               10691c29472b        540MB
docker-teamd                  202012.15-cb79de1b   15135f94fe07        406MB
docker-teamd                  latest               15135f94fe07        406MB
docker-router-advertiser      202012.15-cb79de1b   11e5c3c840a8        395MB
docker-router-advertiser      latest               11e5c3c840a8        395MB
docker-nat                    202012.15-cb79de1b   f28128bcecb0        408MB
docker-nat                    latest               f28128bcecb0        408MB
docker-platform-monitor       202012.15-cb79de1b   68f6c90b7f0e        687MB
docker-platform-monitor       latest               68f6c90b7f0e        687MB
docker-lldp                   202012.15-cb79de1b   ee4cb85cb4bc        435MB
docker-lldp                   latest               ee4cb85cb4bc        435MB
docker-database               202012.15-cb79de1b   7a79adaa829c        394MB
docker-database               latest               7a79adaa829c        394MB
docker-orchagent              202012.15-cb79de1b   177b5e05d036        423MB
docker-orchagent              latest               177b5e05d036        423MB
docker-snmp                   202012.15-cb79de1b   0e1fd1ff2bc3        435MB
docker-snmp                   latest               0e1fd1ff2bc3        435MB
docker-dhcp-relay             202012.15-cb79de1b   0ae260811eaf        401MB
docker-dhcp-relay             latest               0ae260811eaf        401MB
docker-sonic-telemetry        202012.15-cb79de1b   4fcfc6efdcaa        469MB
docker-sonic-telemetry        latest               4fcfc6efdcaa        469MB
docker-sonic-mgmt-framework   202012.15-cb79de1b   b6f7412f2707        612MB
docker-sonic-mgmt-framework   latest               b6f7412f2707        612MB
docker-fpm-frr                202012.15-cb79de1b   4e6dfaf61388        423MB
docker-fpm-frr                latest               4e6dfaf61388        423MB
docker-sflow                  202012.15-cb79de1b   32b2b32b4bd7        406MB
docker-sflow                  latest               32b2b32b4bd7        406MB
```

{{%notice info%}}

During the installation, a default configuration required for What Just Happened to run is pushed to CONFIG_DB after you run `config save`. This does not change the existing configuration, it only applies the new one.

{{%/notice%}}

## Enable What Just Happened in SONiC

After you install WJH, SONiC treats the new WJH Docker image as any other optional SONiC feature, so SONiC `feature` commands can be applied to WJH like it can for any other SONiC container. You can verify SONiC was installed by running the following command:

```
admin@switch:~$ show feature status
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

Notice that WJH is in a *disabled* state by default after installation. To enable WJH, run:

    admin@switch:~$ sudo config feature state what-just-happened enabled

Then save the configuration to make the change persistent across reboots.

    admin@switch:~$ sudo config save -y

If you need to make further configuration changes, follow the steps in the {{<exlink url="https://github.com/Azure/SONiC/blob/master/doc/database/multi_database_instances.md" text="SONiC documentation">}} on GitHub.

Any configuration changes made to the `CONTAINER_FEATURE` table are also applied to the What Just Happened container. Thus, you can configure an auto restart of the container or a high memory alert in the same way you can for any other SONiC Docker container. The output below shows the defaults:

```
admin@switch:~$ redis-cli -n 4 hgetall "CONTAINER_FEATURE|what-just-happened"
1) "auto_restart"
2) "disabled"
3) "high_mem_alert"
4) "disabled"
```

After you enable WJH, you can see its Docker container running in the system:

```
admin@switch:~$ docker ps 
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

### How What Just Happened Interoperates with SONiC systemd

`systemd` manages the What Just Happened container just like any other SONiC component, so you can run any `systemctl` command on What Just Happened. To see the status of the service after you enable What Just Happened:

```
admin@switch:~$ sudo systemctl status what-just-happened.service 
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

### What Just Happened CLI Commands

After you install WJH, the `what-just-happened` command appears under the `show` command. The `show what-just-happened` commands are outlined in the table below.

|  show what-just-happened Command | Description |
| ---- | ------------ |
| show what-just-happened | Top level WJH command. |
| Options | -?, -h, \--help: Show this message and exit. |
| Commands | configuration: show what-just-happened configuration<br />poll*: Polls the WJH user channel.<br />dump: Dumps what-just-happened debug information. |
| Example | <pre>admin@switch:~$ show what-just-happened \--help<br />Usage: show what-just-happened [OPTIONS] COMMAND [ARGS]...<br /><br />"show what-just-happened" command group<br /><br />Options:<br />  -?, -h, \--help  Show this message and exit.<br /><br />Commands:<br />  poll*          Poll what-just-happened user channel<br />  configuration  show what-just-happened configuration<br />  dump           Dump what-just-happened debug information |

| show what-just-happened configuration Command | Description |
| ---- | ------------ |
| show what-just-happened configuration | Shows what-just-happened configuration [OPTIONS] COMMAND [ARGS]... |
| Options | -?, -h, \--help: Show this message and exit. |
| Commands | channels: Shows the WJH channel configuration.<br />global: Shows the global WJH configuration. |
| Basic Example | <pre>admin@switch:~$ show what-just-happened configuration<br />Usage: show what-just-happened configuration [OPTIONS] COMMAND [ARGS]...<br /><br />  show what-just-happened configuration<br /><br />Options: -?, -h, \--help  Show this message and exit.<br /><br />Commands:<br />  channels  show what-just-happened channel configuration<br />  global    show global what-just-happened configuration</pre> |
| Global Example | <pre>admin@switch:~$ show what-just-happened configuration global<br />Mode      PCI Bandwidth (%)    Nice Level<br />\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-<br />debug                    50             1</pre>
| Channels Example | <pre>admin@switch:~$ show what-just-happened configuration channels<br />Channel     Type                Polling Interval (s)    Drop Groups<br />\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-  \-\-\-\-\-\-\-\-\-\-\-\-\-<br />forwarding  raw_and_aggregated  N/A                     L2,L3,Tunnel</pre><p><strong>Note:</strong> Use this command only for a channel that has a type of <em>raw</em> or <em>raw_and_aggregated</em>.</p><p>A <em>raw</em> or <em>raw_and_aggregated</em> channel has a circular buffer for storing dropped packets. The default capacity of the buffer is 1024 packets; you cannot change this value, so the maximum number of packets displayed per channel is 1024. If a new packet gets dropped, the oldest drop is discarded.</p><p>For further information, refer to {{<link url="#channel-types" text="Channel Types">}} below.</p> |

| show what-just-happened poll Command | Description |
| ---- | ------------ |
| show what-just-happened poll | Shows results from WJH channel polls. |
| Options | \--aggregate: Dumps aggregated counters.<br />\--export: Saves dropped packets into a PCAP file.<br />-?, -h, \--help: Show this message and exit. |
| Example | <pre>admin@switch:~$ show what-just-happened poll \--help<br />Usage: show what-just-happened poll [OPTIONS] [CHANNELS]...<br /><br />Poll what-just-happened user channel<br /><br />Options:<br />  \--aggregate     Dump aggregated counters<br />  \--export        Save dropped packets into pcap file.<br />  -?, -h, \--help  Show this message and exit.</pre> |
| Notes | To poll the channel, you can use either <code>show what-just-happened poll [OPTIONS] [CHANNELS]</code> or just use the base command directly: <code>show what-just-happened [OPTIONS] [CHANNELS]</code>. |
| Aggregate example | <pre>admin@switch:~$ show what-just-happened poll \--aggregate</pre> |
| Export example | <pre>admin@switch:~$ show what-just-happened poll \--export</pre> |

| show what-just-happened forwarding Command | Description |
| ---- | ------------ |
| show what-just-happened forwarding | Displays dropped packets. |
| Options | \--aggregate: Displays aggregated counters.<br/>\--export: Saves dropped packets into a PCAP file. |
| Basic Example | <pre>admin@switch:~$ show what-just-happened forwarding<br />#  Timestamp              sPort      dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action<br />Group<br />\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\-\-\-\-\- -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-<br />1  20/06/03 10:51:29.892  Ethernet0  N/A    N/A   e4:1d:2d:a5:f1:4a  33:33:00:00:00:16  IPv6     ::           ff02::16     ip        L3     Error     Source IP is unspecified - Bad packet was received<br />from the peer<br />2  20/06/03 10:51:29.892  Ethernet0  N/A    N/A   e4:1d:2d:a5:f1:4a  33:33:00:00:00:16  IPv6     ::           ff02::16     ip        L3     Error     Source IP is unspecified - Bad packet was received<br />from the peer</pre><p><strong>Note:</strong> This command can be used only for a channel that has a type of raw or raw_and_aggregated.</p><p>A raw or raw_and_aggregated channel has a circular buffer for storing dropped packets, the default capacity of the buffer is 1024 and cannot be changed by the user, thus the maximum number of packets displayed per channel is 1024. If the new packet gets dropped the oldest drop is discarded.</p><p>After drops are read from the channel, they are gone and will not be displayed by subsequent executions of show what-just-happened. To save information you have few options. In case of raw or aggregated or raw_and_aggregated channel you can save the CLI output to a file, in case of raw or raw_and_aggregated channel you can use <code>--export</code> option described below to save dropped packets into PCAP persistently.</p><p>The user must remove any unused saved pcap file to prevent storage consumption.</p> |
| Aggregate Example | <pre>admin@switch:~$ show what-just-happened forwarding --aggregate<br />#  sPort      VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action<br />\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\-\-\-\-\- -\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-<br />1  Ethernet4  N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1:0  127.0.0.1:0  ip        100    Error     Unicast destination IP but multicast destination<br />MAC - Bad packet was received from the peer</pre><p><strong>Note:</strong> This command can be used only for a channel that has a type of <em>aggregated</em> or <em>raw_and_aggregated</em>.</p>An <em>aggregated</em> or <em>raw_and_aggregated</em> channel has a buffer for storing dropped packets, the default capacity of the buffer is 1024 and cannot be changed by the user, thus the maximum number of unique tuples of source, destination MAC, source destination IP and port, ingress port, vlan, protocol and drop reason is 1024, thus the maximum number of rows in aggregated table view per channel is 1024.</p><p>Since aggregation currently is done in software, on high drop rates the Count column may not reflect the actual number of dropped packets.</p> |
| Export Example | <pre>admin@switch:~$ show what-just-happened forwarding --export<br /><br />PCAP file path : /var/log/mellanox/wjh/wjh_user_2020_06_03_10_55_34.pcap<br /><br />#   Timestamp              sPort      dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action<br />Group<br />\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-<br />1   20/06/03 10:55:32.249  Ethernet4  N/A    N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1    127.0.0.1    ip        L3     Error     Unicast destination IP but multicast destination<br />MAC - Bad packet was received from the peer<br />2   20/06/03 10:55:32.249  Ethernet4  N/A    N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1    127.0.0.1    ip        L3     Error     Unicast destination IP but multicast destination<br />MAC - Bad packet was received from the peer</pre> |
| Notes | This command can be used only for a channel that has a type of raw or raw_and_aggregated.<br /><br />PCAP files are saved into /var/log/mellanox/wjh/ folder and named in the following format: <code>wjh_user_YYYY_MM_DD_hh_mm_ss.pcap</code>. Those files are not rotated or automatically cleaned. The user is required to manage the content of /var/log/mellanox/wjh/ and make sure created files will not take all space on the drive. After SONiC-to-SONiC upgrade, /var/log/mellanox/wjh/ will still contain dumps created by the user. As in case of raw table view, the maximum number of packets stored in PCAP file per channel is 1024.<br /><br />If type of the channel is raw_and_aggregated the user can view aggregated information and store packets into PCAP file at the same time.<br /><pre>admin@switch:~$ show what-just-happened --aggregate --export<br /><br />PCAP file path : <code>/var/log/mellanox/wjh/wjh_user_2020_06_03_10_58_31.pcap</code><br /><br />#  sPort      VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action<br />\-\- \-\-\-\-\-\-\-\-\-\- \-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\- \-\-\-\-\-\- \-\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-<br />1  Ethernet4  N/A   00:00:00:00:00:00  ff:ff:ff:ff:ff:ff  IPv4     127.0.0.1:0  127.0.0.1:0  ip        20     Error     Unicast destination IP but multicast destination<br />MAC - Bad packet was received from the peer</pre> |

| Docker Exec WJH | Description |
| --------------- | ----------- |
| docker exec -it what-just-happened supervisorctl status all | Checks whether the WJH service is running inside the Docker container. |
| Example | <pre>admin@switch:~$ docker exec -it what-just-happened supervisorctl status all<br />rsyslogd                         RUNNING   pid 14, uptime 0:00:15<br />start.sh                         EXITED    Jun 03 10:57 AM<br />supervisor-proc-exit-listener    RUNNING   pid 8, uptime 0:00:16<br />wjhd                             RUNNING   pid 19, uptime 0:00:14</pre> |

| Show WJH Dump | Description |
| ------------- | ----------- |
| show what-just-happened dump | Dumps the WJH library to <code>stdout</code>. |
| Example | <pre>admin@switch:~$ show what-just-happened dump<br />######## Init params #########<br />force           : 1<br />max_bw_percent  : 50<br />conf_xml_path   : (null)<br />dbg_file_path   : (null)<br />ingress_info_type       : if_index<br />######## User Channel #########<br />channel id[0], channel type[3].</pre> |

### Upgrade the WJH Package

To upgrade to another version of the WJH package, use the `dpkg` command.

Make sure the new WJH Debian has the proper SDK version integrated into the image. If the version is not the latest, remove the WJH Debian image **before** rebooting to the new image.

For the latest SDK version, refer to the {{<link url="Release-Notes" text="SONiC Release Notes">}}.

```
admin@switch:~$ sudo dpkg -i what-just-happened-202012_1.2.0_amd64.deb 
(Reading database ... 28024 files and directories currently installed.)
Preparing to unpack what-just-happened-202012_1.2.0_amd64.deb ...
Stopping what-just-happened service...
what-just-happened
Removing installed docker what-just-happened images...
Untagged: docker-wjh:202012.master.0-dirty-20200812.172321
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
Unpacking what-just-happened-202012 (1.2.0) over (1.2.0) ...
Setting up what-just-happened-202012 (1.2.0) ...
Loading what-just-happened docker image...
Writing default what-just-happened configuration...
NOTE: config will be saved...
Running command: /usr/local/bin/sonic-cfggen -d --print-data > /etc/sonic/config_db.json
Installing what-just-happened CLI...
Reloading systemd configuration...
Done!!!
```

{{%notice info%}}

If you upgrade the SONiC OS on the switch, WJH gets removed. You need to reinstall the WJH package again.

{{%/notice%}}

## Configure What Just Happened

The configurations for global settings and channel types are stored in the `/etc/sonic/config_db.json` file.

### Global Configuration

WJH has these global settings:

| Setting | Description |
| ------- | ----------- |
| mode | Defines the operation mode for What Just Happened. The mode can be either *debug* or *streaming*, but only debug is available at this time. In debug mode, you can view packets locally on the system using the SONiC CLI. In streaming mode, the CLI is available to you and dropped packets are streamed to a remote collector. |
| nice_level | This setting represents how many CPU resources the What Just Happened process uses relative to other processes running on the switch. You can adjust this setting to control how "nice" the What Just Happened process is to other processes in terms of CPU usage. In order to give more CPU resources to other running processes, you may increase this value. The valid range is from -20 to 19. You can change `nice_level` at runtime while the What Just Happened container is running. |
| pci_bandwidth | <p>Controls what percent of the PCI What Just Happened is allowed to use. Valid range is from 0 to 100. If you change this setting, you must restart the What Just Happened service.</p><pre>admin@switch:~$ sudo systemctl restart what-just-happened.service</pre> |

NVIDIA recommends you keep the default values for the global configuration. However, if you need to change one or more of them, edit the the `/etc/sonic/config_db.json` file. The settings are in the WJH table:

```
admin@switch:~$ vi /etc/sonic/config_db.json
"WJH": {
    "global": {
        "mode": "debug", 
        "nice_level": "1", 
        "pci_bandwidth": "50"
    }
}
```

### Channel Types

A channel is an entity from which dropped packets are read. Just as a trap group that has a list of traps, a channel has a list of drop categories:

```
admin@switch:~$ vi /etc/sonic/config_db.json
"WJH_CHANNEL": {
     "forwarding": {
        "drop_category_list": "L2,L3,Tunnel", 
        "type": "raw_and_aggregated"
     }
}
```

The type defines a type of data returned by What Just Happened, one of:

| Type | Description |
| ---- | ----------- |
| raw | Provides the raw packets and metadata about the dropped packet, such as timestamp, drop reason, drop category and recommended action. |
| aggregated | Provides an aggregated counter, which shows how many packets of a flow have been dropped as well as metadata about the dropped packets. Aggregation is done based on tuple of source and destination MAC addresses, source and destination IP addresses and ports, ingress port, VLAN, protocol and drop reason. |
| raw_and_aggregated | Combined type, which provides both raw and aggregated information. |

You cannot change this configuration at this time.

### Change the Drop Reason and Recommended Action Messages

What Just Happened uses an XML formatted file for configuring messages displayed in the CLI, as shown in this example:

```
<reason-info>
  <reason-id>204</reason-id>
  <reason>Ingress VLAN filtering</reason>
  <severity>Error</severity>
  <description>Validate the VLAN membership configuration on both ends of the link</description>
</reason-info>
```

You can modify the **severity**, **reason** and **description** fields. When the `what-just-happened` service starts, WJH tries to load `/etc/sonic/wjh/wjh.xml` file that can be provided by the user. If this file does not exist, a default provided by the WJH SDK library is used. You can use the file inside What Just-Happened container as a reference for creating your own:

    admin@switch:~$ docker exec -it what-just-happened less /usr/etc/wjh_lib_conf.xml

Once custom `/etc/sonic/wjh/wjh.xml` file is created, the `what-just-happened` service needs to be restarted to load the new XML file.
