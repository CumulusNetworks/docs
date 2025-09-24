---
title: System Packages
author: Cumulus Networks
weight: 407

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages</h>

Shows the list of repositories and keys on the switch.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages
         operational  applied
-------  -----------  -------
use-vrf               mgmt   

repository
=============
    Repository                                       Insecure  Source    Key  Distribution               Pool
    -----------------------------------------------  --------  --------  ---  -------------------------  ----
    copy:/var/lib/cumulus/cumulus-local-apt-archive  enabled   disabled       cumulus-local-apt-archive  main

key
======
    Key ID                                          Path                                                                   Scope 
    ----------------------------------------------  ---------------------------------------------------------------------  ------
    debian-archive-bookworm-automatic.asc           /etc/apt/trusted.gpg.d/debian-archive-bookworm-automatic.asc           global
    debian-archive-bookworm-security-automatic.asc  /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc  global
    debian-archive-bookworm-stable.asc              /etc/apt/trusted.gpg.d/debian-archive-bookworm-stable.asc              global
    debian-archive-bullseye-automatic.asc           /etc/apt/trusted.gpg.d/debian-archive-bullseye-automatic.asc           global
    debian-archive-bullseye-security-automatic.asc  /etc/apt/trusted.gpg.d/debian-archive-bullseye-security-automatic.asc  global
    debian-archive-bullseye-stable.asc              /etc/apt/trusted.gpg.d/debian-archive-bullseye-stable.asc              global
    debian-archive-buster-automatic.asc             /etc/apt/trusted.gpg.d/debian-archive-buster-automatic.asc             global
    debian-archive-buster-security-automatic.asc    /etc/apt/trusted.gpg.d/debian-archive-buster-security-automatic.asc    global
    debian-archive-buster-stable.asc                /etc/apt/trusted.gpg.d/debian-archive-buster-stable.asc                global
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages key</h>

Shows the list of package keys on the switch.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages key
Key ID                                          Path                                                                   Scope 
----------------------------------------------  ---------------------------------------------------------------------  ------ 
debian-archive-bookworm-automatic.asc           /etc/apt/trusted.gpg.d/debian-archive-bookworm-automatic.asc           global 
debian-archive-bookworm-security-automatic.asc  /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc  global 
debian-archive-bookworm-stable.asc              /etc/apt/trusted.gpg.d/debian-archive-bookworm-stable.asc              global 
sample-test-key.asc                             /etc/apt/keyrings/sample-test-key.asc                                  repository
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages key \<key-id\></h>

Shows details for a specific package key.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<key-id>`    | The key ID. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages key debian-archive-bookworm-automatic.asc
        operational 
 -----  --------------------------------------------------------------------- 
 scope  global 
 path   /etc/apt/trusted.gpg.d/debian-archive-bookworm-security-automatic.asc
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository</h>

Shows the list of repositories and their details.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages repository 
Repository                                    Insecure  Source   Distribution             Pool 
--------------------------------------------  --------  -------  -----------------------  ----------- 
https://apps3.cumulusnetworks.com/repos/deb/  enabled   enabled  CumulusLinux-d12         netq-latest 
                                                                 CumulusLinux-d12-latest  netq 
                                                                                          upstream 
https://apt.cumulusnetworks.com/repo                             CumulusLinux-d12-latest  cumulus 
                                                                                          netq 
                                                                                          upstream
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\></h>

Shows details for a specific repository.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<repo-url-id>` | The repository URL. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages repository https://apt.cumulusnetworks.com/repo
                operational              applied 
--------------  -----------------------  ------- 
insecure        enabled                  enabled 
source          enabled                  enabled 
[distribution]  CumulusLinux-d12         CumulusLinux-d12 
[distribution]  CumulusLinux-d12-latest  CumulusLinux-d12-latest
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution</h>

Shows the list of distributions for a repository.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<repo-url-id>` | The repository URL. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages repository https://apt.cumulusnetworks.com/repo distribution
Distribution      Origin            Version  Codename          Pool         Priority 
----------------  ----------------  -------  ----------------  -----------  --------
CumulusLinux-d12  Cumulus Networks           CumulusLinux-d12  netq-latest  991
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution \<repo-dist-id\></h>

Shows distribution details for a repository.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<repo-url-id>` | The repository URL. |
| `<repo-dist-id>` | The repository distribution ID. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages repository https://apps3.cumulusnetworks.com/repos/deb/ distribution CumulusLinux-d12 
          operational       applied 
--------  ----------------  ------- 
[pool]    netq-latest 
codename  CumulusLinux-d12 
origin    Cumulus Networks
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution \<repo-dist-id\> pool</h>

Shows the list of distribution pools for a repository.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<repo-url-id>` | The repository URL. |
| `<repo-dist-id>` | The repository distribution ID. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages repository https://apps3.cumulusnetworks.com/repos/deb/ distribution CumulusLinux-d12 pool 
Pool          priority 
--------      -------- 
netq-latest   100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution \<repo-dist-id\> pool \<repo-pool-id\></h>

Shows details for a specific distribution pool for a repository.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<repo-url-id>` | The repository URL. |
| `<repo-dist-id>` | The repository distribution ID. |
| `<repo-pool-id>` | The repository distribution pool ID. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system packages repository https://apps3.cumulusnetworks.com/repos/deb/ distribution CumulusLinux-d12 pool netq-latest
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system version image</h>

Shows the Cumulus Linux image build ID and build date.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system version image
            operational                   pending
----------  ----------------------------  -------
build-id    fac438cze6639cdd3                    
build-date  Wed Apr 16 06:07:57 UTC 2025
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system version packages installed</h>

Shows the packages installed on the switch.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system version packages installed 
Installed packages
=====================
    Installed package                      Description                                                                                                                                                                                                                                              Package                                Version                                  
    -------------------------------------  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  -------------------------------------  -----------------------------------------
    acpi                                   displays information on ACPI devices                                                                                                                                                                                                                     acpi                                   1.7-1.2                                  
    acpi-support-base                      scripts for handling base ACPI events such as the power button                                                                                                                                                                                           acpi-support-base                      0.143-5.1                                
    acpid                                  Advanced Configuration and Power Interface event daemon                                                                                                                                                                                                  acpid                                  1:2.0.33-2+b1                            
    adduser                                add and remove users and groups                                                                                                                                                                                                                          adduser                                3.134                                    
    apt                                    commandline package manager                                                                                                                                                                                                                              apt                                    2.6.1                                    
    arping                                 sends IP and/or ARP pings (to the MAC address)                                                                                                                                                                                                           arping                                 2.23-1                                   
    arptables                              ARP table administration                                                                                                                                                                                                                                 arptables                              0.0.5-3.1                                
    atftp                                  advanced TFTP client                                                                                                                                                                                                                                     atftp                                  0.8.0-3                                  
    atftpd                                 advanced TFTP server                                                                                                                                                                                                                                     atftpd                                 0.8.0-3                                  
    auditd                                 User space tools for security auditing                                                                                                                                                                                                                   auditd                                 1:3.0.9-1                                
    babeltrace                             Trace conversion program                                                                                                                                                                                                                                 babeltrace                             1.5.11-1+b2                              
    base-files                             Debian base system miscellaneous files                                                                                                                                                                                                                   base-files                             12.4+deb12u10                            
    base-passwd                            Debian base system master password and group files                                                                                                                                                                                                       base-passwd                            3.6.1                                    
    bash                                   GNU Bourne Again SHell                                                                                                                                                                                                                                   bash                                   5.2.15-2+b7                              
    bash-completion                        programmable completion for the bash shell                                                                                                                                                                                                               bash-completion                        1:2.11-6                                 
    bind9-dnsutils                         Clients provided with BIND 9                                                                                                                                                                                                                             bind9-dnsutils                         1:9.18.33-1~deb12u2                      
    bind9-host                             DNS Lookup Utility                                                                                                                                                                                                                                       bind9-host                             1:9.18.33-1~deb12u2                      
    bind9-libs                             Shared Libraries used by BIND 9                                                                                                                                                                                                                          bind9-libs                             1:9.18.33-1~deb12u2                      
    binutils                               GNU assembler, linker and binary utilities                                                                                                                                                                                                               binutils                               2.40-2                                   
    binutils-common                        Common files for the GNU assembler, linker and binary utilities                                                                                                                                                                                          binutils-common                        2.40-2                                   
    binutils-x86-64-linux-gnu              GNU binary utilities, for x86-64-linux-gnu target                                                                                                                                                                                                        binutils-x86-64-linux-gnu              2.40-2                                   
    bridge-utils                           Utilities for configuring the Linux Ethernet bridge                                                                                                                                                                                                      bridge-utils                           1.7.1-cl5.9.0u1                          
    bsd-mailx                              simple mail user agent                                                                                                                                                                                                                                   bsd-mailx                              8.1.2-0.20220412cvs-1
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system version packages installed \<package\></h>

Shows the version of a package installed on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<package>` | The package name. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show system version packages installed vrf
             operational        
-----------  -------------------
package      vrf                
version      1.0-cl5.9.0u4      
description  Linux tools for VRF
```
