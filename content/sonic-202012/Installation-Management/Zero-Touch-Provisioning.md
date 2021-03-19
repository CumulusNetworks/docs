---
title: Zero Touch Provisioning
author: Cumulus Networks
weight: 210
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

*Zero touch provisioning* (ZTP) enables you to deploy network devices quickly in large-scale environments. On first boot, SONiC invokes ZTP, which executes the provisioning automation used to deploy the device for its intended role in the network.

The provisioning framework allows for a one-time, user-provided script to be executed. You can develop this script using a variety of automation tools and scripting languages, providing ample flexibility for you to design the provisioning scheme to meet your needs. You can also use it to add the switch to a configuration management (CM) platform such as {{<exlink url="http://puppet.com/" text="Puppet">}}, {{<exlink url="https://www.chef.io/" text="Chef">}}, {{<exlink url="https://cfengine.com/" text="CFEngine">}} or possibly a custom, proprietary tool.

ZTP can execute automatically in one of the following ways, in this order:

- Through a local file
- Using a USB drive inserted into the switch (ZTP-USB)
- Through DHCP


Example in the blog: https://developer.nvidia.com/blog/building-pure-sonic-image/

## Use a Local File

## Use a USB Drive

## ZTP over DHCP

## Example ZTP Script
