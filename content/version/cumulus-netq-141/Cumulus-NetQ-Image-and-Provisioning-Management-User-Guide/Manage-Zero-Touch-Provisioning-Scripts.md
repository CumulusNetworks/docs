---
title: Manage Zero-Touch Provisioning Scripts
author: Cumulus Networks
weight: 37
aliases:
 - /display/NETQ141/Manage+Zero+Touch+Provisioning+Scripts
 - /pages/viewpage.action?pageId=10453549
pageID: 10453549
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
You can manage your zero-touch provisioning (ZTP) scripts with the NetQ
Image and Provisioning Management (IPM) application. IPM uses a default
ZTP script to provision and configure the basic network information
needed to add them to your data center network automatically during the
first boot of a switch. After that, you can have more than one script
and assign each to selected switches.

{{%notice info%}}

To take advantage of the ZTP script management feature, you must be
running Cumulus Linux 3.6.2 or later.

{{%/notice%}}

## <span>Command Overview</span>

IPM enables you to map and remove mapping of scripts to switches, and
view the available ZTP scripts. The command syntax is:

    tipctl add ztp [-h|--help] MAC SCRIPT
    tipctl del ztp mac [-h|--help] MAC
    tipctl del ztp script [-h|--help] SCRIPT
    tipctl show ztp all [--with-date|-h|--help]
    tipctl show ztp mac [--with-date|-h|--help] MAC
    tipctl show ztp script [--with-date|-h|--help] SCRIPT
    tipctl show repo ztp

The *-h* option is a short cut for the *--help* option.
<span style="color: #000000;"> The </span> *--with-date*
<span style="color: #000000;"> option lists the timestamp when the last
mapping occurred. </span>

## <span>Import Custom Scripts</span>

While IPM is preconfigured to use the default script, *ztp-default.sh*,
you can import additional scripts to manage automatic provisioning and
configuration of switches to better match your network deployment. For
example, you might want a new script for an upgrade or patching process
than you used during the initial configuration. The ZTP scripts are
stored in the */var/tips/www/ztp/scripts/* directory.

To import an image to the local repository:

1.  Open a terminal window.

2.  Log in to the NetQ Telemetry Server using your security credentials.

3.  Copy the image to the */var/tips/www/ztp/scripts/* directory.

This example shows the import of a ZTP script to IPM, and then verifies
it has been imported correctly.

    <username>@<hostname>:~/<directory-name>$ ssh <username>@<telemetry-server-name-or-ip-address>
    <username>@<ts>:~$ cp /<path>/<ztp-script-name> /var/tips/www/ztp/scripts/<ztp-script-name>
    <username>@<ts>:~$ tipctl show ztp all

## <span>View Stored Scripts</span>

You can view all of the scripts loaded into IPM using the `tipctl show
ztp` command. You can filter the results by MAC address and script name.
Additionally, you can display the (creation/install?) date of the
scripts.

This example shows all scripts in the directory.

    cumulus@ts:~$ tipctl show ztp all
    Category   Match             Base
    ---------- ----------------- ---------
    ztp_mac    70:72:cf:f5:5b:fe ns_ztp.sh

This example shows only the ZTP scripts mapped to switches associated
with a MAC address of *70:72:cf:f5:5b:fe*.

    cumulus@ts:~$ tipctl show ztp mac 70:72:cf:f5:5b:fe
    Category   Match             Base
    ---------- ----------------- ---------
    ztp_mac    70:72:cf:f5:5b:fe ns_ztp.sh

This example shows the ZTP script with the name of *ns\_ztp.sh*.

    cumulus@ts:~$ tipctl show ztp ns_ztp.sh
    Category   Match             Base
    ---------- ----------------- ---------
    ztp_mac    70:72:cf:f5:5b:fe ns_ztp.sh

This example show the scripts included in the ZTP repository.

    cumulus@ts:~$ tipctl show repo ztp
    ZTP Script
    ------------ 
    demo_ztp.sh 
    ns_ztp.sh

## <span>Map Scripts to Switches</span>

Once you have all of the ZTP scripts needed loaded into IPM, you can
then map the scripts to the various switches in your network using the
`tipctl add ztp` command. When you upgrade or apply patches, you can
remove an existing switch mapping and map the new script.

### <span>Add a Script Mapping</span>

This example shows how to map a switch with MAC address of
*A0:00:00:00:00:32* to the ZTP script named *ztp-servers* and map a
switch with MAC address of *A0:00:00:00:00:14* to the ZTP script named
*ztp-leafs.* It then verifies the mappings are correct. This example
shows all ZTP scripts for illustration purposes, but if you have a large
number of scripts, you could verify the addition using the MAC address
or by the script name instead.

    cumulus@ts:~$ tipctl add ztp a0:00:00:00:00:32 ztp-servers.sh
    cumulus@ts:~$ tipctl add ztp a0:00:00:00:00:14 ztp-leafs.sh
    cumulus@ts:~$ tipctl show ztp all
    Category   Match             Base
    ---------- ----------------- ---------
    ztp_mac    a0:00:00:00:00:32 ztp-servers.sh
    ztp_mac    a0:00:00:00:00:14 ztp-leafs.sh

### <span>Remove Script Mappings</span>

You can remove all mappings to a ZTP script or the mapping to a
particular switch.This example shows how to remove the mapping of the
*ztp-servers.sh* ZTP script from all of your switches currently using
this script, and then verify that no switches are mapped to that script.

    cumulus@ts:~$ tipctl del ztp script ztp-servers.sh
    cumulus@ts:~$ tipctl show ztp script ztp-servers.sh
    cumulus@ts:~$

This example shows how to remove the current mapping of a ZTP script to
the switch with MAC address of *A0:00:00:00:00:14*.

    cumulus@ts:~$ tipctl del script mac a0:00:00:00:00:14
    cumulus@ts:~$ tipctl show script mac a0:00:00:00:00:14

## <span>Remove Scripts from Repository</span>

If you are no longer using a particular ZTP script, you can remove it
from your local repository to simplify your management processes and
prevent mismapping of switches with incorrect scripts.This example shows
how to remove a script from your local repository, and then verify it
has been deleted.

    cumulus@<ts>:~$ cd ~/var/tips/www/ztp/scripts/
    cumulus@<ts>:~/var/tips/www/ztp/scripts/$ ls
    cumulus@<ts>:~/var/tips/www/ztp/scripts/$ rm <script-filename> 
    cumulus@<ts>:~/var/tips/www/ztp/scripts/$ ls

## <span>Example Script</span>

The following is a sample of the kinds of tasks you might perform in an
provisioning script.

    #!/usr/bin/env bash
     
    function install_license(){
        # Install license
        echo "$(date) INFO: Installing License..."
        echo $1 | /usr/cumulus/bin/cl-license -i
        return_code=$?
        if [ "$return_code" == "0" ]; then
            echo "$(date) INFO: License Installed."
        else
            echo "$(date) ERROR: License not installed. Return code was: $return_code"
            /usr/cumulus/bin/cl-license
            exit 1
        fi
    }
     
    function ping_until_reachable(){
        last_code=1
        max_tries=30
        tries=0
        while [ "0" != "$last_code" ] && [ "$tries" -lt "$max_tries" ]; do
            tries=$((tries+1))
            echo "$(date) INFO: ( Attempt $tries of $max_tries ) Pinging $1 Target Until Reachable."
            ping $1 -c2 &> /dev/null
            last_code=$?
                sleep 1
        done
        if [ "$tries" -eq "$max_tries" ] && [ "$last_code" -ne "0" ]; then
            echo "$(date) ERROR: Reached maximum number of attempts to ping the target $1 ."
            exit 1
        fi
    }
     
    function set_hostname(){
        # Remove DHCP Setting of Hostname
        sed s/'SETHOSTNAME="yes"'/'SETHOSTNAME="no"'/g -i /etc/dhcp/dhclient-exit-hooks.d/dhcp-sethostname
        hostnamectl set-hostname $1
    }
     
    ## A little something for the script to do
     
    #Output state of interfaces
    netshow interface
     
    # CUMULUS-AUTOPROVISIONING
    exit 0

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
