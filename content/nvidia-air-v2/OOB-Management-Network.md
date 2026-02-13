---
title: OOB Management Network
author: NVIDIA
weight: 45
product: NVIDIA Air 2.0
---

## Overview

The out-of-band (OOB) management network is an optional feature that creates a dedicated management plane for your simulation, separate from your data plane. When enabled, Air provisions and configures the entire management network for you.

The OOB network gives you a single entry point to access all nodes in your simulation. From the `oob-mgmt-server`, you can SSH into any node by hostname (for example, `ssh leaf01`). Nodes can also use the OOB network to reach external networks, which is useful for downloading packages, pulling configurations, or other outbound connectivity tasks.

This separation mirrors real-world data center design, where management traffic is isolated from production traffic. Your simulation nodes have two network identities: a management interface (typically `eth0`) on the OOB network, and data interfaces (such as `swp1`, `eth1`) that you configure for your simulation traffic.

## Architecture

The OOB network uses a leaf-spine topology that scales automatically based on the number of nodes in your simulation.

### Basic Topology (up to 226 nodes)

For simulations with 226 or fewer nodes, Air creates a single leaf switch:

```
                     ┌───────────────────────┐
                     │   oob-mgmt-server     │
                     │   192.168.200.1       │
                     │                       │
                     │  • DHCP server        │
                     │  • DNS server         │
                     │  • Gateway/NAT        │
                     └───────────┬───────────┘
                                 │
                     ┌───────────┴───────────┐
                     │   oob-mgmt-switch     │
                     │   (leaf switch)       │
                     │   192.168.200.254     │
                     └───────────┬───────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
        ┌─────┴─────┐      ┌─────┴─────┐      ┌─────┴─────┐
        │  node1    │      │  node2    │      │  node3    │
        │  .200.2   │      │  .200.3   │      │  .200.4   │
        └───────────┘      └───────────┘      └───────────┘
```

### Scaled Topology (227+ nodes)

For larger simulations, Air automatically adds additional leaf switches and spine switches to interconnect them:

```
                          oob-mgmt-server
                                 │
                     ┌───────────┴───────────┐
                     │   oob-mgmt-leaf-1     │
                     │   (nodes 1-226)       │
                     └───────────┬───────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
        ┌─────┴─────┐      ┌─────┴─────┐      ┌─────┴─────┐
        │  spine-1  │      │  spine-2  │      │    ...    │
        └─────┬─────┘      └─────┬─────┘      └─────┬─────┘
              │                  │                  │
    ┌─────────┴──────────────────┴──────────────────┴─────────┐
    │                            │                            │
┌───┴───────────┐      ┌─────────┴───────┐      ┌─────────────┴───┐
│oob-mgmt-leaf-2│      │ oob-mgmt-leaf-3 │      │       ...       │
│(nodes 227-452)│      │ (nodes 453-678) │      │                 │
└───────────────┘      └─────────────────┘      └─────────────────┘
```

The OOB network can scale up to approximately 23,000 nodes.

## IP Addressing

The OOB network uses the `192.168.0.0/16` private address space. Each leaf switch serves a `/24` subnet, starting at `192.168.200.0/24` and allocating downward:

| Subnet | Leaf Switch | Node IP Range | Gateway (Leaf SVI) |
|--------|-------------|---------------|-------------------|
| 192.168.200.0/24 | leaf-1 | 192.168.200.2 - 192.168.200.253 | 192.168.200.254 |
| 192.168.199.0/24 | leaf-2 | 192.168.199.1 - 192.168.199.253 | 192.168.199.254 |
| 192.168.198.0/24 | leaf-3 | 192.168.198.1 - 192.168.198.253 | 192.168.198.254 |
| ... | ... | ... | ... |

### Reserved Addresses

| Address | Purpose |
|---------|---------|
| 192.168.200.1 | OOB management server |
| .254 | Leaf switch gateway (per subnet) |
| .255 | Broadcast |

## What Gets Configured Automatically

When you enable the OOB network, Air automatically configures:

- **DHCP server** on the `oob-mgmt-server` with static IP assignments for each node based on MAC address
- **DNS server** (dnsmasq) so you can reach nodes by hostname (for example, `ssh spine01`)
- **Management interface** (`eth0`) on each node, connected to the appropriate leaf switch
- **IP routing** between subnets using BGP on the leaf and spine switches
- **NAT gateway** on the `oob-mgmt-server` for outbound internet access
- **DHCP relay** on leaf switches to forward DHCP requests to the server
- **SSH key injection** so your Air SSH keys work on the `oob-mgmt-server`

### Disabling the DHCP Service

By default, the OOB network includes a fully configured DHCP server. If you want to manage DHCP yourself — for example, to run your own DHCP server with custom configurations — you can disable the automatic DHCP service while keeping the rest of the OOB network (L2 connectivity, management interfaces, and infrastructure nodes).

To disable DHCP when importing a JSON topology, set `enable_dhcp` to `false` in the `oob` object:

```
{
    "nodes": { ... },
    "links": [ ... ],
    "oob": {
        "enable_dhcp": false
    }
}
```

When DHCP is disabled:

- The `oob-mgmt-server` and OOB switch infrastructure are still created.
- Management interfaces (`eth0`) are still connected to the OOB network.
- No DHCP server, DNS, or NAT gateway is configured on the `oob-mgmt-server`.
- Nodes do not receive automatic IP assignments. You must configure IP addresses manually or provide your own DHCP server.

## Accessing Your Nodes

The `oob-mgmt-server` is the entry point to your simulation. When you connect via SSH (using the service URL provided by Air), you land on this server.

From there, SSH to any node by hostname:

```bash
# Connect to the OOB server via AIR
ssh ubuntu@<air-service-url>

# From OOB server, reach any node by name
ssh leaf01
ssh spine01
ssh server1
```

## Requirements

For nodes to receive their OOB IP address automatically:

- The node must have DHCP enabled on its management interface
- The node must be connected to the OOB network (handled automatically when OOB is enabled)

Standard images (Cumulus Linux, Ubuntu cloud images) work out of the box. For custom images, ensure DHCP is configured on the management interface.

## Interface Naming

For standard nodes (nodes without `emulation_type` in the topology), Air handles interface naming via UDEV rules. Before boot, Air injects rules into the VM filesystem that rename each interface based on its MAC address to match the topology name. The flow is:

1. Air injects UDEV rules mapping MAC addresses to topology names
2. VM boots, UDEV renames interfaces (management interface becomes `eth0`)
3. Image runs DHCP on the management interface
4. Node receives its reserved IP

Air-provided images are pre-configured to work with this system. For custom images, your image must:

- Use kernel parameters: `net.ifnames=1 biosdevname=1` (or any non-zero value for `net.ifnames`)
  - These enable predictable interface naming, which prevents collisions with Air's UDEV rules that use traditional names like `eth0`
- Set `AlternativeNamesPolicy=` (empty) in systemd network configuration
  - This prevents systemd from assigning alternate names that conflict with UDEV

With these settings, your management interface will be named `eth0`.

Emulated nodes (nodes with `emulation_type` in the topology) use their simulator engine's logic for interface naming. Refer to the simulator's documentation for details.
