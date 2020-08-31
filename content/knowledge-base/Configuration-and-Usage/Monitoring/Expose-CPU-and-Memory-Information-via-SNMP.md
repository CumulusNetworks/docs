---
title: Expose CPU and Memory Information via SNMP
author: Cumulus Networks
weight: 352
toc: 4
---

## Issue

How do I expose CPU and memory statistics via SNMP? What is the MIB/OID?

## Environment

- Cumulus Linux, all versions

## Resolution

The relevant OIDs are:

- CPU: .1.3.6.1.4.1.2021.11
    ({{<exlink url="http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt" text="UCD-SNMP-MIB::systemStats">}})
- Memory: .1.3.6.1.4.1.2021.4
    ({{<exlink url="http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt" text="UCD-SNMP-MIB::memory">}})

To configure SNMP to expose CPU and memory information:

1.  If `snmpd` has not already been enabled, follow instructions in the
    {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Monitoring-and-Troubleshooting/Simple-Network-Management-Protocol-SNMP/" text="technical documentation">}} to enable and start `snmpd`.
2.  Allow access to the OIDs by editing `/etc/snmp/snmpd.conf`. The
    following example adds the relevant MIBs to the `systemonly` view.

        ###############################################################################
        #
        #  ACCESS CONTROL
        #
        <CONFIGURATION_TRUNCATED/>
        # Cumulus specific
        view   systemonly  included   .1.3.6.1.4.1.40310.1
        view   systemonly  included   .1.3.6.1.4.1.40310.2
        # Memory utilization
        view   systemonly  included   .1.3.6.1.4.1.2021.4 
        # CPU utilization
        view   systemonly  included   .1.3.6.1.4.1.2021.11

3.  Restart `snmpd` to reload the configuration:

        cumulus@switch:~$ sudo service snmpd restart
