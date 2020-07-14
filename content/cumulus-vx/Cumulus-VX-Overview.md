---
title: Cumulus VX Overview
author: Cumulus Networks
weight: 5
product: Cumulus VX
version: '3.7'
---
Cumulus VX runs in a virtual machine (VM) on a standard x86 environment. The VM is a 64-bit operating system, built on the same foundation as {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux" text="Cumulus Linux">}}, and runs Debian Linux with `virtio` drivers for network and HDD interfaces as well as the logical volume manager (LVM).

## Supported Platforms

Cumulus VX is supported on:

- VirtualBox
- VMware Fusion, Worksation, and vSphere ESXi
- KVM
- Vagrant and VirtualBox
- Vagrant and KVM
- GNS3 and VirtualBox

{{%notice note%}}

Cumulus VX is supported on VMware Fusion, Workstation, and vSphere ESXi. This document provides setup instructions for VMware vSphere ESXi.

{{%/notice%}}

## Tested Versions

- KVM: tested on a server running Debian 3.2.60-1+deb7u3 x86\_64 GNU/Linux with 3.2.0-4-amd64 \#1 SMP processors.

## Cumulus VX Compared with Other Cumulus Networks Products

Cumulus VX is not a production-ready virtual switch or router. It has the same foundation as Cumulus Linux, including all the control plane elements, but without an actual ASIC or NPU for line rate performance or hardware acceleration.

You can use tools like `jdoo` to monitor the virtual switch. The same automation, zero touch provisioning, security, and QoS tools are available.

The following table outlines the similarities and differences between Cumulus VX and other Cumulus Networks operating systems:

| Feature or Functionality | Cumulus VX |
| ------------------------ | -------------------------------- |
| Installation and Upgrade | New images available with every GA release. |
| Hardware acceleration    | Datapath forwarding is dependent on the choice of hypervisor and VM resources. |
| Hardware management      | None |
| Hardware limitations     | None. Dependent on hypervisor and VM resources. Certain features such as route-table-size might accommodate more routes than are supported in hardware (32K routes), given available memory. |
| Production-ready         | No |
| Linux extensibility      | Yes |
| Layer 2 features         | Yes; hypervisor/topology manager dependent. |
| Layer 3 features         | Yes |
| Network virtualization   | Yes (software forwarding) |
| OS management (ZTP, ifupdown2, third party packages) | Yes |
| Automation, monitoring, troubleshooting | Yes |
| Security                 | Yes |
| QoS                      | Yes |

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
- {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/" text="Cumulus Networks knowledge base">}}
- {{<exlink url="https://www.vmware.com/support/pubs/" text="VMware documentation">}}
- {{<exlink url="https://www.virtualbox.org/wiki/Documentation" text="VirtualBox documentation">}}
- {{<exlink url="http://www.linux-kvm.org/page/Documents" text="KVM documentation">}}
- {{<exlink url="https://docs.vagrantup.com/v2/" text="Vagrant documentation">}}
- {{<exlink url="(http://docs.gns3.com/appliances/cumulus-vx.html" text="GNS3 documentation">}}
