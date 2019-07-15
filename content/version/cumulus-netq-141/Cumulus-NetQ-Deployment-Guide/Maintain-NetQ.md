---
title: Maintain NetQ
author: Cumulus Networks
weight: 93
aliases:
 - /display/NETQ141/Maintain-NetQ
 - /pages/viewpage.action?pageId=10453451
pageID: 10453451
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
While regular maintenance of NetQ is not required, there are some tasks
that you may want to perform in the course of everyday operations. As
the network changes, you might have the need to add or remove monitored
nodes, notification integrations, and NetQ Agents for example. You might
also need to restore NetQ to a prior version or upgrade to a new
version.

## <span>Manage the Telemetry Server</span>

<span style="color: #36424a;"> Because the Telemetry Server (TS)
contains the configurations for event notification integrations and NetQ
Notifier filters, you might need to modify these configurations at some
point in the life cycle of your deployment. Adding new integrations and
filters are described in [Configure Optional NetQ
Capabilities](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Configure-Optional-NetQ-Capabilities).
Removing them is described here. </span>

### <span>Remove an Event Notification Integration</span>

You can delete an event notification integration using the `netq config
ts del notifier integration INTEGRATION` command. You can verify it has
been removed using the related `show` command.

For example, to remove a Slack integration and verify it is no longer in
the configuration:

    cumulus@ts:~$ netq config ts del notifier integration slack-test
    cumulus@ts:~$ netq config ts restart notifier 
    cumulus@ts:~$ netq config ts show notifier integration
    Integration Name    Attribute    Value
    ------------------  -----------  -----------------------------------------------------------
    pager-duty-test     api_integration_key  9876543210
                        type                 pagerduty
                        severity             info
                        api_access_key       1234567890
     
    Filter Name    Attribute    Value
    -------------  -----------  -------
    default        output       ALL
                   rule

### <span>Delete a NetQ Notifier Filter</span>

To delete a filter, use the following command, then restart the Notifier
service:

    cumulus@ts:~$ netq config ts del notifier filter <filter-name>
    cumulus@ts:~$ netq config ts restart notifier 
    cumulus@ts:~$ netq config ts show notifier integration

## <span>Manage the NetQ Agents</span>

At various points in time, you might want to change which network nodes
are being monitored by NetQ or look more closely at a network node for
troubleshooting purposes. Adding the NetQ Agent to a switch or host is
described in [Install
NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ).
Removing or simply decommissioning an Agent is described here. Managing
NetQ Agent logging is also presented in this section.

### <span id="src-10453451_MaintainNetQ-decom" class="confluence-anchor-link"></span><span>Remove NetQ Agent from a Node</span>

You can decommission NetQ Agent on a given node. You might need to do
this when you:

  - RMA the switch or host being monitored

  - Change the hostname of the switch or host being monitored

  - Move the switch or host being monitored from one data center to
    another

{{%notice note%}}

Decommissioning the node removes the agent from the NetQ database, along
with the node's history.

{{%/notice%}}

To decommission a node from the NetQ database, first disable the Agent
on that node and then run the following command on the TS:

    cumulus@hostname:~$ netq config stop agent
     
    cumulus@ts:~$ netq ts decommission [hostname] purge

### <span>Disable NetQ Agent on a Node</span>

You can temporarily disable NetQ Agent on a node. Disabling the agent
maintains the activity history in the NetQ database.

To disable NetQ Agent on a node, run the following command from the
node:

    cumulus@switch:~$ netq config stop agent

### <span id="src-10453451_MaintainNetQ-AgentLog" class="confluence-anchor-link"></span><span>Configure Logging for a NetQ Agent</span>

The logging level used for a NetQ Agent determines what types of events
are logged about the NetQ Agent on the switch or host.

<span style="color: #222222;"> First, you need to decide what level of
logging you want to configure. You can configure the logging level to be
the same for every NetQ Agent, or selectively increase or decrease the
logging level for a NetQ Agent on a problematic node. </span>

| Logging Level | Description                                                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| debug         | <span style="color: #ff0000;"> Sends notifications for all debugging-related, informational, warning, and error messages. </span>                           |
| info          | <span style="color: #ff0000;"> <span style="color: #000000;"> Sends notifications for </span> informational, warning, and error messages (default). </span> |
| warning       | <span style="color: #ff0000;"> <span style="color: #000000;"> Sends notifications for </span> warning and error messages. </span>                           |
| error         | <span style="color: #ff0000;"> <span style="color: #000000;"> Sends notifications for </span> errors messages. </span>                                      |

You can view the NetQ Agent log directly. Messages have the following
structure:

`<timestamp> <node> <service>[PID]: <level>: <message>`

| Element         | Description                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------- |
| timestamp       | Date and time event occurred in UTC format                                                   |
| node            | Hostname of network node where event occurred                                                |
| service \[PID\] | Service and Process IDentifier that generated the event                                      |
| level           | Logging level in which the given event is classified; *debug*, *error*, *info*, or *warning* |
| message         | Text description of event, including the node where the event occurred                       |

For example:

{{% imgOld 0 %}}

This example shows a portion of a NetQ Agent log with debug level
logging.

    ...
    2018-10-02T20:41:25.024945+00:00 mlx-2700-03 netq-agent[22438]: DEBUG: RX RTM_NEWLINK for ifname lo, admin_state up, oper_state up
    2018-10-02T20:41:25.028873+00:00 mlx-2700-03 netq-agent[22438]: DEBUG: Adding new link Link(managed=True, down_reason=, oper_state=up, learning_en=False, access_vlan=0, stp_state=3, hostname=mlx-2700-03, parent_if=lo, master=lo, objid=, mac_address=00:00:00:00:00:00, ifname=lo, dstport=0, deleted=False, timestamp=1538512885.02, vni=0, admin_state=up, vrf=default, active=True, vlans=, is_vlan_filtering=False, arp_suppress_en=False, kind=loopback, mtu=65536, localip=, rt_table_id=254, ifindex=1) to DB
    2018-10-02T20:41:25.032503+00:00 mlx-2700-03 netq-agent[22438]: DEBUG: RX RTM_NEWLINK for ifname eth0, admin_state up, oper_state up
    2018-10-02T20:41:23.606085+00:00 mlx-2700-03 netq-agent[22438]: INFO: Redis Ping to server succeeded.
    ...

**Example: Configure debug-level logging**

1.  Set the logging level to *debug.*
    
        cumulus@switch:~$ netq config add agent loglevel debug

2.  Restart the NetQ Agent.
    
        cumulus@switch:~$ netq config restart agent

3.  Verify connection to Telemetry Server.
    
        cumulus@switch:~$ netq config show server
        Server            Port       VRF             Status
        ----------------- ---------- --------------- ----------------
        192.168.0.254     6379       default         ok

<span style="color: #222222;"> **Example: Configure warning-level
logging** </span>

    cumulus@switch:~$ netq config add agent loglevel warning 
    cumulus@switch:~$ netq config restart agent 
    cumulus@switch:~$ netq config show server

**Example: Disable Agent Logging**

<span style="color: #222222;"> If you have set the logging level to
*debug* for troubleshooting, it is recommended that you either change
the logging level to a less heavy mode or completely disable agent
logging altogether when you are finished troubleshooting. </span>

<span style="color: #222222;"> To change the logging level, run the
following command and restart the agent service: </span>

    cumulus@switch:~$ netq config add agent loglevel <LOG_LEVEL> 
    cumulus@switch:~$ netq config restart agent

To disable all logging:

    cumulus@switch:~$ netq config del agent loglevel 
    cumulus@switch:~$ netq config restart agent

## <span id="src-10453451_MaintainNetQ-Backup" class="confluence-anchor-link"></span><span>Restore NetQ from Backup Files</span>

NetQ automatically takes snapshots of the NetQ Telemetry Server at five
minute intervals. These snapshots can be used to restore to a previous
configuration, or to diagnose existing issues with the configuration.
For information regarding how long snapshot data is stored, refer to the
[How Far Back in Time Can You
Travel](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Resolve-Issues/Methods-for-Diagnosing-Network-Issues)
section.

{{%notice note%}}

There are no configuration steps required for setting up backups. NetQ
snapshots occur automatically.

{{%/notice%}}

There are several use-cases in which restoring from a snapshot may be
warranted. These include:

  - Upgrading the physical server to increase available resources.

  - Migrating from one physical server to another.

  - NetQ Telemetry Server becomes unavailable.

### <span>Backup Locations</span>

Backup snapshots can be found in two file locations on the NetQ
Telemetry Server:

  - `/var/log/backup`: The latest, or master, snapshot.

  - `/var/backup`: Directory of previous snapshots.

### <span>Restore NetQ from a Snapshot</span>

To restore the NetQ Telemetry Server from a snapshot:

1.  Extract the GZip snapshot you wish to restore into a file called
    `appendonly.aof`. The example command below uses the master
    snapshot:
    
        root@cumulus:~# gzip -d < /var/backup/appendonly.aof_master_2017-06-06_054601.gz > appendonly.aof
    
    The snapshot filename has several parts:
    
      - `appendonly.aof`: The base file name.
    
      - `_master_`: Defines this file as the current master snapshot.
    
      - `2017-06-06_054601`: The date and time the snapshot was taken.

2.  Shutdown the NetQ stack:
    
        root@cumulus:~# sudo systemctl stop netq-appliance

3.  Copy the extracted `appendonly.aof` file into the data directory:
    
        root@cumulus:~# cp appendonly.aof /mnt/data/redis/master/appendonly.aof

4.  Use the `grep` command to confirm the Redis configuration is still
    set correctly:
    
        root@cumulus:~# grep appendonly /etc/cts/redis/*conf
        /etc/cts/redis/redis.conf:appendonly yes
        /etc/cts/redis/redis.conf:appendfilename "appendonly.aof"
        root@cumulus:~# grep 'save ""' /etc/cts/redis/*conf
        /etc/cts/redis/redis.conf:save ""

5.  Restart the NetQ Stack:
    
        root@cumulus:~# sudo systemctl start netq-appliance

## <span>Upgrade NetQ</span>

This section covers the process for upgrading NetQ. The upgrade process
involves upgrading each of the NetQ components (the NetQ Telemetry
Server and NetQ Agents on Cumulus Linux switches and hosts running other
Linux operating systems), and then connecting the upgraded NetQ
Telemetry Server to the network.

{{%notice info%}}

Cumulus Networks recommends only upgrading NetQ during a network
maintenance window.

{{%/notice%}}

{{%notice warning%}}

Events generated during the upgrade process will not be available in the
database. Once the upgrade process is complete, the agents re-sync with
the current state of the Host or Cumulus Linux switch with the Telemetry
Server.

{{%/notice%}}

Before upgrading NetQ, consider the following:

  - The minimum supported Cumulus Linux version for NetQ 1.4.0 is 3.3.2.

  - You must upgrade your NetQ Agents as well as the Telemetry Server.

  - You can upgrade to NetQ 1.4.0 without upgrading Cumulus Linux.

### <span>Upgrade the NetQ Telemetry Server</span>

The first step in upgrading NetQ is to update your Telemetry Server (or
servers if you are running in HA mode). If you are installing a *new*
instance of NetQ, follow the instruction in the [Install
NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
topic.

1.  Back up the current NetQ Telemetry Server data. For instructions,
    refer to [Restore NetQ from Backup
    Files](#src-10453451_MaintainNetQ-Backup).

2.  Shut down the connectivity from the Agents to the current NetQ
    Telemetry Server.
    
    {{%notice warning%}}
    
    This step is required to ensure Agents don't attempt to communicate
    with the Telemetry Server during the maintenance window.
    
    {{%/notice%}}
    
    On each server or host currently running a NetQ Agent:
    
    1.  Run `netq config stop agent`.
    
    2.  Run `netq del agent`.

3.  Shut down the current NetQ Telemetry Server.
    
    1.  Open your hypervisor management tool, such as Virtual Machine
        Manager or VirtualBox.
    
    2.  Stop the Telemetry Server VM and remove it.

4.  Install the new NetQ Telemetry Server, using instructions in the
    [Install
    NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
    topic.

5.  Restore the data to the new NetQ Telemetry Server. For instructions,
    refer to [Restore NetQ from Backup
    Files](#src-10453451_MaintainNetQ-Backup).
    
    {{%notice info%}}
    
    This step can be skipped if there is no desire to retain the
    previous data. NetQ agents re-populate with the current data once
    they connect to the new NetQ Telemetry Server.
    
    {{%/notice%}}

6.  Validate that the Telemetry Server is up and running.
    
        cumulus@ts:~$ sudo systemctl status netq-appliance.service
        \u25cf netq-appliance.service - NETQ Backend
          Loaded: loaded (/lib/systemd/system/netq-appliance.service; enabled)
          Active: active (running) since Mon 2018-10-01 18:20:53 UTC; 1 day 2h ago
        Main PID: 3471 (docker-compose)
          CGroup: /system.slice/netq-appliance.service
                  \u2514\u25003471 /opt/venvs/cl-docker-compose/bin/python /usr/sbin/docker-compose -p netq -f /etc/cts/docker/netq-base-compose.yml up --no-color
        Oct 01 18:20:53 redis-1 netq-adjust-mem[3462]: Current REDIS max memory setting in /etc/cts/redis/redis.conf is 8589934592
        Oct 01 18:20:53 redis-1 netq-adjust-mem[3462]: Setting REDIS max memory to 11715797811 based on 16736854016 available at 0.70 ratio.
        Oct 01 18:20:53 redis-1 systemd[1]: Started NETQ Backend.
        Oct 01 18:20:54 redis-1 env[3471]: Creating netq_redis_master_1 ...
        Oct 01 18:20:54 redis-1 env[3471]: [83B blob data]
        Oct 01 18:20:54 redis-1 env[3471]: Creating netq_netq_1         ...
        Oct 01 18:20:55 redis-1 env[3471]: [166B blob data]

{{%notice note%}}

Cumulus Networks recommends that the NetQ Agents remain disconnected
from the NetQ Telemetry Server until they have been upgraded to the
current version of NetQ as well.

{{%/notice%}}

### <span>Upgrade the NetQ Agents</span>

The second step in the NetQ upgrade process is to upgrade the NetQ
Agents on each monitored node. Follow the steps for the relevant OS
below to upgrade the NetQ Agents:

#### <span>Cumulus Linux</span>

To upgrade the NetQ Agent on a Cumulus Linux switch, do the following:

1.  Open the `/etc/apt/sources.list` file in a text editor.

2.  Add the following line, and save the file:
    
        cumulus@switch:~$ deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-3 netq-1.4

3.  Install the `cumulus-netq` metapack and its components:
    
        cumulus@switch:~$ sudo apt-get update && sudo apt-get install cumulus-netq

#### <span>Ubuntu 16.04</span>

To upgrade the NetQ Agent on an Ubuntu host, do the following:

1.  Use the `wget` tool to retrieve the public key:
    
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-host-ubuntu.pubkey | apt-key add

2.  Open the `/etc/apt/sources.list` file in a text editor.

3.  Add the following line, and save the file:
    
        root@ubuntu:~# deb https://apps3.cumulusnetworks.com/repos/deb xenial netq-1.4

4.  Install the `cumulus-netq` metapack and its components:
    
        root@ubuntu:~# sudo apt-get update && sudo apt-get install cumulus-netq
    
    When you see the following prompt, type *N* to keep your current
    NetQ configuration in place:
    
        Configuration file '/etc/netq/netq.yml'
         ==> File on system created by you or by a script.
         ==> File also in package provided by package maintainer.
           What would you like to do about it ?  Your options are:
            Y or I  : install the package maintainer's version
            N or O  : keep your currently-installed version
              D     : show the differences between the versions
              Z     : start a shell to examine the situation

#### <span>Red Hat Enterprise Linux 7 / CentOS 7</span>

To upgrade the NetQ Agent on a Red Hat or CentOS host, do the following:

1.  Import the public key:
    
        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-host-el.pubkey

2.  Open `/etc/yum.repos.d/cumulus-host-el.repo` in a text editor.

3.  Define the repository source, and save the file:
    
        [cumulus-arch]
        name=Cumulus Packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.4/$basearch
        gpgcheck=1
        enabled=1
         
        [cumulus-noarch]
        name=Architecture-independent Cumulus packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.4/noarch
        gpgcheck=1
        enabled=1
         
        [cumulus-src]
        name=Cumulus source packages for RHEL
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/$releasever/netq-1.4/src
        gpgcheck=1
        enabled=1

4.  Install the `cumulus-netq` metapack and its components:
    
        root@rhel7:~# yum install cumulus-netq

### <span>Connect the NetQ Telemetry Server to the Network</span>

1.  Once the NetQ Telemetry Server and NetQ agents have been upgraded,
    connect the NetQ Telemetry Server to the network. For more
    information, refer to the [Install
    NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
    topic.

2.  Verify the NetQ Agents are OK, and running NetQ 1.4.
    
        cumulus@ts:~$ netq show agents
        Matching agents records:
        Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
        ----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
        edge01            Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   7d:5h:9m:29s              7d:5h:9m:19s              7d:5h:9m:19s               23.253022s
        exit01            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:4s              5d:0h:53m:27s             5d:0h:53m:27s              31.941781s
        exit02            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:2s              5d:0h:53m:4s              5d:0h:53m:4s               15.969046s
        internet          Fresh            no       1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:6s              5d:5h:54m:45s             5d:5h:54m:45s              9.445051s
        leaf01            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:4s              5d:1h:46m:28s             5d:1h:46m:28s              11.341666s
        leaf02            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:5s              5d:0h:59m:48s             5d:0h:59m:48s              32.870613s
        leaf03            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:2s              5d:0h:58m:59s             5d:0h:58m:59s              5.821239s
        leaf04            Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:54m:57s             5d:0h:55m:39s             5d:0h:55m:39s              11.810535s
        oob-mgmt-server   Fresh            yes      1.4.0-cl3u10~1537731912.eae9c33      7d:5h:11m:1s              7d:5h:10m:37s             7d:5h:10m:37s              5.899206s
        server01          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   5d:5h:53m:13s             5d:5h:53m:4s              5d:5h:53m:4s               6.115634s
        server02          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   5d:5h:53m:13s             5d:5h:53m:3s              5d:5h:53m:3s               18.659022s
        server03          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   5d:5h:53m:13s             5d:5h:53m:3s              5d:5h:53m:3s               13.890821s
        server04          Fresh            yes      1.3.0-ub16.04u9~1522971904.b08ca60   5d:5h:53m:13s             5d:5h:53m:3s              5d:5h:53m:3s               12.524579s
        spine01           Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:55m:3s              5d:0h:54m:55s             5d:0h:54m:55s              18.648519s
        spine02           Fresh            yes      1.3.0-cl3u9~1522970647.b08ca60       5d:5h:54m:56s             5d:0h:54m:27s             5d:0h:54m:27s              5.712222s
         
        cumulus@ts:~$ cat /etc/app-release
        APPLIANCE_VERSION=1.4.0
        APPLIANCE_MANIFEST_HASH=23b30cc

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
