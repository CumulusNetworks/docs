---
title: Synchronous Ethernet - SyncE 
author: NVIDIA
weight: 128
toc: 3

---
<span class="a-tooltip">[SyncE](## "Synchronous Ethernet")</span> is an ITU-T standard for transmitting clock signals over the Ethernet physical layer to synchronize clocks across the network by propagating frequency using the transmission rate of symbols in the network. A dedicated channel, <span class="a-tooltip">[ESMC](## "Ethernet Synchronization Messaging Channel")</span> manages this synchronization, as specified by the ITU-T Rec. G.8264 standard.

The Cumulus Linux switch includes a SyncE controller and a SyncE daemon.
- The SyncE controller reads performance counters to calculate the differences between transmit and receive ethernet symbols on the physical layer to fine tune the clock frequency.
- The SyncE daemon (`synced`):
  - Manages transmitting and receiving <span class="a-tooltip">[SSMs](## "Synchronization Status Messages")</span> on all SyncE enabled ports using the Ethernet Synchronization Messaging Channel (ESMC).
  - Manages the synchronization hierarchy and runs the master selection algorithm to choose the best reference clock from the <span class="a-tooltip">[QL](## "Quality Level")</span> in the SSM.

Cumulus Linux constructs the SyncE clock identity as follows:
- The higher order 3 bytes are from the higher order 3 bytes (OUI) of the base MAC address.
- The middle 2 bytes are 0xff 0xfe.
- The lower order 3 bytes are from the lower order 3 bytes of the base MAC address.

{{%notice note%}}
- Cumulus Linux supports SyncE for the NVIDIA SN3750-SX switch only.
- SyncE on 1G interfaces only supports 1000BASE-SX transceivers, 1000BASE-LX transceivers, and ADVA 5401 GrandMaster transceivers.
{{%/notice%}}

## Basic Configuration

Basic SyncE configuration requires you:
- Enable SyncE on the switch.
- Configure SyncE on at least one interface so that the interface is a timing source that passes to the selection algorithm.
- Set the SyncE bundle ID to prevent loops if more than one link comes from the same clock source. You can set a value between 1 and 256.

The basic configuration shown below uses the default SyncE settings:
<!-- - The {{<link url="#ql-for-the-switch" text="QL">}} for the switch is set to `option 1`, which includes PRC, SSU-A, SSU-B, SEC and DNU.-->
- The {{<link url="#frequency-source-priority" text="frequency source priority">}} on the interface is set to 100.
- The {{<link url="#wait-to-restore-time" text="amount of time SyncE waits">}} after the interface comes up before using the interface for synchronization is set to 5 minutes.

{{< tabs "TabID33 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system synce enable on
cumulus@switch:~$ nv set interface swp2 synce enable on
cumulus@switch:~$ nv set interface swp2 synce bundle-id 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced/synced.conf` file to configure the interface, then enable and start the SyncE service. Adding an interface section in the `/etc/synced/synced.conf` file enables SyncE on that interface.

The following example enables SyncE on swp2.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
# NVUE SyncE state is enable on

[global]
twtr_seconds=300
priority=1

[swp2]
bundle=10
```

```
cumulus@switch:~$ sudo systemctl enable synced.service
cumulus@switch:~$ sudo systemctl start synced.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional Global Configuration

### Wait to Restore Time

The wait to restore time is the number of seconds SyncE waits for each port to be up before opening the Ethernet Synchronization Message Channel (ESMC) for messages. You can set a value between 0 and 720 (12) minutes. The default value is 300 seconds (5 minutes).

The following command example sets the wait to restore time to 180 seconds (3 minutes):

{{< tabs "TabID63 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system synce wait-to-restore-time 180
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced/synced.conf` file to change the `twtr_seconds setting`, then restart the SyncE service.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
[global]
twtr_seconds=180
```

```
cumulus@switch:~$ sudo systemctl restart synced.service
```

{{< /tab >}}
{{< /tabs >}}

### Priority

You can set the priority for the clock source. The lowest priority is 1 and the highest priority is 256. If two clock sources have the same priority, the switch uses the lowest clock source.

The following example command sets the priority to 256:

{{< tabs "TabID96 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system synce provider-default-priority 256
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced/synced.conf` file to change the `priority` setting, then restart the SyncE service.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
[global]
twtr_seconds=180
priority=256
```

```
cumulus@switch:~$ sudo systemctl restart synced.service
```

{{< /tab >}}
{{< /tabs >}}

### Minimum Acceptable Quality Level

You can prevent SyncE from tracking a source with a quality level lower than a specific value. The quality level can be: `eec1`, `eeec`, `ssu-b`, `ssu-a`, `prc`, `eprc`, `prtc`, or `eprtc`, where `eec1` is the lowest quality level and `eprtc` is the highest quality level.

{{< tabs "TabID188 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set system synce min-acceptable-ql <quality-level>` command. The following example prevents SyncE from tracking a source with a quality level lower than `ssu-b`:

```
cumulus@switch:~$ nv set system synce min-acceptable-ql ssu-b
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced/synced.conf` file to add the `min_ql` parameter, then restart the SyncE service. The following example prevents SyncE from tracking a source with a quality level lower than `ssu-b`:

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
min_ql=ssu-b
```

```
cumulus@switch:~$ sudo systemctl restart synced.service
```

{{< /tab >}}
{{< /tabs >}}

### Logging

You can set the logging level that the SyncE service uses:
- `critical` level logs critical errors and notices.
- `debug` level logs fine-grained informational events that are most useful to debug an application.
- `error` level logs errors.
- `info` level logs informational messages.
- `notice` level logs notices.

The following example command sets the logging level to `debug`.

{{< tabs "TabID135 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system synce log-level debug
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the `log-level` setting, then *reload* the SyncE service.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
[global]
twtr_seconds=180
priority=256
loglevel=debug
```

```
cumulus@switch:~$ sudo systemctl reload synced.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional Interface Configuration

### Frequency Source Priority

The clock selection algorithm uses the frequency source priority on an interface to choose between two sources that have the same <span class="a-tooltip">[QL](## "Quality Level")</span>. You can specify a value between 1 (the highest priority) and 256 (the lowest priority). The default value is 1.

The following command example sets the priority on swp2 to 10, on swp2 to 20, and on swp3 to 10:

{{< tabs "TabID172 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 synce provider-priority 10
cumulus@switch:~$ nv set interface swp2 synce provider-priority 20
cumulus@switch:~$ nv set interface swp3 synce provider-priority 10
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the `priority` setting for the interface, then restart the SyncE service.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
[global]
twtr_seconds=180
priority=256
log-level=debug

[swp1]
priority=10
 
[swp2]
priority=20
 
[swp3]
priority=10
```

```
cumulus@switch:~$ sudo systemctl restart synced.service
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

## Show SyncE Configuration and Counters

To show global SyncE configuration, run the NVUE `nv show system synce` command or the Linux `syncectl show status` command.

To show SyncE configuration for a specific interface, run the NVUE `nv show interface <interface-id> synce` command or the Linux  `syncectl show interface status <interface>` command.

```
cumulus@switch:~$ nv show system synce
                           operational                                                        applied
-------------------------  -----------------------------------------------------------------  -------
enable                     On                                                                 on
log-level                  notice
provider-default-priority  10                                                                 10
wait-to-restore-time       40                                                                 40
clock-identity             0x849e00fffe00ca00
local-clock-quality        eec1
network-type               1
summary                    Group #0: TRACKING holdover acquired on swp1. freq_diff: 77 (ppb)
```

To show SyncE statistics for a specific interface, run the NVUE `nv show interface <interface-id> counters synce` command or the Linux `syncectl show interface counters <interface` command:

```
cumulus@switch:~$ nv show interface swp2 counters synce
Packet Type                       Received       Transmitted    
---------------------             ------------   ------------   
ESMC                                      700            708
ESMC Error                                  0              0
ESMC DNU                                  549              0
ESMC EEC1                                   1            558
ESMC E-EEC                                  0              0
ESMC SSU B                                  0              0
ESMC SSU A                                  0              0
ESMC PRC                                  150            150
ESMC E-PRC                                  0              0
ESMC PRTC                                   0              0
ESMC E-PRTC                                 0              0
ESMC Unknown                                0              0
```

## Clear SyncE Interface Counters

To clear counters for a specific SyncE interface, run the NVUE `nv action clear interface <interface> counters synce` command or the Linux `syncectl clear interface counters <interface>` command.

```
cumulus@switch:~$ nv action clear interface swp1 counters synce
swp1 counters cleared
Action succeeded
```

To clear counters for all SyncE interfaces, run the `syncectl clear counters` command.

To see all the `syncectl` commands, run `syncectl -h`.

## Related Information

{{<exlink url="https://www.itu.int/rec/T-REC-G.781" text="ITU G.781">}}
