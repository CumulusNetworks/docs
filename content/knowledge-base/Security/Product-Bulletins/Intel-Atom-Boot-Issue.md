---
title: Intel Atom Boot Issue
author: Cumulus Networks
weight: 432
toc: 4
---

## Issue

The switch fails to power up; there is no console output.

This issue was reported as Cumulus Networks Product Bulletin 2017-02-08.

## Environment

This issue may affect the following switches on the Cumulus Networks {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="hardware compatibility list">}}:

- 100G switches: Dell Z9100-ON, Edge-Core AS7712-32X, HPE Altoline 6960, Mellanox SN2100, Penguin Arctica 3200C, QCT QuantaMesh BMS T7032-IX1, Supermicro SSE-C3632S
- 40G switches: Dell S6010-ON, Edge-Core AS6712-32X, Edge-Core AS6812-32X, HPE Altoline 6940, HPE Altoline 6941, Mellanox SN2100B, Penguin Arctica 3200XLP, QCT QuantaMesh BMS T5032-LY6-x86
- 10G switches: Dell S4048-ON, Dell S4048T-ON, Edge-Core AS5712-54X, Edge-Core AS5812-54T, Edge-Core AS5812-54X, HPE Altoline 6920, HPE Altoline 6921, HPE Altoline 6921T, Penguin Arctica 4806XP, QCT QuantaMesh BMS T3048-LY8, QCT QuantaMesh BMS T3048-LY9, Supermicro SSE-X3648S
- 1G switches: Dell S3048-ON, Penguin Arctica 4804iq, Supermicro SSE-G3648B

## Root Cause

The CPU may fail to boot after the SoC LPC\_CLKOUT0 and/or LPC\_CLKOUT1 signals (low pin count bus clock outputs) stops functioning. For more information, please read AVR54 in the {{<exlink url="http://www.intel.com/content/dam/www/public/us/en/documents/specification-updates/atom-c2000-family-spec-update.pdf" text="Intel Atom Processor C2000 Product Family Specification Update from January 2017">}}.

If this issue occurs, there will be no messages or output on the serial console, the switch fans continue to run at full speed, and the state (on/off/color) of the LEDs will all remain the same.

{{%notice note%}}

This article will be updated as new information arises.

{{%/notice%}}

## Resolution

In the event that the switch fails to boot under the circumstances described above, Cumulus Networks recommends that you contact:

- The {{<exlink url="https://support.mellanox.com/s/contact-support-page" text="NVIDIA Cumulus support team">}} to make them aware of your situation, and,
- Your hardware supplier for the appropriate hardware warranty service.
