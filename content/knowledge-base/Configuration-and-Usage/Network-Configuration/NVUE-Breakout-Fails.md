---
title: NVUE Fails to Apply Configuration After Upgrade
weight: 306
draft: true
---

## Issue

When you apply an NVUE configuration after upgrade to Cumulus Linux 5.4.0 or later from a previous release, the apply fails with a message indicating breakout syntax is invalid:

```
cumulus@switch:~$ nv config apply
Invalid config [rev_id: 4]
  Config invalid at interface.swp1.link.breakout: '4x10G' is not of type 'object'
```

## Environment

This issue is observed when all of the following conditions are true:

- You upgrade to Cumulus Linux 5.4.0 from a previous Cumulus Linux release with `apt upgrade`.

- In the previous release, you configured breakout ports with NVUE.

- You did not {{<kb_link latest="cl" url="Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes.md#important-upgrade-information-for-breakout-ports-and-nvue" text="change the breakout port configuration syntax to the new version">}} introduced with Cumulus Linux 5.4.0 before you upgraded with `apt upgrade`.

## Solution

To resolve this issue:

1. Remove the breakout configuration for every port:

{{%notice note%}}
You must also unset the link breakout configuration from ports set to `link breakout disabled`.
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