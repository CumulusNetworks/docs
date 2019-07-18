---
title: Configure and Manage DHCP Options
author: Cumulus Networks
weight: 33
aliases:
 - /display/NETQ141/Configure+and+Manage+DHCP+Options
 - /pages/viewpage.action?pageId=10453548
pageID: 10453548
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
The default DHCP configuration uses the eth0 interface on which to
listen and uses an address pool of 10.255.0.0/24. A default directory is
provided for the ONIE installer script and the default ZTP script.
Domain name, NTP, and web servers have assigned IP addresses. No
reservations are configured. While not required, you may want to s
<span style="color: #000000;"> pecify a DHCP address pool more
well-suited for your environment or set up reservations for interfaces
that require unchanging IP addresses. </span>

## Command Overview</span>

IPM enables you to add, delete, and view all of the DHCP configurations.
The command syntax is:

    tipctl add dhcp load [--dry-run|--mac <TEXT>|--hostname <TEXT>|--ip <TEXT>|--with-column|--without-column] [-h|--help]
    tipctl add dhcp pool [-h|--help] START_IP END_IP 
    tipctl add dhcp reservation [-h|--help] MAC IP [HOSTNAME]
     
    tipctl del dhcp pool [-h|--help]
    tipctl del dhcp reservation [-h|--help] MAC 
     
    tipctl show dhcp config [-h|--help]
    tipctl show dhcp leases [MAC] [-h|--help] 
    tipctl show dhcp reservations [MAC] [-h|--help]

The *-h* option provides help information for the command.

## View the Current DHCP Configuration</span>

<span style="color: #000000;"> You can view the current configuration of
the DHCP server using the `tipctl show dhcp` command. This example shows
the parameters configured by default on initial start up. Your settings
should reflect the IP addressing scheme of your network. </span>

    cumulus@ts:~$ tipctl show dhcp config
    Config                 Setting
    ---------------------  ----------------------------------------------
    interface              eth0
    subnet                 10.255.0.0/24
    default-ip-ttl         0xf0
    cumulus-provision-url  http://10.255.0.92:9300/default/ztp-default.sh
    default-url            http://10.255.0.92:9300/default/onie-installer
    domain-name            cltips
    domain-name-servers    10.255.0.92
    ntp-servers            10.255.0.92
    www-server             10.255.0.92

## Configure DHCP Address Pool</span>

You can configure a pool that uses a single contiguous address space.
You can also change or remove a configured address pool.

### Configure an Address Pool</span>

Only one DHCP address pool can be defined, and it must be contained
within a contiguous address space. The only exception to this is if you
accidentally configure the address pool with a range that includes the
Telemetry Server address, IPM breaks the pool into two smaller pools
excluding the TS address.

To configure an address pool:

1.  Use the `tipctl add dhcp pool` command and specify the starting and
    ending IP addresses for the space.

2.  Confirm the configuration.

3.  Verify that the change has not adversely impacted IPM operation.

This example shows the creation of an address pool with a starting IP
address of *10.255.0.100* and an ending IP address of *10.255.0.200*.
Then it shows the updated configuration with the newly created pool,
*pool 0*, and confirms the application is still running properly.

    cumulus@ts:~$ tipctl add dhcp pool 10.255.0.100 10.255.0.200
     
    cumulus@ts:~$ tipctl show dhcp config
    Config                 Setting
    ---------------------  ----------------------------------------------
    interface              eth0
    subnet                 10.255.0.0/24
    default-ip-ttl         0xf0
    cumulus-provision-url  http://10.255.0.92:9300/default/ztp-default.sh
    default-url            http://10.255.0.92:9300/default/onie-installer
    domain-name            cltips
    domain-name-servers    10.255.0.92
    ntp-servers            10.255.0.92
    www-server             10.255.0.92
    pool 0                 10.255.0.100 - 10.255.0.200
     
    cumulus@ts:~$ tipctl config verify
    The TIPS application is running as expected.

### Modify an Address Pool</span>

You might want to change the range of addresses available to the DHCP
server due to network changes or current address reservations. For
example, you may want to expand the pool as your network grows, or you
might want to change the range of addresses to avoid addresses that are
reserved.

To modify the existing address pool:

1.  Use the `tipctl add dhcp pool` command and specify the new starting
    and ending IP addresses for the space.

2.  Confirm the configuration.

3.  Verify that the change has not adversely impacted IPM operation.

This example shows the creation of an address pool with a starting IP
address of *10.255.0.100* and an ending IP address of *10.255.0.225*.
Then it shows the updated configuration with the newly modified pool,
*pool 0*, and confirms the application is still running properly.

    cumulus@ts:~$ tipctl add dhcp pool 10.255.0.100 10.255.0.225
     
    cumulus@ts:~$ tipctl show dhcp config
    Config                 Setting
    ---------------------  ----------------------------------------------
    interface              eth0
    subnet                 10.255.0.0/24
    default-ip-ttl         0xf0
    cumulus-provision-url  http://10.255.0.92:9300/default/ztp-default.sh
    default-url            http://10.255.0.92:9300/default/onie-installer
    domain-name            cltips
    domain-name-servers    10.255.0.92
    ntp-servers            10.255.0.92
    www-server             10.255.0.92
    pool 0                 10.255.0.100 - 10.255.0.225
     
    cumulus@ts:~$ tipctl config verify
    The TIPS application is running as expected.

### Remove an Address Pool</span>

You might want to remove the designated address pool altogether if you
are using a separate DHCP server or server pool in your network.

To remove an address pool:

1.  Use the `tipctl del dhcp` command with the *pool* keyword.

2.  Confirm the configuration change.

3.  Verify that the change has not adversely impacted IPM operation.

This example shows the removal of *address* *pool 0*, confirms that it
has been removed, and then verifies the application is still running
properly.

    cumulus@ts:~$ tipctl del dhcp pool
     
    cumulus@ts:~$ tipctl show dhcp config
    Config                 Setting
    ---------------------  ----------------------------------------------
    interface              eth0
    subnet                 10.255.0.0/24
    default-ip-ttl         0xf0
    cumulus-provision-url  http://10.255.0.92:9300/default/ztp-default.sh
    default-url            http://10.255.0.92:9300/default/onie-installer
    domain-name            cltips
    domain-name-servers    10.255.0.92
    ntp-servers            10.255.0.92
    www-server             10.255.0.92
     
    cumulus@ts:~$ tipctl config verify
    The TIPS application is running as expected.

## Configure DHCP Reservations</span>

<span style="color: #000000;"> DHCP reservations are used when you have
a switch that requires the same IP address every time you want to reach
it. Creating a reservation avoids having to look up the address for the
switch each time there is a need to talk to it and simplifies the
assignment because it is handled where the routing decision is made
rather than at the individual switches. Essentially, a DHCP reservation
provides a permanent lease of the address to a particular switch. The
reservation itself maps an IP address to the MAC address of the switch.
</span>

<span style="color: #000000;"> IPM enables you to add, delete, and view
DHCP reservations. Adding reservations can be performed one at a time or
import many from a file. </span>

### Add Reservations Manually</span>

<span style="color: #000000;"> You can add DHCP reservations one at a
time using the `tipctl add dhcp reservation` command. </span>

<span style="color: #000000;"> To add a reservation: </span>

1.  Use the `tipctl add dhcp reservation` command and specify the MAC
    address of the switch you want mapped and the IP address to use when
    talking to it. You can optionally specify a hostname.

2.  Confirm the configuration.

This example show the addition of reservation for spine01 with a MAC
address of *a0:00:00:00:00:21* and an IP address of *192.168.0.21.* We
have included the hostname for additional clarity, but that is optional.
The example then reviews the configuration change.

    cumulus@ts:~$ tipctl add dhcp reservation a0:00:00:00:00:21 192.168.0.21 spine01
    Reservation updated.
    cumulus@ts:~$ tipctl show dhcp reservations
    mac                ip            hostname
    -----------------  ------------  ----------
    A0:00:00:00:00:21  192.168.0.21  spine01

### Import Reservations from a File</span>

<span style="color: #000000;"> If you have a number of switches that you
want to specify DHCP reservations for, then importing the mapping
information using a comma separated values (.csv) file format might be
preferred. This is accomplished by piping the .csv file through the
standard input (stdin) method using the `tipctl add dhcp load` command.
There are several options for the import: </span>

| Option         | Description/Usage                                                                                                                                                                                                                                               |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dry-run        | Imports file, storing the mapping in the DB, but also prints the results to the standard output (stdout) where you can verify that the column mappings imported correctly                                                                                       |
| mac TEXT       | (Required) Location of MAC address in file. Specified by column name or offset.                                                                                                                                                                                 |
| hostname TEXT  | Location of hostname in file. Specified by column name or offset.                                                                                                                                                                                               |
| ip TEXT        | Location of IPv4 address in file. Specified by column name or offset.                                                                                                                                                                                           |
| with-column    | Causes command to calculate MAC, hostname, and IP values using the text specifying the column name. This is applied when the first row of the file contains header text instead of values. Either this option or the *without-column* option must be specified. |
| without-column | Causes command to calculate MAC, hostname, and IP values using a numeric offset. Either this option or the *with-column* option must be specified.                                                                                                              |

<span style="color: #000000;">  
To import reservations: </span>

1.  <span style="color: #000000;"> Use the `tipctl add dhcp load`
    command and specify the name of the column or an offset to the
    column in the file that contains the MAC address of the switch.
    </span>

2.  <span style="color: #000000;"> Optionally, specify a hostname to
    </span>

3.  <span style="color: #000000;"> Optionally, specify an IP address to
    </span>

4.  <span style="color: #000000;"> Specify method to calculate the MAC,
    hostname, and IP address value locations. </span>

5.  <span style="color: #000000;"> View the configuration change.
    </span>

<span style="color: #000000;"> A simple .csv file format might contain a
row for each switch with the MAC address listed first, hostname listed
second, and IP address listed. For example: </span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>MACaddr,Hostname,IPaddr</p>
<p>A0:00:00:00:00:21,spine01,192.168.0.21</p>
<p>A0:00:00:00:00:22,spine02,192.168.0.22</p>
<p>...</p></td>
</tr>
</tbody>
</table>

<span style="color: #000000;"> This example shows how to import the
above sample file. We have named the file *reservations.csv* and have
used column names to identify the locations of the data. </span>

    cumulus@ts:~$ tipctl add dhcp load < <path/reservations.csv> --mac MACaddr --hostname Hostname --ip IPaddr --with-column 
    cumulus@ts:~$ tipctl show dhcp reservations
    mac                ip            hostname
    -----------------  ------------  ----------
    A0:00:00:00:00:21  192.168.0.21  spine01
    A0:00:00:00:00:22  192.168.0.22  spine02
    ...

This example shows how to import the *reservations.csv* file using a
numeric offset to identify the locations of the data.

    cumulus@ts:~$ tipctl add dhcp load < <path/reservations.csv> --mac 0 --hostname 1 --ip 2 --without-column 
    cumulus@ts:~$ tipctl show dhcp reservations
    mac                ip            hostname
    -----------------  ------------  ----------
    A0:00:00:00:00:21  192.168.0.21  spine01
    A0:00:00:00:00:22  192.168.0.22  spine02
    ...

If the `dhcp load` command was not successful, when you run the `show`
command, a *No DHCP reservations* message appears.

### Remove a Reservation</span>

<span style="color: #000000;"> You can remove a DHCP reservation at any
time using the `tipctl` `del dhcp` command with the *reservation*
keyword. This example shows how to remove the reservation for the switch
with a MAC address of *A0:00:00:00:00:22*. </span>

    cumulus@ts:~$ tipctl del dhcp reservation a0:00:00:00:00:22 
    cumulus@ts:~$ tipctl show dhcp reservations
    mac                ip            hostname
    -----------------  ------------  ----------
    A0:00:00:00:00:21  192.168.0.21  spine01

## View Leases</span>

<span style="color: #000000;"> It can be useful to view the leases
currently being used by the DHCP server when you are troubleshooting.
You might need to determine why certain clients are not able to
connect–all of your leases are in use–or confirm whether a switch has
the expected address. </span>

<span style="color: #000000;"> To view leases, use the `tipctl show
leases` command. </span>

    cumulus@switch:~$ tipctl show dhcp leases
    mac               ip         ttl   expire              hostname
    ----------------- ---------- ----- ------------------- ----------
    70:72:CF:F5:5B:FE 89.0.0.151 3600  2018-09-26 22:18:27 sw1
    EC:0D:9A:AB:39:B4 89.0.0.152 3600  2018-09-26 22:20:58 sw2
    00:E0:EC:36:20:F0 89.0.0.153 3600  2018-09-26 22:22:56 sw3
    00:30:AB:F2:D7:A5 89.0.0.154 3600  2018-09-26 22:24:49 sw4

<span style="color: #000000;">  
</span>

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
