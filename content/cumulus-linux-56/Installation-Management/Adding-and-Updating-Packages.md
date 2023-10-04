---
title: Adding and Updating Packages
author: NVIDIA
weight: 80
toc: 3
---

To manage additional applications in the form of packages and to install the latest updates, use the Advanced Packaging Tool (`apt`).

{{%notice warning%}}
Updating, upgrading, and installing packages with `apt` causes disruptions to network services:
- Upgrading a package can cause services to restart or stop.
- Installing a package sometimes disrupts core services by changing core service dependency packages. In some cases, installing new packages also upgrades additional existing packages due to dependencies.
- If services stop, you need to reboot the switch to restart the services.
{{%/notice%}}

## Update the Package Cache

To work correctly, `apt` relies on a local cache listing of the available packages. You must populate the cache initially, then periodically update it with `sudo -E apt-get update`:

```
cumulus@switch:~$ sudo -E apt-get update
Ign:1 copy:/var/lib/cumulus/cumulus-local-apt-archive cumulus-local-apt-archive InRelease
Get:2 copy:/var/lib/cumulus/cumulus-local-apt-archive cumulus-local-apt-archive Release [1,115 B]
Ign:3 copy:/var/lib/cumulus/cumulus-local-apt-archive cumulus-local-apt-archive Release.gpg
Get:4 http://security.debian.org buster/updates InRelease [65.4 kB]                 
Hit:5 http://deb.debian.org/debian buster InRelease                                 
Get:6 http://deb.debian.org/debian buster-updates InRelease [51.9 kB]
Get:7 http://deb.debian.org/debian buster-backports InRelease [46.7 kB]
Get:8 http://deb.debian.org/debian buster-updates/main Sources.diff/Index [8,608 B] 
Get:9 http://deb.debian.org/debian buster-updates/main amd64 Packages.diff/Index [8,608 B]
Get:10 http://deb.debian.org/debian buster-updates/main Sources 2021-09-28-1420.03.pdiff [185 B]
Get:10 http://deb.debian.org/debian buster-updates/main Sources 2021-09-28-1420.03.pdiff [185 B]
Get:11 http://deb.debian.org/debian buster-updates/main amd64 Packages 2021-09-28-1420.03.pdiff [184 B]               
Get:11 http://deb.debian.org/debian buster-updates/main amd64 Packages 2021-09-28-1420.03.pdiff [184 B]               
Get:12 http://deb.debian.org/debian buster-backports/main Sources.diff/Index [27.8 kB]                     
Get:13 http://deb.debian.org/debian buster-backports/main amd64 Packages.diff/Index [27.8 kB]                         
Hit:14 http://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 InRelease                                            
Get:15 http://security.debian.org buster/updates/main Sources [200 kB]                             
Get:16 http://security.debian.org buster/updates/main amd64 Packages [305 kB]              
Hit:17 http://apt.cumulusnetworks.com/repo CumulusLinux-4-latest InRelease                       
Get:18 http://deb.debian.org/debian buster-backports/main Sources 2021-10-02-0801.17.pdiff [681 B]
Get:19 http://deb.debian.org/debian buster-backports/main Sources 2021-10-02-1405.24.pdiff [31 B]
Get:19 http://deb.debian.org/debian buster-backports/main Sources 2021-10-02-1405.24.pdiff [31 B]
Get:20 http://deb.debian.org/debian buster-backports/main amd64 Packages 2021-10-02-1405.24.pdiff [178 B]
Get:20 http://deb.debian.org/debian buster-backports/main amd64 Packages 2021-10-02-1405.24.pdiff [178 B]
Fetched 744 kB in 1s (982 kB/s)
Reading package lists... Done
```

{{%notice tip%}}
Use the `-E` option with `sudo` whenever you run any `apt-get` command. This option preserves your environment variables (such as HTTP proxies) before you install new packages or upgrade your distribution.
{{%/notice%}}

## List Available Packages

After the cache populates, use the `apt-cache` command to search the cache and find the packages of interest or to get information about an available package.

Here are examples of the `search` and `show` sub-commands:

```
cumulus@switch:~$ apt-cache search tcp
collectd-core - statistics collection and monitoring daemon (core system)
fakeroot - tool for simulating superuser privileges
iperf - Internet Protocol bandwidth measuring tool
iptraf-ng - Next Generation Interactive Colorful IP LAN Monitor
libfakeroot - tool for simulating superuser privileges - shared libraries
libfstrm0 - Frame Streams (fstrm) library
libibverbs1 - Library for direct userspace use of RDMA (InfiniBand/iWARP)
libnginx-mod-stream - Stream module for Nginx
libqt4-network - Qt 4 network module
librtr-dev - Small extensible RPKI-RTR-Client C library - development files
librtr0 - Small extensible RPKI-RTR-Client C library
libwiretap8 - network packet capture library -- shared library
libwrap0 - Wietse Venema's TCP wrappers library
libwrap0-dev - Wietse Venema's TCP wrappers library, development files
netbase - Basic TCP/IP networking system
nmap-common - Architecture independent files for nmap
nuttcp - network performance measurement tool
openssh-client - secure shell (SSH) client, for secure access to remote machines
openssh-server - secure shell (SSH) server, for secure access from remote machines
openssh-sftp-server - secure shell (SSH) sftp server module, for SFTP access from remote machines
python-dpkt - Python 2 packet creation / parsing module for basic TCP/IP protocols
rsyslog - reliable system and kernel logging daemon
socat - multipurpose relay for bidirectional data transfer
tcpdump - command-line network traffic analyzer
```

```
cumulus@switch:~$ apt-cache show tcpdump
Package: tcpdump
Version: 4.9.3-1~deb10u1
Installed-Size: 1109
Maintainer: Romain Francoise <rfrancoise@debian.org>
Architecture: amd64
Replaces: apparmor-profiles-extra (<< 1.12~)
Depends: libc6 (>= 2.14), libpcap0.8 (>= 1.5.1), libssl1.1 (>= 1.1.0)
Suggests: apparmor (>= 2.3)
Breaks: apparmor-profiles-extra (<< 1.12~)
Size: 400060
SHA256: 3a63be16f96004bdf8848056f2621fbd863fadc0baf44bdcbc5d75dd98331fd3
SHA1: 2ab9f0d2673f49da466f5164ecec8836350aed42
MD5sum: 603baaf914de63f62a9f8055709257f3
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
Multi-Arch: foreign
Section: net
Priority: optional
Filename: pool/upstream/t/tcpdump/tcpdump_4.9.3-1~deb10u1_amd64.deb
```

{{%notice note%}}
The search commands look for the search terms not only in the package name but in other parts of the package information; the search matches on more packages than you expect.
{{%/notice%}}

## List Packages Installed on the System

The `apt-cache` command shows information about all the packages available in the repository. To see which packages are actually installed on your system with the version, run the following command.

{{< tabs "TabID130 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv show platform software installed
Installed Package   description                                                      package                  version
-----------------   -------------------                                              ----------               --------------------
acpi                displays information on ACPI devices                             acpi                     1.7-1.1
acpi-support-base   scripts for handling base ACPI events such as the power button   acpi-support-base        0.142-8
acpid               Advanced Configuration and Power Interface event daemon          acpid                    1:2.0.31-1
...
```

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ dpkg -l
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                Version                   Architecture Description
+++-===================-=========================-============-=================================
ii  acpi                1.7-1.1                   amd64        displays information on ACPI devices
ii  acpi-support-base   0.142-8                   all          scripts for handling base ACPI events such as th
ii  acpid               1:2.0.31-1                amd64        Advanced Configuration and Power Interface event
ii  adduser             3.118                     all          add and remove users and groups
ii  apt                 1.8.2                     amd64        commandline package manager
ii  arping              2.19-6                    amd64        sends IP and/or ARP pings (to the MAC address)
ii  arptables           0.0.4+snapshot20181021-4  amd64        ARP table administration
...
```

{{< /tab >}}
{{< /tabs >}}

## Show the Version of a Package

To show the version of a specific package installed on the system:

{{< tabs "TabID202 ">}}
{{< tab "NVUE Command ">}}

The following example command shows which version of the `vrf` package is on the system:

```
cumulus@switch:~$ nv show platform software installed vrf
             running              applied  pending  description
-----------  -------------------  -------  -------  -----------
description  Linux tools for VRF                    Description
package      vrf                                    Package
version      1.0-cl5.6.0u9                         Version
```

{{< /tab >}}
{{< tab "Linux Command ">}}

The following example command shows which version of the `vrf` package is on the system:

```
cumulus@switch:~$ dpkg -l vrf
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name       Version      Architecture Description
+++-==========-============-============-=================================
ii  vrf        1.0-cl5.6.0u9    amd64        Linux tools for VRF
```

{{< /tab >}}
{{< /tabs >}}

## Upgrade Packages

To upgrade all the packages installed on the system to their latest versions, run the following commands:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get upgrade
```

The system lists the packages for upgrade and prompts you to continue.

The above commands upgrade all installed versions with their latest versions but do not install any new packages.

## Add New Packages

To add a new package, first ensure the package is not already on the system:

```
cumulus@switch:~$ dpkg -l | grep <name of package>
```

- If the package is already on the system, you can update the package from the Cumulus Linux repository as part of the package upgrade process, which upgrades all packages on the system. See {{<link url="#upgrade-packages" text="Upgrade Packages">}} above.
- If the package is *not* already on the system, add it by running `sudo -E apt-get install <name of package>`. This retrieves the package from the Cumulus Linux repository and installs it on your system together with any other dependent packages. The following example adds the `tcpreplay` package to the system:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install tcpreplay
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
tcpreplay
0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
Need to get 436 kB of archives.
After this operation, 1008 kB of additional disk space will be used
...
```

You can install several packages at the same time:

```
cumulus@switch:~$ sudo -E apt-get install <package1> <package2> <package3>
```

{{%notice tip%}}
In some cases, installing a new package also upgrades additional existing packages due to dependencies. To view these additional packages before you install, run the `apt-get install --dry-run` command.
{{%/notice%}}

## Add Packages From Another Repository

As shipped, Cumulus Linux searches the Cumulus Linux repository for available packages. You can add additional repositories to search by adding them to the list of sources that `apt-get` consults. See `man sources.list` for more information.

NVIDIA adds features or makes bug fixes to certain packages; do not replace these packages with versions from other repositories.

If you want to install packages that are not in the Cumulus Linux repository, the procedure is the same as above, but with one additional step.

{{%notice note%}}
NVIDIA does not test and Cumulus Linux Technical Support does not support packages that are not part of the Cumulus Linux repository.
{{%/notice%}}

Installing packages outside of the Cumulus Linux repository requires the use of `sudo -E apt-get`; however, depending on the package, you can use `easy-install` and other commands.

To install a new package, complete the following steps:

1. Run the `dpkg` command to ensure that the package is not already
    installed on the system:

    ```
    cumulus@switch:~$ dpkg -l | grep <name of package>
    ```

2. If the package is already on the system, ensure it is the version you need. If it is an older version, update the package from the Cumulus Linux repository:

    ```
    cumulus@switch:~$ sudo -E apt-get update
    cumulus@switch:~$ sudo -E apt-get install <name of package>
    cumulus@switch:~$ sudo -E apt-get upgrade
    ```

3. If the package is not on the system, the package source location is **not** in the `/etc/apt/sources.list` file. Edit and add the appropriate source to the file. For example, add the following if you want a package from the Debian repository that is **not** in the Cumulus Linux repository:

    ```
    deb http://http.us.debian.org/debian buster main
    deb http://security.debian.org/ buster/updates main
    ```

    Otherwise, `/etc/apt/sources.list` lists the repository but comments it out. To uncomment the repository, remove the `#` at the start of the line, then save the file.

4. Run `sudo -E apt-get update`, then install the package and upgrade:

    ```
    cumulus@switch:~$ sudo -E apt-get update
    cumulus@switch:~$ sudo -E apt-get install <name of package>
    cumulus@switch:~$ sudo -E apt-get upgrade
    ```

## Add Packages from the Cumulus Linux Local Archive

Cumulus Linux contains a local archive embedded in the Cumulus Linux image. This archive, `cumulus-local-apt-archive`, contains the packages you need to install `{{<link title="ifplugd" text="ifplugd">}}`, {{<link url="LDAP-Authentication-and-Authorization" text="LDAP">}}, {{<link url="RADIUS-AAA" text="RADIUS">}} or  {{<link url="TACACS" text="TACACS+">}} without a network connection.

The archive contains the following packages:

- audisp-tacplus
- ifplugd
- libdaemon0
- libnss-ldapd
- libnss-mapuser
- libnss-tacplus
- libpam-ldapd
- libpam-radius-auth
- libpam-tacplus
- libtac2
- libtacplus-map1
- nslcd

Add these packages with `apt-get update && apt-get install`, as {{<link url="#add-packages-from-another-repository" text="described above">}}.

## Related Information

- {{<exlink url="https://www.debian.org/doc/manuals/debian-faq/pkgtools.en.html" text="Debian GNU/Linux FAQ, Ch 8 Package management tools">}}
- man pages for `apt-get`, `dpkg`, `sources.list`, `apt_preferences`
