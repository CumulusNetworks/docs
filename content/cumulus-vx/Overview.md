---
title: Overview
author: Cumulus Networks
weight: 5
product: Cumulus VX
product: Cumulus VX
version: '4.x'
---
This section provides an overview of Cumulus VX and lists supported hypervisors.

## Cumulus VX

Cumulus VX is a virtual appliance that helps you become familiar with Cumulus Networks technology, and provides a platform for you to prototype network operations and develop custom applications before you deploy into a production environment. Without the need for a bare metal switch or specialized hardware, Cumulus VX runs on all popular hypervisors, making traditional networking protocols such as BGP and MLAG, Cumulus Networks-specific technologies such as ONIE, and Prescriptive Topology Manager (PTM) available for testing and configuration.

Cumulus VX is a virtual machine (VM) on a standard x86 environment. The VM is the same Cumulus Linux operating system supported on NVIDIA ethernet switches and contains the same software features but in a VM format. Cumulus VX provides full data plane functionality through the Linux kernel, as well as layer 2 VLAN, VXLAN bridging, and VXLAN routing capabilities.

{{%notice note%}}

Cumulus VX is designed for testing and not data plane performance. Cumulus VX is not intended to act as a cloud virtual router. No testing or integration has been done with software packet acceleration integrations like SR-IOV or DPDK.

{{%/notice%}}

{{< img src="/images/cumulus-vx/cumulus-vx.png" width="800" >}}

## Cumulus in the Cloud

As an alternative to Cumulus VX, which requires a hypervisor (or hypervisor and orchestrator), you can use
{{<exlink url="https://cumulusnetworks.com/products/cumulus-in-the-cloud/" text="Cumulus in the Cloud">}}, which is a free, personal, virtual data center network that provides a low-effort way to see Cumulus Networks technology in action. Your virtual data center consists of two racks with two dual-homed servers connected with a leaf-spine network. This is a good way to try out Cumulus Linux if you have platform or disk limitations.

## Supported Hypervisors

Cumulus VX is supported with:

- KVM-QEMU
- KVM-QEMU and Vagrant
- VirtualBox
- VirtualBox and GNS3
- VirtualBox and Vagrant
- VMware Fusion, Worksation, and vSphere ESXi

{{%notice note%}}

Cumulus VX is supported with VMware Fusion, Workstation, and vSphere ESXi; however, this document provides setup instructions for VMware vSphere ESXi only.

{{%/notice%}}

## Cumulus VX Compared with Cumulus Linux

The VM is the same Cumulus Linux operating system supported on NVIDIA ethernet switches and contains all the same software features but in a VM format. Cumulus VX provides full data plane functionality through the Linux kernel, as well as layer 2 VLANs and both VXLAN bridging and VXLAN routing capabilities. Due to hardware limitations, certain functionality is supported in Cumulus VX but not on ethernet switches. Due to hardware specific implementations, certain features are not supported in Cumulus VX.

Cumulus VX supports all software functions like BGP, spanning-tree, and SNMP, as well as any automation tooling and third-party packages.

| Cumulus VX | Cumulus Linux |
| -----------| ------------- |
| {{< img src="/images/cumulus-vx/cumulus-vx.png" width="450" >}}| {{< img src="/images/cumulus-vx/cumulus-linux.png" width="450" >}}|

The following table outlines the similarities and differences between Cumulus VX and Cumulus Linux:

| <div style="width:300px">Feature or Functionality | Cumulus Linux | Cumulus Vx |
| ------------------------ | -------------------------------- | -------------------------------- |
| Upgrade available using an ONIE binary or with APT | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Line rate packet forwarding  | <font color="green">Yes</font> via switch ASIC | <font color="red">No</font> |
| Software license install | <font color="green">Yes</font> | <font color="red">No</font> |
| Temperature and sensor 0utputs   | <font color="green">Yes</font> | <font color="red">No</font> |
| ACL and routing entry limits   | Limited depending on switch ASIC | Only limited by VM memory |
| Designed and tested for production | <font color="green">Yes</font> | <font color="red">No</font> |
| Layer 2 VLANs         | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Layer 2 bridging         | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Spanning tree         | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Layer 3 routing       | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Routing protocols (BGP, OSPF) | <font color="green">Yes</font> | <font color="green">Yes</font> |
| VXLAN   | <font color="green">Yes</font> | <font color="green">Yes</font> |
| ECMP | <font color="green">Yes</font>, based on hardware hashing | <font color="green">Yes</font>, based on Linux kernel hashing |
| Packet marking and remarking | <font color="green">Yes</font> | <font color="red">No</font><sup>1</sup> |
| QoS Buffer management | <font color="green">Yes</font> | <font color="red">No</font> |
| QoS Buffer monitoring | <font color="green">Yes</font> | <font color="red">No</font> |
| QoS Shaping | <font color="green">Yes</font> | <font color="red">No</font> |
| What Just Happened | <font color="green">Yes</font> | <font color="red">No</font> |
| ACLs | <font color="green">Yes</font> | <font color="red">No</font><sup>2</sup> | 
| 802.1x | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Cumulus NetQ | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Zero Touch Provisioning | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Third party Linux packages | <font color="green">Yes</font> | <font color="green">Yes</font> |
| DHCP and DHCP relay | <font color="green">Yes</font> | <font color="green">Yes</font> |
| LLDP | <font color="green">Yes</font> | <font color="green">Yes</font> |
| LAG and MLAG | <font color="green">Yes</font> | <font color="green">Yes</font> |
| Multicast, IGMP and PIM | <font color="green">Yes</font> | <font color="green">Yes</font> |
| BFD | <font color="green">Yes</font> | <font color="green">Yes</font> |
| VRFs, Management VRF | <font color="green">Yes</font> | <font color="green">Yes</font> |
| NAT | <font color="green">Yes</font> | <font color="red">No</font><sup>3</sup> |

<sub>1. Marking and remarking is supported in Cumulus VX using kernel and Traffic Control (TC) commands, but these are not supported the same way in Cumulus Linux.</sub>  
<sub>2. ACLs are supported in Cumulus VX using iptables, but the `cl-acltool` command is not supported.</sub>  
<sub>3. NAT is supported in Cumulus VX using iptables but not with `cl-acltool`. Using NAT within Cumulus VX is not the same as Cumulus Linux.</sub>  

## Support Policy

As a Cumulus Linux customer, you can receive formal GSS support for Cumulus VX instances to:

- Test and stage network topologies before deploying to production.
- Analyze, troubleshoot, and correct issues with configurations and software bugs in Cumulus VX that might also apply to Cumulus Linux running on physical devices.
- Analyze, troubleshoot, and correct issues with Cumulus VX if behaving differently than physical devices. This does not apply in scenarios where it is not possible to emulate physical hardware with virtualization.

Cumulus Networks does *not* provide support for:

- Cumulus VX instances used in a production environment.
- Virtualization environments, including installation, setup, and configuration.
- Automation tool playbooks, including creation and troubleshooting.
- Performance or scalability issues related to network traffic running through Cumulus VX instances.

For non-customers, Cumulus VX remains a community-supported product, with no formal support obligations from Cumulus Networks. You can submit questions to the {{<exlink url="https://slack.cumulusnetworks.com/" text="community Slack channel">}} to engage with the wider community.

## Related Information

- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux" text="Cumulus Linux documentation">}}
- {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus VX downloads">}}
- {{<exlink url="https://www.vmware.com/support/pubs/" text="VMware documentation">}}
- {{<exlink url="https://www.virtualbox.org/wiki/Documentation" text="VirtualBox documentation">}}
- {{<exlink url="http://www.linux-kvm.org/page/Documents" text="KVM documentation">}}
- {{<exlink url="https://docs.vagrantup.com/v2/" text="Vagrant documentation">}}
- {{<exlink url="https://www.gns3.com/software" text="GNS3 documentation">}}
