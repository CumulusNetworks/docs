---
title: SyncE 
author: NVIDIA
weight: 129
toc: 3

---
<span style="background-color:#F5F5DC">[SyncE](## "Synchronous Ethernet")</span> is a standard for transmitting clock signals over the Ethernet physical layer to synchronize clocks across the network by propagating frequency using the transmission rate of symbols in the network. A dedicated Ethernet channel, (<span style="background-color:#F5F5DC">[ESMC](## "Ethernet Synchronization Messaging Channel")</span>), manages this synchronization.

The Cumulus Linux switch includes a SyncE controller and a SyncE daemon.
- The SyncE controller reads performance counters to calculate the differences between transmit and receive ethernet symbols on the physical layer to fine tune the clock frequency.
- The SyncE daemon (`syncd`) manages:
  - Transmitting and receiving <span style="background-color:#F5F5DC">[SSMs](## "Synchronization Status Messages")</span> on all SyncE enabled ports using the Ethernet Synchronization Messaging Channel (ESMC).
  - The synchronization hierarchy and runs the master selection algorithm to choose the best reference clock from the <span style="background-color:#F5F5DC">[QL](## "Quality Level")</span> in the SSM.
  - The next best clock to use when the master clock fails. The selection algorithm only selects the best source, which is the Primary Clock source.
  - The switchover time if the algorithm also selects a secondary reference clock in case of primary failure.

{{%notice note%}}
Cumulus Linux supports SyncE for the NVIDIA SN3750-SX switch only.
{{%/notice%}}

## Basic Configuration

Basic SyncE configuration requires you:
- Enable SyncE on the switch.
- Configure SyncE on at least one interface or bond so that the interface is a timing source that passes to the selection algorithm.

The basic configuration shown below uses the default SyncE settings:
<!-- - The {{<link url="#ql-for-the-switch" text="QL">}} for the switch is set to `option 1`, which includes PRC, SSU-A, SSU-B, SEC and DNU.-->
- The {{<link url="#frequency-source-priority" text="frequency source priority">}} on the interface is set to 100.
- The {{<link url="#wait-to-restore-time" text="amount of time SyncE waits">}} after the interface comes up before using the interface for synchronization is set to 5 minutes.

{{< tabs "TabID33 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service synce enable on
cumulus@switch:~$ nv set interface swp2 synce enable on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Start the synce service:

```
cumulus@switch:~$ sudo systemctl enable synced.service
cumulus@switch:~$ sudo systemctl start synced.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional Global Configuration

### Wait to Restore Time

The wait to restore time is the number of seconds SyncE waits for each port to be up before opening the Ethernet Synchronization Message Channel (ESMC) for messages. You can set a value betwen 0 and 720 (12) minutes. The default value is 300 seconds (5 minutes).

The following command example sets the wait to restore time to 180 seconds (3 minutes):

{{< tabs "TabID63 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service synce wait-to-restore-time 180
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced/synced.conf` file to change the `twtr_seconds setting`, then restart the `syncd` service.

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

You can set the priority for the clock source. The lowest priority is 1 and the the highest priority is 256. If two clock sources has the same priority, the switch uses the lowest clock source.

The following example command sets the priority to 256:

{{< tabs "TabID96 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set service synce provider-default-priority 256
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced/synced.conf` file to change the `priority` setting, then restart the `syncd` service.

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
cumulus@switch:~$ nv set service synce log-level debug
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the `log-level` setting, then restart the `syncd` service.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
[global]
twtr_seconds=180
priority=256
loglevel=debug
```

```
cumulus@switch:~$ sudo systemctl restart synced.service
```

{{< /tab >}}
{{< /tabs >}}

## Optional Interface Configuration

### Frequency Source Priority

The clock selection algorithm uses the frequency source priority on an interface to choose between two sources that have the same <span style="background-color:#F5F5DC">[QL](## "Quality Level")</span>. You can specify a value between 1 (the highest priority) and 254 (the lowest priority). The default value is 100.

The following command example sets the priority on swp2 to 1, on swp2 to 10, and on swp3 to 1:

{{< tabs "TabID172 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 synce provider-priority 1
cumulus@switch:~$ nv set interface swp2 synce provider-priority 10
cumulus@switch:~$ nv set interface swp3 synce provider-priority 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the `priority` setting for the interface, then restart the `syncd` service.

```
cumulus@switch:~$ sudo nano /etc/synced/synced.conf
...
[global]
twtr_seconds=180
priority=256
log-level=debug

[swp1]
priority=1
 
[swp2]
priority=10
 
[swp3]
priority=1
```

```
cumulus@switch:~$ sudo systemctl restart synced.service
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show global SyncE configuration, run the `nv show service synce` command. To show SyncE configuration for a specific interface, run the `nv show interface <interface-id> synce` command.

```
cumulus@switch:~$ nv show service synce
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

To show SyncE statistics for a specific interface, run the `nv show interface <interface-id> synce counters` command:

```
cumulus@switch:~$ nv show interface swp2 synce counters
                 operational  applied
---------------  -----------  -------
rx-esmc          248899
rx-esmc-dnu      0
rx-esmc-e-eec    0
rx-esmc-e-prc    241259
rx-esmc-e-prtc   0
rx-esmc-eec1     0
rx-esmc-error    0
rx-esmc-prc      4125
rx-esmc-prtc     0
rx-esmc-ssu-a    0
rx-esmc-ssu-b    0
rx-esmc-unknown  3515
tx-esmc          249107
tx-esmc-dnu      245111
tx-esmc-e-eec    0
tx-esmc-e-prc    107
tx-esmc-e-prtc   0
tx-esmc-eec1     2488
tx-esmc-error    4
tx-esmc-prc      1401
tx-esmc-prtc     0
tx-esmc-ssu-a    0
tx-esmc-ssu-b    0
tx-esmc-unknown  0
```

## Related Information

{{<exlink url="https://www.itu.int/rec/T-REC-G.781" text="ITU G.781">}}
