---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new feature and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.3 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.3.0
<!-- vale on -->

This release includes several performance and infrastructure improvements that make NetQ faster and more reliable. Additional features and improvements include: 

{{<link title="SSO Authentication" text="SSO configuration">}} that lets administrators add user accounts more efficiently.

{{<link title="Flow Analysis" text="Flow analysis">}} UI enhancements, including:

- Animation with source and destination IP address labels to clarify the flow direction.
- Partial-path visualizations that display data from switches outside of discovered paths.
- Revised parameter defaults when creating a flow analysis, including VRF selection for environments with multiple VRFs.

An updated {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/knowledge-base/Support/Licensing/NetQ-Cookie-Policy/" text="cookie policy">}}.

## Upgrade Paths

You can upgrade from NetQ versions 4.2.0 and later directly to version 4.3.0. Upgrades from NetQ versions earlier than 4.2.0 require a fresh installation or an incremental upgrade to version 4.2.0 first.
## Compatible Agent Versions

NetQ 4.3.0 is compatible with NetQ Agent versions 4.2.0 and above. You can install NetQ Agents on switches and servers running:

- Cumulus Linux 3.7.12 and later
- SONiC 202012 and later
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04


