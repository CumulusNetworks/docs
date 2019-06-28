---
title: Zero Touch Provisioning
author: Cumulus Networks
weight: 149
aliases:
 - /display/RMP30/Zero+Touch+Provisioning
 - /pages/viewpage.action?pageId=5118686
pageID: 5118686
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
*Zero touch provisioning* (ZTP) enables network devices to be quickly
deployed in large-scale environments. Data center engineers only need to
rack and stack the switch, then connect it to the management network —
or alternatively, insert a USB stick and boot the switch. From here, the
provisioning process can start automatically and deploy a configuration.

The provisioning framework allows for a one-time, user-provided script
to be executed. This script can be used to add the switch to a
configuration management (CM) platform such as
[Puppet](http://puppetlabs.com/puppet/what-is-puppet),
[Chef](http://www.opscode.com), [CFEngine](https://cfengine.com), or
even a custom, home-grown tool.

In addition, you can use the `autoprovision` command in Cumulus RMP to
manually invoke your provisioning script.

ZTP in Cumulus RMP can occur automatically in one of the following ways,
in this order:

  - Via a local file

  - Using a USB drive inserted into the switch (ZTP-USB)

  - Via DHCP

Each method is discussed in greater detail below.

Contents

## <span>Commands</span>

  - ztp

## <span>Zero Touch Provisioning Using a Local File</span>

ZTP only looks once for a ZTP script on the local file system when the
switch boots. ZTP searches for an install script that matches an
[ONIE](http://onie.org)-style waterfall in `/var/lib/cumulus/ztp`,
looking for the most specific name first, and ending at the most
generic:

  - `'cumulus-ztp-' + architecture + '-' + vendor + '_' + model + '-r' +
    revision`

  - `'cumulus-ztp-' + architecture + '-' + vendor + '_' + model`

  - `'cumulus-ztp-' + vendor + '_' + model`

  - `'cumulus-ztp-' + architecture`

  - `'cumulus-ztp'`

For example:

    /mnt/usb/cumulus-ztp-amd64-cel_pebble-rUNKNOWN
    /mnt/usb/cumulus-ztp-amd64-cel_pebble
    /mnt/usb/cumulus-ztp-cel_pebble
    /mnt/usb/cumulus-ztp-amd64
    /mnt/usb/cumulus-ztp

You can also trigger the ZTP process manually by running the `ztp --run
<URL>` command, where the URL is the path to the ZTP script.

## <span>Zero Touch Provisioning Using USB (ZTP-USB)</span>

{{%notice note%}}

This feature has been tested only with "thumb" drives, not an actual
external large USB hard drive.

{{%/notice%}}

If the `ztp` process did not discover a local script, it tries once to
locate an inserted but unmounted USB drive. If it discovers one, it
begins the ZTP process.

Cumulus RMP supports the use of a FAT32, FAT16, or VFAT-formatted USB
drive as an installation source for ZTP scripts. You must plug in the
USB stick **before** you power up the switch.

At minimum, the script should:

  - Install the Cumulus RMP operating system.

  - Copy over a basic configuration to the switch.

  - Restart the switch or the relevant serves to get `switchd` up and
    running with that configuration.

Follow these steps to perform zero touch provisioning using USB:

1.  Copy the Cumulus RMP installation image to the USB stick.

2.  The `ztp` process searches the root filesystem of the newly mounted
    device for filenames matching an [ONIE-style
    waterfall](https://github.com/opencomputeproject/onie/wiki/Quick-Start-Guide#directly-connected-scenario)
    (see the patterns and examples above), looking for the most specific
    name first, and ending at the most generic.

3.  The script's contents are parsed to ensure it contains the
    `CUMULUS-AUTOPROVISIONING` flag (see [example
    scripts](#src-5118686_ZeroTouchProvisioning-example_scripts)).

## <span>Zero Touch Provisioning over DHCP</span>

If the `ztp` process did not discover a local/ONIE script or applicable
USB drive, it checks DHCP every 10 seconds for up to 5 minutes for the
presence of a ZTP URL specified in `/var/run/ztp.dhcp`. The URL can be
any of HTTP, HTTPS, FTP or TFTP.

For ZTP using DHCP, provisioning initially takes place over the
management network and is initiated via a DHCP hook. A DHCP option is
used to specify a configuration script. This script is then requested
from the Web server and executed locally on the switch.

The zero touch provisioning process over DHCP follows these steps:

1.  The first time you boot Cumulus RMP, eth0 is configured for DHCP and
    makes a DHCP request.

2.  The DHCP server offers a lease to the switch.

3.  If option 239 is present in the response, the zero touch
    provisioning process itself will start.

4.  The zero touch provisioning process requests the contents of the
    script from the URL, sending additional [HTTP
    headers](#src-5118686_ZeroTouchProvisioning-http_headers) containing
    details about the switch.

5.  The script's contents are parsed to ensure it contains the
    `CUMULUS-AUTOPROVISIONING` flag (see [example
    scripts](#src-5118686_ZeroTouchProvisioning-example_scripts)).

6.  If provisioning is necessary, then the script executes locally on
    the switch with root privileges.

7.  The return code of the script gets examined. If it is 0, then the
    provisioning state is marked as complete in the autoprovisioning
    configuration file.

### <span>Triggering ZTP over DHCP</span>

If provisioning has not already occurred, it is possible to trigger the
zero touch provisioning process over DHCP when eth0 is set to use DHCP
and one of the following events occur:

  - Booting the switch

  - Plugging a cable into or unplugging it from the eth0 port

  - Disconnecting then reconnecting the switch's power cord

You can also run the `ztp --run <URL>` command, where the URL is the
path to the ZTP script.

### <span>Configuring The DCHP Server</span>

During the DHCP process over eth0, Cumulus RMP will request DHCP option
239. This option is used to specify the custom provisioning script.

For example, the `/etc/dhcp/dhcpd.conf` file for an ISC DHCP server
would look like:

    option cumulus-provision-url code 239 = text;
     
    subnet 192.0.2.0 netmask 255.255.255.0 {
     range 192.0.2.100 192.168.0.200;
     option cumulus-provision-url "http://192.0.2.1/demo.sh";
    }

Additionally, the hostname of the switch can be specified via the
`host-name` option:

    subnet 192.168.0.0 netmask 255.255.255.0 {
     range 192.168.0.100 192.168.0.200;
     option cumulus-provision-url "http://192.0.2.1/demo.sh";
     host dc1-tor-sw1 { hardware ethernet 44:38:39:00:1a:6b; fixed-address 192.168.0.101; option host-name "dc1-tor-sw1"; }
    }

<span id="src-5118686_ZeroTouchProvisioning-http_headers"></span>

### <span>Detailed Look at HTTP Headers</span>

The following HTTP headers are sent in the request to the webserver to
retrieve the provisioning script:

    Header                        Value                 Example
    ------                        -----                 -------
    User-Agent                                          CumulusLinux-AutoProvision/0.4
    CUMULUS-ARCH                  CPU architecture      x86_64
    CUMULUS-BUILD                                       3.0.0-5c6829a-201309251712-final
    CUMULUS-LICENSE-INSTALLED     Either 0 or 1         0
    CUMULUS-MANUFACTURER                                odm
    CUMULUS-PRODUCTNAME                                 switch_model
    CUMULUS-SERIAL                                      XYZ123004
    CUMULUS-VERSION                                     3.0.0
    CUMULUS-PROV-COUNT                                  0
    CUMULUS-PROV-MAX                                    32

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
RMP, such as:

  - Perl

  - Python

  - Ruby

  - Shell

The script must return an exit code of 0 upon success, as this triggers
the autoprovisioning process to be marked as complete in the
autoprovisioning configuration file.

<span id="src-5118686_ZeroTouchProvisioning-example_scripts"></span>

### <span>Example ZTP Scripts</span>

The following script install Cumulus RMP from USB and applies a
configuration:

    #!/bin/bash
    function error() {
      echo -e "\e[0;33mERROR: The Zero Touch Provisioning script failed while running the command $BASH_COMMAND at line $BASH_LINENO.\e[0m" >&2
      exit 1
    }
     
    # Log all output from this script
    exec >/var/log/autoprovision 2>&1
     
    trap error ERR
     
    #Add Debian Repositories
    echo "deb http://http.us.debian.org/debian jessie main" >> /etc/apt/sources.list
    echo "deb http://security.debian.org/ jessie/updates main" >> /etc/apt/sources.list
     
    #Update Package Cache
    apt-get update -y
     
    #Install netshow diagnostics commands
    apt-get install -y netshow htop nmap
     
    #Load interface config from usb
    cp /mnt/usb/interfaces /etc/network/interfaces
     
    #Load port config from usb
    #   (if breakout cables are used for certain interfaces)
    cp /mnt/usb/ports.conf /etc/cumulus/ports.conf
     
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
    systemctl restart puppet.service
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
    systemctl restart puppet.service
    # CUMULUS-AUTOPROVISIONING
    exit 0

Now `puppet` can take over management of the switch, configuration
authentication, changing the default root password, and setting up
interfaces and routing protocols.

Several ZTP example scripts are available in the [Cumulus GitHub
repository](https://github.com/CumulusNetworks/example-ztp-scripts).

## <span>Testing and Debugging ZTP Scripts</span>

There are a few commands you can use to test and debug your ZTP scripts.

You can use verbose mode to debug your script and see where your script
failed. Include the `-v` option when you run `ztp`:

    cumulus@switch:~$ sudo ztp -v -r http://192.0.2.1/demo.sh
    Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh
                                                                                   
    Broadcast message from root@dell-s6000-01 (ttyS0) (Tue May 10 22:44:17 2016):  
                                                                                   
    ZTP: Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh
    ZTP Manual: URL response code 200
    ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
    ZTP Manual: Executing http://192.0.2.1/demo.sh
    error: ZTP Manual: Payload returned code 1
    error: Script returned failure

You can also run `ztp -s` to get more information about the current
state of ZTP.

    ZTP INFO:
     
    State              enabled
    Version            1.0
    Result             Script Failure
    Date               Tue May 10 22:42:09 2016 UTC
    Method             ZTP DHCP
    URL                http://192.0.2.1/demo.sh

If ZTP ran when the switch booted and not manually, you can run the
`systemctl -l status ztp.service` then `journalctl -l -u ztp.service` to
see if any failures occur:

    cumulus@switch:~$ sudo systemctl -l status ztp.service
    ● ztp.service - Cumulus RMP ZTP
       Loaded: loaded (/lib/systemd/system/ztp.service; enabled)
       Active: failed (Result: exit-code) since Wed 2016-05-11 16:38:45 UTC; 1min 47s ago
         Docs: man:ztp(8)
      Process: 400 ExecStart=/usr/sbin/ztp -b (code=exited, status=1/FAILURE)
     Main PID: 400 (code=exited, status=1/FAILURE)
     
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Device not found
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Looking for ZTP Script provided by DHCP
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: Attempting to provision via ZTP DHCP from http://192.0.2.1/demo.sh
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: URL response code 200
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Found Marker CUMULUS-AUTOPROVISIONING
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Executing http://192.0.2.1/demo.sh
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Payload returned code 1
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: Script returned failure
    May 11 16:38:45 dell-s6000-01 systemd[1]: ztp.service: main process exited, code=exited, status=1/FAILURE
    May 11 16:38:45 dell-s6000-01 systemd[1]: Unit ztp.service entered failed state.
    cumulus@switch:~$ 
    cumulus@switch:~$ sudo journalctl -l -u ztp.service --no-pager
    -- Logs begin at Wed 2016-05-11 16:37:42 UTC, end at Wed 2016-05-11 16:40:39 UTC. --
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: /var/lib/cumulus/ztp: Sate Directory does not exist. Creating it...
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: /var/run/ztp.lock: Lock File does not exist. Creating it...
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: /var/lib/cumulus/ztp/ztp_state.log: State File does not exist. Creating it...
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Looking for ZTP local Script
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6000_s1220-rUNKNOWN
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6000_s1220
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Looking for unmounted USB devices
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Parsing partitions
    May 11 16:37:45 cumulus ztp[400]: ztp [400]: ZTP USB: Device not found
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Looking for ZTP Script provided by DHCP
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: Attempting to provision via ZTP DHCP from http://192.0.2.1/demo.sh
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: URL response code 200
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Found Marker CUMULUS-AUTOPROVISIONING
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Executing http://192.0.2.1/demo.sh
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: ZTP DHCP: Payload returned code 1
    May 11 16:38:45 dell-s6000-01 ztp[400]: ztp [400]: Script returned failure
    May 11 16:38:45 dell-s6000-01 systemd[1]: ztp.service: main process exited, code=exited, status=1/FAILURE
    May 11 16:38:45 dell-s6000-01 systemd[1]: Unit ztp.service entered failed state.

Instead of running `journalctl`, you can see the log history by running:

    cumulus@switch:~$ cat /var/log/syslog | grep ztp
    2016-05-11T16:37:45.132583+00:00 cumulus ztp [400]: /var/lib/cumulus/ztp: State Directory does not exist. Creating it...
    2016-05-11T16:37:45.134081+00:00 cumulus ztp [400]: /var/run/ztp.lock: Lock File does not exist. Creating it...
    2016-05-11T16:37:45.135360+00:00 cumulus ztp [400]: /var/lib/cumulus/ztp/ztp_state.log: State File does not exist. Creating it...
    2016-05-11T16:37:45.185598+00:00 cumulus ztp [400]: ZTP LOCAL: Looking for ZTP local Script
    2016-05-11T16:37:45.485084+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6000_s1220-rUNKNOWN
    2016-05-11T16:37:45.486394+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell_s6000_s1220
    2016-05-11T16:37:45.488385+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64-dell
    2016-05-11T16:37:45.489665+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp-x86_64
    2016-05-11T16:37:45.490854+00:00 cumulus ztp [400]: ZTP LOCAL: Waterfall search for /var/lib/cumulus/ztp/cumulus-ztp
    2016-05-11T16:37:45.492296+00:00 cumulus ztp [400]: ZTP USB: Looking for unmounted USB devices
    2016-05-11T16:37:45.493525+00:00 cumulus ztp [400]: ZTP USB: Parsing partitions
    2016-05-11T16:37:45.636422+00:00 cumulus ztp [400]: ZTP USB: Device not found
    2016-05-11T16:38:43.372857+00:00 cumulus ztp [1805]: Found ZTP DHCP Request
    2016-05-11T16:38:45.696562+00:00 cumulus ztp [400]: ZTP DHCP: Looking for ZTP Script provided by DHCP
    2016-05-11T16:38:45.698598+00:00 cumulus ztp [400]: Attempting to provision via ZTP DHCP from http://192.0.2.1/demo.sh
    2016-05-11T16:38:45.816275+00:00 cumulus ztp [400]: ZTP DHCP: URL response code 200
    2016-05-11T16:38:45.817446+00:00 cumulus ztp [400]: ZTP DHCP: Found Marker CUMULUS-AUTOPROVISIONING
    2016-05-11T16:38:45.818402+00:00 cumulus ztp [400]: ZTP DHCP: Executing http://192.0.2.1/demo.sh
    2016-05-11T16:38:45.834240+00:00 cumulus ztp [400]: ZTP DHCP: Payload returned code 1
    2016-05-11T16:38:45.835488+00:00 cumulus ztp [400]: Script returned failure
    2016-05-11T16:38:45.876334+00:00 cumulus systemd[1]: ztp.service: main process exited, code=exited, status=1/FAILURE
    2016-05-11T16:38:45.879410+00:00 cumulus systemd[1]: Unit ztp.service entered failed state.

If you see that the issue is a script failure, you can modify the script
and then run `ztp` manually using `ztp -v -r <URL/path to that script>`,
as above.

    cumulus@switch:~$ sudo ztp -v -r http://192.0.2.1/demo.sh
    Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh
                                                                                   
    Broadcast message from root@dell-s6000-01 (ttyS0) (Tue May 10 22:44:17 2016):  
                                                                                   
    ZTP: Attempting to provision via ZTP Manual from http://192.0.2.1/demo.sh
    ZTP Manual: URL response code 200
    ZTP Manual: Found Marker CUMULUS-AUTOPROVISIONING
    ZTP Manual: Executing http://192.0.2.1/demo.sh
    error: ZTP Manual: Payload returned code 1
    error: Script returned failure
    cumulus@switch:~$ sudo ztp -s
    State      enabled                        
    Version    1.0                            
    Result     Script Failure                 
    Date       Tue May 10 22:44:17 2016 UTC   
    Method     ZTP Manual                     
    URL        http://192.0.2.1/demo.sh

## <span>Manually Using the ztp Command</span>

To enable zero touch provisioning, use the `-e` option:

    cumulus@switch:~$ sudo ztp -e

{{%notice note%}}

Enabling `ztp` means that `ztp` will try to occur the next time the
switch boots. However, if ZTP already occurred on a previous boot up or
if a manual configuration has been found, ZTP will just exit without
trying to look for any script.

ZTP checks for these manual configurations during bootup:

  - Password changes

  - Users and groups changes

  - Packages changes

  - Interfaces changes

When the switch is booted for the very first time, ZTP records the state
of some important files that are most likely going to be modified after
that the switch is configured. If ZTP is still enabled after a reboot,
ZTP will compare the recorded state to the current state of these files.
If they do not match, ZTP considers that the switch has already been
provisioned and exits. These files are only erased after a reset.

{{%/notice%}}

To reset `ztp` to its original state, use the `-R` option. This removes
the `ztp` directory and `ztp` runs the next time the switch reboots.

    cumulus@switch:~$ sudo ztp -R

To disable zero touch provisioning, use the `-d` option:

    cumulus@switch:~$ sudo ztp -d

To force provisioning to occur and ignore the status listed in the
configuration file use the `-r` option:

    cumulus@switch:~$ sudo ztp -r /mnt/usb/cumulus-ztp.sh

To see the current `ztp` state, use the `-s` option:

    cumulus@switch:~$ sudo ztp -s
    ZTP INFO:
    State disabled 
    Version 1.0 
    Result success 
    Date Thu May 5 16:49:33 2016 UTC 
    Method Switch manually configured  
    URL None

## <span>Notes</span>

  - During the development of a provisioning script, the switch may need
    to be reset.

  - You can use the Cumulus RMP ` onie-select  `-`i` command to cause
    the switch to reprovision itself and install a network operating
    system again using ONIE.

## <span>Configuration Files</span>

  - /var/lib/cumulus/autoprovision.conf
