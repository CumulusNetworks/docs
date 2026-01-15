---
title: Docker with Cumulus Linux
author: NVIDIA
weight: 297
toc: 3
---
You can use Cumulus Linux to run the {{<exlink url="https://www.docker.com/" text="Docker">}} container platform.

The Docker package installs as part of the Cumulus Linux installation or ONIE upgrade process and the service is running by default. The Docker package includes Docker Engine, and dependencies and configuration files required to run the Docker service.

{{%notice note%}}
Docker has a global limit to use ten percent of the overall switch system resources. WJH also runs in docker; if you exhaust the ten percent limit, then start WJH, you might see issues when using WJH. Make sure to free up resources, then restart the WJH service.
{{%/notice%}}

## Before Managing Docker Containers

Before managing Docker containers, validate that the service is running.

{{< tabs "TabID22 ">}}
{{< tab "NVUE Commands">}}
Check the status of the docker service with the `nv show system docker` command:

```
cumulus@switch:~$ nv show system docker
       operational  applied
-----  -----------  -------
vrf    mgmt         mgmt   
state  enabled      enabled

Docker Containers
====================
    Container Name      Image                            Container ID  Status               Ports  Summary
    ------------------  -------------------------------  ------------  -------------------  -----  -------             
    what-just-happened  docker-wjh:latest                f834edf7fd3c  Up 6 days      
```
{{< /tab >}}
{{< tab "Linux Commands">}}

Check the status of the Docker service with the `systemctl status docker@mgmt.service` command:

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
```
{{< /tab >}}
{{< /tabs >}}

If the service is not currently running, enable and start the service.

{{< tabs "TabID66 ">}}
{{< tab "NVUE Commands">}}

To enable Docker:

```
cumulus@switch:~$ nv set system docker state enabled
cumulus@switch:~$ nv config apply
```

To disable Docker:

```
cumulus@switch:~$ nv set system docker state disabled
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
The {{<link title="What Just Happened (WJH)" text="What Just Happened">}} (WJH) service relies on Docker. If you disable Docker, WJH must also be disabled with the `nv set system wjh state disabled` command.
{{%/notice%}}


You can test Docker by running the `hello-world` container if Docker is running in a VRF with Internet access:

```
cumulus@switch:~$ nv action pull system docker image hello-world
Action executing ...
Docker image hello-world successfully pulled.
Action succeeded
cumulus@switch:~$ nv action run system docker container hello-word image hello-world
Action executing ...
Successfully run docker container hello-word from image hello-world.
Action succeeded
cumulus@switch:~$ $ nv show system docker container 
Container Name      Image                            Container ID  Status                         Ports  Summary
------------------  -------------------------------  ------------  -----------------------------  -----  -------
hello-word          hello-world                      6ad36b761217  Exited (0) About a minute ago      
```

{{< /tab >}}

{{< tab "Linux Commands">}}

Enable and start Docker:

```
cumulus@switch:~$ sudo systemctl enable docker@mgmt.service
Created symlink /etc/systemd/system/vrf@mgmt.target.wants/docker@mgmt.service → /etc/systemd/system/docker@.service.
cumulus@switch:~$ sudo systemctl start docker@mgmt.service
```

To disable and stop Docker:

```
cumulus@switch:~$ sudo systemctl disable docker@mgmt.service
cumulus@switch:~$ sudo systemctl stop docker@mgmt.service
```
{{%notice note%}}
The {{<link title="What Just Happened (WJH)" text="What Just Happened">}} (WJH) service relies on Docker. If you disable Docker, WJH must also be disabled.
{{%/notice%}}

You can test Docker by running the `hello-world` container if Docker is running in a VRF with Internet access:

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

{{< /tab >}}
{{< /tabs >}}


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

This example assumes that the `RED` VRF is already configured with NVUE. To learn more about configuring VRFs, reference {{<link url="Virtual-Routing-and-Forwarding-VRF" text="Virtual Routing and Forwarding">}}. 

To reset the Docker container to run in the management VRF (the default setting), run the `nv unset system docker vrf` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Disable the service in the `mgmt` VRF and run the `systemctl start docker@<vrf-id>.service` command. For example:

```
cumulus@switch:~$ sudo systemctl disable docker@mgmt.service
cumulus@switch:~$ sudo systemctl stop docker@mgmt.service
cumulus@switch:~$ systemctl enable docker@RED.service
cumulus@switch:~$ systemctl stop docker@RED.service
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

To download a Docker image from a registry, import an image from an archive, or remove a Docker image from the switch, run the following commands.

{{< tabs "TabID180">}}
{{< tab "NVUE Commands">}}

To download a Docker image from a registry, run the `nv action pull system docker image <image-id> tag <tag-name>` command. If you do not specify a `tag` name, the name defaults to `latest`. 

```
cumulus@switch:~$ nv action pull system docker image nginx tag latest
```

To import a Docker image from an archive, run the `nv action import system docker image <image-url> repository <repository-name> [tag <tag-name>]` command:

```
cumulus@switch:~$ nv action import system docker image /path/to/exampleimage.tgz repository xyz tag imported
```

{{%notice note%}}
Supported archive formats for `nv action import system docker` include `.tar`, `.tar.gz`, `.tgz`, `.bzip`, `.tar.xz`, and `.txz`.
{{%/notice%}}

To delete a Docker image from the switch, run the `nv action remove system docker image <image-id>` command:

```
cumulus@switch:~$ nv action remove system docker image nginx tag latest
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To download a Docker image from a registry, run the `docker pull <image-id>` command:

```
cumulus@switch:~$ docker pull nginx
```

To import a Docker image from an archive run the `docker load <image-path>` command:

```
cumulus@switch:~$ docker load -i /path/to/tarball/filename.tgz
```

To delete a Docker image from the switch, run the `docker rmi <image-id>` command:

```
cumulus@switch:~$ docker rmi nginx
```

{{< /tab >}}
{{< /tabs >}}

### Docker Containers

To create and run a new container from an image, stop a container or delete a Docker container, run the following commands.

{{< tabs "TabID217">}}
{{< tab "NVUE Commands">}}

To create and run a new container from an image, run the `nv action run system docker container <container-name> image <image-id>` command. You can use Docker run `options` such as `--pid`, `--network`, and `--storage-opt size`. To define arguments for the container application, specify `args`.  

{{%notice infonopad%}}
You must escape special characters used in any Docker `options` and `args` specified in NVUE commands. 
{{%/notice%}}


```
cumulus@switch:~$ nv action run system docker container nginx-demo image nginx:alpine option '\-\-hostname nginx-demo \-p 8080:80 \-\-restart unless-stopped \-e NGINX_ENTRYPOINT_QUIET_LOGS=1 \-v site:/usr/share/nginx/html:ro \-\-log-opt max-size=10m \-\-log-opt max-file=3' args "nginx -g 'daemon off; worker_processes auto; error_log /var/log/nginx/error.log warn;'"
```

To stop a container, run the `nv action stop system docker container <container-name>` command:

```
cumulus@switch:~$ nv action stop system docker container nginx-demo
```

To delete a Docker container from the switch, run the `nv action remove system docker container <container-id>` command:

```
cumulus@switch:~$ nv action remove system docker container nginx-demo
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To create and run a new container from an image, run the `sudo docker run -d <image-id> --name <container-name>` command. 

```
cumulus@switch:~$ sudo docker run -d nginx --name nginx-demo
```

To stop a container, run the `sudo docker stop <container-name>` command:

```
cumulus@switch:~$ sudo docker stop nginx-demo
```

To delete a Docker container from the switch, run the `sudo docker rm <container-name>` command:

```
cumulus@switch:~$ sudo docker rm nginx-demo 
```

{{< /tab >}}
{{< /tabs >}}

## Show Docker Information

To show Docker information on the switch, run the `nv show system docker` command:

```
cumulus@switch:~$ nv show system docker
       operational  applied
-----  -----------  -------
vrf    mgmt         mgmt   
state  enabled      enabled



Docker Containers
====================
    Container Name      Image                            Container ID  Status               Ports  Summary
    ------------------  -------------------------------  ------------  -------------------  -----  -------
    repo                cumulus-linux-apt-mirror:5.16.0  a941e1e51c3e  Up 6 days (healthy)                
    what-just-happened  docker-wjh:latest                f834edf7fd3c  Up 7 days  
```

To show Docker images present on the switch, run the `nv show system docker image` command. Add the `-o native` option to display additional data from Docker inspect.

```
cumulus@switch:~$ nv show system docker image
Image Id      Image Name                Tag     Size    Date                           Summary
------------  ------------------------  ------  ------  -----------------------------  -------
283e2bf92e80  docker-wjh                latest  716MB   2025-10-29 21:47:09 -0400 EDT         
d839322a5483  cumulus-linux-apt-mirror  5.16.0  3.47GB  2025-10-30 02:35:30 -0400 EDT      
```

To list all containers and their status, including stopped containers, run the `nv show system docker container` command. Add the `-o native` option to display additional data from Docker inspect.

```
cumulus@switch:~$ nv show system docker container
Container Name      Image                            Container ID  Status               Ports  Summary
------------------  -------------------------------  ------------  -------------------  -----  -------
repo                cumulus-linux-apt-mirror:5.16.0  a941e1e51c3e  Up 6 days (healthy)                
what-just-happened  docker-wjh:latest                f834edf7fd3c  Up 7 days  
```

To show details of container, run the `nv show system docker container <container-id>` command:

```
cumulus@switch:~$ nv show system docker container repo
               operational                    
-------------  -------------------------------
id             a941e1e51c3e                   
status         Up 6 days (healthy)            
image-name     cumulus-linux-apt-mirror:5.16.0
port                                          
stats                                         
  cpu          0.00%                          
  mem-usage    8.105MiB                       
  mem-limit    15.02GiB                       
  mem-percent  0.05%                          
  net-io       0B / 0B                        
  block-io     160kB / 41kB                   
  pids         9                              

```

To show all container statistics, run the `nv show system docker container stats` command:

```
cumulus@switch:~$ $ nv show system docker container stats
Container Name      CPU%   MEM USAGE  MEM LIMIT  MEM%   NET I/O  BLOCK I/O       PIDS
------------------  -----  ---------  ---------  -----  -------  --------------  ----
repo                0.00%  8.102MiB   15.02GiB   0.05%  0B / 0B  160kB / 41kB    9   
what-just-happened  0.05%  81.96MiB   15.02GiB   0.53%  0B / 0B  496kB / 16.4kB  9
```

To show statistics for a specific container, run the `nv show system docker container <container-id-name> stats` command:

```
cumulus@switch:~$ nv show system docker container repo stats 
             operational 
-----------  ------------
cpu          0.00%       
mem-usage    8.102MiB    
mem-limit    15.02GiB    
mem-percent  0.05%       
net-io       0B / 0B     
block-io     160kB / 41kB
pids         9           

```

To show Docker engine configuration, run the `nv show system docker engine` command. Add the `-o native` option to display additional data from Docker inspect.

```
cumulus@switch:~$ nv show system docker engine
                operational                                                                                    
--------------  -----------------------------------------------------------------------------------------------
client                                                                                                         
  name          Docker Engine - Community                                                                      
  version       28.5.1                                                                                         
  context       default                                                                                        
server                                                                                                         
  containers    2                                                                                              
  running       2                                                                                              
  paused        0                                                                                              
  stopped       0                                                                                              
plugins                                                                                                        
  volume        ['local']                                                                                      
  network       ['bridge', 'host', 'ipvlan', 'macvlan', 'null', 'overlay']                                     
  log           ['awslogs', 'fluentd', 'gcplogs', 'gelf', 'journald', 'json-file', 'local', 'splunk', 'syslog']
images          2                                                                                              
server-version  28.5.1                                                                                         
id              ae4be5b9-6806-435d-80cb-5e4548a9c11a                                                           
init-binary     docker-init                                                                                    
data-root       /docker                                                                                        
debug-mode      False                                                                                          
log-level       json-file   
```

## Manage Docker Container Resources

By default, the switch restricts unknown containers to 20 percent of host resources and limited containers to 50 percent. You can customize these values by editing the `/etc/cumulus/docker/resources.conf` file.

```
cumulus@switch: sudo nano /etc/cumulus/docker/resources.conf
RESTRICTED_PERCENT=10  # Tighter jail for unknown apps
LIMITED_PERCENT=60     # Slightly more room for limited apps
```

After editing the `/etc/cumulus/docker/resources.conf` file, you must restart `cumulus-docker-resource-limit-calculator.service`.

```
cumulus@switch: systemctl restart cumulus-docker-resource-limit-calculator.service
```

The docker image whitelist maintains the list of trusted and limited images and is located in the `/etc/cumulus/docker/whitelist.json` file.

By default, the `/etc/cumulus/docker/whitelist.json` file ships with the following content.

```
cumulus@switch: sudo cat /etc/cumulus/docker/whitelist.json
{
  "trusted_images": [ ],
  "limited_images": ["docker-wjh"]
}
```

You can edit this file to add trusted and limited images.

```
cumulus@switch: sudo nano /etc/cumulus/docker/whitelist.json
{
  "trusted_images": [
    "internal-app",
    "postgres"
  ],
  "limited_images": [
    "jenkins-agent",
    "python-worker"
  ]
}
```

To show memory resource usage for containers, run the Linux `sudo cat /sys/fs/cgroup/cumulus-docker-trusted/memory.current` command.

```
cumulus@switch: sudo cat /sys/fs/cgroup/cumulus-docker-trusted/memory.current

```

To show CPU resource usage for containers, run the Linux `sudo cat sys/fs/cgroup/cumulus-docker-trusted/cpu.stat` command and `sudo cat /sys/fs/cgroup/cumulus-docker-limited/cpu.stat` command.

```
cumulus@switch: sudo cat /sys/fs/cgroup/cumulus-docker-limited/cpu.stat

```

To show which container processes are trusted and which are limited, run the `sudo cat /sys/fs/cgroup/cumulus-docker-trusted/cgroup.procs` command or the `sudo cat /sys/fs/cgroup/cumulus-docker-limited/cgroup.procs` command:

```
cumulus@switch: sudo cat /sys/fs/cgroup/cumulus-docker-limited/cgroup.procs

```

## Considerations

- Be mindful of the types of applications you want to run in containers on a Cumulus Linux switch. Depending on the configuration of the container, DHCP servers, custom scripts, and other lightweight services run well. However, VPN, NAT and encryption-type services are CPU-intensive and lead to undesirable effects on critical applications.
- NVUE manages the `/etc/docker/daemon.json` file and overwrites the file on every configuration. If you want to update this file, make sure to use a snippet. The following example shows a snippet that updates the `/etc/docker/daemon.json` file:

      ```
      cumulus@switch:/etc/systemd/system$ nv config patch text.conf
      created [rev_id: 35]
      cumulus@switch:/etc/systemd/system$ nv config diff
      - set:
         system:
            config:
            snippet:
               docker-daemon: |
                  {
                     "iptables": false,
                     "ip6tables": false,
                     "ip-forward": false,
                     "ip-masq": false,
                     "bridge": "none",
                     "data-root": "/docker"
                  }
      ```
