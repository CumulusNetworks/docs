---
title: Cumulus Linux Security Guide
author: NVIDIA
weight: 30
product: Technical Guides
---
Cumulus Linux is a powerful operating system for routers that comes with secure defaults and is ready to use. This document discusses additional security measures that enable you to further secure your switch to meet corporate, regulatory, and governmental standards. It focuses on three types of security measures:

- High impact to security and low impact to usability
- Medium impact to both security and usability
- Low impact to security and high impact to usability

{{%notice note%}}

All security measures are not created equally; certain measures can ruin a user experience without adding a significant amount of security. NVIDIA recommends that you focus on security measures with the greatest benefits and the fewest drawbacks. Then, expand to include other security mitigations as your comfort level increases.

{{%/notice%}}

## High Impact to Security and Low Impact to Usability

This section discusses issues that have the biggest security impacts with the least impact to management and user experiences.

### Secure Switch Hardware

Securing the switch hardware is vital because an attacker with physical access to the hardware can eventually have access to the entire device, allowing them to change configurations, capture all the traffic moving through the switch, and even steal the switch itself. If there is a security breach in the hardware, the entire system becomes compromised. Securing the router from various attacks or misconfigurations is very important.

### Prevent Denial of Service

Denial of Service (DOS) attacks aim to disrupt normal use of a service or device. To create a DOS attack, an attacker sends a very large number of redundant and unnecessary requests to a target system to overwhelm it and block intended users from accessing the service or hinder the target system from serving an application. DOS attacks commonly target routers and firewalls. Cumulus Linux comes with a built-in check system for these types of attacks. When enabled, the switch can intelligently analyze packets coming into the system and drop packets that match specific criteria.

To enable automatic checks on your switch, open the `/etc/cumulus/datapath/traffic.conf` file in a text editor and change the value of the `dos_enable` setting to _true_:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
...
dos_enable = true
```

Restart the `switchd` service for the changes to take effect.

{{<cl/restart-switchd>}}

To specify which DOS checks you want to enable, open the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf` file and enable the desired DOS checks by setting the corresponding values to _true_:

```
cumulus@switch:~$ sudo nano /usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf
...
# Enabling/disabling Denial of service (DOS) prevention checks
# To change the default configuration:
# enable/disable the individual DOS checks.
dos.sip_eq_dip = true
dos.smac_eq_dmac = true
dos.tcp_hdr_partial = true
dos.tcp_syn_frag = true
dos.tcp_ports_eq = true
dos.tcp_flags_syn_fin = true
dos.tcp_flags_fup_seq0 = true
dos.tcp_offset1 = true
dos.tcp_ctrl0_seq0 = true
dos.udp_ports_eq = true
dos.icmp_frag = true
dos.icmpv4_length = true
dos.icmpv6_length = true
dos.ipv6_min_frag = true
```

Restart the `switchd` service for the changes to take effect.

{{<cl/restart-switchd>}}

### Configure Switch Ports

Cyber attackers often steal information through vulnerable switch ports. Many companies with VLANs use VLAN 1 instead of choosing a custom VLAN ID because VLAN 1 is the default VLAN ID on most network devices. Because this default is very well known, it is the first place attackers look to gain VLAN access.

By default, the router configuration protects against VLAN hopping attacks, where an attacker can try to fool the target switch into sending traffic from other networks by using generic tags or using dynamic VLAN negotiation protocols. If successful, the attacker can gain access to other networks connected to the switch, but are otherwise unavailable to the attacker. Cumulus Linux mitigates this threat by ignoring packet requests coupled with generic tags.

To protect your ports, ensure that access ports are not assigned to VLAN 1 or any unused VLAN ID.
The following shows an example of how you configure switch ports 1 to 48 as access ports for VLAN 99:

```
cumulus@switch:~$ net add bridge bridge ports swp1-48
cumulus@switch:~$ net add interface swp1-48 bridge access 99
cumulus@switch:~$ net commit
```

Ensure that no trunk ports use VLAN 1 and be thoughtful when assigning and removing VLANs to and from ports. In this example, Cumulus Linux adds swp3 as a trunk port and assigns it to VLANs 100 and 200.

```
cumulus@switch:~$ net add interface swp3 bridge vids 100,200
cumulus@switch:~$ net commit
```

### Customize Control Plane Policies

Cumulus Linux has a default control plane security policy in the `/etc/cumulus/acl/policy.d/` directory. You can see a full list of the default rules [here]({{<ref "/cumulus-linux-44/System-Configuration/Netfilter-ACLs/Default-Cumulus-Linux-ACL-Configuration" >}}).

Best practices dictate that:

- All ACL drops get logged
- The configuration requires the use of `iptables`
- Any line with the action *LOG* must be immediately followed with the same line with the action *DROP*

Be sure to apply changes to the default control plane policies with `cl-acltool` so that they get accelerated in hardware correctly.

The following command installs all the ACLs and control plane policy rules in the `/etc/cumulus/acl/policy.d/` directory:

```
cumulus@switch:~$ sudo cl-acltool -i
```

You can verify that `cl-acltool` applied the rules with the following command:

```
cumulus@switch:~$ sudo cl-acltool -L all
```

### Disable Insecure SSL and TLS Protocol Versions in NGINX

{{%notice note%}}
This procedure applies only to Cumulus Linux 5.3 and earlier, which supports the Cumulus HTTP API. Cumulus Linux 5.4 and later supports the NVUE API and includes the correct TLS configuration. You can stop and disable the `nginx.service` with the `sudo systemctl stop nginx.service` and `sudo systemctl disable nginx.service` commands.
{{%/notice%}}
<!-- vale off -->
Cumulus Linux contains a package for NGINX, an open source web server that supports the Cumulus Linux [RESTful HTTP API]({{<ref "/cumulus-linux-43/System-Configuration/HTTP-API" >}}) through HTTPS. By default, NGINX is enabled and listening on localhost (127.0.0.1 port 8080.
<!-- vale on -->

For backward compatibility, NGINX natively supports the outdated and vulnerable SSLv3 and TLSv1 protocols. To secure against potential exploits using those protocols, you must disable them. Open the `/etc/nginx/nginx.conf` file in a text editor and edit the `ssl_protocols` line to allow only the TLSv1.1 and TLSv1.2 protocols:

```
cumulus@switch:~$ sudo nano /etc/nginx/nginx.conf
...
ssl_protocols TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
```

Restart the `nginx` service for the setting to take effect:

```
cumulus@switch:~$ sudo systemctl restart nginx.service
```

If you are not using the Cumulus HTTP API, you can uninstall NGINX to completely eliminate the TLS attack vector:

```
cumulus@switch:~$ sudo apt-get remove python-cumulus-restapi nginx-common
cumulus@switch:~$ sudo apt-get autoremove
```

### Management Security

#### Enable Management VRF

Management virtual routing tables and forwarding (VRF) separates out-of-band management network traffic from the in-band data plane network. Management VRF increases network security by separating the management routing tables from the main routing tables. It also protects the management network from interference or attacks directed at the routing infrastructure of the main network, which might prevent you from managing the router or switch.

<!-- vale off -->
To take advantage of management VRF, connect interface eth0 to the out-of-band management network. Management VRF is enabled by default in Cumulus Linux 4.0 and later. For earlier versions of Cumulus Linux, use the following commands to configure a management VRF and eth0 to be a member of that VRF:
<!-- vale on -->

```
cumulus@switch:~$ net add vrf mgmt
cumulus@switch:~$ net commit
```

For more information about working with a management VRF, such as [running services]({{<ref "/cumulus-linux-43/Layer-3/VRFs/Management-VRF" >}}) in a specific VRF, refer to the [Management VRF documentation" >}}).

Be sure to enable all the network services inside each VRF, including:

- Traffic flow reporting
- `syslog`
- SNMP
- DNS
- NTP

#### Customize the Management ACL

The management access control list (ACL) is the main list of user permissions for Cumulus Linux. Review and customize the management ACL as soon as possible during the installation process to help prevent user errors or malicious behavior by restricting the abilities of administrative users. Due to many unique needs and environments, the management ACL is highly customizable; it is important that you change the defaults.

Use the following guidelines as a starting point to build your management ACL. These guidelines reference example IP addresses and ports that appear in detail in the firewall rules in the next section.

- Allow SSH inbound only for the management network (192.168.200.0/24).
- Allow UDP ports for the DHCP client on the management network (UDP port 67 and 68).
- Allow SNMP polling only from specific management stations (192.168.200.1).
- Allow NTP only from internal network time servers (192.168.200.1).
- Allow DNS only from configured DNS servers (192.168.200.1).
- Allow TACACS from the management network on eth0 (TCP port 49).
- Allow MLAG traffic on the backup interface eth0 (UDP port 5342).
- Allow outbound `syslog` only to known logging stations (UDP port 514).
- Allow outbound flow only to known flow collectors (UDP port 6343).
- Allow outbound connections for the NetQ agent to the NetQ server (TCP port 31980).
- Block transit traffic on the management network (allow ingress to the switch or egress from the switch).
- Allow the forwarding of traffic to and from the local subnets through the data plane switch ports.

Create `iptables` rules to restrict traffic flow in both directions &mdash; inbound _and_ outbound. The following example shows the switch configured with the management IP address 192.168.200.29.

To create the sample `iptables` firewall rules, create the `/etc/cumulus/acl/policy.d/50management-acl.rules` file, then add the following contents to the file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/50management-acl.rules
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

{{%notice note%}}
This ACL does not take effect until you apply it with the `cl-acltool -i` command, as described [above](#customize-control-plane-policies).
{{%/notice%}}

### User Security

#### Lock the root Account

Safeguarding access to the root account is imperative to a secure system. Users should not have direct access to the root account. This helps to prevent someone from making universal changes to the system accidentally. By default, Cumulus Linux locks the root account.

To verify the root account status, run the following command:

```
cumulus@switch:~$ sudo passwd -S root
```

In the command output, the `L` (immediately following the word `root`) indicates Cumulus Linux locked the account:

```
cumulus@switch:~$ sudo passwd -S root
root L 08/07/2019 0 99999 7 -1
```

The `P` (immediately following the word `root`) indicates the account is *not* locked:

```
cumulus@switch:~$ sudo passwd -S root
root P 09/10/2019 0 99999 7 -1
```

To lock the root account, run the following command:

```
cumulus@switch:~$ sudo passwd -l root
```

#### Harden sudo Access

The `sudo` command allows you to execute programs in Linux with the security privileges of a superuser. It is important to enforce `sudo` rules to avoid abuse. By default, Cumulus Linux caches `sudo` credentials for a set amount of time after you execute a command with privileges using `sudo`.

To increase security, configure Cumulus Linux to require the superuser password with the `sudo` command. Run the `visudo` command to edit the default settings and change the `timestamp_timeout` option to `0`:

```
cumulus@switch:~$ sudo visudo
...
Defaults        env_reset,timestamp_timeout=0
```

Ensure that there are no occurrences of `NOPASSWD` or `!authenticate` in the `/etc/sudoers` file or in files in the `/etc/sudoers.d` directory:

```
cumulus@switch:~$  sudo grep NOPASSWD /etc/sudoers
cumulus@switch:~$  sudo grep NOPASSWD /etc/sudoers.d/*
cumulus@switch:~$  sudo grep \!authenticate /etc/sudoers.d/*
cumulus@switch:~$  sudo grep \!authenticate /etc/sudoers
```

#### Limit User Sessions

It is important to limit the number of sessions a user can run at the same time so that a single user or account does not make contradictory changes. Good practice is to set the limit to 10.

Add the following line at the top of the `/etc/security/limits.conf` file:

```
cumulus@switch:~$ sudo nano /etc/security/limits.conf
hard maxlogins 10
```

Add the following lines to the `/etc/profile.d/autologout.sh` script to set the inactivity timeout to 10 minutes (600 seconds). Create the file if it does not exist:

```
cumulus@switch:~$ sudo nano /etc/profile.d/autologout.sh
TMOUT=600
readonly TMOUT
export TMOUT
```

Add the following line to the `/etc/profile` file to set a console timeout:

```
cumulus@switch:~$ sudo nano /etc/profile.d/autologout.sh
export TMOUT=600
```

### Remote Access Security

Secure Shell (SSH) is a protocol for secure remote login and other secure network services over an insecure network. It is most commonly used to allow administrators to securely access remote systems, such as Linux.

By default, Cumulus Linux includes the following SSH security settings:

<!-- vale off -->
- Version 2 of the SSH protocol is on.
- Empty passwords are not permitted.
- User environment is not permitted.
- Print last login is enabled.
- Strict modes is enabled.
- User privilege separation is enabled.
- Encryption for connections for interactive users.

SSH public key files are protected with permissive mode 0644:
<!-- vale on -->

```
cumulus@switch:~$ ls -l /etc/ssh/*.pub
-rw-r--r-- 1 root root 602 Apr 29  2017 /etc/ssh/ssh_host_dsa_key.pub
-rw-r--r-- 1 root root 174 Apr 29  2017 /etc/ssh/ssh_host_ecdsa_key.pub
-rw-r--r-- 1 root root  94 Apr 29  2017 /etc/ssh/ssh_host_ed25519_key.pub
-rw-r--r-- 1 root root 394 Apr 29  2017 /etc/ssh/ssh_host_rsa_key.pub
```

Verify the SSH private host key files under `/etc/ssh` are set to read/write for your user account only:

```
cumulus@switch:~$ ls -alL /etc/ssh/ssh_host*key
-rw------- 1 root root  668 Apr 29  2017 /etc/ssh/ssh_host_dsa_key
-rw------- 1 root root  227 Apr 29  2017 /etc/ssh/ssh_host_ecdsa_key
-rw------- 1 root root  399 Apr 29  2017 /etc/ssh/ssh_host_ed25519_key
-rw------- 1 root root 1679 Apr 29  2017 /etc/ssh/ssh_host_rsa_key
```

To secure SSH further, consider enabling or reviewing the following options in the `/etc/ssh/sshd_config` file:

- Make sure SSH listens on the eth0 or management VRF interfaces only. Configure the `ListenAddress` option.
- Disable root SSH login access. Configure the `PermitRootLogin no` option.
- Review the default SSH cryptographic policy.
- Review enabled ciphers.
- Review Message Authentication Codes.
- Review HostKeyAlgorithms.
- Review KexAlgorithms.
- Enable SSH session timeouts. Configure the `ClientAliveInterval` and `ClientAliveCountMax` options.
- Use key based authentication.
- Disable SSH compression.

For more information about the options in `sshd`, read the [man page](https://linux.die.net/man/5/sshd_config).

### Secure Network Protocols

#### Enable NTP Authentication

Network time protocol (NTP) synchronizes the time between a computer client and/or server to another time source or server. Time synchronization is critical for authentication and log management. To mitigate attacks involving forged time synchronization, connect your Cumulus Linux switch to an authenticated NTP server.

Add authentication keys to the `/etc/ntp.keys` file:

```
cumulus@switch:~$ sudo nano /etc/ntp.keys
#
# PLEASE DO NOT USE THE DEFAULT VALUES HERE.
#
#65535  M  akey
#1      M  pass
1  M  cumulus123
```

After you add the keys to the file, add at least two servers and their associated trusted keys to the `/etc/ntp.conf` file:

```
cumulus@switch:~$ sudo nano /etc/ntp.conf
server 192.168.0.254 key 1
keys /etc/ntp.keys
trustedkey 1
controlkey 1
requestkey 1
```

To configure time synchronization to occur at least one time every 24 hours, add or correct the following lines in the `/etc/ntp.conf` file. Replace `[source]` in the following line with an authoritative time source:

```
cumulus@switch:~$ sudo nano /etc/ntp.conf
maxpoll = 17
server [source] iburst
```

Restart NTP for the changes to take effect:

```
cumulus@switch:~$ sudo systemctl restart ntp@mgmt.service
```

#### Secure Routing Protocols

Open Shortest Path First (OSPF) and Border Gateway Protocol (BGP) are dynamic routing protocols that allow routers to negotiate with each other to determine the best path to send traffic through the network. During this negotiation, routers learn about the networks connected to the other routers. The routers then use this information to determine where to send traffic on the network.

If left unsecured, an attacker can exploit a dynamic routing protocol such as OSPF or BGP to reroute packets to a rogue system instead of its intended destination. To help mitigate this threat, enable authentication on these protocols.

Configuring OSPF authentication requires two NCLU commands: one to add the key and a second to enable authentication on an interface (swp1 in the command example):

```
cumulus@switch:~$ net add interface swp1 ospf message-digest-key 1 md5 thisisthekey
cumulus@switch:~$ net add interface swp1 ospf authentication message-digest
cumulus@switch:~$ net commit
```

For more information, read the [OSPF chapter]({{<ref "/cumulus-linux-43/Layer-3/OSPF/Open-Shortest-Path-First-v2-OSPFv2#md5-authentication" >}}) of the Cumulus Linux user guide.

To configure BGP authentication for an existing BGP neighbor, you need just one password:

```
cumulus@switch:~$ net add bgp neighbor 1.1.1.1 password BGPPWD
cumulus@switch:~$ net commit
```

For more information, read the [BGP chapter]({{<ref "/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/Optional-BGP-Configuration#md5-enabled-bgp-neighbors" >}}) of the Cumulus Linux user guide.

#### Remove File Transfer Services

Trivial File Transfer Protocol (TFTP) is a simple and unauthenticated alternative to File Transfer Protcol (FTP) and is often used to update the configuration of network devices. By nature, TFTP contains no means to authenticate the user. If using TFTP is not mandatory within your organization, disable or uninstall it.

To uninstall the TFTP service:

```
cumulus@switch:~$ sudo apt-get remove atftp atftpd
cumulus@switch:~$ sudo apt-get remove tftpd-hpa
```

To uninstall the FTP service:

```
cumulus@switch:~$ sudo apt-get remove vsftpd
```

To verify the removal of the TFTP nor FTP packages:

```
cumulus@switch:~$ sudo dpkg -l | grep *ftp*
```

## Medium Impact to Security, Medium Impact to Usability

This section discusses items that have similar impacts to security as well as management and user experiences.

### Hardware Security

<!-- vale off -->
#### Configure 802.1X
<!-- vale on -->

802.1X is a popular technology because it authenticates devices that physically attach to the switch. It can also assign these devices different levels of access to the network after they authenticate. There are many use cases for this technology and each configuration varies widely. For additional details, see the [802.1X Interfaces]({{<ref "/cumulus-linux-43/Layer-1-and-Switch-Ports/802.1X-Interfaces.md" >}}) chapter in the Cumulus Linux user guide.

The following example is a starting point to build on. This is a base 802.1X configuration:

1. Run the following commands:

    ```
    cumulus@switch:~$ net add dot1x radius server-ip 192.168.200.254 vrf mgmt
    cumulus@switch:~$ net add dot1x radius client-source-ip 192.168.200.29
    cumulus@switch:~$ net add dot1x radius shared-secret supersecret
    cumulus@switch:~$ net add dot1x send-eap-request-id
    cumulus@switch:~$ net add dot1x dynamic-vlan
    cumulus@switch:~$ net commit
    ```

2. Open the `hostapd.conf` file in a text editor and change the last two values in the file from _1_ to _0_:

    ```
    cumulus@switch:~$ sudo nano hostapd.conf
    ...
    radius_das_require_event_timestamp=0
    radius_das_require_message_authenticator=0
    ```

3. Restart `hostapd.service`.

    ```
    cumulus@switch:~$ sudo systemctl restart hostapd.service
    ```

4. Enable 802.1X on switch ports (swp1 through swp4 in this example):

    ```
    cumulus@switch:~$ net add interface swp1-4 dot1x
    ```

5. Configure the 802.1X reauthentication period:

    ```
    cumulus@switch:~$ net add dot1x eap-reauth-period 3600
    ```

6. Configure the maximum number of stations:

    ```
    cumulus@switch:~$ net add dot1x max-number-stations 1
    cumulus@switch:~$ net commit
    ```

#### Disable USB Ports

The Cumulus Linux switch comes with several USB ports as part of the external hardware. USB drives are standard among many industries and therefore easily accessible to those who want to do harm to the switch. While a best practice for any switch, disabling the USB ports is especially important if Cumulus Linux is set up in a publicly available area.

### Management Security

#### Set Password Policies

User passwords are the easiest way to break into any system. After a hacker steals a password, they have access to whatever the user has and can obtain information without raising too much suspicion. Therefore, many companies enforce specific user password requirements.

The default password requirements for Cumulus Linux are strong cryptographic hash (SHA-512). No accounts with `nullok` exist in the `/etc/pam.d` file.

Password configurations should be consistent with NIST [password complexity guidelines](https://en.wikipedia.org/wiki/Password_policy#NIST_guidelines), but companies can set their own individual requirements for users.

#### Remove Unnecessary Services

Unnecessary services that remain installed can cause open sockets that become target attack vectors. These services can be accidentally misused and can cause malfunctions. It is important to uninstall any programs or services that are not in use.

#### Enable an Emergency User Account

If your organization relies on a central authentication system such as TACACS or RADIUS, consider enabling an emergency administration account to access Cumulus Linux during times when the authentication systems are unavailable. Create the emergency admin account with its age set to never expire.

Run the following command to set the password policy for the emergency administrator account to never expire. Replace `[Emergency_Administrator]` with the correct emergency administrator account. You can create an emergency administrator user account with your standard user creation workflow.

```
cumulus@switch:~$ sudo chage -I -1 -M 99999 [Emergency_Administrator]
```

#### Configure a Login Banner

To prominently disclose the security and restrictions in place on your switch, enable login banners for all users so that they see your message upon login. Proper disclosure of your security policies upon login can help rule out legal defenses for inappropriate use of the equipment. Consult with the legal representative in your organization to obtain the proper wording of the login banner message.

To enable a login banner for all SSH login sessions:

1. Edit the `/etc/issue.net` file and add the login banner text approved by your organizational security policy:

    ```
    cumulus@switch:~$ sudo nano /etc/issue.net
    You are accessing an Information System (IS) that is provided for authorized use only.
    ```

2. Edit the  `/etc/ssh/sshd_config` file to enable the login banner:

    ```
    cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
    ...
    Banner /etc/issue.net
    ```

3. Restart the `ssh` service:

    ```
    cumulus@switch:~$ sudo systemctl restart ssh@mgmt.service
    ```

#### Configure System Audits

Configure your system to log administrative events. Periodically audit those logs to ensure your system security policies are working as desired, and also to detect any unauthorized attempts to gain access to your system. Auditing the system can also be helpful when troubleshooting issues. By looking at specific log events, you can identify consistent problems.

Cumulus Linux has many audit logs enabled by default. Make sure that the overall level of audit logging required conforms to your organizational security policy, as well as its need to track performance information about the system.

To view the default configurations:

```
cumulus@switch:~$ sudo grep log_file /etc/audit/auditd.conf
log_file = /var/log/audit/audit.log
max_log_file = 6
max_log_file_action = ROTATE
```

To view the size of the audit logs:

```
cumulus@switch:~$ df /var/log/audit/ -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda4       5.8G  931M  4.6G  17% /var/log
```

### Secure Network Protocols

#### Prevent Source Routing

Source routing is a common security threat that allows attackers to send packets to your network, then use the returned information to break into your network. If your organization is not purposefully using source routing, disable it.

To disable IPv4 source-routed packets, set the current behavior with the following command:

```
cumulus@switch:~$ sudo sysctl -w net.ipv4.conf.default.accept_source_route=0
```

Check the default (boot up) setting:

```
cumulus@switch:~$ sudo sysctl net.ipv4.conf.default.accept_source_route
```

If the default value is not _0_, add or update the following line in the `/etc/sysctl.conf` file so the setting persists after a reboot:

```
cumulus@switch:~$ sudo nano /etc/sysctl.conf
...
net.ipv4.conf.default.accept_source_route=0
```

Or, you can create a new file in the `/etc/sysctl.d` directory, then add the `net.ipv4.conf.default.accept_source_route = 0` line to the file.

#### Prevent ICMP Redirects

Internet Control Message Protocol (ICMP) is a great troubleshooting tool, but can be a security threat if your router automatically accepts an ICMP redirect message. Attackers can use this to their advantage by sending unrecognized redirects to either capture your traffic or create a DOS attack.

To prevent the system from accepting IPv4 ICMP redirect messages, set a runtime configuration with the following commands. A runtime configuration does not persist when you reboot the switch.

```
cumulus@switch:~$ sudo sysctl -w net.ipv4.conf.default.accept_redirects=0
```

Check the default (boot up) setting:

```
cumulus@switch:~$ sudo sysctl net.ipv4.conf.default.accept_redirects
```

If the default value is not _0_, you can make the setting persist after a reboot. Add or update the following line in the `/etc/sysctl.conf` file:

```
cumulus@switch:~$ sudo nano /etc/sysctl.conf
...
net.ipv4.conf.default.accept_redirects = 0
```

Or, you can create a new file in the `/etc/sysctl.d` directory and add the `net.ipv4.conf.default.accept_redirects =0` line.

To prevent the system from sending IPv4 ICMP redirect messages, set a runtime configuration with the following commands. A runtime configuration does not persist when you reboot the switch.

```
cumulus@switch:~$ sudo sysctl -w net.ipv4.conf.default.send_redirects=0
cumulus@switch:~$ sudo sysctl -w net.ipv4.conf.all.send_redirects=0
```

Check the default (boot up) setting:

```
cumulus@switch:~$ sudo sysctl net.ipv4.conf.default.send_redirects
net.ipv4.conf.default.send_redirects = 1

cumulus@switch:~$ sudo sysctl net.ipv4.conf.all.send_redirects
net.ipv4.conf.all.send_redirects = 1
```

If the default value is not _0_, you can make the setting persist after a reboot. Add or update the following lines in the `/etc/sysctl.conf` file:

```
cumulus@switch:~$ sudo nano /etc/sysctl.conf
...
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.all.send_redirects = 0
```

Or, you can create a new file in the `/etc/sysctl.d` directory and add the `net.ipv4.conf.default.send_redirects = 0` and `net.ipv4.conf.all.send_redirects = 0` lines.

## Low Impact to Security, High Impact to Usability

This section discusses items that have low impact on security but have the potential to greatly disrupt the user experience.

### Password Protect the Bootloader

A _bootloader_ is a program that launches the operating system when the switch is running or rebooted. Adding a password to the bootloader does not significantly improve the security of a system but it can cause accidental outages.

Consider this example. If you configure the switch to have a bootloader password, then work on the switch remotely and make a change that requires a reboot, when the system begins to boot, it halts and waits for the bootloader password, which you cannot enter unless you are physically at the switch. Instead of a quick reboot, the switch sits offline until someone can enter the bootloader password on the switch and allow it to launch the operating system and bring the switch back online.

### Debian Packages

One of the most tempting services to configure is the Debian package manager that controls the software and updates installed on your switch. For example, you might think it is a good idea to configure the package manager to remove all outdated software packages after a new update finishes. While it makes more disk space available, it also prevents you from quickly rolling back to a previous version if a software glitch causes the system to malfunction or stop communicating.
