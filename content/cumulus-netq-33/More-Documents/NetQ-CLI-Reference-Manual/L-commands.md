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

    add      :  Add netq tca configuration
    del       :  Delete netq tca configuration
    discover  :  Perform switch discovery operation
    show      :  Show fabric-wide info about specified object
    upgrade   :  Upgrade NetQ


    netq lcm add cl-image <text-image-path>
    netq lcm add credentials username <text-switch-username> (password <text-switch-password> | ssh-key <text-ssh-key>)
    netq lcm add default-version cl-images <text-cumulus-linux-version>
    netq lcm add default-version netq-images <text-netq-version>
    netq lcm add netq-image <text-netq-image-path>
    netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
    netq lcm del cl-image <text-image-id>
    netq lcm del credentials
    netq lcm del netq-image <text-image-id>
    netq lcm discover (ip-range <text-ip-range> | csv-file <text-csv-file-path>)
    netq lcm show cl-images [<text-image-id>] [json]
    netq lcm show credentials [json]
    netq lcm show default-version cl-images [json]
    netq lcm show default-version netq-images [json]
    netq lcm show discovery-job <text-discovery-job-id> [json]
    netq lcm show netq-config [json]
    netq lcm show netq-images [<text-netq-image-id>] [json]
    netq lcm show status cl-image <text-lcm-job-id> [json]
    netq lcm show status netq-image <text-netq-upgrade-job-id> [json]
    netq lcm show switches [cl-version <text-cumulus-linux-version>] [netq-version <text-netq-version>] [json]
    netq lcm show upgrade-jobs cl-image [json]
    netq lcm show upgrade-jobs netq-image [json]
    netq lcm upgrade [cl-image] name <text-job-name> cl-version <text-cumulus-linux-version> netq-version <text-netq-version> hostnames <text-switch-hostnames> [run-restore-on-failure] [run-before-after]
    netq lcm upgrade netq-image name <text-job-name> [netq-version <text-netq-version>] [upgrade-cli True | upgrade-cli False] hostnames <text-switch-hostnames> [config_profile <text-config-profile>]
