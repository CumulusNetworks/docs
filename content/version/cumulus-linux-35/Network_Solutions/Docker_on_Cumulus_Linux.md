---
title: Docker on Cumulus Linux
author: Cumulus Networks
weight: 237
aliases:
 - /display/CL35/Docker+on+Cumulus+Linux
 - /pages/viewpage.action?pageId=8357760
pageID: 8357760
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
Cumulus Linux 3.4 is based on Linux kernel 4.1, which supports the
[Docker](https://www.docker.com/) engine. Docker can be installed
directly on a Cumulus Linux switch, and Docker containers can be run
natively on the switch. This section covers the installation and set up
instructions for Docker.

## <span>Setting up Docker on Cumulus Linux</span>

### <span>Configure the Repositories</span>

1.  Add the following line to the end of
    `/etc/apt/sources.list.d/jessie.list` in a text editor, and save the
    file:
    
        cumulus@switch:$ sudo nano /etc/apt/sources.list.d/jessie.list
         
        ...
         
        deb http://httpredir.debian.org/debian jessie main contrib non-free
        deb-src http://httpredir.debian.org/debian jessie main contrib non-free

2.  Create the `/etc/apt/sources.list.d/docker.list` file, add the
    following line in a text editor, and save the file:
    
        cumulus@switch:$ sudo nano /etc/apt/sources.list.d/docker.list
         
        deb https://apt.dockerproject.org/repo debian-jessie main

### <span>Install the Authentication Key</span>

1.  Install the authentication key for Docker:
    
        cumulus@switch:$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

### <span>Install the docker-engine Package</span>

1.  Install Docker:
    
        cumulus@switch:$ sudo -E apt-get update -y
        cumulus@switch:$ sudo -E apt-get install docker-engine -qy

### <span>Configure systemd for Docker</span>

1.  Add `docker` as a new line at the bottom of `/etc/vrf/systemd.conf`,
    and save the file.
    
        cumulus@switch:$ sudo nano /etc/vrf/systemd.conf
         
        ...
         
        docker

2.  Create a directory for the `systemd` configuration file for Docker:
    
        cumulus@switch:$ sudo mkdir -p /etc/systemd/system/docker.service.d/

3.  In a text editor, create a file called
    `/etc/systemd/system/docker.service.d/noiptables-mgmt-vrf.conf`, add
    the following lines to it, then save the file:
    
        cumulus@switch:$ sudo nano /etc/systemd/system/docker.service.d/noiptables-mgmt-vrf.conf
         
        [Service]
        ExecStart=
        ExecStart=/usr/bin/docker daemon --iptables=false --ip-masq=false --ip-forward=false

### <span>Stop/Disable the Docker Services</span>

1.  Stop the various Docker services:
    
        cumulus@switch:$ sudo systemctl daemon-reload
        cumulus@switch:$ sudo systemctl stop docker.socket
        cumulus@switch:$ sudo systemctl disable docker.socket
        cumulus@switch:$ sudo systemctl stop docker.service
        cumulus@switch:$ sudo systemctl disable docker.service

### <span>Launch Docker and the Ubuntu Container</span>

1.  Enable the Docker management daemon so it starts when the switch
    boots:
    
        cumulus@switch:$ sudo systemctl enable docker@mgmt

2.  Start the Docker management daemon:
    
        cumulus@switch:$ sudo systemctl start docker@mgmt

3.  Run the Ubuntu container and launch the terminal instance:
    
        cumulus@switch:$ docker run -i -t ubuntu /bin/bash

## <span>Performance Notes</span>

Keep in mind switches are not servers, in terms of the hardware that
drives them. As such, you should be mindful of the types of applications
you want to run in containers on a Cumulus Linux switch. In general,
depending upon the configuration of the container, you can expect DHCP
servers, custom scripts and other lightweight services to run well.
However, VPN, NAT and encryption-type services are CPU-intensive and
could lead to undesirable effects on critical applications. Use of any
resource-intensive services should be avoided and is not supported.
