---
title: Configure SNMP
author: Cumulus Networks
weight: 1082
toc: 4
---

The simplest use case for using SNMP consists of creating a read-only community password and enabling a listening address for the loopback address (this is the default listening-address provided). This allows for testing functionality of `snmpd` before extending the listening addresses to IP addresses reachable from outside the switch or router.

The following example adds a listening address on the loopback interface. Since this is not a change from the default, you see a message stating that the configuration has not changed. Then it sets a simple SNMPv2 community password for testing and changes the system-name object in the system table.

```
cumulus@switch:~$ net add snmp-server listening-address localhost
Cannot add 127.0.0.1. It is already a listener-address
The configuration has not changed.
cumulus@switch:~$ net add snmp-server readonly-community mynotsosecretpassword access any
cumulus@switch:~$ net add snmp-server system-name my little router
cumulus@switch:~$ net commit
```

To check the status of `snmpd`, run:

```
cumulus@switch:~$ net show snmp-server status

Simple Network Management Protocol (SNMP) Daemon.
---------------------------------  ----------------
Current Status                     active (running)
Reload Status                      enabled
Listening IP Addresses             localhost
Main snmpd PID                     13669
Version 1 and 2c Community String  Configured
Version 3 Usernames                Not Configured
---------------------------------  ----------------
```

This command gets the first MIB object in the system table:

```
cumulus@switch:~$ snmpgetnext -v 2c -c mynotsosecretpassword localhost SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: my little router
```

## Configure SNMP with NCLU

For external SNMP NMS systems to poll Cumulus Linux switches and routers, you must configure the SNMP agent (`snmpd`) running on the switch with one or more IP addresses (with `net add snmp-server listening-address <ip>`) on which the agent listens. You must configure these IP addresses on interfaces that have link state UP. By default, the SNMP configuration has a listening address of localhost (or 127.0.0.1), which allows the daemon to respond to SNMP requests originating on the switch itself. This is a useful method of checking the configuration for SNMP without exposing the switch to attacks from the outside. The only other required configuration is a readonly community password (configured with `net add snmp-server readonly-community <password> access <ip | any>)`, that allows polling of the various MIB objects on the device itself. SNMPv3 is recommended since SNMPv2c (with a community string) exposes the password in the `GetRequest` and `GetResponse` packets. SNMPv3 does not expose the username passwords and has the option of encrypting the packet contents.

{{%notice note%}}

- Cumulus Networks recommends that you use NCLU to configure `snmpd` even though NCLU does not provide functionality to configure every `snmpd` feature. You are not restricted to using NCLU for configuration and can edit the `/etc/snmp/snmpd.conf` file and control `snmpd` with `systemctl` commands.
- Cumulus Linux provides VRF listening-address, as well as Trap/Inform support. When management VRF is enabled, the eth0 interface is placed in the management VRF. When you configure the `listening-address` for `snmp-server`, you must run the `net add snmp-server listening-address <address> vrf mgmt` command to enable listening on the eth0 interface. These additional parameters are described in detail below.
- You must add a default community string for v1 or v2c environments so that the `snmpd` daemon can respond to requests. For security reasons, the default configuration configures `snmpd` to listen to SNMP requests on the loopback interface so access to the switch is restricted to requests originating from the switch itself. The only required commands for `snmpd` to function are a `listening-address` and either a `username` or a `readonly-community` string.

{{%/notice%}}


The table below highlights the structure of NCLU commands available for configuring SNMP. An example command set is provided below the table. NCLU restarts the `snmpd` daemon after configuration changes are made and committed.

| Command | Summary |
|-------- |-------- |
| net add snmp-server listening-address (localhost\|localhost-v6) | For security reasons, the localhost is set to a listening address 127.0.0.1 by default so that the SNMP agent only responds to requests originating on the switch itself. You can also configure listening only on the IPv6 localhost address with localhost-v6. When using IPv6 addresses or localhost, you can use a readonly-community-v6 for v1 and v2c requests. For v3 requests, you can use the username command to restrict access.<pre>net add snmp-server listening-address localhost<br>net add snmp-server listening-address localhost-v6</pre> |
| net add snmp-server listening-address (all\|all-v6) | Configures the `snmpd` agent to listen on all interfaces for either IPv4 or IPv6 UDP port 161 SNMP requests. This command removes all other individual IP addresses configured.<br><br>**Note**: This command does not allow `snmpd` to cross VRF table boundaries. To listen on IP addresses in different VRF tables, use multiple listening-address commands each with a VRF name, as shown below.<pre>net add snmp-server listening-address all<br>net add snmp-server listening-address all-v6</pre>|
| net add snmp-server listening-address IP_ADDRESS IP_ADDRESS ...|Sets `snmpd` to listen to a specific IPv4 or IPv6 address, or a group of addresses with space separated values, for incoming SNMP queries. If VRF tables are used, be sure to specify an IP address with an associated VRF name, as shown below. If you omit a VRF name, the default VRF is used.<pre>net add snmp-server listening-address 10.10.10.10<br>net add snmp-server listening-address 10.10.10.10 44.44.44.44</pre> |
|net add snmp-server listening-address IP_ADDRESS vrf VRF_NAME|Sets `snmpd` to listen to a specific IPv4 or IPv6 address on an interface within a particular VRF. With VRFs, identical IP addresses can exist in different VRF tables. This command restricts listening to a particular IP address within a particular VRF. If the VRF name is not given, the default VRF is used.<pre>net add snmp-server listening-address 10.10.10.10 vrf mgmt</pre> |
| net add snmp-server username \[user name\] (auth-none\|auth-md5\|auth-sha) PASSWORD \[(encrypt-des\|encrypt-aes) PASSWORD\] (oid <OID>\|view \<view name>) | Creates an SNMPv3 username and the necessary credentials for access. You can restrict a user to a particular OID tree or predefined view name if these are specified. If you specify auth-none, no authentication password is required. Otherwise, an MD5 or SHA password is required for access to the MIB objects. If specified, an encryption password is used to hide the contents of the request and response packets.<pre>net add snmp-server username testusernoauth  auth-none<br>net add snmp-server username testuserauth    auth-md5  myauthmd5password <br>net add snmp-server username testuserboth    auth-md5  mynewmd5password   encrypt-aes  myencryptsecret<br>net add snmp-server username limiteduser1    auth-md5  md5password1   encrypt-aes  myaessecret  oid 1.3.6.1.2.1.1</pre> |
| net add snmp-server viewname \[view name] (included\|excluded) \[OID or name] | Creates a view name that is used in readonly-community to restrict MIB tree exposure. By itself, this view definition has no effect; however, when linked to an SNMPv3 username or community password, and a host from a restricted subnet, any SNMP request with that username and password must have a source IP address within the configured subnet.<br><br>**Note**: OID can be either a string of period separated decimal numbers or a unique text string that identifies an SNMP MIB object. Some MIBs are not installed by default; you must install them either by hand or with the latest Debian package called snmp-mibs-downloader. You can remove specific view name entries with the delete command or with just a view name to remove all entries matching that view name. You can define a specific view name multiple times and fine tune to provide or restrict access using the included or excluded command to specify branches of certain MIB trees.<pre>net add snmp-server viewname cumulusOnly included .1.3.6.1.4.1.40310<br>net add snmp-server viewname cumulusCounters included .1.3.6.1.4.1.40310.2<br>net add snmp-server readonly-community simplepassword access any view cumulusOnly<br>net add snmp-server username testusernoauth  auth-none view cumulusOnly<br>net add snmp-server username limiteduser1  auth-md5 md5password1 encrypt-aes  myaessecret  view cumulusCounters</pre>|
| net add snmp-server (readonly-community \| readonly-community-v6) [password] access (any \| localhost \| [network]) [(view [view name]) or [oid [oid or name]) | This command defines the password required for SNMP version 1 or 2c requests for GET or GETNEXT. By default, this provides access to the full OID tree for such requests, regardless of from where they were sent. There is no default password set, so snmpd does not respond to any requests that arrive. Users often specify a source IP address token to restrict access to only that host or network given. You can specify a view name to restrict the subset of the OID tree.<br>Examples of readonly-community commands are shown below. The first command sets the read only community string to simplepassword for SNMP requests and this restricts requests to those sourced from hosts in the 10.10.10.0/24 subnet and restricts viewing to the mysystem view name defined with the viewname command. The second example creates a read-only community password showitall that allows access to the entire OID tree for requests originating from any source IP address.<pre>net add snmp-server viewname mysystem included 1.3.6.1.2.1.1<br>net add snmp-server readonly-community simplepassword access 10.10.10.0/24 view mysystem<br>net add snmp-server readonly-community showitall access any |
| net add snmp-server trap-destination (localhost \| [ipaddress]) [vrf vrf name] community-password [password] [version [1 \| 2c]] | For SNMP versions 1 and 2C, this command sets the SNMP Trap destination IP address. Multiple destinations can exist, but you must set up at least one to enable SNMP Traps to be sent. Removing all settings disables SNMP traps. The default version is 2c, unless otherwise configured. You must include a VRF name with the IP address to force Traps to be sent in a non-default VRF table.<pre>net add snmp-server trap-destination 10.10.10.10 community-password mynotsosecretpassword version 1<br>net add snmp-server trap-destination 20.20.20.20 vrf mgmt community-password mymanagementvrfpassword version 2c</pre>|
| net add snmp-server trap-destination (localhost \| [ipaddress]) [vrf vrf name] username \<v3 username\> (auth-md5\|auth-sha) PASSWORD [(encrypt-des\|encrypt-aes) PASSWORD] engine-id TEXT [inform] | For SNMPv3 Trap and Inform messages, this command configures the trap destination IP address (with an optional VRF name). You must define the authentication type and password. The encryption type and password are optional. You must specify the engine ID/user name pair. The inform keyword is used to specify an Inform message where the SNMP agent waits for an acknowledgement.<br>For Traps, the engine ID/user name is for the CL switch sending the traps. This can be found at the end of the /var/lib/snmp/snmpd.conf file labelled oldEngineID. Configure this same engine ID/user name (with authentication and encryption passwords) for the Trap daemon receiving the trap to validate the received Trap.<pre>net add snmp-server trap-destination 10.10.10.10 username myv3userrsion auth-md5 md5password1 encrypt-aes myaessecret engine-id  0x80001f888070939b14a514da5a00000000<br>net add snmp-server trap-destination 20.20.20.20 vrf mgmt username mymgmtvrfusername auth-md5 md5password2 encrypt-aes myaessecret2 engine-id  0x80001f888070939b14a514da5a00000000</pre>For Inform messages (Informs are acknowledged version 3 Traps), the engine ID/user name is the one used to create the username on the receiving Trap daemon server. The Trap receiver sends the response for the Trap message using its own engine ID/user name. In practice, the trap daemon generates the usernames with its own engine ID and after these are created, the SNMP server (or agent) needs to use these engine ID/user names when configuring the Inform messages so that they are correctly authenticated and the correct response is sent to the snmpd agent that sent it.<pre>net add snmp-server trap-destination 10.10.10.10 username myv3userrsion auth-md5 md5password1 encrypt-aes myaessecret engine-id  0x80001f888070939b14a514da5a00000000 inform<br>net add snmp-server trap-destination 20.20.20.20 vrf mgmt username mymgmtvrfusername auth-md5 md5password2 encrypt-aes myaessecret2 engine-id  0x80001f888070939b14a514da5a00000000 inform</pre> |
| net add snmp-server trap-link-up [check-frequency [seconds]] | Enables notifications for interface link-up to be sent to SNMP Trap destinations.<pre>net add snmp-server trap-link-up check-frequency 15</pre> |
| net add snmp-server trap-link-down [check-frequency [seconds]]|Enables notifications for interface link-down to be sent to SNMP Trap destinations.<pre>net add snmp-server trap-link-down check-frequency 10</pre> |
| net add snmp-server trap-snmp-auth-failures | Enables SNMP Trap notifications to be sent for every SNMP authentication failure.<pre>net add snmp-server trap-snmp-auth-failures</pre> |
| net add snmp-server trap-cpu-load-average one-minute [threshold] five-minute [5-min-threshold]fifteen-minute [15-min-threshold] | Enables a trap when the cpu-load-average exceeds the configured threshold. You can only use integers or floating point numbers.<pre>net add snmp-server trap-cpu-load-average one-minute 4.34 five-minute 2.32 fifteen-minute 6.5</pre> |

This table describes system setting configuration commands for SNMPv2-MIB.

| Command | Summary |
|-------- |-------- |
| net add snmp-server system-location [string] | Sets the system physical location for the node in the SNMPv2-MIB system table.<br />`net add snmp-server system-location  My private bunker` |
| net add snmp-server system-contact [string] | Sets the identification of the contact person for this managed node, together with information on how to contact this person.<br />`net add snmp-server system-contact user X at myemail@example.com` |
| net add snmp-server system-name [string] | Sets an administratively-assigned name for the managed node. By convention, this is the fully-qualified domain name of the node.<br />`net add snmp-server system-name CumulusBox number 1,543,567` |

### Example Configuration

The example commands below enable an SNMP agent to listen on all IPv4 addresses with a community string password, set the trap destination host IP address, and create four types of SNMP traps.

```
cumulus@switch:~$ net add snmp-server listening-address all
cumulus@switch:~$ net add snmp-server readonly-community tempPassword access any
cumulus@switch:~$ net add snmp-server trap-destination 1.1.1.1 community-password mypass version 2c
cumulus@switch:~$ net add snmp-server trap-link-up check-frequency 15
cumulus@switch:~$ net add snmp-server trap-link-down check-frequency 10
cumulus@switch:~$ net add snmp-server trap-cpu-load-average one-minute 7.45 five-minute 5.14
cumulus@switch:~$ net add snmp-server trap-snmp-auth-failures
```

### Restore the Default SNMP Configuration

The following command removes all custom entries in the `/etc/snmp/snmpd.conf` file and replaces them with defaults, including for all SNMPv3 usernames and readonly-communities. A `listening-address` for the localhost is configured in its place.

    cumulus@switch:~$ net del snmp-server all

## Configure SNMP Manually

If you need to manually edit the SNMP configuration; for example, if the necessary option has not been implemented in NCLU, you need to edit the configuration directly, which is stored in the `/etc/snmp/snmpd.conf` file.

Use caution when editing this file. The next time you use NCLU to update your SNMP configuration, if NCLU is unable to correctly parse the syntax, some of the options might be overwritten.

Make sure you do not delete the `snmpd.conf` file; this can cause issues with the package manager the next time you update Cumulus Linux.

The SNMP daemon, `snmpd`, uses the `/etc/snmp/snmpd.conf` configuration file for most of its configuration. The syntax of the most important keywords are defined in the following table.

| Syntax| Meaning|
|------ |------- |
| agentaddress | <strong>Required</strong>. This command sets the protocol, IP address, and the port for snmpd to listen for incoming requests. The IP address must exist on an interface that has link UP on the switch where snmpd is being used. By default, this is set to udp:127.0.0.1:161, which means snmpd listens on the loopback interface and only responds to requests (snmpwalk, snmpget, snmpgetnext) originating from the switch. A wildcard setting of udp:161,udp6:161 forces snmpd to listen on all IPv4 and IPv6 interfaces for incoming SNMP requests.<br><br>You can configure multiple IP addresses as comma-separated values; for example, udp:66.66.66.66:161,udp:77.77.77.77:161,udp6:[2001::1]:161. You can use multiple lines to define listening addresses. To bind to a particular IP address within a particular VRF table, follow the IP address with a @ and the name of the VRF table (for example, 10.10.10.10@mgmt). |
| rocommunity | <strong>Required</strong>. This command defines the password that is required for SNMP version 1 or 2c requests for GET or GETNEXT. By default, this provides access to the full OID tree for such requests, regardless of from where they were sent. There is no default password set, so snmpd does not respond to any requests that arrive. Specify a source IP address token to restrict access to only that host or network given. Specify a view name (as defined above) to restrict the subset of the OID tree.<br><br>Examples of rocommunity commands are shown below. The first command sets the read only community string to simplepassword for SNMP requests sourced from the 10.10.10.0/24 subnet and restricts viewing to the systemonly view name defined previously with the view command. The second example creates a read-only community password that allows access to the entire OID tree from any source IP address.<pre>rocommunity simplepassword 10.10.10.0/24 -V systemonly<br>rocommunity cumulustestpassword</pre> |
| view | This command defines a view name that specifies a subset of the overall OID tree. You can reference this restricted view by name in the rocommunity command to link the view to a password that is used to see this restricted OID subset. By default, the snmpd.conf file contains numerous views with the systemonly view name.<pre>view   systemonly  included   .1.3.6.1.2.1.1 <br>view   systemonly  included   .1.3.6.1.2.1.2<br>view   systemonly  included   .1.3.6.1.2.1.3</pre>The systemonly view is used by rocommunity to create a password for access to only these branches of the OID tree. |
| trapsink<br>trap2sink | This command defines the IP address of the notification (or trap) receiver for either SNMPv1 traps or SNMPv2 traps. If you specify several sink directives, multiple copies of each notification (in the appropriate formats) are generated. You must configure a trap server to receive and decode these trap messages (for example, snmptrapd). You can configure the address of the trap receiver with a different protocol and port but this is most often left out. The defaults are to use the well-known UDP packets and port 162. |
| createuser<br>iquerysecName<br>rouser | These three commands define an internal SNMPv3 username that is required for snmpd to send traps. This username is required to authorize the DisMan service even though SNMPv3 is not being configured for use. The example snmpd.conf configuration shown below creates snmptrapusernameX as the username (this is just an example username) using the createUser command. iquerysecname defines the default SNMPv3 username to be used when making internal queries to retrieve monitored expressions. rouser specifies the username for these SNMPv3 queries. All three are required for snmpd to retrieve information and send built-in traps or for those configured with the monitor command shown below in the examples.<pre>createuser snmptrapusernameX<br>iquerysecname snmptrapusernameX<br>rouser snmptrapusernameX</pre> |
| linkUpDownNotifications yes | This command enables link up and link down trap notifications, assuming the other trap configurations settings are set. This command configures the Event MIB tables to monitor the ifTable for network interfaces being taken up or down, and triggering a linkUp or linkDown notification as appropriate. This is equivalent to the following configuration:<pre>notificationEvent  linkUpTrap    linkUp   ifIndex ifAdminStatus ifOperStatus<br>notificationEvent  linkDownTrap  linkDown ifIndex ifAdminStatus ifOperStatus <br>monitor  -r 60 -e linkUpTrap   "Generate linkUp" ifOperStatus != 2<br>monitor  -r 60 -e linkDownTrap "Generate linkDown" ifOperStatus == 2</pre> |
| defaultMonitors yes | This command configures the Event MIB tables to monitor the various UCD-SNMP-MIB tables for problems (as indicated by the appropriate xxErrFlag column objects) and send a trap. This assumes you have downloaded the snmp-mibs-downloader Debian package and commented out mibs from the /etc/snmp/snmp.conf file (#mibs). This command is exactly equivalent to the following configuration:<pre>monitor   -o prNames -o prErrMessage "process table" prErrorFlag != 0<br>monitor   -o memErrorName -o memSwapErrorMsg "memory" memSwapError != 0<br>monitor   -o extNames -o extOutput "extTable" extResult != 0<br>monitor   -o dskPath -o dskErrorMsg "dskTable" dskErrorFlag != 0<br>monitor   -o laNames -o laErrMessage  "laTable" laErrorFlag != 0<br>monitor   -o fileName -o fileErrorMsg  "fileTable" fileErrorFlag != 0</pre> |

### Start the SNMP Daemon

Use the recommended process described below to start `snmpd` and monitor it using `systemctl`.

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

### Set up the Custom Cumulus Networks MIBs

No changes are required in the `/etc/snmp/snmpd.conf` file on the switch to support the custom Cumulus Networks MIBs. The following lines are already included by default and provide support for both the Cumulus Counters and the Cumulus Resource Query MIBs.

```
sysObjectID 1.3.6.1.4.1.40310
pass_persist .1.3.6.1.4.1.40310.1 /usr/share/snmp/resq_pp.py
pass_persist .1.3.6.1.4.1.40310.2 /usr/share/snmp/cl_drop_cntrs_pp.py
```

However, you need to copy several files to the NMS server for the custom Cumulus MIB to be recognized on the NMS server.

- `/usr/share/snmp/mibs/Cumulus-Snmp-MIB.txt`
- `/usr/share/snmp/mibs/Cumulus-Counters-MIB.txt`
- `/usr/share/snmp/mibs/Cumulus-Resource-Query-MIB.txt`

### Set the Community String

The `snmpd` authentication for versions 1 and 2 is disabled by default in Cumulus Linux. You can enable this password (called a community string) by setting **rocommunity** (for read-only access or **rwcommunity** (for read-write access). Setting a community string is required.

1. To enable read-only querying by a client, open the `/etc/snmp/snmpd.conf` file in a text editor and uncomment the following line:

   ```
   rocommunity public default -V systemonly
   ```

   | Keyword| Meaning|
   |------- |------- |
   | `rocommunity` | Read-only community; `rwcommunity` is for read-write access. |
   | `public` | Plain text password/community string.<br><br>**Note**: Cumulus Networks strongly recommends you change this password to something else. |
   | `default` | The default keyword allows connections from any system. The localhost keyword allows requests only from the local host. A restricted source can either be a specific hostname (or address), or a subnet, represented as IP/MASK (like 10.10.10.0/255.255.255.0), or IP/BITS (like 10.10.10.0/24), or the IPv6 equivalents. |
   |`systemonly`| The name of this particular SNMP view. This is a user-defined value. |

2. Restart `snmpd`:

   ```
   cumulus@switch:~$ systemctl restart snmpd.service
   ```

## Enable SNMP Support for FRRouting

SNMP supports Routing MIBs in {{<link url="FRRouting" text="FRRouting">}}. To enable SNMP support for FRRouting, you need to:

- Configure {{<exlink url="http://www.net-snmp.org/docs/README.agentx.html" text="AgentX">}} (ASX) access in FRR.
- The default `/etc/snmp/snmpd.conf` configuration already enables AgentX and sets the correct permissions.

Enabling FRR includes support for BGP. However, if you plan on using the BGP4 MIB, be sure to provide access to the MIB tree 1.3.6.1.2.1.15.

{{%notice note%}}

At this time, SNMP does not support monitoring BGP unnumbered neighbors.

{{%/notice%}}

If you plan on using the OSPFv2 MIB, provide access to 1.3.6.1.2.1.14 and to 1.3.6.1.2.1.191 for the OSPv3 MIB.

To enable SNMP support for FRR:

1. Configure AgentX access in FRR:

   ```
   cumulus@switch:~$ net add routing agentx
   cumulus@switch:~$ net pending
   cumulus@switch:~$ net commit
   ```

2. Update the SNMP configuration to enable FRR to respond to SNMP requests. Open the `/etc/snmp/snmpd.conf` file in a text editor and verify that the following configuration exists:

   ```
   agentxsocket /var/agentx/master
   agentxperms 777 777 snmp snmp
   master agentx
   ```

   {{%notice note%}}

Make sure that the `/var/agentx` directory is world-readable andworld-searchable (octal mode 755).

   {{%/notice%}}

3. Optionally, you might need to expose various MIBs:

    - For the BGP4 MIB, allow access to `1.3.6.1.2.1.15`
    - For the OSPF MIB, allow access to `1.3.6.1.2.1.14`
    - For the OSPFV3 MIB, allow access to `1.3.6.1.2.1.191`

To verify the configuration, run `snmpwalk`. For example, if you have a running OSPF configuration with routes, you can check this OSPF-MIB first from the switch itself with:

```
cumulus@switch:~$ sudo snmpwalk -v2c -cpublic localhost 1.3.6.1.2.1.14
```

### Enable the .1.3.6.1.2.1 Range

Some MIBs, including storage information, are not included by default in `snmpd.conf` in Cumulus Linux. This results in some default views on common network tools (like `librenms`) to return less than optimal data. You can include more MIBs by enabling all the .1.3.6.1.2.1 range. This simplifies the configuration file, removing concern that any required MIBs will be missed by the monitoring system. Various MIBs were added to version 3.0 and include the following: ENTITY and ENTITY-SENSOR MIB and parts of the BRIDGE-MIB and Q-BRIDGE-MIBs. These are included in the default configuration.

{{%notice warning%}}

This configuration grants access to a large number of MIBs, including all SNMPv2-MIB, which might reveal more data than expected. In addition to being a security vulnerability, it might consume more CPU resources.

{{%/notice%}}

To enable the .1.3.6.1.2.1 range, make sure the view name commands include the required MIB objects.

### Configure SNMPv3

SNMPv3 is often used to enable authentication and encryption, as community strings in versions 1 and 2c are sent in plaintext. SNMPv3 usernames are added to the `/etc/snmp/snmpd.conf` file, along with plaintext authentication and encryption pass phrases.

{{%notice note%}}

Cumulus Networks recommends that you configure SNMPv3 usernames and passwords with NCLU. However, if you prefer to edit the `/etc/snmp/snmpd.conf` manually instead, be aware that `snmpd` caches SNMPv3 usernames and passwords in the /`var/lib/snmp/snmpd.conf` file. Make sure you stop `snmpd` and remove the old entries when making changes. Otherwise, Cumulus Linux uses the old usernames and passwords in the `/var/lib/snmp/snmpd.conf` file instead of the ones in the `/etc/snmp/snmpd.conf` file.

{{%/notice%}}

The NCLU command structures for configuring SNMP user passwords are:

```
cumulus@switch:~$ net add snmp-server username <username> [auth-none] | [(auth-md5 | auth-sha) <auth-password>]
cumulus@switch:~$ net add snmp-server username <username> auth-(none | sha | md5)  (oid <OID> | view <view>)
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
```

After configuring user passwords and restarting the `snmpd` daemon, you can check user access with a client.

{{%notice note%}}

The `snmp` Debian package contains `snmpget`, `snmpwalk`, and other programs that are useful for checking daemon functionality from the switch itself or from another workstation.

{{%/notice%}}

The following commands check the access for each user defined above from the localhost:

```
# check user1 which has no authentication or encryption (NoauthNoPriv)
snmpget -v 3 -u user1 -l NoauthNoPriv localhost 1.3.6.1.2.1.1.1.0
snmpwalk -v 3 -u user1 -l NoauthNoPriv localhost 1.3.6.1.2.1.1
 
# check user2 which has authentication but no encryption (authNoPriv)
snmpget -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1.1.1.0
snmpget -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1.2.1.0
snmpwalk -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1
      
# check user3 which has both authentication and encryption (authPriv)
snmpget -v 3 -u user3 -l authPriv -a MD5 -A user3password -x DES -X user3encryption localhost .1.3.6.1.2.1.1.1.0
snmpwalk -v 3 -u user3 -l authPriv -a MD5 -A user3password -x DES -X user3encryption localhost .1.3.6.1.2.1
snmpwalk -v 3 -u user666 -l authPriv -a SHA -x AES -A user666password -X user666encryption localhost 1.3.6.1.2.1.1
snmpwalk -v 3 -u user999 -l authPriv -a MD5 -x DES -A user999password -X user999encryption localhost 1.3.6.1.2.1.1
```

The following procedure shows a slightly more secure method of configuring SNMPv3 users without creating cleartext passwords:

1. Install the `net-snmp-config` script that is in `libsnmp-dev` package:

   ```
   cumulus@switch:~$ sudo -E apt-get update
   cumulus@switch:~$ sudo -E apt-get install libsnmp-dev
   ```

2. Stop the daemon:

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

From a client, you access the MIB with the correct credentials. (The roles of `-x`, `-a` and `-X` and `-A` are reversed on the client side as compared with the `net-snmp-config` command used above.)

```
snmpwalk -v 3 -u userMD5withDES -l authPriv -a MD5 -x DES -A md5authpass -X desprivpass localhost 1.3.6.1.2.1.1.1
snmpwalk -v 3 -u userSHAwithAES -l authPriv -a SHA -x AES -A shaauthpass -X aesprivpass localhost 1.3.6.1.2.1.1.1
```

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
