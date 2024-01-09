---
title: Licensing in Cumulus Linux 4.4 and Later
author: NVIDIA
weight: 252
toc: 4
---

In NVIDIA Cumulus Linux 4.4 and later, you no longer need a specific software license key to enable the `switchd` service. In earlier Cumulus Linux releases, the `switchd` service fails to start and the switch ports are inoperable if you do *not* install a license key.

This knowledge base article answers some frequently asked questions.
<!-- vale off -->
## What different behavior should I expect?
<!-- vale on -->
When you install Cumulus Linux 4.4 or later on an NVIDIA Spectrum switch, the ASIC runs and you can configure the front-panel ports without additional requirements. Cumulus Linux no longer includes the `cl-license` command on the system and returns a `command not found` error message if you run the command.

## Is Cumulus Linux no longer licensed?

You still need to purchase Cumulus Linux when purchasing an NVIDIA Spectrum switch. Purchasing Cumulus Linux grants you the right to install and use the product. This just removes the additional step of copying the license to the individual switch.
<!-- vale off -->
## Is only one copy of Cumulus Linux required for all my switches?
<!-- vale on -->
No. A single purchase of Cumulus Linux entitles you to install Cumulus Linux on a single switch. You must purchase a copy of Cumulus Linux for each NVIDIA Spectrum switch on which you intend to install the Cumulus Linux software. Failure to do so is a violation of the licensing agreement.
<!-- vale off -->
## What does this mean for my NVIDIA Spectrum switches running an earlier Cumulus Linux release?
<!-- vale on -->
In Cumulus Linux 4.4 and later, you are no longer required to install a license key. You might need to adjust your Zero Touch Provisioning or automation processes because the `cl-license` command no longer exists. This does not change the number of licenses you own or their validity.
<!-- vale off -->
## Is support still required when I purchase Cumulus Linux?
<!-- vale on -->
Support is still required when you purchase a switch with Cumulus Linux software.
<!-- vale off -->
## For Spectrum switches purchased with Onyx or as ONIE switches, do I need a license to run Cumulus Linux?
<!-- vale on -->
You still need to purchase a license and support to run Cumulus Linux on a switch that is not sold with Cumulus Linux.
