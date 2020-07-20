---
title: What's New
author: Cumulus Networks
weight: 630
---

Cumulus NetQ {{<version>}} adds significant functionality improvements that streamline network operations and eliminate barriers to adoption of open networking for your customers. Included in the updated software are lifecycle Management (LCM) capabilities that enable NetQ to deliver upgrade and configuration management with push button simplicity.

Upgrade paths include:

- NetQ 2.4.x to NetQ 3.1.0
- NetQ 3.0.0 to NetQ 3.1.0

Upgrades from NetQ 2.3.x and earlier require a fresh installation.

**Cumulus NetQ 3.1.0** includes the following new features and improvements:

- {{<link url="Lifecycle-Management" text="Lifecycle Management">}}
    - Simple NetQ UI workflow to install or upgrade Cumulus NetQ (Agent and CLI) on monitored switches
    - Discover or import Cumulus Linux switches without NetQ running for NetQ installation
    - Create NetQ configuration profile
    - Select protocols and services to include in network snapshot
    - Software upgrade available for cloud deployments on request
- Events
    - Digital optics module monitoring support ({{<link url="Monitor-Network-Elements/#view-digital-optics" text="NetQ UI">}}, {{<link url="Monitor-Physical-Layer-Components/#view-digital-optics" text="NetQ CLI">}})
    - {{<link url="Integrate-NetQ-with-Notification-Applications/#create-an-email-channel" text="Email notification">}} of user-selected events configurable through NetQ CLI
    - {{<link url="Integrate-NetQ-with-Notification-Applications/#suppress-events" text="Event suppression">}} for user-selected message types configurable through NetQ CLI
- Access
    - Password change required on first login to NetQ UI
    - Password policy implemented and enforced for NetQ UI
    - Login required for Admin UI
    - User lockout after three failed login attempts to NetQ Cloud
- NetQ Agent CPU usage limitation support extended to all Cumulus Linux 3.6 and 3.7 releases
- APIs
    - Validation and trace support

For information regarding bug fixes and known issues present in this release, refer to the {{<link title="Cumulus NetQ 3.1 Release Notes" text="release notes">}}.
