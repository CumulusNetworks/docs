---
title: What's New
author: NVIDIA
weight: 20
product: NVIDIA DSX Air
---
<!-- vale off -->
Check out the latest updates to {{<exlink url="https://dsx-air.nvidia.com" text="NVIDIA DSX Air">}}.

## August 2026
<!-- Air:WhatsNew --> 
### 82.2.1.24.1000
- Added ability to clone a simulation directly from the UI
- The UI now shows the rate required to run a simulation
- Demos can now be published to a specific subset of organizations
### 82.2.1.23.1000
- You can now create your own demo and submit it for publication to the Demo Marketplace
<!-- Air:WhatsNew -->

## July 2026
### 82.2.1.20.27
- Node boot order: You can now specify an ordered list of boot devices for a node using the `boot` advanced attribute in your topology. List devices such as `network`, `hd`, and `cdrom` in the order you want them tried, so a node can attempt PXE (network) boot first and fall back to local disk. Specifying a single boot device continues to work as before.
- Removed NetQ SaaS support.

## May 2026
### 82.2.1.15.2
- Updated and added Jupiter Notebook examples in the SDK
- Fixed a UI issue where not all valid interfaces were displayed during service creation 
- Fixed an issue causing the console to remain stuck in a loading state when opened during a simulation rebuild


## April 2026
### 82.2.1.8.11
- Fixed an issue where high-fidelity nodes with outbound interfaces could not consistently use their data ports
- Fixed an issue where users were able to select enablement durations exceeding the five‑year limit enforced by NGC

### 82.2.1.7.3
- Reduced the risk of S3 throttling during cloning operations

## March 2026
### 82.2.1.5.7
- Fixed an issue where the node instructions table did not resize correctly on smaller viewports
- Fixed a UI display issue affecting images with names longer than 128 characters

### 82.2.1.5.6
- Fixed an issue that prevented large simulations from being deleted

