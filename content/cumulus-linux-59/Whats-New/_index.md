---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.9 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.9, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.9, see the {{<link title="Cumulus Linux 5.9 Release Notes" text="Cumulus Linux 5.9 Release Notes">}}.
- To upgrade to Cumulus Linux 5.9, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.9.0
<!-- vale on -->
Cumulus Linux 5.9.0 contains several new features and improvements, and provides bug fixes.

### New Features and Enhancements
- {{<link url="Precision-Time-Protocol-PTP" text="PTP">}} is now generally available on Spectrum-4 switches
- {{<link url="Precision-Time-Protocol-PTP/#clock-timestamp-mode" text="PTP one step clock timestamp mode">}} is now generally available on Spectrum-4 switches
- {{<link url="Precision-Time-Protocol-PTP/#noise-transfer-servo" text="PTP Noise Transfer Servo">}}
- {{<link url="Precision-Time-Protocol-PTP/#ptp-version" text="Force PTP version">}}
- Improved SyncE and PPS noise transfer algorithm on the NVIDIA SN3750-SX switch
- {{<link url="Synchronous-Ethernet-SyncE" text="SyncE">}} support at 1G speed (optical)
- {{<link url="Synchronous-Ethernet-SyncE" text="SyncE">}} Clock Identity set according to ITU-T G.8264
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Warmboot support for VXLAN EVPN">}} available for Beta (without support for EVPN MLAG or EVPN multihoming)
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Warmboot support for 802.1X">}}
- {{<link url="802.1X-Interfaces/#host-modes" text="802.1X multi host mode">}}
- NVUE command to {{<link url="VLAN-aware-Bridge-Mode/#keep-svis-perpetually-up" text="keep SVIs always UP">}}
- {{<link url="Installing-a-New-Cumulus-Linux-Image/#install-using-a-local-file" text="Stage an NVUE startup.yaml file during binary image installation">}} from Cumulus Linux
- Improved {{<link url="Understanding-the-cl-support-Output-File" text="cl-support script ">}} to prevent switch disruption
- Minimized data retrieval for the NVUE `nv show router nexthop rib` and `nv show vrf <vrf> router rib ipv4 route` commands
- {{< expand "Improved tab completion for NVUE routing commands" >}}
  ```
  nv show vrf <vrf> router bgp nexthop ipv4 ip-address
  nv show vrf <vrf> router bgp address-family l2vpn-evpn loc-rib rd <rd> route-type <type> route
  nv show evpn vni <vni>
  nv show evpn access-vlan-info vlan
  nv show evpn vni <vni> multihoming bgp-info esi
  nv show vrf <vrf> router rib ipv4 route
  nv show vrf <vrf> router rib ipv6 route
  nv show vrf <vrf> router rib ipv4 route <route> protocol connected entry-index
  nv show vrf <vrf> router bgp address-family l2vpn-evpn loc-rib rd <rd> route-type macip route
  nv show vrf <vrf> router bgp address-family l2vpn-evpn loc-rib rd <rd> route-type prefix route <route> path
  nv show vrf <vrf> router bgp neighbor <neighbor> address-family ipv4-unicast advertised-routes <routes> path
  ```
  {{< /expand >}}
- {{< expand "New NVUE Commands" >}}
  For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
  
  {{< tabs "TabID49 ">}}
  {{< tab "nv show ">}}
  
  ```
  nv show bridge domain <bridge> svi-force-up
  nv show system global svi-force-up
  nv show service ptp <instance-id> force-version
  ```

  {{< /tab >}}
  {{< tab "nv set ">}}

  ```
  nv set interface <interface> dot1x host-mode
  nv set bridge domain <bridge> svi-force-up enable
  nv set system global svi-force-up enable
  nv set service ptp <instance-id> force-version
  ```
  
  {{< /tab >}}
  {{< tab "nv unset ">}}
  
  ```
  nv unset interface <interface> dot1x host-mode
  nv unset bridge domain <bridge> svi-force-up enable
  nv unset system global svi-force-up enable
  nv unset service ptp <instance-id> force-version
  ```

  {{< /tab >}}
  {{< tab "nv action ">}}
  
  ```
  nv action deauthenticate interface <interface-id> dot1x authorized-sessions <mac-address> [silent]
  ```

  {{< /tab >}}
  {{< /tabs >}}
  
  {{< /expand >}}

{{%notice note%}}
The repository key stored in Cumulus Linux 5.5.0 and earlier has expired. Before performing a package upgrade to Cumulus Linux 5.9.0 from Cumulus Linux 5.5.0 and earlier, you must install the new key. See [this knowledge base article]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys" >}}).
{{%/notice%}}

{{%notice info%}}
Cumulus Linux 5.9 includes the NVUE object model. After you upgrade to Cumulus Linux 5.9, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
