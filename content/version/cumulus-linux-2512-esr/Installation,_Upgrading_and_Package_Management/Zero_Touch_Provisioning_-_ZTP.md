---
title: Zero Touch Provisioning - ZTP
author: Cumulus Networks
weight: 43
aliases:
 - /display/CL25ESR/Zero+Touch+Provisioning+-+ZTP
 - /pages/viewpage.action?pageId=5115987
pageID: 5115987
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
*Zero *touch provisioning** (ZTP) allows devices to be quickly deployed
in large-scale environments. Data center engineers only need to rack and
stack the switch, connect it to the management network, then install
Cumulus Linux via ONIE; the initial configuration gets invoked via ZTP.
Alternatively, you can insert a USB stick with the configuration so the
provisioning process can start automatically.

The provisioning framework allows for a one-time, user-provided script
to be executed. This script can be used to add the switch to a
configuration management (CM) platform such as
[puppet](http://puppetlabs.com/puppet/what-is-puppet),
[Chef](http://www.opscode.com), [CFEngine](https://cfengine.com), or
even a custom, home-grown tool.

In addition, you can use the `autoprovision` command in Cumulus Linux to
manually invoke your provisioning script.

ZTP in Cumulus Linux can occur automatically in one of two ways:

  - Via DHCP

  - Using a USB drive inserted into the switch (ZTP-USB)

The two methods for using ZTP are discussed below in greater detail.

{{%notice note%}}

The standard Cumulus Linux license requires you to page through the
license file before accepting the terms, which can hinder an unattended
installation like zero touch provisioning. To request a license without
the EULA, email
[licensing@cumulusnetworks.com](mailto:licensing%40cumulusnetworks.com).

{{%/notice%}}

## <span>Commands</span>

  - autoprovision

## <span>Zero Touch Provisioning over DHCP</span>

For ZTP using DHCP, provisioning initially takes place over the
management network and is initiated via a DHCP hook. A DHCP option is
used to specify a configuration script. This script is then requested
from the Web server and executed locally on the switch.

The zero touch provisioning process over DHCP follows these steps:

1.  The first time you boot Cumulus Linux, eth0 is configured for DHCP
    and makes a DHCP request.

2.  The DHCP server offers a lease to the switch.

3.  If option 239 is present in the response, the zero touch
    provisioning process itself will start.

4.  The zero touch provisioning process requests the contents of the
    script from the URL, sending additional [HTTP
    headers](#src-5115987_ZeroTouchProvisioning-ZTP-http_headers)
    containing details about the switch.

5.  The script's contents are parsed to ensure it contains the
    `CUMULUS-AUTOPROVISIONING` flag (see [example
    scripts](#src-5115987_ZeroTouchProvisioning-ZTP-example_scripts)).

6.  The`  autoprovision ` command checks its [configuration
    file](#src-5115987_ZeroTouchProvisioning-ZTP-config_files) to see if
    autoprovisioning has already occurred and completed.

7.  If `autoprovision` determines that provisioning is necessary, then
    the script executes locally on the switch with root privileges.

8.  The return code of the script gets examined. If it is 0, then the
    provisioning state is marked as complete in the autoprovisioning
    configuration file.

### <span>Triggering ZTP over DHCP</span>

If provisioning has not already occurred, it is possible to trigger the
zero touch provisioning process over DHCP when eth0 is set to use DHCP
and one of the following events occur:

  - Booting the switch

  - Plugging a cable into or unplugging it from the eth0 port

  - Disconnecting then reconnecting the switch's power cord

### <span>Configuring The DCHP Server</span>

During the DHCP process over eth0, Cumulus Linux will request DHCP
option 239. This option is used to specify the custom provisioning
script.

For example, the `/etc/dhcp/dhcpd.conf` file for an ISC DHCP server
would look like:

    option cumulus-provision-url code 239 = text;
     
    subnet 192.168.0.0 netmask 255.255.255.0 {
     range 192.168.0.100 192.168.0.200;
     option cumulus-provision-url "http://192.168.0.2/demo.sh";
    }

Additionally, the hostname of the switch can be specified via the
`host-name` option:

    subnet 192.168.0.0 netmask 255.255.255.0 {
     range 192.168.0.100 192.168.0.200;
     option cumulus-provision-url "http://192.168.0.2/demo.sh";
     host dc1-tor-sw1 { hardware ethernet 44:38:39:00:1a:6b; fixed-address 192.168.0.101; option host-name "dc1-tor-sw1"; }
    }

<span id="src-5115987_ZeroTouchProvisioning-ZTP-http_headers"></span>

### <span>Detailed Look at HTTP Headers</span>

The following HTTP headers are sent in the request to the webserver to
retrieve the provisioning script:

    Header                        Value                 Example
    ------                        -----                 -------
    User-Agent                                          CumulusLinux-AutoProvision/0.4
    CUMULUS-ARCH                  CPU architecture      powerpc
    CUMULUS-BUILD                                       1.5.1-5c6829a-201309251712-final
    CUMULUS-LICENSE-INSTALLED     Either 0 or 1         1
    CUMULUS-MANUFACTURER                                dni
    CUMULUS-PRODUCTNAME                                 et-7448bf
    CUMULUS-SERIAL                                      XYZ123004
    CUMULUS-VERSION                                     1.5.1
    CUMULUS-PROV-COUNT                                  0
    CUMULUS-PROV-MAX                                    32

### <span>Testing and Debugging ZTP Scripts for DHCP</span>

One can manually run a provisioning session at any time using --force
(-f) option with the `autoprovision` command as shown below:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision --force --url http://192.168.1.1/demo.sh

## <span>Zero Touch Provisioning Using USB (ZTP-USB)</span>

{{%notice note%}}

This feature has been tested only with "thumb" drives, not an actual
external large USB hard drive.

{{%/notice%}}

Cumulus Linux supports the use of a FAT32, FAT16, or VFAT-formatted USB
drive as an installation source for ZTP scripts. A daemon called
`ztp-usb` runs by default in Cumulus Linux (you can disable it by
specifying `START=no` in `/etc/default/ztp-usb`).You can plug in a USB
stick at any time — when you power up a switch or even when the switch
has been running for some time. This is useful for performing a full
installation of the operating system for cases like fresh installs or
disaster recovery.

At minimum, the script should:

  - Install the Cumulus Linux operating system and license.

  - Copy over a basic configuration to the switch.

  - Restart the switch or the relevant serves to get `switchd` up and
    running with that configuration.

Follow these steps to perform zero touch provisioning using USB:

1.  Copy the Cumulus Linux license and installation image to the USB
    stick.

2.  When Cumulus Linux boots, the `ztp-usb` daemon starts.

3.  Each new device detected by the kernel is mounted to `/mnt/usb`.

4.  The daemon searches the root filesystem of the newly mounted device
    for filenames matching an [ONIE-style
    waterfall](https://github.com/opencomputeproject/onie/wiki/Quick-Start-Guide#directly-connected-scenario)
    (see the patterns and examples below), looking for the most specific
    name first, and ending at the most generic.

5.  The script's contents are parsed to ensure it contains the
    `CUMULUS-AUTOPROVISIONING` flag (see [example
    scripts](#src-5115987_ZeroTouchProvisioning-ZTP-example_scripts)).

6.  The`  autoprovision ` command checks its [configuration
    file](#src-5115987_ZeroTouchProvisioning-ZTP-config_files) to see if
    autoprovisioning has already occurred and completed.

7.  If `autoprovision` determines that provisioning is necessary, then
    the script executes locally on the switch with root privileges.

8.  After it completes one pass through all the devices, the `ztp-usb`
    daemon exits.

The filenames searched are as follows:

  - `'cumulus-ztp-' + architecture + '-' + vendor + '_' + model + '-r' +
    revision`

  - `'cumulus-ztp-' + architecture + '-' + vendor + '_' + model`

  - `'cumulus-ztp-' + vendor + '_' + model`

  - `'cumulus-ztp-' + architecture`

  - `'cumulus-ztp'`

For example:

    /mnt/usb/cumulus-ztp-powerpc-cel_smallstone-rUNKNOWN
    /mnt/usb/cumulus-ztp-powerpc-cel_smallstone
    /mnt/usb/cumulus-ztp-cel_smallstone
    /mnt/usb/cumulus-ztp-powerpc
    /mnt/usb/cumulus-ztp

### <span>Testing and Debugging ZTP-USB Scripts</span>

It is possible to test the scripts you've written for `ztp-usb` using
the techniques described below.

Once a script has been placed on a USB drive and is ready for testing
follow the procedure below:

1.  Disable the `ztp-usb` daemon.
    
        cumulus@switch:~$ sudo service ztp-usb stop
        cumulus@switch:~$ sudo service ztp-usb status
        [FAIL] ztp-usb is not running ... failed!

2.  Insert the USB stick into the switch.

3.  Move the `autoprovision` configuration file to a safe location.
    
        cumulus@switch:~$ sudo mv /var/lib/cumulus/autoprovision.conf /var/lib/cumulus/autoprovision.conf.original
    
    By moving the configuration file to a new location, the
    `autoprovision` framework has no record of previous provisioning
    successes or failures, which means any new attempt to
    `autoprovision` succeeds.

4.  Use debugging mode to run the `ztp-usb` script.
    
        cumulus@wan1$ sudo /usr/lib/cumulus/ztp-usb -d
        ztp-usb: 2015-09-18 14:39:49,280 Initial hash value 731845549779ee9c37bd630c7d24cc1d
        ztp-usb: 2015-09-18 14:39:49,280 Parsing partitions
        ztp-usb: 2015-09-18 14:39:49,518 /dev/sda: unsupported partition type = 
        ztp-usb: 2015-09-18 14:39:49,519 INFO: Trying to mount: "/dev/sda1" of type: "vfat"
        ztp-usb: 2015-09-18 14:39:49,519 Creating /mnt/usb mount directory
        ztp-usb: 2015-09-18 14:39:49,640 Waterfall search for /mnt/usb/cumulus-ztp-unknown-accton_as5712_54x-rUNKNOWN
        ztp-usb: 2015-09-18 14:39:49,640 Waterfall search for /mnt/usb/cumulus-ztp-unknown-accton_as5712_54x
        ztp-usb: 2015-09-18 14:39:49,640 Waterfall search for /mnt/usb/cumulus-ztp-unknown-accton
        ztp-usb: 2015-09-18 14:39:49,640 Waterfall search for /mnt/usb/cumulus-ztp-unknown
        ztp-usb: 2015-09-18 14:39:49,640 Waterfall search for /mnt/usb/cumulus-ztp
        ztp-usb: 2015-09-18 14:39:49,641 Found matching name, passing /mnt/usb/cumulus-ztp to autoprovision wrapper
        ztp-usb: 2015-09-18 14:39:49,641 Found /mnt/usb/cumulus-ztp script, passing to autoprovision
        ztp-usb: 2015-09-18 14:39:51,370 Script returned exit code 0
        ztp-usb: 2015-09-18 14:39:51,370 Unmounting drive and removing mountpoint.
        ztp-usb: 2015-09-18 14:39:51,396 /dev/sdb: unsupported partition type = 
        ztp-usb: 2015-09-18 14:39:51,396 /dev/sdb1: unsupported partition type = 
        ztp-usb: 2015-09-18 14:39:51,396 /dev/sdb2: unsupported partition type = ext4
        ztp-usb: 2015-09-18 14:39:51,396 /dev/sdb3: unsupported partition type = ext4
        ztp-usb: 2015-09-18 14:39:51,396 /dev/sdb4: unsupported partition type = LVM2_member
        ztp-usb: 2015-09-18 14:39:51,396 /dev/CUMULUS-PERSIST: unsupported partition type = RM=0
        ztp-usb: 2015-09-18 14:39:51,396 /dev/CUMULUS-SYSROOT1: unsupported partition type = RM=0
        ztp-usb: 2015-09-18 14:39:51,397 /dev/CUMULUS-SYSROOT2: unsupported partition type = RM=0
        ztp-usb: 2015-09-18 14:39:51,397 Current hash value 731845549779ee9c37bd630c7d24cc1d
        ztp-usb: 2015-09-18 14:40:21,427 Current hash value 731845549779ee9c37bd630c7d24cc1d

## <span>Writing ZTP Scripts </span>

{{%notice note%}}

Remember to include the following line in any of the supported scripts
which are expected to be run via the autoprovisioning framework.

    # CUMULUS-AUTOPROVISIONING

This line is required somewhere in the script file in order for
execution to occur.

{{%/notice%}}

The script must contain the `CUMULUS-AUTOPROVISIONING` flag. This can be
in a comment or remark and does not needed to be echoed or written to
`stdout`.

The script can be written in any language currently supported by Cumulus
Linux, such as:

  - Perl

  - Python

  - Ruby

  - Shell

The script must return an exit code of 0 upon success, as this triggers
the autoprovisioning process to be marked as complete in the
autoprovisioning configuration file.

### <span>Example ZTP Scripts</span>

The following script install Cumulus Linux and its license from USB and
applies a configuration:

    #!/bin/bash
    function error() {
      echo -e "\e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
      exit 1
    }
     
    # Log all output from this script
    exec >/var/log/autoprovision 2>&1
     
    trap error ERR
     
    #Add Debian Repositories
    echo "deb http://http.us.debian.org/debian wheezy main" >> /etc/apt/sources.list
    echo "deb http://security.debian.org/ wheezy/updates main" >> /etc/apt/sources.list
     
    #Update Package Cache
    apt-get update -y
     
    #Install netshow diagnostics commands
    apt-get install -y netshow htop nmap
     
    #Load interface config from usb
    cp /mnt/usb/interfaces /etc/network/interfaces
     
    #Load port config from usb
    #   (if breakout cables are used for certain interfaces)
    cp /mnt/usb/ports.conf /etc/cumulus/ports.conf
     
    #Install a License from usb and restart switchd
    cl-license -i /mnt/usb/license.txt && service switchd restart
     
    #Reload interfaces to apply loaded config
    ifreload -a
     
    #Output state of interfaces
    netshow interface
     
    # CUMULUS-AUTOPROVISIONING
    exit 0

Here is a simple script to install `puppet`:

    #!/bin/bash
    function error() {
      echo -e "\e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
      exit 1
    }
    trap error ERR
    apt-get update -y
    apt-get upgrade -y
    apt-get install puppet -y
    sed -i /etc/default/puppet -e 's/START=no/START=yes/'
    sed -i /etc/puppet/puppet.conf -e 's/\[main\]/\[main\]\npluginsync=true/'
    service puppet restart
    # CUMULUS-AUTOPROVISIONING
    exit 0

This script illustrates how to specify an internal APT mirror and
`puppet` master:

    #!/bin/bash
    function error() {
      echo -e "\e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
      exit 1
    }
    trap error ERR
    sed -i /etc/apt/sources.list -e 's/repo.cumulusnetworks.com/labrepo.mycompany.com/'
    apt-get update -y
    apt-get upgrade -y
    apt-get install puppet -y
    sed -i /etc/default/puppet -e 's/START=no/START=yes/'
    sed -i /etc/puppet/puppet.conf -e 's/\[main\]/\[main\]\npluginsync=true/'
    sed -i /etc/puppet/puppet.conf -e 's/\[main\]/\[main\]\nserver=labpuppet.mycompany.com/'
    service puppet restart
    # CUMULUS-AUTOPROVISIONING
    exit 0

Now `puppet` can take over management of the switch, configuration
authentication, changing the default root password, and setting up
interfaces and routing protocols.

Several ZTP example scripts are available in the [Cumulus GitHub
repository](https://github.com/CumulusNetworks/example-ztp-scripts).

## <span>Manually Using the autoprovision Command</span>

{{%notice note%}}

Be sure to specify the full path to the `autoprovision` command.

{{%/notice%}}

All forms of ZTP use the `autoprovision` command on the backend to
execute a provided provisioning script, whether that script is sourced
from a URL over the network or locally via a file from a USB drive. One
of the benefits of using the `autoprovision` command — instead of simply
scheduling a cronjob to run your script — is that `autoprovision` tracks
whether or not a script has already been executed (and when) in its
configuration file `/var/lib/cumulus/autoprovision.conf`, ensuring that
a switch that has already been provisioned is not accidentally
provisioned again at a later date.

Users with root privileges can interact with the `autoprovision` command
directly using the examples below.

To enable zero touch provisioning, use the `-e` option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -e

To run the provisioning script against a script hosted on a Web server,
use the `-u` option and include the URL to the script:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -u http://192.168.0.1/ztp.sh

To run the provisioning script against a script hosted on the local
filesystem, use the `--file` or -i option and include the file location
of the script:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision --file /mnt/usb/cumulus-ztp.sh

To disable zero touch provisioning, use the `-x` option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -x

To enable startup discovery mode, without relying on DHCP when you boot
the switch, use the `-s` option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -s

To force provisioning to occur and ignore the status listed in the
configuration file use the -f option:

    cumulus@switch:~$ sudo /usr/lib/cumulus/autoprovision -f --file /mnt/usb/cumulus-ztp.sh

## <span>Notes</span>

  - During the development of a provisioning script, the switch may need
    to be reset.

  - You can use the Cumulus Linux `cl-img-clear-overlay` command to
    revert the image to its original configuration.

  - You can use the Cumulus Linux `cl-img-select -i` command to cause
    the switch to reprovision itself and install a network operating
    system again using ONIE.

## <span id="src-5115987_ZeroTouchProvisioning-ZTP-config_files" class="confluence-anchor-link"></span><span> Configuration Files</span>

  - /var/lib/cumulus/autoprovision.conf: Stores configuration options
    and details for the autoprovisioning framework

  - /etc/default/ztp-usb: Stores the enable/disable flag for the
    `ztp-usb` service
