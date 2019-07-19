---
title: IPM Command Line Overview
author: Cumulus Networks
weight: 29
aliases:
 - /display/NETQ141/IPM+Command+Line+Overview
 - /pages/viewpage.action?pageId=10453537
pageID: 10453537
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
The IPM CLI (TIPCTL) **** behaves in a similar manner to the other
Cumulus CLIs <span style="color: #333333;"> . It provides help for
commands and options, but it does not support TAB completion of commands
</span> <span style="color: #333333;"> . The commands support four
functional categories–configuration, DHCP (dynamic host control
protocol), network OS (operating system), and ZTP (zero-touch
provisioning): </span>

  - **config:** sets the network interface the service is bound to
    (either eth0 or eth1) and the IP address where it publishes.

  - **dhcp**: adds and deletes DHCP reservations of IP and hostname
    options, and shows reservations and leases.

  - **nos:** manages the mappings between meta-information sent by the
    [ONIE](https://opencomputeproject.github.io/onie/) tool and NOS
    (network operating system) images**.**

  - **ztp:** manages mappings between ZTP scripts and the
    meta-information the
    [ZTP](/display/NETQ141/Zero+Touch+Provisioning+-+ZTP) tool sends.

The TIPCTL syntax is organized around the command actions–add, delete,
show, configure, import, sync, and reset–for each of the functions, as
appropriate.

{{%notice note%}}

The NetQ IPM command line interface only runs on switches and server
hosts implemented with Intel x86 or ARM-based architectures.
<span style="color: #353744;"> If you are unsure what architecture your
switch or server employs, check the Cumulus [Hardware Compatibility
List](https://cumulusnetworks.com/products/hardware-compatibility-list/)
and verify the value in the **Platforms** tab \> **CPU** column. </span>

{{%/notice%}}

## CLI Access</span>

Once you have enabled the IPM service (refer to the [Activate and
Initialize
IPM](/version/cumulus-netq-141/Cumulus-NetQ-Image-and-Provisioning-Management-User-Guide/Activate-and-Initialize-IPM)
topic) and logged into the NetQ Telemetry Server (TS), simply enter
commands at the prompt. <span style="color: #353744;"> </span>

<span style="color: #353744;"> To access the CLI from TS: </span>

1.  <span style="color: #353744;"> Log in to TS. This example uses a
    username of *Cumulus* and a Telemetry Server with a name of *ts*.  
    </span>
    
        <computer>:~Cumulus$ ssh ts

2.  <span style="color: #353744;"> Enter your password, if required, to
    reach the command prompt. For example: </span>
    
        Enter passphrase for key '/Users/<username>/.ssh/id_rsa': 
        Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-112-generic x86_64)
         * Documentation:  https://help.ubuntu.com
         * Management:     https://landscape.canonical.com
         * Support:        https://ubuntu.com/advantage
        Last login: Thu Aug 16 06:28:12 2018 from 10.50.11.103
        Cumulus@ts:~$ 

3.  <span style="color: #353744;"> Run commands. For example:  
    </span>
    
        Cumulus@ts:~$ tipctl config setup
        Cumulus@ts:~$ tipctl add ztp 

## Command Line Structure</span>

<span style="color: #353744;"> The Cumulus NetQ IPM command line has a
flat structure as opposed to a modal structure. This means that all
commands can be run from the primary prompt instead of only in a
specific mode. </span> <span style="color: #353744;"> For example, some
command lines require the administrator to switch between a
configuration mode and an operation mode. Configuration commands can
only be run in the configuration mode and operational commands can only
be run in operation mode. This structure requires the administrator to
switch between modes to run commands which can be tedious and time
consuming. Cumulus NetQ IPM command line enables the administrator to
run all of its commands at the same level. </span>

## Command Syntax</span>

<span style="color: #353744;"> IPM CLI commands all begin with `tipctl`.
</span> The TIPCTL syntax is organized around the command actions–add,
delete, show, configure, import, sync, and reset. The syntax is as
follows:

    tipctl [--version|--help|-h] add [dhcp <options>|nos <options>|ztp <options>]
    tipctl [--version|--help|-h] config [setup <options>|verify <options>]
    tipctl [--version|--help|-h] del [dhcp <options>|nos <options>|ztp <options>]
    tipctl [--version|--help|-h] show [dhcp <options>|nos <options>|repo <options>|ztp <options>]

| Symbols               | Meaning                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| Parentheses ( )       | Enter one of the objects or keywords                                                              |
| Square brackets \[ \] | Optional parameter; enter keyword or keyword-value pair as needed                                 |
| Angle brackets \< \>  | Variable value for a keyword or option; required, enter according to your deployment nomenclature |
| Pipe |                | Separates keyword options, also separates value options; enter one keyword and zero or one value  |

## Command Prompt</span>

<span style="color: #353744;"> IPM code examples use the following
prompt: </span>

  - `cumulus@ts:~$` Indicates the user *cumulus* is logged in to the
    NetQ Telemetry Server (TS) to run the example command

The TS must be running the Cumulus Linux operating system (OS) and NetQ
. Refer to the [Install
NetQ](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
topic for details.

## Command Help</span>

<span style="color: #353744;"> As you enter commands, you can get help
with command syntax by entering --*help* or *-h* at various points
within a command entry. For example, to find out what options are
available for DHCP configuration, enter -*h* </span>
<span style="color: #353744;"> after entering a portion of the `tipctl
add dhcp` command. In this example, you can see that there are three
possible commands related to DHCP configuration. </span>

    cumulus@ts:~$ tipctl add dhcp -h
     
    Usage: tipctl add dhcp [OPTIONS] COMMAND [ARGS]...
      Add reservations and subnet pools
     
    Options:
      -h, --help  Show this message and exit.
     
    Commands:
      load         Load reservations from a CSV file via stdin
      pool         Add DHCP subnet pool
      reservation  Add DHCP reservation
     
    cumulus@ts:~$

## Command History</span>

The CLI stores commands issued within a session, which enables you to
review and rerun commands that have already been run. At the command
prompt, press the **Up Arrow** and **Down Arrow** keys to move back and
forth through the list of commands previously entered. When you have
found a given command, you can run the command by pressing **Enter**,
just as you would if you had entered it manually. Optionally you can
modify the command before you run it.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
