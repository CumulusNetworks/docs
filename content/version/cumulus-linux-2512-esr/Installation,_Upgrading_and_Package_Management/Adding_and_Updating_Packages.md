---
title: Adding and Updating Packages
author: Cumulus Networks
weight: 41
aliases:
 - /display/CL25ESR/Adding+and+Updating+Packages
 - /pages/viewpage.action?pageId=5115986
pageID: 5115986
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
You use the Advanced Packaging Tool (APT) to manage additional
applications (in the form of packages) and to install the latest
updates.

## <span>Commands</span>

  - apt-get

  - apt-cache

  - dpkg

## <span>Updating the Package Cache</span>

To work properly, APT relies on a local cache of the available packages.
You must populate the cache initially, and then periodically update it
with `apt-get update`:

    cumulus@switch:~$ sudo apt-get update
    Get:1 http://repo.cumulusnetworks.com CumulusLinux-2.5 Release.gpg [490 B]
    Get:2 http://repo.cumulusnetworks.com CumulusLinux-2.5 Release [16.2 kB]
    Get:3 http://repo.cumulusnetworks.com CumulusLinux-2.5/main powerpc Packages [181 kB]
    Get:4 http://repo.cumulusnetworks.com CumulusLinux-2.5/addons powerpc Packages [75.1 kB]
    Get:5 http://repo.cumulusnetworks.com CumulusLinux-2.5/updates powerpc Packages [112 kB]
    Get:6 http://repo.cumulusnetworks.com CumulusLinux-2.5/security-updates powerpc Packages [28.5 kB]
    Ign http://repo.cumulusnetworks.com CumulusLinux-2.5/addons Translation-en
    Ign http://repo.cumulusnetworks.com CumulusLinux-2.5/main Translation-en
    Ign http://repo.cumulusnetworks.com CumulusLinux-2.5/security-updates Translation-en
    Ign http://repo.cumulusnetworks.com CumulusLinux-2.5/updates Translation-en
    Fetched 413 kB in 3s (117 kB/s)Reading package lists... Done

## <span>Listing Available Packages</span>

Once the cache is populated, use `apt-cache` to search the cache to find
the packages you are interested in or to get information about an
available package. Here are examples of the `search` and `show`
sub-commands:

    cumulus@switch:~$ apt-cache search tcp
    netbase - Basic TCP/IP networking system
    quagga-doc - documentation files for quagga
    libwrap0-dev - Wietse Venema's TCP wrappers library, development files
    libwrap0 - Wietse Venema's TCP wrappers library
    librelp0 - Reliable Event Logging Protocol (RELP) library
    socat - multipurpose relay for bidirectional data transfer
    openssh-client - secure shell (SSH) client, for secure access to remote machines
    libpq5 - PostgreSQL C client library
    rsyslog - reliable system and kernel logging daemon
    tcpdump - command-line network traffic analyzer
    openssh-server - secure shell (SSH) server, for secure access from remote machines
    librelp-dev - Reliable Event Logging Protocol (RELP) library - development files
    fakeroot - tool for simulating superuser privileges
    quagga - BGP/OSPF/RIP routing daemon
    monit - utility for monitoring and managing daemons or similar programs
    python-dpkt - Python packet creation / parsing module
    iperf - Internet Protocol bandwidth measuring tool
    nmap - The Network Mapper
    tcpstat - network interface statistics reporting tool
    tcpreplay - Tool to replay saved tcpdump files at arbitrary speeds
    nuttcp - network performance measurement tool
    collectd-core - statistics collection and monitoring daemon (core system)
    tcpxtract - extracts files from network traffic based on file signatures
    nagios-plugins-basic - Plugins for nagios compatible monitoring systems
    tcptrace - Tool for analyzing tcpdump output
    jdoo - utility for monitoring and managing daemons or similar programs
    hping3 - Active Network Smashing Tool
    
    cumulus@switch:~$ apt-cache show tcpreplay
    Package: tcpreplay
    Priority: optional
    Section: net
    Installed-Size: 984
    Maintainer: Noël Köthe <noel@debian.org>
    Architecture: powerpc
    Version: 3.4.3-2+wheezy1
    Depends: libc6 (>= 2.7), libpcap0.8 (>= 0.9.8)
    Filename: pool/CumulusLinux-2.5/addons/tcpreplay_3.4.3-2+wheezy1_powerpc.deb
    Size: 435904
    MD5sum: cf20bec7282ef77a091e79372a29fe1e
    SHA1: 8ee1b9b02dacd0c48a474844f4466eb54c7e1568
    SHA256: 03dc29057cb608d2ddf08207aedf18d47988ed6c23db0af69d30746768a639ae
    SHA512: a411b08e7a7bea62331c527d152533afca735b795f2118507260a5a0c3b6143500df9f6723cff736a1de0969a63e7a7ad0ce8a181ea7dfb36e2330a95d046fb1
    Description: Tool to replay saved tcpdump files at arbitrary speeds
     Tcpreplay is aimed at testing the performance of a NIDS by
     replaying real background network traffic in which to hide
     attacks. Tcpreplay allows you to control the speed at which the
     traffic is replayed, and can replay arbitrary tcpdump traces. Unlike
     programmatically-generated artificial traffic which doesn't
     exercise the application/protocol inspection that a NIDS performs,
     and doesn't reproduce the real-world anomalies that appear on
     production networks (asymmetric routes, traffic bursts/lulls,
     fragmentation, retransmissions, etc.), tcpreplay allows for exact
     replication of real traffic seen on real networks.
    Homepage: http://tcpreplay.synfin.net/
    cumulus@switch:~$

{{%notice note%}}

The search commands look for the search terms not only in the package
name but in other parts of the package information. Consequently, it
will match on more packages than you would expect.

{{%/notice%}}

## <span>Adding a Package</span>

In order to add a new package, first ensure the package is not already
installed in the system:

    cumulus@switch:~$ dpkg -l | grep {name of package}

If the package is installed already, ensure it’s the version you need.
If it’s an older version, then update the package from the Cumulus Linux
repository:

    cumulus@switch:~$ sudo apt-get update

If the package is not already on the system, add it by running `apt-get
install`. This retrieves the package from the Cumulus Linux repository
and installs it on your system together with any other packages that
this package might depend on.

For example, the following adds the package `tcpreplay` to the system:

    cumulus@switch:~$ sudo apt-get install tcpreplay
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    The following NEW packages will be installed:
    tcpreplay
    0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
    Need to get 436 kB of archives.
    After this operation, 1008 kB of additional disk space will be used.
    Get:1 https://repo.cumulusnetworks.com/ CumulusLinux-1.5/main tcpreplay powerpc 3.4.3-2+wheezy1 [436 kB]
    Fetched 436 kB in 0s (1501 kB/s)
    Selecting previously unselected package tcpreplay.
    (Reading database ... 15930 files and directories currently installed.)
    Unpacking tcpreplay (from .../tcpreplay_3.4.3-2+wheezy1_powerpc.deb) ...
    Processing triggers for man-db ...
    Setting up tcpreplay (3.4.3-2+wheezy1) ...
    cumulus@switch:~$ 

## <span>Listing Installed Packages</span>

The APT cache contains information about all the packages available on
the repository. To see which packages are actually installed on your
system, use `dpkg`. The following example lists all the packages on the
system that have "tcp" in their package names:

    cumulus@switch:~$ dpkg -l \*tcp\*
    Desired=Unknown/Install/Remove/Purge/Hold
    | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
    |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
    ||/ Name           Version      Architecture Description
    +++-==============-============-============-=================================
    ii  tcpd           7.6.q-24     powerpc      Wietse Venema's TCP wrapper utili
    ii  tcpdump        4.3.0-1      powerpc      command-line network traffic anal
    ii  tcpreplay      3.4.3-2+whee powerpc      Tool to replay saved tcpdump file
    cumulus@switch:~$

## <span>Upgrading to Newer Versions of Installed Packages</span>

### <span>Upgrading a Single Package</span>

A single package can be upgraded by simply installing that package again
with `apt-get install`. You should perform an update first so that the
APT cache is populated with the latest information about the packages.

To see if a package needs to be upgraded, use `apt-cache show <pkgname>`
to show the latest version number of the package. Use `dpkg -l
<pkgname>` to show the version number of the installed package.

{{%notice warning%}}

Upgrading a single package in the Cumulus Linux distribution is not
advised unless directed by [Cumulus Networks
Support](https://cumulusnetworks.com/support/overview/).

{{%/notice%}}

### <span>Upgrading All Packages</span>

You can update all packages on the system by running `apt-get update`,
then `apt-get dist-upgrade`. This upgrades all installed versions with
their latest versions but will not install any new packages.

## <span>Adding Packages from Another Repository</span>

As shipped, Cumulus Linux searches the Cumulus Linux repository for
available packages. You can add additional repositories to search by
adding them to the list of sources that `apt-get` consults. See `man
sources.list` for more information.

{{%notice tip%}}

For several packages, Cumulus Networks has added features or made bug
fixes and these packages must not be replaced with versions from other
repositories. Cumulus Linux has been configured to ensure that the
packages from the Cumulus Linux repository are always preferred over
packages from other repositories.

{{%/notice%}}

If you want to install packages that are not in the Cumulus Linux
repository, the procedure is the same as above with one additional step.

{{%notice note%}}

Packages not part of the Cumulus Linux Repository have generally not
been tested, and may not be supported by Cumulus Linux support.

{{%/notice%}}

Installing packages outside of the Cumulus Linux repository requires the
use of `apt-get`, but, depending on the package, `easy-install` and
other commands can also be used.

To install a new package, please complete the following steps:

1.  First, ensure package is not already installed in the system. Use
    the `dpkg` command:
    
        cumulus@switch:~$ dpkg -l | grep {name of package}

2.  If the package is installed already, ensure it's the version you
    need. If it's an older version, then update the package from the
    Cumulus Linux repository:
    
        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install {name of package}

3.  If the package is not on the system, then most likely the package
    source location is also **not** in the `/etc/apt/sources.list` file.
    If the source for the new package is **not** in `sources.list`,
    please edit and add the appropriate source to the file. For example,
    add the following if you wanted a package from the Debian repository
    that is **not** in the Cumulus Linux repository:
    
        deb http://http.us.debian.org/debian wheezy main
        deb http://security.debian.org/ wheezy/updates main
    
    Otherwise, the repository may be listed in `/etc/apt/sources.list`
    but is commented out, as can be the case with the testing
    repository:
    
        #deb http://repo.cumulusnetworks.com CumulusLinux-VERSION testing
    
    To uncomment the repository, remove the \# at the start of the line,
    then save the file:
    
        deb http://repo.cumulusnetworks.com CumulusLinux-VERSION testing

4.  Run `apt-get update` then install the package:
    
        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install {name of package}

## <span>Configuration Files</span>

  - /etc/apt/apt.conf

  - /etc/apt/preferences

  - /etc/apt/sources.list

## <span>Useful Links</span>

  - [Debian GNU/Linux FAQ, Ch 8 Package management
    tools](http://www.debian.org/doc/manuals/debian-faq/ch-pkgtools.en.html)

  - man pages for apt-get, dpkg, sources.list, apt\_preferences
