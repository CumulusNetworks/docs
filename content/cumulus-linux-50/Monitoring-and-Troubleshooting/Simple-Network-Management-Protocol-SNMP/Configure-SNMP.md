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

The SNMPv3 username is the recommended option instead of the read-only community name, as it is more secure; it does not expose the user credentials and can also encrypt packet contents. However, a read-only community password is required for SNMPv1 or SNMPv2c environments so that the `snmpd` daemon can respond to requests. The read-only community string allows polling of the various MIB objects on the device itself.

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

Cumulus Networks recommends that you use NCLU to configure `snmpd` even though NCLU does not provide functionality to configure every `snmpd` feature. You are not restricted to using NCLU for configuration and can edit the `/etc/snmp/snmpd.conf` file and control `snmpd` with `systemctl` commands.

{{%notice info%}}

If you need to manually edit the SNMP configuration &mdash; for example, if the necessary option has not been implemented in NCLU &mdash; you need to edit the configuration directly in the `/etc/snmp/snmpd.conf` file.

Use caution when editing this file. Be aware that `snmpd` caches SNMPv3 usernames and passwords in the /`var/lib/snmp/snmpd.conf` file. Make sure you stop `snmpd` and remove the old entries when making changes. Otherwise, Cumulus Linux uses the old usernames and passwords in the `/var/lib/snmp/snmpd.conf` file instead of the ones in the `/etc/snmp/snmpd.conf` file.

The next time you use NCLU to update your SNMP configuration, if NCLU is unable to correctly parse the syntax, some of the options might be overwritten.

Make sure you do not delete the `snmpd.conf` file; this can cause issues with the package manager the next time you update Cumulus Linux.

The `snmpd` daemon uses the `/etc/snmp/snmpd.conf` configuration file for most of its configuration. The syntax of the most important keywords are defined in the following table.

{{%/notice%}}

### Configure the Listening IP Addresses

For security reasons, the listening address is set to the localhost by default so that the SNMP agent only responds to requests originating on the switch itself. You can also configure listening only on the IPv6 localhost address. When using IPv6 addresses or localhost, you can use a `readonly-community-v6` for SNMPv1 and SNMPv2c requests. For SNMPv3 requests, you can use the `username` command to restrict access. See {{<link url="#configure-the-snmpv3-username" text="Configure the SNMPv3 Username">}} below.

The IP address must exist on an interface that has link UP on the switch where `snmpd` is being used. By default, this is set to `udp:127.0.0.1:161`, so `snmpd` only responds to requests (such as `snmpwalk`, `snmpget`, `snmpgetnext`) originating from the switch. A wildcard setting of *udp:161,udp6:161* forces `snmpd` to listen on all IPv4 and IPv6 interfaces for incoming SNMP requests.

You can configure multiple IP addresses and bind to a particular IP address within a particular VRF table.

{{< tabs "Listening IP" >}}

{{< tab "NCLU Commands" >}}

To configure the `snmpd` daemon to listen on the localhost IPv4 and IPv6 interfaces, run:

```
cumulus@switch:~$ net add snmp-server listening-address localhost
cumulus@switch:~$ net add snmp-server listening-address localhost-v6
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice tip%}}

If you configure the listening address on the loopback interface, since it is not a change from the default, a message appears in the console stating that the configuration has not changed.

```
cumulus@switch:~$ net add snmp-server listening-address localhost
Cannot add 127.0.0.1. It is already a listener-address
The configuration has not changed.
```

{{%/notice%}}

To configure the `snmpd` daemon to listen on all interfaces for either IPv4 or IPv6 UDP port 161 SNMP requests, run the following command, which removes all other individual IP addresses configured:

```
cumulus@switch:~$ net add snmp-server listening-address all
cumulus@switch:~$ net add snmp-server listening-address all-v6
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To configure `snmpd` to listen to a specific IPv4 or IPv6 address, run:

```
cumulus@switch:~$ net add snmp-server listening-address 192.168.200.11
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To configure `snmpd` to listen to a group of addresses with space separated values for incoming SNMP queries, run:

```
cumulus@switch:~$ net add snmp-server listening-address 192.168.200.11 192.168.200.21
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and add the IP address, protocol and port for `snmpd` to listen for incoming requests. An example configuration is shown below.

You can use multiple lines to define multiple listening addresses or use a comma-separated list on a single line.

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

Cumulus Linux provides a listening address for VRFs along with trap and inform support. You can configure `snmpd` to listen to a specific IPv4 or IPv6 address on an interface within a particular VRF. With VRFs, identical IP addresses can exist in different VRF tables. This command restricts listening to a particular IP address within a particular VRF. If the VRF name is not given, the default VRF is used.

{{< tabs "SNMP and VRFs" >}}

{{< tab "NCLU Commands" >}}

The following command configures `snmpd` to listen to IP address 10.10.10.10 on eth0, the management interface in the management VRF:

```
cumulus@switch:~$ net add snmp-server listening-address 10.10.10.10 vrf mgmt
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

By default, `snmpd` does not cross VRF table boundaries. To listen on IP addresses in different VRF tables, use multiple listening-address commands each with a VRF name, as shown below.

```
cumulus@switch:~$ net add snmp-server listening-address 10.10.10.10 vrf rocket
cumulus@switch:~$ net add snmp-server listening-address 10.10.10.20 vrf turtle
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

To bind to a particular IP address within a particular VRF table, edit the `/etc/snmp/snmpd.conf` file and append an *@* and the name of the VRF table to the IP address (for example, *192.168.200.11@mgmt*).

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
...
agentAddress 192.168.200.11@mgmt
agentAddress udp:66.66.66.66:161,udp:77.77.77.77:161,udp6:[2001::1]:161
...
```

{{< /tab >}}

{{< /tabs >}}

### Configure the SNMPv3 Username

As mentioned above, Cumulus Networks recommends you use an SNMPv3 username and password instead of the read-only community string as the more secure way to use SNMP, since SNMPv3 does not expose the password in the `GetRequest` and `GetResponse` packets and can also encrypt packet contents. You can configure multiple usernames for different user roles with different levels of access to various MIBs.

SNMPv3 usernames are added to the `/etc/snmp/snmpd.conf` file, along with plaintext authentication and encryption pass phrases.

{{%notice note%}}

The default `snmpd.conf` file contains a default user, *_snmptrapusernameX*. This username cannot be used for authentication, but is required for SNMP traps.

{{%/notice%}}

You have three choices for authenticating the user:

- No authentication password (if you specify `auth-none`)
- MD5 password
- SHA password

{{< tabs "username" >}}

{{< tab "NCLU Commands" >}}

For no authentication, run:

```
cumulus@switch:~$ net add snmp-server username testusernoauth auth-none
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

For MD5 authentication, run:

```
cumulus@switch:~$ net add snmp-server username testuserauth auth-md5 myauthmd5password
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

For SHA authentication, run:

```
cumulus@switch:~$ net add snmp-server username limiteduser1 auth-sha SHApassword1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

If you specify MD5 or SHA authentication, you can also specify an AES or DES encryption password to encrypt the contents of the request and response packets.

```
cumulus@switch:~$ net add snmp-server username testuserboth auth-md5 mynewmd5password encrypt-aes myencryptsecret
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can restrict a user to a particular OID tree. The OID can be either a string of period separated decimal numbers or a unique text string that identifies an SNMP MIB object. The MIBs included in Cumulus Linux are located in `/usr/share/snmp/mibs/`. If the MIB you want to use is not installed by default, you must install it with the latest Debian `snmp-mibs-downloader` package.

```
cumulus@switch:~$ net add snmp-server username limiteduser1 auth-md5 md5password1 encrypt-aes myaessecret oid 1.3.6.1.2.1.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

Or you can restrict a user to a predefined view if one is specified.

```
cumulus@switch:~$ net add snmp-server username limiteduser1 auth-md5 md5password1 encrypt-aes myaessecret viewname rocket
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The example below defines five users, each with a different combination of authentication and encryption:

```
cumulus@switch:~$ net add snmp-server username user1 auth-none
cumulus@switch:~$ net add snmp-server username user2 auth-md5 user2password
cumulus@switch:~$ net add snmp-server username user3 auth-md5 user3password encrypt-des user3encryption
cumulus@switch:~$ net add snmp-server username user666 auth-sha user666password encrypt-aes user666encryption
cumulus@switch:~$ net add snmp-server username user999 auth-md5 user999password encrypt-des user999encryption
cumulus@switch:~$ net add snmp-server username user1 auth-none oid 1.3.6.1.2.1
cumulus@switch:~$ net add snmp-server username user1 auth-none oid system
cumulus@switch:~$ net add snmp-server username user2 auth-md5 test1234 view testview oid 1.3.6.1.2.1
cumulus@switch:~$ net add snmp-server username user3 auth-sha testshax encrypt-aes testaesx oid 1.3.6.1.2.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

There are three directives that define an internal SNMPv3 username that are required for `snmpd` to retrieve information and send built-in traps or for those configured with the `monitor` command (see {{<link url="#configure-snmp-trap-and-inform-messages" text="below">}}):

- `createuser`: the default SNMPv3 username.
- `iquerysecName`: the default SNMPv3 username to use when making internal queries to retrieve monitored expressions &mdash; either for evaluating the monitored expression or building a notification payload. These internal queries always use SNMPv3, even if normal querying of the agent is done using SNMPv1 or SNMPv2c. The `iquerysecname` directive is purely concerned with defining which user should be used, not with actually setting this user up.
- `rouser`: the username for these SNMPv3 queries.

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

The following example shows a more advanced but slightly more secure method of configuring SNMPv3 users without creating cleartext passwords:

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

This adds a `createUser` command in `/var/lib/snmp/snmpd.conf`. Do **not** edit this file by hand unless you are removing usernames. You can edit this file and restrict access to certain parts of the MIB by adding *noauth*, *auth* or *priv* to allow unauthenticated access, require authentication, or to enforce use of encryption.

The `snmpd` daemon reads the information from the `/var/lib/snmp/snpmd.conf` file and then the line is removed (eliminating the storage of the master password for that user) and replaced with the key that is derived from it (using the EngineID). This key is a localized key, so that if it is stolen, it cannot be used to access other agents. To remove the two users `userMD5withDES` and `userSHAwithAES`, stop the `snmpd` daemon and edit the `/var/lib/snmp/snmpd.conf` file. Remove the lines containing the username, then restart the `snmpd` daemon as in step 3 above.

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

### Configure an SNMP View Definition

To restrict MIB tree exposure, you can define a view for an SNMPv3 username or community password, and a host from a restricted subnet. In doing so, any SNMP request with that username and password must have a source IP address within the configured subnet.

You can define a specific view multiple times and fine tune to provide or restrict access using the `included` or `excluded` command to specify branches of certain MIB trees.

By default, the `snmpd.conf` file contains numerous views within the *systemonly* view.

{{< tabs "viewname" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add snmp-server viewname cumulusOnly included .1.3.6.1.4.1.40310
cumulus@switch:~$ net add snmp-server viewname cumulusCounters included .1.3.6.1.4.1.40310.2
cumulus@switch:~$ net add snmp-server readonly-community simplepassword access any view cumulusOnly
cumulus@switch:~$ net add snmp-server username testusernoauth auth-none view cumulusOnly
cumulus@switch:~$ net add snmp-server username limiteduser1 auth-md5 md5password1 encrypt-aes myaessecret view cumulusCounters
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/snmp/snmpd.conf` file and add the `view` command.

The *systemonly* view is used by `rocommunity` to create a password for access to only these branches of the OID tree.

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

The `snmpd` authentication for SNMPv1 and SNMPv2c is disabled by default in Cumulus Linux. You enable it by providing a password (called a community string) for SNMPv1 or SNMPv2c environments so that the `snmpd` daemon can respond to requests. By default, this provides access to the full OID tree for such requests, regardless of from where they were sent. No default password is set, so `snmpd` does not respond to any requests that arrive unless you set the read-only community password.

For SNMPv1 and SNMPv2c you can specify a read-only community string. For SNMPv3, you can specify a read-only or a read-write community string (provided you are not using the preferred {{<link url="#configure-the-snmpv3-username" text="username method">}}  described above), but you must configure the read-write community string directly in the `snmpd.conf` file; you cannot use NCLU to configure it. If you configure a read-write community string, then edit the SNMP configuration later with NCLU, the read-write community configuration is preserved.

You can specify a source IP address token to restrict access to only that host or network given.

You can also specify a view to restrict the subset of the OID tree.

{{< tabs "community-string" >}}

{{< tab "NCLU Commands" >}}

The following example configuration:

- Sets the read only community string to *simplepassword* for SNMP requests
- Restricts requests to only those sourced from hosts in the 192.168.200.10/24 subnet
- Restricts viewing to the *mysystem* view defined with the `viewname` command

```
cumulus@switch:~$ net add snmp-server viewname mysystem included 1.3.6.1.2.1.1
cumulus@switch:~$ net add snmp-server readonly-community simplepassword access 192.168.200.10/24 view mysystem
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

This example creates a read-only community password *showitall* that allows access to the entire OID tree for requests originating from any source IP address.

```
cumulus@switch:~$ net add snmp-server readonly-community showitall access any
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

You enable the community string by providing a community string and then setting **rocommunity** (for read-only access) or **rwcommunity** (for read-write access). Other options you can specify are described below.

- `rocommunity`/`rwcommunity`: `rwcommunity` is for a read-only community; `rwcommunity` is for read-write access. Specify one or the other.
- `public`: The plaintext password/community string.

  {{%notice info%}}

Cumulus Networks strongly recommends you change this password to something else.

{{%/notice%}}

- `default`: Allows connections from any system.
- `localhost`: Allows requests only from the local host. A restricted source can either be a specific hostname (or address), or a subnet, represented as IP/MASK (like 10.10.10.0/255.255.255.0), or IP/BITS (like 10.10.10.0/24), or the IPv6 equivalents.
- `-V`: Restricts viewing to a specific {{<link url="#configure-an-snmp-view-name" text="view">}}. For example, *systemonly* is one SNMP view. This is a user-defined value.

Edit the `/etc/snmp/snmpd.conf` file and add the community string.

In the following example, the first line sets the read-only community string to *turtle* for SNMP requests sourced from the *192.168.200.10/24* subnet and restricts viewing to the *systemonly* view defined with the `-V` option. The second line creates a read-only community string that allows access to the entire OID tree from any source IP address.

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
- An administratively-assigned name for the managed node (the `sysname`).

{{< tabs "sys-settings" >}}

{{< tab "NCLU Commands" >}}

For example, to set the system physical location for the node in the SNMPv2-MIB system table, run:

```
cumulus@switch:~$ net add snmp-server system-location My private bunker
cumulus@switch:~$ net commit
```

To set the username and email address of the contact person for this managed node, run:

```
cumulus@switch:~$ net add snmp-server system-contact user X at myemail@example.com
cumulus@switch:~$ net commit
```

To set an administratively-assigned name for the managed node, run the following command. Typically, this is the fully-qualified domain name of the node.

```
cumulus@switch:~$ net add snmp-server system-name CumulusBox number 1,543,567
cumulus@switch:~$ net commit
```

These commands append the following content to the `/etc/snmp/snmpd.conf` file:

```
cumulus@switch:~$ cat /etc/snmp/snmpd.conf
...
syscontact user X at myemail@example.com
syslocation My private bunker
sysname CumulusBox number 1,543,567
...
```

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

## Enable SNMP Support for FRRouting

SNMP supports routing MIBs in {{<link url="FRRouting" text="FRRouting">}}. To enable SNMP support for FRRouting, you need to configure {{<exlink url="http://www.net-snmp.org/docs/README.agentx.html" text="AgentX">}} (ASX) access in FRR.

The default `/etc/snmp/snmpd.conf` configuration already enables AgentX and sets the correct permissions.

Enabling FRR includes support for BGP. However, if you plan on using the BGP4 MIB, be sure to provide access to the MIB tree 1.3.6.1.2.1.15.

{{%notice note%}}

At this time, SNMP does not support monitoring BGP unnumbered neighbors.

{{%/notice%}}

{{%notice tip%}}

If you plan on using the OSPFv2 MIB, provide access to 1.3.6.1.2.1.14 and to 1.3.6.1.2.1.191 for the OSPv3 MIB.

{{%/notice%}}

To enable SNMP support for FRR:

1. Configure AgentX access in FRR:

   ```
   cumulus@switch:~$ net add routing agentx
   cumulus@switch:~$ net pending
   cumulus@switch:~$ net commit
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

### Enable the .1.3.6.1.2.1 Range

Some MIBs, including storage information, are not included by default in `snmpd.conf` in Cumulus Linux. This results in some default views on common network tools (like `librenms`) to return less than optimal data. You can include more MIBs by enabling the complete .1.3.6.1.2.1 range. This simplifies the configuration file, removing the concern that any required MIBs might be missed by the monitoring system. Various MIBs included were added to the default SNMPv3 configuration and include the following:

- ENTITY-MIB
- ENTITY-SENSOR MIB
- Parts of the BRIDGE-MIB and Q-BRIDGE-MIBs

{{%notice warning%}}

This configuration grants access to a large number of MIBs, including all SNMPv2-MIB, which might reveal more data than expected. In addition to being a security vulnerability, it might consume more CPU resources.

{{%/notice%}}

To enable the .1.3.6.1.2.1 range, make sure the view commands include the required MIB objects.

## Restore the Default SNMP Configuration

The following command removes all custom entries in the `/etc/snmp/snmpd.conf` file and replaces them with defaults, including for all SNMPv3 usernames and readonly-communities. A `listening-address` for the localhost is configured in its place.

```
cumulus@switch:~$ net del snmp-server all
cumulus@switch:~$ net commit
```

## Set up the Custom Cumulus Networks MIBs on the NMS

No changes are required in the `/etc/snmp/snmpd.conf` file on the switch to support the custom Cumulus Networks MIBs. The following lines are already included by default and provide support for both the Cumulus Counters and the Cumulus Resource Query MIBs.

```
cumulus@switch:~$ cat /etc/snmp/snmpd.conf
...
sysObjectID 1.3.6.1.4.1.40310
pass_persist .1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
pass_persist .1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py
...
```

However, you need to copy several files to the NMS server for the custom Cumulus MIB to be recognized on the NMS server.

- `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`
- `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`
- `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt`

## Pass Persist Scripts

The pass persist scripts in Cumulus Linux use the {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tut:Extending_snmpd_using_shell_scripts#Pass_persist" text="pass_persist extension">}} to Net-SNMP. The scripts are stored in `/usr/share/snmp` and include:

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

All the scripts are enabled by default in Cumulus Linux, except for:

- `bgp4_pp.py`, which is handled by {{<link url="FRRouting" text="FRRouting">}}.
- `cl_poe_pp.py`, which is disabled by default as only certain platforms that Cumulus Linux supports are capable of doing {{<link url="Power-over-Ethernet-PoE" text="Power over Ethernet">}}.

## Example Configuration

The following example configuration:

- Enables an SNMP agent to listen on all IPv4 addresses with a community string password.
- Sets the trap destination host IP address.
- Creates four types of SNMP traps.

You can find a working example configuration on the {{<exlink url="https://gitlab.com/nvidia-networking/systems-engineering/poc-support/snmp-and-cl" text="NVIDIA Networking GitLab project">}}, which you can try for free with {{<exlink url="https://air.cumulusnetworks.com" text="Cumulus AIR">}}.

{{< tabs "example-config" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add snmp-server listening-address all
cumulus@switch:~$ net add snmp-server readonly-community tempPassword access any
cumulus@switch:~$ net add snmp-server trap-destination 1.1.1.1 community-password mypass version 2c
cumulus@switch:~$ net add snmp-server trap-link-up check-frequency 15
cumulus@switch:~$ net add snmp-server trap-link-down check-frequency 10
cumulus@switch:~$ net add snmp-server trap-cpu-load-average one-minute 7.45 five-minute 5.14
cumulus@switch:~$ net add snmp-server trap-snmp-auth-failures
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following `/etc/snmp/snmpd.conf` file:

```
cumulus@switch:~$ sudo nano /etc/snmp/snmpd.conf
agentaddress udp:161
agentxperms 777 777 snmp snmp
agentxsocket /var/agentx/master
+authtrapenable 1
createuser _snmptrapusernameX
iquerysecname _snmptrapusernameX
load 7.45 5.14 0
master agentx
monitor -r 60 -o laNames -o laErrMessage "laTable" laErrorFlag != 0
monitor CumulusLinkDOWN -S -r 10 -o ifName -o ifIndex -o ifAdminStatus -o ifOperStatus ifOperStatus == 2
monitor CumulusLinkUP -S -r 15 -o ifName -o ifIndex -o ifAdminStatus -o ifOperStatus ifOperStatus != 2
pass -p 10 1.3.6.1.2.1.1.1 /usr/share/snmp/sysDescr_pass.py
pass_persist 1.2.840.10006.300.43 /usr/share/snmp/ieee8023_lag_pp.py
pass_persist 1.3.6.1.2.1.17 /usr/share/snmp/bridge_pp.py
pass_persist 1.3.6.1.2.1.31.1.1.1.18 /usr/share/snmp/snmpifAlias_pp.py
pass_persist 1.3.6.1.2.1.47 /usr/share/snmp/entity_pp.py
pass_persist 1.3.6.1.2.1.99 /usr/share/snmp/entity_sensor_pp.py
pass_persist 1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
pass_persist 1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py
pass_persist 1.3.6.1.4.1.40310.3 /usr/share/snmp/cl_poe_pp.py
rocommunity neteng default
rocommunity tempPassword default
rouser _snmptrapusernameX
syslocation leaf01
sysobjectid 1.3.6.1.4.1.40310
sysservices 72
trap2sink 1.1.1.1 mypass
```

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
