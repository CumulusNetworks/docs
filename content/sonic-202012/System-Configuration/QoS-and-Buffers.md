---
title: QoS and Buffers
author: NVIDIA
weight: 350
product: SONiC
version: 202012
siteSlug: sonic
---

This topic discusses buffer configuration, explicit congestion notification with weighted random early detection and priority flow control.

## Buffers

A buffer configuration includes:

- **Buffer pool size**: The maximum memory a certain kind of traffic can occupy.
- **Buffer profile**: Typically, most ports can share the same buffer configuration. You can create a buffer profile to attach that configuration to a port.
- **Buffer PG**: The profile for each ingress priority.
- **Buffer queue**: The profile for each egress queue.

The buffer configuration is stored in the BUFFER_POOL, BUFFER_PROFILE and BUFFER_PG tables. These tables are described in detail below.

### Buffer Calculation Models

There are two buffer calculation models:

- A *traditional model*, which SONiC adopted as the default for releases before the 202012. If the switch is configured with this model, all buffer-related configurations must be configured manually in CONFIG_DB. There are some switches that use this mode by default. <!-- which ones? -->
- A *dynamic model* is the recommended model, which was introduced in SONiC 202012. It is enabled by default on every switch. If the switch is configured with this model, the buffer profile for lossless traffic gets created automatically and the buffer size for `ingress_lossless_pool`, `ingress_lossy_pool` and `egress_lossy_pool` is calculated dynamically. You don't need to configure them manually. Because they are generated dynamically, they are no longer stored in CONFIG_DB but can be listed when you run the `show buffer information` command.

#### Dynamic Buffer Calculation

Dynamic buffer calculation:

- Calculates the lossless profiles for each port according to its speed, cable length and MTU.
- Calculates the buffer sizes of `ingress_lossless_pool`, `ingress_lossy_pool` and `egress_lossy_pool` automatically.
- Supports an arbitrary cable length.
- Releases all the unused memory to a shared buffer pool.

### BUFFER_POOL Table

The BUFFER_POOL table defines the buffer pools for lossless/lossy and ingress/egress. It contains the following fields:

-	**size**: The size of the buffer pool.
-	**type**: Egress or ingress.
-	**mode**: Static or dynamic.
-	**xoff**: The size of the shared headroom pool, available for ingress_lossless_pool only.

There are four predefined buffer pools:

- egress_lossless_pool
- egress_lossy_pool
- ingress_lossless_pool
- ingress_lossy_pool

{{% notice tip%}}

Since these pools are predefined or dynamically calculated, there is no need to define a new buffer pool or to modify them.

{{%/notice%}}

The **size** of `egress_lossless_pool` is always the maximum available memory whereas the the size of all the other pools is the quantity of the accumulative per port/PG/queue reserved buffer size subtracted from the maximum available buffer size.

For a switch running the dynamic model, the **size** of the `ingress_lossless_pool`, `ingress_lossy_pool` and `egress_lossy_pool` and **xoff** for `ingress_lossless_pool` is calculated dynamically.

For a switch running the traditional model, a default buffer configuration is provided for both top of rack and leaf router topologies, which use different port speeds and cable lengths. This affects the per PG reserved buffer size as follows:

- For a top of rack switch, SONiC assumes there are 28 ports with 5m cables and 4 ports with 40m cables. This is called a *t0* topology in SONiC. Its buffer configuration is in `sonic-buildimage/device/mellanox/<platform>/<sku>/buffers_defaults_t0.j2`.
- For a leaf router, SONiC assumes there are 16 ports with 40m cables and 16 ports with 300m cables. This is called a *t1* topology in SONiC. Its buffer configuration is in `sonic-buildimage/device/mellanox/<platform>/<sku>/buffers_defaults_t1.j2`.
- All ports run at the highest speed.

This table is referenced by the BUFFER_PROFILE table.

### BUFFER_PROFILE Table

The BUFFER_PROFILE table defines the buffer profiles. It contains the following fields:

- **pool**: The buffer pool object defined in the BUFFER_POOL table.
- **xon** and **xoff**: The xon and xoff thresholds.
- **size**: The headroom size.
- **dynamic_th**: The maximum proportion of the free size of the buffer pool the port can occupy. The available values of dynamic_th and its corresponding alpha are:
  - **dynamic_th -8**: Alpha 0.
  - **dynamic_th -7**: ~ 6 represents alpha 2\**dynamic_th. For example, dynamic_th 0 represents alpha 1 (2**0 = 1).
  - **dynamic_th 7**:
- **static_th**: The maximum size of the buffer pool the port can occupy.

The table contains the following pre-defined profiles:

- egress_lossless_profile
- egress_lossy_profile
- ingress_lossless_profile
- ingress_lossy_profile

When the switch is running in the dynamic model and it first encounters a new combination of speed and cable length, it creates a new profile and calculates its parameters automatically. You can also configure a static buffer profile.

When the switch is running in the traditional model, it has profiles for lossless traffic that get generated dynamically by querying `pg_profile_lookup.ini` with cable length and speed as the key. The xoff threshold of lossless traffic is determined by the port's cable length, speed and port MTU. The xoff threshold calculation uses the configured port speed and cable length, and the maximum MTU (9100) regardless of the configured value.

This table is referenced by the physical ports (BUFFER_PG) table.

### BUFFER_PG Table

The BUFFER_PG table defines the mapping from port/priority to the buffer profile. It provides the ability to designate a buffer profile for traffic coming from a certain priority group of a port. Typically, priorities 3 and 4 are used for lossless traffic, and other priorities are used for lossy traffic.

When the switch is running in the dynamic model, it is updated automatically when the port's speed, cable length or MTU is updated. By default, the priorities 3 and 4 are used for lossless traffic. You can also configure other PGs as lossless.

When the switch is running in the traditional model, it is updated automatically when the port's speed is updated. If the cable length has been configured, priorities 3 and 4 are always generated for lossless traffic. A new profile is generated accordingly and referenced by the port in BUFFER_PG table when the port's speed is updated. When the port's cable or MTU is updated, no update is made in the BUFFER_PG table.

The BUFFER_PG table can also be modified manually by creating a JSON file and then running `sonic-cfggen -j qos_test_cfg.json --write-to-db`.

### BUFFER_QUEUE Table

The BUFFER_QUEUE table defines the mapping from a port orr queue to egress to the buffer profile. It provides the ability to designate a buffer profile for traffic going through a certain queue of a port. Typically, queue 3 and 4 are used for lossless traffic and others for lossy traffic.

The BUFFER_QUEUE table can be modified manually by creating a JSON file and then running `config qos reload`.

### CABLE_LENGTH Table

THe CABLE_LENGTH table defines the length of the cables connected to the ports of the switch.

When the switch is running in the dynamic model, arbitrary cable lengths are supported. When a port's cable length is updated, the BUFFER_PG is updated automatically.

When the switch is running in the traditional model, only 5m, 40m and 300m cable length values are supported. When updating the cable length of a port, the BUFFER_PG is not updated.

### Buffer Configuration Relationships Diagram

The following diagram shows the relationships within the buffer configuration.

{{<img src="/images/sonic/qos-buffers.png">}}

### Configure a Buffer in the Dynamic Model

When a switch is running in the dynamic model (which is the default in SONiC 202012), you can configure the following:

- Cable length
- Lossless profile for headroom override
- Lossless priorities other than 3 or 4
- Oversubscription ratio for shared headroom pool
- Size of the shared headroom pool

#### Configure Interface Cable Length

To configure the interface's cable length, run the `config interface cable-length <interface_name> <cable_length>` command. The `<cable_length>` is a number appended by the letter *m*, like *5m*.

{{%notice note%}}

There is a limitation for the maximum headroom on each port. When a new cable length is configured on a port, SONiC checks whether the currently accumulated headroom size exceeds the maximum headroom on the port. If it does, the new cable length won't be applied to the switch and an error gets generated in `syslog`. You must specify a shorter cable length.

{{%/notice%}}

For example:

    admin@switch:~$ config interface cable-length Ethernet0 10m 

#### Configure a Buffer Profile

You can configure these buffer profiles:

- *headroom override*: This is a buffer profile with statically configured parameters. If this profile is referenced by a BUFFER_PG entry, the buffer parameters are not dynamically calculated; thus, they won't be updated when the port's configuration changes.

  When you configure a headroom override profile:

  - The `xon` is mandatory.
  - The `xoff` is mandatory if the shared headroom pool is enabled. Otherwise, you can specify either `xoff` or `size`.
  - All other options are not required.

- *non-default dynamic_th*: If this profile is referenced by a BUFFER_PG entry, the buffer parameters are still dynamically calculated when the port's configuration changes, but the `dynamic_th` does not use the default value but uses the one configured in this profile instead.

  To configure a non-default dynamic profile, You need to specify only `dynamic_th`; do not specify any other option.

After creating a new profile, you can modify it using the `config buffer profile set` command. All modification takes effect after you save the configuration. However, you cannot change the type of profile it is &mdash; that is, you cannot change from a headroom override profile to a non-default dynamic_th profile and vice versa.

You create a buffer profile using the following command:

    config buffer profile <add> <set> <remove> <profile_name> <xon> <xoff> <size> <dynamic_th> <pool> 

The command takes these options:

| Option | Description |
| ------ | ----------- |
| add | Creates a new profile. |
| set | Modifies an existing profile. |
| remove | Removes an existing profile. |
| profile_name | The name of the buffer profile. |
| xon | The xon value. This option is required. |
| xoff | The xoff value. This option is required when a shared headroom pool is enabled. You need to specify either the `xoff` or `size` when the shared headroom pool is disabled. |
| size | The size. This option is required. If it is not provided, the system uses the sum of the xon and xoff for the size if a shared headroom pool is enabled. Otherwise, it uses the xon value as the size. |
| dynamic_th | The dynamic TH value. This option is not required. The default value is *0*. |
| pool | The buffer pool for this profile in case you want to use a pool other than `ingress_lossless_pool`. This is not recommended. |

This example creates a headroom override profile called *myHOprofile* with the :

    admin@sonic:~$ config buffer profile add myHOprofile --xon 19456 --xoff 30720 

#### Configure a Lossless Buffer Priority Group

{{%notice note%}}

There is a limitation for the maximum headroom on each port. When a new priority group is configured on a port, SONiC checks whether the currently accumulated headroom size exceeds the maximum headroom on the port. If it does, the new priority group won't be applied to the switch and an error gets generated in `syslog`. You must remove the new priority group with the `config buffer profile remove` command.

{{%/notice%}}

You create a buffer priority group using the `config interface buffer priority-group lossless <add> <set> <remove> <interface> <pg_map> <profile>` command.

The command takes these options:

| Option | Description |
| ------ | ----------- |
| add | Creates a new priority group. |
| set | Modifies an existing priority group. |
| remove | Removes an existing priority group. |
| interface | The name of the interface where you are configuring the priority group. |
| pg_map | The priority group map, like *2* or *3-4*. When adding a new priority group, it should not overlap with any existing priority group. For example, 5 overlaps with 5-6.<br /><br />When setting or removing a priority group, it must be the same group that was already listed in the configuration database. For example, if there is 3-4 configured in configuration database, you can only remove both priorities and to remove 3 or 4 is illegal.<br /><br />If you need to remove one priority from the group, you must remove the entire group and then create a new priority group for the priorities you intend to keep.<br /><br />The `pg_map` is required when you `add` or `set` the group, but is optional when you `remove` a group. If you do not specify the `pg_map` in a remove command means to remove all the lossless priorities on the port. |
| profile | The name of the buffer profile. This option is not required. If you do not specify a buffer profile, then SONiC adds a priority group with the buffer parameters dynamically calculated and the dynamic_th uses the default value. |

This example creates a lossless buffer priority group on interface Ethernet0 with priority group map *5*:

    admin@switch:~$ config interface buffer priority-group lossless add Ethernet0 5

### Shared Headroom Pool

*Headroom* is a dedicated area of buffer introduced to guarantee that the traffic is not lost due to insufficient buffer in case of congestion. By default, the headroom is reserved for each lossless priority group, which means it cannot be occupied by other priority groups even if there is no congestion on that priority group. This guarantees that each priority group always has available headroom in case of congestion. However, as all lossless priority groups can hardly suffer congestion at the same time, it can also waste buffer. The shared headroom pool mechanism addresses this downside.

The idea of the shared headroom pool solution is that the headroom should no longer be reserved for one priority group but should be shared among all the lossless priority groups in the system. Thus an over-subscription ratio is introduced, which indicates the proportion of the priority groups that can be under congestion at the same time. The shared headroom pool size should be calculated as accumulative headroom size (*xoff*) of all lossless priority groups in the system divided by the oversubscription ratio. As all the headroom has been moved to the shared headroom pool, the rest of the accumulative headroom size can be released to the shared buffer pool.

Meanwhile, as the headroom is no longer reserved on a per-priority group basis, the buffer profiles for the lossless priority groups should be adjusted accordingly. By default, the size can be equal to *xon* instead of *xon + xoff*.

The existing buffer profiles for lossless priority groups are in the BUFFER_PROFILE table and follow the naming convention of `pg_lossless_<speed>_<cable-length>_profile`. If a new tuple of speed and cable length appears in the system, the buffer manager fetches related data from a file called `pg_profile_lookup.ini` located in the switch's directory.

The size column should also be adjusted.

#### Configure a Shared Headroom Pool

Calculate the shared headroom pool as follows:

1. Define the oversubscription ratio.
1. Get the headroom pool size:
   1. Calculate the accumulated headroom of all lossless priorities in the system.
   1. Divide the sum by the oversubscription ratio.
1. Configure the BUFFER_POOL and BUFFER_PROFILE tables accordingly.
   1. The size of shared headroom pool is represented by the `xoff` field in the entry `ingress_lossless_pool` in the BUFFER_POOL table.
   1. In the profiles of lossless traffic, the `size` should be equal to `xon` by default.
1. Update the `pg_profile_lookup.ini` file. By default, the `size` column should be the same as the `xon` column.

{{<tabs "Headroom">}}

{{<tab "SONiC CLI">}}

To configure the shared headroom pool, you specify either the oversubscription ratio or size, or both. Although if you specify both, the size takes precedence.

| Option | Description |
| ------ | ----------- |
| ratio | The oversubscription ratio. The ratio should be in this range: [0, number of ports]. Specifying the oversubscription ratio enables the shared headroom pool; the size is calculated by accumulating the xoff of all lossless priorities and dividing the sum by the oversubscription ratio. |
| size | The size of the shared headroom pool. Specifying the size enables the shared headroom pool, using the size as the configured value. |

    admin@switch:~$ sudo config buffer shared-headroom-pool <ratio> <size>

To disable the shared headroom pool, set both `size` and `ratio` to *0*.

{{</tab>}}

{{<tab "config_db.json">}}

Configure the shared headroom pool in the BUFFER_POOL and BUFFER_PROFILE tables in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

{ 
  "BUFFER_POOL": { 
    "ingress_lossless_pool": { 
    "mode": "dynamic", 
    "size": "7719936", 
    “xoff”:”1032192”, 
    "type": "egress" 
    } 
  }, 
  “BUFFER_PROFILE”: { 
    “pg_lossless_50000_40m_profile”: { 
      “xon”: “19456”, 
      “xoff”: “25600”, 
      “size”: “19456”, 
      “pool”: “[BUFFER_POOL|ingress_lossless_pool]” 
    } 
  } 
} 
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

For more information about shared headroom, see the {{<exlink url="https://github.com/Azure/SONiC/blob/415f19931bccd900ac528b100aafffa6000e82e9/doc/qos/dynamically-headroom-calculation.md" text="Azure GitHub documentation">}}.

### Configure a Buffer in the Traditional Model

The traditional model is no longer the default for SONiC 202012. If you configure a switch with this model, you need to manually configure all buffer-related configurations in CONFIG_DB.

#### Create a New Buffer Pool

Typically, there is no need to create a new buffer pool. However, if a new one is required, complete the following steps:

1. Create a JSON file called `qos_test_buffer_pool.json` that contains the buffer pool definition:

       admin@switch:~$ sudo vi qos_test_buffer_pool.json
       {
         "BUFFER_POOL": {
           "egress_lossless_pool": {
           "mode": "dynamic",
           "size": "16777152",
           "type": "egress"
           }
         }
       }
2. Apply the JSON file:

       admin@switch:~$ sudo sonic-cfggen -j qos_test_buffer_pool.json --write-to-db

#### Update the BUFFER_PG Table

The lossless priority group of a port in BUFFER_PG table is updated automatically when the port's speed is updated. For example, when Ethernet0's speed is updated, the entry `Ethernet0|3-4` in BUFFER_PG is updated automatically.

To update the BUFFER_PG table:

1. Create a JSON file called `qos_test_buffer_pg.json`. The JSON array should contain the definition of the new buffer profile; if you decide to reuse a profile that already exists, you don't need to specify it again. It should also contain the definition of the new port or priority group to buffer profile map.

       admin@switch:~$ sudo vi qos_test_buffer_pg.json
       {
         "BUFFER_PROFILE": {
            "ingress_lossy_test_profile": {
            "dynamic_th": "3",
            "pool": "[BUFFER_POOL|ingress_lossy_pool]",
            "size": "0"
            },
         },
         "BUFFER_PG": {
            "Ethernet0|0": {
            "profile": "[BUFFER_PROFILE|ingress_lossy_test_profile]"
            }
         }
       }
2. Shut down interface Ethernet0.

       admin@switch:~$ sudo config interface shutdown Ethernet0
3. Apply the JSON file:

       admin@switch:~$ sonic-cfggen -j qos_test_buffer_pg.json --write-to-db
4. Start up the interface.

       admin@switch:~$ sudo config interface startup Ethernet0

#### Update the BUFFER_PROFILE Table

Due to some restrictions in SONiC, you cannot update a buffer profile on the fly if it is already in use by a port/priority group pair. If you must change a buffer profile, you need to define a new buffer profile and modify the BUFFER_PG entry by pointing to the new buffer profile. See the previous section for instructions.

#### Update the CABLE_LENGTH Table

To update the CABLE_LENGTH table:

1. Create a JSON file called `qos_test_cable_length.json` that contains the new cable length of a port:

       admin@switch:~$ sudo vi qos_test_cable_length.json
       {
         "CABLE_LENGTH":{
           "AZURE":{
             "Ethernet0": "5m"
           }
         }
       }
2. Since the BUFFER_PG table is not updated automatically after you update the cable length, you need to manually save and reload the configuration.

       admin@switch:~$ sudo config save -y
       admin@switch:~$ sudo config reload -y

#### Display the BUFFER_POOL and BUFFER_PROFILE

To display BUFFER_POOL and BUFFER_PROFILE tables, run:

```
admin@switch:~$ mmuconfig -l
 
Pool: ingress_lossless_pool
---- -------
type ingress
mode dynamic
size 2097152
---- -------
Pool: egress_lossless_pool
---- --------
type egress
mode dynamic
size 16777152
---- --------
Pool: ingress_lossy_pool
---- -------
type ingress
mode dynamic
size 5242880
---- -------
Pool: egress_lossy_pool
---- -------
type egress
mode dynamic
size 5242880
---- -------
Profile: q_lossy_profile
---------- -------------------------------
dynamic_th 3
pool [BUFFER_POOL|egress_lossy_pool]
size 0
---------- -------------------------------
Profile: egress_lossy_profile
---------- -------------------------------
dynamic_th 3
pool [BUFFER_POOL|egress_lossy_pool]
size 4096
---------- -------------------------------
Profile: pg_lossless_100000_300m_profile
---------- -----------------------------------
dynamic_th 0
xon 18432
xoff 165888
pool [BUFFER_POOL|ingress_lossless_pool]
size 184320
---------- -----------------------------------
Profile: egress_lossless_profile
---------- ----------------------------------
dynamic_th 7
pool [BUFFER_POOL|egress_lossless_pool]
size 0
---------- ----------------------------------
Profile: ingress_lossless_profile
---------- -----------------------------------
dynamic_th 0
pool [BUFFER_POOL|ingress_lossless_pool]
size 0
---------- -----------------------------------
Profile: pg_lossless_50000_40m_profile
---------- -----------------------------------
dynamic_th 0
xon 18432
xoff 23552
pool [BUFFER_POOL|ingress_lossless_pool]
size 41984
---------- -----------------------------------
Profile: pg_lossless_100000_40m_profile
---------- -----------------------------------
dynamic_th 0
xon 18432
xoff 35840
pool [BUFFER_POOL|ingress_lossless_pool]
size 54272
---------- -----------------------------------
Profile: ingress_lossy_profile
---------- --------------------------------
dynamic_th 3
pool [BUFFER_POOL|ingress_lossy_pool]
size 0
---------- --------------------------------
admin@sonic:~$
```

## ECN and WRED

*Weighted Random Early Detection* (WRED) and Random Early Detection (RED) are mechanisms that improve TCP flow behavior when congestion occurs in the network by dropping packets before the buffer becomes full, causing packets to drop. The basis of these mechanisms is to enable random packets to drop upon congestion in the switch. WRED is an extension of the RED mechanism, and enables a different configuration of RED for different traffic profiles.

By using WRED minimum and maximum thresholds, a maximum probability can be configured for each color. The probability at which the traffic is dropped depends on the length of the queue:

- If it is less than the minimum threshold, there is no drop.
- If it is between the minimum and maximum threshold, the drop probability is calculated as: maximum_probability * (queue_length – minimum_threshold) / (maximum_threshold – minimum_threshold).
- If it is greater than the maximum threshold, the drop probability is 100%.

*Explicit Congestion Notification* (ECN) is defined by {{<exlink url="https://tools.ietf.org/html/rfc3168" text="RFC 3168">}}. It is used for congestion control protocols (TCP and RoCE CC – DCQCN) to handle congestion before packets are dropped. When congestion is identified, a switch may send a forward notification by marking its packet at the layer 3 header. Further actions may be taken by the destination in order to let the source know about it, and in its turn to handle the congestion. The decision whether to mark packets with ECN is like the drop decision of the WRED.

On SONiC, you configure the WRED and ECN on a per-queue basis.

### Configure the WRED Profile

The WRED_PROFILE table includes the following fields:

- `green_max_threshold`, `yellow_max_threshold` and `red_max_threshold`: These fields represent the maximum threshold for traffic marked as green, yellow or red, respectively. If the number of bytes accumulated in the queue exceeds the threshold, 100% of the traffic is lost.
- `green_min_threshold`, `yellow_min_threshold` and `red_min_threshold`: These fields represent the minimum threshold for traffic marked as green, yellow or red, respectively. If the number of bytes accumulated in the queue exceeds the threshold, the traffic starts to be lost.
- `green_drop_probability`, `yellow_drop_probability` and `red_drop_probability`: These fields represent the maximum drop priority for the traffic marked as that color.
- `ecn`: ECN works on any color. It can be any color or any composition of the colors, like: ecn_all, ecn_none, ecn_red, ecn_yellow_red, etc.

The available options are listed below:

| Option | Description |
| ------ | ----------- |
| -gmin GREEN_MIN, --green-min GREEN_MIN | Sets the minimum threshold for packets marked *green*. |
| -gmax GREEN_MAX, --green-max GREEN_MAX | Sets the maximum threshold for packets marked *green*. |
| -ymin YELLOW_MIN, --yellow-min YELLOW_MIN | Sets the minimum threshold for packets marked *yellow*. |
| -ymax YELLOW_MAX, --yellow-max YELLOW_MAX | Sets the maximum threshold for packets marked *yellow*. |
| -rmin RED_MIN, --red-min RED_MIN | Sets the minimum threshold for packets marked *red*. |
| -rmax RED_MAX, --red-max RED_MAX | Sets the maximum threshold for packets marked *red*. |
| -gdrop GREEN_DROP_PROB, --green-drop-prob GREEN_DROP_PROB | Sets the maximum drop/mark probability for packets marked *green*. |
| -ydrop YELLOW_DROP_PROB, --yellow-drop-prob YELLOW_DROP_PROB | Sets the maximum drop/mark probability for packets marked *yellow*. |
| -rdrop RED_DROP_PROB, --red-drop-prob RED_DROP_PROB | Sets the maximum drop/mark probability for packets marked *red*. |
| -p PROFILE | The name of the profile. This field is required. |

Once a WRED profile has been added to the system, it can also be updated by using the `ecnconfig` command:

```
admin@sonic:~$ ecnconfig -l

Profile: AZURE_LOSSLESS
-----------------------  -------
red_max_threshold        2097152
red_drop_probability     5
yellow_max_threshold     2097152
ecn                      ecn_all
green_min_threshold      1048576
red_min_threshold        1048576
wred_yellow_enable       true
yellow_min_threshold     1048576
green_max_threshold      2097152
green_drop_probability   5
wred_green_enable        true
yellow_drop_probability  5
wred_red_enable          true
-----------------------  -------
```

To configure the WRED_PROFILE table:

1. Create a JSON file called `qos_wred_test.json` that contains the profile information.

       admin@switch:~$ sudo vi qos_wred_test.json
       {
          "WRED_PROFILE": {
               "NEW_PROFILE": {
                   "ecn": "ecn_all",
                   "green_drop_probability": "5",
                   "green_max_threshold": "2097152",
                   "green_min_threshold": "1048576",
                   "red_drop_probability": "5",
                   "red_max_threshold": "2097152",
                   "red_min_threshold": "1048576",
                   "wred_green_enable": "true",
                   "wred_red_enable": "true",
                   "wred_yellow_enable": "true",
                   "yellow_drop_probability": "5",
                   "yellow_max_threshold": "2097152",
                   "yellow_min_threshold": "1048576"
               }
           }
       }
2. Load the JSON file into the config database.

       admin@switch:~$ sudo sonic-cfggen -j qos_wred_test.json --write-to-db

### Configure the Queue

Configuring a queue involves referencing the WRED_PROFILE table in the `wred_profile` field.

To configure the QUEUE table:

1. Create a JSON file called `qos_queue_test.json` that contains the queue and new WRED profile information.

       admin@switch:~$ sudo vi qos_queue_test.json
       {
          "QUEUE": {
               "Ethernet0|3": {
                   "wred_profile": "[WRED_PROFILE|NEW_PROFILE]"
               }
           }
       }
2. Load the JSON file into the config database.

       admin@switch:~$ sudo sonic-cfggen -j qos_queue_test.json --write-to-db

## Priority Flow Control - PFC

*Priority flow control* (PFC) provides an enhancement to the existing pause mechanism in Ethernet. The current Ethernet pause option stops all traffic on a link. PFC creates eight separate virtual links on the physical link and allows any of these links to be paused and restarted independently, enabling the network to create a lossless class of service for an individual virtual link.

PFC oversees:

- Mapping of an incoming packet to a priority according to its DSCP value or IEEE priority.
- Mapping of the priority to an egress queue.
- Sending a PFC frame for lossless priority if it runs out of headroom.
- Ceasing the egress queue on receiving a PFC frame.

These operations depend on the mappings among queue, priorities and DSCP, which are defined below.

### CONFIG_DB Tables

PFC uses the following tables in CONFIG_DB:

| Table | Description |
| ----- | ----------- |
| TC_TO_QUEUE_MAP | In the egress direction, maps the traffic class to an egress queue. |
| DSCP_TO_TC_MAP | In the ingress direction, maps the DSCP field in an IP packet into a traffic class. By utilizing this table and the TC_TO_QUEUE_MAP table, a packet can be mapped from its DSCP field to the egress queue. In case there is a congestion in the egress queue, the back-pressure mechanism is triggered, and the PFC frame can be sent. The priority in the PFC frame is determined by TC to priority group mapping table. |
| MAP_PFC_PRIORITY_TO_QUEUE | Maps the priority in the received PFC frames to an egress queue so that the switch knows which egress to resume or pause. |
| PFC_PRIORITY_TO_PRIORITY_GROUP_MAP | Maps PFC priority to a priority group. |
| TC_TO_PRIORITY_GROUP_MAP | Maps the PFC priority to a priority group and enables the switch to set the PFC priority in xon/xoff frames in order to resume/pause corresponding egress queue at the link peer. |
| PORT_QOS_MAP | Defines the mappings adopted by a port, including:<br />- `tc_to_queue_map`, default value is TC_TO_QUEUE_MAP\|AZURE<br />- `dscp_to_tc_map`, default value is DSCP_TO_TC_MAP\|AZURE<br />- `pfc_to_queue_map`, default value is MAP_PFC_PRIORITY_TO_QUEUE\|AZURE<br />- `pfc_to_pg_map`, default value is PFC_PRIORITY_TO_PRIORITY_GROUP_MAP\|AZURE<br />- `tc_to_pg_map`, default value is TC_TO_PRIORITY_GROUP_MAP|AZURE<br />- `pfc_enable`, on which priorities are PFC enabled. |

### Configure PFC

All the mapping tables are simple integer-to-integer mappings.

To update the mappings:

1. Create a temporary JSON file containing the new port mapping configuration.

   ```
   admin@switch:~$ sudo vi new_cfg.json
   { 
     "DSCP_TO_TC_MAP": { 
        "AZURE": { 
            "0": "1",  
            "1": "1",  
            "2": "1",  
            "3": "3",  
            "4": "4",  
            "5": "2",  
            "6": "1",  
            "7": "1",  
            "8": "0",  
            "9": "1",  
            "10": "1",  
            "11": "1",
            "12": "1",  
            "13": "1",  
            "14": "1",  
            "15": "1",  
            "16": "1",
            "17": "1",  
            "18": "1",  
            "19": "1",  
            "20": "1",  
            "21": "1",  
            "22": "1",  
            "23": "1",  
            "24": "1",  
            "25": "1", 
            "26": "1",  
            "27": "1",  
            "28": "1",  
            "29": "1",  
            "30": "1",  
            "31": "1",  
            "32": "1",  
            "33": "1",  
            "34": "1",  
            "35": "1",  
            "36": "1",  
            "37": "1",  
            "38": "1",  
            "39": "1",  
            "40": "1",  
            "41": "1",  
            "42": "1",  
            "43": "1",  
            "44": "1",  
            "45": "1", 
            "46": "5",  
            "47": "1",  
            "48": "6",  
            "49": "1",  
            "50": "1",  
            "51": "1",  
            "52": "1",  
            "53": "1",  
            "54": "1",  
            "55": "1",  
            "56": "1",  
            "57": "1",  
            "58": "1",  
            "59": "1",  
            "60": "1",  
            "61": "1",  
            "62": "1",  
            "63": "1" 
        } 
      },  

      "MAP_PFC_PRIORITY_TO_QUEUE": { 
        "AZURE": { 
            "0": "0",  
            "1": "1",  
            "2": "2",  
            "3": "3",  
            "4": "4",  
            "5": "5",  
            "6": "6",  
            "7": "7" 
        } 
      },  

      "PFC_PRIORITY_TO_PRIORITY_GROUP_MAP": { 
        "AZURE": { 
            "3": "3",  
            "4": "4" 
        } 
      },  

      "PORT_QOS_MAP": { 
        "Ethernet0": { 
            "dscp_to_tc_map": "[DSCP_TO_TC_MAP|AZURE]",  
            "pfc_enable": "3,4",  
            "pfc_to_pg_map": "[PFC_PRIORITY_TO_PRIORITY_GROUP_MAP|AZURE]",  
            "pfc_to_queue_map": "[MAP_PFC_PRIORITY_TO_QUEUE|AZURE]",  
            "tc_to_pg_map": "[TC_TO_PRIORITY_GROUP_MAP|AZURE]",  
            "tc_to_queue_map": "[TC_TO_QUEUE_MAP|AZURE]" 
        } 
      },  

      "SCHEDULER": { 
        "scheduler.0": { 
            "type": "DWRR",  
            "weight": "14" 
        },  
        "scheduler.1": { 
            "type": "DWRR",  
            "weight": "15" 
        } 
      },  

      "TC_TO_PRIORITY_GROUP_MAP": { 
        "AZURE": { 
            "0": "0",  
            "1": "0",  
            "2": "0",  
            "3": "3",  
            "4": "4",  
            "5": "0",  
            "6": "0",  
            "7": "7" 
        } 
      },  

      "TC_TO_QUEUE_MAP": { 
        "AZURE": { 
            "0": "0",  
            "1": "1",  
            "2": "2",  
            "3": "3",  
            "4": "4",  
            "5": "5",  
            "6": "6", 
            "7": "7" 
        } 
      }
    }
    ```
2. Deploy the new configuration:

       admin@switch:~$ sudo sonic-cfggen -j new_cfg.json -w

## Update Buffers and QoS Configuration Using Templates

Buffers and QoS configuration can be rendered from templates. If you are going to update the configuration of the entire switch in batch mode, follow the steps below:

1. Modify the templates:

   1. For buffer configuration, modify the `/usr/share/sonic/templates/buffers_config.j2` file.
   1. For QoS configuration, modify the `/usr/share/sonic/templates/qos_config.j2` file.
1. Reload the QoS configuration:

       admin@switch:~$ sudo config qos reload -y

{{%notice info%}}

Due to a limitation, the `config qos reload` command fails. To solve the issue, follow these steps:

1. Reload the QoS configuration:

       admin@switch:~$ sudo config qos reload -y
2. Save the configuration:

       admin@switch:~$ sudo config save -y
3. Reload the SONiC configuration:

       admin@switch:~$ sudo config reload -y

{{%/notice%}}
