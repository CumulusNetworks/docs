---
title: Installing NetQ on the Host
author: Cumulus Networks
weight: 15
aliases:
 - /display/HOSTPACK/Installing+NetQ+on+the+Host
 - /pages/viewpage.action?pageId=7110684
pageID: 7110684
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
NetQ on the Host is the version of NetQ you install on physical servers
and in container hosts.

## <span>Install on an Ubuntu Server</span>

Before you install the NetQ Agent on an Ubuntu server, make sure the
following packages are installed and running these minimum versions:

  - docker-ce 17.06.1\~ce-0\~ubuntu amd64
    
    {{%notice note%}}
    
    This package is required only if you plan to monitor Docker
    instances on the host; otherwise do not install it.
    
    {{%/notice%}}

  - iproute 1:4.3.0-1ubuntu3.16.04.1 all

  - iproute2 4.3.0-1ubuntu3 amd64

  - lldpd 0.7.19-1 amd64
    
    {{%notice note%}}
    
    Make sure you are running **lldpd**, not lldpad.
    
    Ubuntu does not include `lldpd` by default, which is required for
    the installation. To install this package, run the following
    commands:
    
        root@ubuntu:~# apt-get update
        root@ubuntu:~# apt-get install lldpd
        root@ubuntu:~# systemctl enable lldpd.service
        root@ubuntu:~# systemctl start lldpd.service
    
    {{%/notice%}}

  - ntp 1:4.2.8p4+dfsg-3ubuntu5.6 amd64

To install the NetQ Agent on an Ubuntu server:

1.  Reference and update the local `apt` repository:
    
        root@ubuntu:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-deb.pubkey | apt-key add -

2.  Create the file
    `/etc/apt/sources.list.d/cumulus-host-ubuntu-xenial.list` and add
    the following lines:
    
        root@ubuntu:~# vi /etc/apt/sources.list.d/cumulus-apps-deb-xenial.list
         
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial netq-latest
        deb [arch=amd64] https://apps3.cumulusnetworks.com/repos/deb xenial roh-3
    
    {{%notice note%}}
    
    Mentioning `netq-latest` above means always upgrade, even in the
    case of a major version. If you want to keep the repository on a
    specific version — such as `netq-1.3` — use that instead.
    
    {{%/notice%}}

3.  Install NTP on the server:
    
        root@ubuntu:~# apt install ntp
        root@ubuntu:~# systemctl enable ntp
        root@ubuntu:~# systemctl start ntp

4.  Install the metapackage on the server:
    
        root@ubuntu:~# apt-get update ; apt-get install cumulus-netq

5.  Restart the NetQ daemon:
    
        root@ubuntu:~# systemctl enable netqd ; systemctl restart netqd

## <span>Install on a Red Hat or CentOS Server</span>

Before you install the NetQ Agent on a Red Hat or CentOS server, make
sure the following packages are installed and running these minimum
versions:

  - iproute-3.10.0-54.el7\_2.1.x86\_64

  - lldpd-0.9.7-5.el7.x86\_64
    
    {{%notice note%}}
    
    Make sure you are running **lldpd**, not lldpad.
    
    CentOS does not include `lldpd` by default, nor does it include
    `wget`, which is required for the installation. To install these
    packages, run the following commands:
    
        root@centos:~# yum -y install epel-release
        root@centos:~# yum -y install lldpd
        root@centos:~# systemctl enable lldpd.service
        root@centos:~# systemctl start lldpd.service
        root@centos:~# yum install wget
    
    {{%/notice%}}

  - ntp-4.2.6p5-25.el7.centos.2.x86\_64

  - ntpdate-4.2.6p5-25.el7.centos.2.x86\_64

To install the NetQ Agent on a Red Hat or CentOS server:

1.  Reference and update the local `yum` repository:
    
        root@rhel7:~# rpm --import https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm.pubkey
        root@rhel7:~# wget -O- https://apps3.cumulusnetworks.com/setup/cumulus-apps-rpm-el7.repo > /etc/yum.repos.d/cumulus-host-el.repo

2.  Edit `/etc/yum.repos.d/cumulus-host-el.repo` to set the `enabled=1`
    flag for the two NetQ repositories:
    
        root@rhel7:~# vi /etc/yum.repos.d/cumulus-host-el.repo
         
        [cumulus-arch-netq-1.1]
        name=Cumulus netq packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-1.1/$basearch 
        gpgcheck=1
        enabled=1
        [cumulus-noarch-netq-1.1]
        name=Cumulus netq architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/netq-1.1/noarch
        gpgcheck=1
        enabled=1
         
        [cumulus-arch-roh-3]
        name=Cumulus roh packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/roh-3/$basearch 
        gpgcheck=1
        enabled=0
         
        [cumulus-noarch-roh-3]
        name=Cumulus roh architecture-independent packages
        baseurl=https://apps3.cumulusnetworks.com/repos/rpm/el/7/roh-3/noarch
        gpgcheck=1
        enabled=0

3.  Install NTP on the server:
    
        root@ubuntu:~# yum install ntp
        root@ubuntu:~# systemctl enable ntpd
        root@ubuntu:~# systemctl start ntpd

4.  Install the Bash completion and NetQ metapackages on the server:
    
        root@rhel7:~# yum -y install bash-completion
        root@rhel7:~# yum install cumulus-netq
