---
title: Verify Software and Hardware Version Information
author: Cumulus Networks
weight: 701
toc: 4
---

Cumulus Linux users familiar with Cisco IOS may look for the same level
of information from commands they have learned and used over time. One
of the most common commands used in Cisco IOS
is `show version`,
which displays the currently loaded software along with hardware and
device information. This same level of information can be found in
Cumulus Linux using the following commands:

- `cat /etc/lsb-release`
- `cl-img-select`
- `decode-syseeprom`

## Use cat /etc/lsb-release to Verify the Running System Image

The following command displays the version of Cumulus Linux running in
the current slot, and will be updated to reflect version changes
accomplished via `apt-get`:

    cumulus@switch:~$ cat /etc/lsb-release   
    DISTRIB_ID=Cumulus Networks  
    DISTRIB_RELEASE=1.5.1  
    DISTRIB_DESCRIPTION=1.5.1-5c6829a-201309251712-final

## Use decode-syseeprom to Verify Hardware Model, Version and Other Vendor-specific Details

Similar to how Cisco offers the `show idprom` command for IOS and `show sprom` for NX-OS, Cumulus Networks created the `decode-syseeprom` command to provide a universal {{<exlink url="http://en.wikipedia.org/wiki/EEPROM" text="EEPROM">}} format that delivers a consistent way to display hardware platform-specific information. All vendors approved on the {{<exlink url="https://cumulusnetworks.com/hcl/" text="Cumulus Linux hardware compatibility list">}} adhere to this EEPROM format to be certified for Cumulus Linux.

For example:

    cumulus@switch:~$ sudo decode-syseeprom   
    TLV Name             Code Len Value  
    -------------------- ---- --- -----  
    Magic Number         0xFF   1 0xE0  
    Product Name         0x01   3 LB9  
    Part Number          0x02  11 1LB9BZZ0STQ  
    Serial Number        0x03  13 QTFCA63280046  
    Base MAC Address     0x04   6 08:9E:01:CE:C5:AA  
    Manufacture Date     0x05   4 2013/7/4  
    Card Type            0x06   4 0x00000001  
    Hardware Version     0x07   4 1.0  
    Label Revision       0x08   1 1  
    Model Name           0x09  10 QUANTA LB9  
    Software Version     0x0A   4 0.0.0.0  
    QUANTA-CRC           0x00   2 0x3B99  
    (checksum valid)

## Determine the Version of the Installed ONIE Software

Determining the ONIE version depends on the hardware architecture. The following command determines the hardware platform:

    cumulus@switch$ uname -m

| uname -m output | Architecture |
| --------------- | ------------ |
| ppc             | PowerPC      |
| armv7l          | ARM          |
| x86\_64         | x86          |

### x86

Reading the ONIE version on an x86 switch requires temporarily mounting
the ONIE partition as follows.

1.  Temporarily mount the ONIE partition read-only in order to read the
    ONIE version:\

        cumulus@switch$ sudo mkdir /mnt/onie
        cumulus@switch$ sudo mount -o ro -L ONIE-BOOT /mnt/onie

2.  Read the ONIE version:\

        cumulus@sw5$ grep ^onie_version /mnt/onie/grub/grub.cfg
        onie_version=2014.08.0.0.3

3.  Unmount the ONIE partition:\

        cumulus@switch$ sudo umount /mnt/onie

### PowerPC and ARM

The `fw_printenv` command is a U-Boot tool inherited from the standard
Debian distribution. It can be used to query the `onie_version`, the
version of ONIE installed with U-Boot.

For example:

    cumulus@switch:~$ fw_printenv onie_version  
    onie_version="1.3.0"
