---
title: Adding and Updating Packages
author: Cumulus Networks
weight: 49
aliases:
 - /display/DOCS/Adding+and+Updating+Packages
 - /pages/viewpage.action?pageId=8362631
pageID: 8362631
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
You use the Advanced Packaging Tool (`apt`) to manage additional
applications (in the form of packages) and to install the latest
updates.

{{%notice warning%}}

**Network Disruptions**

Updating, upgrading, and installing packages with `apt` causes
disruptions to network services:

  - Upgrading a package might result in services being restarted or
    stopped as part of the upgrade process.

  - Installing a package might disrupt core services by changing core
    service dependency packages. In some cases, installing new packages
    might also upgrade additional existing packages due to dependencies.

If services are stopped, you might need to reboot the switch for those
services to restart.

{{%/notice%}}

## <span>Update the Package Cache</span>

To work properly, `apt` relies on a local cache of the available
packages. You must populate the cache initially, and then periodically
update it with `-E apt-get update`:

    cumulus@switch:~$ sudo -E apt-get update
    Get:1 http://repo3.cumulusnetworks.com CumulusLinux-3 InRelease [7,624 B]
    Get:2 http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates InRelease [7,555 B]
    Get:3 http://repo3.cumulusnetworks.com CumulusLinux-3-updates InRelease [7,660 B]
    Get:4 http://repo3.cumulusnetworks.com CumulusLinux-3/cumulus Sources [20 B]
    Get:5 http://repo3.cumulusnetworks.com CumulusLinux-3/upstream Sources [20 B]
    Get:6 http://repo3.cumulusnetworks.com CumulusLinux-3/cumulus amd64 Packages [38.4 kB]
    Get:7 http://repo3.cumulusnetworks.com CumulusLinux-3/upstream amd64 Packages [445 kB]
    Get:8 http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/cumulus Sources [20 B]
    Get:9 http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/upstream Sources [11.8 kB]
    Get:10 http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/cumulus amd64 Packages [20 B]
    Get:11 http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/upstream amd64 Packages [8,941 B]
    Get:12 http://repo3.cumulusnetworks.com CumulusLinux-3-updates/cumulus Sources [20 B]
    Get:13 http://repo3.cumulusnetworks.com CumulusLinux-3-updates/upstream Sources [776 B]
    Get:14 http://repo3.cumulusnetworks.com CumulusLinux-3-updates/cumulus amd64 Packages [38.4 kB]
    Get:15 http://repo3.cumulusnetworks.com CumulusLinux-3-updates/upstream amd64 Packages [444 kB]
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3/cumulus Translation-en_US
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3/cumulus Translation-en
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3/upstream Translation-en_US
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3/upstream Translation-en
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/cumulus Translation-en_US
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/cumulus Translation-en
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/upstream Translation-en_US
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-security-updates/upstream Translation-en
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-updates/cumulus Translation-en_US
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-updates/cumulus Translation-en
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-updates/upstream Translation-en_US
    Ign http://repo3.cumulusnetworks.com CumulusLinux-3-updates/upstream Translation-en
    Fetched 1,011 kB in 1s (797 kB/s)
    Reading package lists... Done

{{%notice tip%}}

Cumulus Networks recommends you use the `-E` option with `sudo` whenever
you run any `apt-get` command. This option preserves your environment
variables (such as HTTP proxies) before you install new packages or
upgrade your distribution.

{{%/notice%}}

## <span>List Available Packages</span>

After the cache is populated, use the `apt-cache` command to search the
cache and find the packages in which you are interested or to get
information about an available package. Here are examples of the
`search` and `show` sub-commands:

    cumulus@switch:~$ apt-cache search tcp
    socat - multipurpose relay for bidirectional data transfer
    fakeroot - tool for simulating superuser privileges
    tcpdump - command-line network traffic analyzer
    openssh-server - secure shell (SSH) server, for secure access from remote machines
    openssh-sftp-server - secure shell (SSH) sftp server module, for SFTP access from remote machines
    python-dpkt - Python packet creation / parsing module
    libfakeroot - tool for simulating superuser privileges - shared libraries
    openssh-client - secure shell (SSH) client, for secure access to remote machines
    rsyslog - reliable system and kernel logging daemon
    libwrap0 - Wietse Venema's TCP wrappers library
    netbase - Basic TCP/IP networking system

    cumulus@switch:~$ apt-cache show tcpdump
    Package: tcpdump
    Status: install ok installed
    Priority: optional
    Section: net
    Installed-Size: 1092
    Maintainer: Romain Francoise <rfrancoise@debian.org>
    Architecture: amd64
    Multi-Arch: foreign
    Version: 4.6.2-5+deb8u1
    Depends: libc6 (>= 2.14), libpcap0.8 (>= 1.5.1), libssl1.0.0 (>= 1.0.0)
    Description: command-line network traffic analyzer
     This program allows you to dump the traffic on a network. tcpdump
     is able to examine IPv4, ICMPv4, IPv6, ICMPv6, UDP, TCP, SNMP, AFS
     BGP, RIP, PIM, DVMRP, IGMP, SMB, OSPF, NFS and many other packet
     types.
     .
     It can be used to print out the headers of packets on a network
     interface, filter packets that match a certain expression. You can
     use this tool to track down network problems, to detect attacks
     or to monitor network activities.
    Description-md5: f01841bfda357d116d7ff7b7a47e8782
    Homepage: http://www.tcpdump.org/
    cumulus@switch:~$

{{%notice note%}}

The search commands look for the search terms not only in the package
name but in other parts of the package information; the search matches
on more packages than you might expect.

{{%/notice%}}

## <span>List Installed Packages</span>

The APT cache contains information about all the packages available in
the repository. To see which packages are actually installed on your
system, use `dpkg`. The following example lists all the package names on
the system that contain `tcp`:

    cumulus@switch:~$ dpkg -l \*tcp\*
    Desired=Unknown/Install/Remove/Purge/Hold
    | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
    |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
    ||/ Name                          Version             Architecture        Description
    +++-=============================-===================-===================-===============================================================
    un  tcpd                          <none>              <none>              (no description available)
    ii  tcpdump                       4.6.2-5+deb8u1      amd64               command-line network traffic analyzer
    cumulus@switch:~$

## <span id="src-8362631_AddingandUpdatingPackages-versionDisplay" class="confluence-anchor-link"></span><span>Display the Version of a Package</span>

To show the version of a specific package installed on the system, run
the `net show package version <package>` command. For example, the
following command shows which version of the `vrf` package is installed
on the system:

    cumulus@switch:~$ net show package version vrf
    1.0-cl3u11

As an alternative to the NCLU command described above, you can run the
Linux `dpkg -l <package_name>` command.

To see a list of all packages installed on the system with their
versions, run the `net show package version` command. For example:

    cumulus@switch:~$ net show package version
    Package                            Installed Version(s)
    ---------------------------------  -----------------------------------------------------------------------
    acl                                2.2.52-2
    acpi                               1.7-1
    acpi-support-base                  0.142-6
    acpid                              1:2.0.23-2
    adduser                            3.113+nmu3
    apt                                1.0.9.8.2-cl3u3~1532198712.6d9298c
    apt-doc                            1.0.9.8.2-cl3u3~1532198712.6d9298c
    apt-transport-https                1.0.9.8.2-cl3u3~1532198712.6d9298c
    apt-utils                          1.0.9.8.2-cl3u3~1532198712.6d9298c
    arping                             2.14-1
    arptables                          0.0.3.4-1
    ...

## <span id="src-8362631_AddingandUpdatingPackages-upgrade-packages" class="confluence-anchor-link"></span><span>Upgrade Packages</span>

To upgrade all the packages installed on the system to their latest
versions, run the following commands:

    cumulus@switch:~$ sudo -E apt-get update
    cumulus@switch:~$ sudo -E apt-get upgrade

A list of packages that will be upgraded is displayed and you are
prompted to continue.

The above commands upgrade all installed versions with their latest
versions but do not install any new packages.

Refer to [Upgrading Cumulus
Linux](/cumulus-linux/Installation_Management/Upgrading_Cumulus_Linux)
for additional information.

## <span>Add New Packages</span>

To add a new package:

1.  First ensure the package is not already installed on the system:
    
        cumulus@switch:~$ dpkg -l | grep <name of package>
    
    If the package is installed already, you can update the package from
    the Cumulus Linux repository as part of the package upgrade process,
    which upgrades all packages on the system. See [Upgrade
    Packages](#src-8362631_AddingandUpdatingPackages-upgrade-packages)
    above.

2.  If the package is *not* already installed, add it by running `-E
    apt-get install <name of package>`. This retrieves the package from
    the Cumulus Linux repository and installs it on your system together
    with any other packages on which this package might depend. The
    following example adds the `tcpreplay` package to the system:
    
        cumulus@switch:~$ sudo -E apt-get install tcpreplay
        Reading package lists... Done
        Building dependency tree
        Reading state information... Done
        The following NEW packages will be installed:
        tcpreplay
        0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
        Need to get 436 kB of archives.
        After this operation, 1008 kB of additional disk space will be used.
        Get:1 https://repo.cumulusnetworks.com/ CumulusLinux-1.5/main tcpreplay amd64 4.6.2-5+deb8u1 [436 kB]
        Fetched 436 kB in 0s (1501 kB/s)
        Selecting previously unselected package tcpreplay.
        (Reading database ... 15930 files and directories currently installed.)
        Unpacking tcpreplay (from .../tcpreplay_4.6.2-5+deb8u1_amd64.deb) ...
        Processing triggers for man-db ...
        Setting up tcpreplay (4.6.2-5+deb8u1) ...
        cumulus@switch:~$
    
    You can install several packages at the same time:
    
        cumulus@switch:~$ sudo -E apt-get install <package 1> <package 2> <package 3>
    
    {{%notice tip%}}
    
    In some cases, installing a new package might also upgrade
    additional existing packages due to dependencies. To view these
    additional packages before you install, run the `apt-get install
    --dry-run` command.
    
    {{%/notice%}}

## <span>Add Packages from Another Repository</span>

As shipped, Cumulus Linux searches the Cumulus Linux repository for
available packages. You can add additional repositories to search by
adding them to the list of sources that `apt-get` consults. See `man
sources.list` for more information.

{{%notice tip%}}

Cumulus Networks has added features or made bug fixes to certain
packages; you must not replace these packages with versions from other
repositories. Cumulus Linux is configured to ensure that the packages
from the Cumulus Linux repository are always preferred over packages
from other repositories.

{{%/notice%}}

If you want to install packages that are not in the Cumulus Linux
repository, the procedure is the same as above, but with one additional
step.

{{%notice note%}}

Packages that are not part of the Cumulus Linux Repository are not
typically tested and might not be supported by Cumulus Linux Technical
Support.

{{%/notice%}}

Installing packages outside of the Cumulus Linux repository requires the
use of `-E apt-get`; however, depending on the package, you can use
`easy-install` and other commands.

To install a new package, complete the following steps:

1.  Run the `dpkg` command to ensure that the package is not already
    installed on the system:
    
        cumulus@switch:~$ dpkg -l | grep {name of package}

2.  If the package is installed already, ensure it is the version you
    need. If it is an older version, update the package from the Cumulus
    Linux repository:
    
        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get install {name of package}
        cumulus@switch:~$ sudo -E apt-get upgrade

3.  If the package is not on the system, the package source location is
    most likely **not** in the `/etc/apt/sources.list` file. If the
    source for the new package is **not** in `sources.list`, edit and
    add the appropriate source to the file. For example, add the
    following if you want a package from the Debian repository that is
    **not** in the Cumulus Linux repository:
    
        deb http://http.us.debian.org/debian jessie main
        deb http://security.debian.org/ jessie/updates main
    
    Otherwise, the repository might be listed in `/etc/apt/sources.list`
    but is commented out, as can be the case with the early-access
    repository:
    
        #deb http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus
    
    To uncomment the repository, remove the \# at the start of the line,
    then save the file:
    
        deb http://repo3.cumulusnetworks.com/repo CumulusLinux-3-early-access cumulus

4.  Run `-E apt-get update`, then install the package and upgrade:
    
        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get install {name of package}
        cumulus@switch:~$ sudo -E apt-get upgrade

## <span>Cumulus Supplemental Repository</span>

Cumulus Networks provides a *Supplemental Repository* that contains
third party applications commonly installed on switches.

The repository is provided for convenience only. You can download and
use these applications; however, the applications in this repository are
not tested, developed, certified, or supported by Cumulus Networks.

Below is a non-exhaustive list of some of the packages present in the
repository:

  - `htop` lets you view CPU, memory, and process information.

  - `scamper` is an ECMP traceroute utility.

  - `mtr` is an ECMP traceroute utility.

  - `dhcpdump` is similar to TCPdump but focused only on DHCP traffic.

  - `vim` is a text editor.

  - `fping` provides a list of targets through textfile to check
    reachability.

  - `scapy` is a custom packet generator for testing.

  - `bwm-ng` is a real-time bandwidth monitor.

  - `iftop` is a real-time traffic monitor.

  - `tshark` is a CLI version of wireshark.

  - `nmap` is a network scanning utility.

  - `minicom` is a USB/Serial console utility that turns your switch
    into a terminal server (useful for out of band management switches
    to provide a console on the dataplane switches in the rack).

  - `apt-cacher-ng` caches packages for mirroring purposes.

  - `iptraf` is a ncurses-based traffic visualization utility.

  - `swatch` monitors system activity. It reads a configuration file
    that contains patterns for which to search and actions to perform
    when each pattern is found.

  - `dos2unix` converts line endings from Windows to Unix.

  - `fail2ban` monitors log files (such as `/var/log/auth.log` and
    `/var/log/apache/access.log`) and temporarily or persistently bans
    the login of failure-prone IP addresses by updating existing
    firewall rules. This utility is not hardware accelerated on a
    Cumulus Linux switch, so only affects the control plane.

To enable the Supplemental Repository:

1.  In a file editor, open the `/etc/apt/sources.list` file.
    
        cumulus@leaf01:~$ sudo nano /etc/apt/sources.list

2.  Uncomment the following lines:
    
        #deb http://repo3.cumulusnetworks.com/repo Jessie-supplemental upstream
        #deb-src http://repo3.cumulusnetworks.com/repo Jessie-supplemental upstream

3.  Update the list of software packages:
    
        cumulus@leaf01:~$ sudo -E apt-get update -y

4.  Install the software in which you are interested:
    
        cumulus@leaf01:~$ sudo -E apt-get install htop

## <span>Related Information</span>

  - [Debian GNU/Linux FAQ, Ch 8 Package management
    tools](http://www.debian.org/doc/manuals/debian-faq/ch-pkgtools.en.html)

  - man pages for `apt-get`, `dpkg`, `sources.list`, `apt_preferences`
