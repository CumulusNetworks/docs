---
title: Upgrading Cumulus Linux
author: Cumulus Networks
weight: 45
pageID: 8362647
---
This topic describes how to upgrade Cumulus Linux on your switches to a more recent release.

Cumulus Networks recommends that you deploy, provision, configure, and upgrade switches using automation, even with small networks or test labs. During the upgrade process, you can quickly upgrade dozens of devices in a repeatable manner. Using tools like Ansible, Chef, or Puppet for configuration management greatly increases the speed and accuracy of the next major upgrade; these tools also enable the quick swap of failed switch hardware.

## Before You Upgrade Cumulus Linux

{{%notice tip%}}

Be sure to read the knowledge base article [Upgrades: Network Device and Linux Host Worldview Comparison]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Network-Device-and-Linux-Host-Worldview-Comparison" >}}), which provides a detailed comparison between the network device and Linux host worldview of upgrade and installation.

{{%/notice%}}
