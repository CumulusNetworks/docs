---
title: Docker on Cumulus Linux
author: NVIDIA
weight: 253
pageID: 8362980
---
Cumulus Linux is based on Linux kernel 4.1, which supports the
{{<exlink url="https://www.docker.com/" text="Docker">}} engine. Docker can be installed
directly on a Cumulus Linux switch, and Docker containers can be run
natively on the switch. This section covers the installation and set up
instructions for Docker.

## Set up Docker on Cumulus Linux

### Configure the Repositories

1.  Add the following line to the end of
    `/etc/apt/sources.list.d/jessie.list` in a text editor, and save the
    file:

        cumulus@switch:$ sudo nano /etc/apt/sources.list.d/jessie.list
         
        ...
         
        deb http://httpredir.debian.org/debian jessie main contrib non-free
        deb-src http://httpredir.debian.org/debian jessie main contrib non-free

2.  Create the `/etc/apt/sources.list.d/docker.list` file, add the
    following line in a text editor, and save the file:

        cumulus@switch:$ sudo nano /etc/apt/sources.list.d/docker.list
         
        deb https://download.docker.com/linux/debian jessie stable

### Install the Authentication Key

Install the authentication key for Docker:

        cumulus@switch:$ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

        cumulus@switch:$ sudo apt-key finger
        ...
        pub   4096R/0EBFCD88 2017-02-22
              Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
        uid                  Docker Release (CE deb) <docker@docker.com>
        sub   4096R/F273FCD8 2017-02-22

### Install the docker-engine Package

Install Docker:

        cumulus@switch:$ sudo -E apt-get update -y
        cumulus@switch:$ sudo -E apt-get install docker-ce -qy

### Configure systemd for Docker

1.  Add `docker` as a new line at the bottom of `/etc/vrf/systemd.conf`,
    and save the file.

        cumulus@switch:$ sudo nano /etc/vrf/systemd.conf
         
        ...
         
        docker

2.  Create the directory for the `systemd` configuration file for Docker:

        cumulus@switch:$ sudo mkdir -p /etc/systemd/system/docker.service.d/

3.  In a text editor, create a file called
    `/etc/systemd/system/docker.service.d/noiptables-mgmt-vrf.conf`, add
    the following lines to it, then save the file:

        cumulus@switch:$ sudo nano /etc/systemd/system/docker.service.d/noiptables-mgmt-vrf.conf
         
        [Service]
        ExecStart=
        ExecStart=/usr/bin/dockerd --iptables=false --ip-masq=false --ip-forward=false

4.  In a text editor, edit a file called `/lib/systemd/system/docker.service`,
    and comment out the line starting with `Delegate`:

        cumulus@switch:$ sudo nano /lib/systemd/system/docker.service
        
        [Service]
        ...
        #Delegate=yes
        ...

5.  In a text editor, create a file called `/etc/docker/daemon.json`, add
    the following line to it, then save the file:

        cumulus@switch:$ sudo nano /etc/docker/daemon.json

        {"exec-opts": ["native.cgroupdriver=systemd"]}

### Stop/Disable the Docker Services

Stop the various Docker services:

        cumulus@switch:$ sudo systemctl daemon-reload
        cumulus@switch:$ sudo systemctl stop docker.service docker.socket
        cumulus@switch:$ sudo systemctl disable docker.service docker.socket

### Launch Docker and the Ubuntu Container

1.  Enable the Docker management daemon so it starts when the switch
    boots:

        cumulus@switch:$ sudo systemctl enable docker@mgmt

2.  Start the Docker management daemon:

        cumulus@switch:$ sudo systemctl start docker@mgmt

3.  Run the Ubuntu container and launch the terminal instance:

        cumulus@switch:$ docker run -i -t ubuntu /bin/bash

## Performance Notes

Keep in mind switches are not servers, in terms of the hardware that
drives them. As such, you should be mindful of the types of applications
you want to run in containers on a Cumulus Linux switch. In general,
depending upon the configuration of the container, you can expect DHCP
servers, custom scripts and other lightweight services to run well.
However, VPN, NAT and encryption-type services are CPU-intensive and
could lead to undesirable effects on critical applications. Use of any
resource-intensive services should be avoided and is not supported.
