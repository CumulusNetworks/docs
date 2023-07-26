---
title: portwd invalid SFF identifier Error
author: NVIDIA
weight: 336
toc: 4
---

## Issue

The following log messages constantly appear in `/var/log/syslog`:

    2017-03-16T00:39:30.292349+00:00 hostname portwd: Port 49, invalid SFF identifier: 0x0c
    2017-03-16T00:39:30.298340+00:00 hostname portwd: Port 50, invalid SFF identifier: 0x0c
    2017-03-16T00:39:30.300035+00:00 hostname portwd: Port 50, invalid SFF identifier: 0x0c
    2017-03-16T00:39:30.301740+00:00 hostname portwd: Port 50, invalid SFF identifier: 0x0c
    2017-03-16T00:39:30.303486+00:00 hostname portwd: Port 50, invalid SFF identifier: 0x0c
    2017-03-16T00:39:30.309608+00:00 hostname portwd: Port 51, invalid SFF identifier: 0x0c

## Environment

- Cumulus Linux 3.y.z

## Cause

This issue occurs because `portwd` is unable to correctly identify the optic. This is usually because the optic has not correctly identified its capabilities.

Here is an example of `ethtool` output showing a correctly identified optic:

    cumulus@switch:~$ sudo ethtool -m swp1
            Identifier                                : 0x0d (QSFP+)
            Extended identifier                       : 0x00 (1.5W max. Power consumption, No CDR in TX, No CDR in RX)
            Connector                                 : 0x0c (MPO Parallel Optic)
            Transceiver codes                         : 0x04 0x00 0x00 0x00 0x40 0x40 0x02 0x00
            Transceiver type                          : 40G Ethernet: 40G Base-SR4
            Transceiver type                          : FC: short distance (S)
            Transceiver type                          : FC: Shortwave laser w/o OFC (SN)
            Transceiver type                          : FC: Multimode, 50um (OM3)

Here is an example of `ethtool` output showing an optic that has not identified its capabilities:

    cumulus@switch:~$ sudo ethtool -m swp29
            Identifier                                : 0x0d (QSFP+)
            Extended identifier                       : 0xdc (3.5W max. Power consumption, CDR present in TX, CDR present in RX)
            Connector                                 : 0x07 (LC)
            Transceiver codes                         : 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00
            Encoding                                  : 0x05 (64B/66B)

## Resolution

If you encounter this message and believe the optic is not behaving as expected, then {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Cumulus support team">}}.

## Suppressing Log Messages

The "Invalid SFF Identifer" log message generates constantly in your `/var/log/syslog`, making it harder to interpret other log messages. You can prevent the logging of this message by adding the following line to your `rsyslog` configuration:

    :msg, contains, "invalid SFF identifier:" ~

You need to add this configuration before the system defines the `/var/log/syslog` file. The simplest way to do this is to create a file named `/etc/rsyslogd.d/1-suppress.conf` and put the entry in this file:

1.  Create the file:  

        cumulus@switch:~$ sudo vi /etc/rsyslog.d/1-suppress.conf

2.  Add the following line to the file:  

        :msg, contains, "invalid SFF identifier:" ~

3.  Restart `rsyslogd`:  

        cumulus@switch:~$ sudo systemctl restart rsyslog.service
