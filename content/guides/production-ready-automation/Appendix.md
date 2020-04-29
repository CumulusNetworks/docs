---
title: Appendix
author: Cumulus Networks
weight: 50
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
This appendix 

## Package dependency install script without Gitlab CI/CD

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

## Package dependency install script including Gitlab runner for CI/CD

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

## Clean up Stuck or Orphaned Libvirt Simulations from Vagrant

Occasionally errors occur while using Vagrant or an in use project’s files may get deleted forgetting that the simulation may have still been running. In instances where either simulations are orphaned without the ability to use Vagrant to clean them up, it may be necessary to use virsh to destroy and clean them up. 

1. Use virsh list --all to inspect the system and see all running libvirt simulations. Find your libvirt ‘domains’ that you wish to clean-up. Simulations often have a common prefix from the same simulation that is normally the parent folder. For unmodified Cumulus Networks demos, the 
2. Use virsh to perform three operations on each virtual machine (libvirt domain) that you wish to cleanup.
    1. virsh destroy <name>
    2. virsh undefine <name>
    3. virsh vol-delete --pool default <name>.img
Use the script below to clean up all simulations that match a common pattern from `virsh list`. * Please use this with caution on servers with other simulations and in shared environments as it does not ask for confirmation and may delete machines you match accidentally! *
```
#for vm in $(virsh list --all | grep <match-pattern> | awk -F ' ' '{print$2}'); do virsh destroy $vm; virsh undefine $vm; virsh vol-delete --pool default $vm.img; done
```
