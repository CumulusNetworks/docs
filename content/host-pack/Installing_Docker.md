---
title: Installing Docker
author: Cumulus Networks
weight: 19
aliases:
 - /display/HOSTPACK/Installing+Docker
 - /pages/viewpage.action?pageId=7110689
pageID: 7110689
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
Before using a Docker container, you must first install Docker. The
following steps were done on an Ubuntu 16.04 host.

1.  Add the Docker repository key.
    
        root@host:~# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

2.  Install the Docker repository.
    
        root@host:~# echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

3.  Update the package lists.
    
        root@host:~# apt-get update

4.  Install Docker on the Ubuntu host.
    
        root@host:~# apt-get install -y docker-ce

5.  Check that the Docker service is running on the Ubuntu 16.04 host.
    
        root@host:~# systemctl status docker
        ● docker.service - Docker Application Container Engine
           Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
           Active: active (running) since Wed 2017-10-18 02:51:48 UTC; 1min 42s ago
             Docs: https://docs.docker.com
         Main PID: 18661 (dockerd)
           CGroup: /system.slice/docker.service
                   ├─18661 /usr/bin/dockerd -H fd://
                   └─18666 docker-containerd -l unix:///var/run/docker/libcontainerd/docker-containerd.sock --metrics-interval=0 --start-timeout 2m --state-dir /var/run/docker/libcontainerd/containerd --shim docker-containerd-shim --runtime docker-runc

6.  **Optional:** Add the docker group to your user account to be able
    to run docker commands without using sudo.
    
        user@host:~$ sudo adduser ${USER} docker
    
    {{%notice note%}}
    
    Adding groups to different users requires a logout and login to take
    effect.
    
    {{%/notice%}}
