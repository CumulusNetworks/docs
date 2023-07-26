---
title: Using dtach for In-band apt-get Upgrades
author: NVIDIA
weight: 293
toc: 4
---

## Issue
<!-- vale off -->
My SSH session was terminated while performing an in-band upgrade.
<!-- vale on -->
## Environment

- Cumulus Linux, all versions
- In-band SSH connection: upgrading via SSH connection over a logical (bridge or bond) or switch (swp) port, rather than the management eth0 port

## Root Cause

Upgrades involving certain packages, such as switchd or FRR/Quagga, might result in a temporary loss of in-band SSH connections (generally a minute or two) to the switch.

## Resolution

When upgrading in-band, NVIDIA recommends running the upgrade with the `dtach` or `screen` command. This makes it possible to re-attach to the upgrade process in the event of an interrupted connection.

### Using dtach

    cumulus@switch$ sudo apt-get update
    cumulus@switch$ dtach -c /tmp/apt-get -z sudo apt-get upgrade

Where:

- `/tmp/apt-get` is a socket to re-attach later
- `-z` disables the suspend key from suspending `dtach`

To re-attach to the `apt-get` process after reconnecting to the switch:

    cumulus@switch$ dtach -a /tmp/apt-get

If the `dtach` socket file does not exist as in the following error:

    cumulus@switch$ dtach -a /tmp/apt-get
    dtach: /tmp/apt-get: No such file or directory

Then the upgrade is complete. Before rebooting (if needed) you can review the results of the upgrade in `/var/log/apt/term.log`:

    cumulus@switch$ less /var/log/apt/term.log

### Using screen

Start a `screen` session specifying a name to re-attach to later:

    screen -S apt-get

In the new `screen` session, proceed with the upgrade process:

    cumulus@switch$ sudo apt-get update
    cumulus@switch$ sudo apt-get upgrade

To re-attach to the `apt-get` process after reconnecting to the switch:

    screen -r apt-get
