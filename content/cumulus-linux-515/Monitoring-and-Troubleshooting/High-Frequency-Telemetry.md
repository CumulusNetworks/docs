---
title: High Frequency Telemetry
author: NVIDIA
weight: 1229
toc: 2
---

High frequency telemetry enables you to collect counters at very short sampling intervals (single digit milliseconds to microseconds). The data can help you detect short duration events like microbursts, and provides information about where in time the events happen and for how long.

High frequency telemetry data provides time-series data that traditional histograms cannot provide. This data can help you understand the shape of the traffic pattern and identify any variability, or jitter in the traffic.

Cumulus Linux provides two different methods to collect and analyze high frequency telemetry data:
- {{<link url="#streaming-hft-export" text="Stream HFT data">}} to an external collector through {{<link url="Open-Telemetry-Export/#grpc-otlp-export" text="open telemetry export">}}.
- {{<link url="#collect-hft-in-json-file" text="Collect HFT data in a JSON format file">}} on the switch filesystem, and upload the file to an external location for analysis.

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 and later switches. 
- Cumulus Linux does not support high frequency telemetry on ports using 8 lanes. On the Spectrum-4 switch, swp1 through swp64 use all 8 lanes; to run high frequency telemetry, you must break out these ports.
- To correlate counters from different switches, the switches must have the same time (Cumulus Linux adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP; however, NVIDIA recommends using PTP because the timestamp is accurate between switches in the fabric at the microsecond level.
- Streaming HFT export produces a large number of metrics and is supported only with a {{<link url="Open-Telemetry-Export/#grpc-otlp-export" text="single gRPC export destination">}}. If you are exporting OTEL data to more than one destination, do not enable HFT globally and configure a {{<link url="Open-Telemetry-Export/#customize-export" text="`stats-group`">}} to enable `hft` export to only one destination.
{{%/notice%}}

## Streaming HFT Export

You can stream HFT data to your {{<link url="Open-Telemetry-Export/#grpc-otlp-export" text="open telemetry export destination">}}.  To configure OTLP streaming of HFT data:

1. Configure {{<link url="Open-Telemetry-Export" text="open telemetry">}} and add your collector as a gRPC export destination.

2. Configure streaming HFT parameters:

Configure the sampling interval for HFT data. The default value is 5000 microseconds. The interval must be specified in microseconds, with a valid range of 100 to 12,750 and in multiples of 50:

```
cumulus@switch:~$ nv set system telemetry hft sample-interval-usec 1000
cumulus@switch:~$ nv config apply
```

Configure the counters that are sampled at the defined interval. The options for sampling are received bytes (`rx-byte`), transmitted bytes (`tx-byte`), received packets (`rx-packet`), transmitted packets (`tx-packet`), and traffic class buffer occupancy (`tc-occupancy`):

```
cumulus@switch:~$ nv set system telemetry hft counter rx-byte
cumulus@switch:~$ nv set system telemetry hft counter tx-byte
cumulus@switch:~$ nv set system telemetry hft counter tc-occupancy
cumulus@switch:~$ nv config apply
```

When collecting traffic class buffer occupancy counters, configure the traffic classes to monitor:

```
cumulus@switch:~$ nv set system telemetry hft egress-buffer traffic-class 0,1,5
cumulus@switch:~$ nv config apply
```

Configure the interfaces that HFT monitors to collect data:

```
cumulus@switch:~$ nv set interface swp1s0-3,swp2s0-3 telemetry hft state enabled
cumulus@switch:~$ nv config apply
```

Configure a duration, in seconds, to stop streaming HFT data after a specified period. The maximum duration is 1 hour (3600 seconds):

```
cumulus@switch:~$ nv set system telemetry hft duration 120
cumulus@switch:~$ nv config apply
```

3. Enable HFT streaming to export data to your configured {{<link url="Open-Telemetry-Export/#grpc-otlp-export" text="open telemetry export destination">}}:

If you are only exporting OTEL data to a single collector from your switch, you can enable HFT export globally:

```
cumulus@switch:~$ nv set system telemetry hft export state enabled 
cumulus@switch:~$ nv config apply
```

Otherwise, configure a new statistic group to enable only HFT export to a destination:

```
cumulus@switch:~$ nv set system telemetry stats-group ONLY-HFT hft export state enabled
cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 stats-group ONLY-HFT
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
After you enable HFT export and the configured duration completes, you must disable and then reenable HFT export if you want to restart HFT collection and export.

If you have HFT enabled globally (for when you are only generating OTLP data to a single collector for HFT):

```
cumulus@switch:~$ nv set system telemetry hft export state disabled
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv set system telemetry hft export state enabled
cumulus@switch:~$ nv config apply
```

If you have a statistics group configured to enable HFT only for a single destination:

```
cumulus@switch:~$ nv set system telemetry stats-group ONLY-HFT hft export state disabled
cumulus@switch:~$ nv config apply
cumulus@switch:~$ nv set system telemetry stats-group ONLY-HFT hft export state enabled
cumulus@switch:~$ nv config apply
```
{{%/notice%}}

You can view HFT status and configured parameters with the `nv show system telemetry hft` command:

```
cumulus@switch:mgmt:~# nv show system telemetry hft
                      operational          applied  pending
--------------------  -------------------  -------  -------
export                                                     
  state                                    enabled  enabled
duration                                   120      120    
sample-interval-usec                       1000     1000   
session-status                                             
  status              COMPLETED                            
  timestamp           2025-10-29 08:02:08                  



Counters
===========
    Counter     
    ------------
    rx-byte     
    tc-occupancy
    tx-byte     



Egress Buffer
================
    Traffic Class
    -------------
    0            
    1            
    5            



HFT Interfaces
=================
    Interface
    ---------
    swp1s0   
    swp1s1   
    swp1s2   
    swp1s3   
    swp2s0   
    swp2s1   
    swp2s2   
    swp2s3   



profile
==========
    Profile   traffic-class  counter       sample-interval
    --------  -------------  ------------  ---------------
    standard  3              rx-byte       5000           
                             tc-occupancy                 
                             tx-byte                      



job
======
No Data
```

### Considerations and Scale

High-frequency telemetry generates a significant volume of data records. For example, enabling a single counter for HFT on one port with a sample interval of 100 microseconds can produce approximately 90 MB of data during a 10-second collection period. At higher interface or counter scales, the required storage capacity on your collector increases substantially. To optimize storage utilization, enable data compression on the collector when handling large telemetry datasets.

## Collect HFT in JSON File

Cumulus Linux provides two options to configure HFT to collect data in a JSON file on the switch; you can run NVUE commands or use the Cumulus Linux job management tool (`cl-hft-tool`). You can see all the `cl-hft-tool` command options with `cl-hft-tool -h`. NVIDIA recommends that you use NVUE commands.

To configure high frequency telemetry:
1. Enable telemetry with the `nv set system telemetry state enabled` command.
2. {{<link url="#configure-data-collection" text="Configure data collection">}}.
3. {{<link url="#configure-json-data-export" text="Configure data export">}}.
4. {{<link url="#configure-the-schedule" text="Configure the schedule">}}.

### Configure Data Collection

High frequency telemetry uses profiles for JSON file data collection. A profile is a set of configurations. Cumulus Linux provides a default profile called `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).

{{%notice note%}}
- You cannot delete or modify a profile if data collection jobs are already running or scheduled.
{{%/notice%}}

To configure data collection:
- Set the sampling interval in microseconds for the profile. You can specify a value between 100 and 12750. The value must be a multiple of 50. The default value is 5000 microseconds.
- Specify the type of data you want to collect for the profile. You can collect transmitted bytes, received bytes, and current traffic class buffer occupancy. The `standard` profile collects all three data types.
- Set the egress queue priorities (traffic class 0-15) for the profile if the data types you want to collect include current traffic class buffer occupancy. The `standard` profile setting is 3.

{{%notice note%}}
Use commas (no spaces) to separate the list of traffic classes. For example, to set traffic class 1, 3, and 6, specify `1,3,6`.
{{%/notice%}}

{{< tabs "TabID26 ">}}
{{< tab "NVUE Commands ">}}

The following example configures `profile1` and sets the sampling interval to 1000, the traffic class to 0, 3, and 7, and the type of data to collect to traffic class buffer occupancy (`tc-occupancy`):

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 sample-interval 1000
cumulus@switch:~$ nv set system telemetry hft profile profile1 counter tc-occupancy
cumulus@switch:~$ nv set system telemetry hft profile profile1 traffic-class 0,3,7 
cumulus@switch:~$ nv config apply
```

The following example configures `profile2` and sets the sampling interval to 1000, and the type of data to collect to received bytes (`rx-byte`) and transmitted bytes (`tx-byte`).

{{%notice note%}}
You must specify the `nv set system telemetry hft profile <profile-id> counter` command for each data type you want to collect.
{{%/notice%}}

```
cumulus@switch:~$ nv set system telemetry hft profile profile2 sample-interval 1000
cumulus@switch:~$ nv set system telemetry hft profile profile2 counter rx-byte
cumulus@switch:~$ nv set system telemetry hft profile profile2 counter tx-byte
cumulus@switch:~$ nv config apply
```

To delete a profile, run the `nv unset system telemetry hft profile <profile-id>` command.

{{< /tab >}}
{{< tab "Job Management Tool ">}}

The following example configures `profile1` and sets the sampling interval to 1000, the traffic class to 0, 3, and 7, and the type of data to collect to traffic class buffer occupancy (`tc_curr_occupancy`):

```
cumulus@switch:~$ cl-hft-tool profile-add --name profile1 --counter tc_curr_occupancy --tc 0,3,7 --interval 1000 
```

The following example configures `profile2`, and sets the sampling interval to 1000 and the type of data to collect to received bytes (`if_in_octets`) and transmitted bytes (`if_out_octets`):

```
cumulus@switch:~$ cl-hft-tool profile-add --name profile2 --counter if_in_octets,if_out_octets --interval 1000 
```

To delete a profile, run the `cl-hft-tool profile-delete --name <profile-id>` command:

```
cumulus@switch:~$ cl-hft-tool profile-delete --name profile1 
```

To delete all profiles, run the `cl-hft-tool profile-delete --name all` command.

{{< /tab >}}
{{< /tabs >}}

### Configure JSON Data Export

You can save the collected data locally to a `json` file in the `/var/run/cumulus/hft` directory, then export the `json` file to an external location with NVUE commands (or the API). The `json` format file includes the data for each sampling interval and a timestamp for the collected data.

{{%notice note%}}
- The collected data is available on the switch until you trigger the next data collection or until you reboot the switch.
- You must configure data export (the target) before you can configure a schedule.
{{%/notice%}}

{{< tabs "TabID56 ">}}
{{< tab "NVUE Commands ">}}

To save the collected data locally to a `json` file, run the `nv set system telemetry hft target local` command:

```
cumulus@switch:~$ nv set system telemetry hft target local
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Job Management Tool ">}}

The following example saves the collected data locally to a `json` file:

```
cumulus@switch:~$ cl-hft-tool target-add --target local
```

To delete a target, run the `cl-hft-tool target-delete --target local` command:

```
cumulus@switch:~$ cl-hft-tool target-delete --target local 
```

{{< /tab >}}
{{< /tabs >}}

To export a `json` file to an external location, run the NVUE `nv action upload system telemetry hft job <job-id> <remote-url>` command. Cumulus Linux supports <span class="a-tooltip">[FTP](## "File Transfer Protocol")</span>, <span class="a-tooltip">[SCP](## "Secure Copy Protocol")</span>, and <span class="a-tooltip">[SFTP](## "Secure File Transfer Protocol")</span>. You can see the list of jobs with the `nv show system telemetry hft job` command.

```
cumulus@switch:~$ nv action upload system telemetry hft job 1 scp://root@host1:/home/telemetry/
```

### Configure the Job Schedule

To configure the schedule for a JSON data collection profile, set:
- The start date and time. You can also start data collection immediately with the `now` option.
- The session duration in seconds. The default value is 20 seconds.
- The ports on which you want to collect the data. You can specify a range of ports, multiple comma separated ports, or `all` for all the ports. The default value is `all`.

{{%notice note%}}
- You can schedule a maximum of 25 sessions (jobs). These 25 jobs are active jobs whose states are either `running` (collecting counters now) or `pending` (scheduled to collect data in a future date and time). The switch can keep data for 10 jobs (in a `completed`, `cancelled`, or `failed` state) in addition to the 25 maximum active jobs.
- You must configure data export (the target) before you can configure the schedule.
- The switch ASIC can only run one high frequency telemetry job at a time; You cannot schedule two jobs to run at the same time.
- There might be a delay of two to three seconds between the scheduled time and the actual data sampling start time in the ASIC.

{{%/notice%}}

{{< tabs "TabID79 ">}}
{{< tab "NVUE Commands ">}}

The following example configures `profile1` to start on 2024-07-17 at 10:00:00, run for 30 seconds, and collect data on swp1s0 through swp9s0.

Specify the date and time in `YYYY-MM-DD HH:MM:SS` format.

``` 
cumulus@switch:~$ nv action schedule system telemetry hft job 2024–07-17 10:00:00 duration 30 profile profile1 ports swp1s0-swp9s0
Action executing ...
Job schedule successfull.
HFT job schedule successful: job-id 1

Action succeeded
```

You can provide a short reason why you are collecting the data. If the description contains more than one word, you must enclose the description in quotes. A description is optional.

```
cumulus@switch:~$ nv action schedule system telemetry hft job 2024-07-17 10:00:00 duration 30 profile profile1 ports swp1s0-swp9s0 description "bandwidth profiling"
Action executing ...
Job schedule successfull.
HFT job schedule successful: job-id 1

Action succeeded
```

You can specify `now` for the date and/or time to configure the current date and time of day. The following example configures `profile2` to start today at 10:00:00, run for 30 seconds, and collect data on swp2s0.

``` 
cumulus@switch:~$ nv action schedule system telemetry hft job now 10:00:00 duration 30 profile profile2 ports swp2s0
Action executing ...
Job schedule successfull.
HFT job schedule successful: job-id 2

Action succeeded
```


The following example configures `profile2` to start immediately, run for 30 seconds, and collect data on swp2s0.

``` 
cumulus@switch:~$ nv action schedule system telemetry hft job now now duration 30 profile profile2 ports swp2s0
Action executing ...
Job schedule successfull.
HFT job schedule successful: job-id 2

Action succeeded
```

{{< /tab >}}
{{< tab "Job Management Tool ">}}

The following example configures `profile1` to start on 2024-07-17 at 10:00:00, run for 30 seconds, and collect data on swp1s0 through swp9s0.

Specify the date and time in `YYYY-MM-DD-HH:MM:SS` format.

```
cumulus@switch:~$ cl-hft-tool job-schedule --time 2024–07-17-10:00:00 --duration 30 --profile profile1 --ports swp1s0-swp9s0  
```

You can provide a short reason why you are collecting the data. If the description contains more than one word, you must enclose the description in quotes. A description is optional.

```
cumulus@switch:~$ cl-hft-tool job-schedule --time 2024–07-17-10:00:00 --duration 30 --profile profile1 --ports swp1s0-swp9s0 --description "bandwidth profiling"
```

{{< /tab >}}
{{< /tabs >}}

### Cancel Data Collection

You can cancel a specific or all data collection jobs, or a specific or all jobs for a profile.

{{< tabs "TabID102 ">}}
{{< tab "NVUE Commands ">}}

To cancel a scheduled telemetry job, run the `nv action cancel system telemetry hft job <job-id> profile <profile-id>` command. Run the `nv show system telemetry hft job` command to see the list of job IDs.

The following example cancels all jobs for profile `profile1`:

```
cumulus@switch:~$ nv action cancel system telemetry hft job all profile profile1
Action executing ...
Action succeeded
```

The following example cancels job 6:

```
cumulus@switch:~$ nv action cancel system telemetry hft job 6
Action executing ...
Action succeeded
```

{{< /tab >}}
{{< tab "Job Management Tool ">}}

To cancel a scheduled telemetry job, run the `cl-hft-tool job-cancel --job <job-id>` command.

The following example cancels job 6:

```
cumulus@switch:~$ cl-hft-tool  job-cancel --job 6
```

{{< /tab >}}
{{< /tabs >}}

### Show Session Information

To show a summary of high frequency telemetry configuration and data:

```
cumulus@switch:~$ nv show system telemetry hft
profile
==========
    Profile        traffic-class  counter       sample-interval
    -------------  -------------  ------------  ---------------
    standard       3              rx-byte       5000
                                  tc-occupancy
                                  tx-byte
    user_profile1  0              rx-byte       1000
                   1              tc-occupancy
                   2              tx-byte

job
======
    Job  Counter                       duration  sample-interval  Start Time            Traffic Class  Status     Description
    ---  ----------------------------  --------  ---------------  --------------------  -------------  ---------  -----------
    1    tx-byte,rx-byte,tc-occupancy  20        5000             2024-07-30T05:34:23Z  3              completed  NA
    2    tx-byte,rx-byte,tc-occupancy  20        1000             2024-07-30T05:35:17Z  0-2            completed  NA
...
```

To show the high frequency telemetry profiles configured on the switch:

```
cumulus@switch:~$ nv show system telemetry hft profile
Profile        traffic-class  counter       sample-interval
-------------  -------------  ------------  ---------------
standard       3              rx-byte       5000
                              tc-occupancy
                              tx-byte
user_profile1  0              rx-byte       1000
               1              tc-occupancy
               2              tx-byte
```

To show the settings for a specific profile:

```
cumulus@switch:~$ nv show system telemetry hft profile profile1
                 operational  applied
---------------  -----------  -------
sample-interval  1000         1000   
[traffic-class]  0            0      
[traffic-class]  1            1      
[traffic-class]  2            2      
[traffic-class]  3            3      
[traffic-class]  4            4      
[traffic-class]  5            5      
[traffic-class]  6            6      
[traffic-class]  7            7      
[traffic-class]  8            8      
[traffic-class]  9            9      
[counter]        rx-byte      rx-byte
[counter]        tx-byte      tx-byte
```

To show configured targets:

```
cumulus@switch:~$ nv show system telemetry hft target
applied
-------
local  
```

To show information for all data collection jobs:

```
cumulus@switch:~$ nv show system telemetry hft job
Job  Counter                       duration  sample-interval  Start Time            Traffic Class  Status     Description
---  ----------------------------  --------  ---------------  --------------------  -------------  ---------  -----------
1    tx-byte,rx-byte,tc-occupancy  20        5000             2024-07-30T05:34:23Z  3              completed  NA
2    tx-byte,rx-byte,tc-occupancy  20        1000             2024-07-30T05:35:17Z  0-2            completed  NA
```

To show information about a specific data collection job:

```
cumulus@switch:~$ nv show system telemetry hft job 1
duration      : 20                sample_interval : 5000
status        : completed         start_time      : 2024-07-30T05:34:23Z
traffic_class : 3                 counter         : tx-byte,rx-byte,tc-occupancy
description   : NA
target        : /var/run/cumulus/hft
port          : swp9s0
```
