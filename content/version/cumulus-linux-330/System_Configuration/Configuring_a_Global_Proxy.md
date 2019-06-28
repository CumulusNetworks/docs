---
title: Configuring a Global Proxy
author: Cumulus Networks
weight: 77
aliases:
 - /display/CL330/Configuring+a+Global+Proxy
 - /pages/viewpage.action?pageId=5866124
pageID: 5866124
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
---
You configure [global HTTP and HTTPS
proxies](https://wiki.archlinux.org/index.php/proxy_settings) in the
`/etc/profile.d/` directory of Cumulus Linux. To do so, set the
`http_proxy` and `https_proxy` variables, which tells the switch the
address of the proxy server to use to fetch URLs on the command line.
This is useful for programs such as `apt`/`apt-get`, `curl` and `wget`,
which can all use this proxy.

1.  In a terminal, create a new file in the `/etc/profile.d/` directory.
    In the code example below, the file is called `proxy.sh`, and is
    created using the text editor `nano`.
    
        cumulus@switch:~$ sudo nano /etc/profile.d/proxy.sh

2.  Add a line to the file to configure either an HTTP or an HTTPS
    proxy, or both:
    
      - HTTP proxy:
        
            http_proxy=http://myproxy.domain.com:8080
            export http_proxy
    
      - HTTPS proxy:
        
            https_proxy=https://myproxy.domain.com:8080
            export https_proxy

3.  Create a file in the `/etc/apt/apt.conf.d` directory and add the
    following lines to the file for acquiring the HTTP and HTTPS
    proxies; the example below uses `http_proxy.sh` as the file name:
    
        cumulus@switch:~$ sudo nano /etc/apt/apt.conf.d/http_proxy.sh
        Acquire::http::Proxy "http://myproxy.domain.com:8080";
        Acquire::https::Proxy "https://myproxy.domain.com:8080";

4.  Add the proxy addresses to `/etc/wgetrc`; you may have to uncomment
    the `http_proxy` and `https_proxy` lines:
    
        cumulus@switch:~$ sudo nano /etc/wgetrc
        ...
         
        https_proxy = https://myproxy.domain.com:8080
        http_proxy = http://myproxy.domain.com:8080
         
        ...

5.  Run the `source` command, to execute the file in the current
    environment:
    
        cumulus@switch:~$ source /etc/profile.d/proxy.sh

The proxy is now configured. The `echo` command can be used to confirm a
proxy is set up correctly:

  - HTTP proxy:
    
        cumulus@switch:~$ echo $http_proxy
        http://myproxy.domain.com:8080

  - HTTPS proxy:
    
        cumulus@switch:~$ echo $https_proxy
        https://myproxy.domain.com:8080

## <span>Related Information</span>

  - [Setting up an apt package
    cache](https://support.cumulusnetworks.com/hc/en-us/articles/232058388-Setting-up-an-apt-Package-Cache)
