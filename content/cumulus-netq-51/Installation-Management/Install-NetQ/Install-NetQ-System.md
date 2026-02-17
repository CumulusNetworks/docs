---
title: Install the NetQ System
author: NVIDIA
weight: 200
toc: 3
---

## NetQ for Ethernet

The following deployment models use NetQ to monitor Ethernet-only networks.

{{<tabs "TabID11" >}}

{{<tab "On-premises" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| Single server | KVM or VMware | {{<link title="Set Up Your Virtual Machine for a Single On-premises Server" text="Start install">}} |
| High-availability cluster | KVM or VMware | {{<link title="Set Up Your Virtual Machine for an On-premises HA Server Cluster" text="Start install">}} |
| High-availability scale cluster | KVM or VMware | {{<link title="Set Up Your Virtual Machine for an On-premises HA Scale Cluster" text="Start install">}} |

{{</tab>}}

{{</tabs>}}

## NetQ for NVLink

The following deployment model uses NetQ to monitor NVLink-only networks.

{{<tabs "TabID35" >}}

{{<tab "On-premises" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| High-availability scale cluster | KVM or VMware | {{<link title="Install NetQ NVLink" text="Start install">}} |

{{</tab>}}

{{</tabs>}}


## NetQ for Ethernet and NVLink

The following deployment models use NetQ to monitor networks that use both Ethernet and NVLink.

{{<tabs "TabID56" >}}

{{<tab "On-premises" >}}

| Server Arrangement | Hypervisor | Requirements & Installation |
| :--- | --- | :---: |
| High-availability scale cluster: three nodes | KVM or VMware | {{<link title="Install NetQ for Ethernet and NVLink" text="Start install">}} |
| High-availability scale cluster: user-defined nodes* | KVM or VMware | {{<link title="Install NetQ for Ethernet and NVLink (Beta)" text="Start install">}} |
{{</tab>}}

{{</tabs>}}

*This deployment option is in beta. Deployments with more than three nodes will require a fresh installation upon subsequent NetQ releases.

## Base Command Manager

You can also deploy NetQ using NVIDIA Base Command Manager. To get started, refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}}.

## Related Information

- {{<link title="Before You Install" text="NetQ Deployments Overview">}}
- {{<link title="Troubleshoot NetQ/#troubleshoot-netq-installation-and-upgrade-issues" text="Troubleshoot NetQ Installation and Upgrade Issues">}}