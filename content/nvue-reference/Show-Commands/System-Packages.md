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
