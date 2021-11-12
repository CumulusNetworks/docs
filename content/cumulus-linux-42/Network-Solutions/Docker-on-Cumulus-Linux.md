---
title: Docker on Cumulus Linux
author: NVIDIA
weight: 1310
toc: 3
---
Cumulus Linux can be used to run the {{<exlink url="https://www.docker.com/" text="Docker">}} container platform. You can install Docker Engine directly on a Cumulus Linux switch and run Docker containers natively on the switch.

To set up Docker on Cumulus Linux, run the following commands **as root**.

1. Install the authentication key for Docker:

   ```
   root@switch:~# curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
   ```

2. Configure the repositories for Docker:

   ```
   root@switch:~# echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" >/etc/apt/sources.list.d/docker.list
   ```

3. Install the Docker package:

   ```
   root@switch:~# apt update
   root@switch:~# apt install -y docker-ce
   ```

4. Run the following commands:

   ```
   cumulus@switch:mgmt:~$ sudo bash -c 'echo docker >> /etc/vrf/systemd.conf'
   cumulus@switch:mgmt:~$ sudo systemctl daemon-reload
   ```

5. In the managment VRF, enable the Docker service. Docker pulls container images from the internet, which requires internet access through the management VRF.

   ```
   cumulus@switch:mgmt:~$ sudo systemctl enable --now docker@mgmt.service
   Created symlink /etc/systemd/system/multi-user.target.wants/docker@mgmt.service → /etc/systemd/system/docker@.service.
   Warning: The unit file, source configuration file or drop-ins of docker@mgmt.service changed on disk. Run 'systemctl daemon-reload' to reload units.
   ```

   {{%notice note%}}
The warning is a known issue, which has no functional impact.
{{%/notice%}}

6. Check the status of the Docker service with the `systemctl status docker@mgmt.service` command:

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

7. Test your installation by running the `hello-world` container:

   ```
   root@switch:~# docker run hello-world
   ```

{{%notice note%}}

Be mindful of the types of applications you want to run in containers on a Cumulus Linux switch. Depending on the configuration of the container, DHCP servers, custom scripts, and other lightweight services run well. However, VPN, NAT and encryption-type services are CPU-intensive and might lead to undesirable effects on critical applications. Resource-intensive services are not supported.

{{%/notice%}}
