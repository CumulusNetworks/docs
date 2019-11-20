---
title: HTTP API
author: Cumulus Networks
weight: 81
aliases:
 - /display/DOCS/HTTP+API
 - /pages/viewpage.action?pageId=8366312
product: Cumulus Linux
version: '4.0'
---
Cumulus Linux implements an HTTP application programing interface to [OpenStack ML2 driver](../../Network-Solutions/OpenStack-Neutron-ML2-and-Cumulus-Linux/) and [NCLU](../Network-Command-Line-Utility-NCLU/). Instead of accessing Cumulus Linux using SSH, you can interact with the switch using an HTTP client, such as cURL, HTTPie or a web browser.

{{%notice note%}}

The HTTP API service is enabled by default on chassis hardware only. However, the associated server is configured to only listen to traffic originating from within the chassis.

The service is not enabled by default on non-chassis hardware.

{{%/notice%}}

### HTTP API Basics

The supporting software for the API is installed with Cumulus Linux.

To enable the HTTP API service, run the following `systemd` command:

```
cumulus@switch:~$ sudo systemctl enable restserver
```

Use the `systemctl start` and `systemctl stop` commands to start or stop the HTTP API service:

```
cumulus@switch:~$ sudo systemctl start restserver
cumulus@switch:~$ sudo systemctl stop restserver
```

{{%notice note%}}

Each service runs as a background daemon.

{{%/notice%}}

### Configuration

The HTTP API services use two configuration files:

- `/etc/nginx/sites-available/nginx-restapi.conf (`used for non-chassis hardware)
- `/etc/nginx/sites-available/nginx-restapi-chassis.conf` (used for chassis hardware)

You only need to edit the configuration file relevant to your hardware; the associated services determine the appropriate configuration file to use at run time.

#### Enable External Traffic on a Chassis

The HTTP API services are configured to listen on port 8080 for chassis hardware by default. However, only HTTP traffic originating from internal link local management IPv6s is allowed. To configure the services to also accept HTTP requests originating from external sources:

1. Open `/etc/nginx/sites-available/nginx-restapi-chassis.conf` in a text editor.
2. Uncomment the `server` block lines near the end of the file.
3. Change the port on the now uncommented `listen` line if the default value, 8080, is not the preferred port, and save the configuration file.
4. Verify that the configuration file is still valid:

```
cumulus@switch:~$ sudo nginx -c /etc/nginx/sites-available/nginx-restapi-chassis.conf -t
```

    If the configuration file is not valid, return to step 1; review any changes and correct the errors.

5. Restart the daemons:

```
cumulus@switch:~$ sudo systemctl restart restserver
```

#### IP and Port Settings

You can modify the IP:port combinations to which services listen by changing the parameters of the `listen` directive(s). By default, `nginx-restapi.conf` has only one `listen` parameter, whereas `/etc/nginx/sites-available/nginx-restapi-chassis.conf` has two independently configurable `server` blocks, each with a `listen` directive. One server block is for external traffic and the other for internal traffic.

{{%notice note%}}

All URLs must use HTTPS instead of HTTP.

{{%/notice%}}

For more information on the listen directive, refer to the [NGINX documentation](https://nginx.org/en/docs/http/ngx_http_core_module.html#listen).

{{%notice warning%}}

Do not set the same listening port for internal and external chassis traffic.

{{%/notice%}}

### Security

#### Authentication

The default configuration requires all HTTP requests from external sources (not internal switch traffic) to set the HTTP Basic Authentication header.

The user and password must correspond to a user on the host switch.

#### Transport Layer Security

All traffic must be secured in transport using TLSv1.2 by default. Cumulus Linux contains a self-signed certificate and private key used server-side in this application so that it works out of the box, but Cumulus Networks recommends you use your own certificates and keys. Certificates must be in the PEM format.

For step by step documentation for generating self-signed certificates
and keys, and installing them to the switch, refer to the [Ubuntu
Certificates and Security
documentation](https://help.ubuntu.com/lts/serverguide/certificates-and-security.html).

{{%notice warning%}}

Do not copy the `cumulus.pem` or `cumulus.key` files. After installation, edit the `ssl_certificate` and `ssl_certificate_key` values in the configuration file for your hardware.

{{%/notice%}}

### cURL Examples

This section includes several example cURL commands you can use to send HTTP requests to a non-chassis host. The following settings are used for these examples:

- Username: `user`
- Password: `pw`
- IP: `192.168.0.32`
- Port: `8080`

{{%notice note%}}

Requests for NCLU require setting the Content-Type request header to be set to `application/json`.

The cURL `-k` flag is necessary when the server uses a self-signed certificate. This is the default configuration (see the [Security section](#security)). To display the response headers, include the `-D` flag in the command.

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

## Caveats

The `/etc/restapi.conf` file is *not* listed in the `net show configuration files` command output.
