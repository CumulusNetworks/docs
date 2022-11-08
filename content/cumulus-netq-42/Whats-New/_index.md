---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

This page summarizes new features and improvements for the NetQ {{<version>}} release. For a complete list of open and fixed issues, see the {{<link title="NVIDIA NetQ 4.2 Release Notes" text="release notes">}}.

<!-- vale off -->
## What's New in NetQ 4.2.0
<!-- vale on -->

NetQ 4.2.0 includes the following new features and improvements:

-  {{<link title="Monitor Events" text= "Events management UI enhancements">}}, including:
    - a simplified Events card design with integrated validation checks
    - event acknowledgement and suppression options
- Flow analysis enhancements, including:
  - {{<link title="Flow Analysis#partial-path-support" text="Partial path support">}}
  - {{<link title="Flow Analysis#view-wjh-events" text="WJH event support">}}
- {{<link title="Validation Checks#roce-validation-tests" text="RoCE validation">}}
- {{<link title="gNMI Streaming" text="New gNMI object models">}}:
  - openconfig-plaftorm
  - openconfig-lldp
- {{<link title="Install the NetQ System" text="Simplified installation process">}}
- {{<link title="Validate Overall Network Health" text="Improved network health UI with validation summary">}}
- GUI support for {{<link title="Validation Checks##addresses-validation-tests" text="duplicate address detection">}}
- Early Access {{<link title="Install NetQ Agents#configure-the-on-switch-opta" text="on-switch OPTA support for NetQ cloud deployments.">}}
- Early Access support for {{<link title="Monitor DPU Inventory" text="DPU monitoring">}}
## Upgrade Paths

You can upgrade NetQ versions 4.1.0 and later directly to version 4.2.0. Upgrades from NetQ versions earlier than 4.1.0 require a fresh installation or an incremental upgrade to version 4.1.0 first.

NetQ no longer supports the Admin UI for installation and upgrades. Follow the {{<link title="Installation Management" text="updated instructions">}} according to your deployment model.
## Compatible Agent Versions

NetQ 4.2.0 is compatible with NetQ Agent version 4.1.0 and above. 

You can install NetQ Agents on switches and servers running

- Cumulus Linux 3.7.12 and later
- SONiC 202012 and later
- CentOS 7
- RHEL 7.1
- Ubuntu 18.04


