---
title: Configuring a Global Proxy
author: NVIDIA
weight: 260
toc: 3
---
You configure {{<exlink url="https://wiki.archlinux.org/index.php/proxy_settings" text="global HTTP and HTTPS proxies">}} in the `/etc/profile.d/` directory of Cumulus Linux. To do so, set the `http_proxy` and `https_proxy` variables, which tells the switch the address of the proxy server to use to fetch URLs on the command line. This is useful for programs such as `apt`/`apt-get`, `curl` and `wget`, which can all use this proxy.

1. In a terminal, create a new file in the `/etc/profile.d/` directory. In the code example below, the file is called `proxy.sh`, and is created using the text editor `nano`.

    ```
    cumulus@switch:~$ sudo nano /etc/profile.d/proxy.sh
    ```

2. Add a line to the file to configure either an HTTP or an HTTPS proxy, or both.

    ```
    http_proxy=http://myproxy.domain.com:8080
    export http_proxy

    https_proxy=https://myproxy.domain.com:8080
    export https_proxy
    ```

3. Create a file in the `/etc/apt/apt.conf.d` directory and add the following lines to the file for acquiring the HTTP and HTTPS proxies; the example below uses `http_proxy` as the file name:

    ```
    cumulus@switch:~$ sudo nano /etc/apt/apt.conf.d/http_proxy
    Acquire::http::Proxy "http://myproxy.domain.com:8080";
    Acquire::https::Proxy "https://myproxy.domain.com:8080";
    ```

4. Add the proxy addresses to `/etc/wgetrc`; you may have to uncomment the `http_proxy` and `https_proxy` lines:

    ```
    cumulus@switch:~$ sudo nano /etc/wgetrc
    ...
    https_proxy = https://myproxy.domain.com:8080
    http_proxy = http://myproxy.domain.com:8080
    ...
    ```

5. Run the `source` command, to execute the file in the current environment:

    ```
    cumulus@switch:~$ source /etc/profile.d/proxy.sh
    ```

The proxy is now configured. The `echo` command can be used to confirm aproxy is set up correctly:

- HTTP proxy:

    ```
    cumulus@switch:~$ echo $http_proxy
    http://myproxy.domain.com:8080
    ```

- HTTPS proxy:

    ```
    cumulus@switch:~$ echo $https_proxy
    https://myproxy.domain.com:8080
    ```

## Related Information

[Set up an apt package cache]({{<ref "/knowledge-base/Installing-and-Upgrading/Installation/Set-up-an-apt-Package-Cache.md" >}})
