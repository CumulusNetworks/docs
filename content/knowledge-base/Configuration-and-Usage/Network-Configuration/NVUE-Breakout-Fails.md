---
title: NVUE Fails to Apply Configuration After Upgrade
weight: 306
draft: true
---

## Issue

When you apply an NVUE configuration after upgrade to Cumulus Linux 5.4.0 or later from a prior version, the apply fails with a message indicating breakout syntax is invalid:

```
"Invalid config [rev_id: 2]
Config invalid at interface.swp9.link.breakout: '4x10G' is not of type 'object'"
```

## Environment

This issue is observed when all of the following conditions are true:

- You perform an `apt upgrade` of Cumulus Linux from a version prior to 5.4.0.

- You had breakout ports configured with NVUE.

- You did not {{<kb_link latest="cl" url="Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes.md#important-upgrade-information-for-breakout-ports-and-nvue" text="change the breakout port configuration syntax to the new version">}} introduced with Cumulus Linux 5.4 prior to `apt upgrade`.

## Solution

To resolve this issue:

1. Remove the breakout configuration for every port, and reapply the configuration with the new syntax:

{{%notice note%}}
It is also required to unset the link breakout configuration from ports that were set to disabled.
{{%/notice%}}

```
nv unset interface swp1 link breakout
nv unset interface swp2 link breakout
nv unset interface swp3 link breakout
nv unset interface swp4 link breakout
...
nv config apply
```

2. Apply the breakout configuration again using the {{<kb_link latest="cl" url="Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes.md/#configure-a-breakout-port" text="supported syntax in Cumulus Linux 5.4.0">}}:

```
nv set interface swp1 link breakout 4x
nv set interface swp2 link breakout disabled
nv set interface swp3 link breakout 4x
nv set interface swp4 link breakout disabled
...
nv config apply
```