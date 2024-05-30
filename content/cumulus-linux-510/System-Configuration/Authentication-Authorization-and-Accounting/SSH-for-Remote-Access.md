---
title: SSH for Remote Access
author: NVIDIA
weight: 140
toc: 4
---
Cumulus Linux uses the OpenSSH package to provide access to the system using the Secure Shell (SSH) protocol.

## Configure SSH

You can configure SSH to provide login access to the root user and to specific user accounts, limit SSH to listen on a specific VRF, and configure timeouts and session options.

### Root User Settings

By default, the root account cannot use SSH to log in.

You can configure the root account to use SSH to log into the switch with:
- A password
- A public key or any allowed mechanism that is *not* a password and not keyboard interactive. This is the default setting.
- A set of commands defined in the `authorized_keys` file.

{{< tabs "TabID118 ">}}
{{< tab "NVUE Commands ">}}

To allow the root account to SSH into the switch with a password:

```
cumulus@switch:~$ nv set system ssh-server permit-root-login enabled
cumulus@switch:~$ nv config apply
```

Run the `nv set system ssh-server permit-root-login disabled` command to disable SSH login for the root account with a password.

To allow the root account to SSH into the switch and authenticate with a public key or any allowed mechanism that is *not* a password and not keyboard interactive:

```
cumulus@switch:~$ nv set system ssh-server permit-root-login prohibit-password
cumulus@switch:~$ nv config apply
```

To allow the root account to SSH into the switch and only run a set of commands defined in the `authorized_keys` file:

```
cumulus@switch:~$ nv set system ssh-server permit-root-login forced-commands-only
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To allow the root account to SSH into the switch using a password, edit the `/etc/ssh/sshd_config` file and set the `PermitRootLogin` option to `yes`:

```
cumulus@switch:~$ sudo cat /etc/ssh/sshd_config
...
# Authentication:
LoginGraceTime 2m
PermitRootLogin yes
...
```

Set the `PermitRootLogin` command to `no` to disable SSH login with a password.

To allow the root account to SSH into the switch and authenticate with a public key or any allowed mechanism that is *not* a password and not keyboard interactive:

1. Create an `.ssh` directory for the root user.

   ```
   cumulus@switch:~$ sudo mkdir -p /root/.ssh
   cumulus@switch:~$ sudo chmod 0700 /root/.ssh 
   ```

2. As a privileged user (such as the `cumulus` user), either `echo` the public key contents and redirect the contents to the authorized key file *or* copy the public key file to the switch, then copy it to the root account (with privilege escalation).

   To echo the public key contents and redirect the contents to the authorized key file:

   ```
   cumulus@switch:~$ echo "<SSH public key contents>" | sudo tee -a /root/.ssh/authorized_keys 
   cumulus@switch:~$ sudo chmod 0644 /root/.ssh/authorized_keys 
   ```

   To copy the public key file to the switch, then copy it to the root account:

   ```
   cumulus@switch:~$ sudo cp <SSH public key file> /root/.ssh/authorized_keys 
   cumulus@switch:~$ sudo chmod 0644 /root/.ssh/authorized_keys
   ```

{{< /tab >}}
{{< /tabs >}}

### Allow and Deny Users

{{< tabs "TabID187 ">}}
{{< tab "NVUE Commands ">}}

To allow certain users to establish an SSH session:

```
cumulus@switch:~$ nv set system ssh-server allow-users user1
cumulus@switch:~$ nv config apply
```

To deny certain users to establish an SSH session:

```
cumulus@switch:~$ nv set system ssh-server deny-users user4
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To allow certain users to establish an SSH session, edit the `/etc/ssh/sshd_config` file and add the `AllowUsers` parameter:

```
cumulus@switch:~$ sudo cat /etc/ssh/sshd_config
...
...
# Example of overriding settings on a per-user basis
#Match User anoncvs
# X11Forwarding no
# AllowTcpForwarding no
# PermitTTY no
# ForceCommand cvs server
AllowUsers = user1
```

To deny certain users to establish an SSH session, edit the `/etc/ssh/sshd_config` file and add the `DenyUsers` parameter:

```
cumulus@switch:~$ sudo cat /etc/ssh/sshd_config
...
# Example of overriding settings on a per-user basis
#Match User anoncvs
# X11Forwarding no
# AllowTcpForwarding no
# PermitTTY no
# ForceCommand cvs server
AllowUsers = user1
DenyUsers  = user4
```

{{< /tab >}}
{{< /tabs >}}

### SSH and VRFs

The SSH service runs in the default VRF on the switch but listens on all interfaces in all VRFs. You can limit SSH to listen on specific VRFs.

{{%notice note%}}
You cannot run SSH in the default VRF and other VRFs at the same time.
{{%/notice%}}

{{< tabs "TabID143 ">}}
{{< tab "NVUE Commands ">}}

The following example configures SSH to listen only on the management VRF:

```
cumulus@switch:~$ nv set system ssh-server vrf mgmt
cumulus@switch:~$ nv config apply
```

The following example configures SSH to listen on the management VRF and VRF RED:

```
cumulus@switch:~$ nv set system ssh-server vrf mgmt
cumulus@switch:~$ nv set system ssh-server vrf RED
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Bind the SSH service to the VRF. The following example configures SSH to listen only on the management VRF:

```
cumulus@switch:~$ sudo systemctl stop ssh.service
cumulus@switch:~$ sudo systemctl disable ssh.service
cumulus@switch:~$ sudo systemctl start ssh@mgmt.service
cumulus@switch:~$ sudo systemctl enable ssh@mgmt.service
```

The following example configures SSH to listen on the management VRF and VRF RED:

```
cumulus@switch:~$ sudo systemctl stop ssh.service
cumulus@switch:~$ sudo systemctl disable ssh.service
cumulus@switch:~$ sudo systemctl start ssh@mgmt.service
cumulus@switch:~$ sudo systemctl enable ssh@mgmt.service
cumulus@switch:~$ sudo systemctl start ssh@RED.service
cumulus@switch:~$ sudo systemctl enable ssh@RED.service
```

To configure SSH to listen to only one IP address or a subnet in a VRF, you need to bind the service to that VRF (as above), then set the `ListenAddress` parameter in the `/etc/ssh/sshd_config` file to the IP address or subnet in that VRF.

```
cumulus@switch:~$ sudo cat /etc/ssh/sshd_config
...

#Port 22
#AddressFamily any
ListenAddress 10.10.10.6
#ListenAddress ::
```

{{< /tab >}}
{{< /tabs >}}

### Enable and Disable the SSH Server

Cumulus Linux enables the SSH server by default. To disable the SSH server:

{{< tabs "TabID172 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system ssh-server state disabled
cumulus@switch:~$ nv config apply
```

Run the `nv set system ssh-server state enabled` command to renable the SSH server.

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo systemctl stop ssh.service
cumulus@switch:~$ sudo systemctl disable ssh.service
```

To renable the SSH server:

```
cumulus@switch:~$ sudo systemctl start ssh.service
cumulus@switch:~$ sudo systemctl enable ssh.service
```

{{< /tab >}}
{{< /tabs >}}

### SSH Strict Mode

By default, SSH strict mode is `on`; Cumulus Linux disables X11, TCP forwarding, and compression and enforces secure ciphers.

{{< tabs "TabID247 ">}}
{{< tab "NVUE Commands ">}}

To disable SSH strict mode, run the `nv set system ssh-server strict disabled` command:

```
cumulus@switch:~$ nv set system ssh-server strict disabled
cumulus@switch:~$ nv config apply
```

To renable strict mode, run the `nv set system ssh-server strict enabled` command.

To show if strict mode is `on` or `off`, run the `nv show system ssh-server` command:

```
cumulus@switch:~$ nv show system ssh-server

                             applied
---------------------------  --------
authentication-retries       6
login-timeout                120
inactive-timeout             0
permit-root-login            enabled
max-sessions-per-connection  30
state                        enabled
strict                       disabled
...  
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ssh/sshd_config` file and change the `AllowTcpForwarding`, `X11Forwarding` and `Compression` parameters to `yes`. Also, remove the ciphers and keys under `#RekeyLimit default none` in the `Ciphers and keying` section of the file.

```
cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
...

# Ciphers and keying
#RekeyLimit default none
...
#AllowAgentForwarding yes
AllowTcpForwarding yes
#GatewayPorts no
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes
PrintMotd no
#PrintLastLog yes
#TCPKeepAlive yes
#PermitUserEnvironment no
Compression yes
ClientAliveInterval 0
ClientAliveCountMax 0
#UseDNS no
#PidFile /var/run/sshd.pid
MaxStartups 10:30:100
#PermitTunnel no
#ChrootDirectory none
#VersionAddendum none
```

{{< /tab >}}
{{< /tabs >}}

### Configure Timeouts and Sessions

You can configure the following SSH timeout and session options:

- The number of login attempts allowed before rejecting the SSH session. You can specify a value between 3 and 100. The default value is 3 login attempts.
- The number of seconds allowed before login times out. You can specify a value between 1 and 600. The default value is 120 seconds.
- The TCP port numbers that listen for incoming SSH sessions. You can specify a value between 1 and 65535.
- The number of minutes a session can be inactive before the SSH server terminates the connection. The default value is 0 minutes.
- The maximum number of SSH sessions allowed per TCP connection. You can specify a value between 1 and 100. The default value is 10.
- Unauthenticated SSH sessions:
  - The maximum number of unauthenticated SSH sessions allowed. You can specify a value between 1 and 10000. The default value is 100.
  - The number of unauthenticated SSH sessions allowed before throttling starts. You can specify a value between 1 and 10000. The default value is 10.
  - The starting percentage of connections to reject above the throttle start count before reaching the session count limit. You can specify a value between 1 and 100. The default value is 30.

The following example configures the number of login attempts allowed before rejecting the SSH session to 10 and the number of seconds allowed before login times out to 200:

{{< tabs "TabID216 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system ssh-server authentication-retries 10
cumulus@switch:~$ nv set system ssh-server login-timeout 200
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ssh/sshd_config` file and change the `MaxAuthTries` parameter in the `Authentication` section to 10 and the `LoginGraceTime` parameter to 200:

```
cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
...
# Authentication:

LoginGraceTime 200s
PermitRootLogin prohibit-password
#StrictModes yes
MaxAuthTries 10
MaxSessions 10
```

{{< /tab >}}
{{< /tabs >}}

The following example configures the TCP port that listens for incoming SSH sessions to 443:

{{< tabs "TabID233 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system ssh-server port 443
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ssh/sshd_config` file and add the `Port` parameter:

```
cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
...
Port 443
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::
...
```

{{< /tab >}}
{{< /tabs >}}

The following example configures the amount of time a session can be inactive before the SSH server terminates the connection to 5 minutes (300 seconds) and the maximum number of SSH sessions allowed per TCP connection to 5:

{{< tabs "TabID249 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system ssh-server inactive-timeout 5
cumulus@switch:~$ nv set system ssh-server max-sessions-per-connection 5
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit `Authentication` section of the `/etc/ssh/sshd_config` file.
- To configure the amount of time (in seconds) a session can be inactive before the SSH server terminates the connection, change the `ClientAliveInterval` parameter. 
- To configure the maximum number of SSH sessions allowed per TCP connection, change the `MaxSessions` parameter.

```
cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
...
# Authentication:

LoginGraceTime 120s
PermitRootLogin prohibit-password
#StrictModes yes
MaxAuthTries 10
MaxSessions 5
...
#AllowAgentForwarding yes
#AllowTcpForwarding yes
#GatewayPorts no
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
#PermitTTY yes
PrintMotd no
#PrintLastLog yes
#TCPKeepAlive yes
#PermitUserEnvironment no
#Compression delayed
ClientAliveInterval 300
...
```

{{< /tab >}}
{{< /tabs >}}

The following example configures:
- The number of unauthenticated SSH sessions allowed before throttling starts to 5.
- The starting percentage of connections to reject above the throttle start count before reaching the session count limit to 22.
- The maximum number of unauthenticated SSH sessions allowed to 20.

{{< tabs "TabID269 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system ssh-server max-unauthenticated throttle-start 5
cumulus@switch:~$ nv set system ssh-server max-unauthenticated throttle-percent 22
cumulus@switch:~$ nv set system ssh-server max-unauthenticated session-count 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/ssh/sshd_config` file and change the `MaxStartups` parameter.

The following example configures:
- The number of unauthenticated SSH sessions allowed before throttling starts to 5.
- The starting percentage of connections to reject above the throttle start count before reaching the session count limit to 22.
- The maximum number of unauthenticated SSH sessions allowed to 20.

```
cumulus@switch:~$ sudo nano /etc/ssh/sshd_config
...
MaxStartups 5:22:20
...
```

{{< /tab >}}
{{< /tabs >}}

## Generate and Install an SSH Key Pair

This section describes how to generate an SSH key pair on one system and install the key as an authorized key on another system.

### Generate an SSH Key Pair

To generate an SSH key pair, run the `ssh-keygen` command and follow the prompts.

{{%notice note%}}
To configure the system without a password, do not enter a passphrase when prompted in the following step.
{{%/notice%}}

```
cumulus@host01:~$ ssh-keygen 
Generating public/private rsa key pair. 
Enter file in which to save the key (/home/cumulus/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/cumulus/.ssh/id_rsa. 
Your public key has been saved in /home/cumulus/.ssh/id_rsa.pub. 
The key fingerprint is: 
5a:b4:16:a0:f9:14:6b:51:f6:f6:c0:76:1a:35:2b:bb cumulus@leaf04 
The key's randomart image is: 
+---[RSA 2048]----+ 
|      +.o   o    | 
|     o * o . o   | 
|    o + o O o    | 
|     + . = O     | 
|      . S o .    | 
|       +   .     | 
|      .   E      | 
|                 | 
|                 | 
+-----------------+ 
```

### Install an Authorized SSH Key

To install an authorized SSH key, you take the contents of an SSH public key and add it to the SSH authorized key file (`~/.ssh/authorized_keys`) of the user.

A public key is a text file with three space separated fields:

```
<type> <key string> <comment>
```

| Field | Description |
| ----- | ----------- |
| `<type>`  | The algorithm you want to use to hash the key. The algorithm can be `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, `ecdsa-sha2-nistp521`, `ssh-dss`, `ssh-ed25519`, or `ssh-rsa` (the default value). |
| `<key string>` | A base64 format string for the key. |
| `<comment>` | A single word string. By default, this is the name of the system that generated the key. NVUE uses the `<comment>` field as the key name. |

The procedure to install an authorized SSH key is different based on whether the user is an NVUE managed user or a non-NVUE managed user.

{{< tabs "TabID449 ">}}
{{< tab "NVUE Managed User ">}}

The following example adds an authorized key named `prod_key` to the user `admin2`. The content of the public key file is `ssh-rsa 1234 prod_key`.

```
cumulus@leaf01:~$ nv set system aaa user admin2 ssh authorized-key prod_key key XABDB3NzaC1yc2EAAAADAQABAAABgQCvjs/RFPhxLQMkckONg+1RE1PTIO2JQhzFN9TRg7ox7o0tfZ+IzSB99lr2dmmVe8FRWgxVjc...
cumulus@leaf01:~$ nv set system aaa user admin2 ssh authorized-key prod_key type ssh-rsa
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Non-NVUE Managed User ">}}

The following example adds an authorized key file from the account `cumulus` on a host to the `cumulus` account on the switch:

1. To copy a previously generated public key to the desired location, run the `ssh-copy-id` command and follow the prompts:

   ```
   cumulus@host01:~$ ssh-copy-id -i /home/cumulus/.ssh/id_rsa.pub cumulus@leaf02
   The authenticity of host 'leaf02 (192.168.0.11)' can't be established.
   ECDSA key fingerprint is b1:ce:b7:6a:20:f4:06:3a:09:3c:d9:42:de:99:66:6e.
   Are you sure you want to continue connecting (yes/no)? yes
   /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
   /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
   cumulus@leaf01's password:
   Number of key(s) added: 1
   ```

   The `ssh-copy-id` command does not work if the username on the remote switch is different from the username on the local switch. To work around this issue, use the `scp` command instead:

   ```
   cumulus@host01:~$ scp .ssh/id_rsa.pub cumulus@leaf02:.ssh/authorized_keys
   Enter passphrase for key '/home/cumulus/.ssh/id_rsa':
   id_rsa.pub
   ```

2. Connect to the remote switch to confirm that the authentication keys are in place:

   ```
   cumulus@leaf01:~$ ssh cumulus@leaf02
   Welcome to Cumulus VX (TM) 
   Cumulus VX (TM) is a community supported virtual appliance designed for
   experiencing, testing and prototyping the latest technology.
   For any questions or technical support, visit our community site at:
   http://community.cumulusnetworks.com 
   The registered trademark Linux (R) is used pursuant to a sublicense from LMI,
   the exclusive licensee of Linus Torvalds, owner of the mark on a world-wide basis. 
   Last login: Thu Sep 29 16:56:54 2016
   ```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

To show all the current SSH server configuration settings, run the NVUE `nv show system ssh-server` command:

```
cumulus@switch:~$ nv show system ssh-server
                             applied          
---------------------------  -----------------
authentication-retries       6                  6                
login-timeout                120                120              
inactive-timeout             0                  0                
permit-root-login            prohibit-password  prohibit-password
max-sessions-per-connection  10                 10               
state                        enabled            enabled          
strict                       enabled            enabled          
max-unauthenticated                                              
  session-count              100                100              
  throttle-percent           30                 30               
  throttle-start             10                 10 
```

To show the current number of active SSH sessions, run the NVUE `nv show system ssh-server active-sessions` command or the Linux `w` command:

```
cumulus@switch:~$ nv show system ssh-server active-sessions
Peer Address:Port    Local Address:Port      State
-------------------  ----------------------  -----
192.168.200.1:46528  192.168.200.11%mgmt:22  ESTAB
```

```
cumulus@switch:~$ w
 11:10:46 up 19:19,  4 users,  load average: 0.08, 0.05, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
cumulus  ttyS0    -                Wed15   19:19m  0.03s  0.02s -bash
cumulus  pts/0    192.168.200.1    07:27    3:43m  0.03s  0.03s -bash
cumulus  pts/1    192.168.200.1    10:01    1:09m  0.02s  0.02s -bash
cumulus  pts/2    192.168.200.1    11:10    1.00s  0.03s  0.00s w
```

To show which users can establish an SSH session, run the `nv show system ssh-server allow-users` command. To show which users *cannot* establish an SSH session, run the `nv show system ssh-server deny-users` command. You can also show information for a specific user with the `nv show system ssh-server allow-users <user>` command and the `nv show system ssh-server deny-users <user>` command.

To show the TCP port numbers that listen for incoming SSH sessions, run the `nv show system ssh-server port` command. You can also show information for a specific port with the `nv show system ssh-server port <port>` command.

To show the SSH timer and session information, run the `nv show system ssh-server max-unauthenticated` command:

```
cumulus@switch:~$ nv show system ssh-server max-unauthenticated
                  applied
----------------  -------
session-count     20     
throttle-percent  22     
throttle-start    5
```
