---
title: Configure SNMP
author: NVIDIA
weight: 1155
toc: 4
---

The most basic SNMP configuration requires you to specify:

- One or more IP addresses on which the SNMP agent listens.
- Either a username (for SNMPv3) or a read-only community string (a password, for SNMPv1 or SNMPv2c).

By default, the SNMP configuration has a listening address of localhost (127.0.0.1), which allows the agent (the `snmpd` daemon) to respond to SNMP requests originating on the switch itself. This is a secure method that allows checking the SNMP configuration without exposing the switch to outside attacks. In order for an external SNMP NMS to poll a Cumulus Linux switch, you must configure the `snmpd` daemon running on the switch to listen to one or more IP addresses on interfaces that have a link state UP.

Use the SNMPv3 username instead of the read-only community name. The SNMPv3 username does not expose the user credentials and can encrypt packet contents. However, SNMPv1 and SNMPv2c environments require read-only community passwords so that the `snmpd` daemon can respond to requests. The read-only community string enables you to poll various MIB objects on the device.

## Start the SNMP Daemon

Before you can use SNMP, you need to enable and start the `snmpd` service.

{{%notice note%}}
If you intend to run this service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF#run-services-as-a-non-root-user" text="these steps">}} for configuring the service.
{{%/notice%}}

To start the SNMP daemon:

1. Start the `snmpd` daemon:

   ```
   cumulus@switch:~$ sudo systemctl start snmpd.service
   ```

2. Enable the `snmpd` daemon to start automatically after reboot:

   ```
   cumulus@switch:~$ sudo systemctl enable snmpd.service
   ```

3. To enable `snmpd` to restart automatically after failure, create a file called `/etc/systemd/system/snmpd.service.d/restart.conf` and add the following lines:

   ```
   [Service]
   Restart=always
   RestartSec=60
   ```

4. Run the `sudo systemctl daemon-reload` command.

After the service starts, you can use SNMP to manage various components on the switch.

## Configure SNMP

To configure `snmpd` edit the `/etc/snmp/snmpd.conf` file and control `snmpd` with `systemctl` commands.

{{%notice info%}}
Use caution when editing this file. `snmpd` caches SNMPv3 usernames and passwords in the /`var/lib/snmp/snmpd.conf` file. Make sure you stop `snmpd` and remove the old entries when making changes. Otherwise, Cumulus Linux uses the old usernames and passwords in the `/var/lib/snmp/snmpd.conf` file instead of the ones in the `/etc/snmp/snmpd.conf` file.

Make sure you do not delete the `snmpd.conf` file; this can cause issues with the package manager the next time you update Cumulus Linux.

The `snmpd` daemon uses the `/etc/snmp/snmpd.conf` configuration file for most of its configuration. The following table defines the syntax for the most important keywords.
{{%/notice%}}

### Configure the Listening IP Addresses

The listening address is `localhost` by default so that the SNMP agent only responds to requests originating on the switch itself in the `default` VRF. To configure the switch to respond to requests sent to `localhost` in a `mgmt` VRF shell, see {{<link url="#snmp-and-vrfs" text="SNMP and VRFs">}}. You can also configure listening only on the IPv6 localhost address. When using IPv6 addresses or localhost, you can use a `readonly-community-v6` for SNMPv1 and SNMPv2c requests. For SNMPv3 requests, you can use the `username` command to restrict access. See {{<link url="#configure-the-snmpv3-username" text="Configure the SNMPv3 Username">}} below.

The IP address must exist on an interface that has link UP on the switch where you use `snmpd`. By default, the IP address is `udp:127.0.0.1:161`, so `snmpd` only responds to requests (such as `snmpwalk`, `snmpget`, `snmpgetnext`) that originate from the switch. A wildcard setting of *udp:161,udp6:161* forces `snmpd` to listen on all IPv4 and IPv6 interfaces for incoming SNMP requests.

You can configure multiple IP addresses and bind to a particular IP address within a particular VRF table.

{{< tabs "Listening IP" >}}
{{< tab "NVUE Commands" >}}

Cumulus Linux does not provide NVUE commands for SNMP configuration.

{{< /tab >}}
{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and add the IP address, protocol and port for `snmpd` to listen for incoming requests. You can use multiple lines to define multiple listening addresses or use a comma-separated list on a single line.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
agentAddress 192.168.200.11@mgmt
agentAddress udp:66.66.66.66:161,udp:77.77.77.77:161,udp6:[2001::1]:161
...
```

{{< /tab >}}
{{< /tabs >}}

#### SNMP and VRFs

Cumulus Linux provides a listening address for VRFs together with trap and inform support. You can configure `snmpd` to listen to a specific IPv4 or IPv6 address on an interface within a particular VRF. With VRFs, identical IP addresses can exist in different VRF tables. This command restricts listening to a particular IP address within a particular VRF. If you do not provide a VRF name, Cumulus Linux uses the default VRF.

{{< tabs "SNMP and VRFs" >}}
{{< tab "NVUE Commands" >}}

The following command configures snmpd to listen to IP address 10.10.10.10 on eth0, the management interface in the management VRF:

```
cumulus@switch:~$ nv set service snmp-server listening-address 10.10.10.10 vrf mgmt
cumulus@switch:~$ nv config apply
```

By default, `snmpd` does not cross VRF table boundaries. To listen on IP addresses in different VRF tables, use multiple `listening-address` commands each with a VRF name:

```
cumulus@switch:~$ nv set service snmp-server listening-address 10.10.10.10 vrf rocket
cumulus@switch:~$ nv set service snmp-server listening-address 10.10.10.20 vrf turtle
cumulus@switch:~$ nv config apply
```

By default, `snmpd` only responds to `localhost` requests in the `default` VRF. You can configure the switch to respond to requests sent to `localhost` in a `mgmt` VRF shell. To configure the `snmpd` daemon to listen on `localhost` in the `mgmt` VRF, run:

```
cumulus@switch:~$ nv set service snmp-server listening-address localhost vrf mgmt
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands" >}}

To bind to a particular IP address within a particular VRF table, edit the `/etc/snmp/snmpd.conf` file and append `@` and the name of the VRF table to the IP address (for example, `192.168.200.11@mgmt`).

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
agentAddress 192.168.200.11@mgmt
agentAddress udp:66.66.66.66:161,udp:77.77.77.77:161,udp6:[2001::1]:161
...
```

By default, `snmpd` only responds to `localhost` requests in the `default` VRF. You can configure the switch to respond to requests sent to `localhost` in a `mgmt` VRF shell. Edit the `/etc/snmp/snmpd.conf` file and add `@mgmt` to the `agentaddress` configuration:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
agentaddress 127.0.0.1@mgmt
...
```
Then restart `snmpd` with the `sudo systemctl restart snmpd` command.

{{< /tab >}}
{{< /tabs >}}

### Configure the SNMPv3 Username

NVIDIA recommends you use an SNMPv3 username and password instead of the read-only community string as the more secure way to use SNMP because SNMPv3 does not expose the password in the `GetRequest` and `GetResponse` packets and can also encrypt packet contents. You can configure multiple usernames for different user roles with different levels of access to various MIBs.

You add SNMPv3 usernames, together with plain text authentication and encryption pass phrases, to the `/etc/snmp/snmpd.conf` file.

{{%notice note%}}
The default `snmpd.conf` file contains the default user `_snmptrapusernameX`. You cannot use this username for authentication. SNMP traps require this username.
{{%/notice%}}

You can authenticate the user in the following ways:

- With no authentication password (if you specify `auth-none`)
- With an MD5 password
- With a SHA password

{{< tabs "username" >}}
{{< tab "NVUE Commands" >}}

Cumulus Linux does not provide NVUE commands for SNMP configuration.

{{< /tab >}}
{{< tab "Linux Commands" >}}

Three directives define an internal SNMPv3 username that you need for `snmpd` to retrieve information and send built-in traps or for traps you configure with the `monitor` command (see {{<link url="#configure-snmp-trap-and-inform-messages" text="below">}}):

- `createuser` is the default SNMPv3 username.
- `iquerysecName` is the default SNMPv3 username you use when making internal queries to retrieve monitored expressions &mdash; either to evaluate the monitored expression or build a notification payload. These internal queries always use SNMPv3, even if you query the agent using SNMPv1 or SNMPv2c. The `iquerysecname` directive only defines which user to use.
- `rouser` is the username for these SNMPv3 queries.

Edit the `/etc/snmp/snmpd.conf` file and add the `createuser`, `iquerysecName`, `rouser` commands. The example configuration here configures *snmptrapusernameX* as the username using the `createUser` command.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
createuser snmptrapusernameX
iquerysecname snmptrapusernameX
rouser snmptrapusernameX
...
```

The example below defines five users, each with a different combination of authentication and encryption:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
# simple no auth user
#createuser user1

# user with MD5 authentication
#createuser user2 MD5 user2password

# user with MD5 for auth and DES for encryption
#createuser user3 MD5 user3password DES user3encryption

# user666 with SHA for authentication and AES for encryption
createuser user666 SHA user666password AES user666encryption

# user999 with MD5 for authentication and DES for encryption
createuser user999 MD5 user999password DES user999encryption

# restrict users to certain OIDs
# (Note: creating rouser or rwuser will give
# access regardless of the createUser command above. However,
# createUser without rouser or rwuser will not provide any access).
rouser user1 noauth 1.3.6.1.2.1
rouser user2 auth 1.3.6.1.2.1
rwuser user3 priv 1.3.6.1.2.1
rwuser user666
rwuser user999
...
```

{{%notice tip%}}
The following example shows a more advanced but slightly more secure method of configuring SNMPv3 users without creating `cleartext` passwords:

1. Install the `net-snmp-config` script that is in `libsnmp-dev` package:

   ```
   cumulus@switch:~$ sudo -E apt-get update
   cumulus@switch:~$ sudo -E apt-get install libsnmp-dev
   ```

2. Stop the `snmpd` daemon:

   ```
   cumulus@switch:~$ sudo systemctl stop snmpd.service
   ```

3. Use the `net-snmp-config` command to create two users, one with MD5 and DES, and the next with SHA and AES.

    {{%notice note%}}

The minimum password length is eight characters and the arguments `-a` and `-x` have different meanings in `net-snmp-config` than `snmpwalk`.
{{%/notice%}}

   ```
   cumulus@switch:~$ sudo net-snmp-config --create-snmpv3-user -a md5authpass -x desprivpass -A MD5 -X DES userMD5withDES
   cumulus@switch:~$ sudo net-snmp-config --create-snmpv3-user -a shaauthpass -x aesprivpass -A SHA -X AES userSHAwithAES
   cumulus@switch:~$ sudo systemctl start snmpd.service
   ```

This adds a `createUser` command in `/var/lib/snmp/snmpd.conf`. Do **not** edit this file by hand unless you are removing usernames. You can edit this file and restrict access to certain parts of the MIB by adding `noauth`, `auth` or `priv` to allow unauthenticated access, require authentication, or to enforce use of encryption.

The `snmpd` daemon reads the information from the `/var/lib/snmp/snpmd.conf` file and then removes the line (so that Cumulus Linux does not store the master password for that user) and replaces it with the key it derives (using the EngineID). The key is a localized key so that if someone steals the password, they cannot use it to access other agents. To remove the two users `userMD5withDES` and `userSHAwithAES`, stop the `snmpd` daemon and edit the `/var/lib/snmp/snmpd.conf` file. Remove the lines containing the username, then restart the `snmpd` daemon as in step 3 above.

{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

### Configure an SNMP View Definition

To restrict MIB tree exposure, you can define a view for an SNMPv3 username or community password, and a host from a restricted subnet. In doing so, any SNMP request with that username and password must have a source IP address within the configured subnet.

You can define a specific view multiple times and fine tune to provide or restrict access using the `included` or `excluded` command to specify branches of certain MIB trees.

By default, the `snmpd.conf` file contains many views within the `systemonly` view.

{{< tabs "366 " >}}
{{< tab "NVUE Commands" >}}

Cumulus Linux does not provide NVUE commands for SNMP configuration.

{{< /tab >}}
{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and add the `view` command.

`rocommunity` uses the `systemonly` view to create a password that can only access these branches of the OID tree.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
view systemonly included .1.3.6.1.2.1.1
view systemonly included .1.3.6.1.2.1.2
view systemonly included .1.3.6.1.2.1.3
...
```

{{< /tab >}}
{{< /tabs >}}

### Configure the Community String

Cumulus Linux disables `snmpd` authentication for SNMPv1 and SNMPv2c by default. To enable authentication, provide a password (community string) for SNMPv1 or SNMPv2c environments so that the `snmpd` daemon can respond to requests. By default, this provides access to the full OID tree for such requests, regardless of their source. Cumulus Linux does not set a default password so `snmpd` does not respond to any requests that arrive unless you set the read-only community password.

For SNMPv1 and SNMPv2c, you can specify a read-only community string. For SNMPv3, you can specify a read-only or a read-write community string (as long as you are not using the preferred {{<link url="#configure-the-snmpv3-username" text="username method">}}; see above).

You can specify a source IP address token to restrict access to only that a host or network.

You can also specify a view to restrict the subset of the OID tree.

{{< tabs "community-string" >}}
{{< tab "NVUE Commands" >}}

Cumulus Linux does not provide NVUE commands for SNMP configuration.

{{< /tab >}}
{{< tab "Linux Commands" >}}

To enable the community string, provide a community string, then set:

- `rocommunity` or `rwcommunity`: `rocommunity` is for a read-only community; `rwcommunity` is for read-write access. Specify one or the other.
- `public`: The plain text password or community string.

  {{%notice info%}}
NVIDIA strongly recommends you change this password to something else.
{{%/notice%}}

- `default`: Allows connections from any system.
- `localhost`: Allows requests only from the local host. A restricted source can either be a specific hostname (or address), or a subnet, represented as IP/MASK (like 10.10.10.0/255.255.255.0), or IP/BITS (like 10.10.10.0/24), or the IPv6 equivalents.
- `-V`: Restricts viewing to a specific {{<link url="#configure-an-snmp-view-name" text="view">}}. For example, `systemonly` is one SNMP view. This is a user-defined value.

Edit the `/etc/snmp/snmpd.conf` file and add the community string.

In the following example, the first line sets the read-only community string to `turtle` for SNMP requests sourced from the *192.168.200.10/24* subnet and restricts viewing to the `systemonly` view defined with the `-V` option. The second line creates a read-only community string that allows access to the entire OID tree from any source IP address.

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
rocommunity turtle 192.168.200.10/24 -V systemonly
rocommunity cumuluspassword
...
```

Restart `snmpd` for the changes to take effect:

```
cumulus@switch:~$ systemctl restart snmpd.service
```

{{< /tab >}}
{{< /tabs >}}

### Configure System Settings

You can configure system settings for the SNMPv2 MIB. The example commands here set:

- The system physical location for the node in the SNMPv2-MIB system table (the `syslocation`).
- The username and email address of the contact person for this managed node (the `syscontact`).
- An administratively assigned name for the managed node (the `sysname`).

{{< tabs "sys-settings" >}}
{{< tab "NVUE Commands" >}}

Cumulus Linux does not provide NVUE commands for SNMP configuration.

{{< /tab >}}
{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and add the following configuration:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
syscontact user X at myemail@example.com
syslocation My private bunker
sysname CumulusBox number 1,543,567
...
```

{{< /tab >}}
{{< /tabs >}}

## Enable SNMP Support for FRR

SNMP supports routing MIBs in {{<link url="FRRouting" text="FRR">}}. To enable SNMP support for FRR, you need to configure {{<exlink url="http://www.net-snmp.org/docs/README.agentx.html" text="AgentX">}} (ASX) access in FRR.

The default `/etc/snmp/snmpd.conf` configuration already enables AgentX and sets the correct permissions.

Enabling FRR includes support for BGP. However, if you plan on using the BGP4 MIB, be sure to provide access to the MIB tree 1.3.6.1.2.1.15.

{{%notice tip%}}
If you plan on using the OSPFv2 MIB, provide access to 1.3.6.1.2.1.14 and to 1.3.6.1.2.1.191 for the OSPv3 MIB.
{{%/notice%}}

To enable SNMP support for FRR:

1. Configure AgentX access in FRR:

   ```
   cumulus@switch:~$ sudo vtysh
   ...
   switch# configure terminal
   switch(config)# agentx
   switch(config)# end
   switch# write memory
   switch# exit
   ```

2. Edit `/etc/frr/daemons` and add a line like the following to configure the appropriate routing daemon; the example below uses `bgpd`, the BGP daemon.

   ```
   cumulus@switch:~$ sudo nano /etc/frr/daemons
   bgpd_options=" -M snmp -A 127.0.0.1"
   ```

3. Restart FRR.

   ```
   cumulus@switch:~$ sudo systemctl restart frr.service
   ```

4. Update the SNMP configuration to enable FRR to respond to SNMP requests. Edit `/etc/snmp/snmpd.conf` and verify that the following configuration exists:

   ```
   cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
   agentxsocket /var/agentx/master
   agentxperms 777 777 snmp snmp
   master agentx
   ```

   {{%notice note%}}

Make sure that the `/var/agentx` directory is world-readable and world-searchable (octal mode 755).

```
cumulus@switch:~$ ls -la /var/
...
drwxr-xr-x  2 root root  4096 Nov 11 12:06 agentx
...
```

   {{%/notice%}}

5. Optionally, you might need to expose various MIBs:

    - For the BGP4 MIB, allow access to `1.3.6.1.2.1.15`
    - For the OSPF MIB, allow access to `1.3.6.1.2.1.14`
    - For the OSPFV3 MIB, allow access to `1.3.6.1.2.1.191`

To verify the configuration, run `snmpwalk`. For example, if you have a running OSPF configuration with routes, you can check this OSPF-MIB first from the switch itself with:

```
cumulus@switch:~$ sudo snmpwalk -v2c -cpublic localhost 1.3.6.1.2.1.14
```
<!-- vale off -->
### Enable the .1.3.6.1.2.1 Range
<!-- vale on -->
The `snmpd.conf` file in Cumulus Linux does not include certain MIBs by default. This results in some default views on common network tools (like `librenms`) to return less than optimal data. To include more MIBs, enable the complete .1.3.6.1.2.1 range. The default SNMPv3 configuration includes:

- ENTITY-MIB
- ENTITY-SENSOR MIB
- Parts of the BRIDGE-MIB and Q-BRIDGE-MIBs

{{%notice warning%}}
This configuration grants access to a large number of MIBs, including all SNMPv2-MIB, which shows more data than you expect. In addition to being a security vulnerability, it consumes more CPU resources.
{{%/notice%}}

To enable the .1.3.6.1.2.1 range, make sure the view commands include the required MIB objects.

## Set up the Custom MIBs on the NMS

You do not need to change the `/etc/snmp/snmpd.conf` file on the switch to support the custom MIBs. The file includes the following lines by default and provides support for both the Cumulus Counters and the Cumulus Resource Query MIBs.

```
cumulus@switch:~$ cat /etc/snmp/snmpd.conf
...
sysObjectID 1.3.6.1.4.1.40310
pass_persist .1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
pass_persist .1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py
...
```

You need to copy several files to the NMS server for it to recognize the custom Cumulus MIB.

- `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`
- `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`
- `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt`

## Pass Persist Scripts

The pass persist scripts in Cumulus Linux use the {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tut:Extending_snmpd_using_shell_scripts#Pass_persist" text="pass_persist extension">}} to Net-SNMP. The scripts are in `/usr/share/snmp` and include:

- `bgp4_pp.py`
- `bridge_pp.py`
- `cl_drop_cntrs_pp.py`
- `cl_poe_pp.py`
- `entity_pp.py`
- `entity_sensor_pp.py`
- `ieee8023_lag_pp.py`
- `resq_pp.py`
- `snmpifAlias_pp.py`
- `sysDescr_pass.py`

Cumulus Linux enables all the scripts by default except for `bgp4_pp.py`, which {{<link url="FRRouting" text="FRR">}} uses.

## Example Configuration

The following example configuration:

- Enables an SNMP agent to listen on all IPv4 addresses with a community string password.
- Sets the trap destination host IP address.
- Creates four types of SNMP traps.

You can find a working example configuration on the {{<exlink url="https://gitlab.com/nvidia-networking/systems-engineering/poc-support/snmp-and-cl" text="NVIDIA Networking GitLab project">}}, which you can try for free with {{<exlink url="https://air.nvidia.com" text="NVIDIA AIR Simulation Platform">}}.

{{< tabs "example-config" >}}
{{< tab "NVUE Commands" >}}

Cumulus Linux does not provide NVUE commands for SNMP configuration.

{{< /tab >}}
{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and apply the following configuration (add every line starting with a +):

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
+agentaddress udp:161
agentxperms 777 777 snmp snmp
agentxsocket /var/agentx/master
+authtrapenable 1
createuser _snmptrapusernameX
iquerysecname _snmptrapusernameX
+load 7.45 5.14 0
master agentx
monitor -r 60 -o laNames -o laErrMessage "laTable" laErrorFlag != 0
+monitor CumulusLinkDOWN -S -r 10 -o ifName -o ifIndex -o ifAdminStatus -o ifOperStatus ifOperStatus == 2
+monitor CumulusLinkUP -S -r 15 -o ifName -o ifIndex -o ifAdminStatus -o ifOperStatus ifOperStatus != 2
pass -p 10 1.3.6.1.2.1.1.1 /usr/share/snmp/sysDescr_pass.py
pass_persist 1.2.840.10006.300.43 /usr/share/snmp/ieee8023_lag_pp.py
pass_persist 1.3.6.1.2.1.17 /usr/share/snmp/bridge_pp.py
pass_persist 1.3.6.1.2.1.31.1.1.1.18 /usr/share/snmp/snmpifAlias_pp.py
pass_persist 1.3.6.1.2.1.47 /usr/share/snmp/entity_pp.py
pass_persist 1.3.6.1.2.1.99 /usr/share/snmp/entity_sensor_pp.py
pass_persist 1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
pass_persist 1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py
pass_persist 1.3.6.1.4.1.40310.3 /usr/share/snmp/cl_poe_pp.py
+rocommunity neteng default
+rocommunity tempPassword default
rouser _snmptrapusernameX
+syslocation leaf01
sysobjectid 1.3.6.1.4.1.40310
sysservices 72
+trap2sink 1.1.1.1 mypass
```

{{< /tab >}}
{{< /tabs >}}
