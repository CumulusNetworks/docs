---
title: VirtualBox and Vagrant
author: Cumulus Networks
weight: 35
---
This section describes how to install and set up Cumulus VX within VirtualBox and Vagrant to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with Cumulus VX 4.2, VirtualBox version 6.1.12, and Vagrant version 2.2.9 on macOS version 10.14.6.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have Vagrant, VirtualBox, and Linux experience.

### Download and Install the Software

1. Download and install {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox">}}.

2. Download and install {{<exlink url="https://www.vagrantup.com/downloads.html" text="Vagrant">}}.

### Create VMs and Network Connections

{{% notice note %}}

The Cumulus VX box image defines the CPU, memory and disk requirements. Cumulus VX requires at least 768MB of RAM and 6GB of disk space.

{{% /notice %}}

{{% vx/vagrant-setup %}}

## Log into the Switches

{{% vx/login-vagrant %}}

## Basic Switch Configuration

{{% vx/basic-config-vagrant %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
