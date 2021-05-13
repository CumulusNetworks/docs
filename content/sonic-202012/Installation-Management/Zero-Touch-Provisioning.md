---
title: Zero Touch Provisioning
author: NVIDIA
weight: 210
product: SONiC
version: 202012
siteSlug: sonic
---

*Zero touch provisioning* (ZTP) enables you to deploy network devices quickly in large-scale environments. On first boot, SONiC invokes ZTP, which executes the provisioning automation used to deploy the device for its intended role in the network.

The provisioning framework allows for a one-time, user-provided script to be executed. You can develop this script using a variety of automation tools and scripting languages, providing ample flexibility for you to design the provisioning scheme to meet your needs. You can also use it to add the switch to a configuration management (CM) platform such as {{<exlink url="http://puppet.com/" text="Puppet">}}, {{<exlink url="https://www.chef.io/" text="Chef">}}, {{<exlink url="https://cfengine.com/" text="CFEngine">}} or possibly a custom, proprietary tool.

The ZTP service (`ztp.service`) is a `systemd` service that runs natively in SONiC; it does not run inside a container. ZTP is enabled by default, which allows for ZTP to run before SONiC is installed.

ZTP can execute automatically in one of the following ways, in this order:

1. A local ZTP JSON file called `/host/ztp/ztp_local_data.json`.
1. A ZTP JSON URL specified via DHCP option 67.
1. A ZTP JSON URL constructed using DHCP option 66 TFTP server name, DHCP option 67 file path on TFTP server.
1. A ZTP JSON URL specified via DHCPv6 option 59.
1. A provisioning script URL specified via DHCP option 239.
1. A provisioning script URL specified via DHCPv6 option 239.

You can learn about the DHCP options in the {{<exlink url="https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md#34-dhcp-options" text="Azure GitHub">}} documentation.

## Configure ZTP

The {{<exlink url="https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md#6-configuring-ztp" text="Azure GitHub documentation">}} has detailed instructions on configuring ZTP.

## Enable and Disable ZTP

ZTP is enabled by default, which allows for ZTP to run before SONiC is installed. If you need to disable ZTP, run:

    admin@leaf01:~$ sudo config ztp disable
    admin@leaf01:~$ sudo config save -y

To enable ZTP again, run either `config ztp enable` or `config ztp run -y`:

    admin@leaf01:~$ sudo config ztp enable
    admin@leaf01:~$ sudo config save -y

## Manually Run ZTP

You can use the `config ztp run` command to manually start a new ZTP session after the session has failed for one reason or another, or if ZTP was disabled.

This command deletes the existing `/etc/sonic/config_db.json` file and starts the ZTP service. It also erases the previous ZTP session data. The ZTP configuration is loaded on to the switch and ZTP discovery is performed.

## Check ZTP

https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md

## Use a Local File

```
admin@switch:~$ sudo show ztp status
ZTP Admin Mode : True
ZTP Service    : Inactive
ZTP Status     : SUCCESS
ZTP Source     : dhcp-opt67 (eth0)
Runtime        : 05m 31s
Timestamp      : 2019-09-11 19:12:24 UTC

ZTP Service is not running

01-configdb-json: SUCCESS
02-connectivity-check: SUCCESS
```

The `--verbose` option displays very detailed information.

```
admin@switch:~$ sudo  show ztp status --verbose
Command: ztp status --verbose
========================================
ZTP
========================================
ZTP Admin Mode : True
ZTP Service    : Inactive
ZTP Status     : SUCCESS
ZTP Source     : dhcp-opt67 (eth0)
Runtime        : 05m 31s
Timestamp      : 2019-09-11 19:12:16 UTC
ZTP JSON Version : 1.0

ZTP Service is not running

----------------------------------------
01-configdb-json
----------------------------------------
Status          : SUCCESS
Runtime         : 02m 48s
Timestamp       : 2019-09-11 19:11:55 UTC
Exit Code       : 0
Ignore Result   : False

----------------------------------------
02-connectivity-check
----------------------------------------
Status          : SUCCESS
Runtime         : 04s
Timestamp       : 2019-09-11 19:12:16 UTC
Exit Code       : 0
Ignore Result   : False
```

You can also use systemd to check the status of the ZTP service:

```
admin@switch:~$ sudo systemctl status ztp.service
● ztp.service - SONiC Zero Touch Provisioning service
   Loaded: loaded (/lib/systemd/system/ztp.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Thu 2020-12-03 14:55:23 UTC; 3 months 25 days ago
 Main PID: 3047 (code=exited, status=0/SUCCESS)
      CPU: 11min 28.067s

Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.
```

## Example ZTP Script

You can find a working example script on the {{<exlink url="https://developer.nvidia.com/blog/building-pure-sonic-image/" text="NVIDIA blog">}}. In addition, the {{<exlink url="https://github.com/Azure/SONiC/blob/master/doc/ztp/ztp.md#10-examples" text="Azure GitHub documentation">}} has many examples and suggested usage.
