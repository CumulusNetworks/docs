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

## <h>nv show system packages key \<key-id\></h>

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ 
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository</h>

Showa the list of repositories and their details.

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

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution</h>

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution \<repo-dist-id\></h>

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution \<repo-dist-id\> pool</h>

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system packages repository \<repo-url-id\> distribution \<repo-dist-id\> pool \<repo-pool-id\></h>

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ 
```
