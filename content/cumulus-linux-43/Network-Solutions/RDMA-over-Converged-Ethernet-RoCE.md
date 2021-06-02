---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 1340
toc: 3
---
RDMA over Converged Ethernet ({{<exlink url="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet" text="RoCE">}}) enables you to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on congestion control and lossless Ethernet to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments.

{{%notice note%}}

While Cumulus Linux can support RoCE environments, the hosts send and receive the RoCE packets.

{{%/notice%}}

RoCE helps you obtain a *converged network*, where all services run over the Ethernet infrastructure, including Infiniband apps.

There are two versions of RoCE, which run at separate layers of the stack:

- RoCEv1 runs at the link layer and allows communication between any two hosts in the same Ethernet broadcast domain.
- RoCEv2 is an internet layer protocol and runs over layer 3.

## Enable RDMA over Converged Ethernet lossless (with PFC and ECN)

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB global route header rides directly on top of the Ethernet header. The lossless Ethernet layer handles congestion hop by hop.

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, use NCLU to configure RoCE with PFC and ECN:

```
cumulus@switch:~$ net add roce lossless
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

- {{<link url="Buffer-and-Queue-Management#link-pause" text="Link pause">}} is another way to provide lossless ethernet; however, PFC is the preferred method. PFC allows more granular control by pausing the traffic flow for a given CoS group instead of the entire link.
- RoCEv1 depends on 802.1p fields for traffic classification; therefore it is not supported with access ports. Use trunk ports with RoCEv1.

{{%/notice%}}

## Enable RDMA over Converged Ethernet lossy (with ECN)

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the Infiniband (IB) Transport Protocol over UDP. The IB transport protocol includes an end-to-end reliable delivery mechanism and has its own sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion experienced to the receiver. The receiver generates an RoCEv2 congestion notification packet directed to the source of the packet.

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, use NCLU to configure RoCE with ECN:

```
cumulus@switch:~$ net add roce lossy
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

## Considerations

### RoCE Command and net commit

- Do not include any other NCLU commands with `net add roce lossless` or `net add roce lossy` when you commit the configuration with `net commit`.
- Make sure there is no pending configuration when you commit the RoCE configuration.

### net add interface <interface> storage-optimized Command

The `net add interface <interface> storage-optimized` and `net add interface <interface> storage-optimized pfc` commands configure RoCE on a specific interface. These commands will be deprecated in a future release. If you configured RoCE on a specific interface in an earlier Cumulus Linux release, you need to migrate to the new RoCE commands (`net add roce lossy` and `net add roce lossless`).

Follow this recommended procedure for port breakout configuration:

1. Delete the RoCE configuration with the `net del roce` command:

   ```
   cumulus@switch:~$ net del roce
   cumulus@switch:~$ net commit
   ```

2. Apply the breakout configuration with the `net add interface <interface> breakout <configuration>` command. For example:

   ```
   cumulus@switch:~$ net add interface swp5 breakout 4x
   cumulus@switch:~$ net commit
   ```

3. Enable RoCE with the `net add roce lossless` or `net add roce lossy` command. For example:

   ```
   cumulus@switch:~$ net add roce lossless
   cumulus@switch:~$ net commit
   ```

If you prefer *not* to migrate to the new RoCE commands, you can run `net add storage-optimized correct-legacy-qos-config` to correct storage-optimized issues. This command does *not* perform any migration; it only enables you to correct legacy configurations.

## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
- {{<exlink url="https://community.mellanox.com/s/article/understanding-rocev2-congestion-management" text="RoCEv2 congestion management">}} - community.mellanox.com
- {{<exlink url="https://community.mellanox.com/s/article/lossless-roce-configuration-for-spectrum-based-cumulus-switches-in-dscp-based-qos-mode" text="Configuring RoCE over a DSCP-based lossless network">}} on a switch with a Mellanox Spectrum ASIC
