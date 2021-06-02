---
title: Monitoring and Troubleshooting
author: NVIDIA
weight: 600
product: SONiC
version: 202012
siteSlug: sonic
---

SONiC provides a number of ways to troubleshoot a network switch. Many of them should be familiar to someone who administers Linux systems and containers.

## syslog

All SONiC logs are available at `/var/log/syslog`.

To add a link to the `syslog` server, run:

    admin@switch:~$ sudo config syslog add <IP address>

You can link to more that one `syslog` server from a switch.

To delete the `syslog` server link from the switch, run:

    admin@sonic:~$ sudo config syslog delete <IP address>

Adding or deleting the `syslog` link restarts  the `rsyslog-config` service.

To change the logging level for a component, use the `swssloglevel` utility. Here are some example changes you can make.

To set the `orchagent` severity level to NOTICE, run:

    admin@switch:~$ swssloglevel -l NOTICE -c orchagent

To set SAI_API_SWITCH severity to ERROR:

    admin@switch:~$ swssloglevel -l SAI_LOG_LEVEL_ERROR -s -c SWITCH

To set all SAI_API_* severity to DEBUG:

    admin@switch:~$ swssloglevel -l SAI_LOG_LEVEL_DEBUG -s -a

## Docker Status

To verify that all Docker containers are running:

    admin@switch:~$ docker ps

To verify that all processes are running in a container, run:

    admin@switch:~$ sudo docker exec -it CONTAINER supervisorctl status

Containers are started by `systemd`, so you can use `systemctl` to get the status of a container service. For example to get the status of the `swss` service:

    admin@switch:~$ systemctl status swss.service

If a Docker container is not running:

1. Check whether all services are running.

       admin@switch:~$ systemctl status

       ● mlx-2100-06
           State: degraded
            Jobs: 0 queued
          Failed: 3 units
           Since: Thu 2020-12-03 01:23:32 UTC; 3 months 20 days ago
          CGroup: /
                  ├─docker
                  │ ├─3c95f59e99b5c350cdd097e2a5abb5609ff0986731f103d51e96dad67afcc4b2
                  │ │ ├─4234 /usr/bin/python /usr/bin/supervisord
                  │ │ ├─4902 python /usr/bin/supervisor-proc-exit-listener --container-name radv
                  │ │ └─5064 /usr/sbin/rsyslogd -n -iNONE
                  │ ├─64bbae35104cac9e2c5c4f01b00f5217f4f83ee4a51b648322841bf8918aed13
                  │ │ ├─2207 /usr/bin/python /usr/bin/supervisord
                  │ │ ├─2373 python /usr/bin/supervisor-proc-exit-listener --container-name database
                  │ │ ├─2374 /usr/sbin/rsyslogd -n -iNONE
                  │ │ └─2375 /usr/bin/redis-server 127.0.0.1:6379
            ...

2. Check `/var/log/syslog` for errors.
3. Restart the SONiC service that failed. For example, if you need to restart the `swss` service, run:

       admin@switch:~$ sudo systemctl restart swss.service

## System Dump

The `show techsupport` command generates a dump of the operating system for debugging purposes, including `syslog` entries, database state and routing stack state. After the command is run, it compresses all the information into an archive file called `/var/dump/<DEVICE_HOST_NAME>_YYYYMMDD_HHMMSS.tar.gz`. You can send this archive file to the SONiC development team for examination.

If you need to report an issue, you must include a system dump. The information can assist in reproducing the issue and analyzing it offline.

To generate a system dump, run:

```
admin@leaf01:~$ show techsupport
...
/var/dump/sonic_dump_leaf01_20201118_140851.tar:         88.1% -- replaced with /var/dump/sonic_dump_leaf01_20201118_140851.tar.gz
/var/dump/sonic_dump_leaf01
```

A system dump includes the following information:

- State of `/proc` file system
- Platform information, including version, hostname and more
- System configuration, including interfaces, routes and BGP
- System information, including running processes, memory and disk utilization
- Redis DB instances dump
- SAI attributes dump
- Log files
- Core dump files
- Platform-specific files

{{%notice tip%}}

On NVIDIA Spectrum switches, the system dump also includes the SDK dump, firmware trace and MST (Mellanox Software Tools) dump.

{{%/notice%}}

## Hardware Troubleshooting

To check system memory, run:

```
admin@switch:~$ show system-memory 
              total        used        free      shared  buff/cache   available
Mem:           7950        1205        4572         111        2172        6331
Swap:             0           0           0
```

## What Just Happened

If you are running SONiC on an NVIDIA Spectrum switch, you can use the {{<link url="What-Just-Happened">}} feature to provide real-time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, and ACL or layer 1 problems.

There are also some Mellanox platform-specific {{<link title="Mellanox Debug Tools for SONiC" text="debug tools">}}.
