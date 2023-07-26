---
title: Monitor Interface Administrative State and Physical State on Cumulus Linux
author: NVIDIA
weight: 373
toc: 4
---

## Issue

Logging is useful for determining:

- Admin state (whether the port/bridge/bond up or down)
- Physical state (whether the connection for the port/bridge/bond up or down)

When the current level is not enough in `/var/log/`.

## Environment

- Cumulus Linux, all versions

## Resolution

### Utilizing ip monitor

Use the Linux `ip monitor` tool to monitor link state.

    cumulus@switch:~$ ip -timestamp monitor link

- The `-timestamp` command allows you to timestamp each message
- The `link` keyword specifies to only pay attention to link changes

### Running in the Background

What if you want to run it in the background and redirect it to a log?

Cumulus Linux is Linux so use the `&` and `>` to redirect the output:

    cumulus@switch:~$ sudo sh -c "ip -timestamp monitor link > /var/log/link.log" &

The redirect (\>) in the previous example requires you to use the quotation marks around the two commands subjected to the redirection clause (\>) so that the root user runs both commands. If using the root account (disabled by default on Cumulus Linux 2.0 and later) there is no need:

    root@switch:~# ip -timestamp monitor link > /var/log/link.log &

### Automatically Logging on Boot

What if you automatically want to log link activity, even if the switch reboots?

Utilize the `rc.local` startup script located at `/etc/rc.local`. Here `rc.local` is already configured on a Cumulus Linux switch:

    cumulus@switch:~$ cat /etc/rc.local
    #!/bin/sh -e
    #
    # rc.local
    #
    # This script is executed at the end of each multiuser runlevel.
    # Make sure that the script will "exit 0" on success or any other
    # value on error.
    #
    # In order to enable or disable this script just change the execution
    # bits.
    #
    # By default this script does nothing.
    ip -timestamp monitor link > /var/log/link.log
    
    exit 0

    cumulus@switch:~$

### Looking at the Log Output

What does admin state versus physical state look like in the log?

To see the difference, turn a port off and on and look at the log.

    cumulus@switch:~$ sudo ip link set swp1 down

    cumulus@switch:~$ sudo ip link set swp1 up

    cumulus@switch:~$ cat /var/log/link.log
    Timestamp: Wed Jul 16 19:00:35 2014 350805 usec
    3: swp1: <BROADCAST,MULTICAST,SLAVE> mtu 1500 qdisc pfifo_fast master bond24 state DOWN
        link/ether 44:38:39:00:25:d9 brd ff:ff:ff:ff:ff:ff
    Timestamp: Wed Jul 16 19:00:37 2014 840831 usec
    3: swp1: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 1500 qdisc pfifo_fast master bond24 state DOWN
        link/ether 44:38:39:00:25:d9 brd ff:ff:ff:ff:ff:ff

### /var/log/linkstate

Cumulus Linux provides a link state log, that outputs to `/var/log/linkstate`, and provides concise records of all physical and logical network link state changes. In particular, the output shows up/down changes, for both physical and admin links.

This log exists because link state changes occur far less often than other logged events, and a separate log ensures the recording of link state changes for a longer period of time, as the information does not rotate out with the rest of `syslog`.

    cumulus@leaf01:mgmt-vrf:~$ sudo tail /var/log/linkstate
    2017-05-22T11:21:07.085595-04:00 leaf01 switchd[19517]: sync_base.c:596 swp51: ifindex 54, admin down
    2017-05-22T11:21:07.086167-04:00 leaf01 switchd[19517]: sync_base.c:604 swp51: ifindex 54, oper down
    2017-05-22T11:21:07.153894-04:00 leaf01 switchd[19517]: nic.c:223 nic_set_carrier: swp51: setting kernel carrier: down
    2017-05-22T11:23:02.968972-04:00 leaf01 switchd[19517]: sync_base.c:596 swp51: ifindex 54, admin up
    2017-05-22T11:23:05.152445-04:00 leaf01 switchd[19517]: nic.c:223 nic_set_carrier: swp51: setting kernel carrier: up
    2017-05-22T11:23:05.165747-04:00 leaf01 switchd[19517]: sync_base.c:604 swp51: ifindex 54, oper up
    2017-05-22T11:23:06.683631-04:00 leaf01 switchd[19517]: sync_base.c:596 swp51: ifindex 54, admin down
    2017-05-22T11:23:06.684531-04:00 leaf01 switchd[19517]: sync_base.c:604 swp51: ifindex 54, oper down
    2017-05-22T11:23:06.723817-04:00 leaf01 switchd[19517]: nic.c:223 nic_set_carrier: swp51: setting kernel carrier: down

### Admin/Physical State Troubleshooting Table

Now look at every possible scenario to make troubleshooting easier.

| Admin State | Physical State | ip link show Output |
| ----------- | -------------- | ------------------- |
| up          | up             | `swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500`  |
| up          | down           | `swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500`  |
| down        | up             | `swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500` |
| down        | down           | `swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500` |

{{%notice info%}}

Notice how Admin down (down/up above) and down/down look identical.

{{%/notice%}}

For additional troubleshooting of physical ports, read the documentation on [duplex, speed and auto-negotiation settings]({{<ref "/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes" >}}).
