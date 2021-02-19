---
title: QoS and Buffers
author: Cumulus Networks
weight: 350
product: SONiC
version: 4.0
siteSlug: sonic
---

For specific buffer configuration for non-existing SKUs, contact Mellanox Support.  

## Configuring the Buffers

Buffer configuration includes:

- Buffer pool size: Represents the maximum memory a certain kind of traffic can occupy
- Buffer profile: In general, most of ports can share the same buffer configuration. Buffer profile is created for that and will be attached to the port
- Buffer PG: Represents the profile for each ingress priority
- Buffer queue: Represents the profile for each egress queue

All the buffer configuration is stored in the following tables.

### CONFIG_DB Tables

| Tables | Description |
| ------ | ----------- |
| BUFFER_POOL | Defines the buffer pools for lossless/lossy and ingress/egress. The following fields are included:<br />- size, the size of the buffer pool<br />- type, egress or ingress<br />- mode, static or dynamic<br />There are four predefined buffer pools:<br />- egress_lossless_pool<br />- egress_lossy_pool<br />- ingress_lossless_pool<br />- ingress_lossy_pool<br />**Note:** As they typically are predefined, there is no need to define a new buffer pool or to modify them on the fly.<br />Buffer size<br />- The size of egress_lossless_pool is always the maximum available memory<br />- The size of all other pools is the quantity of the accumulative per port/PG/queue reserved buffer size subtracted from the maximum available buffer size.<br />Default buffer configuration is provided for ToR and leaf router scenario. The difference between them is the ports’ speed and cable length which affects the per PG reserved buffer size:<br />- In ToR scenario, we assume there are 28 ports with 5m cable and 4 ports with 40m cable<br />- In leaf router scenario, we assume there are 16 ports with 40m cable and 16 ports with 300m cable<br />- All ports run at the highest speed<br />Referenced by BUFFER_PROFILE |
| BUFFER_PROFILE | Defines the buffer profiles which includes the following fields:<br />- pool, representing the buffer pool object which is defined in BUFFER_POOL table.<br />- xon and xoff, representing the xon and xoff threshold.<br />- size, the headroom size.<br />- dynamic_th, indicating the max proportion of the free size of the buffer pool the port can occupy. The available values of dynamic_th and its corresponding alpha are listed below:<br />* dynamic_th -8 represents alpha 0<br />* dynamic_th -7 ~ 6 represents alpha 2\**dynamic_th<br />For example: dynamic_th 0 represents alpha 1 (2**0 = 1).<br />* dynamic_th 7 represents alpha INFINITY<br />- static_th, representing the max size of the buffer pool the port can occupy.<br />Predefined profiles include:<br />- egress_lossless_profile<br />- egress_lossy_profile<br />- ingress_lossless_profile<br />- ingress_lossy_profile.<br />Other profiles are for lossless traffic and generated dynamically by looking up from pg_profile_lookup.ini with cable length and speed as the key. The "xoff" threshold of lossless traffic is determined by the port’s cable length, speed and MTU. "xoff" threshold calculation uses the configured port speed and cable length, and the maximum MTU (which is 9100) regardless of the configured value.<br /><br />Referenced by physical ports (BUFFER_PG) |
| BUFFER_PG | Defines the mapping from (port, priority) to the buffer profile.<br /><br />Provides ability to designate a buffer profile for traffic coming from a certain priority group of a port.<br /><br />Typically, priorities 3 and 4 are used for lossless traffic and others for lossy traffic.<br /><br />It is updated automatically when the port's speed is updated. If the cable length has been configured, priorities 3 and 4 will always be generated for lossless traffic at this time.<br /><br />A new profile will be generated accordingly and referenced by the port in BUFFER_PG table when the port’s speed is updated. No such update in BUFFER_PG table when port’s cable or MTU is updated.<br /><br />It can also be modified manually by composing a json file and then executing "sonic-cfggen -j qos_test_cfg.json --write-to-db" |
| BUFFER_QUEUE | Defines the mapping from (Port, queue) to (egress) to the buffer profile.<br />Provides ability to designate a buffer profile for traffic going through a certain queue of a port.<br /><br />Typically, queue 3 and 4 are used for lossless traffic and others for lossy traffic.<br /><br />It can be modified manually by composing a json file and then executing "config qos reload" |
| CABLE_LENGTH | Defines the length of the cables connected to the ports of the switch.<br />Only values 5m, 40m and 300m are supported for now.<br /><br />When updated the cable length of a port, the BUFFER_PG will not be updated. |

{{<img src="/images/sonic/qos-buffers.png">}}

### Configuring the Buffers

#### Creating a New Buffer Pool

Typically, there is no need to create a new buffer pool. However, if a new one is required, it can be done as described in the steps below.

To create a new buffer pool:

1. Compose a json file (qos_test_buffer_pool.json) which contains the definition of the pool:

       {
         "BUFFER_POOL": {
           "egress_lossless_pool": {
           "mode": "dynamic",
           "size": "16777152",
           "type": "egress"
           }
         }
       }
2. Apply the json file:

       sonic-cfggen -j qos_test_buffer_pool.json --write-to-db

#### Updating the BUFFER_PG Table

The lossless priority group of a port in BUFFER_PG table will be updated automatically when the port's speed is updated. For example, when Ethernet0's speed is updated, the entry "Ethernet0|3-4" in BUFFER_PG will be updated automatically.

To update the BUFFER_PG table:

1. Compose a json file (qos_test_buffer_pg.json) which contains:

   - the definition of the new buffer profile. If you decide to reuse the profile that already exists, this can be skipped
   - the definition of the new (port, pg) to buffer profile map

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
2. Shut down the interface Ethernet0.
3. Apply the json file:

       sonic-cfggen -j qos_test_buffer_pg.json --write-to-db
4. Startup the interface.

#### Updating the BUFFER_PROFILE Table

Due to some restrictions, a buffer profile cannot be modified on the fly if it has already been used by some (port, priority group) pair. If you decide to do that, you have to define a new buffer profile and modify the BUFFER_PG entry by pointing to the new buffer profile. See Updating the BUFFER_PG Table section for instructions on how to do so.

#### Updating the CABLE_LENGTH Table

To update the CABLE_LENGTH table:

1. Compose a json file (qos_test_cable_length.json) containing the new cable length of a port:

       {
         "CABLE_LENGTH":{
           "AZURE":{
             "Ethernet0": "5m"
           }
         }
       }
2. Since the BUFFER_PG table is not updated automatically after the cable length is updated, manual update is required as described the following steps:

   a. Save configuration
   b. Reload configuration

#### Displaying BUFFER_POOL and BUFFER_PROFILE

To display BUFFER_POOL and BUFFER_PROFILE:

```
admin@sonic:~$ mmuconfig -l
 
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

## Configuring ECN

###	CONFIG_DB Tables

| Tables | Description |
| ------ | ----------- |
| WRED_PROFILE | Defines the WRED profiles. The following fields are included:<br />- green_max_threshold, yellow_max_threshold and red_max_threshold, representing the max threshold for traffic marked as green, yellow or red respectively. If the number of bytes accumulated in the queue exceeds the threshold, the traffic will be 100% lost.<br />- green_min_threshold, yellow_min and red_min_threshold, representing the min threshold for traffic marked as yellow, green and red respectively. If the number of bytes accumulated in the queue exceeds the threshold, the traffic will start to be lost.<br />- green_drop_probability, yellow_drop_probability and red_drop_probability, representing the maximum drop priority for the traffic marked as that color.<br />Referenced by QUEUE table |
| QUEUE | Reference WRED_PROFILE table by field "wred_profile" |

## Configuring WRED

To update WRED_PROFILE table:

1. Compose a json file (qos_wred_test.json) which contains the profile info.

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
2. Load the json file to the config database.

       sonic-cfggen -j qos_wred_test.json --write-to-db

WRED profiles can also be configured using the CLI command “ecnconfig”. The available options are listed below:

| Option | Description |
| ------ | ----------- |
| -gmin GREEN_MIN, --green-min GREEN_MIN | set min threshold for packets marked 'green' |
| -gmax GREEN_MAX, --green-max GREEN_MAX | set max threshold for packets marked 'green' |
| -ymin YELLOW_MIN, --yellow-min YELLOW_MIN | set min threshold for packets marked 'yellow' |
| -ymax YELLOW_MAX, --yellow-max YELLOW_MAX | set max threshold for packets marked 'yellow' |
| -rmin RED_MIN, --red-min RED_MIN | set min threshold for packets marked 'red' |
| -rmax RED_MAX, --red-max RED_MAX | set max threshold for packets marked 'red' |
| -gdrop GREEN_DROP_PROB, --green-drop-prob GREEN_DROP_PROB | set max drop/mark probability for packets marked 'green' |
| -ydrop YELLOW_DROP_PROB, --yellow-drop-prob YELLOW_DROP_PROB | set max drop/mark probability for packets marked 'yellow' |
| -rdrop RED_DROP_PROB, --red-drop-prob RED_DROP_PROB | set max drop/mark probability for packets marked 'red' |
| -p PROFILE | The name of the profile. It must exist. | 

To update the QUEUE table:

1. Compose a json file which contains the queue and new WRED profile info. 

       {
          "QUEUE": {
               "Ethernet0|3": {
                   "wred_profile": "[WRED_PROFILE|NEW_PROFILE]"
               }
           }
       }
2. Load the json file into the config database.

## Configuring PFC

PFC oversees:
- Mapping of an incoming packet to a priority according to its DSCP value or IEEE priority
- Mapping of the priority to an egress queue
- Sending a PFC frame for lossless priority if it runs out of headroom
- Ceasing the egress queue on receiving a PFC frame.

These operations depend on the mappings among queue, priorities and DSCP, which are defined below.

### CONFIG_DB Tables

| Tables | Description |
| ------ | ----------- |
| TC_TO_QUEUE_MAP | In the egress direction, maps the traffic class to an egress queue. |
| DSCP_TO_TC_MAP | In the ingress direction, maps the DSCP field in an IP packet into a traffic class. |
| MAP_PFC_PRIORITY_TO_QUEUE | Maps the priority in the received PFC frames to an egress queue so that the switch knows which egress to resume/pause. |
| PFC_PRIORITY_TO_PRIORITY_GROUP_MAP | Maps PFC priority to priority group. |
| TC_TO_PRIORITY_GROUP_MAP | Allows the switch to set the PFC priority in xon/xoff frames in order to resume/pause corresponding egress queue at the link peer. |
| PORT_QOS_MAP | Defines the mappings adopted by a port, including:<br />- tc_to_queue_map, default value is TC_TO_QUEUE_MAP\|AZURE<br />- dscp_to_tc_map, default value is DSCP_TO_TC_MAP\|AZURE<br />- pfc_to_queue_map, default value is MAP_PFC_PRIORITY_TO_QUEUE\|AZURE<br />- pfc_to_pg_map, default value is PFC_PRIORITY_TO_PRIORITY_GROUP_MAP\|AZURE<br />- tc_to_pg_map, default value is TC_TO_PRIORITY_GROUP_MAP|AZURE<br />- pfc_enable, on which priorities is pfc enabled |

### Configuring PFC

All the mapping tables are simple integer-to-integer mappings.

To update the mappings:
1. Compose a temporary json file containing the new config.
2. Deploy by using "sonic-cfggen -j new_cfg.json -w".

## Updating the Buffers and QoS Configuration using Templates

Buffers and QoS configuration can be rendered from templates. If you are going to update the configuration of the entire switch in batch mode, follow the steps below:

1. Modify the templates:
   1. For buffer configuration, modify the /usr/share/sonic/templates/buffers_config.j2
   1. For QoS configuration, modify the /usr/share/sonic/templates/qos_config.j2
2. Reload qos config by executing "config qos reload"

{{%notice info%}}

Due to a limitation, the "config qos reload" command fails. to solve the issue, follow the steps below:

1. Execute "config qos reload"
2. Execute "config save"
3. Execute "config reload"

{{%/notice%}}
