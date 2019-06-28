---
title: ifplugd
author: Cumulus Networks
weight: 311
aliases:
 - /display/DOCS/ifplugd
 - /pages/viewpage.action?pageId=8362693
pageID: 8362693
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
`ifplugd` is an Ethernet link-state monitoring daemon, that can execute
user-specified scripts to configure an Ethernet device when a cable is
plugged in, or automatically unconfigure it when a cable is removed.

Follow the steps below to install and configure the `ifplugd` daemon.

## <span>Install ifplugd</span>

1.  Update the switch before installing the daemon:
    
        cumulus@switch:~$ sudo -E apt-get update

2.  Install the `ifplugd` package:
    
        cumulus@switch:~$ sudo -E apt-get install ifplugd

## <span>Configure ifplugd</span>

Once `ifplugd` is installed, two configuration files must be edited to
set up `ifplugd`:

  - `/etc/default/ifplugd`

  - `/etc/ifplugd/action.d/ifupdown`

{{%notice info has%}}

**Example ifplugd Configuration**

The example `ifplugd` configuration below show that `ifplugd` has been
configured to bring down all uplinks when the peerbond goes down in an
MLAG environment.

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info has%}}

`ifplugd` is configured on both both the primary and secondary
[MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
switches in this example.

{{%/notice%}}

1.  Open `/etc/default/ifplugd` in a text editor.

2.  Configure the file as appropriate, and add the peerbond name, before
    saving:
    
    ``` 
        INTERFACES="peerbond"
        HOTPLUG_INTERFACES=""
        ARGS="-q -f -u0 -d1 -w -I"
        SUSPEND_ACTION="stop"
    ```

3.  Open `/etc/ifplugd/action.d/ifupdown` in a text editor.

4.  Configure the script, and save the file.
    
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

5.  Restart `ifplugd` to implement the changes:
    
        cumulus@switch:$ sudo systemctl restart ifplugd.service

{{%/notice%}}

## <span>Caveats and Errata</span>

The default shell for `ifplugd` is `dash` (`/bin/sh`), rather than
`bash`, as it provides a faster and more nimble shell. However, it
contains less features than `bash` (such as being unable to handle
multiple uplinks).
