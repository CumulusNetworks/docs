---
title: Adding and Updating Packages
author: Cumulus Networks
weight: 133
aliases:
 - /display/RMP25ESR/Adding+and+Updating+Packages
 - /pages/viewpage.action?pageId=5116321
pageID: 5116321
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
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
    Ign https://repo.cumulusnetworks.com CumulusRMP-2.5.3 Release.gpg
    Get:1 https://repo.cumulusnetworks.com CumulusRMP-2.5.3 Release [9027 B]
    Get:2 https://repo.cumulusnetworks.com CumulusRMP-2.5.3/main powerpc Packages [105 kB]
    Get:3 https://repo.cumulusnetworks.com CumulusRMP-2.5.3/extras powerpc Packages [20 B]
    Get:4 https://repo.cumulusnetworks.com CumulusRMP-2.5.3/updates powerpc Packages [20 B]
    Get:5 https://repo.cumulusnetworks.com CumulusRMP-2.5.3/security-updates powerpc Packages [20 B]
    Ign https://repo.cumulusnetworks.com CumulusRMP-2.5.3/extras Translation-en
    Ign https://repo.cumulusnetworks.com CumulusRMP-2.5.3/main Translation-en
    Ign https://repo.cumulusnetworks.com CumulusRMP-2.5.3/security-updates Translation-en
    Ign https://repo.cumulusnetworks.com CumulusRMP-2.5.3/updates Translation-en
    Fetched 115 kB in 2s (56.3 kB/s)
    Reading package lists... Done

## <span>Listing Available Packages</span>

Once the cache is populated, use `apt-cache` to search the cache to find
the packages you are interested in or to get information about an
available package. Here are examples of the `search` and `show`
sub-commands:

    cumulus@switch:~$ apt-cache search tcp
    fakeroot - tool for simulating superuser privileges
    libwrap0 - Wietse Venema's TCP wrappers library
    libwrap0-dev - Wietse Venema's TCP wrappers library, development files
    netbase - Basic TCP/IP networking system
    nmap - The Network Mapper
    openbsd-inetd - OpenBSD Internet Superserver
    openssh-client - secure shell (SSH) client, for secure access to remote machines
    openssh-server - secure shell (SSH) server, for secure access from remote machines
    rsyslog - reliable system and kernel logging daemon
    socat - multipurpose relay for bidirectional data transfer
    tcpd - Wietse Venema's TCP wrapper utilities
    tcpdump - command-line network traffic analyzer
    tcpreplay - Tool to replay saved tcpdump files at arbitrary speeds
    tcpstat - network interface statistics reporting tool
    tcptrace - Tool for analyzing tcpdump output
    tcpxtract - extracts files from network traffic based on file signatures
    quagga - BGP/OSPF/RIP routing daemon
    jdoo - utility for monitoring and managing daemons or similar programs
    
    cumulus@switch:~$ apt-cache show tcpreplay
    Package: tcpreplay
    Version: 3.4.3-2+wheezy1
    Architecture: powerpc
    Maintainer: Noël Köthe <noel@debian.org>
    Installed-Size: 984
    Depends: libc6 (>= 2.7), libpcap0.8 (>= 0.9.8)
    Homepage: http://tcpreplay.synfin.net/
    Priority: optional
    Section: net
    Filename: pool/main/t/tcpreplay/tcpreplay_3.4.3-2+wheezy1_powerpc.deb
    Size: 435904
    SHA256: 03dc29057cb608d2ddf08207aedf18d47988ed6c23db0af69d30746768a639ae
    SHA1: 8ee1b9b02dacd0c48a474844f4466eb54c7e1568
    MD5sum: cf20bec7282ef77a091e79372a29fe1e
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
If it’s an older version, then update the package from the Cumulus RMP
repository:

    cumulus@switch:~$ sudo apt-get update

If the package is not already on the system, add it by running `apt-get
install`. This retrieves the package from the Cumulus RMP repository and
installs it on your system together with any other packages that this
package might depend on.

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
    Get:1 https://repo.cumulusnetworks.com/ CumulusRMP-2.5.3/main tcpreplay powerpc 3.4.3-2+wheezy1 [436 kB]
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

### <span>Upgrading All Packages</span>

You can update all packages on the system with `apt-get update`. This
upgrades all installed versions with their latest versions but will not
install any new packages.

## <span>Adding Packages from Another Repository</span>

As shipped, Cumulus RMP searches the Cumulus RMP repository for
available packages. You can add additional repositories to search by
adding them to the list of sources that `apt-get` consults. See `man
sources.list` for more information.

{{%notice tip%}}

For several packages, Cumulus Networks has added features or made bug
fixes and these packages must not be replaced with versions from other
repositories. Cumulus RMP has been configured to ensure that the
packages from the Cumulus RMP repository are always preferred over
packages from other repositories.

{{%/notice%}}

If you want to install packages that are not in the Cumulus RMP
repository, the procedure is the same as above with one additional step.

{{%notice note%}}

Packages not part of the Cumulus RMP repository have generally not been
tested, and may not be supported by Cumulus RMP support.

{{%/notice%}}

Installing packages outside of the Cumulus RMP repository requires the
use of `apt-get`, but, depending on the package, `easy-install` and
other commands can also be used.

To install a new package, please complete the following steps:

1.  First, ensure package is not already installed in the system. Use
    the `dpkg` command:
    
        cumulus@switch:~$ dpkg -l | grep {name of package}

2.  If the package is installed already, ensure it's the version you
    need. If it's an older version, then update the package from the
    Cumulus RMP repository:
    
        cumulus@switch:~$ sudo apt-get update
        cumulus@switch:~$ sudo apt-get install {name of package}

3.  If the package is not on the system, then most likely the package
    source location is also **not** in the `/etc/apt/sources.list` file.
    If the source for the new package is **not** in `sources.list`,
    please edit and add the appropriate source to the file. For example,
    add the following if you wanted a package from the Debian repository
    that is **not** in the Cumulus RMP repository:
    
        deb http://http.us.debian.org/debian wheezy main
        deb http://security.debian.org/ wheezy/updates main
    
    Otherwise, the repository may be listed in /etc/apt/sources.list but
    is commented out, as can be the case with the testing repository:
    
    ``` 
                #deb http://repo.cumulusnetworks.com CumulusRMP-VERSION testing
    ```
    
    To uncomment the repository, remove the \# at the start of the line,
    then save the file:
    
        deb http://repo.cumulusnetworks.com CumulusRMP-VERSION testing

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
