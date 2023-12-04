---
title: Pulse Per Second - PPS
author: NVIDIA
weight: 127
toc: 3
---
<span style="background-color:#F5F5DC">[PPS](## "Pulse per second")</span> is the simplest form of synchronization. The PPS source provides a signal precisely every second. The NVIDIA Spectrum switch is capable of using an external PPS signal to synchronize its <span style="background-color:#F5F5DC">[PHC](## "Physical Hardware Clock")</span> (for PPS In) and can also generate the PPS signal that other devices can use to synchronize their clocks (for PPS Out).
- In PPS Out mode, the switch can output the PPS signal. The switch can use this signal to check the accuracy of its PHC frequency and other devices can use this signal to synchronize their PHC.
- In PPS In mode, the switch can use an external PPS signal to synchronize the frequency of its PHC. The PPS signal provides frequency synchronization for the clock but does not provide the <span style="background-color:#F5F5DC">[ToD](## "Time Of Day")</span>. Cumulus Linux uses PTP for the ToD; you must have a PTP slave port configured on the switch for PPS In.

{{%notice note%}}
Cumulus Linux supports PPS for the NVIDIA SN3750-SX switch only.
{{%/notice%}}

## Enable PPS Synchronization

To enable PPS synchronization:

{{< tabs "TabID498 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID501 ">}}
{{< tab "Enable PPS In ">}}

Before you enable PPS In, make sure to configure a PTP slave port on the switch. See {{<link url="Precision-Time-Protocol-PTP/#basic-configuration" text="Precision Time Protocol - PTP.">}}

```
cumulus@switch:~$ nv set platform pulse-per-second in state enabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Enable PPS Out ">}}

```
cumulus@switch:~$ nv set platform pulse-per-second out state enabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID522 ">}}
{{< tab "Enable PPS In ">}}

1. Edit the `/etc/linuxptp/ts2phc.conf` file to set the following parameters.

   ```
   cumulus@switch:~$ sudo nano /etc/linuxptp/ts2phc.conf
   # Default configurations
   [global]
   use_syslog                0
   verbose                   1
   logging_level             6
   slave_event_monitor       /var/run/ptp_sem.sock
   ts2phc.pulsewidth         500000000
   ts2phc.tod_source         ptp 
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
   step_threshold                 0.000000050
   first_step_threshold           0.000000001
   max_frequency                  500000000
   sanity_freq_limit              0

   [/dev/ptp1] 
   ts2phc.pin_index               0 
   ts2phc.channel                 0
   ts2phc.extts_polarity          rising 
   ts2phc.extts_correction        0
   ```

2. Edit the `Default interface options` section of the `/etc/ptp4l.conf` file to configure the PTP slave port on the switch, which is required for PPS In.

   ```
   cumulus@switch:~$ sudo nano /etc/linuxptp/pps_out.conf
   ...
   # Default interface options
   #
   time_stamping                  hardware
   [swp29]
   udp_ttl                      1
   masterOnly                   0
   delay_mechanism              E2E
   network_transport            UDPv4
   ```

3. Enable and start the `ptp4l` and `phc2sys` services:

   ```
   cumulus@switch:~$ sudo systemctl enable ptp4l.service phc2sys.service
   cumulus@switch:~$ sudo systemctl start ptp4l.service phc2sys.service
   ```

{{< /tab >}}
{{< tab "Enable PPS Out ">}}

1. Edit the `/etc/linuxptp/pps_out.conf` file to set the following parameters.

  ```
  cumulus@switch:~$ sudo nano /etc/linuxptp/pps_out.conf
  # Configuration file used for the pps_out.service
  # It is shell formatted and the file is source'd by the service
  # Set the PTP device to source our PPS from. 
  # If not specified, the service will find the first device with a clock name "sx_ptp".
  PTP_DEV=/dev/ptp1
  # Set the pin index on the PPS device to send on. 
  # On the NVIDIA systems, only pin 1 (0-based) is supported
  OUT_PIN=1
  # Set the file where to cache the last started values. 
  # This is used primarily in the "stop" operation to know what to clean up.
  CACHE_FILE=/var/run/pps_out
  # Set the out pulse charateristics for frequency and width
  PULSE_FREQ=1000000000
  PULSE_WIDTH=500000000
  PULSE_PHASE=0
  ```

2. Enable and start the `pps_out` service:

   ```
   cumulus@switch:~$ sudo systemctl enable pps_out.service 
   cumulus@switch:~$ sudo systemctl start pps_out.service 
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## PPS Synchronization Settings

You can configure these PPS settings:

| PPS In Setting | Description |
| ------- | ----------- |
| `channel-index` | Sets the channel index. You can set a value of 1 or 0. The default value is 0.|
| `logging-level` | Sets the logging level for PPS In. You can specify `emergency`, `alert`, `critical`, `error`, `warning`, `notice`, `info`, or `debug`. The default logging level is `info`.|
| `pin-index` |  Sets the pin index. You can set a value of 1 or 0. The default value is 0.|
| `signal-polarity` | Sets the polarity of the PPS IN signal. You can specify `rising-edge`, `falling-edge`, or `both`. The default setting is `rising-edge`.|
| `signal-width` | Sets the pulse width of the PPS IN signal. You can set a value between 1000000 and 999000000. The default value is 500000000.|
| `timestamp-correction` | Sets the value, in nanoseconds, to add to each PPS time stamp. You can set a value between -1000000000 and 1000000000. The default value is 0. |  

| PPS Out Setting | Description |
| ------- | ----------- |
| `channel-index`| Sets the channel index. You can set a value of 1 or 0. The default value is 0.|
| `frequency-adjustment` | Sets the frequency adjustment of the PPS Out signal. You can set a value between 1000000000 and 2147483647. The default value is 1000000000.|
| `phase-adjustment` | Sets the phase adjustment of the PPS Out signal. You can set a value between 0 and 1000000000. The default value is 0.|
| `pin-index` | Sets the pin index. Cumulus Linux supports only pin 1.|
| `signal-width` | Sets the pulse width of the PPS OUT signal. You can set a value between 1000000 and 999000000. The default value is 500000000.|

{{< tabs "TabID592 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID621 ">}}
{{< tab "PPS In ">}}

The following example configures PPS In and sets:
- The channel index to 1.
- The pin index to 1.
- The signal width to 999000000.
- The time stamp correction to 1000000000.
- The logging level to `warning`.
- The polarity of the PPS IN signal to `falling-edge`.

```
cumulus@switch:~$ nv set platform pulse-per-second in channel-index 1
cumulus@switch:~$ nv set platform pulse-per-second in pin-index 1
cumulus@switch:~$ nv set platform pulse-per-second in signal-width 999000000
cumulus@switch:~$ nv set platform pulse-per-second in timestamp-correction 1000000000
cumulus@switch:~$ nv set platform pulse-per-second in logging-level warning
cumulus@switch:~$ nv set platform pulse-per-second in signal-polarity falling-edge
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "PPS Out ">}}

The following example configures PPS Out and sets:
- The channel index to 1.
- The signal width to 999000000.
- The phase adjustment of the PPS Out signal to 1000000000.
- The frequency-adjustment of the PPS Out signal to 2147483647.

```
cumulus@switch:~$ nv set platform pulse-per-second out channel-index 1
cumulus@switch:~$ nv set platform pulse-per-second out signal-width 999000000
cumulus@switch:~$ nv set platform pulse-per-second out phase-adjustment 1000000000
cumulus@switch:~$ nv set platform pulse-per-second out frequency-adjustment 2147483647
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID665 ">}}
{{< tab "PPS In ">}}

To configure PPS In, edit the `/etc/linuxptp/ts2phc.conf` file, then restart the PPS In service with the `sudo systemctl restart ts2phc.service` command.

The following example configures PPS In and sets:
- The channel index to 1
- The pin index to 1
- The signal width to 999000000.
- The time stamp correction to 1000000000.
- The logging level to 4 (warning).
- The polarity of the PPS IN signal to falling edge (`falling`).

```
cumulus@switch:~$ sudo nano /etc/linuxptp/ts2phc.conf
# ts2phc is enabled 
[global] 
use_syslog                     0 
verbose                        1 
slave_event_monitor            /var/run/ptp_sem.sock 
logging_level                  4 
ts2phc.pulsewidth              999000000 
ts2phc.tod_source              ptp 
domainNumber                   0
...
[/dev/ptp1] 
ts2phc.pin_index               1 
ts2phc.channel                 1 
ts2phc.extts_polarity          falling 
ts2phc.extts_correction        0
```

{{< /tab >}}
{{< tab "PPS Out ">}}

To configure PPS Out, edit the `/etc/linuxptp/pps_out.conf.conf` file, then restart the PPS Out service with the `sudo systemctl restart pps_out.service` command.

The following example configures PPS Out and sets:
- The channel index to 1.
- The signal width to 999000000.
- The phase adjustment of the PPS Out signal to 1000000000.
- The frequency-adjustment of the PPS Out signal to 2147483647.

```
cumulus@switch:~$ sudo nano /etc/linuxptp/pps_out.conf.conf
# Configuration file used for the pps_out.service
# It is shell formatted and the file is source'd by the service

# Set the PTP device to source our PPS from. 
# If not specified, the service will find the first device with a clock name "sx_ptp".
PTP_DEV=/dev/ptp1

# Set the pin index on the PPS device to send on. 
# On the NVIDIA systems, only pin 1 (0-based) is supported
OUT_PIN=1

OUT_CHANNEL=1 

# Set the file where to cache the last started values. 
# This is used primarily in the "stop" operation to know what to clean up.
CACHE_FILE=/var/run/pps_out

# Set the out pulse charateristics for frequency and width
PULSE_FREQ=2147483647
PULSE_WIDTH=999000000
PULSE_PHASE=1000000000
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

To show a summary of the PPS In and PPS out configuration settings, run the `nv show platform pulse-per-second` command.

```
cumulus@switch:~$ nv show platform pulse-per-second
                        applied
----------------------  -----------
in
  state                 enabled
  pin-index             0
  channel-index         0
  signal-width          500000000
  signal-polarity       rising-edge
  timestamp-correction  0
  logging-level         info
out
  state                 disabled
  pin-index             1
  channel-index         0
  frequency-adjustment  1000000000
  phase-adjustment      0
  signal-width          500000000
```

To show only PPS In configuration settings, run the `nv show platform pulse-per-second in` command:

```
cumulus@switch:~$ nv show platform pulse-per-second in
                      applied
--------------------  -----------
state                 enabled
pin-index             0
channel-index         0
signal-width          500000000
signal-polarity       rising-edge
timestamp-correction  0
logging-level         info
```

To show only PPS Out configuration settings, run the `nv show platform pulse-per-second out` command:

```
cumulus@switch:~$ nv show platform pulse-per-second out
                      applied
--------------------  ----------
state                 disabled
pin-index             1
channel-index         0
frequency-adjustment  1000000000
phase-adjustment      0
signal-width          500000000
```
