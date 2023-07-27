---
title: Set up a Basic Ansible Lab
author: NVIDIA
weight: 321
toc: 4
---

This article outlines the process for managing a switch using Ansible in a lab environment. This example is showing off Ansible's {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/intro_adhoc.html" text="ad-hoc commands">}}. For repeated tasks, use an Ansible playbook; like this {{<link url="Ansible-Simple-Playbook-Example-with-an-FRR-Template" text="easy playbook example">}}.

## Requirements

- One switch running Cumulus Linux (any version), called switch1
- A server or virtual machine running Debian, with a basic
    installation (default packages only), called server1

On the server, set up the following:

- DHCP
- Ansible

## Network Addresses

This example uses the 192.168.0.0/24 subnet.

| IP Address   | Entity               |
| ------------ | -------------------- |
| 192.168.0.1  | The existing gateway |
| 192.168.0.2  | server1              |
| 192.168.0.10 | switch1              |

## Configure server1

Configure a DHCP server on the server, then install Ansible.

1. Install the required packages:  

       root@server:~# apt-get install isc-dhcp-server

2. Assign the static IP address 192.168.0.2 to server1. Edit `/etc/network/interfaces` so it looks like:  

       auto lo
       iface lo inet loopback

       auto eth0
       iface eth0 inet static
           address 192.168.0.2
           netmask 255.255.255.0
           gateway 192.168.0.1

3. Configure the DHCP scope. Edit `/etc/dhcp/dhcpd.conf` and add this to the file:  

       subnet 192.168.0.0 netmask 255.255.255.0 {
           range 192.168.0.100 192.168.0.200
           option routers 192.168.0.1;
           option domain-name-server 192.168.0.2;
           option domain-name "example.com";
        
           host switch1 {
             hardware ethernet 00:JJ:YU:38:AC:45;
             fixed-address 192.168.0.10;
           }

4. Restart server1.

5. Reboot switch1.

6. Confirm that switch1 is reachable from server1:  

        root@server:~# ping 192.168.0.10 
        64 bytes from 192.168.100.11: icmp_req=2 ttl=64 time=0.141 ms

7. Install Ansible:

       root@server:~# apt-get install python-pip
       root@server:~# pip install ansible

## Configure a MOTD via Ansible

This section describes how to create a simple message of the day (MOTD) using Ansible.

1. Create a sample MOTD file:

        root@server:~#  echo "SAMPLE MOTD" > ~/sample.motd

2. Create an inventory file with switch1 in the list:

        root@server:~#  echo "192.168.0.10" > ~/ansible.hosts

3. Push the sample MOTD to switch1 (192.168.0.10). Enter the password for the *cumulus* user (the default user):  

       root@server:~# ansible -k -K -u cumulus -i ~/ansible.hosts -m 'copy' -a 'src=~/sample.motd dest=/etc/motd' 192.168.0.10
         
        
       SSH password:
       sudo password [defaults to SSH password]: 
        sw1 | success >> {
           "changed": false, 
           "dest": "/etc/motd", 
           "gid": 0, 
           "group": "root", 
           "md5sum": "b04dde3768174a34f75fdde78142849d", 
           "mode": "0644", 
           "owner": "root", 
           "path": "/etc/motd", 
           "size": 12, 
           "state": "file", 
           "uid": 0
       }

## See Also

{{<link url="Default-User-Name-and-Password-in-Cumulus-Linux" text="Default username and password for Cumulus Linux">}}
