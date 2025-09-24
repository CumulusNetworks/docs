---
title: Docker with Cumulus Linux
author: NVIDIA
weight: 297
toc: 3
---
You can use Cumulus Linux to run the {{<exlink url="https://www.docker.com/" text="Docker">}} container platform.

The Docker package installs as part of the Cumulus Linux installation or ONIE upgrade process. The Docker package includes Docker Engine, and dependencies and configuration files required to run the Docker service. If you upgrade the switch with apt-upgrade, you must install the Docker package manually.

{{%notice note%}}
Docker has a global limit to use ten percent of the overall resources. WJH also runs in docker; if you exhaust the ten percent limit, then start WJH, you might see issues when using WJH. Make sure to free up Docker resources, then launch WJH again.
{{%/notice%}}

## Run Docker Containers on the Switch

To run Docker containers on the Cumulus Linux switch:

1. Check if the Docker package already exists on the switch with the `dpkg-query -l cumulus-docker-setup` command.

{{< tabs "TabID16 ">}}
{{< tab "Docker exists on the switch">}}

The following command output shows that the Docker package exists. Go to the next step to enable the Docker service.

   ```
   cumulus@switch:~$ dpkg-query -l cumulus-docker-setup
   Desired=Unknown/Install/Remove/Purge/Hold
   | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
   |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
   ||/ Name                 Version                           Architecture Description
   +++-====================-================-============-=========================================
   ii  cumulus-docker-setup 1.0-cl5.11.0u2   all          Cumulus Linux docker configuration files.
   ```

{{< /tab >}}
{{< tab "Docker does not exist on the switch ">}}

The following command output shows that the Docker package does *not* exist on the switch:

```
cumulus@switch:~$ dpkg-query -l cumulus-docker-setup
dpkg-query: no packages found matching cumulus-docker-setup
```

To install the Docker package, run the following commands:

```
cumulus@switch:~$ sudo -E apt-get update
cumulus@switch:~$ sudo -E apt-get install cumulus-docker-setup
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

{{< /tab >}}
{{< /tabs >}}

2. In the management VRF, enable the Docker service. Docker pulls container images from the internet, which requires internet access through the management VRF.

```
cumulus@switch:~$ sudo systemctl enable --now docker@mgmt.service
Created symlink /etc/systemd/system/vrf@mgmt.target.wants/docker@mgmt.service → /etc/systemd/system/docker@.service.
```

3. Check the status of the Docker service with the `systemctl status docker@mgmt.service` command:

```
cumulus@switch:~$ sudo systemctl status docker@mgmt.service
● docker@mgmt.service - Docker Application Container Engine in vrf mgmt
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; preset: enabled)
    Drop-In: /run/systemd/generator/docker@.service.d
             └─vrf.conf
     Active: active (running) since Wed 2025-03-12 19:37:44 UTC; 35s ago
       Docs: https://docs.docker.com
   Main PID: 733337 (dockerd)
      Tasks: 7
     Memory: 102.5M
        CPU: 100ms
     CGroup: /system.slice/system-docker.slice/docker@mgmt.service
             └─vrf
               └─mgmt
                 └─733337 /usr/bin/dockerd --containerd=/run/containerd/containerd.sock

Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.398286828Z" level=info msg="Starting up"
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.402889994Z" level=info msg="OTEL tracing is not>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.498193844Z" level=info msg="[graphdriver] using>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.500889739Z" level=info msg="Loading containers:>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.508097913Z" level=info msg="Loading containers:>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.521363744Z" level=warning msg="WARNING: No swap>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.521540931Z" level=info msg="Docker daemon" comm>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.521799269Z" level=info msg="Daemon has complete>
Mar 12 19:37:44 leaf01 systemd_wait.py[733337]: time="2025-03-12T19:37:44.554397244Z" level=info msg="API listen on /var/>
Mar 12 19:37:44 leaf01 systemd[1]: Started docker@mgmt.service - Docker Application Container Engine in vrf mgmt.
...
```

3. Test your installation by running the `hello-world` container:

```
cumulus@switch:~$ sudo docker run hello-world
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

Be mindful of the types of applications you want to run in containers on a Cumulus Linux switch. Depending on the configuration of the container, DHCP servers, custom scripts, and other lightweight services run well. However, VPN, NAT and encryption-type services are CPU-intensive and lead to undesirable effects on critical applications.

## Change the Docker Service VRF

By default, the Docker service runs in the management VRF. To run Docker in a different VRF, run the following commands.

{{%notice note%}}
Changing the Docker VRF restarts the Docker service, which disrupts all running containers.
{{%/notice%}}

{{< tabs "TabID142 ">}}
{{< tab "NVUE Commands">}}

Run the `nv set system docker vrf <vrf-id>` command:

```
cumulus@switch:~$ nv set system docker vrf RED
cumulus@switch:~$ nv config apply
```

To reset the Docker container to run in the management VRF (the default setting), run the `nv unset system docker vrf` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Run the `systemctl start docker@<vrf-id>.service` command. For example:

```
cumulus@switch:~$ systemctl start docker@RED.service
```

{{< /tab >}}
{{< /tabs >}}

## Container Management

NVUE provides commands to:
- Download a Docker image from a registry.
- Delete a Docker image from the switch.
- Create and run a new container from an image.
- Stop a container.
- Delete a Docker container.

### Docker Images

To download a Docker image from a registry or remove a Docker image from the switch, run the following commands.

In the following commands, `image-id` is the hexadecimal string representing the docker internal identifier for an image.

{{< tabs "TabID180">}}
{{< tab "NVUE Commands">}}

To download a Docker image from a registry, run the `nv action pull system docker image <image-id>` command:

```
cumulus@switch:~$ nv action pull system docker image 97662d24417b
```

To delete a Docker image from the switch, run the `nv action remove system docker image <image-id>` command:

```
cumulus@switch:~$ nv action remove system docker image 97662d24417b
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To download a Docker image from a registry, run the `docker pull <image-id>` command:

```
cumulus@switch:~$ docker pull 97662d24417b
```

To delete a Docker image from the switch, run the `docker rmi <image-id>` command:

```
cumulus@switch:~$ docker rmi 97662d24417b
```

{{< /tab >}}
{{< /tabs >}}

### Docker Containers

To create and run a new container from an image, stop a container or delete a Docker container, run the following commands.

{{< tabs "TabID217">}}
{{< tab "NVUE Commands">}}

To create and run a new container from an image, run the `nv action start system docker container <container-name> image <image-id>` command. You can use Docker run options such as `--pid`, `--cap-add`, and `--storage-opt size`.

```
cumulus@switch:~$ nv action start system docker container CONTAINER1 image 97662d24417b --storage-opt size=120G
```

To stop a container, run the `nv action stop system docker container <container-name>` command:

```
cumulus@switch:~$ nv action stop system docker container CONTAINER1
```

To delete a Docker container from the switch, run the `nv action remove system docker container <container-id>` command:

```
cumulus@switch:~$ nv action remove system docker container CONTAINER1
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To create and run a new container from an image, run the `sudo docker run -d <image-id> --name <container-name>` command. You can use Docker run options such as `--pid`, `--cap-add`, and `--storage-opt size`.

```
cumulus@switch:~$ sudo docker run -d 97662d24417b --name CONTAINER1
```

To stop a container, run the `sudo docker stop <container-name>` command:

```
cumulus@switch:~$ sudo docker stop CONTAINER1
```

To delete a Docker container from the switch, run the `sudo docker rm <container-name>` command:

```
cumulus@switch:~$ sudo docker rm CONTAINER1 
```

{{< /tab >}}
{{< /tabs >}}

## Show Docker Information

To show Docker information on the switch, run the `nv show system docker` command:

```
cumulus@switch:~$ nv show system docker
```

To show docker images present on the switch, run the `nv show system docker image` command:

```
cumulus@switch:~$ nv show system docker image
```

To list all containers and their status, including stopped containers, run the `nv show system docker container` command:

```
cumulus@switch:~$ nv show system docker container
```

To show details of container, run the `nv show system docker container <container-id>` command:

```
cumulus@switch:~$ nv show system docker container CONTAINER1
```

To show all container statistics, run the `nv show system docker container stats` command:

```
cumulus@switch:~$ nv show system docker container stats
```

To show statistics for a specific container, run the `nv show system docker container <container-id-name> stats` command:

```
cumulus@switch:~$ nv show system docker container CONTAINER1 stats
```

To show docker engine configuration, run the `nv show system docker engine` command:

```
cumulus@switch:~$ nv show system docker engine 
```

