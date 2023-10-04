---
title: Automation with Cumulus Linux
author: NVIDIA
weight: 30
product: Technical Guides
imgData: guides
---
NVUE is an object-oriented, schema driven model of a complete Cumulus Linux system (hardware and software) providing a robust API that allows for multiple interfaces to both view (show) and configure (set and unset) any element within a system running the NVUE software.

The NVUE object model definition uses the {{<exlink url="https://github.com/OAI/OpenAPI-Specification" text="OpenAPI specification (OAS)">}}. OAS is a data definition, manipulation, and modeling language (DML) that lets you build model-driven interfaces for both humans and machines. Although the computer networking and telecommunications industry commonly uses YANG (standardized by IETF) as a DML, the adoption of OpenAPI is broader, spanning cloud to compute to storage to IoT and even social media. The {{<exlink url="https://www.openapis.org/about" text="OpenAPI Initiative (OAI) consortium ">}} leads OpenAPI standardization, a chartered project under the Linux Foundation.

Like other systems that use OpenAPI, the NVUE OAS schema defines the endpoints (paths) exposed as RESTful APIs. With these REST APIs, you can perform various create, retrieve, update, delete, and eXecute (CRUDX) operations. The OAS schema also describes the API inputs and outputs (data models).

You can use the NVUE object model in the following ways:
- With the NVUE CLI, where you configure, monitor, and manage the Cumulus Linux network elements. The CLI commands translate to their equivalent REST APIs, which Cumulus Linux then runs on the NVUE object model.
- With the NVUE REST API, where you run the GET, PATCH, DELETE, and other REST APIs on the NVUE object model endpoints to configure, monitor, and manage the switch. Because of the large user community and maturity of OAS, you can work with several popular tools and libraries to create client-side bindings to use the NVUE REST API. You can view the NVUE REST API documentation using Swagger {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-54/api/index.html" text="here">}}.

## Enable the NVUE API

With Cumulus Linux 5.4 and later, you must enable the NVUE API to access it. Run the following set of commands on the switch:

```
cumulus@switch:~$ sudo ln -s /etc/nginx/sites-{available,enabled}/nvue.conf 
cumulus@switch:~$ sudo sed -i 's/listen localhost:8765 ssl;/listen \[::\]:8765 ipv6only=off ssl;/g' /etc/nginx/sites-available/nvue.conf 
cumulus@switch:~$ sudo systemctl restart nginx 
```

The CLI and the REST API are equivalent in functionality; you can run all management operations from the REST API or the CLI. The NVUE object model drives both the REST API and the CLI management operations. All operations are consistent; for example, the CLI `nv show` commands reflect any PATCH operation (create) you run through the REST API.

NVUE follows a declarative model, removing context-specific commands and settings. It is structured as a big tree that represents the entire state of a Cumulus Linux instance. At the base of the tree are high level branches representing objects, such as router and interface. Under each of these branches are additional branches. As you navigate through the tree, you gain a more specific context. At the leaves of the tree are actual attributes, represented as key-value pairs. The path through the tree is similar to a filesystem path.

## Run your First NVUE API

You can use any tool that can run API calls. In this guide, the sample implementation uses curl.

The following example performs a GET operation to fetch the current running configuration on the switch.

{{< tabs "TabID36 ">}}
{{< tab "Sample Call ">}}

{{< tabs "TabID39 ">}}
{{< tab "NVUE REST API ">}}

```
cumulus@switch:~$ curl -k -u cumulus:CumulusLinux! -X GET "https://127.0.0.1:8765/nvue_v1/?rev=applied"
```

{{< /tab >}}
{{< tab "NVUE CLI Command ">}}

```
cumulus@switch:~$ nv config show
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Sample Output ">}}

{{< tabs "TabID59 ">}}
{{< tab "NVUE REST API ">}}

```
"acl": {},
  "bridge": { 
    "domain": { 
      "br_default": { 
        "encap": "802.1Q", 
        "mac-address": "auto", 
        "multicast": { 
          "snooping": { 
            "enable": "off" 
          } 
        }, 
        "stp": { 
          "priority": 32768, 
          "state": { 
            "up": {} 
          } 
        }, 
        "type": "vlan-aware", 
        "untagged": 1, 
        "vlan": { 
          "10": { 
            "multicast": { 
...
```

{{< /tab >}}
{{< tab "NVUE CLI Command ">}}

```
- set: 
    bridge: 
      domain: 
        br_default: 
          type: vlan-aware 
          vlan: 
            '10': 
              vni: 
                '10': {} 
            '20': 
              vni: 
                '20': {} 
            '30': 
              vni: 
                '30': {} 
    evpn: 
      enable: on 
    mlag: 
      backup: 
        10.10.10.2: {} 
      enable: on 
      init-delay: 10 
      mac-address: 44:38:39:BE:EF:AA
... 
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## NVUE Configuration File

When you use NVUE to save network configuration, NVUE saves the configuration in a configuration file called `/etc/nvue.d/startup.yaml`.

You can edit or replace the contents of this file. NVUE applies the configuration in the file during system boot only if the `nvue-startup.service` is running. After you apply the configuration, NVUE writes to the corresponding Linux files.

When you configure the switch with NVUE commands, NVUE overwrites the settings in any file it manages. Do not run NVUE commands and manually edit the configuration files at the same time to configure the switch. Either configure the switch with NVUE commands only or manually edit the configuration files.

You can configure NVUE to ignore certain underlying Linux files when applying configuration changes. You can find more information {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-54/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="here">}}.

## NVUE Feature Support

With Cumulus Linux 5.4, the NVUE Object Model supports most features on the Cumulus Linux switch. At a high level, these are the supported objects:

| High-level Objects | Description |
| ------------------ | ----------- |
| acl | Access control lists. |
| bridge | Bridge domain configuration. |
| evpn | EVPN configuration. |
| interface | Interface configuration. |
| mlag | MLAG configuration. |
| nve | Network virtualization configuration, such as VXLAN-specfic MLAG configuration and VXLAN flooding. |
| platform | Platform configuration, such as hardware and software components. |
| qos | QoS RoCE configuration. |
| router | Router configuration, such as router policies, global BGP and OSPF configuration, PBR, PIM, IGMP, VRR, and VRRP configuration. |
| service | DHCP relays and server, NTP, PTP, LLDP, and syslog configuration. |
| system | Global system settings, such as the reserved routing table range for PBR and the reserved VLAN range for layer 3 VNIs, system login messages and switch reboot history. |
| vrf | VRF configuration. |

For features that NVUE does not yet support, you can use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-54/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-Snippets/#flexible-snippets" text="snippets">}}. Reach out to the Professional Services team for assistance.

## Ansible

Ansible® is an open-source IT automation tool that automates provisioning, configuration management, application deployment, orchestration, and many other manual IT processes. It works by connecting to what you want automated and pushing programs that execute instructions you normally do manually. These programs utilize Ansible modules that are written based on the specific expectations of the endpoint connectivity, interface, and commands.

An Ansible playbook is a blueprint of automation tasks, which are complex IT actions executed with no need for human involvement. Ansible playbooks are written in human-readable {{<exlink url="https://www.redhat.com/en/topics/automation/what-is-yaml" text="YAML">}} format and executed on a set, group, or classification of hosts, which together make up an Ansible inventory.

### Production Ready Automation (PRA)

The Production Ready Automation package from NVIDIA uses Ansible roles to provide several examples of a fully operationalized, automated data center in the form of playbooks and includes:
- A standard reference topology for all examples.
- A variety of golden standard EVPN-VXLAN architecture reference configurations for the following examples:
  - EVPN centralized
  - EVPN layer 2 Only
  - EVPN symmetric
  - EVPN multihoming
- A full Vagrant and libvirt simulation of the NVIDIA reference topology (cldemo2) that provides the foundational physical infrastructure and bootstrap configuration to support and demonstrate Cumulus Linux features and technologies.
- Best practice Ansible automation and infrastructure as code (IaC).
- Working examples of Continuous Integration and Continuous Deployment (CI/CD) using GitLab.
- CI/CD testing powered by NetQ Cloud.

You can use this Production Ready Automation package as a learning resource and as a starting template to implement these features, technologies, and operational workflows in your Cumulus Linux network environments.

Production Ready Automation generates the `jinja2` template for the startup configuration (`startup.yaml`) that NVUE uses.

You can find more information {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/production-ready-automation/" text="here">}}.

### Ansible Modules

{{<exlink url="https://galaxy.ansible.com/nvidia/nvue" text="The NVIDIA NVUE Collection">}} (`nvidia.nvue`) includes Ansible modules to help you interact with NVIDIA devices managed by NVUE. The modules are developed and validated using Ansible 2.11 and Python 3.6, and are supported on Cumulus Linux 5.x.

{{%notice note%}}
The various modules available as of the publication of this guide are: 
- The **CLI** is a wrapper around the `nv` command line tool with added templating and automated dialog prompting.
- The **REST API** enables you to send and retrieve NVUE configuration.
- **Object specific modules** are designed to work with the individual network objects and support various parameters that allow you to interact with them as required. The various modules supported include bridge, router, interface, evpn, mlag, system, vrf, and vxlan. 
You can find more details {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/Data-Center-Network-Automation-Ansible-Deployment-Guide/" text="here">}}.
{{%/notice%}}

## NVUE Migration Tool

The {{<exlink url="https://air.nvidia.com/migrate/" text="NVUE Migration tool">}} is designed to help you automate migration from older Cumulus Linux systems that support NCLU and ONYX to the newer systems that support NVUE.

{{< img src = "/images/guides/migration-tool.png" >}}

## NVIDIA Air

{{<exlink url="https://air.nvidia.com/SimulationsAll" text="NVIDIA Air">}} is a cloud hosted, network simulation platform that behaves exactly like a real-world production environment. NVIDIA Air can be used to create a digital twin of the IT infrastructure to validate automation code.

The {{<exlink url="https://air.nvidia.com/marketplace" text="demo marketplace">}} on NVIDIA Air has some fully configured pre-built labs that demonstrate best-practice configuration. It contains an {{<exlink url="https://air.nvidia.com/marketplace?demo_id=aa77bb13-6a7d-431c-9203-640510778beb" text="NVUE API lab">}} that helps you get started with the REST API.
