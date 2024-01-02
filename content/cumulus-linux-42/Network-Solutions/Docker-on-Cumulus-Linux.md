---
title: Docker on Cumulus Linux
author: NVIDIA
weight: 1310
toc: 3
---
You can use Cumulus Linux to run the {{<exlink url="https://www.docker.com/" text="Docker">}} container platform. You can install Docker Engine directly on a Cumulus Linux switch and run Docker containers natively on the switch.

To run Docker containers on the Cumulus Linux switch:

1. Install the Docker package:

```
cumulus@switch:mgmt:~$ sudo -E apt-get update
cumulus@switch:mgmt:~$ sudo -E apt-get install cumulus-docker-setup
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
 containerd.io docker-ce docker-ce-cli
Suggested packages:
 aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
 apparmor docker-ce-rootless-extras libltdl7 pigz
The following NEW packages will be installed:
 containerd.io cumulus-docker-setup docker-ce docker-ce-cli
0 upgraded, 4 newly installed, 0 to remove and 6 not upgraded.
Need to get 91.9 MB of archives.
After this operation, 420 MB of additional disk space will be used.
Do you want to continue? [Y/n]
```

2. Run the following commands:

   ```
   cumulus@switch:mgmt:~$ sudo bash -c 'echo docker >> /etc/vrf/systemd.conf'
   cumulus@switch:mgmt:~$ sudo systemctl daemon-reload
   ```

3. In the management VRF, enable the Docker service. Docker pulls container images from the internet, which requires internet access through the management VRF.

   ```
   cumulus@switch:mgmt:~$ sudo systemctl enable --now docker@mgmt.service
   Created symlink /etc/systemd/system/multi-user.target.wants/docker@mgmt.service → /etc/systemd/system/docker@.service.
   Warning: The unit file, source configuration file or drop-ins of docker@mgmt.service changed on disk. Run 'systemctl daemon-reload' to reload units.
   ```

   {{%notice note%}}
The warning is a known issue, which has no functional impact.
{{%/notice%}}

4. Check the status of the Docker service with the `systemctl status docker@mgmt.service` command:

   ```
   cumulus@switch:mgmt:~$ sudo systemctl status docker@mgmt.service
   Warning: The unit file, source configuration file or drop-ins of docker@mgmt.service changed on di
   ● docker@mgmt.service - Docker Application Container Engine
      Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
      Drop-In: /run/systemd/generator/docker@.service.d
          └─vrf.conf
      Active: active (running) since Tue 2020-12-15 01:02:36 UTC; 7s ago
       Docs: https://docs.docker.com
   Main PID: 9558 (dockerd)
    Memory: 40.5M
    CGroup: /system.slice/system-docker.slice/docker@mgmt.service
        └─vrf
         └─mgmt
          └─9558 /usr/bin/dockerd --containerd=/run/containerd/containerd.sock

   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.235571032Z" level=info msg="ccReso
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.235612700Z" level=info msg="Client
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.351654900Z" level=warning msg="Una
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.352171765Z" level=info msg="Loadin
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.432399835Z" level=info msg="Defaul
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.473407023Z" level=info msg="Loadin
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.527590296Z" level=info msg="Docker
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.527846668Z" level=info msg="Daemon
   Dec 15 01:02:36 act-5812-10 systemd[1]: Started Docker Application Container Engine.
   Dec 15 01:02:36 act-5812-10 ip[9558]: time="2020-12-15T01:02:36.635997529Z" level=info msg="API li

5. Test your installation by running the `hello-world` container:

   ```
   cumulus@switch:mgmt:~$ docker run hello-world
   Unable to find image 'hello-world:latest' locally
   latest: Pulling from library/hello-world
   0e03bdcc26d7: Pull complete
   Digest: sha256:1a523af650137b8accdaed439c17d684df61ee4d74feac151b5b337bd29e7eec
   Status: Downloaded newer image for hello-world:latest

   Hello from Docker!
   This message shows that your installation appears to be working correctly.

   To generate this message, Docker took the following steps:
   1. The Docker client contacted the Docker daemon.
   2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
      (amd64)
   3. The Docker daemon created a new container from that image which runs the
      executable that produces the output you are currently reading.
   4. The Docker daemon streamed that output to the Docker client, which sent it
      to your terminal.

   To try something more ambitious, you can run an Ubuntu container with:
   $ docker run -it ubuntu bash

   Share images, automate workflows, and more with a free Docker ID:
   https://hub.docker.com/

   For more examples and ideas, visit:
   https://docs.docker.com/get-started/
   ```

{{%notice note%}}
The Docker daemon runs in the management VRF; however, Docker containers run outside a VRF by default. To run a container process inside the management VRF on the host, run the `docker run —privileged —ulimit memlock=131072 —rm —network host ip vrf exec mgmt` command. For example:

```
cumulus@switch:mgmt:~$ sudo docker run —privileged —ulimit memlock=131072 —rm —network host debian ip vrf exec mgmt ping -c3 8.8.8.8

PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=110 time=1.21 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=110 time=1.24 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=110 time=1.26 ms
8.8.8.8 ping statistics -

3 packets transmitted, 3 received, 0% packet loss, time 5ms
rtt min/avg/max/mdev = 1.212/1.237/1.262/0.045 ms
```

If you see the error `Failed to load BPF prog: ‘Operation not permitted’`, increase the `memlock` limit by doubling the value.
{{%/notice%}}

Be mindful of the types of applications you want to run in containers on a Cumulus Linux switch. Depending on the configuration of the container, DHCP servers, custom scripts, and other lightweight services run well. However, VPN, NAT and encryption-type services are CPU-intensive and might lead to undesirable effects on critical applications. Resource-intensive services are not supported.
