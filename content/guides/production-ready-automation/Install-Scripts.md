---
title: Example Install Scripts
weight: 47
---
This section provides the following package dependency install scripts:

- Install script with GitLab Runner for CI/CD
- Install script without GitLab Runner for CI/CD

{{< tabs "TABID01 ">}}

{{< tab "Without GitLab Runner ">}}

```
#!/bin/bash
#
#Debian/Ubuntu setup script
#run with/as sudo/root
#
apt-get update -y
apt-get install -qy libvirt-bin libvirt-dev qemu-utils qemu git
addgroup libvirtd
usermod -a -G libvirtd <users-that-will-run-simulations>
wget https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.deb
dpkg -i vagrant_2.2.7_x86_64.deb
vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
```

{{< /tab >}}

{{< tab "With GitLab Runner ">}}

```
#!/bin/bash
#
#Debian/Ubuntu setup script
#run with/as sudo/root
#
apt-get update -y
apt-get install -qy libvirt-bin libvirt-dev qemu-utils qemu git
addgroup libvirtd
usermod -a -G libvirtd <users-that-will-run-simulations>
wget https://releases.hashicorp.com/vagrant/2.2.7/vagrant_2.2.7_x86_64.deb
dpkg -i vagrant_2.2.7_x86_64.deb
vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
# setup gitlab-runner
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
apt-get install gitlab-runner
sudo su - gitlab-runner
echo 'PATH=/usr/sbin:$PATH' >> ./.bashrc
adduser gitlab-runner libvirtd 
vagrant plugin install vagrant-libvirt vagrant-mutate vagrant-scp
```

{{< /tab >}}

{{< /tabs >}}
