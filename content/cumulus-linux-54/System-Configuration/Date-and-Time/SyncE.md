---
title: SyncE 
author: NVIDIA
weight: 129
draft: true
toc: 3

---
{{%notice note%}}
SyncE is available for early access only.
{{%/notice%}}

<span class="a-tooltip">[SyncE](## "Synchronous Ethernet")</span> is a standard for transmitting clock signals over the Ethernet physical layer to synchronize clocks across the network by propagating frequency using the transmission rate of symbols in the network. A dedicated Ethernet channel, (<span class="a-tooltip">[ESMC](## "Ethernet Synchronization Messaging Channel")</span>), manages this synchronization.

The Cumulus Linux switch includes a SyncE controller and a SyncE daemon.
- The SyncE controller reads performance counters to calculate the differences between TX and RX ethernet symbols on the physical layer to fine tune the clock frequency.
- The SyncE daemon (`syncd`) manages:
  - Transmitting and receiving <span class="a-tooltip">[SSMs](## "Synchronization Status Messages")</span> on all SyncE enabled ports using the Ethernet Synchronization Messaging Channel (ESMC).
  - The synchronization hierarchy and runs the master selection algorithm to choose the best reference clock from the <span class="a-tooltip">[QL](## "Quality Level")</span> in the SSM.
  - Using to the next best clock when the master clock fails. The selection algorithm only selects the best source, which is the Primary Clock source.
  - The switchover time if the algorithm also selects a secondary reference clock in case of primary failure.

## Basic Configuration

Basic SyncE configuration requires you:
- Enable SyncE on the switch.
- Configure SyncE on at least one interface or bond so that the interface is a timing source that passes to the selection algorithm.

The basic configuration shown below uses the default settings:
- The {{<link url="#ql-for-the-switch" text="QL">}} for the switch is set to `option 1`, which includes PRC, SSU-A, SSU-B, SEC and DNU.
- The {{<link url="#frequency-source-priority" text="frequency source priority">}} on the interface is set to 100.
- The {{<link url="#wait-to-restore-time" text="amount of time SyncE waits">}} after the interface comes up before using it for synchronization is set to 5 minutes.

```
cumulus@switch:~$ nv set synce enable on
cumulus@switch:~$ nv set interface swp2 synce enable on
cumulus@switch:~$ nv config apply
```

## Optional Global Configuration

### QL for the Switch

You can specify the ITU-T QL for the switch. You can specify one of the following values. The default is `option 1`.
- `option 1` includes PRC, SSU-A, SSU-B, SEC and DNU.
- `option 2` includes PRS, STU, ST2, ST3, SMC, ST4, RES and DUS.
- `option 3` includes PRS, STU, ST2, ST3, TNC, ST3E, SMC, ST4, PROV and DUS.

The following command example sets the QL for the switch to `option 2`:

{{< tabs "TabID49 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set synce network-type option 2
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the QL setting, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

### Logging

By default, SyncE logging is off on the switch. You can enable logging to write a log message:
- Every time there is a change to the selected source in addition to errors
- Only when there are no available frequency sources or when the only available frequency source is the internal oscillator

The following command example sets logging to write a log message every time there is a change to the selected source in addition to errors:

{{< tabs "TabID81 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set synce changes
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the logging setting, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

The following command example sets logging to write a log message only when there are no available frequency sources or when the only available frequency source is the internal oscillator:

{{< tabs "TabID107 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set synce errors
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the logging setting, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

## Optional Interface Configuration

### Frequency Source Priority

The clock selection algorithm uses the frequency source priority on an interface to choose between two sources that have the same QL. You can specify a value between 1 (the highest priority) and 254 (the lowest priority). The default value is 100.

The following command example sets the priority on swp2 to 254:

{{< tabs "TabID139 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp2 synce priority 254
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the priority setting, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

### Wait to Restore Time

The wait to restore time is the amount of time SyncE waits after the interface comes up before using it for synchronization. You can set a value betwen 0 and 12 minutes. The default value is 5 minutes.

The following command example sets the wait to restore time to 3 minutes:

{{< tabs "TabID169 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp2 synce wait-to-restore 3
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to change the wait to restore time setting, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

### Disable Synchronization Status Messages

You can disable <span class="a-tooltip">[SSMs](## "Synchronization Status Messages")</span> on an interface to prevent sending ESMC packets and ignore any received ESMC packets.

The following command example disables SSMs on swp2:

{{< tabs "TabID199 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp2 synce ssm disable
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to disable SSMs, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

### QL to Transmit in Status Messages

To override the QL (`option 1`, `option 2 generation 1`, or `option 2 generation 2`) transmitted in SSM messages, you can set the following options:
- `exact <ql>` specifies the exact QL regardless of the value received.
- `highest <ql>` specifies an upper limit on the QL. If the selected source has a higher QL than the QL specified here, the switch transmits this QL instead.
- `lowest <ql>` specifies a lower limit on the QL. If the selected source has a lower QL than the QL specified here, the switch transmits DNU instead.

The following command example specifies an upper limit of `option 1`:

{{< tabs "TabID232 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp2 synce highest option 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to specify an upper limit of `option 1`, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The QL must match the globally configured QL with the `network-type` command.
{{%/notice%}}

### QL to Receive in Status Messages

To override the QL (`option 1`, `option 2 generation 1`, or `option 2 generation 2`) received in SSM messages before using it in the selection algorithm, you can set one of the following options:
- `exact <quality-level>`  specifies the exact QL regardless of the value received unless the received value is DNU.
- `highest <quality-level>` specifies an upper limit on the received QL. If the received value is higher than this specified QL, the switch transmits this QL instead.
- `lowest <quality-level>` specifies a lower limit on the received QL. If the received value is lower than this specified QL, the switch transmits DNU instead.

The following command example specifies a lower limit of `option 2 generation 1`:

{{< tabs "TabID269 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp2 synce lowest option 2 generation 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/synced.conf` file to specify a lower limit of `option 2 generation 1`, then restart the `syncd` service.

```
EXAMPLE FILE HERE
```

```
cumulus@switch:~$ sudo systemctl restart syncd
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The QL to receive must match the globally configured QL set with the `network-type` command.
{{%/notice%}}

## Troubleshooting

To show SyncE configuration, run the `nv show synce` command:

```
cumulus@switch:~$ nv show synce
ADD OUTPUT
```

To show SyncE statistics for all the enabled interfaces, run the `nv show synce interface statistics` command:

```
cumulus@switch:~$ nv show synce interface statistics
ADD OUTPUT
```

To show SyncE statistics for a specific interfaces, run the `nv show synce interface statistics <interface>` command:

```
cumulus@switch:~$ nv show synce interface statistics swp2
ADD OUTPUT
```

## Related Information

{{<exlink url="https://www.itu.int/rec/T-REC-G.781" text="ITU G.781">}}
