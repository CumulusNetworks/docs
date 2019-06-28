---
title: Docker on Cumulus Linux
author: Cumulus Networks
weight: 223
aliases:
 - /display/CL321/Docker+on+Cumulus+Linux
 - /pages/viewpage.action?pageId=5127082
pageID: 5127082
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
Cumulus Linux 3.2 is based on Linux kernel 4.1, which supports the
[Docker](https://www.docker.com/) engine. This means you can install
Docker directly on a Cumulus Linux switch and you can run Docker
containers natively on the switch.

    cumulus@switch:~$ uname -r
    4.1.0-cl-1-amd64

## <span>Installing Docker</span>

Before installing Docker, add the Debian Jessie `apt` repository to
Cumulus Linux:

    cumulus@switch:~$ echo "deb http://ftp.us.debian.org/debian/ jessie main contrib non-free" | sudo tee -a /etc/apt/sources.list

To install the Docker Engine, follow the
[instructions](https://docs.docker.com/engine/installation/linux/debian/)
for installing it on Debian Linux, as they work for Cumulus Linux as is.

{{%notice tip%}}

There's a community-supported Ansible playbook for installing Docker on
Cumulus Linux on
[GitHub](https://github.com/plumbis/demos/blob/master/install_docker.yml).

{{%/notice%}}

### <span>Verifying the Docker Install</span>

Docker provides a "Hello World" testing application that can be run on
Cumulus Linux to validate that Docker Engine was installed correctly.

    cumulus@switch:~$ docker run ubuntu /bin/echo 'Hello world'
    Hello world

## <span>Caveats and Errata</span>

### <span>iptables and Docker</span>

By default, Docker Engine creates `iptables` rules to manage Docker
container connectivity and provide IP masquerade (NAT). Docker Engine
adds NAT entries to the *nat* table.These ACL rules do not properly sync
with the hardware of Cumulus Linux, so when you run `cl-acltool -i` to
install new hardware based ACLs, the Docker Engine rules get removed.

When using Docker Engine on Cumulus Linux, you must disable the
`iptables` functionality within Docker Engine. To do so, use the
`--iptables=false` option when you start Docker Engine. To do this
automatically, you can modify the `systemd` service startup parameters:

1.  Create the directory `/etc/systemd/system/docker.service.d`:
    
        cumulus@switch:~$ sudo mkdir /etc/systemd/system/docker.service.d

2.  Create the file
    `/etc/systemd/system/docker.service.d/noiptables.conf`: and populate
    it with the following:
    
        cumulus@switch:~$ sudo nano /etc/systemd/system/docker.service.d/noiptables.conf
         
        [Service]
        ExecStart=
        ExecStart=/usr/bin/docker daemon -H fd:// --iptables=false

3.  Reload the `systemd` configuration settings; this has no impact on
    currently running services.
    
        cumulus@switch:~$ sudo systemctl daemon-reload

4.  If Docker Engine was already started, reset the nat table entries,
    then reset the software `iptables` rules:
    
        cumulus@switch:~$ sudo iptables -t nat -F
        cumulus@switch:~$ sudo cl-acltool -i

5.  Restart the Docker Engine:
    
        cumulus@switch:~$ sudo systemctl restart docker.service

To check if the Docker Engine `iptables` rules have been installed, run
`iptables -L DOCKER` to print the current software `iptables` rules. If
the Docker Engine `iptables` rules are installed, you will see output
similar to the following:

    cumulus@switch:~$ sudo iptables -L DOCKER
    Chain DOCKER (1 references)
    target prot opt source destination
    cumulus@switch:~$

If the Docker Engine `iptables` rules are not installed, an error gets
returned:

    cumulus@switch:~$ sudo iptables -L DOCKER
    iptables: No chain/target/match by that name.

### <span>Management VRF and Docker</span>

If you have a management VRF configured on a Cumulus Linux 3.0.z switch,
you cannot run Docker commands that go to another node (for example,
`docker pull`) over the management VRF.
