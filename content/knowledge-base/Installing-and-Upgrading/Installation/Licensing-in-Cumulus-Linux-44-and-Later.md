---
title: Licensing in Cumulus Linux 4.4 and Later
author: Cumulus Networks
weight: 252
toc: 4
---
In NVIDIA Cumulus Linux 4.4 and later, you no longer need a specific software license key to enable the `switchd` service. In earlier Cumulus Linux releases, the `switchd` service fails to start and the switch ports are inoperable if you do *not* install a license key.

This knowledge base article answers some frequently asked questions.

## What different behavior should I expect?

When you install Cumulus Linux 4.4 or later on an NVIDIA Spectrum switch, the ASIC runs and you can configure the front-panel ports without additional requirements. Cumulus Linux no longer includes the `cl-license` command on the system and returns a `command not found` error message if you run the command.

## Is Cumulus Linux no longer licensed?

You still need to purchase Cumulus Linux when purchasing an NVIDIA Spectrum switch. Purchasing Cumulus Linux grants you the right to install and use the product. This simply removes the additional step of copying the license to the individual switch.

## Is only one copy of Cumulus Linux required for all of my switches?

No. A single purchase of Cumulus Linux entitles you to install Cumulus Linux on a single switch. You must purchase a copy of Cumulus Linux for each NVIDIA Spectrum switch on which you intend to install the Cumulus Linux software. Failure to do so is a violation of the licensing agreement.

## What does this mean for my NVIDIA Spectrum switches running an earlier Cumulus Linux release?

In Cumulus Linux 4.4 and later, you are no longer required to install a license key. You might need to adjust your Zero Touch Provisioning or automation processes because the `cl-license` command no longer exists. This does not change the number of licenses you own or their validity.

## Is support still required when Cumulus Linux is purchased?

Support is still required when you purchase a switch with Cumulus Linux software.

## For Spectrum switches purchased with Onyx or as ONIE switches, do I need a license to run Cumulus Linux?

You still need to purchase a license and support to run Cumulus Linux on a switch that is not sold with Cumulus Linux.

## Will ZTP be supported on front panel ports?

Not today because the default configuration is not changing. The front panel ports do not participate in DHCP by default, preventing them from accessing a ZTP script.
