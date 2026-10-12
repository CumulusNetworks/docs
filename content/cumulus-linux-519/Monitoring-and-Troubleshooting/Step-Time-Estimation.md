---
title: Step Time Estimation
author: NVIDIA
weight: 1230
toc: 2
---
Step time estimation reports the step time of an AI training workload running across the fabric, so that you can track workload progress and spot infrastructure problems without access to the servers running the workload. The switch looks for periodicity in the traffic patterns on the monitored interfaces and derives one estimate for each interface. Only the estimates leave the switch; the switch does not export the data used to derive the estimates.

Cumulus Linux exports the estimate as the `nvswitch_interface_step_time_estimate` OTLP gauge, in seconds, carrying an `interface` label, and as the gNMI path `/interfaces/interface[name=<interface-id>]/step-time-estimation/state/step-time-estimate`. A gNMI subscription to this path does not enable step time estimation and the subscription interval does not change how often the switch produces an estimate; the interval controls only how often gNMI exports the current value. The switch produces a new estimate only once per batch interval; the gNMI notification for this path carries the timestamp of when the switch produced that estimate, not the timestamp of the notification itself.

{{%notice note%}}
- You cannot run step time estimation at the same time as continuous streaming HFT export. 
- You cannot run step time estimation at the same time as a {{<link url="High-Frequency-Telemetry/#collect-hft-in-json-file" text="JSON file data collection job">}}; the switch does not support using the `cl-hft-tool` job management tool while step time estimation is running.
- You can configure step time estimation and a fixed duration streaming HFT export session at the same time, but the HFT session takes priority. The switch exports no step time estimates while that session runs.
- Step time estimation is supported only on interfaces with four lanes or less.
- You must enable step time estimation on at least one interface before you enable step time estimation export.
- You cannot change `batch-interval` while step time estimation is enabled. Disable step time estimation export, change the value, then reenable export.
- When the algorithm produces no estimate for an interface, the switch exports no data point for that interface. When it produces no estimate for any interface, the switch exports no metric at all.
{{%/notice%}}

To configure step time estimation:

1. Add your collector as a gRPC OTEL export destination, as described in {{<link url="High-Frequency-Telemetry/#streaming-hft-export" text="Streaming HFT Export">}}.

2. Enable step time estimation on the interfaces you want to monitor. In a fabric, these interfaces are typically the leaf downlinks facing the servers running the workload:

   ```
   cumulus@switch:~$ nv set interface swp1s0-3,swp2s0-3 telemetry step-time-estimation state enabled
   cumulus@switch:~$ nv config apply
   ```

3. Configure the batch interval, in seconds. This is the interval between successive runs of the algorithm, and therefore the interval between successive exports of the metric. You can set a value between 300 and 3600. The default value is 300 seconds.

   ```
   cumulus@switch:~$ nv set system telemetry step-time-estimation batch-interval 600
   cumulus@switch:~$ nv config apply
   ```

4. Enable step time estimation export:

   ```
   cumulus@switch:~$ nv set system telemetry step-time-estimation export state enabled
   cumulus@switch:~$ nv config apply
   ```

   To export step time estimates to a single destination when you export OTEL data to more than one collector, enable export in a statistics group instead of globally:

   ```
   cumulus@switch:~$ nv set system telemetry stats-group ONLY-STEP-TIME step-time-estimation export state enabled
   cumulus@switch:~$ nv set system telemetry export otlp grpc destination 10.1.1.100 stats-group ONLY-STEP-TIME
   cumulus@switch:~$ nv config apply
   ```

To correlate an estimate with the server behind the interface, configure {{<link url="Open-Telemetry-Export/#static-labels" text="static labels">}} for the switch and its interfaces. The collector then receives the label descriptions alongside the estimate.

To stop exporting step time estimates, run the `nv unset system telemetry step-time-estimation export state` command. To stop monitoring an interface, run the `nv unset interface <interface-id> telemetry step-time-estimation state` command.

To show step time estimation status and configured parameters, run the `nv show system telemetry step-time-estimation` command.
