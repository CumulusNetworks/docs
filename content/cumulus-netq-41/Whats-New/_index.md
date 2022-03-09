---
title: What's New
author: NVIDIA
weight: 10
subsection: true
toc: 1
---

{{<product>}} {{<version>}} eases your customers deployment and maintenance activities for their data center networks with new configuration, performance, and security features and improvements.

<!-- vale off -->
## What's New in NetQ 4.1.1 

<!-- vale on -->
NetQ 4.1.1 is a maintenance release that contains {{<link title="NVIDIA Cumulus NetQ 4.1 Release Notes#fixed-issues-in-411" text="fixes for security vulnerabilities">}}.

<!-- vale off -->
## What's New in NetQ 4.1.0
<!-- vale on -->

NetQ 4.1.0 includes the following new features and improvements:

- {{<link title="Flow Analysis" text="Flow trace and analysis support for Cumulus Linux fabrics.">}}
- {{<link title="Configure and Monitor What Just Happened#view-what-just-happened-metrics" text="Improved What Just Happened (WJH) dashboard.">}}
- {{<link title="gNMI Streaming" text="gNMI telemetry streaming">}} for system resource, interface, and counter data on Cumulus Linux.
- Early access support for {{<link title="gNMI Streaming#collect-wjh-data-using-gnmi" text="gNMI collection of What Just Happened data on SONiC.">}}
- {{<link title="Decommission Switches#decommission-from-the-netq-ui" text="You can decommision a switch from the NetQ UI.">}}
- The k8s cluster security certificate is now valid for 10 years from the date of installation.
- Enhanced monitoring for the SONiC operating system. Support includes collection of the MAC FDB, interface counters, and DOM information. This is an early access feature.
- Validation performance improvements and the ability to {{<link title="Validation Checks#disabling-validation-checks" text="disable validation checks.">}}
- {{<link title="Configure System Event Notifications#create-a-channel" text="Generic webhook notification channel.">}}
- {{<link title="Manage Device Groups" text="Device group labels">}} to create validations for specific sets of devices.
- {{<link title="Validation Checks#addresses-validation-tests" text="Validation for duplicate IP address detection in your network.">}}

## Upgrade Paths

You can upgrade NetQ versions 3.0.0 and later directly to version 4.1.0. Upgrades from NetQ 2.4.x and earlier require a fresh installation.

## Additional Information

For information regarding bug fixes and known issues present in this release, refer to the {{<link title="NVIDIA Cumulus NetQ 4.1 Release Notes" text="release notes">}}.
