---
title: Configuring a Global Proxy
author: Cumulus Networks
weight: 65
aliases:
 - /display/CL25ESR/Configuring+a+Global+Proxy
 - /pages/viewpage.action?pageId=5115910
pageID: 5115910
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
[Global HTTP and HTTPS
proxies](https://wiki.archlinux.org/index.php/proxy_settings) are
configured in the `/etc/profile.d/` directory of Cumulus Linux.

1.  In a terminal, create a new file in the `/etc/profile.d/` directory.
    In the code example below, the file is called `proxy`, and is
    created using the text editor `vi`.
    
        cumulus@switch:~$ sudo vi /etc/profile.d/proxy

2.  Add a line to the file to configure either an HTTP or an HTTPS
    proxy, and save the file:
    
      - HTTP proxy:
        
            http_proxy=http://myproxy.domain.com:8080
            export http_proxy
    
      - HTTPS proxy:
        
            https_proxy=https://myproxy.domain.com:8080
            export https_proxy

3.  Run the `source` command, to execute the file in the current
    environment:
    
        cumulus@switch:~$ source /etc/profile.d/proxy

The proxy is now configured. The `echo` command can be used to confirm a
proxy is set up correctly:

  - HTTP proxy:
    
        cumulus@switch:~$ echo $http_proxy
        http://myproxy.domain.com:8080

  - HTTPS proxy:
    
        cumulus@switch:~$ echo $https_proxy
        https://myproxy.domain.com:8080
