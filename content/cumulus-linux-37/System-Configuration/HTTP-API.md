---
title: HTTP API
author: NVIDIA
weight: 79
pageID: 8362591
---
Cumulus Linux implements an HTTP (Web) application programing interface
to the {{<link url="OpenStack-Neutron-ML2-and-Cumulus-Linux" text="OpenStack ML2 driver">}}
and the {{<link url="Network-Command-Line-Utility-NCLU" text="NCLU">}}
API. Rather than accessing Cumulus Linux using SSH, you can interact with the
switch using an HTTP client, such as cURL, HTTPie or a web browser.

{{%notice note%}}

The HTTP API service is enabled by default on chassis hardware only.
However, the associated server is configured to only listen to traffic
originating from within the chassis.

The service is not enabled by default on non-chassis hardware.

{{%/notice%}}

## HTTP API Basics

{{%notice note%}}

If you are upgrading from a version of Cumulus Linux earlier than 3.4.0,
the supporting software for the API may not be installed. Install the
required software with the following command.

    cumulus@switch:~$ sudo apt-get install python-cumulus-restapi

Then restart the `nginx` service to apply the API configuration.

    cumulus@switch:~$ sudo systemctl restart nginx

{{%/notice%}}

To enable the HTTP API service, run the following `systemd` command:

    cumulus@switch:~$ sudo systemctl enable restserver

Use the `systemctl start` and `systemctl stop` commands to start/stop
the HTTP API service:

    cumulus@switch:~$ sudo systemctl start restserver
    cumulus@switch:~$ sudo systemctl stop restserver

Use the `systemctl disable` command to disable the HTTP API service
from running at startup:

    cumulus@switch:~$ sudo systemctl disable restserver

{{%notice note%}}

Each service runs as a background daemon once started.

{{%/notice%}}

## Configuration

There are two configuration files associated with the HTTP API services:

- `/etc/nginx/sites-available/nginx-restapi.conf`
- `/etc/nginx/sites-available/nginx-restapi-chassis.conf`

The first configuration file is used for non-chassis hardware; the
second, for chassis hardware.

Generally, only the configuration file relevant to your hardware needs
to be edited, as the associated services determine the appropriate
configuration file to use at run time.

### Enable External Traffic on a Chassis

The HTTP API services are configured to listen on port 8080 for chassis
hardware by default. However, only HTTP traffic originating from
internal link local management IPv6s will be allowed. To configure the
services to also accept HTTP requests originating from external sources:

1. Open `/etc/nginx/sites-available/nginx-restapi-chassis.conf` in a
   text editor.

2. Uncomment the `server` block lines near the end of the file.

3. Change the port on the now uncommented `listen` line if the default
   value, 8080, is not the preferred port, and save the configuration
   file.

4. Verify the configuration file is still valid:

        cumulus@switch:~$ sudo nginx -c /etc/nginx/sites-available/nginx-restapi-chassis.conf -t

    If the configuration file is not valid, return to step 1; review any
    changes that were made, and correct the errors.

5. Restart the daemons:

        cumulus@switch:~$ sudo systemctl restart restserver

### IP and Port Settings

The IP:port combinations that services listen to can be modified by
changing the parameters of the `listen` directive(s). By default,
`nginx-restapi.conf` has only one `listen` parameter, whereas
`/etc/nginx/sites-available/nginx-restapi-chassis.conf` has two
independently configurable `server` blocks, each with a `listen`
directive. One server block is for external traffic, and the other for
internal traffic.

{{%notice note%}}

All URLs must use HTTPS, rather than HTTP.

{{%/notice%}}

For more information on the listen directive, refer to the
{{<exlink url="https://nginx.org/en/docs/http/ngx_http_core_module.html#listen" text="NGINX documentation">}}.

{{%notice warning%}}

Do not set the same listening port for internal and external chassis
traffic.

{{%/notice%}}

## Security

### Authentication

The default configuration requires all HTTP requests from external
sources (not internal switch traffic) to set the HTTP Basic
Authentication header.

The user and password should correspond to a user on the host switch.

### Transport Layer Security

All traffic must be secured in transport using TLSv1.2 by default. Cumulus Linux contains a self-signed certificate and private key used server-side in this application so that it works out of the box, but using your own certificates and keys is recommended. Certificates must be in the PEM format.

For step by step documentation for generating self-signed certificates and keys, and installing them to the switch, refer to the
{{<exlink url="https://help.ubuntu.com/lts/serverguide/certificates-and-security.html" text="Ubuntu Certificates and Security documentation">}}.

{{%notice warning%}}

Do not copy the `cumulus.pem` or `cumulus.key` files. After
installation, edit the `ssl\_certificate` and `ssl\_certificate\_key`
values in the configuration file for your hardware.

{{%/notice%}}

## cURL Examples

This section contains several example cURL commands for sending HTTP
requests to a non-chassis host. The following settings are used for
these examples:

- Username: `user`
- Password: `pw`
- IP: `192.168.0.32`
- Port: `8080`

{{%notice note%}}

Requests for NCLU require setting the Content-Type request header to be
set to `application/json`.

{{%/notice%}}

{{%notice info%}}

The cURL `-k` flag is necessary when the server uses a self-signed
certificate. This is the default configuration (see the {{<link url="#security" text="Security section">}}). To display the response
headers, include `-D` flag in the command.

{{%/notice%}}

To retrieve a list of all available HTTP endpoints:

    cumulus@switch:~$ curl -X GET -k -u user:pw https://192.168.0.32:8080

To run `net show counters` on the host as a remote procedure call:

    cumulus@switch:~$ curl -X POST -k -u user:pw -H "Content-Type: application/json" -d '{"cmd": "show counters"}' https://192.168.0.32:8080/nclu/v1/rpc

To add a bridge using ML2:

    cumulus@switch:~$ curl -X PUT -k -u user:pw https://192.168.0.32:8080/ml2/v1/bridge/"br1"/200

## Caveats

The `/etc/restapi.conf` file is not listed in the `net show configuration files` command output.
