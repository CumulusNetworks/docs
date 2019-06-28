---
title: Configuring a Global Proxy
author: Cumulus Networks
weight: 69
aliases:
 - /display/CL31/Configuring+a+Global+Proxy
 - /pages/viewpage.action?pageId=5121944
pageID: 5121944
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
You configure [global HTTP and HTTPS
proxies](https://wiki.archlinux.org/index.php/proxy_settings) in the
`/etc/profile.d/` directory of Cumulus Linux. To do so, set the
`http_proxy` variable, which tells the switch the address of the proxy
server to use to fetch URLs on the command line. This is useful for
programs such as `apt`/`apt-get`, `curl` and `wget`, which can all use
this proxy.

1.  In a terminal, create a new file in the `/etc/profile.d/` directory.
    In the code example below, the file is called `proxy`, and is
    created using the text editor `vi`.
    
        cumulus@switch:~$ sudo vi /etc/profile.d/proxy.sh

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
    
        cumulus@switch:~$ source /etc/profile.d/proxy.sh

The proxy is now configured. The `echo` command can be used to confirm a
proxy is set up correctly:

  - HTTP proxy:
    
        cumulus@switch:~$ echo $http_proxy
        http://myproxy.domain.com:8080

  - HTTPS proxy:
    
        cumulus@switch:~$ echo $https_proxy
        https://myproxy.domain.com:8080

## <span>Related Links</span>

  - [Setting up an apt package
    cache](https://support.cumulusnetworks.com/hc/en-us/articles/232058388-Setting-up-an-apt-Package-Cache)
