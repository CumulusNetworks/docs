---
title: NVLink Quick Start Guide
author: NVIDIA
weight: 1000
toc: 3

---

## System Requirements and Installation

Follow the installation instructions for the NetQ on-premises deployment with a server cluster arrangement. This arrangement requires 3 worker nodes. Each node requires the following:

{{<netq-install/vm-reqs deployment="onprem" hypervisor="kvm" version="4.2.0">}}

After ensuring you have the minimum system resource requirements, follow the installation instructions for either a {{<link title="Set Up Your KVM Virtual Machine for an On-premises Server Cluster" text="KVM hypervisor">}} or {{<link title="Set Up Your VMware Virtual Machine for an On-premises Server Cluster" text="VMware hypervisor">}}.

After you complete the installation, log in to NetQ as described in the next section.

## Log in to NetQ

1. Open a new Chrome or Firefox browser window or tab.
2. Enter the following URL into the address bar: *https://\<hostname-or-ipaddress\>:443*  

 {{<figure src="/images/netq/splashscreen-480.png" alt="NetQ login screen" width="700">}}

3. Log in. 

    The default username and password for UI access is *admin, admin*

After creating a new password and accepting the Terms of Use, the default workbench opens with your username displayed in the upper-right corner.

## Access NVLink4

NVLink4 features are hidden by default in the NetQ UI. To access these features, run `netq features nvl4 enable` on your NetQ server's CLI. Return to the UI and refresh the page. The NVL4 icon should be visible in the header. Select this icon to display the NVLink management dashboard.

{{<figure src="/images/netq/nvl4-header-480.png" alt="" width="950">}}

To verify that NVLink4 features are enabled, run `netq show features nvl4`. You can also hide the NVLink4 features in the UI with `netq features nvl4 disable`.

## Intro to the NetQ UI

If you are unfamiliar with NetQ, the following sections provide an overview of the NetQ layout and functionality.

- {{<link title="NetQ User Interface Overview">}} 
- {{<link title="Events and Notifications">}}
- {{<link title="Lifecycle Management">}}

