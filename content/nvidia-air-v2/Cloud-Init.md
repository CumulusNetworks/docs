---
title: Cloud-Init
author: NVIDIA
weight: 50
product: NVIDIA Air 2.0
---

## Overview

Cloud-init is an industry-standard tool for automating the initial configuration of virtual machines on first boot. NVIDIA Air supports cloud-init through the {{<exlink url="https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html" text="NoCloud datasource">}}, which allows you to inject user-data and meta-data into your simulation nodes.

With cloud-init, you can automate tasks such as:
- Setting hostnames
- Installing packages
- Writing configuration files
- Running custom scripts on first boot

## Supported Images

Cloud-init is supported on the following Air-provided images:

| Image | Cloud-Init Support |
|-------|-------------------|
| `generic/ubuntu2404` | Yes |
| `generic/ubuntu2204` | Yes |
| `generic/ubuntu2004` | Yes |

Custom images that include cloud-init with NoCloud datasource support also work with this feature.

## Configuration

Cloud-init configuration consists of two components:

- **User-data**: Defines the actions to perform on first boot, such as installing packages, running commands, or writing files. Supports all standard {{<exlink url="https://cloudinit.readthedocs.io/en/latest/explanation/format.html" text="cloud-init user-data formats">}}.
- **Meta-data**: Provides instance metadata such as the hostname. Uses a simple `key: value` format.

### Workflow

Cloud-init is configured through the API. The general workflow is:

1. Create a simulation with your desired topology, but do not start it yet.
2. Create **UserConfig** resources containing your user-data and meta-data content. UserConfigs are reusable — for example, you can create one user-data config and share it across multiple nodes, while giving each node its own meta-data with a unique hostname.
3. Assign the UserConfig resources to simulation nodes using the {{<exlink url="https://air-ngc.nvidia.com/api/docs/#tag/nodes/PATCH/api/v3/simulations/nodes/bulk-assign" text="bulk-assign endpoint">}}. This endpoint lets you assign both user-data and meta-data to multiple nodes in a single request.
4. Start the simulation. Cloud-init runs automatically on each node during its first boot.

{{%notice note%}}
Cloud-init runs during the initial boot of each node. Configure cloud-init assignments before starting the simulation for the first time. Assignments made after a node has already booted do not take effect until the node is rebuilt.
{{%/notice%}}

### Example

The following `cloud-config` user-data installs packages and writes a configuration file on first boot:

```yaml
#cloud-config

packages:
- curl
- jq

write_files:
- path: /etc/myapp/config.yaml
  content: |
    server:
      listen: 0.0.0.0:8080
      log_level: info
```

For information and additional examples of user-data and meta-data formats, refer to the {{<exlink url="https://cloudinit.readthedocs.io/en/latest/explanation/format.html" text="cloud-init documentation">}}.
