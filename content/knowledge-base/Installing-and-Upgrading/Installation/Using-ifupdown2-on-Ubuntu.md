---
title: Using ifupdown2 on Ubuntu
author: NVIDIA
weight: 255
toc: 4
---

<!-- vale off -->
`ifupdown2` improves network configuration for standard Debian and Ubuntu instances and is the standard interface configuration tool for Cumulus Linux since release 2.1. This article describes how to install `ifupdown2` on Ubuntu hosts.
<!-- vale on -->

## Verify Ubuntu Version

Before you start the install, verify the version of Ubuntu installed on the instance:

    user@host:~$ cat /etc/lsb-release
    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=14.04
    DISTRIB_CODENAME=trusty
    DISTRIB_DESCRIPTION="Ubuntu 14.04.3 LTS"

Follow the appropriate instructions below for your installed version of Ubuntu.

## Installing ifupdown2 on an Ubuntu Host
<!-- vale off -->
### Ubuntu 16.04 Xenial
<!-- vale on -->
The default package list for Ubuntu 16.04 includes`ifupdown2`. The package is available here: {{<exlink url="http://packages.ubuntu.com/xenial/ifupdown2" text="ifupdown2">}}.

1. Open `/etc/apt/sources.list` in an editor.

2. Uncomment the following line, and save the file:

        deb http://us.archive.ubuntu.com/ubuntu/ xenial universe

3.  Update the Ubuntu instance:

        user@host:~$ sudo apt-get update

4.  Install the `ifupdown2` package:

        user@host:~$ sudo apt-get install ifupdown2

5.  Make sure the following configuration is present in the `systemd` file:

        [Unit]
        Description=ifupdown2 init script
        
        [Service]
        Type=oneshot
        ExecStart=/sbin/ifup -a
        ExecStop=/sbin/ifdown -a
        RemainAfterExit=yes
        
        [Install]
        WantedBy=multi-user.target
<!-- vale off -->
### Ubuntu 14.04 Trusty
<!-- vale on -->
The default package list for Ubuntu 14.04 does **not** include `ifupdown2`. However, as Ubuntu 16.04 includes it, you can work around this restriction by upgrading.

{{%notice tip%}}

An {{<exlink url="https://gist.github.com/ericpulvino/5f7eabb7058e3076a7b5f2e357f0ca0b" text="Ansible playbook is available">}} to automate these tasks.

{{%/notice%}}

1.  Enter the *root* account. The remaining commands in these instructions assume use of the root account.

2.  Add the Ubuntu Xenial sources to your Ubuntu Trusty installation:

        root@host# echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial universe" > /etc/apt/sources.list.d/xenial.list

3.  Update the Ubuntu package cache. You might see warnings in the output, which you can ignore:

        root@host# apt-get update
        <snip>
        Ign http://us.archive.ubuntu.com trusty/multiverse Translation-en_US
        Ign http://us.archive.ubuntu.com trusty/restricted Translation-en_US
        Ign http://us.archive.ubuntu.com trusty/universe Translation-en_US
        Reading package lists... Done 
        W: Unknown Multi-Arch type 'no' for package 'libkf5akonadisearch-bin'
        W: Ignoring Provides line with DepCompareOp for package php-psr-http-message-implementation
        W: Ignoring Provides line with DepCompareOp for package php-psr-log-implementation
        W: Ignoring Provides line with DepCompareOp for package php-math-biginteger
        W: Unknown Multi-Arch type 'no' for package 'libkf5akonadisearch-bin'
        W: You may want to run apt-get update to correct these problems

4.  **Important**: After the initial configuration, the repositories have equal preference for installing packages, resulting in the installation of the newest (Xenial) packages. As the goal of this article is to install `ifupdown2` only, this step ensures that you install the Trusty packages first.

    Before continuing, you must either raise the priority for the Trusty repository  or lower the priority of the Xenial repository. The example steps below show how to lower the priority of the Xenial repository, ensuring you install the Trusty packages first, and Xenial packages are only installed if no Trusty package exists:

    1.  Create a file called `/etc/apt/preferences.d/xenial` and add the following text to the file, then save the file:

            Explanation: give xenial a low priority number
            Package: *
            Pin: release a=xenial
            Pin-Priority: 100

        Or, run this command to perform the same task:

            root@host# echo -e "Explanation: give xenial a low priority number\nPackage: *\nPin: release a=xenial\nPin-Priority: 100\n" > /etc/apt/preferences.d/xenial

    2.  Verify that Xenial packages do not override all other packages. The example below uses the Ansible package for verification, as different versions are available on Trusty (Ansible 1.5.4), and Xenial (Ansible 1.9.4):

            root@host# apt-cache policy ansible
            ansible:
              Installed: (none)
              Candidate: 1.5.4+dfsg-1
              Version table:
                 1.9.4-1 0
                    100 http://us.archive.ubuntu.com/ubuntu/ xenial/universe amd64 Packages
                 1.7.2+dfsg-1~ubuntu14.04.1 0
                    100 http://us.archive.ubuntu.com/ubuntu/ trusty-backports/universe amd64 Packages
                 1.5.4+dfsg-1 0
                    500 http://us.archive.ubuntu.com/ubuntu/ trusty/universe amd64 Packages

        The `Candidate` above is *1.5.4*, and you lowered the Xenial priority from *500* to *100*, which means that Xenial packages do not override Trusty repository packages.

5.  Install the `ifupdown2` package dependencies:

        root@host# apt-get install python-ipaddr python-argcomplete python-gvgen python-mako  

6.  Place a hold on the `ifupdown` package:

        root@host# echo ifupdown hold | dpkg --set-selections

7.  Download the `ifupdown2 package:`

        root@host# apt-get download ifupdown2

8.  Manually install the `ifupdown2` package:

        root@host# dpkg --force-conflicts --force-depends --force-overwrite -i ./ifupdown2*.deb
        Selecting previously unselected package ifupdown2.
        dpkg: considering removing ifupdown in favour of ifupdown2 ...
        dpkg: warning: ignoring dependency problem with removal of ifupdown:
         upstart depends on ifupdown (>= 0.6.10ubuntu5)
         ifupdown is to be removed.
        
        Package ifupdown is on hold, not touching it. Use --force-hold to override.
        dpkg: regarding .../ifupdown2_1.0~git20151029-1_all.deb containing ifupdown2:
         ifupdown2 conflicts with ifupdown
         ifupdown (version 0.7.47.2ubuntu4.1) is present and installed.
        
        dpkg: warning: ignoring conflict, may proceed anyway!
        (Reading database ... 197912 files and directories currently installed.)
        Preparing to unpack .../ifupdown2_1.0~git20151029-1_all.deb ...
        Unpacking ifupdown2 (1.0~git20151029-1) ...
        Replacing files in old package ifupdown (0.7.47.2ubuntu4.1) ...
        dpkg: ifupdown2: dependency problems, but configuring anyway as you requested:
         ifupdown2 depends on init-system-helpers (>= 1.18~); however:
         Version of init-system-helpers on system is 1.14.
        
        Setting up ifupdown2 (1.0~git20151029-1) ...
        Installing new version of config file /etc/init.d/networking ...
        update-rc.d: warning: default start runlevel arguments (2 3 4 5) do not match networking Default-Start values (S)
        Processing triggers for man-db (2.6.7.1-1ubuntu1) ...
        Processing triggers for ureadahead (0.100.0-16) ...
        ureadahead will be reprofiled on next reboot

9.  Examine the "Depends" and "Conflicts" lines from the installed `ifupdown2` package.

    <pre>root@host# grep -A 34 "Package: ifupdown2" /var/lib/dpkg/status<br />Package: ifupdown2<br />Status: install ok installed<br />Priority: optional<br />Section: admin<br />Installed-Size: 595<br />Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com><br />Architecture: all<br />Version: 1.0~git20151029-1<br />Replaces: ifupdown<br />Provides: ifupdown<br /><span style="color:red;">Depends: python:any (>= 2.7.5-5~), init-system-helpers (>= 1.18~), python-argcomplete, python-ipaddr</span><br />Suggests: python-gvgen, python-mako<br /><span style="color:red;">Conflicts: ifupdown</span><br />Conffiles:<br />/etc/default/networking/networking.default 76a6935f125a8db5cbcddee1d422fc81<br />/etc/init.d/networking 703fab9e50c7c539efc6e1ce6b9c7633<br />/etc/network/ifupdown2/addons.conf c39be66aa58f59b4343c9dc6541043fe<br />/etc/network/ifupdown2/ifupdown2.conf 85fd2d75c77c6b68438a16888ae08510<br />Description: Network Interface Management tool similar to ifupdown<br /> ifupdown2 is ifupdown re-written in Python. It replaces ifupdown and provides<br /> the same user interface as ifupdown for network interface configuration.<br /> Like ifupdown, ifupdown2 is a high level tool to configure (or, respectively<br /> deconfigure) network interfaces based on interface definitions in<br /> /etc/network/interfaces. It is capable of detecting network interface<br /> dependencies and comes with several new features which are available as<br /> new command options to ifup/ifdown/ifquery commands. It also comes with a new<br /> command ifreload to reload interface configuration with minimum<br /> disruption. Most commands are also capable of input and output in JSON format.<br /> It is backward compatible with ifupdown /etc/network/interfaces format and<br /> supports newer simplified format. It also supports interface templates with<br /> python-mako for large scale interface deployments. See<br /> /usr/share/doc/ifupdown2/README.rst for details about ifupdown2. Examples<br /> are available under /usr/share/doc/ifupdown2/examples.<br /> Original-Maintainer: Roopa Prabhu <roopa@nvidia.com><br /> Homepage: https://github.com/CumulusNetworks/ifupdown2</pre>

10. **Optional:** At this point you need to amend the package manager's understanding of the dependencies and conflicts for the `ifupdown2` package. This requires two very precise edits to the `/var/lib/dpkg/status` file. To ensure that those edits produce the desired changes, first confirm that the two find-and-replaces that you are performing in Step 11 each only have one instance to replace.

        root@host# grep -c "Conflicts: ifupdown" /var/lib/dpkg/status
        1
        root@host# grep -c "Depends: python:any (>= 2.7.5-5~), init-system-helpers (>= 1.18~), python-argcomplete, python-ipaddr" /var/lib/dpkg/status
        1

11. Update the package manager with new dependency and conflict information for the `ifupdown2` package by using the `sed` command to find and replace the two lines (shown in red during Step 9):

        root@host# sed -i "s/Depends: python:any (>= 2.7.5-5~), init-system-helpers (>= 1.18~), python-argcomplete, python-ipaddr/Depends: python:any (>= 2.7.5-5~), init-system-helpers (>= 1.14~), python-argcomplete, python-ipaddr/g" /var/lib/dpkg/status
    
        root@host# sed -i "/Conflicts: ifupdown/d" /var/lib/dpkg/status

12. Confirm you made your edits to the file successfully. Note that you changed the minimum required `init-system-helpers` version from *1.18* to *1.14* and you removed the `Conflicts` line when compared to Step 9:

        root@host# grep -A 34 "Package: ifupdown2" /var/lib/dpkg/status
        Package: ifupdown2
        Status: install ok installed
        Priority: optional
        Section: admin
        Installed-Size: 595
        Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
        Architecture: all
        Version: 1.0~git20151029-1
        Replaces: ifupdown
        Provides: ifupdown
        Depends: python:any (>= 2.7.5-5~), init-system-helpers (>= 1.14~), python-argcomplete, python-ipaddr
        Suggests: python-gvgen, python-mako
        Conffiles:
         /etc/default/networking/networking.default 76a6935f125a8db5cbcddee1d422fc81
         /etc/init.d/networking 703fab9e50c7c539efc6e1ce6b9c7633
         /etc/network/ifupdown2/addons.conf c39be66aa58f59b4343c9dc6541043fe
         /etc/network/ifupdown2/ifupdown2.conf 85fd2d75c77c6b68438a16888ae08510
        Description: Network Interface Management tool similar to ifupdown
         ifupdown2 is ifupdown re-written in Python. It replaces ifupdown and provides
         the same user interface as ifupdown for network interface configuration.
         Like ifupdown, ifupdown2 is a high level tool to configure (or, respectively
         deconfigure) network interfaces based on interface definitions in
         /etc/network/interfaces. It is capable of detecting network interface
         dependencies and comes with several new features which are available as
         new command options to ifup/ifdown/ifquery commands. It also comes with a new
         command ifreload to reload interface configuration with minimum
         disruption. Most commands are also capable of input and output in JSON format.
         It is backward compatible with ifupdown /etc/network/interfaces format and
         supports newer simplified format. It also supports interface templates with
         python-mako for large scale interface deployments. See
         /usr/share/doc/ifupdown2/README.rst for details about ifupdown2. Examples
         are available under /usr/share/doc/ifupdown2/examples.
        Original-Maintainer: Roopa Prabhu <roopa@cumulusnetworks.com>
        Homepage: https://github.com/CumulusNetworks/ifupdown2

13. Disable the Xenial package repository until you need it again:

        root@host# sed -i "s/deb/#deb/g" /etc/apt/sources.list.d/xenial.list

14. Update the Ubuntu package cache again to remove the Xenial sources from the package cache.

        root@host# apt-get update

## Verifying ifupdown2

After the `ifupdown2` installation finishes, you can use `ifupdown2`-specific commands to test and verify:

    user@host:~$ sudo ifquery -ra
    auto lo
    iface lo inet loopback
        mtu 65536
    
    auto eth0
    iface eth0
        address 10.50.10.160/24
        link-speed 1000
        link-duplex full
        link-autoneg on

### Installing Other Tools

In addition, you can install the `brctl` and `bridge` commands so the host more closely resembles Cumulus Linux. These commands let you get information and configure your bridges:

    user@host:~$ sudo apt-get install bridge-utils

You can now review bridges on the host in the same way as in Cumulus Linux:

    user@host:~$ ifquery -a
    auto lo
    iface lo inet loopback
    
    auto eth0
    iface eth0 inet dhcp
    
    auto bridge
    iface bridge
        bridge-ports eth1
        bridge-stp on

Use the `brctl` command to look at the bridge STP state:

    user@host:~$ brctl show
    bridge name bridge id       STP enabled interfaces
    bridge      8000.080027d73d5d   yes     eth1

## Removing ifupdown2

1.  Remove the package in the normal Debian/Ubuntu manner:  

        sudo apt-get remove ifupdown2

2.  **On Ubuntu 14.04 only**:  

        sudo apt-get install ifupdown --reinstall

## Further Reading

- {{<link title="Compare ifupdown2 Commands with ifupdown Commands" text="Comparing ifupdown2 Commands with ifupdown Commands">}}
- {{<exlink url="https://packages.debian.org/sid/ifupdown2" text="ifupdown2 on Debian">}}
