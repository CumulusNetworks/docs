---
title: NVUE Flexible Snippets
author: NVIDIA
weight: 121
toc: 3
---
Use NVUE flexible snippets if you configure Cumulus Linux with NVUE commands, then want to configure a feature that does not yet support the NVUE Object Model. You create a snippet in `yaml` format and add the configuration to either the `/etc/frr/frr.conf` or `/etc/network/interfaces` file.
<!-- vale off -->
## /etc/frr/frr.conf Snippets
<!-- vale on -->
NVUE does not support configuring BGP to peer across the default route. The following example configures BGP to peer across the default route from the default VRF:

1. Create a `.yaml` file with the following snippet:

   ```
   cumulus@switch:~$ sudo nano ./bgp_snippet.yaml
   - set:
       system:
         config:
           snippet:
             frr.conf: |
               ip nht resolve-via-default
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch ./bgp_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/frr/frr.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/frr/frr.conf
   ...
   ! end of router ospf block
   !---- CUE snippets ----
   ip nht resolve-via-default
   ```

## /etc/network/interfaces Snippets

### Configure MLAG Timers

NVUE supports configuring only one of the {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#set-clagctl-timers" text="MLAG service timeouts">}} (initDelay). The following example configures the MLAG peer timeout to 400 seconds:

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano ./mlag_snippet.yaml
   - set:
       system:
         config:
           snippet:
             ifupdown2_eni:
               peerlink.4094: |
                 clagd-args --peerTimeout 400
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch ./mlag_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists in the peerlink.4094 stanza of the `/etc/network/interfaces` file:

   ```
   cumulus@switch:~$ sudo cat /etc/network/interfaces
   ...
   auto peerlink.4094
   iface peerlink.4094
    clagd-args --peerTimeout 400
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
   ...
   ```

### Configure a Traditional Bridge

NVUE does not support configuring traditional bridges. The following example configures a traditional bridge called `br0` with the IP address 11.0.0.10/24. swp1, swp2 are members of the bridge.

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano ./bridge_snippet.yaml
   - set:
       system:
        config:
          snippet:
            ifupdown2_eni:
              eni_stanzas: |
                auto br0
                iface br0
                  address 11.0.0.10/24
                  bridge-ports swp1 swp2
                  bridge-vlan-aware no
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch ./bridge_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/network/interfaces` file:

   ```
   cumulus@switch:~$ sudo cat /etc/network/interfaces
   ...
   auto br0
   iface br0
     address 11.0.0.10/24
     bridge-ports swp1 swp2
     bridge-vlan-aware no
   ```
