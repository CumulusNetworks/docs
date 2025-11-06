---
title: Simple Network Management Protocol - SNMP
author: NVIDIA
weight: 1150
toc: 3
---

SNMP is an IETF standards-based network management architecture and protocol. Cumulus Linux uses the open source Net-SNMP agent `snmpd`, which provides support for most of the common industry-wide {{<link url="#management-information-base-mib" text="MIBs">}}, including interface counters, and TCP and UDP IP stack data. The SNMP version in Cumulus Linux adds custom MIBs and pass-through, and {{<link url="Configure-SNMP#pass-persist-scripts" text="pass-persist scripts">}}.

## SNMP Components

The main components of SNMP in Cumulus Linux include:

- The SNMP network management system (NMS)
- SNMP agents
- The MIBs (management information bases)

### SNMP Network Management System

An SNMP network management system (NMS) is a system configured to poll SNMP agents (such as Cumulus Linux switches or routers), which respond with data. A variety of command line tools exist to poll agents, such as `snmpget`, `snmpgetnext`, `snmpwalk`, `snmpbulkget`, and `snmpbulkwalk`. SNMP agents can also send unsolicited traps and inform messages to the NMS based on predefined criteria, such as link changes.

### SNMP Agent

The SNMP agent (`snmpd`) running on a Cumulus Linux switch gathers information about the local system and stores the data in a MIB. Parts of the MIB tree are available and provided to incoming requests originating from an NMS host that has authenticated with the correct credentials. You can configure the Cumulus Linux switch with usernames and credentials to provide authenticated and encrypted responses to NMS requests. The `snmpd` agent can also proxy requests and act as a *master agent* to sub-agents running on other daemons, such as FRR or LLDP.

### Management Information Base (MIB)

The MIB is a database for the `snmpd` service that runs on the agent. MIBs adhere to IETF standards but are flexible enough to allow vendor-specific additions. Cumulus Linux includes custom enterprise MIB tables in a set of text files on the switch; the files are in `/usr/share/snmp/mibs/` and their names all start with *Cumulus*; for example, Cumulus-Counters-MIB.txt.

The MIB is a top-down hierarchical tree. Each branch that forks off has both an identifying number (starting with 1) and an identifying string that is unique for that level of the hierarchy. You can use the strings and numbers interchangeably. The parent IDs (numbers or strings) combine, starting with the most general to form an address for the MIB object. A dot in this notation represents each junction in the hierarchy so that the address is a series of ID strings or numbers separated by dots. This entire address is an object identifier (OID).
<!-- vale off -->
You can use various online and command line tools to translate between numbers and strings and to also provide definitions for the various MIB objects. For example, you can view the *sysLocation* object (in `SNMPv2-MIB.txt`) in the system table as either a series of numbers *1.3.6.1.2.1.1.6* or as the string *iso.org.dod.internet.mgmt.mib-2.system.sysLocation*. You view the definition with the `snmptranslate` command, which is part of the `snmp` Debian package in Cumulus Linux.
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
In the last line above, the section *1.3.6.1* or *iso.org.dod.internet* is the OID that defines internet resources. The *2* or *mgmt* that follows is for a management subcategory. The *1* or *mib-2* under that defines the MIB-2 specification. The *1* or *system* is the parent for child objects *sysDescr*, *sysObjectID*, *sysUpTime*, *sysContact*, *sysName*, *sysLocation*, *sysServices*, and so on, as you see in the tree output from the second `snmptranslate` command below, where *sysLocation* is *6*.
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
