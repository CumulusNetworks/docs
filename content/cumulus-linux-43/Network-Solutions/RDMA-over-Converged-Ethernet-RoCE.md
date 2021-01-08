---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 1340
toc: 3
---
*RDMA over Converged Ethernet* ({{<exlink url="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet" text="RoCE">}}) enables you to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on congestion control and lossless Ethernet to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments.

{{%notice note%}}

While Cumulus Linux can support RoCE environments, the hosts send and receive the RoCE packets.

{{%/notice%}}

RoCE helps you obtain a *converged network*, where all services run over the Ethernet infrastructure, including Infiniband apps.

There are two versions of RoCE, which run at separate layers of the stack:

- RoCEv1 runs at the link layer and cannot be run over a routed network. Therefore, it requires Priority Flow Control (PFC).
- RoCEv2 runs over layer 3. Because it is a routed solution, congestion-notification (ECN) bits are communicated end-to-end across a routed network.

## Enable RDMA over Converged Ethernet lossless (with PFC and ECN)

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB global route header rides directly on top of the Ethernet header. The lossless Ethernet layer handles congestion hop by hop.

On switches with {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/?asic%5B0%5D=Mellanox%20Spectrum&asic%5B1%5D=Mellanox%20Spectrum_A1" text="Spectrum ASICs">}}, use NCLU to configure RoCE with PFC:

```
cumulus@switch:~$ net add roce lossless
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

{{<link url="Buffer-and-Queue-Management#link-pause" text="Link pause">}} is another way to provide lossless ethernet, however,PFC is the preferred method. PFC allows more granular control by pausing the traffic flow for a given CoS group instead of the entire link.

{{%/notice%}}

## Enable RDMA over Converged Ethernet lossy (with ECN)

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the Infiniband (IB) Transport Protocol over UDP. The IB transport protocol includes an end-to-end reliable delivery mechanism and has its own sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion experienced to the receiver. The receiver generates an RoCEv2 congestion notification packet directed to the source of the packet.

On switches with {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/?asic%5B0%5D=Mellanox%20Spectrum&asic%5B1%5D=Mellanox%20Spectrum_A1" text="Spectrum ASICs">}}, use NCLU to configure RoCE with ECN:

```
cumulus@switch:~$ net add roce lossy
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

## Considerations

- Do not run any other NCLU commands with RoCE commands when you commit the configuration with `net commit`.
- Make sure there is no pending configuration when you commit the RoCE configuration.
- The `net add interface <interface> storage-optimized` and `net add interface <interface> storage-optimized pfc` commands configure RoCE with PFC and RoCE with ECN on a specific interface. These commands will be deprecated in a future release. If you configured RoCE on a specific interface in an earlier Cumulus Linux release, you need to migrate to the new RoCE commands (`net add roce lossy` and `net add roce lossless`).
   {{< expand "Recommended Workflow for Port Breakout Configuration" >}}

1. Delete the RoCE configuration:

   ```
   cumulus@switch:~$ net del roce
   cumulus@switch:~$ net commit
   ```

2. Apply the breakout configuration with NCLU commands:

   ```
   cumulus@switch:~$ net add interface swp5 breakout <breakout configuration>
   cumulus@switch:~$ net commit
   ```

3. Enable RoCE again:

   ```
   cumulus@switch:~$ net add roce lossless|lossy
   cumulus@switch:~$ net commit
   ```
{{< /expand >}}

   If you prefer *not* to migrate to the new RoCE commands, you can run `net add storage-optimized correct-legacy-qos-config` to correct storage-optimized issues. Be aware that this command does not perform any migration; it only enables you to correct legacy configurations.

## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
- {{<exlink url="https://community.mellanox.com/s/article/understanding-rocev2-congestion-management" text="RoCEv2 congestion management">}} - community.mellanox.com
- {{<exlink url="https://community.mellanox.com/s/article/lossless-roce-configuration-for-spectrum-based-cumulus-switches-in-dscp-based-qos-mode" text="Configuring RoCE over a DSCP-based lossless network">}} on a switch with a Mellanox Spectrum ASIC
