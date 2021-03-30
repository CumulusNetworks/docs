---
title: Docker on Cumulus Linux
author: NVIDIA
weight: 1170
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

4. Configure Docker to minimize impact on the system's firewall and forwarding configuration:

   ```
   root@switch:~# cat >/etc/docker/daemon.json <<EOD
   {
		"iptables": false,
		"ip-forward": false,
		"ip-masq": false
   }
   EOD
   ```

5. Configure Docker to run in the management VRF:

   ```
   root@switch:~# cp /lib/systemd/system/docker.service /lib/systemd/system/docker@.service
   root@switch:~# sed -i -re '
        /^Requires=docker.socket$/ d;
        /^ExecStart\>/ s/-H fd:\/\/ //
   ' /lib/systemd/system/docker@.service

   root@switch:~# echo "docker" >>/etc/vrf/systemd.conf
   root@switch:~# systemctl daemon-reload
   root@switch:~# systemctl mask docker.socket
   root@switch:~# systemctl disable --now docker.service
   root@switch:~# systemctl enable --now docker@mgmt
   ```

6. Test your installation by running the `hello-world` container:

   ```
   root@switch:~# docker run hello-world
   ```

{{%notice note%}}

Be mindful of the types of applications you want to run in containers on a Cumulus Linux switch. Depending on the configuration of the container, DHCP servers, custom scripts, and other lightweight services run well. However, VPN, NAT and encryption-type services are CPU-intensive and might lead to undesirable effects on critical applications. Resource-intensive services are not supported.

{{%/notice%}}
