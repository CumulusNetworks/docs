---
title: NVUE Automation with Ansible
author: NVIDIA
weight: 30
product: Technical Guides
imgData: guides
---
To automate the network infrastructure in your datacenter using Ansible, NVIDIA provides the following options:
- Ansible Modules
- Production Ready Automation

## Ansible Modules

{{<exlink url="https://galaxy.ansible.com/nvidia/nvue" text="The NVIDIA NVUE Collection">}} includes Ansible modules to help you interact with NVIDIA devices managed by NVUE. The modules are developed and validated using Ansible 2.11 and Python 3.6, and are supported on Cumulus Linux 5.x.
The collection includes high-level wrapper modules and object specific modules as listed below:

**High-level modules**
 - nvidia.nvue.command - A wrapper around the NVUE command line tool with added templating and automated dialog prompting.
 - nvidia.nvue.api – A wrapper around the NVUE REST API to send and retrieve NVUE configuration.

**Object specific modules**
 - nvidia.nvue.bridge - Bridge configuration with the REST API.
 - nvidia.nvue.config – Revisions with the REST API
 - nvidia.nvue.evpn - EVPN configuration with the REST API.
 - nvidia.nvue.interface - Interface configuration with the REST API.
 - nvidia.nvue.mlag - MLAG configuration with the REST API.
 - nvidia.nvue.router - Router configuration with the REST API.
 - nvidia.nvue.service - Service configuration with the REST API.
 - nvidia.nvue.system – System configuration with the REST API.
 - nvidia.nvue.vrf - VRF configuration with the REST API.
 - nvidia.nvue.vxlan - VXLAN configuration with the REST API.

For REST API endpoints that are not covered by the object-specific modules or for sub-paths within the object specific modules (for example, `/interface/<id>/qos/roce/counters`), you can leverage the `nvidia.nvue.api` module and specify the endpoint in the `path` parameter.

## Production Ready Automation (PRA)

The Production Ready Automation package from NVIDIA uses Ansible roles to provide several examples of a fully operationalized, automated data center in the form of playbooks and includes:
 - A standard reference topology for all examples.  
 - A variety of golden standard EVPN-VXLAN architecture reference configurations for the following examples:
    - EVPN centralized
    - EVPN layer 2 only
    - EVPN symmetric
    - EVPN multihoming
 - A full Vagrant and libvirt simulation of the NVIDIA reference topology (cldemo2) that provides the foundational physical infrastructure and bootstrap configuration to support and demonstrate Cumulus Linux features and technologies.
 - Best practice Ansible automation and infrastructure as code (IaC).
 - Working examples of Continuous Integration and Continuous Deployment (CI/CD) using GitLab.
 - CI/CD testing powered by NetQ Cloud.

You can use this Production Ready Automation package as a learning resource and as a starting template to implement these features, technologies, and operational workflows in your Cumulus Linux network environments.

Production Ready Automation generates the jinja2 template for the startup configuration (`startup.yaml`) that NVUE uses.

You can find more information {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/production-ready-automation/" text="here">}}.

## Recommendations

|Configuration|Cumulus Linux Version | Recommendations|
|-------------|----------------------|----------------|
|Day 0        | Prior to 5.0         | Use the **PRA** package to automate `startup.yaml` file generation.|
|             |5.x and above         |Use the **Ansible modules** to set up the configuration as desired and run it across all the switches.|
|Day 1        |5.x and above         | Use the **Ansible modules** that are available to make configuration changes on the go.|

