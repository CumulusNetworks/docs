---
title: Using dtach for In-band apt-get Upgrades
author: NVIDIA
weight: 293
toc: 4
---

## Issue

My SSH session was terminated while performing an in-band upgrade.

## Environment

- Cumulus Linux, all versions
- In-band SSH connection: upgrading via SSH connection over a logical (bridge or bond) or switch (swp) port, rather than the management eth0 port

## Root Cause

Upgrades involving certain packages, such as switchd or FRR/Quagga, may result in a temporary loss of in-band ssh connections (generally a minute or two) to the switch.

## Resolution

When upgrading in-band, it is recommended to run the upgrade with the `dtach` or `screen` command. This makes it possible to re-attach to the upgrade process in the event the connection is interrupted.

### Using dtach

    cumulus@switch$ sudo apt-get update
    cumulus@switch$ dtach -c /tmp/apt-get -z sudo apt-get upgrade

Where:

- `/tmp/apt-get` is a socket that will be used to re-attach later
- `-z` disables the suspend key from suspending `dtach`

To re-attach to the `apt-get` process after reconnecting to the switch:

    cumulus@switch$ dtach -a /tmp/apt-get

If the `dtach` socket file does not exist as in the following error:

    cumulus@switch$ dtach -a /tmp/apt-get
    dtach: /tmp/apt-get: No such file or directory

... then upgrade has finished. Prior to rebooting (if needed) results of the upgrade can be reviewed in `/var/log/apt/term.log`:

    cumulus@switch$ less /var/log/apt/term.log

### Using screen

Start a `screen` session specifying a name to re-attach to later:

    screen -S apt-get

In the new `screen` session, proceed with the upgrade process:

    cumulus@switch$ sudo apt-get update
    cumulus@switch$ sudo apt-get upgrade

To re-attach to the `apt-get` process after reconnecting to the switch:

    screen -r apt-get
