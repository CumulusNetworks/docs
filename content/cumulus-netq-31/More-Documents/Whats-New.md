---
title: What's New
author: Cumulus Networks
weight: 630
---

Cumulus NetQ {{<version>}} adds significant functionality improvements that streamline network operations and eliminate barriers to adoption of open networking for your customers. Included in the updated software are lifecycle Management (LCM) capabilities that enable NetQ to deliver upgrade and configuration management with push button simplicity.

You can upgrade from NetQ 2.4.x to NetQ 3.0.0. Upgrades from NetQ 2.3.x and earlier require a fresh installation.

**Cumulus NetQ 3.0.0** includes the following new features and improvements:

- {{<link url="Lifecycle-Management" text="Lifecycle Management">}} support for Cumulus Linux upgrade on monitored switches (NetQ UI or CLI)
    - Simple NetQ UI workflow to prepare, run upgrade jobs, and evaluate results
    - Option to automatically generate before and after network snapshots for comparison
    - Option to roll back to previous CL version in the event of upgrade failure
- Manage {{<link url="Application-Management/#specify-notification-channels" text="notification channels">}} for threshold-based events through NetQ UI
- Embedded NetQ UI application help, with step-by-step instructions and link to user documentation
- Password change required on first login to NetQ UI
- Display all addresses in a subnet, supernet or layer 3 gateway of an address using `netq show ip addresses` and `netq show ipv6 addresses` commands
- Tune NetQ Agent polling for events and resources, and specify polling frequency using `netq config agent command` command set
- Specify a list of hostnames when running `netq check` commands
- View additional statistics from `netq <hostname> show ethtool-status` command
- Ported Python 2 codebase to Python 3

{{<notice note>}}
LNV support has been removed as of this release.
{{</notice>}}

For information regarding bug fixes and known issues present in this release, refer to the {{<link title="Cumulus NetQ 3.0 Release Notes" text="release notes">}}.
