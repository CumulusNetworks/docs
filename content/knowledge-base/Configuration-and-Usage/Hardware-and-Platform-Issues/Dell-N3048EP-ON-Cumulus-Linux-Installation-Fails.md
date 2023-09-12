---
title: Dell N3048EP-ON - Cumulus Linux Installation Fails
author: NVIDIA
weight: 351
toc: 3
---

## Issue

You cannot install Cumulus Linux on early revisions of the Dell N3048EP-ON switch.

## Description

You cannot install Cumulus Linux on the A0 and A1 revisions of the Dell N3048EP-ON switch because its internal storage is only 1GB, which is insufficient to contain the operating system. You can install Cumulus Linux on revision A02 of the switch.

If you try to install Cumulus Linux on one of these earlier revisions, you get an error, and the OS does not install.

To determine the revision you have, boot into ONIE and run the `onie-syseeprom` command. Look for the **Label Revision** field. If its value is *A00* or *A01*, then you have one of the older, incompatible revisions.

     ONIE:~ # onie-syseeprom
     TlvInfo Header:
     Id String: TlvInfo
     Version: 1
     Total Length: 182
     TLV Name Code Len Value
     -------------------- ---- --- -----
     Product Name 0x21 10 N3048EP-ON
     Part Number 0x22 6 0JDFTF
     Serial Number 0x23 20 CN0JDFTFDND0093XXXX
     Base MAC Address 0x24 6 20:04:0F:3F:FF:FF
     Manufacture Date 0x25 19 03/22/2019 14:12:14
     Device Version 0x26 1 1
     Label Revision 0x27 3 A02
     Platform Name 0x28 31 armv7a-dellemc_n3048ep_iproc-r0
     ONIE Version 0x29 10 4.39.1.0-5
     MAC Addresses 0x2A 2 128
     Manufacturer 0x2B 5 DND00
     Country Code 0x2C 2 CN
     Vendor Name 0x2D 8 Dell EMC
     Diag Version 0x2E 10 4.39.3.0-1
     Service Tag 0x2F 7 JNSVXXX
     Vendor Extension 0xFD 4 0x00 0x00 0x02 0xA2
     CRC-32 0xFE 4 0x164CE9C2
     Checksum is valid.

## Resolution

To resolve this issue, contact your Dell representative. You cannot get a field replaceable unit for the storage, as it is permanently attached to the system.
