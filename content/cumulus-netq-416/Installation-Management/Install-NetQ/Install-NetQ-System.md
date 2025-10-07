---
title: Install the NetQ System
author: NVIDIA
weight: 200
toc: 3
---
You can install NetQ either on your premises or as a remote, cloud solution. If you are unsure which option is best for your network, refer to {{<link title="Before You Install" text="Before You Install">}}.


## Ethernet Deployments

{{<tabs "TabID11" >}}

{{<tab "On-premises" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| Single server | KVM or VMware | {{<link title="Set Up Your Virtual Machine for a Single On-premises Server" text="Start install">}} |
| High-availability cluster | KVM or VMware | {{<link title="Set Up Your Virtual Machine for an On-premises HA Server Cluster" text="Start install">}} |
| High-availability scale cluster | KVM or VMware | {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster" text="Start install">}} |

{{</tab>}}

{{<tab "Cloud (OPTA)" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| Single server | KVM or VMware | {{<link title="Set Up Your Virtual Machine for a Single Cloud Server" text="Start install">}} |

{{</tab>}}

{{</tabs>}}

## NVLink Deployments

{{<tabs "TabID35" >}}

{{<tab "On-premises" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| High-availability scale cluster | KVM or VMware | {{<link title="Install NetQ NVLink" text="Start install">}} |

{{</tab>}}

{{</tabs>}}


## Combined Ethernet and NVLink Deployments

{{<tabs "TabID56" >}}

{{<tab "On-premises" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| High-availability scale cluster | KVM or VMware | {{<link title="Install NetQ NVLink" text="Start install">}} |

{{</tab>}}

{{</tabs>}}

## Base Command Manager

You can also deploy NetQ using NVIDIA Base Command Manager. To get started, refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}}.

## Related Information

- {{<link title="Troubleshoot NetQ/#troubleshoot-netq-installation-and-upgrade-issues" text="Troubleshoot NetQ Installation and Upgrade Issues">}}