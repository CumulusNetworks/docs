---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.8 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.8, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.8, see the {{<link title="Cumulus Linux 5.8 Release Notes" text="Cumulus Linux 5.8 Release Notes">}}.
- To upgrade to Cumulus Linux 5.8, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.8.0
<!-- vale on -->
Cumulus Linux 5.8.0 contains several new features and improvements, and provides bug fixes.

### New Features and Enhancements

- {{<link url="Precision-Time-Protocol-PTP" text="PTP">}} now generally available on Spectrum-4 switches
- {{<link url="Synchronous-Ethernet-SyncE" text="SyncE">}} support at 1G speed (copper and optical)
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Warmboot support for VXLAN EVPN">}} (no EVPN MLAG or EVPN multihoming support)
- ISSU warm boot with 802.1X
- {{<link url="Port-Security" text="Port security with 802.1x">}}
- {{<link url="Synchronous-Ethernet-SyncE" text="SyncE">}} Clock Identity set according to ITU-T G.8264
- NVUE command to {{<link url="VLAN-aware-Bridge-Mode/#keep-the-svi-perpetually-up" text="configure a dummy interface">}} to keep SVIs always UP
- {{<link url="FRRouting/#vtysh-modal-cli" text="FRR tab completion">}} with static representation
- Interface summary view with filtering
- Admin state added to NVUE `nv show interface` commands

{{< expand "Changed Commands" >}}

{{< tabs "TabID66 ">}}
{{< tab "nv show ">}}

| Previous Command  |  New Command  |
| ------------ | ------------- |
| | |

{{< /tab >}}
{{< tab "nv set ">}}

| Previous Commands  |  New Commands  |
| ------------ | ------------- |
|  | |

{{< /tab >}}
{{< tab "nv action ">}}

| Previous Command  |  New Command  |
| ------------ | ------------- |
| |  |

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{< expand "New NVUE Commands" >}}

For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

{{< tabs "TabID40 ">}}
{{< tab "nv show ">}}

```

```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set system global svi-force-up enabled
nv set interface <interface-name> link state forced-up
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset system global svi-force-up enabled
nv unset interface <interface-name> link state forced-up
```

{{< /tab >}}
{{< tab "nv action ">}}

```

```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.8 includes the NVUE object model. After you upgrade to Cumulus Linux 5.8, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
