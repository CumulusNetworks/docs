---
title: Precision Time Protocol - PTP
author: NVIDIA
weight: 126
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
- UDPv4, UDPv6, and 802.3 encapsulation.
- Only a single PTP domain per network.
- PTP on layer 3 interfaces, trunk ports, bonds, and switch ports belonging to a VLAN.
- Multicast, unicast, and mixed message mode.
- End-to-End delay mechanism only. Cumulus Linux does not support Peer-to-Peer.
- One-step and two-step clock timestamp mode.
- Hardware timestamping for PTP packets. This allows PTP to avoid inaccuracies caused by message transfer delays and improves the accuracy of time synchronization.

{{%notice note%}}
- On NVIDIA switches with Spectrum-2 and later, PTP is not supported on 1G interfaces.
- On Spectrum-4 switches, PTP is Beta.
- You cannot run *both* PTP and NTP on the switch.
- PTP supports the default VRF only.
{{%/notice%}}

## Basic Configuration

Basic PTP configuration requires you:

- Enable PTP on the switch.
- Configure PTP on at least one interface; this can be a layer 3 routed port, switch port, or trunk port. You do not need to specify which is a master interface and which is a slave interface; the PTP Best Master Clock Algorithm (BMCA) determines the master and slave.

{{%notice note%}}
If you configure PTP with Linux commands, you must also enable PTP timestamping; see step 1 of the Linux procedure below. NVUE enables timestamping when you enable PTP on the switch.
{{%/notice%}}

The basic configuration shown below uses the *default* PTP settings:
- The clock mode is Boundary. This is the only clock mode that Cumulus Linux supports.
- {{<link url="#clock-domains" text="The PTP clock domain">}} is 0.
- {{<link url="#ptp-priority" text="PTP Priority1 and Priority2">}} are both 128.
- {{<link url="#dscp" text="The DSCP" >}} is 46 for both general and event messages.
- {{<link url="#Transport-mode" text="The PTP interface transport mode">}} is IPv4.
- {{<link url="#Forced-master-mode" text="Announce messages from any master are accepted">}}.
- {{<link url="#Message-mode" text="The PTP Interface Message Mode">}} is multicast.
- The delay mechanism is End-to-End (E2E), where the slave measures the delay between itself and the master. The master and slave send delay request and delay response messages between each other to measure the delay.
- The clock timestamp mode is two-step.

To configure other settings, such as the PTP profile, domain, priority, and DSCP, the PTP interface transport mode and timers, and PTP monitoring, see the Optional Configuration sections below.

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
cumulus@switch:~$ nv set interface vlan10 ptp enable on
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
   
   twoStepFlag             1
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

   For a trunk VLAN, add the VLAN configuration to the switch port stanza: set `l2_mode` to `trunk`, `vlan_intf` to the VLAN interface, and `src_ip` to the IP address of the VLAN interface:

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

   For a switch port VLAN, add the VLAN configuration to the switch port stanza: set `l2_mode` to `access`, `vlan_intf` to the VLAN interface, and  `src_ip` to the IP address of the VLAN interface:
   
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

## Global Configuration

Cumulus Linux provides several ways to modify the default basic global configuration. You can:
- Use profiles.
- Modify the parameters directly with NVUE commands.
- Modify the Linux `/etc/ptp4l.conf` file.

When a predefined profile is set, NVUE does not allow you to configure global parameters. Do not edit the Linux `/etc/ptp4l.conf` file to modify the global parameters when a predefined profile is in use. For information about profiles, see {{<link url="#ptp-profiles" text="PTP Profiles">}}.

### Clock Domains

PTP domains allow different independent timing systems to be present in the same network without confusing each other. A PTP domain is a network or a portion of a network within which all the clocks synchronize. Every PTP message contains a domain number. A PTP instance works in only one domain and ignores messages that contain a different domain number. Cumulus Linux supports only one domain in the system.

You can specify multiple PTP clock domains. PTP isolates each domain from other domains so that each domain is a different PTP network. You can specify a number between 0 and 127.

The following example commands configure domain 3 when a profile is not set:

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

### Clock Timestamp Mode

The Cumulus Linux switch provides the following clock timestamp modes:
- *One-step*, where PTP adds the precise time that the Sync packet egresses the port to the packet. There is no need for a follow up packet.
- *Two-step*, where PTP notes the precise time when the Sync packet egresses the port and sends it in a separate follow up message.

One-step mode significantly reduces the number of PTP messages. Two-step mode is the default configuration.

{{%notice note%}}
Cumulus Linux supports one-step mode on switches with Spectrum-2 and later.
{{%/notice%}}

{{< tabs "TabID345 ">}}
{{< tab "NVUE Commands ">}}

The following example commands configure one-step mode when a profile is not set:

```
cumulus@switch:~$ nv set service ptp 1 two-step off
cumulus@switch:~$ nv config apply
```

To revert the clock timestamp mode to the default setting (two-step mode), run the `nv set service ptp 1 two-step on` command.  

To set the clock timestamp mode for a custom profile based on IEEE1588, ITU 8275-1 or ITU 8275-2, run the `nv set service ptp <instance-id> profile <profile-id> two-step` command. For example, to set one-step mode for the custom profile called CUSTOM1, run the `nv set service ptp 1 profile CUSTOM1 two-step off` command.

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

To revert the clock timestamp mode to the default setting (two-step mode), change the `twoStepFlag` setting to 1.

{{< /tab >}}
{{< /tabs >}}

### PTP Priority

Use the PTP priority to select the best master clock. You can set priority 1 and 2:
- Priority 1 overrides the clock class and quality selection criteria to select the best master clock.
- Priority 2 identifies primary and backup clocks among identical redundant Grandmasters.

The range for both priority1 and priority2 is between 0 and 255. The default priority is 128. For the boundary clock, use a number above 128. The lower priority applies first.

The following example commands set priority 1 and priority 2 to 200 when a profile is not set:

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

### Local Priority

Use the local priority when you create a custom profile based on a Telecom profile (ITU 8275-1 or ITU 8275-2). Modify the local priority in a custom profile to set the local priority of the local clock. You can set a value between 0 and 255. The default priority is 128.

The following example command configures the local priority to 10 for the custom profile called CUSTOM1, based on ITU 8275-2:

{{< tabs "TabID387 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 profile CUSTOM1 local-priority 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `G.8275.defaultDS.localPriority` option in the `/etc/ptp4l.conf` file. After you save the `/etc/ptp4l.conf` file, restart the `ptp4l` service.

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

twoStepFlag                    1
dscp_event                     46
dscp_general                   46
network_transport              L2
dataset_comparison             G.8275.x
G.8275.defaultDS.localPriority 10
ptp_dst_mac                    01:80:C2:00:00:0E
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}
<!--
### Noise Transfer Servo

ITU-T specifies the following key elements to measure, test, and classify the accuracy of a clock:
- Noise generation&mdash;jitter and wander noise in the output of a clock in reference to a <span class="a-tooltip">[PRTC](## "Primary Reference Time Clock")</span>.
- Noise tolerance&mdash;how much noise the clock can tolerate before it switches to another stable source.
- Noise transfer&mdash;smoothe out the input noise so that noise does not accumulate and increase over a network of clocks.
- Transient response&mdash;the response from the clock to a transient.
- Hold over&mdash;the time interval during which the clock maintains its output after losing the input reference signal.

Cumulus Linux PTP has an option to use a servo specifically designed to handle ITU-T’s Noise Transfer specification. When you use this option, the <span class="a-tooltip">[PHC](## "Physical Hardware Clock")</span> is disciplined by Noise Transfer Servo, which smoothes the jitter and wander noise from the Master clock.

{{%notice note%}}
- To use Noise Transfer Servo, you need to enable SyncE on the switch and on PTP interfaces. 
- Cumulus Linux supports Noise Transfer Servo on Spectrum ASICs that support SyncE.
- NVIDIA recommends you do not change the default Noise Transfer Servo configuration parameters.
- NVIDIA recommends you use Noise Transfer Servo with PTP Telecom profiles. If you use other profiles or choose not to use a profile, make sure to set the sync interval to -3 or better.
{{%/notice%}}

To enable Noise Transfer Servo:

{{< tabs "TabID500 ">}}
{{< tab "NVUE Commands ">}}

The following example enables PTP, sets the profile to `default-itu-8275-1`, enables SyncE, enables PTP on swp3, and enables Noise Transfer Servo.

```
cumulus@switch:~$ nv set service ptp 1 enable on
cumulus@switch:~$ nv set service ptp 1 current-profile default-itu-8275-1
cumulus@switch:~$ nv set system synce enable on
cumulus@switch:~$ nv set interface swp3 ptp enable on
cumulus@switch:~$ nv set service ptp 1 servo noise-transfer
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ptp4l.conf` and the `/etc/firefly_servo/servo.conf` files; see examples below.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
[global]
#
# Default Data Set
#
slaveOnly                      0
free_running                   1
slave_event_monitor            /var/run/servo_slave_event_monitor
priority1                      128
priority2                      128
domainNumber                   24

twoStepFlag                    1
dscp_event                     46
dscp_general                   46
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
tsmonitor_num_log_sets             2
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
first_step_threshold           0.000020
step_threshold                 0.000000025
servo_offset_threshold         20
servo_num_offset_values        10
write_phase_mode               1
max_frequency                  50000000
sanity_freq_limit              0
#
# Default interface options
#
time_stamping                  hardware

[swp3]
udp_ttl                      1
masterOnly                   0
delay_mechanism              E2E
```

```
cumulus@switch:~$ sudo nano /etc/firefly_servo/servo.conf
[global]
free_running                        0
domainNumber                        24

offset_from_master_min_threshold    -50
offset_from_master_max_threshold    50

# Debugging & Logging
doca_logging_level                  50

init_max_time_adjustment            0
max_time_adjustment                 1500
hold_over_timer                     0
# Sampling Window & servo logic
servo_window_timer                  3000
servo_window_min_samples            10
servo_num_offset_values             5
```

{{< /tab >}}
{{< /tabs >}}

To show Noise Transfer Servo configuration settings, run the `nv show service ptp <instance-id> servo` command:

```
cumulus@switch:~$ nv show service ptp 1 servo
       operational  applied
-----  -----------  --------------
servo               noise-transfer
```
-->
## Optional Global Configuration

Optional global PTP configuration includes configuring the DiffServ code point (DSCP). You can configure the DSCP value for all PTP IPv4 packets originated locally. You can set a value between 0 and 63.

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

twoStepFlag             1
dscp_event              22
dscp_general            22
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

## PTP Interface Configuration

Cumulus Linux provides several ways to modify the default basic interface configuration. You can:
- Use profiles
- Modify the parameters directly with NVUE commands
- Modify the Linux `/etc/ptp4l.conf` configuration file.

When a profile is in use, avoid configuring the following interface configuration parameters with NVUE or in the Linux configuration file so that the interface retains its profile settings.

### Transport Mode

By default, Cumulus Linux encapsulates PTP messages in UDP IPV4 frames. To encapsulate PTP messages on an interface in UDP IPV6 frames:

{{< tabs "TabID557 ">}}
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

### Message Mode

Cumulus Linux supports the following PTP message modes:
- *Multicast*, where the ports subscribe to two multicast addresses, one for event messages with timestamps and the other for general messages without timestamps. The Sync message that the master sends is a multicast message; all slave ports receive this message because the slaves need the time from the master. The slave ports in turn generate a Delay Request to the master. This is a multicast message that the intended master for the message and other slave ports receive. Similarly, all slave ports in addition to the intended slave port receive the master's Delay Response. The slave ports receiving the unintended Delay Requests and Responses need to drop the packets. This can affect network bandwidth if there are hundreds of slave ports.
- *Mixed*, where Sync and Announce messages are multicast messages but Delay Request and Response messages are unicast. This avoids the issue seen in multicast message mode where every slave port sees Delay Requests and Responses from every other slave port.
- *Unicast*, where you configure the port as a unicast client or server. See {{<link url="#unicast-mode" text="Unicast Mode">}}.

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
hybrid_e2e              1
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

To change the message mode back to the default setting of multicast, remove the `hybrid_e2e` line under the interface, then restart the `ptp4l` service.

{{< /tab >}}
{{< /tabs >}}

### PTP Interface Timers

You can set the following timers for PTP messages.

| Timer | Description |
| ----- | ----------- |
| `announce-interval` | The average interval between successive Announce messages. Specify the value as a power of two in seconds. |
| `announce-timeout` | The number of announce intervals that have to occur without receiving an Announce message before a timeout occurs. Make sure that this value is longer than the announce-interval in your network.|
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

- To set the announce interval between successive Announce messages on swp1 to -1, add `logAnnounceInterval  -1` under the interface stanza.
- To set the mean sync-interval for multicast messages on swp1 to -5, add `logSyncInterval  -5` under the interface stanza.

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

### Local Priority

Set the local priority on an interface for a profile that uses ITU 8275-1 or ITU 8275-2. You can set a value between 0 and 255. The default priority is 128.

The following example sets the local priority on swp1 to 10.

{{< tabs "TabID658 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp local-priority 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the `G.8275.portDS.localPriority` option to the `interface` section of the `/etc/ptp4l.conf` file, then restart the `ptp4l` service.

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
[swp1]
udp_ttl                      1
hybrid_e2e                   1
masterOnly                   0
delay_mechanism              E2E
network_transport            UDPv6
G.8275.portDS.localPriority  10
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional PTP Interface Configuration

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

## Unicast Mode

Cumulus Linux supports unicast mode so that a unicast client can perform *Unicast Discover and Negotiation* with servers. Unlike the default multicast mode, where both the server(master) and client(slave) start sending out announce requests and discover each other, in unicast mode, the client starts by sending out requests for unicast transmission. The client sends this to every server address in its Unicast Master Table. The server responds with an accept or deny to the request.

### Global Unicast Configuration

Unicast clients need a unicast master table for unicast negotiation; you must configure at least one unicast master table on the switch.

To configure unicast globally:
- Set the unicast table ID; a unique ID that identifies the unicast master table.
- Set the unicast master address. You can set more than one unicast master address, which can be an IPv4, IPv6, or MAC address.
- Optional: Set the unicast master query interval, which is the mean interval between requests for Announce messages. Specify this value as a power of two in seconds. You can specify a value between -3 and 4. The default value is -0 (2 power).
{{< tabs "TabID668 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 address 10.10.10.1
cumulus@switch:~$ nv set service ptp 1 unicast-master 1 query-interval 4
cumulus@switch:~$ nv set interface swp1 ptp unicast-master-table-id 1
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

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

### Interface Unicast Configuration

For interface unicast configuration, in addition to enabling PTP on an interface, you also need to configure the PTP interface to be either a unicast client or a unicast server.

When configuring multiple PTP interfaces on the switch to be unicast clients, you must configure a unicast table ID on every interface set as a unicast client. Each client must have a different table ID.

To configure a PTP interface to be the unicast *client*:

{{< tabs "TabID757 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-service-mode client
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Add the following lines at the end of the interface section of the  `/etc/ptp4l.conf` file:

   ```
   [unicast_master_table]
   table_id               3
   logQueryInterval       0
   UDPv4                  100.100.100.1

   [swp1]
   table_id                1
   ...
   ```

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

To configure a PTP interface to be the unicast *server*:

{{< tabs "TabID788 ">}}
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
   unicast_listen      1
   ...
   ```

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

To configure a unicast table ID:

{{< tabs "TabID819 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-master-table-id 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Add the table ID at the end of the interface section of the  `/etc/ptp4l.conf` file:

   ```
   [swp1]
   ...
   table_id   1

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

To show the unicast master table configuration on the switch, run the `nv show service ptp <instance-id> unicast-master <table-id>` command.

### Optional Unicast Interface Configuration

You can set the unicast request duration for unicast clients, which is the service time in seconds requested by the unicast client during unicast negotiation. The default value is 300 seconds.

{{< tabs "TabID855 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 ptp unicast-request-duration 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Add the `unicast_request_duration` parameter at the end of the interface section of the  `/etc/ptp4l.conf` file:

   ```
   [swp1]
   ...
   table_id   1
   unicast_request_duration 20
   ```

3. Restart the `ptp4l` service.

   ```
   cumulus@switch:~$ sudo systemctl restart ptp4l.service
   ```

{{< /tab >}}
{{< /tabs >}}

## PTP Profiles

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
- You cannot set global PTP parameters in a profile currently in use.
- PTP profiles do not support VLANs or bonds.
- If you set a predefined or custom profile, do not change any global PTP settings, such as the <span class="a-tooltip">[DSCP](## "DiffServ code point")</span> or the clock domain.
- For better performance in a high scale network with PTP on multiple interfaces, configure a higher system policer rate with the `nv set system control-plane policer lldp-ptp burst <value>` and `nv set system control-plane policer lldp-ptp rate <value>` commands. The switch uses the LLDP policer for PTP protocol packets. The default value for the LLDP policer is 2500. When you use the ITU 8275.1 profile with higher sync rates, use higher policer values.
{{%/notice%}}

### Set a Predefined Profile

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

To set the predefined ITU 8275.1 profile, edit the `/etc/ptp4l.conf` file and set the parameters shown below, then restart the `ptp4l` service:

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
...
[global]
#
# Default Data Set
#
slaveOnly                      0
priority1                      128
priority2                      128
domainNumber                   24

twoStepFlag                    1
dscp_event                     46
dscp_general                   46
dataset_comparison             G.8275.x
G.8275.defaultDS.localPriority 128
ptp_dst_mac                    01:80:C2:00:00:0E
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

To set the predefined ITU 8275.2 profile, edit the `/etc/ptp4l.conf` file and set the parameters shown below, then restart the `ptp4l` service:

```
cumulus@switch:~$ sudo nano /etc/ptp4l.conf
...
...
[global]
#
# Default Data Set
#
slaveOnly                      0
priority1                      128
priority2                      128
domainNumber                   24

twoStepFlag                    1 
dscp_event                     46
dscp_general                   46
network_transport              UDPv4
dataset_comparison             G.8275.x
G.8275.defaultDS.localPriority 128
hybrid_e2e                     1
inhibit_multicast_service      1
unicast_listen                 1
unicast_req_duration           60
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

To use the predefined IEEE 1588 profile, edit the `/etc/ptp4l.conf` file and set the parameters shown below, then restart the `ptp4l` service:

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

twoStepFlag                    1
dscp_event                     46
dscp_general                   46
network_transport              UDPv4
dataset_comparison             ieee1588
...
```

```
cumulus@switch:~$ sudo systemctl restart ptp4l.service
```

{{< /tab >}}
{{< /tabs >}}

### Create a Custom Profile

To create a custom profile:

{{< tabs "TabID322 ">}}
{{< tab "NVUE Commands ">}}

- Create a profile name.
- Set the profile type on which to base the new profile (`itu-g-8275-1` `itu-g-8275-2`, or `ieee-1588`).
- Update any of the profile settings you want to change (`announce-interval`, `delay-req-interval`, `priority1`, `sync-interval`, `announce-timeout`, `domain`, `priority2`, `transport`, `delay-mechanism`, `local-priority`).
- Set the custom profile to be the current profile.

The following example commands create a custom profile called CUSTOM1 based on the predefined profile ITU 8275-1. The commands set the `domain` to 28 and the `announce-timeout` to 3, then set `CUSTOM1` to be the current profile:

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

The following example `/etc/ptp4l.conf` file creates a custom profile based on the predefined profile ITU 8275-1 and sets the `domain` to 28 and the `announce-timeout` to 3.

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

twoStepFlag                    1
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

To show the settings for a profile, run the `nv show service ptp <instance> profile <profile-name>` command:

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

## Optional Acceptable Master Table

The acceptable master table option is a security feature that prevents a rogue player from pretending to be the grandmaster clock to take over the PTP network. To use this feature, you configure the clock IDs of known grandmaster clocks in the acceptable master table and set the acceptable master table option on a PTP port. The BMC algorithm checks if the grandmaster clock received in the Announce message is in this table before proceeding with the master selection. Cumulus Linux disables this option by default on PTP ports.
<!-- vale off -->
The following example command adds the grandmaster clock ID 24:8a:07:ff:fe:f4:16:06 to the acceptable master table and enables the PTP acceptable master table option for swp1:
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

Cumulus Linux provides the following optional PTP monitoring configuration.

### Configure Clock TimeStamp and Path Delay Thresholds

Cumulus Linux monitors clock timestamp and path delay against thresholds, and generates counters when PTP reaches the set thresholds. You can see the counters in the NVUE `nv show` command output and in log messages.

You can configure the following monitor settings:

{{< tabs "TabID851 ">}}
{{< tab "NVUE Commands ">}}

| Command | Description |
| ----- | ----------- |
| `nv set service ptp <instance> monitor min-offset-threshold` | Sets the minimum difference allowed between the master and slave time. You can set a value between -1000000000 and 0 nanoseconds. The default value is -50 nanoseconds.|
| `nv set service ptp <instance> monitor max-offset-threshold` | Sets the maximum difference allowed between the master and slave time. You can set a value between 0 and 1000000000 nanoseconds. The default value is 50 nanoseconds.|
| `nv set service ptp <instance> monitor path-delay-threshold` | Sets the mean time that PTP packets take to travel between the master and slave. You can set a value between 0 and 1000000000 nanoseconds. The default value is 200 nanoseconds. |
| `nv set service ptp <instance> monitor max-timestamp-entries` | Sets the maximum number of timestamp entries allowed. Cumulus Linux updates the timestamps continuously. You can specify a value between 100 and 200. The default value is 100 entries.|

The following example sets the minimum offset threshold to -1000, the maximum offset threshold to 1000, and the path delay threshold to 300:

```
cumulus@switch:~$ nv set service ptp 1 monitor min-offset-threshold -1000
cumulus@switch:~$ nv set service ptp 1 monitor max-offset-threshold 1000
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

The following example sets the minimum offset threshold to -1000, the maximum offset threshold to 1000, and the path delay threshold to 300:

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

offset_from_master_min_threshold   -1000
offset_from_master_max_threshold   1000
mean_path_delay_threshold          300
...
```

{{< /tab >}}
{{< /tabs >}}

### Configure PTP Logging

A log set contains the log entries for clock timestamp and path delay violations at different times. You can set the number of entries to log and the interval between successive violation logs.

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
| `tsmonitor_num_log_sets` | Sets the maximum number of log sets allowed. You can specify a value between 2 and 4. The default value is 3.|
| `tsmonitor_num_log_entries`  |  Sets the maximum number of log entries allowed in a log set. You can specify a value between 4 and 8. The default value is 4.|
| `tsmonitor_log_wait_seconds` |  Sets the number of seconds to wait before logging back-to-back violations. You can specify a value between 0 and 60. The default value is 1.|

The following example sets the maximum number of log sets allowed to 4, the maximum number of log entries allowed to 6, and the violation log interval to 10:

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
| `nv show service ptp <instance> monitor violations` |  Shows the threshold violation count and the last time a violation of a specific type occurred. |
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

- To clear the maximum offset violation logs, run the `nv action clear service ptp <instance> monitor violations log max-offset` command.
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

### Show PTP Configuration

To show a summary of the PTP configuration on the switch, run the `nv show service ptp <instance>` command:

```
cumulus@switch:~$ nv show service ptp 1
                             operational  applied
---------------------------  -----------  ------------------
enable                       on           on
current-profile                            default-itu-8275-2
domain                                    0
ip-dscp                                   46
logging-level                             info
priority1                                 128
priority2                                 128
[acceptable-master]
monitor
  max-offset-threshold                     50
  max-timestamp-entries                   100
  max-violation-log-entries               4
  max-violation-log-sets                  2
  min-offset-threshold                     -50
  path-delay-threshold                    200
  violation-log-interval                  1
[profile]                                  abc
[profile]                                  default-1588
[profile]                                  default-itu-8275-1
[profile]                                  default-itu-8275-2
[unicast-master]                          1
[unicast-master]                          2
[unicast-master]                          3
[unicast-master]                          4
...
```

You can drill down with the following `nv show service ptp <instance>` commands:
- `nv show service ptp <instance> acceptable-master` shows acceptable master configuration.
- `nv show service ptp <instance> clock-quality` shows the clock quality status.
- `nv show service ptp <instance> current` shows the local states learned during PTP message exchange.
- `nv show service ptp <instance> domain` shows the domain configuration.
- `nv show service ptp <instance> ip-dscp` shows PTP DSCP configuration.
- `nv show service ptp <instance> monitor` shows PTP monitor configuration.
- `nv show service ptp <instance> profile` shows PTP profile configuration.
- `nv show service ptp <instance> parent` shows the local states learned during PTP message exchange.
- `nv show service ptp <instance> priority1` shows PTP priority1 configuration.
- `nv show service ptp <instance> priority2` shows PTP priority2 configuration.
- `nv show service ptp <instance> status` shows the status of all PTP interfaces.
- `nv show service ptp <instance> time-properties` shows the clock time attributes.
- `nv show service ptp <instance> unicast-master` shows the unicast master configuration.

### Show PTP Interface Configuration

To check configuration for a PTP interface, run the `nv show interface <interface> ptp` command.

```
cumulus@switch:~$ nv show interface swp1 ptp
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
```

### Show PTP Counters

To show all PTP counters, run the `nv show service ptp <instance> counters` command:

```
cumulus@switch:~$ nv show service ptp 1 counters
Packet Type              Received       Transmitted    
---------------------    ------------   ------------   
Port swp4
  Announce                 0              10370            
  Sync                     0              20731             
  Follow-up                0              20731            
  Delay Request            0              0              
  Delay Response           0              0              
  Peer Delay Request       0              0              
  Peer Delay Response      0              0              
  Management               0              0              
  Signaling                0              0
```

To show PTP counters for an interface, run the `nv show interface <interface> counters ptp` command.

To clear PTP counters for an interface, run the `nv action clear interface <interface> counters ptp` command:

```
cumulus@switch:~$ nv action clear interface swp1 counters ptp
Action succeeded
```

### Show the Status of All PTP Interfaces

To show the status of all PTP interfaces, run the `nv show service ptp <instance> status` command.
The command output shows the PTP enabled ports, the PTP port mode (unicast or multicast), the state of the port based on BMCA, the unicast state, and identifies the server address to which the client connects.

```
cumulus@switch:~$ nv show service ptp 1 status
Port   Mode   State    Ustate                           Server
-----  -----  -------  -------------------------------  -------
swp9   Ucast  SLAVE    Sync and Delay Granted (H_SYDY)  9.9.9.2
swp10  Ucast  PASSIVE  Initial State (WAIT)
swp11  Ucast  PASSIVE  Initial State (WAIT)
swp12  Ucast  PASSIVE  Initial State (WAIT)
```

### Show the List of NVUE PTP Commands

- To see a full list of NVUE show commands for PTP, run the `nv list-commands service ptp` command.
- To show a full list of show commands for a PTP interface, run the `nv list-commands | grep 'nv show interface <interface-id> ptp'` command.

```
cumulus@switch:~$ nv list-commands service ptp
nv show service ptp
nv show service ptp <instance-id>
nv show service ptp <instance-id> status
nv show service ptp <instance-id> domain
nv show service ptp <instance-id> priority1
nv show service ptp <instance-id> priority2
nv show service ptp <instance-id> ip-dscp
nv show service ptp <instance-id> acceptable-master
...
```

```
cumulus@switch:~$ nv list-commands | grep 'nv show interface <interface-id> ptp'
...
nv show interface <interface-id> ptp
nv show interface <interface-id> ptp timers
nv show interface <interface-id> ptp shaper
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
slaveOnly                      0
priority1                      254
priority2                      254
domainNumber                   3

twoStepFlag                    1
dscp_event                     46
dscp_general                   46

offset_from_master_min_threshold   -50
offset_from_master_max_threshold   50
mean_path_delay_threshold          200
tsmonitor_num_ts                   100
tsmonitor_num_log_sets             2
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
udp_ttl                      1
masterOnly                   0
delay_mechanism              E2E
network_transport            UDPv4

[swp2]
udp_ttl                      1
masterOnly                   0
delay_mechanism              E2E
network_transport            UDPv4

[swp3]
udp_ttl                      1
masterOnly                   0
delay_mechanism              E2E
network_transport            UDPv4

[swp4]
udp_ttl                      1
masterOnly                   0
delay_mechanism              E2E
network_transport            UDPv4
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

### PTP Traffic Shaping

To improve performance on the NVIDIA Spectrum 1 switch for PTP-enabled ports with speeds lower than 100G, you can enable a pre-defined traffic shaping profile. For example, if you see that the PTP timing offset varies widely and does not stabilize, enable PTP shaping on all PTP enabled ports to reduce the bandwidth on the ports slightly and improve timing stabilization.

{{%notice note%}}
- Switches with Spectrum-2 and later do not support PTP shaping.
- Bonds do not support PTP shaping.
- You cannot configure {{<link url="Quality-of-Service/#shaping" text="QoS traffic shaping">}} and PTP traffic shaping on the same ports.
- You must configure a {{<link url="Quality-of-Service/#egress-scheduler" text="strict priority">}} for PTP traffic; for example:

  ```
  cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 0-5,7 mode dwrr
  cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 0-5,7 bw-percent 12
  cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 6 mode strict
  ```

{{%/notice%}}

{{< tabs "TabID1387 ">}}
{{< tab "NVUE Commands ">}}

For each PTP-enabled port on which you want to set traffic shaping, run the `nv set interface <interface> ptp shaper enable on` command.

```
cumulus@switch:~$ nv set interface swp1 ptp shaper enable on
cumulus@switch:~$ nv set interface swp2 ptp shaper enable on
cumulus@switch:~$ nv config apply
```

To see the PTP shaping setting for an interface, run the `nv show interface <interface> ptp shaper` command:

```
cumulus@switch:~$ nv show interface swp1 ptp shaper
        operational  applied  
------  -----------  -------  
enable               on   
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/cumulus/switchd.d/ptp_shaper.conf` file, set the following parameters for the interfaces to which you want to apply traffic shaping and enable the traffic shaper. You must reload `switchd` for the changes to take effect.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/ptp_shaper.conf
## Per-port configuration for PTP shaper
ptp_shaper.port_group_list = [enable-group]
ptp_shaper.enable-group.port_set = swp1,swp2
ptp_shaper.enable-group.ptp_shaper_enable = true
```

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

{{< /tab >}}
{{< /tabs >}}

### Spanning Tree and PTP
<!-- vale off -->
PTP frames are affected by <span class="a-tooltip">[STP](## "Spanning Tree Protocol")</span> filtering; events, such as an STP topology change (where ports temporarily go into the blocking state), can cause interruptions to PTP communications.

If you configure PTP on bridge ports, NVIDIA recommends that the bridge ports are spanning tree edge ports or in a bridge domain where spanning tree is disabled.
<!-- vale on -->