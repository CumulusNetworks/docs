---
title: Cumulus Linux Security Guide
author: Cumulus Networks
product: Cumulus Networks Guides
version: "1.0"
Draft: True
---

# Introduction
Cumulus Linux is a powerful operating system for routers that comes with secure defaults and is ready to use. However, this whitepaper will discuss additional security measures an organization can use to further secure their device and meet corporate, regulatory, and governmental standards. The topics will focus on three types of security measures: big impact to security and low impact to usability; medium impact to both; and low impact to security and high impact to usability. These impacts are all relative, but Cumulus uses them to help you prioritize how to get the most value from your changes for the time you have available and for the impact to your management practices.

# Big impact to security, low impact to usability
This section is going to cover things that will have the biggest security impacts with the least impact to the management and user experiences. First to be discussed will be securing the hardware, then user accounts, then remote access and, finally, securing network protocols.

## Hardware security
Securing the hardware is vital because an attacker with physical access to the hardware will eventually have access to the entire device, allowing them to change configurations, capture all the traffic moving through the device, or even steal the device itself. If there’s a security breach in the hardware, the entire system is compromised. Additionally, securing the router from various attacks or misconfigurations is very important.

## Denial of Service (DOS) prevention
Denial of Service attacks, or DOS attacks, aim to disrupt normal use of a service or device. To create a DOS attack an attacker sends a very large number of redundant and unnecessary requests to a target system in hopes of overwhelming it and blocking the intended users from accessing the service or application being served by the target system. Routers and firewalls are commonly targeted by DOS attacks. Cumulus Linux comes with a built-in check system for these types of attacks. Once enabled, the machine can intelligently analyze packets coming into the system and drop packets that match specific criteria.

To enable automatic checks on your machine:
* Open the `/etc/cumulus/datapath/traffic.conf` file in a text editor such as vi or nano.
* Enable checks by changing the following value to true: `dos_enable = true`
* Save the file.

To specify which DOS checks should be enabled:
* Open the file `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf`
* Enable the desired DOS check(s) by setting their corresponding value(s) to true.
* Restart the switchd service: `sudo systemctl restart switchd.service`

### Switch port configuration
Cyber-attackers often steal information through vulnerable switch ports. Many companies with VLANs use VLAN 1 instead of choosing a custom VLAN ID because VLAN 1 is the default VLAN ID on most network devices. Because this default is very well known, it’s the first place attackers look to gain VLAN access.

By default, the router configuration protects against VLAN hopping attacks. In a VLAN hopping attack an attacker attempts to fool the target switch into sending him/her traffic from other networks by using generic tags or by using dynamic VLAN negotiation protocols. If successful, the attacker would gain access to networks that are connected to the switch, but otherwise unavailable to the attacker.  Cumulus Linux is built to mitigate this threat by ignoring packet requests coupled with generic tags.

To protect your ports:
* Ensure that access ports aren’t assigned to VLAN 1 or any unused VLAN ID.
Example of configuring switch ports 1 to 48 as access ports for VLAN 99
```
net add bridge bridge ports swp1-48
net add interface swp1-48 bridge access 99
```
* Ensure that no trunk ports use VLAN 1 and be thoughtful when assigning and pruning (removing) VLANs to ports.
In this example, swp3 is added as a trunk port and assigned to VLANs 100 and 200.
`net add interface swp3 bridge vids 100,200`

### Control plane policy policing
Cumulus Linux comes out of the box with a default control plane security policy that can be found in the directory: /etc/cumulus/acl/policy.d/. A full list of the default rules can be found [here](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/Netfilter-ACLs/Default-Cumulus-Linux-ACL-Configuration/).

Best practices dictate that:
* All ACL drops are logged.
* The use of IP Tables is required in configuration.
* Any line with the action *LOG* must be immediately followed with the same line with the action *DROP*.
Ensure changes to the default control plane policies are applied using the `cl-acltool` so that they’re properly hardware accelerated.
The following command applies all the ACLs and control plane policy rules in the directory `/etc/cumulus/acl/policy.d/`:

`sudo cl-acltool -i`

You can verify the rules are applied by using the following command:
`sudo cl-acltool -L all`

### Disable insecure SSL and TLS protocol versions in Nginx
Cumulus Linux is packaged with Nginx, an open source web server that supports the Cumulus Linux RESTful API via HTTPS. By default, Nginx is enabled and listening on localhost (127.0.0.1) port 8080. For more information, go [here](https://docs.cumulusnetworks.com/cumulus-linux/System-Configuration/HTTP-API/).

For backward compatibility, Nginx natively supports the outdated and vulnerable SSLv3 and TLSv1 protocols. To secure against potential exploits using those protocols, disable them using this procedure:
* Open the file `/etc/nginx/nginx.conf` in a text file editor.
* Edit the ssl_protocols line to allow only the protocols TLSv1.1 and TLSv1.2:
`ssl_protocols TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE`
* Restart the Nginx service for the setting to take effect:
`sudo systemctl restart nginx.service`

If you are not using the Cumulus REST API, Nginx may be uninstalled. This completely eliminates the TLS attack vector:
```
sudo apt-get remove python-cumulus-restapi nginx-common
sudo apt-get autoremove
```

## Management security
### Management VRF
Management virtual routing tables and forwarding (VRF) separates out-of-band management network traffic from the in-band data plane network. Management VRF increases network security by separating the management routing tables from the main routing tables, thus protecting the management network from interference or attacks directed at the routing infrastructure of the main network which may interrupt an administrator’s ability to manage the router or switch.

To take advantage of management VRF, connect interface eth0 to the Out-Of-Band management network. Management VRF is enabled by default in Cumulus Linux 4 and above. For older versions, use the following commands to configure a management VRF and eth0 to be a member of that VRF:
```
net add vrf mgmt
net commit
```

For more information about working with a management VRF, such as running services in a specific VRF, please refer to the Management VRF documentation.

Also remember to enable all the network services inside each VRF including the following:
* Traffic flow reporting
* Syslog
* SNMP
* DNS
* NTP

### Management ACL
Management Access Control List (ACL) is the main list of user permissions for Cumulus Linux, and you should review and customize the Management ACL as soon as possible during the installation process. This will help prevent user errors or malicious behavior by restricting the abilities of administrative users. Due to many unique needs and environments, the Management ACL is highly customizable and should be adjusted from the default.
The following *guidelines* may be used as a starting point to build your Management ACL. These guidelines reference example IP addresses and ports that are shown in detail in the firewall rules in the next section.
* Allow SSH inbound only for management network (192.168.200.0/24).
* Allow UDP ports for DHCP client on management network (UDP port 67 & 68).
* Allow SNMP polling only from specific management stations (192.168.200.1).
* Allow NTP only from internal network time servers (192.168.200.1).
* Allow DNS only from configured DNS servers (192.168.200.1).
* Allow TACACS from the management network on eth0 (TCP port 49).
* Allow MLAG traffic on backup interface eth0 (UDP port 5342).
* Allow outbound syslog only to known logging stations (UDP port 514).
* Allow outbound Flow only to known flow collectors (UDP port 6343).
* Allow outbound connection for NetQ agent to NetQ server (TCP port 31980).
* Block transit traffic on management network (allow ingress to the switch or egress from the switch).
* Allow traffic to and from the local subnets to be forwarded through the data plane switch ports.

You should create iptables rules to restrict traffic flow in both directions, inbound and outbound. In the following example the switch has been assigned the management IP address 192.168.200.29.

To create the sample iptables firewall rules, create the following file: `/etc/cumulus/acl/policy.d/50management-acl.rules`

Then add to the file the following contents:
```
[iptables]
INGRESS_INTF = swp+
-A INPUT -i eth0 -p udp --dport 68 -j ACCEPT
-A INPUT -i eth0 -s 192.168.200.0/24 -d 192.168.200.29 -p tcp --dport 22 -j ACCEPT
-A INPUT -i eth0 -s 192.168.200.10 -d 192.168.200.29 -p udp --dport 161 -j ACCEPT
-A INPUT -i eth0 -s 192.168.200.1 -d 192.168.200.29 -p udp --dport 123 -j ACCEPT
-A INPUT -i eth0 -s 192.168.200.1 -d 192.168.200.29 -p udp --dport 53 -j ACCEPT
-A INPUT -i eth0 -s 192.168.200.0/24 -d 192.168.200.29 -p udp --dport 5342 -j ACCEPT
-A INPUT -i eth0 -s 192.168.200.0/24 -d 192.168.200.29 -p udp --sport 5342 -j ACCEPT
-A INPUT -i eth0 -j LOG
-A INPUT -i eth0 -j DROP
-A OUTPUT -o eth0 -p udp --dport 67 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.0/24 -p tcp --sport 22 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.0/24 -p udp --sport 5342 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.0/24 -p udp --dport 5342 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.1 -p udp --dport 161 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.1 -p udp --dport 123 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.1 -p udp --dport 53 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.1 -p udp --dport 514 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.1 -p udp --dport 6343 -j ACCEPT
-A OUTPUT -o eth0 -s 192.168.200.29 -d 192.168.200.250 -p tcp --dport 31980 -j ACCEPT
-A OUTPUT -o eth0 -j LOG
-A OUTPUT -o eth0 -j DROP
-A INPUT --in-interface $INGRESS_INTF -s 10.0.0.0/8 -d 10.0.0.0/8 -j ACCEPT
-A INPUT --in-interface $INGRESS_INTF -j LOG
-A INPUT --in-interface $INGRESS_INTF -j DROP
```
Note: This ACL will not take effect until it has been applied with the `cl-acltool -i` command.

## User security
### Lock the root account
Safeguarding access to the root account is imperative to a secure system. Users should not have direct access to the root account. This will help prevent universal changes from being accidentally made to the system. By default, the root account is locked, but you should verify this.
Run the following command to verify the root account status. In the output of the command, the `L` (immediately following the word "root") indicates the account is locked:
```
cumulus@cumulus:mgmt-vrf:~$ sudo passwd -S root
root L 08/07/2019 0 99999 7 -1
cumulus@cumulus:mgmt-vrf:~$
```

If the root account is not locked, the command will instead produce the following output with a `P`:
```
cumulus@cumulus:mgmt-vrf:~$ sudo passwd -S root
root P 09/10/2019 0 99999 7 -1
cumulus@cumulus:mgmt-vrf:~$
```

If the root account is not locked, run the following command:
`passwd -l root`

### Harden sudo access
The sudo command allows a user to execute programs in Linux using the security privileges of a superuser. It is important to enforce sudo rules to avoid abuse. By default, sudo credentials are cached for a set amount of time after a user executes a command with privileges via sudo.

You can increase security by requiring users to enter the superuser password anytime they use the sudo command. To do so, change the `timestamp_timeout` option to `0` as follows:

Use the `visudo` command to edit the default settings and change the line `Defaults	env_reset` to match the line below:
```
sudo visudo
Defaults        env_reset,timestamp_timeout=0
```
Ensure there are no occurrences of `NOPASSWD` or `!authenticate` found in `/etc/sudoers` file or files in the `/etc/sudoers.d` directory:

```
sudo grep NOPASSWD /etc/sudoers
sudo grep NOPASSWD /etc/sudoers.d/*
sudo grep \!authenticate /etc/sudoers.d/*
sudo grep \!authenticate /etc/sudoers
```

### Session timeouts and limits
It’s important to limit the number of sessions a user can run at the same time, so a single user or account doesn’t make contradictory changes. A general good practice is to set the limit to 10.

Add the following line to the top of the `/etc/security/limits.conf`:
`hard maxlogins 10`

Add the following lines to the `/etc/profile.d/autologout.sh` script to set the inactivity timeout to 5 minutes (600 seconds). Create the file if it doesn’t already exist:
```
TMOUT=600
readonly TMOUT
export TMOUT
```

Add the following to `/etc/profile` for a console timeout:
`export TMOUT=600`

## Remote access security
### Restrict SSH
Secure Shell (SSH) is a protocol for secure remote login and other secure network services over an insecure network. It is most commonly used to allow administrators to securely access remote systems, such as Linux.
By default, Cumulus Linux includes the following ssh security settings:

* Version 2 of the SSH protocol is on.
* Empty passwords are not permitted.
* User environment is not permitted.
* Print last login is enabled.
* Strict modes is enabled.
* User privilege separate is enabled.
* Encryption for connections for interactive users.

SSH public key files are protected with permissive mode 0644:
```
ls -l /etc/ssh/*.pub
-rw-r--r-- 1 root root 602 Apr 29  2017 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 174 Apr 29  2017 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root  94 Apr 29  2017 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 394 Apr 29  2017 /etc/ssh/ssh_host_rsa_key.pub
SSH private host key files under /etc/ssh to 0600 with the following command:
ls -alL /etc/ssh/ssh_host*key
-rw------- 1 root root  668 Apr 29  2017 /etc/ssh/ssh_host_dsa_key
-rw------- 1 root root  227 Apr 29  2017 /etc/ssh/ssh_host_ecdsa_key
-rw------- 1 root root  399 Apr 29  2017 /etc/ssh/ssh_host_ed25519_key
-rw------- 1 root root 1679 Apr 29  2017 /etc/ssh/ssh_host_rsa_key
```

To secure SSH further, you should consider enabling or reviewing the following options in `/etc/ssh/sshd_config`
* SSH should listen on the eth0 or mgmt vrf interfaces only. Option:  `ListenAddress`
* Disable root SSH login access. Option: `PermitRootLogin no`
* Review default SSH cryptographic policy
* Review enabled ciphers.
* Review Message Authentication Codes.
* Review HostKeyAlgorithms
* Review KexAlgorithms
* Enable  SSH session timeouts.
* Can be accomplished with a combination of the two options: `ClientAliveInterval`, `ClientAliveCountMax`
* Use key based authentication
* Disable SSH compression.

For more information, about these options in sshd, click [here] (https://linux.die.net/man/5/sshd_config).

## Securing network protocols
### Enable NTP authentication
Network time protocol is used to synchronize the time between a computer client and/or server to another time source or server. Time synchronization is critical for authentication and for log management. To mitigate attacks involving forged time synchronization, connect your Cumulus Linux system to an authenticated NTP server.
To do this, add authentication keys to the file: /etc/ntp.keys
```
#
# PLEASE DO NOT USE THE DEFAULT VALUES HERE.
#
#65535  M  akey
#1      M  pass
1  M  cumulus123
```

Once the keys are added to the file above, add at least two (2) servers and their associated trusted keys to `/etc/ntp.conf`:
```
server 192.168.0.254 key 1
keys /etc/ntp.keys
trustedkey 1
controlkey 1
requestkey 1
```

To configure the time synchronization to occur at least once every 24 hours, edit the `/etc/ntp.conf` file. Add or correct the following lines, by replacing `[source]` in the following line with an authoritative time source:
```
maxpoll = 17
server [source] iburst
```

Restart NTP for the changes to take effect:
`sudo systemctl restart ntp@mgmt.service`

### Routing protocol security
Open Shortest Path First (OSPF) and Border Gateway Protocol (BGP) are dynamic routing protocols that allow routers to negotiate with each other to determine the best path to send traffic through the network. During this negotiation, routers learn about the networks connected to the other routers. The routers then use this information to determine where to send traffic on the network.
If left unsecured, an attacker could exploit a dynamic routing protocol such as OSPF or BGP to reroute packets to a rogue system instead of its intended destination. To help mitigate this threat, enable authentication on these protocols.
To configure OSPF authentication, two NCLU commands are required: one to add the key, and a second to enable authentication on the interface:
```
net add interface swp# ospf message-digest-key 1 md5 thisisthekey
net add interface swp# ospf authentication message-digest
```
For more information, click [here](https://docs.cumulusnetworks.com/version/cumulus-linux-37/Layer-3/Open-Shortest-Path-First-OSPF/#configure-md5-authentication-for-ospf-neighbors).

To configure BGP authentication for an existing BGP neighbor, only a single password is required:

`net add bgp neighbor 1.1.1.1 password BGPPWD`

For more information, see [here](https://docs.cumulusnetworks.com/version/cumulus-linux-37/Layer-3/Border-Gateway-Protocol-BGP/#configure-md5-enabled-bgp-neighbors).

### File services
Trivial File Transfer Protocol (TFTP) is a simple and unauthenticated alternative to File Transfer Protcol (FTP) and is often used to update the configuration of network devices. By nature, TFTP contains no means to authenticate the user and therefore should be disabled or uninstalled if its usage is not otherwise mandatory within your organization.

The TFTP service can be removed by:
```
sudo apt-get remove atftp atftpd
sudo apt-get remove tftpd-hpa
```

The FTP service can be removed by:
`sudo apt-get remove vsftpd`

Verify that neither TFTP nor FTP is installed by:
`sudo dpkg -l | grep *ftp*`

# Medium impact to security, medium impact to usability
This section will discuss items that have similar impacts to both security and the management and user experiences. It will start with hardware security, then discuss management security, and finish with network protocol security.

## Hardware security

### 802.1X

802.1X is a popular technology among tech users because it authenticates devices that physically attach to the switch. It can also assign these devices different levels of access to the network once they’re authenticated. There are many use cases for this technology and each configuration varies widely. For additional details, go [here](https://docs.cumulusnetworks.com/cumulus-linux/Layer-1-and-Switch-Ports/802.1X-Interfaces/) and [here](https://cumulusnetworks.com/blog/campus-design-feature-set-up-part-4/).
The following example is a starting point to build on. This is a base 802.1X configuration:
```
net add dot1x radius server-ip 192.168.200.254 vrf mgmt
net add dot1x radius client-source-ip 192.168.200.29
net add dot1x radius shared-secret supersecret
net add dot1x send-eap-request-id
net add dot1x dynamic-vlan
```

* Open the `hostapd.conf` file
* The next step is to change the bottom two values in the `/etc/hostapd.conf` file from `=1` to `=0`
```
radius_das_require_event_timestamp=0
radius_das_require_message_authenticator=0
```
* Restart the `hostapd.service` after making the above changes with the following command:
`sudo systemctl restart hostapd.service`
* Enable 802.1X on switchports:
`net add interface swp1-4 dot1x`
* Configure 802.1X reauth period:
`net add dot1x eap-reauth-period 3600`
* Configure the max number of stations:
` net add dot1x max-number-stations 1`

### USB
The Cumulus Linux device comes with several USB ports as part of the external hardware. USB drives are standard among many industries and therefore easily accessible to those who may want to do harm to the machine. While a best practice for any machine, disabling the USB ports is especially important if the Cumulus Linux is set up in a publicly available area.

## Management security
### Password policy & user management
User passwords are the easiest way to break into any system. Once a hacker steals a password, they have access to whatever the user has and can gain information without raising too much suspicion. Therefore, many companies enforce specific user password requirements.
The default password requirements for Cumulus Linux are strong cryptographic hash (SHA-512). No accounts with nullok are in `/etc/pam.d`.

Password configurations should be consistent with NIST [password complexity guidelines](https://en.wikipedia.org/wiki/Password_policy#NIST_guidelines), but companies can set their own individual requirements for users.

### Remove unnecessary services
When unnecessary services remain installed, it can cause open sockets that become target attack vectors. Additionally, they can be accidentally misused and can cause malfunctions. Therefore, it’s important to uninstall any programs or services that aren’t in use.

### Emergency user account
If your organization relies on a central authentication system such as TACACS or RADIUS, you should consider enabling an emergency administration account to access Cumulus Linux during times when the authentication systems are unavailable. The emergency admin account should be created with its age never set to expire.

In the following example, replace `[Emergency_Administrator]` in the following command with the correct emergency administrator account to set the password policy for the emergency administrator account to never expire. An emergency administrator user account can be created using your standard user creation workflow.

Run the following command:
`sudo chage -I -1 -M 99999 [Emergency_Administrator]`


### Login banner
To prominently disclose the security and restrictions in place on your device, enable login banners for all users. Upon login each user will see your text message. Proper disclosure of your security policies upon logon can help rule out legal defenses for inappropriate use of the equipment on the part of the user. Consult with your organization’s legal representative to obtain the proper wording of the login banner message.

To enable the login banner for all console login sessions, edit the file `/etc/issue.net`. with the text approved by your organizational security policy. For example:

>You are accessing an Information System (IS) that is provided for authorized use only.

To enable the login banner for all SSH login sessions:
* Edit the file `/etc/issue.net` to add your login banner text to the file.
* Edit the file `/etc/ssh/sshd_config` to enable the logon banner. Uncomment the following line:
`Banner /etc/issue.net`
* Restart the ssh service:
`sudo systemctl restart ssh@mgmt.service`

### Audit
You should configure your system to log administrative events, and then periodically audit those logs to ensure your system security policies are working as desired, as well as to detect any unauthorized attempts to gain access to your system. Auditing the system can also be helpful when troubleshooting issues. By looking at specific log events, administrators can identify consistent problems.

Cumulus Linux has many audit logs enabled by default to help in this process. The overall level of audit logging required should conform to your organizational security policy, as well as its need to track performance information about the system.

To view the default configurations:
```
sudo grep log_file /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log
max_log_file = 6
max_log_file_action = ROTATE
```

To view the size of the audit logs (example output included below):
```
df /var/log/audit/ -h
Filesystem  	Size  Used Avail Use% Mounted on
/dev/sda4   	5.8G  931M  4.6G  17% /var/log
```

## Securing network protocols
### Source route
Source routing is a common security threat that allows attackers to send packets to your network and then use the returned information to break into your network. Therefore, if your organization isn’t purposefully using source routing, it should be disabled.

To disable IPv4 source-routed packets:
Set the current behavior with the following command:

`sudo sysctl -w net.ipv4.conf.default.accept_source_route=0`

Check the default (boot up) setting:

`sudo sysctl net.ipv4.conf.default.accept_source_route`

If the default value is not 0:
Add or update the following line in the file `/etc/sysctl.conf` so the setting will persist after a reboot:
`net.ipv4.conf.default.accept_source_route=0`

Alternatively, you may create a new file with the following text in the directory: `/etc/sysctl.d`
`net.ipv4.conf.default.accept_source_route=0`

### ICMP redirects
Internet Control Message Protocol (ICMP) is a great troubleshooting tool, but can be a security threat if your router automatically accepts an ICMP redirect message. Attackers can use this to their advantage by sending unrecognized redirects to either capture your traffic or create a DOS attack.

To prevent IPv4 ICMP redirect messages from being accepted:
Set the current behavior with the following command:

`sudo sysctl -w net.ipv4.conf.default.accept_redirects=0`

Check the default (boot up) setting:

`sudo sysctl net.ipv4.conf.default.accept_redirects`

If the default value is not 0:
Add or update the following line in the file `/etc/sysctl.conf` so the setting will persist after a reboot:
`net.ipv4.conf.default.accept_redirects =0`

Alternatively you may create a new file with the following text in the directory: `/etc/sysctl.d`
`net.ipv4.conf.default.accept_redirects =0`

To prevent IPv4 ICMP redirect messages from being sent:
Set the current behavior with the following command:
```
sudo sysctl -w net.ipv4.conf.default.send_redirects=0
sudo sysctl -w net.ipv4.conf.all.send_redirects=0
```

Check the default (boot up) setting:
```
sudo sysctl net.ipv4.conf.default.send_redirects
net.ipv4.conf.default.send_redirects = 1
```

```
sudo sysctl net.ipv4.conf.all.send_redirects
net.ipv4.conf.all.send_redirects = 1
```

If the default value is not 0:
Add or update the following line in the file `/etc/sysctl.conf` so the setting will persist after a reboot:
```
net.ipv4.conf.default.send_redirects=0
net.ipv4.conf.all.send_redirects=0
```

Alternatively, you may create a new file with the following text in the directory: `/etc/sysctl.d`
```
net.ipv4.conf.default.send_redirects=0
net.ipv4.conf.all.send_redirects=0
```

# Low impact to security, high impact to usability
This section will discuss items that have a relatively low impact on security but have the potential to greatly disturb the user experience.

## Password protect bootloader
A bootloader is the program that launches the operating system when the machine is powered on or rebooted. Adding a password to the bootloader doesn’t significantly improve the security of a system, but it can cause accidental outages.

For example: You configure a device to have a bootloader password. Later you’re working on the device remotely and make a change to the device that necessitates a system reboot, which you perform. However, when the system begins to boot, it halts waiting for the bootloader password, which you cannot enter unless you’re physically at the device. Therefore, instead of a quick reboot, the device sits offline until someone can enter the bootloader password on the device and allow it to launch the operating system and bring the device back online.

## Debian packages
One of the most tempting services to configure is the Debian package manager that controls the software and updates installed on your device. For example, you might think it would be a good plan to configure the package manager to remove all outdated software packages after a new update is completed. While it would make more disk space available, it also prevents your ability to quickly roll back to a previous version in the event that a software glitch causes the system to malfunction or stop communicating.

# Not all security measures are created equal
Cumulus Linux comes out the box ready for use and with built-in security. But when organizations want or need to customize the default security configuration or add additional security controls, the measures described in this document will help achieve the required result. Not all security measures are created equal, and many can ruin a user experience without adding a significant amount of security. You should first focus on security measures with the greatest benefits and the least drawbacks. Later expand to include other security mitigations as your comfort level increases.

