---
title: Cumulus Production Ready Automation
author: Cumulus Networks
weight: 10
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
The Cumulus production ready automation package provides several examples of a fully operationalized, automated data center and includes:

- A standard reference topology for all examples
- A full Vagrant/libvirt simulation of the reference topology (cldemo2) that provides the foundational physical infrastructure and bootstrap configuration to support and demonstrate Cumulus Linux features and technologies
- Best practice Ansible automation and infrastructure as code (IaC)
- Working examples of continuous integration/continuous deployment (CI/CD) using Gitlab
- CI/CD testing powered by NetQ Cloud
- A variety of golden standard EVPN-VXLAN architecture reference configurations

You can use this production ready automation package as a learning resource and as a starting template to implement these features, technologies and operational workflows in your Cumulus Linux Network environments.

## Cumulus Linux Reference Topology

The Cumulus Linux reference topology provides a common and consistent preconfigured spine and leaf base network topology, which serves as the basis for all supported Cumulus demos and golden standards.

This reference topology is intended to be a blank slate with minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

When you start the reference topology simulation environment, all interfaces (except for the out of band management network) are unconfigured and administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that are applied to this simulation topology.

See the Contributors Guide for more information on how to build a package like this, or contribute your own demo or environment for the base cumulus reference topology.

The Cumulus Linux reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out of band management. The devices include:

- 4 Cumulus Linux 3.7 spines
- 4 Cumulus Linux 3.7 leafs
- 8 Ubuntu 18.04 servers
- 2 Cumulus Linux 3.7 border leafs
- 2 Cumulus Linux 3.7 "fw" devices providing a placeholder for ‘policy’ devices
- 1 Ubuntu 18.04 out of band management server (oob-mgmt-server)
- 1 Cumulus Linux 3.7 out of band management switch (oob-mgmt-switch)
- 1 Cumulus NetQ Cloud virtual appliance (netq-ts)

{{<img src="/images/guides/cldemo2-diagram.png" >}}

The Cumulus Linux reference topology is included with every officially supported Cumulus Linux demo. More details about that relationship are discussed in the Contributors Guide. To see a full example of cumulus production ready automation, use one of the {{<link text="EVPN VXLAN golden standard demos" title="#Golden Standard Demos" >}}.

## Infrastructure as Code

The Cumulus production ready automation package contains examples of Cumulus best practice Ansible automation and infrastructure as code (IaC). A completely stock Ansible core installation is used without any vendor specific or third party plugins. Examples of Ansible best practices using roles, highly granular templates, and structured variables represent how you can store your network configurations as a highly scalable version of infrastructure as code. It is that base code that gets rendered by the automation engine to produce the final configurations that exist on the network devices.

## Continuous Integration/Continuous Deployment

As network operations become more programmatic and automated, and in combination with a robust simulation platform, CI/CD and devops style workflows are supplanting legacy workflows. You can test configuration changes automatically in a simulated environment to allow for more rapid and robust change management workflows. Cumulus production ready automation provides an example CI/CD pipeline implemented on Gitlab with the CI network testing and validation powered by {{<exlink url="https://docs.cumulusnetworks.com/cumulus-netq/" text="Cumulus NetQ">}}.

## Golden Standard Demos

Cumulus Networks currently provides three officially supported demo solutions to overlay and provision the Cumulus reference topology. These demos are EVPN-VXLAN environments; each performs tenant routing in a different style.

These golden standard demos and the underlying base reference topology are officially hosted on gitlab in the Golden Turtle folder of the {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle" text="Cumulus Consulting Gitlab group">}}.

{{%notice note%}}

The name *Golden Turtle* comes from the idea of a *golden reference* and the rocket turtle, which is the Cumulus Networks mascot. Golden reference + rocket turtle = Golden Turtle.

{{%/notice%}}

- {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnl2only" text="EVPN Layer 2 Only">}} is an EVPN-VXLAN environment with only a layer 2 extension.
- {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpncent" text="EVPN Centralized Routing">}} is an EVPN-VXLAN environment with a layer 2 extension between tenants with inter-tenant routing on a centralized (fw) device.
- {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym" text="EVPN Symmetric Mode">}} is an EVPN-VXLAN environment with a layer 2 extension, layer 3 VXLAN routing, and VRFs for multi-tenancy.

To see more detailed information, such as IP addressing and specifics of the included features, see the {{<exlink url="https://gitlab.com/cumulus-consulting/goldenturtle" text="README.md page of the demo">}}.
