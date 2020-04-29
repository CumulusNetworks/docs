---
title: Cumulus Production Ready Automation
author: Cumulus Networks
weight: 10
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
Cumulus production ready automation provides several examples of a fully operationalized, automated data center and includes:

- A standard reference topology for all examples
- A full Vagrant/libvirt simulation of the reference topology
- Best practice Ansible automation and infrastructure as code (IaC)
- Working examples of continuous integration/continuous deployment (CI/CD) using Gitlab
- CI/CD testing powered by NetQ Cloud
- A variety of golden standard EVPN-VXLAN architecture reference configurations

You can use this production ready automation package as a learning resource and as a starting template to implement these features, technologies and operational workflows in your Cumulus Linux Network environments.

Network devices and hosts in simulation that are the core architecture of this example are simulated in a pre-constructed network topology referred to as the Cumulus Linux Reference Topology (cldemo2). This simulation environment is based on Vagrant and libvirt/kvm. It provides the foundational physical infrastructure and bootstrap configuration to be able to support and demonstrate Cumulus Linux features and technologies. Additional technical details are discussed in {{<link url="#cumulus-linux-reference-topology" text="Cumulus Linux Reference Topology">}}.

{{%notice note%}}

This is the second Cumulus Linux demo environment, creating the name `cldemo2`

{{%/notice%}}

This package also contains examples of Cumulus best practice Ansible automation and infrastructure as code (IaC). A completely stock Ansible core installation is used without any vendor specific or 3rd party plugins. Examples of Ansible best practices using roles, highly granular templates, and structured variables represent how your network configurations can be stored as a highly scalable version of infrastructure as code. It is that base code that gets rendered by the automation engine to produce the final configurations that exist on the network devices.

As network operations become more programmatic and automated, and in combination with a robust simulation platform, CI/CD and devops style workflows are supplanting legacy workflows. You can test configuration changes automatically in a simulated environment to allow for more rapid and robust change management workflows. Cumulus production ready automation provides an example CI/CD pipeline implemented on Gitlab with the CI network testing and validation powered by {{% exlink text="Cumulus NetQ" url="https://docs.cumulusnetworks.com/cumulus-netq/" %}}.

These golden standard demos and the underlying base reference topology are officially hosted on gitlab in the Golden Turtle folder of the {{% exlink text="Cumulus Consulting Gitlab group" url="https://gitlab.com/cumulus-consulting/goldenturtle" %}}.

{{%notice note%}}

The name *Golden Turtle* comes from the idea of a *golden reference* and the rocket turtle, which is the Cumulus Networks mascot. Golden reference + rocket turtle = Golden Turtle.

{{%/notice%}}

## Golden Standard Demos

Cumulus Networks currently provides three officially supported demo solutions to overlay and provision the Cumulus reference topology. All of these demos are EVPN-VXLAN environments that each perform tenant routing in a different style.

- [EVPN Layer 2 Only](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnl2only) - An EVPN-VXLAN environment with only layer 2 extension.
- [EVPN Centralized Routing](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpncent) - A EVPN-VXLAN environment with layer 2 extension between tenants with inter-tenant routing on a centralized (fw) device.
- [EVPN Symmetric Mode](https://gitlab.com/cumulus-consulting/goldenturtle/dc_configs_vxlan_evpnsym) - An EVPN-VXLAN environment with layer 2 extension, layer 3 VXLAN routing and VRFs for multi-tenancy

You can see more detailed information, such as IP addressing and specifics of the included features on the README.md page of each demo: https://gitlab.com/cumulus-consulting/goldenturtle.

## Cumulus Linux Reference Topology

The Cumulus Linux reference topology provides a common and consistent preconfigured spine and leaf base network topology. This serves as the basis for all supported Cumulus demos and golden standards. This reference topology is intended to be a blank slate with minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

When you start the reference topology simulation environment, all interfaces (except for the out of band management network) are unconfigured and administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that are applied to this simulation topology.

See the Contributors Guide for more information on how to build a package like this or contribute your own demo or environment for the base cumulus reference topology.

The Cumulus Linux reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out of band management. The devices include:

- 4x Cumulus Linux 3.7 spines
- 2x Cumulus Linux 3.7 leafs
- 8x Ubuntu 18.04 servers
- 2x Cumulus Linux 3.7 border leafs
- 2x Cumulus Linux 3.7 "fw" devices providing a placeholder for ‘policy’ devices
- 1x Ubuntu 18.04 out of band management server (oob-mgmt-server)
- 1x Cumulus Linux 3.7 out of band management switch (oob-mgmt-switch)
- 1x Cumulus NetQ Cloud virtual appliance (netq-ts)

{{<img src="/images/guides/cldemo2-diagram.png" >}}

The Cumulus Linux reference topology is included with every officially supported Cumulus Linux demo. More details about that relationship are discussed in the Contributors Guide. To see a full example of cumulus production ready automation, use one of the {{<link text="EVPN VXLAN golden standard demos" title="#Golden Standard Demos" >}}.
