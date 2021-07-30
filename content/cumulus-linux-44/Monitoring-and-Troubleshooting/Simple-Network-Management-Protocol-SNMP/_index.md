---
title: Simple Network Management Protocol - SNMP
author: NVIDIA
weight: 1150
toc: 3
---

SNMP is an IETF standards-based network management architecture and protocol. Cumulus Linux uses the open source Net-SNMP agent `snmpd` version 5.8.1.pre1, which provides support for most of the common industry-wide {{<link url="#management-information-base-mib" text="MIBs">}}, including interface counters and TCP/UDP IP stack data. The version in Cumulus Linux adds custom MIBs and pass-through and {{<link url="Configure-SNMP#pass-persist-scripts" text="pass-persist scripts">}}.

## SNMP Components

The main components of SNMP in Cumulus Linux are:

- SNMP network management system (NMS)
- SNMP agents
- The MIBs (management information bases)

### SNMP Network Management System

An SNMP network management system (NMS) is a system configured to poll SNMP agents (such as Cumulus Linux switches or routers) that can send query requests to SNMP agents with the correct credentials. The managers poll the agents and the agents respond with the data. There are a variety of command line tools for polling, including `snmpget`, `snmpgetnext`, `snmpwalk`, `snmpbulkget`, and `snmpbulkwalk`. SNMP agents can also send unsolicited traps and inform messages to the NMS based on predefined criteria, like link changes.

### SNMP Agent

The SNMP agent (the `snmpd` daemon) running on a Cumulus Linux switch gathers information about the local system and stores the data in a *management information base*, or MIB. Parts of the MIB tree are available and provided to incoming requests originating from an NMS host that has authenticated with the correct credentials. You can configure the Cumulus Linux switch with usernames and credentials to provide authenticated and encrypted responses to NMS requests. The `snmpd` agent can also proxy requests and act as a *master agent* to sub-agents running on other daemons, like for FRR or LLDP.

### Management Information Base (MIB)

The MIB is a database for the `snmpd` daemon that runs on the agent. MIBs adhere to IETF standards but are flexible enough to allow vendor-specific additions. Cumulus Linux includes custom enterprise MIB tables, which are defined in a set text files on the switch; the files are located in `/usr/share/snmp/mibs/` and their names all start with *Cumulus*. They include:
<!-- vale off -->
- Cumulus-Counters-MIB.txt
- Cumulus-POE-MIB.txt
- Cumulus-Resource-Query-MIB.txt
- Cumulus-Snmp-MIB.txt
<!-- vale on --> 
The MIB is structured as a top-down hierarchical tree. Each branch that forks off is labeled with both an identifying number (starting with 1) and an identifying string that is unique for that level of the hierarchy. The strings and numbers can be used interchangeably. The parent IDs (numbers or strings) are strung together, starting with the most general to form an address for the MIB object. Each junction in the hierarchy is represented by a dot in this notation so that the address ends up being a series of ID strings or numbers separated by dots. This entire address is known as an object identifier (OID).
<!-- vale off -->
You can use various online and command line tools to translate between numbers and strings and to also provide definitions for the various MIB objects. For example, you can view the *sysLocation* object (which is defined in `SNMPv2-MIB.txt`) in the system table as either a series of numbers *1.3.6.1.2.1.1.6* or as the string *iso.org.dod.internet.mgmt.mib-2.system.sysLocation*. You view the definition with the `snmptranslate` command, which is part of the `snmp` Debian package in Cumulus Linux.
<!-- vale on -->
```
cumulus@switch:~$ snmptranslate -Td -On SNMPv2-MIB::sysLocation
.1.3.6.1.2.1.1.6
sysLocation OBJECT-TYPE
  -- FROM       SNMPv2-MIB
  -- TEXTUAL CONVENTION DisplayString
  SYNTAX        OCTET STRING (0..255)
  DISPLAY-HINT  "255a"
  MAX-ACCESS    read-write
  STATUS        current
  DESCRIPTION   "The physical location of this node (e.g., 'telephone
            closet, 3rd floor').  If the location is unknown, the
            value is the zero-length string."
::= { iso(1) org(3) dod(6) internet(1) mgmt(2) mib-2(1) system(1) 6 }
```
<!-- vale off -->
In the last line above, the section *1.3.6.1* or *iso.org.dod.internet* is the OID that defines internet resources. The *2* or *mgmt* that follows is for a management subcategory. The *1* or *mib-2* under that defines the MIB-2 specification. The *1* or *system* is the parent for child objects *sysDescr*, *sysObjectID*, *sysUpTime*, *sysContact*, *sysName*, *sysLocation*, *sysServices*, and so on, as seen in the tree output from the second `snmptranslate` command below, where *sysLocation* is defined as *6*.
<!-- vale on -->
```
cumulus@leaf01:mgmt:~$ snmptranslate -Tp -IR system
+--system(1)
   |
   +-- -R-- String    sysDescr(1)
   |        Textual Convention: DisplayString
   |        Size: 0..255
   +-- -R-- ObjID     sysObjectID(2)
   +-- -R-- TimeTicks sysUpTime(3)
   |  |
   |  +--sysUpTimeInstance(0)
   |
   +-- -RW- String    sysContact(4)
   |        Textual Convention: DisplayString
   |        Size: 0..255
   +-- -RW- String    sysName(5)
   |        Textual Convention: DisplayString
   |        Size: 0..255
   +-- -RW- String    sysLocation(6)
   |        Textual Convention: DisplayString
   |        Size: 0..255
   +-- -R-- INTEGER   sysServices(7)
   |        Range: 0..127
   +-- -R-- TimeTicks sysORLastChange(8)
   |        Textual Convention: TimeStamp
   |
   +--sysORTable(9)
      |
      +--sysOREntry(1)
         |  Index: sysORIndex
         |
         +-- ---- INTEGER   sysORIndex(1)
         |        Range: 1..2147483647
         +-- -R-- ObjID     sysORID(2)
         +-- -R-- String    sysORDescr(3)
         |        Textual Convention: DisplayString
         |        Size: 0..255
         +-- -R-- TimeTicks sysORUpTime(4)
                  Textual Convention: TimeStamp
```
