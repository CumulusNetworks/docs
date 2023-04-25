---
title: Precision Time Protocol - PTP
author: NVIDIA
weight: 128
toc: 3
---
Cumulus Linux supports IEEE 1588-2008 Precision Timing Protocol (PTPv2), which defines the algorithm and method for synchronizing clocks of various devices across packet-based networks, including Ethernet switches and IP routers.

PTP is capable of sub-microsecond accuracy. The clocks are in a master-slave hierarchy, where the slaves synchronize to their masters, which can be slaves to their own masters. The best master clock (BMC) algorithm, which runs on every clock, creates and updates the hierarchy automatically. The grandmaster clock is the top-level master. To provide a high-degree of accuracy, a Global Positioning System (GPS) time source typically synchronizes the grandmaster clock.

In the following example:
- Boundary clock 2 receives time from Master 1 (the grandmaster) on a PTP slave port, sets its clock and passes the time down from the PTP master port to Boundary clock 1. 
- Boundary clock 1 receives the time on a PTP slave port, sets its clock and passes the time down the hierarchy through the PTP master ports to the hosts that receive the time.

{{< img src = "/images/cumulus-linux/date-time-ptp-example.png" >}}

## Cumulus Linux and PTP

PTP in Cumulus Linux uses the `linuxptp` package that includes the following programs:
- `ptp4l` provides the PTP protocol and state machines
- `phc2sys` provides PTP Hardware Clock and System Clock synchronization
- `timemaster` provides System Clock and PTP synchronization

Cumulus Linux supports:
- PTP boundary clock mode only (the switch provides timing to downstream servers; it is a slave to a higher-level clock and a master to downstream clocks).
- Both IPv4 and IPv6 UDP PTP encapsulation.
- Only a single PTP domain per network.
- PTP on layer 3 interfaces, trunk ports, bonds, and switch ports belonging to a VLAN.
- Multicast, unicast, and mixed message mode.
- End-to-End delay mechanism only. Cumulus Linux does not support Peer-to-Peer.
- Two-step clock correction mode, where PTP notes the time when the packet goes out of the port and sends the time in a separate (follow-up) message. Cumulus Linux does not support one-step mode.
- Hardware time stamping for PTP packets. This allows PTP to avoid inaccuracies caused by message transfer delays and improves the accuracy of time synchronization.

{{%notice note%}}
- On NVIDIA switches with Spectrum-2 and later, PTP is not supported on 1G interfaces.
- You cannot run *both* PTP and NTP on the switch.
- PTP supports the default VRF only.
{{%/notice%}}

## Basic Configuration

Basic PTP configuration requires you:

- Enable PTP on the switch.
- Configure PTP on at least one interface; this can be a layer 3 routed port, switch port, or trunk port. You do not need to specify which is a master interface and which is a slave interface; the PTP Best Master Clock Algorithm (BMCA) determines the master and slave.

{{%notice note%}}
If you configure PTP with Linux commands, you must also enable PTP timestamping; see step 1 of the Linux procedure below. NVUE enables PTP timestamping automatically; you do not have to run any NVUE commands to enable PTP timestamping.
{{%/notice%}}

The basic configuration shown below uses the *default* PTP settings:
- The clock mode is Boundary. This is the only clock mode that Cumulus Linux supports.
- {{<link url="#clock-domains" text="The PTP clock domain">}} is 0.
- {{<link url="#ptp-priority" text="PTP Priority1 and Priority2">}} are both 128.
- {{<link url="#dscp" text="The DSCP" >}} is 46 for both general and event messages.
- {{<link url="#Transport-mode" text="The PPT interface transport mode">}} is IPv4.
- {{<link url="#Forced-master-mode" text="Announce messages from any master are accepted">}}.
- {{<link url="#Message-mode" text="The PTP Interface Message Mode">}} is multicast.
- The delay mechanism is End-to-End (E2E), where the slave measures the delay between itself and the master. The master and slave send delay request and delay response messages between each other to measure the delay.
- The hardware packet time stamping mode is two-step.

To configure optional settings, such as the PTP profile, domain, priority, and DSCP, the PTP interface transport mode and timers, and PTP monitoring, see the Optional Configuration sections below.

{{< tabs "TabID65 ">}}
{{< tab "NVUE Commands ">}}

The NVUE `nv set service ptp` commands require an instance number (1 in the example command below) for management purposes.

{{%notice warning%}}
When you enable the PTP service with the `nv set service ptp <instance> enable on` command, NVUE restarts the `switchd` service, which causes all network ports to reset in addition to resetting the switch hardware configuration.
{{%/notice%}}

{{< tabs "TabID68 ">}}
{{< tab "Layer 3 Routed Port ">}}

```
cumulus@switch:~$ nv set service ptp 1 enable on
cumulus@switch:~$ nv set interface swp1 ip address 10.0.0.9/32
cumulus@switch:~$ nv set interface swp2 ip address 10.0.0.10/32
cumulus@switch:~$ nv set interface swp1 ptp enable on
cumulus@switch:~$ nv set interface swp2 ptp enable on
cumulus@switch:~$ nv config apply
```

The configuration writes to the `/etc/ptp4l.conf` file.

{{< /tab >}}
{{< tab "Trunk Port VLAN ">}}

```
cumulus@switch:~$ nv set service ptp 1 enable on
cumulus@switch:~$ nv set bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default type vlan-aware
cumulus@switch:~$ nv set bridge domain br_default vlan 10-30
cumulus@switch:~$ nv set bridge domain br_default vlan 10 ptp enable on
cumulus@switch:~$ nv set interface vlan10 type svi
cumulus@switch:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ nv set interface swp1 bridge domain br_default
cumulus@switch:~$ nv set interface swp1 bridge domain br_default vlan 10
cumulus@switch:~$ nv set interface swp1 ptp enable on
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- You can configure only one address; either IPv4 or IPv6.
- For IPv6, set the trunk port transport mode to ipv6.
{{%/notice%}}

The configuration writes to the `/etc/ptp4l.conf` file.

{{< /tab >}}
{{< tab "Switch Port (Access Port) VLAN ">}}

```
cumulus@switch:~$ nv set service ptp 1 enable on
cumulus@switch:~$ nv set bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default type vlan-aware
cumulus@switch:~$ nv set bridge domain br_default vlan 10-30
cumulus@switch:~$ nv set bridge domain br_default vlan 10 ptp enable on
cumulus@switch:~$ nv set interface vlan10 type svi
cumulus@switch:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ nv set interface swp2 bridge domain br_default
cumulus@switch:~$ nv set interface swp2 bridge domain br_default access 10
cumulus@switch:~$ nv set interface swp2 ptp enable on
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- You can configure only one address; either IPv4 or IPv6.
- For IPv6, set the trunk port transport mode to ipv6.
{{%/notice%}}

The configuration writes to the `/etc/ptp4l.conf` file.

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/switchd.d/ptp.conf` file to set the `ptp.timestamping` parameter to `TRUE`:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/ptp.conf
   ...
   ptp.timestamping     TRUE
   ...
   ```

2. Restart the `switchd` service:

   ```
   cumulus@switch:~$ sudo systemctl restart switchd.service
   ```

   {{%notice warning%}}
Restarting the `switchd` service causes all network ports to reset in addition to resetting the switch hardware configuration.
{{%/notice%}}

3. Enable and start the ptp4l and phc2sys services:

    ```
    cumulus@switch:~$ sudo systemctl enable ptp4l.service phc2sys.service
    cumulus@switch:~$ sudo systemctl start ptp4l.service phc2sys.service
    ```

4. Edit the `Default interface options` section of the `/etc/ptp4l.conf` file to configure the interfaces on the switch that you want to use for PTP.

   ```
   cumulus@switch:~$ sudo nano /etc/ptp4l.conf
   ...
   [global]
   #
   # Default Data Set
   #
   slaveOnly               0
   priority1               128
   priority2               128
   domainNumber            0
   
   dscp_event              46
   dscp_general            46
   network_transport              L2
   dataset_comparison             G.8275.x
   G.8275.defaultDS.localPriority 128
   ptp_dst_mac                    01:80:C2:00:00:0E

   #
   # Port Data Set
   #
   logAnnounceInterval            -3
   logSyncInterval                -4
   logMinDelayReqInterval         -4
   announceReceiptTimeout         3
   delay_mechanism                E2E

   offset_from_master_min_threshold   -50
   offset_from_master_max_threshold   50
   mean_path_delay_threshold          200
   tsmonitor_num_ts                   100
   tsmonitor_num_log_sets             3
   tsmonitor_num_log_entries          4
   tsmonitor_log_wait_seconds         1

   #
   # Run time options
   #
   logging_level           6
   path_trace_enabled      0
   use_syslog              1
   verbose                 0
   summary_interval        0
   
   #
   # servo parameters
   #
   pi_proportional_const          0.000000
   pi_integral_const              0.000000
   pi_proportional_scale          0.700000
   pi_proportional_exponent       -0.300000
   pi_proportional_norm_max       0.700000
   pi_integral_scale              0.300000
   pi_integral_exponent           0.400000
   pi_integral_norm_max           0.300000
   step_threshold                 0.000002
   first_step_threshold           0.000020
   max_frequency                  900000000
   sanity_freq_limit              0
   
   #
   # Default interface options
   #
   time_stamping                  software
   
   
   # Interfaces in which ptp should be enabled
   # these interfaces should be routed ports
   # if an interface does not have an ip address
   # the ptp4l will not work as expected.
   
   [swp1]
   udp_ttl                 1
   masterOnly              0
   delay_mechanism         E2E
   
   [swp2]
   udp_ttl                 1
   masterOnly              0
   delay_mechanism         E2E
   ```
   
   For a trunk VLAN, add the VLAN configuration to the switch port stanza: set `l2_mode` to `trunk`, `vlan_intf` to the VLAN interface, and `src_ip` to    the IP adress of the VLAN interface:
   
   ```
   [swp1]
   l2_mode                 trunk
   vlan_intf               vlan10
   src_ip                  10.1.10.2
   udp_ttl                 1
   masterOnly              0
   delay_mechanism         E2E
   network_transport       UDPv4
   ```
   
   For a switch port VLAN, add the VLAN configuration to the switch port stanza: set `l2_mode` to `access`, `vlan_intf` to the VLAN interface, and    `src_ip` to the IP adress of the VLAN interface:
   
   ```
   [swp2]
   l2_mode                 access
   vlan_intf               vlan10
   src_ip                  10.1.10.2
   udp_ttl                 1
   masterOnly              0
   delay_mechanism         E2E
   network_transport       UDPv4
   ```

5. Restart the `ptp4l` service:

    ```
    cumulus@switch:~$ sudo systemctl restart ptp4l.service
    ```

{{< /tab >}}
{{< /tabs >}}

## Optional Global PTP Configuration

### PTP Profiles

PTP profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

Cumulus Linux supports the following predefined profiles:

|  | IEEE 1588 | ITU 8275-1 | ITU 8275-2 |
| --------- | --------- | ---------- | ---------- |
| **Application** | Enterprise | Mobile Networks | Mobile Networks |
| **Transport** | Layer 2 and Layer 3  | Layer 2 | Layer 3 |
| **Encapsulation** | 802.3, UDPv4, or UDPv6 | 802.3 | UDPv4 or UDPv6 |
| **Transmission** | Unicast and Multicast  | Multicast | Unicast |
| **Supported Clock Types** | Boundary Clock  | Boundary Clock | Boundary Clock |

{{%notice note%}}
- You cannot modify the predefined profiles. If you want to set a parameter to a different value in a predefined profile, you need to create a custom profile. You can modify a custom profile within the range applicable to the profile type.
- You cannot set the current profile to a profile not yet created.
- You cannot set global PTP parameters in the currently set profile.
- PTP profiles do not support VLANs and bonds. You must configure profile settings individually for each bond or VLAN.
- If you set a predefined or custom profile, do not change any global PTP settings, such as the DiffServ code point (DSCP) or the clock domain.
- For better performance in a high scale network with PTP on multiple interfaces, configure a higher system policer rate with the `nv set system control-plane policer lldp burst <value>` and `nv set system control-plane policer lldp rate <value>` commands. The switch uses the LLDP policer for PTP protocol packets. The default value for the LLDP policer is 2500. When you use the ITU 8275.1 profile with higher sync rates, use higher policer values.
{{%/notice%}}

To set a predefined profile:

{{< tabs "TabID276 ">}}
{{< tab "NVUE Commands ">}}

- To set the ITU 8275.1 profile, run the `nv set service ptp <instance-id> current-profile default-itu-8275-1` command.
- To set the ITU 8275.2 profile, run the `nv set service ptp <instance-id> current-profile default-itu-8275-2` command.

The following example sets the profile to ITU 8275.1

```
cumulus@switch:~$ nv set service ptp 1 current-profile default-itu-8275-1
cumulus@switch:~$ nv config apply
```

To set the IEEE 1588 profile:

```
cumulus@switch:~$ nv set service ptp 1 current-profile default-1588
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

- To set the predefined ITU 8275.1 profile, edit the `/etc/ptp4l.conf` file and set the `dataset_comparison` parameter to G.8275.1, then restart the `ptp4l` service.
- To set the predefined ITU 8275.2 profile, edit the `/etc/ptp4l.conf` file and set the `dataset_comparison` parameter to G.8275.2, then restart the `ptp4l` service.

The following example sets the profile to ITU 8275.1

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
[global]
#
# Default Data Set
#
slaveOnly                      0
priority1                      128
priority2                      128
domainNumber                   24

dscp_event                     46
dscp_general                   46
dataset_comparison             G.8275.1
G.8275.defaultDS.localPriority 128
ptp_dst_mac                    01:80:C2:00:00:0E

#
# Port Data Set
#
logAnnounceInterval            -3
logSyncInterval                -4
logMinDelayReqInterval         -4
announceReceiptTimeout         3
delay_mechanism                E2E

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          200
tsmonitor_num_ts                   100
tsmonitor_num_log_sets             3
tsmonitor_num_log_entries          4
tsmonitor_log_wait_seconds         1

#
# Run time options
#
logging_level                  6
path_trace_enabled             0
use_syslog                     1
verbose                        0
summary_interval               0

#
# servo parameters
#
pi_proportional_const          0.000000
pi_integral_const              0.000000
pi_proportional_scale          0.700000
pi_proportional_exponent       -0.300000
pi_proportional_norm_max       0.700000
pi_integral_scale              0.300000
pi_integral_exponent           0.400000
pi_integral_norm_max           0.300000
step_threshold                 0.000002
first_step_threshold           0.000020
max_frequency                  900000000
sanity_freq_limit              0

#
# Default interface options
#
time_stamping                  software


# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E

[swp2]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

To use the predefined IEEE 1588 profile, edit the `/etc/ptp4l.conf` file and set the `dataset_comparison` parameter to ieee1588, then restart the `ptp4l` service. Here is an example:

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly                      0
priority1                      128
priority2                      128
domainNumber                   0

dscp_event                     46
dscp_general                   46
network_transport              UDPv4
dataset_comparison             ieee1588

#
# Port Data Set
#
logAnnounceInterval            1
logSyncInterval                0
logMinDelayReqInterval         0
announceReceiptTimeout         3
delay_mechanism                E2E

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          200
tsmonitor_num_ts                   100
tsmonitor_num_log_sets             3
tsmonitor_num_log_entries          4
tsmonitor_log_wait_seconds         1

#
# Run time options
#
logging_level                  6
path_trace_enabled             0
use_syslog                     1
verbose                        0
summary_interval               0

#
# servo parameters
#
pi_proportional_const          0.000000
pi_integral_const              0.000000
pi_proportional_scale          0.700000
pi_proportional_exponent       -0.300000
pi_proportional_norm_max       0.700000
pi_integral_scale              0.300000
pi_integral_exponent           0.400000
pi_integral_norm_max           0.300000
step_threshold                 0.000002
first_step_threshold           0.000020
max_frequency                  900000000
sanity_freq_limit              0

#
# Default interface options
#
time_stamping                  software


# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E

[swp2]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

To create a custom profile:

{{< tabs "TabID322 ">}}
{{< tab "NVUE Commands ">}}

- Create a profile name.
- Set the profile type on which to base the new profile (`itu-g-8275-1` `itu-g-8275-2`, or `ieee-1588`).
- Update any of the profile settings you want to change (`announce-interval`, `delay-req-interval`, `priority1`, `sync-interval`, `announce-timeout`, `domain`, `priority2`, `transport`, `delay-mechanism`, `local-priority`).
- Set the custom profile to be the current profile.

The following example commands create a custom profile called CUSTOM1 based on the predifined profile ITU 8275-1. The commands set the `domain` to 28 and the `announce-timeout` to 3, then set `CUSTOM1` to be the current profile:

```
cumulus@switch:~$  nv set service ptp 1 profile CUSTOM1 
cumulus@switch:~$  nv set service ptp 1 profile CUSTOM1 profile-type itu-g-8275-1  
cumulus@switch:~$  nv set service ptp 1 profile CUSTOM1 domain 28
cumulus@switch:~$  nv set service ptp 1 profile CUSTOM1 announce-timeout 3
cumulus@switch:~$  nv set service ptp 1 current-profile CUSTOM1
cumulus@switch:~$  nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following example `/etc/ptp4l.conf` file creates a custom profile based on the predifined profile ITU 8275-1 and sets the `domain` to 28 and the `announce-timeout` to 3.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly                      0
priority1                      128
priority2                      128
domainNumber                   28

dscp_event                     46
dscp_general                   46
network_transport              L2
dataset_comparison             G.8275.x
G.8275.defaultDS.localPriority 128
ptp_dst_mac                    01:80:C2:00:00:0E

#
# Port Data Set
#
logAnnounceInterval            5
logSyncInterval                -4
logMinDelayReqInterval         -4
announceReceiptTimeout         3
delay_mechanism                E2E

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          200
tsmonitor_num_ts                   100
tsmonitor_num_log_sets             3
tsmonitor_num_log_entries          4
tsmonitor_log_wait_seconds         1

#
# Run time options
#
logging_level                  6
path_trace_enabled             0
use_syslog                     1
verbose                        0
summary_interval               0

#
# servo parameters
#
pi_proportional_const          0.000000
pi_integral_const              0.000000
pi_proportional_scale          0.700000
pi_proportional_exponent       -0.300000
pi_proportional_norm_max       0.700000
pi_integral_scale              0.300000
pi_integral_exponent           0.400000
pi_integral_norm_max           0.300000
step_threshold                 0.000002
first_step_threshold           0.000020
max_frequency                  900000000
sanity_freq_limit              0

#
# Default interface options
#
time_stamping                  software


# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E

[swp2]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

To show the current PTP profile setting, run the `nv show service ptp <ptp-instance>` command:

```
cumulus@switch:~$ nv show service ptp 1
                             operational  applied             description
---------------------------  -----------  ------------------  --------------------------------------------------------------------
enable                       on           on                  Turn the feature 'on' or 'off'.  The default is 'off'.
current-profile                           default-itu-8275-1  Current PTP profile index
domain                       24           0                   Domain number of the current syntonization
ip-dscp                      46           46                  Sets the Diffserv code point for all PTP packets originated locally.
priority1                    128          128                 Priority1 attribute of the local clock
priority2                    128          128                 Priority2 attribute of the local clock
...
```

To show the settings for a profile, run the `nv show service ptp 1 profile <profile-name>` command:

```
cumulus@switch:~$ nv show service ptp 1 profile CUSTOM1
                             operational  applied           
---------------------------  -----------  ------------------
enable                                    on                
current-profile                           default-itu-8275-1
domain                                    0                 
ip-dscp                                   46                
logging-level                             info              
priority1                                 128               
priority2                                 128               
[acceptable-master]    
monitor                                                     
  max-offset-threshold                    50                
  max-timestamp-entries                   100               
  max-violation-log-entries               4                 
  max-violation-log-sets                  3                 
  min-offset-threshold                    -50               
  path-delay-threshold                    200               
  violation-log-interval                  1                 
```

### Clock Domains

PTP domains allow different independent timing systems to be present in the same network without confusing each other. A PTP domain is a network or a portion of a network within which all the clocks synchronize. Every PTP message contains a domain number. A PTP instance works in only one domain and ignores messages that contain a different domain number.

You can specify multiple PTP clock domains. PTP isolates each domain from other domains so that each domain is a different PTP network. You can specify a number between 0 and 127.

The following example commands configure domain 3:

{{< tabs "TabID173 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 domain 3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default Data Set` section of the `/etc/ptp4l.conf` file to change the `domainNumber` setting, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               128
priority2               128
domainNumber            3
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

### PTP Priority

Use the PTP priority to select the best master clock. You can set priority 1 and 2:
- Priority 1 overrides the clock class and quality selection criteria to select the best master clock.
- Priority 2 identifies primary and backup clocks among identical redundant Grandmasters.

The range for both priority1 and priority2 is between 0 and 255. The default priority is 128. For the boundary clock, use a number above 128. The lower priority applies first.

The following example commands set priority 1 and priority 2 to 200:

{{< tabs "TabID212 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 priority1 200
cumulus@switch:~$ nv set service ptp 1 priority2 200
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default Data Set` section of the `/etc/ptp4l.conf` file to change the `priority1` and, or `priority2` setting, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               200
priority2               200
domainNumber            3
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}
<!--
### One-step and Two-step Clock

The Cumulus Linux switch supports hardware packet time stamping and provides two modes:
- In *one-step* mode, the PTP packet is time stamped as it egresses the port and there is no need for a follow-up packet.
- In *two-step* mode, PTP notes the time when the PTP packet egresses the port and sents it in a separate (follow-up) message.

{{%notice note%}}
One-step mode is available for early access only.
{{%/notice%}}

Two-step mode is the default configuration. To configure the switch to use one-step mode:

{{< tabs "TabID272 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 two-step off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default Data Set` section of the `/etc/ptp4l.conf` file to change the `twoStepFlag` setting to 0, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               254
priority2               254
domainNumber            3

twoStepFlag             0
dscp_event              43
dscp_general            43
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}
 -->
### DSCP

You can configure the DiffServ code point (DSCP) value for all PTP IPv4 packets originated locally. You can set a value between 0 and 63.

{{< tabs "TabID320 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 ip-dscp 22
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default Data Set` section of the `/etc/ptp4l.conf` file to change the `dscp_event` setting for PTP messages that trigger a timestamp read from the clock and the `dscp_general` setting for PTP messages that carry commands, responses, information, or timestamps.

After you save the `/etc/ptp4l.conf` file, restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               200
priority2               200
domainNumber            3

dscp_event              22
dscp_general            22
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional PTP Interface Configuration

### Transport Mode

By default, Cumulus Linux encapsulates PTP messages in UDP/IPV4 frames. To encapsulate PTP messages on an interface in UDP/IPV6 frames:

{{< tabs "TabID274 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp transport ipv6
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the `/etc/ptp4l.conf` file to change the `network_transport` setting for the interface, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
network_transport       UDPv6

[swp2]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
network_transport       UDPv6
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

### Forced Master Mode

By default, PTP ports are in auto mode, where the BMC algorithm determines the state of the port.

You can configure *Forced Master* mode on a PTP port so that it is always in a master state and the BMC algorithm does not run for this port. This port ignores any Announce messages it receives.

{{< tabs "TabID384 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp forced-master on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the `/etc/ptp4l.conf` file to change the `masterOnly` setting for the interface, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 1
masterOnly              1
delay_mechanism         E2E
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

### Message Mode

Cumulus Linux supports the following PTP message modes:
- *Multicast*, where the ports subscribe to two multicast addresses, one for event messages with timestamps and the other for general messages without timestamps. The Sync message that the master sends is a multicast message; all slave ports receive this message because the slaves need the time from the master. The slave ports in turn generate a Delay Request to the master. This is a multicast message that the intended master for the message and other slave ports receive. Similarly, all slave ports in addition to the intended slave port receive the master's Delay Response. The slave ports receiving the unintended Delay Requests and Responses need to drop the packets. This can affect network bandwidth if there are hundreds of slave ports.
- *Unicast*, where you configure the port as a unicast client or server. The client sends out requests for Announce, Sync and Delay Response from its list of servers (masters) from the Unicast Master Table. The servers respond, then start sending Announce Messages. The client uses the Announce Messages to run the BMCA and to choose the best master. You typically use PTP unicast when multicast is not an option in the network or when sending multicast traffic to unintended devices is not desirable.
- *Mixed*, where Sync and Announce messages are multicast messages but Delay Request and Response messages are unicast. This avoids the issue seen in multicast message mode where every slave port sees Delay Requests and Responses from every other slave port.

#### Multicast and Mixed Mode

Multicast mode is the default setting; when you enable PTP on an interface, the message mode is multicast. 

To change the message mode to mixed on swp1:

{{< tabs "TabID494 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp mixed-multicast-unicast on
cumulus@switch:~$ nv config apply
```

To change the message mode back to the default setting of multicast on swp1:

```
cumulus@switch:~$ nv set interface swp1 ptp mixed-multicast-unicast off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the  `/etc/ptp4l.conf` file to add the `hybrid_e2e  1` line under the interface, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
Hybrid_e2e              1
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

To change the message mode back to the default setting of multicast, remove the `hybrid_e2e` line under the interface, then restart the `ptp4l` service.

{{< /tab >}}
{{< /tabs >}}

#### Unicast Mode

You can configure a PTP interface on the switch to be a unicast client or a unicast server. Unicast mode reduces the amount of bandwidth consumed.

{{%notice note%}}
PTP unicast mode does not support bond or VLAN interfaces.
{{%/notice%}}

To configure a PTP interface to be the unicast *client*:
- Configure the unicast master table. You must configure at least one unicast master table on the switch. If you configure more than one unicast master table, each table must have a unique ID.
  - Set the unicast table ID; a unique ID that identifies the unicast master table.
  - Set the unicast master address. You can set more than one unicast master address, which can be an IPv4, IPv6, or MAC address.
  - Optional: Set the unicast master query interval, which is the mean interval between requests for announce messages. Specify this value as a power of two in seconds. You can specify a value between `-3` and `4`. The default value is `-0` (2 power).
- On the PTP interface:
  - Set the table ID of the unicast master table you want to use.
  - Set the unicast service mode to `client`.
  - Optional: Set the unicast request duration; the service time in seconds requested during discovery. The default value is 300 seconds.

{{%notice note%}}
A PTP interface as a unicast client or server only supports a single communictation mode and does not work with multicast servers or clients. Make sure that both sides of a PTP link are in unicast mode.
{{%/notice%}}

The following example commands configure a unicast master table with ID 1. The commands set the unicast master address to 10.10.10.1, the query interval to 4, the unicast service mode to `client`, and the unicast request duration to 20 in the unicast master table.

{{< tabs "TabID668 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 address 10.10.10.1
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 query-interval 4
cumulus@switch:~$ nv set interface swp1 ptp unicast-master-table-id 1
cumulus@switch:~$ nv set interface swp1 ptp unicast-service-mode client
cumulus@switch:~$ nv set interface swp1 ptp unicast-request-duration 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Add the following lines at the end of the `# Default interface options` section of the  `/etc/ptp4l.conf` file:

   ```
   cumulus@switch:~$ sudo nano /etc/ptp4l.conf
   ...
   # Default interface options
   ...
   [unicast_master_table]
   table_id               1
   logQueryInterval       4
   UDPv4                  10.10.10.1
   ...
   ```

2. Add the following lines at the end of the interface section (`[swp1]` in the example) of the  `/etc/ptp4l.conf` file:

   ```
   [swp1]
   ...
   table_id                 1
   unicast_request_duration 20
   ...
   ```

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

To configure a PTP interface to be the unicast *server*, set PTP unicast-service-mode to `server`.

{{< tabs "TabID706 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-service-mode server
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Add the following lines at the end of the interface section of the  `/etc/ptp4l.conf` file:

   ```
   [swp1]
   ...
   unicast_listen            1
   inhibit_multicast_service 1

   ...
   ```

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
When you configure a unicast client or server on a PTP interface, make sure to set the global parameter `Priority1` or `Priority2` so that BMCA can choose that end to be the slave or master. See {{<link url="#ptp-priority" text="PTP Priority">}}.
{{%/notice%}}

#### Show Unicast Master Information

To show the unicast master table configuration on the switch, run the `nv show service ptp <instance-id> unicast-master <table-id>` command:

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1
                operational  applied     
--------------  -----------  ----------
Query-interval  0             0  
[address]       10.10.10.1   10.10.10.1
```

### TTL for a PTP Message

To restrict the number of hops a PTP message can travel, set the TTL on the PTP interface. You can set a value between 1 and 255.

{{< tabs "TabID462 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp ttl 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the  `/etc/ptp4l.conf` file to change the `udp_ttl` setting for the interface, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 20
masterOnly              1
delay_mechanism         E2E
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

### PTP Interface Timers

You can set the following timers for PTP messages.

| Timer | Description |
| ----- | ----------- |
| `announce-interval` | The average interval between successive Announce messages. Specify the value as a power of two in seconds. |
| `announce-timeout` | The number of announce intervals that have to occur without receiving an Announce message before a timeout occurs. <br>Make sure that this value is longer than the announce-interval in your network.|
| `delay-req-interval` | The minimum average time interval allowed between successive Delay Required messages. |
| `sync-interval` | The interval between PTP synchronization messages on an interface. Specify the value as a power of two in seconds. |

- To set the timers with NVUE, run the `nv set interface <interface> ptp timers <timer> <value>` command.
- To set the timers with Linux commands, edit the `/etc/ptp4l.conf` file and set the timers in the `Default interface options` section.

{{< tabs "TabID542 ">}}
{{< tab "NVUE Commands ">}}

The following example sets the announce interval between successive Announce messages on swp1 to -1.

```
cumulus@switch:~$ nv set interface swp1 ptp timers announce-interval -1
cumulus@switch:~$ nv config apply
```

The following example sets the mean sync-interval for multicast messages on swp1 to -5.

```
cumulus@switch:~$ nv set interface swp1 ptp timers sync-interval -5
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the `/etc/ptp4l.conf` file:

- To set the announce interval between successive Announce messages on swp1 to -1, change the `logAnnounceInterval` setting for the interface to -1.
- To set the mean sync-interval for multicast messages on swp1 to -5, change the `logSyncInterval` setting for the interface to -5.

After you edit the `/etc/ptp4l.conf` file, restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
logAnnounceInterval     -1
logSyncInterval         -5
udp_ttl                 20
masterOnly              1
delay_mechanism         E2E
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

<!--### Delay Mechanism

For PTP nodes to synchronize the time of day, each slave has to learn the delay between iteself and the master. There are two delay mehanism modes:
- Peer-to-peer, where each network device measures the delay between its input port and the device attached to the other end of the input port. This is the default mode. 
- End-to-end, where the slave measures the delay between itself and the master. The master and slave send delay request and delay response messages between each other to measure the delay.

To set the delay mechanism to end-to-end:

{{< tabs "TabID753 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp delay-mechanism end-to-end
cumulus@switch:~$ nv config apply
```

To reset the delay mechanism to peer-to-peer, run the `unset interface <interface> ptp delay-mechanism end-to-end` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the `/etc/ptp4l.conf` file and set the `end-to-end` option to 1 for the interface, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 20
masterOnly              1
delay_mechanism         E2E
network_transport       UDPv4
end-to-end              1
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}
-->
### Acceptable Master Table

The acceptable master table option is a security feature that prevents a rogue player from pretending to be the Grandmaster to take over the PTP network. To use this feature, you configure the clock IDs of known Grandmasters in the acceptable master table and set the acceptable master table option on a PTP port. The BMC algorithm checks if the Grandmaster received on the Announce message is in this table before proceeding with the master selection. Cumulus Linux disables this option by default on PTP ports.
<!-- vale off -->
The following example command adds the Grandmaster clock ID 24:8a:07:ff:fe:f4:16:06 to the acceptable master table and enable the PTP acceptable master table option for swp1:
<!-- vale on -->
{{< tabs "TabID614 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
cumulus@switch:~$ nv config apply
```

You can also configure an alternate priority 1 value for the Grandmaster:

```
cumulus@switch:~$ nv set service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06 alt-priority 2
```

To enable the PTP acceptable master table option for swp1:

```
cumulus@switch:~$ nv set interface swp1 ptp acceptable-master on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Default interface options` section of the `/etc/ptp4l.conf` file to add `acceptable_master_clockIdentity 248a07.fffe.f41606`.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
#
# Default interface options
#
time_stamping           hardware


[acceptable_master_table]
maxTableSize 16
acceptable_master_clockIdentity 248a07.fffe.f41606
...
```

You can also configure an alternate priority 1 value for the Grandmaster.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
#
# Default interface options
#
time_stamping           hardware


[acceptable_master_table]
maxTableSize 16
acceptable_master_clockIdentity 248a07.fffe.f41606 2
```

To enable the PTP acceptable master table option for swp1, add `acceptable_master on` under `[swp1]`.

```
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 20
masterOnly              1
delay_mechanism         E2E
acceptable_master       on
...
```

Restart the `ptp4l` service:

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional Monitor Configuration

### Configure Clock Correction and Path Delay Thresholds

Cumulus Linux monitors clock correction and path delay against thresholds, and generates counters that show in NVUE show command output and log messages when PTP reaches the thresholds. You can configure the following monitor settings:

{{< tabs "TabID851 ">}}
{{< tab "NVUE Commands ">}}

| Command | Description |
| ----- | ----------- |
| `nv set service ptp <instance> monitor min-offset-threshold` | Sets the minimum difference allowed between the master and slave time. You can set a value between -1000000000 and 0 nanoseconds. The default value is -50 nanoseconds.|
| `nv set service ptp <instance> monitor max-offset-threshold` | Sets the maximum difference allowed between the master and slave time. You can set a value between 0 and 1000000000 nanoseconds. The default value is 50 nanoseconds.|
| `nv set service ptp <instance> monitor path-delay-threshold` | Sets the mean time that PTP packets take to travel between the master and slave. You can set a value between 0 and 1000000000 nanoseconds . The default value is 200 nanoseconds. |
| `nv set service ptp <instance> monitor max-timestamp-entries` | Sets the maximum number of timestamp entries allowed. Cumulus Linux updates the timestamps continuously. You can specify a value between 100 and 200. The default value is 100 entries.|
| `nv set service ptp <instance> monitor max-violation-log-sets` | Sets the maximum number of violation log sets allowed. You can specify a value between 2 and 4. The default value is 2 sets.|
| `nv set service ptp <instance> monitor max-violation-log-entries` | Sets the maximum number of violation log entries allowed for each set. You can specify a value between 4 and 8. The default value is 8 entries.|
| `nv set service ptp <instance> monitor violation-log-interval` | Sets the violation log interval. You can specify a value between 0 and 60 seconds. The default value is 0 seconds.|

The following example sets the path delay threshold to 300:

```
cumulus@switch:~$ nv set service ptp 1 monitor path-delay-threshold 300
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can configure the following monitor settings manually in the `/etc/ptp4l.conf` file. Be sure to run the `sudo systemctl restart ptp4l.service` to apply the settings.

| Parameter | Description |
| ----- | ----------- |
| `offset_from_master_min_threshold` | Sets the minimum difference allowed between the master and slave time. You can set a value between -1000000000 and 0 nanoseconds. The default value is -50 nanoseconds. |
| `offset_from_master_max_threshold` | Sets the maximum difference allowed between the master and slave time. You can set a value between 0 and 1000000000 nanoseconds. The default value is 50 nanoseconds. |
| `mean_path_delay_threshold` | Sets the mean time that PTP packets take to travel between the master and slave. You can set a value between 0 and 1000000000 nanoseconds. The default value is 200 nanoseconds. |

The following example sets the path delay threshold to 300 nanoseconds:

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               128
priority2               128
domainNumber            0

twoStepFlag             1
dscp_event              46
dscp_general            46

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          300
...
```

{{< /tab >}}
{{< /tabs >}}

### Configure PTP Logging

A log set contains the log entries for clock correction and path delay violations at different times. You can set the number of entries to log and the interval between successive violation logs.

{{< tabs "TabID1450 ">}}
{{< tab "NVUE Commands ">}}

| Command  | Description |
| -------- | ----------- |
| `nv set service ptp 1 monitor max-violation-log-sets` | Sets the maximum number of log sets allowed. You can specify a value between 2 and 4. The default value is 3. |
| `nv set service ptp 1 monitor max-violation-log-entries` | Sets the maximum number of log entries allowed in a log set. You can specify a value between 4 and 8. The default value is 4. |
| `nv set service ptp 1 monitor violation-log-interval` |  Sets the number of seconds to wait before logging back-to-back violations. You can specify a value between 0 and 60. The default value is 1.|

The following example sets the maximum number of log sets allowed to 4, the maximum number of log entries allowed to 6, and the violation log interval to 10:

```
cumulus@switch:~$ nv set service ptp 1 monitor max-violation-log-sets 4
cumulus@switch:~$ nv set service ptp 1 monitor max-violation-log-entries 6
cumulus@switch:~$ nv set service ptp 1 monitor violation-log-interval 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can configure the following monitor settings manually in the `/etc/ptp4l.conf` file. Be sure to run the `sudo systemctl restart ptp4l.service` to apply the settings.

| Parameter | Description |
| ----- | ----------- |
| `tsmonitor_num_log_sets` | Sets the maxumum number of log sets allowed. You can specify a value between 2 and 4. The default value is 3.|
| `tsmonitor_num_log_entries`  |  Sets the maximum number of log entries allowed in a log set. You can specify a value between 4 and 8. The default value is 4.|
| `tsmonitor_log_wait_seconds` |  Sets the number of seconds to wait before logging back-to-back violations. You can specify a value between 0 and 60. The default value is 1.|

The following example sets the maxumum number of log sets allowed to 4, the maximum number of log entries allowed to 6, and the violation log interval to 10:

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               128
priority2               128
domainNumber            0

twoStepFlag             1
dscp_event              46
dscp_general            46

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          300
tsmonitor_num_ts                   100
tsmonitor_num_log_sets             4
tsmonitor_num_log_entries          6
tsmonitor_log_wait_seconds         10
...
```

{{< /tab >}}
{{< /tabs >}}

### Show PTP Logs

PTP monitoring provides commands to show counters for violations as well as the timestamp log entries for a violation.

| Command  | Description |
| -------- | ----------- |
| `nv show service ptp <instance> monitor timestamp-log` | Shows the last 25 PTP timestamps.  |
| `nv show service ptp <instance> monitor violations` |  Shows the threshold violation count and the last time a violation of a specific type occured. |
| `nv show service ptp 1 monitor violations log acceptable-master` | Shows logs with violations that occur when a PTP server not in the Acceptable Master table sends an Announce request. |
| `nv show service ptp 1 monitor violations log forced-master`  | Shows logs with violations that occur when a forced master port gets a higher clock. |
| `nv show service ptp 1 monitor violations log max-offset` | Shows logs with violations that occur when the timestamp offset is higher than the max offset threshold. |
| `nv show service ptp 1 monitor violations log min-Offset`  | Shows logs with violations that occur when the timestamp offset is lower than the minimum offset threshold. |
| `nv show service ptp 1 monitor violations log path-delay`  | Shows logs with violations that occur when the mean path delay is higher than the path delay threshold. |

The following example shows the threshold violation count and the last time a minimum offset threshold violation occurred:

```
cumulus@switch:~$ nv show service ptp 1 monitor violations
                  operational                  applied
----------------  ---------------------------  -------
last-max-offset
last-min-offset   2023-04-24T15:22:01.312295Z
last-path-delay
max-offset-count  0
min-offset-count  2
path-delay-count  0
```

### Clear PTP Violation Logs

- To clear the maximum offset violation logs, run the `nv action clear service ptp <instance> monitor violations log max-offset` command 
- To clear the minimum offset violation logs, run the `nv action clear service ptp <instance> monitor violations log min-offset` command.
- To clear the path delay violation logs, run the `nv action clear service ptp <instance> monitor violations log path-delay` command.

```
cumulus@leaf01:mgmt:~$ nv action clear service ptp 1 monitor violations log path-delay
Action succeeded
```

## Delete PTP Configuration

To delete PTP configuration, delete the PTP master and slave interfaces. The following example commands delete the PTP interfaces `swp1`, `swp2`, and `swp3`.

{{< tabs "TabID602 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv unset interface swp1 ptp
cumulus@switch:~$ nv unset interface swp2 ptp
cumulus@switch:~$ nv unset interface swp3 ptp
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ptp4l.conf` file to remove the interfaces from the `Default interface options` section, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

To disable PTP on the switch and stop the `ptp4l` and `phc2sys` processes:

{{< tabs "TabID627 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 enable off
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo systemctl stop ptp4l.service phc2sys.service
cumulus@switch:~$ sudo systemctl disable ptp4l.service phc2sys.service
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

### PTP Configuration and Status

To show a summary of the PTP configuration on the switch, run the `nv show service ptp <instance>` command:

```
cumulus@switch:~$ nv show service ptp 1

---------------------------  -----------  -------  --------------------------------------------------------------------
enable                       on           on       Turn the feature 'on' or 'off'.  The default is 'off'.
domain                       0            0        Domain number of the current syntonization
ip-dscp                      46           46       Sets the Diffserv code point for all PTP packets originated locally.
priority1                    128          128      Priority1 attribute of the local clock
priority2                    128          128      Priority2 attribute of the local clock
two-step                     on           on       Determines if the Clock is a 2 step clock
monitor
  max-offset-threshold       50           50       Maximum offset threshold in nano seconds
  max-timestamp-entries                   400      Maximum timestamp entries allowed
  max-violation-log-entries               8        Maximum violation log entries per set
  max-violation-log-sets                  8        Maximum violation logs sets allowed
  min-offset-threshold       -50          -50      Minimum offset threshold in nano seconds
  path-delay-threshold       200          200      Path delay threshold in nano seconds
  violation-log-interval                  0        violation log intervals in seconds
...
```

You can drill down with the following `nv show service ptp <instance>` commands:
- `nv show service ptp <instance> acceptable-master` shows a collection of acceptable masters.
- `nv show service ptp <instance> monitor` shows PTP monitor configuration.
- `nv show service ptp <instance> current` shows the local states learned during PTP message exchange.
- `nv show service ptp <instance> clock-quality` shows the clock quality status.
- `nv show service ptp <instance> parent` shows the local states learned during PTP message exchange.
- `nv show service ptp <instance> time-properties` shows the clock time attributes.

To check configuration for a PTP interface, run the `nv show interface <interface> ptp` command. This command also shows PTP counters (statistics, such as the number of announce messages received, the number of Sync messages received, and so on).

```
cumulus@leaf03:mgmt:~$ nv show interface swp1 ptp
                           operational  applied     description
-------------------------  -----------  ----------  ----------------------------------------------------------------------
enable                                  on          Turn the feature 'on' or 'off'.  The default is 'off'.
acceptable-master                       off         Determines if acceptable master check is enabled for this interface.
delay-mechanism            end-to-end   end-to-end  Mode in which PTP message is transmitted.
forced-master              off          off         Configures PTP interfaces to forced master state.
instance                                1           PTP instance number.
mixed-multicast-unicast                 off         Enables Multicast for Announce, Sync and Followup and Unicast for D...
transport                  ipv4         ipv4        Transport method for the PTP messages.
ttl                        1            1           Maximum number of hops the PTP messages can make before it gets dro...
unicast-request-duration                300         The service time in seconds to be requested during discovery.
timers
  announce-interval        0            0           Mean time interval between successive Announce messages.  It's spec...
  announce-timeout         3            3           The number of announceIntervals that have to pass without receipt o...
  delay-req-interval       -3           -3          The minimum permitted mean time interval between successive Delay R...
  sync-interval            -3           -3          The mean SyncInterval for multicast messages.  It's specified as a...
peer-mean-path-delay       0                        An estimate of the current one-way propagation delay on the link wh...
port-state                 master                   State of the port
protocol-version           2                        The PTP version in use on the port
counters
  rx-announce              0                        Number of Announce messages received
  rx-delay-req             0                        Number of Delay Request messages received
  rx-delay-resp            0                        Number of Delay response messages received
  rx-delay-resp-follow-up  0                        Number of Delay response follow upmessages received
  rx-follow-up             0                        Number of Follow up messages received
  rx-management            0                        Number of Management messages received
  rx-peer-delay-req        0                        Number of Peer Delay Request messages received
  rx-peer-delay-resp       0                        Number of Peer Delay Response messages received
  rx-signaling             0                        Number of singnaling messages received
  rx-sync                  0                        Number of Sync messages received
  tx-announce              2639                     Number of Announce messages transmitted
  tx-delay-req             0                        Number of Delay Request messages transmitted
  tx-delay-resp            0                        Number of Delay response messages transmitted
  tx-delay-resp-follow-up  0                        Number of Delay response follow upmessages transmitted
  tx-follow-up             21099                    Number of Follow up messages transmitted
  tx-management            0                        Number of Management messages transmitted
  tx-peer-delay-req        0                        Number of Peer Delay Request messages transmitted
  tx-peer-delay-resp       0                        Number of Peer Delay Response messages transmitted
  tx-signaling             0                        Number of singnaling messages transmitted
  tx-sync                  21099                    Number of Sync messages transmitted
```

To show PTP counters only for an interface, run the `nv show interface <interface> counters ptp` command.

To show PTP status information, including the delta in nanoseconds from the master clock:

```
cumulus@switch:~$ sudo pmc -u -b 0 'GET TIME_STATUS_NP'
sending: GET TIME_STATUS_NP
    7cfe90.fffe.f56dfc-0 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
        master_offset              12610
        ingress_time               1525717806521177336
        cumulativeScaledRateOffset +0.000000000
        scaledLastGmPhaseChange    0
        gmTimeBaseIndicator        0
        lastGmPhaseChange          0x0000'0000000000000000.0000
        gmPresent                  true
        gmIdentity                 000200.fffe.000005
    000200.fffe.000005-1 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
        master_offset              0
        ingress_time               0
        cumulativeScaledRateOffset +0.000000000
        scaledLastGmPhaseChange    0
        gmTimeBaseIndicator        0
        lastGmPhaseChange          0x0000'0000000000000000.0000
        gmPresent                  false
        gmIdentity                 000200.fffe.000005
    000200.fffe.000006-1 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
        master_offset              5544033534
        ingress_time               1525717812106811842
        cumulativeScaledRateOffset +0.000000000
        scaledLastGmPhaseChange    0
        gmTimeBaseIndicator        0
        lastGmPhaseChange          0x0000'0000000000000000.0000
        gmPresent                  true
        gmIdentity                 000200.fffe.000005
```

- To see a full list of NVUE show commands for PTP, run the `nv list-commands service ptp` command.
- To show a full list of show commands for a PTP interface, run the `nv list-commands interface` command, then scroll to see PTP.

```
cumulus@switch:~$ nv list-commands service ptp
nv show service ptp
nv show service ptp <instance-id>
nv show service ptp <instance-id> acceptable-master
nv show service ptp <instance-id> acceptable-master <clock-id>
nv show service ptp <instance-id> unicast-master
nv show service ptp <instance-id> unicast-master <table-id>
nv show service ptp <instance-id> unicast-master <table-id> address
nv show service ptp <instance-id> unicast-master <table-id> address <ip-mac-address-id>
...
```

```
cumulus@switch:~$ nv list-commands interface
...
nv show interface <interface-id> ptp
nv show interface <interface-id> ptp timers
nv show interface <interface-id> ptp counters
...
```

## Example Configuration

In the following example, the boundary clock on the switch receives time from Master 1 (the grandmaster) on PTP slave port swp1, sets its clock and passes the time down through PTP master ports swp2, swp3, and swp4 to the hosts that receive the time.

{{< img src = "/images/cumulus-linux/date-time-ptp-config.png" >}}

The following example configuration assumes that you have already configured the layer 3 routed interfaces (`swp1`, `swp2`, `swp3`, and `swp4`) you want to use for PTP.

{{< tabs "518 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 enable on
cumulus@switch:~$ nv set service ptp 1 priority2 254
cumulus@switch:~$ nv set service ptp 1 priority1 254
cumulus@switch:~$ nv set service ptp 1 domain 3
cumulus@switch:~$ nv set interface swp1 ptp enable on
cumulus@switch:~$ nv set interface swp2 ptp enable on
cumulus@switch:~$ nv set interface swp3 ptp enable on
cumulus@switch:~$ nv set interface swp4 ptp enable on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml file ">}}

```
cumulus@switch:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      swp1:
        ptp:
          enable: on
        type: swp
      swp2:
        ptp:
          enable: on
        type: swp
      swp3:
        ptp:
          enable: on
        type: swp
      swp4:
        ptp:
          enable: on
        type: swp
    service:
      ptp:
        '1':
          domain: 3
          enable: on
          priority1: 254
          priority2: 254
```

{{< /tab >}}
{{< tab "/etc/ptp4l.conf file ">}}

```
cumulus@switch:~$ sudo cat /etc/ptp4l.conf
...
[global]
#
# Default Data Set
#
slaveOnly               0
priority1               254
priority2               254
domainNumber            3

twoStepFlag             1
dscp_event              46
dscp_general            46

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          200

#
# Run time options
#
logging_level           6
path_trace_enabled      0
use_syslog              1
verbose                 0
summary_interval        0

#
# Default interface options
#
time_stamping           hardware

# Interfaces in which ptp should be enabled
# these interfaces should be routed ports
# if an interface does not have an ip address
# the ptp4l will not work as expected.

[swp1]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
network_transport       UDPv4

[swp2]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
network_transport       UDPv4

[swp3]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
network_transport       UDPv4

[swp4]
udp_ttl                 1
masterOnly              0
delay_mechanism         E2E
network_transport       UDPv4
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

### PTP Traffic Shaping

To improve performance on the NVIDA Spectrum 1 switch for PTP-enabled ports with speeds lower than 100G, you can configure traffic shaping.
For example, if you see that the PTP timing offset varies widely and is does not stabilize, enable PTP shaping on all PTP enabled ports to reduce the bandwidth on the ports slightly and improve timing stabilization.

{{%notice note%}}
- Switches with Spectrum-2 and later do not support PTP shaping.
- Bonds do not support PTP shaping.
- Do not configure QoS, such as egress queue or port based scheduling, on the same ports with PTP traffic shaping.
{{%/notice%}}

{{< tabs "TabID1387 ">}}
{{< tab "NVUE Commands ">}}

For each PTP-enabled port where you want to set traffic shaping, run the `nv set interface <interface> ptp shaper enable on` command.

```
cumulus@switch:~$ nv set interface swp1 ptp shaper enable on
cumulus@switch:~$ nv set interface swp2 ptp shaper enable on
cumulus@switch:~$ nv config apply
```

To see the PTP shaping setting for a switch port, run the `nv show interface <interface> ptp shaper` command:

```
cumulus@switch:~$ nv show interface swp1 ptp shaper
        operational  applied  
------  -----------  -------  
enable               on   
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/cumulus/switchd.d/ptp_shaper.conf` file, set the `interface.<interface>.ptp.shaper` parameter to TRUE for the interfaces to which you want to apply traffic shaping, then reload `switchd`.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/ptp_shaper.conf
## Per-port configuration for PTP shaper
interface.swp1.ptp.shaper = TRUE
#interface.swp2.ptp.shaper = FALSE
#interface.swp9.ptp.shaper = TRUE
#interface.swp12.ptp.shaper = TRUE
```

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

{{< /tab >}}
{{< /tabs >}}

### Spanning Tree and PTP
<!-- vale off -->
PTP frames are affected by <span style="background-color:#F5F5DC">[STP](## "Spanning Tree Protocol")</span> filtering; events, such as an STP topology change (where ports temporarily go into the blocking state), can cause interruptions to PTP communications.

If you configure PTP on bridge ports, NVIDIA recommends that the bridge ports are spanning tree edge ports or in a bridge domain where spanning tree is disabled.
<!-- vale on -->