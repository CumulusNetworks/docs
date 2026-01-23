---
title: OOB Management Network
author: NVIDIA
weight: 45
product: NVIDIA Air
---

## Overview

The Out-of-Band (OOB) management network is an optional feature that creates a dedicated management plane for your simulation, separate from your data plane. When enabled, AIR provisions and configures the entire management network for you.

The OOB network gives you a single entry point to access all nodes in your simulation. From the `oob-mgmt-server`, you can SSH to any node by hostname (for example, `ssh leaf01`). Nodes can also use the OOB network to reach external networks—useful for downloading packages, pulling configurations, or other outbound connectivity.

This separation mirrors real-world data center design, where management traffic is isolated from production traffic. Your simulation nodes have two network identities: a management interface (typically `eth0`) on the OOB network, and data interfaces (such as `swp1`, `eth1`) that you configure for your simulation traffic.

## Architecture

The OOB network uses a leaf-spine topology that scales automatically based on the number of nodes in your simulation.

### Basic Topology (up to 226 nodes)

For simulations with 226 or fewer nodes, AIR creates a single leaf switch:

```
                     ┌───────────────────────┐
                     │   oob-mgmt-server     │
                     │   192.168.0.253       │
                     │                       │
                     │  • DHCP server        │
                     │  • DNS server         │
                     │  • Gateway/NAT        │
                     └───────────┬───────────┘
                                 │
                     ┌───────────┴───────────┐
                     │   oob-mgmt-switch     │
                     │   (leaf switch)       │
                     │   192.168.0.254       │
                     └───────────┬───────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
        ┌─────┴─────┐      ┌─────┴─────┐      ┌─────┴─────┐
        │  node1    │      │  node2    │      │  node3    │
        │  .0.1     │      │  .0.2     │      │  .0.3     │
        └───────────┘      └───────────┘      └───────────┘
```

### Scaled Topology (227+ nodes)

For larger simulations, AIR automatically adds additional leaf switches and spine switches to interconnect them:

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

The OOB network uses the `192.168.0.0/16` private address space. Each leaf switch serves a `/24` subnet:

| Subnet | Leaf Switch | Node IP Range | Gateway (Leaf SVI) |
|--------|-------------|---------------|-------------------|
| 192.168.0.0/24 | leaf-1 | 192.168.0.1 - 192.168.0.252 | 192.168.0.254 |
| 192.168.1.0/24 | leaf-2 | 192.168.1.1 - 192.168.1.252 | 192.168.1.254 |
| 192.168.2.0/24 | leaf-3 | 192.168.2.1 - 192.168.2.252 | 192.168.2.254 |
| ... | ... | ... | ... |

### Reserved Addresses

| Address | Purpose |
|---------|---------|
| .253 | OOB management server (on 192.168.0.0/24 only) |
| .254 | Leaf switch gateway |
| .255 | Broadcast |

## What Gets Configured Automatically

When you enable the OOB network, AIR automatically configures:

- **DHCP server** on the `oob-mgmt-server` with static IP assignments for each node based on MAC address
- **DNS server** (dnsmasq) so you can reach nodes by hostname (for example, `ssh spine01`)
- **Management interface** (`eth0`) on each node, connected to the appropriate leaf switch
- **IP routing** between subnets using BGP on the leaf and spine switches
- **NAT gateway** on the `oob-mgmt-server` for outbound internet access
- **DHCP relay** on leaf switches to forward DHCP requests to the server
- **SSH key injection** so your AIR SSH keys work on the `oob-mgmt-server`

## Accessing Your Nodes

The `oob-mgmt-server` is the entry point to your simulation. When you connect via SSH (using the service URL provided by AIR), you land on this server.

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

For standard nodes (nodes without `emulation_type` in the topology), AIR handles interface naming via UDEV rules. Before boot, AIR injects rules into the VM filesystem that rename each interface based on its MAC address to match the topology name. The flow is:

1. AIR injects UDEV rules mapping MAC addresses to topology names
2. VM boots, UDEV renames interfaces (management interface becomes `eth0`)
3. Image runs DHCP on the management interface
4. Node receives its reserved IP

AIR-provided images are pre-configured to work with this system. For custom images, your image must:

- Use kernel parameters: `net.ifnames=4 biosdevname=1`
- Set `AlternativeNamesPolicy=` (empty) in systemd network configuration

With these settings, your management interface will be named `eth0`.

Emulated nodes (nodes with `emulation_type` in the topology) use their simulator engine's logic for interface naming—see the simulator's documentation for details.
