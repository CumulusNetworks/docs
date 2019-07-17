---
title: ifplugd
author: Cumulus Networks
weight: 3115
aliases:
 - /display/CL3740/ifplugd
 - /pages/viewpage.action?pageId=83626936416
pageID: 83626936416
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
`ifplugd` is an Ethernet link-state monitoring daemon, that can executes
user-specified scripts to configure an Ethernet device when a cable is
plugged in, or automatically unconfigure itan Ethernet device when a cable 
is removed.

 Follow the steps below to install and configure the 
`ifplugd` daemon.

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
configuredAfter you install `ifplugd`, you must edit two configuration files:

  - `/etc/default/ifplugd`

  - `/etc/ifplugd/action.d/ifupdown`

The example configuration below configures `ifplugd` to bring down all 
uplinks when the peer bond goes down in an
 MLAG environment.

<div class="confbox admonition admonition-note">

<span class="admonition-icon confluence-information-macro-icon"></span>

<div class="admonition-body">

{{%notice info has%}}

`ifplugd` is configured on both both the primary and secondary
[MLAG](/version/cumulus-linux-377/Layer-2/Multi-Chassis-Link-Aggregation---MLAG)
switches in this example.

{{%/notice%}}

</div>

</div>

1.  Open `/etc/default/ifplugd` in a text editor.

2.  C and configure the file
    as appropriate, and a. Add the `peerbond` name, before
    saving:
    
    ``` you save the file.
    
        INTERFACES="peerbond"
        HOTPLUG_INTERFACES=""
        ARGS="-q -f -u0 -d1 -w -I"
        SUSPEND_ACTION="stop"
    ```

3
2.  Open the `/etc/ifplugd/action.d/ifupdown` file in a text editor.

4.    Configure the script, andthen save the file.
    
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

53.  Restart the `ifplugd` daemon to implement the changes:
    
        cumulus@switch:~$ sudo systemctl restart ifplugd.service

{{%/notice%}}

## <span>Caveats and Errata</span>

The default shell for `ifplugd` is `dash` (`/bin/sh`), rather than
 instead of `bash`, 
as it provides a faster and more nimble shell. However, it
`dash` contains less
fewer features than `bash` (such as beingfor example, `dash` is unable to handle
multiple uplinks).

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1OTY0NjEwODVdfQ==
-->