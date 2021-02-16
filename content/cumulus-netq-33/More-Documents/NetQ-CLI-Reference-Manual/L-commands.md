---
title: L through R Commands
author: NVIDIA
weight: 1105
toc: 3
right_toc_levels: 1
pdfhidden: true
draft: true
---

This topic includes all commands that begin with `netq l*`, `netq m*`, `netq n*`, `netq o*`, `netq p*`, `netq q*`, and `netq r*`.

## netq lcm

cumulus@netq-ts:~$ netq lcm 
    add       :  Add netq tca configuration
    del       :  Delete netq tca configuration
    discover  :  Perform switch discovery operation
    show      :  Show fabric-wide info about specified object
    upgrade   :  Upgrade NetQ
cumulus@netq-ts:~$ netq lcm add 
    cl-image         :  Cumulus Linux Image
    credentials      :  Switch credentials
    default-version  :  add help text
    netq-image       :  NetQ Agent/CLI Image
    role             :  Assign switches as superspine, spine, leaf, or exit
cumulus@netq-ts:~$ netq lcm del 
    cl-image     :  Cumulus Linux Image
    credentials  :  Switch credentials
    netq-image   :  NetQ Agent/CLI Image
cumulus@netq-ts:~$ netq lcm discover 
    csv-file  :  Discovery job input as csv file
    ip-range  :  Discovery job input as ip address range
cumulus@netq-ts:~$ netq lcm show 
    cl-images        :  Cumulus Linux Images
    credentials      :  Switch credentials
    default-version  :  add help text
    discovery-job    :  Get status of discovery job
    netq-config      :  Display NetQ config profiles
    netq-images      :  NETQ Agent/CLI Images
    status           :  Get status on CL/NetQ Upgrade
    switches         :  Switches running Cumulus Linux
    upgrade-jobs     :  Get history of all upgrade jobs
cumulus@netq-ts:~$ netq lcm upgrade 
    cl-image    :  Cumulus Linux Image
    name        :  Validation name
    netq-image  :  NetQ Agent/CLI Image

    netq lcm upgrade name <text-job-name> image-id <text-image-id> license <text-cumulus-license> hostnames <text-switch-hostnames> [order <text-upgrade-order>] [run-before-after]
    netq lcm add credentials (username <text-switch-username> password <text-switch-password> | ssh-key <text-ssh-key>)
    netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
    netq lcm del credentials
    netq lcm show credentials [json]
    netq lcm show switches [version <text-cumulus-linux-version>] [json]
    netq lcm show status <text-lcm-job-id> [json]
    netq lcm add image <text-image-path>
    netq lcm del image <text-image-id>
    netq lcm show images [<text-image-id>] [json]
    netq lcm show upgrade-jobs [json]