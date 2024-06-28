---
title: High Frequency Telemetry
author: NVIDIA
weight: 1232
toc: 3
---
High frequency telemetry enables you to collect counters at very short sampling intervals (single digit milliseconds to microseconds), which is useful for AI training. The data can help you detect short duration events like microbursts, and provides information about where in time the events happen and for how long. High frequency telemetry data provides time series data that traditional histograms cannot provide. The time series data helps you understand the shape of the traffic pattern and identify any spikes or dips, or jitter in the traffic.

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 switches.
- To correlate counters from different switches for debugging and profiling, the switches must have the same time (the switch adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP. NVIDIA recommends using PTP because the timestamp is accurate among the switches in the fabric at the microsecond level.
{{%/notice%}}

After the high frequency telemetry session completes, you can either:
- Export the data to a configured influxDB.
- Export the `json` file with the collected data to an external target. The `json` format file is stored in the `/var/run/cumulus/hft` directory, and includes the counter data for each sampling interval and a timestamp showing when the data was collected.

You can then process the data, plot it into a time-series graph and see how the network behaves in each training step with high precision.

{{%notice note%}}
This collected data is available on the switch until you trigger the next data collection or you reboot the switch.
{{%/notice%}}

## Configure Data Collection

High frequency telemetry uses profiles for data collection. A profile is a set of configurations.

{{%notice note%}}
You cannot delete or modification a profile if jobs are already running or scheduled.
{{%/notice%}}

To configure data collection:
- Set the sampling interval in microseconds.
- Set the egress queue priorities (traffic class 0-15).
- Specify the list of counters you want to collect (`tx-byte`, `rx-byte`, `tc-occupancy`)

The following example sets the sampling interval to 1000, the traffic class 0, 3, and 7, and the list of counters to `tx-byte` and `tc-occupancy`:

```
cumulus@switch:~$ nv set service telemetry hft profile profile1 sample-interval 1000
cumulus@switch:~$ nv set service telemetry hft profile profile1 traffic-class 0,3,7 
cumulus@switch:~$ nv set service telemetry hft profile profile1 counter tx-byte,tc-occupancy
```

## Configure Data Export

To configure the data export, specify the external target information: the IP address and port of the influxDB host, the bucket, organization, and token.

The following example configures data upload to a configured influxDB and sets the influxDB host IP address to 10.10.1.1, port to 12345, bucket to `hft-data`, organization to `nvidia` and token to `token1`:

``` 
cumulus@switch:~$ nv set service telemetry hft target influxdb host 10.10.1.1 
cumulus@switch:~$ nv set service telemetry hft target influxdb port 12345 
cumulus@switch:~$ nv set service telemetry hft target influxdb bucket hft-data 
cumulus@switch:~$ nv set service telemetry hft target influxdb org nvidia 
cumulus@switch:~$ nv set service telemetry hft target influxdb token token1 
```

## Configure the Session Schedule

To schedule the session, configure:
- The start date and time in YYYY-MM-DD HH:MM:SS format.
- The session duration in seconds.
- The profile name.
- The ports on which you want to collect the data.
- A short description for the session (in quotes).

The following example configures the session to start on 2024-01-01 at 10:00:00, last 30 seconds, use the profile called profile1, collect the data on swp1 through swp64 and provide the session description `first collection`.
``` 
cumulus@switch:~$ nv action schedule service telemetry hft job 2024-01-01 10:00:00 duration 30 profile profile1 ports swp1-swp64 description "first collection"
```

## Cancel a Session

To cancel a scheduled telemetry session, run the `nv action cancel service telemetry hft job <job-id> profile <profile-id>` command. You can cancel a specific or all sessions (jobs).

The following example cancels all sessions under the profile called `profile1`:

```
cumulus@switch:~$ nv action cancel service telemetry hft job all profile profile1
```