---
title: ifplugd
author: NVIDIA
weight: 310
toc: 4
---
`ifplugd` is an Ethernet link-state monitoring daemon that executes scripts to configure an Ethernet device when you plug in or remove a cable. Follow the steps below to install and configure the `ifplugd` daemon.

## Install ifplugd

You can install this package even if the switch does not connect to the internet. The package is in the `cumulus-local-apt-archive` repository on the {{<link url="Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" text="Cumulus Linux image">}}.

To install `ifplugd`:

1. Update the switch before installing the daemon:

    ```
    cumulus@switch:~$ sudo -E apt-get update
    ```

2. Install the `ifplugd` package:

    ```
    cumulus@switch:~$ sudo -E apt-get install ifplugd
    ```

## Configure ifplugd

After you install `ifplugd`, you must edit two configuration files:

- `/etc/default/ifplugd`
- `/etc/ifplugd/action.d/ifupdown`

The example configuration below configures `ifplugd` to bring down all uplinks when the peer bond goes down in an MLAG environment.

1. Open `/etc/default/ifplugd` in a text editor and configure the file as appropriate. Add the `peerbond` name before you save the file.

    ```
    INTERFACES="peerbond"
    HOTPLUG_INTERFACES=""
    ARGS="-q -f -u0 -d1 -w -I"
    SUSPEND_ACTION="stop"
    ```

2. Open the `/etc/ifplugd/action.d/ifupdown` file in a text editor. Configure the script, then save the file.

    ```
    #!/bin/sh
    set -e
    case "$2" in
    up)
            clagrole=$(clagctl | grep "Our Priority" | awk '{print $8}')
            if [ "$clagrole" = "secondary" ]
            then
                #List all the interfaces below to bring up when clag peerbond comes up.
                for interface in swp1 bond1 bond3 bond4
                do
                    echo "bringing up : $interface"  
                    ip link set $interface up
                done
            fi
        ;;
    down)
            clagrole=$(clagctl | grep "Our Priority" | awk '{print $8}')
            if [ "$clagrole" = "secondary" ]
            then
                #List all the interfaces below to bring down when clag peerbond goes down.
                for interface in swp1 bond1 bond3 bond4
                do
                    echo "bringing down : $interface"
                    ip link set $interface down
                done
            fi
        ;;
    esac
    ```

3. Restart the `ifplugd` daemon to implement the changes:

    ```
    cumulus@switch:~$ sudo systemctl restart ifplugd.service
    ```

## Considerations

The default shell for `ifplugd` is `dash` (`/bin/sh`) instead of `bash`, as it provides a faster and more nimble shell. However, `dash` contains fewer features than `bash` (for example, `dash` is unable to handle multiple uplinks).
