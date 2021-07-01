---
title: HTTP API
author: NVIDIA
weight: 270
toc: 3
---
Cumulus Linux implements an HTTP application programming interface to the {{<link url="Network-Command-Line-Utility-NCLU" text="NCLU">}}. Instead of accessing Cumulus Linux using SSH, you can interact with the switch using an HTTP client, such as cURL, HTTPie or a web browser.

## HTTP API Basics

The supporting software for the API is installed with Cumulus Linux.

To use the REST API, you must enable `nginx` on the switch:

```
cumulus@switch:~$ sudo systemctl enable nginx; systemctl restart nginx
```

To enable the HTTP API service, run the following `systemd` command:

```
cumulus@switch:~$ sudo systemctl enable restserver
```

Use the `systemctl start` and `systemctl stop` commands to start or stop the service:

```
cumulus@switch:~$ sudo systemctl start restserver
cumulus@switch:~$ sudo systemctl stop restserver
```

Each service runs as a background daemon.

## Configure API Services

To configure the HTTP API services, edit the `/etc/nginx/sites-available/nginx-restapi.conf` configuration file, enter in the IP address in which the REST API will listen on and then run the command `sudo systemctl restart nginx`.

### IP and Port Settings

You can modify the IP:port combinations to which services listen by changing the parameters of the `listen` directives. By default, `nginx-restapi.conf` has only one `listen` parameter.

{{%notice note%}}

All URLs must use HTTPS instead of HTTP.

{{%/notice%}}

For more information on the listen directive, refer to the {{<exlink url="https://nginx.org/en/docs/http/ngx_http_core_module.html#listen" text="NGINX documentation">}}.

## Configure Security

### Authentication

The default configuration requires all HTTP requests from external sources (not internal switch traffic) to set the HTTP Basic Authentication header.

The user and password must correspond to a user on the host switch.

### Transport Layer Security

All traffic must be secured in transport using TLSv1.2 by default. Cumulus Linux contains a self-signed certificate and private key used server-side in this application so that it works out of the box, but NVIDIA recommends you use your own certificates and keys. Certificates must be in the PEM format.

For step by step documentation for generating self-signed certificates and keys, and installing them to the switch, refer to the {{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}.

{{%notice warning%}}

Do not copy the `cumulus.pem` or `cumulus.key` files. After installation, edit the `ssl_certificate` and `ssl_certificate_key` values in the configuration file for your hardware.

{{%/notice%}}
<!-- vale off -->
### cURL Examples
<!-- vale on --> 
This section includes several example cURL commands you can use to send HTTP requests to a host. The following settings are used for these examples:

- Username: `user`
- Password: `pw`
- IP: `192.168.0.32`
- Port: `8080`

{{%notice note%}}

Requests for NCLU require setting the Content-Type request header to be set to `application/json`.

The cURL `-k` flag is necessary when the server uses a self-signed certificate. This is the default configuration (see the {{<link url="#security" text="Security section">}}). To display the response headers, include the `-D` flag in the command.

{{%/notice%}}

To retrieve a list of all available HTTP endpoints:

```
cumulus@switch:~$ curl -X GET -k -u user:pw https://192.168.0.32:8080
```

To run `net show counters` on the host as a remote procedure call:

```
cumulus@switch:~$ curl -X POST -k -u user:pw -H "Content-Type: application/json" -d '{"cmd": "show counters"}' https://192.168.0.32:8080/nclu/v1/rpc
```

To add a bridge using ML2:

```
cumulus@switch:~$ curl -X PUT -k -u user:pw https://192.168.0.32:8080/ml2/v1/bridge/"br1"/200
```

## Considerations

The `/etc/restapi.conf` file is *not* listed in the `net show configuration files` command output.
