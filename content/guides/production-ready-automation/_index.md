---
title: Production Ready Automation Guide
weight: 40
cascade:
    product: Technical Guides
    author: NVIDIA
---

The Production Ready Automation package from NVIDIA provides several examples of a fully operationalized, automated data center and includes:

- A standard reference topology for all examples
- A variety of golden standard EVPN-VXLAN architecture reference configurations
- A full Vagrant and libvirt simulation of the NVIDIA reference topology (cldemo2) that provides the foundational physical infrastructure and bootstrap configuration to support and demonstrate Cumulus Linux features and technologies
- Best practice Ansible automation and infrastructure as code (IaC)
- Working examples of Continuous Integration and Continuous Deployment (CI/CD) using GitLab
- CI/CD testing powered by NetQ Cloud

You can use this Production Ready Automation package as a learning resource and as a starting template to implement these features, technologies and operational workflows in your Cumulus Linux network environments.

## NVIDIA Reference Topology

The NVIDIA reference topology provides a common and consistent preconfigured spine and leaf base network topology, which serves as the basis for all supported NVIDIA demos and golden standards. This reference topology is a blank slate with minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

The NVIDIA reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out-of-band management. The devices include:

- Four Cumulus Linux 3.7 spines
- Four Cumulus Linux 3.7 leafs
- Eight Ubuntu 18.04 servers
- Two Cumulus Linux 3.7 border leafs
- Two Cumulus Linux 3.7 *fw* devices that provide a placeholder for *policy* devices
- One Ubuntu 18.04 out-of-band management server (oob-mgmt-server)
- One Cumulus Linux 3.7 out-of-band management switch (oob-mgmt-switch)
- One Cumulus NetQ Cloud virtual appliance (netq-ts)

{{<img src="/images/guides/cldemo2-diagram.png" >}}

When you start the reference topology simulation environment, all interfaces (except for the out-of-band management network) are not configured and are administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that you apply to this simulation topology.

Every officially supported Cumulus Linux demo includes the NVIDIA reference topology. To see a full example of the Production Ready Automation, use one of the {{<link text="EVPN-VXLAN golden standard demos" title="#golden standard demos" >}}.

<!-- For information on how to build a package like this, or contribute your own demo or environment for the base NVIDIA reference topology, refer to the Contributors Guide.-->

## Golden Standard Demos

NVIDIA currently provides three officially supported demo solutions to overlay and provision the reference topology. These demos are EVPN-VXLAN environments and each performs tenant routing in a different style.

The golden standard demos and the underlying base reference topology are officially hosted on GitLab in the Golden Turtle folder of the {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle" text="Cumulus Consulting GitLab group">}}.

{{%notice note%}}

The name *Golden Turtle* comes from the idea of a *golden reference* and the rocket turtle, which is the Cumulus Linux mascot. Golden reference + rocket turtle = Golden Turtle.

{{%/notice%}}

- {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnl2only" text="EVPN Layer 2 Only">}} is an EVPN-VXLAN environment with only a layer 2 extension.
- {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpncent" text="EVPN Centralized Routing">}} is an EVPN-VXLAN environment with a layer 2 extension between tenants with inter-tenant routing on a centralized (fw) device.
- {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym" text="EVPN Symmetric Mode">}} is an EVPN-VXLAN environment with a layer 2 extension, layer 3 VXLAN routing, and VRFs for multi-tenancy.

For more detailed information about IP addressing and included features, refer to the {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle" text="README">}} page of the demo.

## Infrastructure as Code

The Production Ready Automation package contains examples of best practice Ansible automation and infrastructure as code (IaC). It uses a completely stock Ansible core installation without any vendor specific or third-party plugins. Examples of Ansible best practices using roles, highly granular templates, and structured variables represent how you can store your network configurations as a highly scalable version of infrastructure as code. It is that base code that the automation engine renders to produce the final configurations that exist on the network devices.

## Continuous Integration and Continuous Deployment

As network operations become more programmatic and automated, and in combination with a robust simulation platform, CI/CD and DevOps style workflows are supplanting legacy workflows. You can test configuration changes automatically in a simulated environment to allow for more rapid and robust change management workflows. The Production Ready Automation package provides an example CI/CD pipeline implemented on GitLab with the CI network testing and validation powered by {{<kb_link latest="netq" text="NVIDIA NetQ">}}.
