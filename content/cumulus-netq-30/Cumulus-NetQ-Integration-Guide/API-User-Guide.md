---
title: Cumulus NetQ API User Guide
author: Cumulus Networks
weight: 205
toc: 3
---
The NetQ API provides access to key telemetry and system monitoring data
gathered about the performance and operation of your data center network
and devices so that you can view that data in your internal or
third-party analytic tools. The API gives you access to the health of
individual switches, network protocols and services, and views of
network-wide inventory and events.

This guide provides an overview of the API framework and some examples
of how to use the API to extract the data you need. Descriptions of each
endpoint and model parameter are contained in the API .json files.

For information regarding new features, improvements, bug fixes, and
known issues present in this release, refer to the
{{<link title="Cumulus NetQ 3.0 Release Notes" text="release notes">}}.

## API Organization

The Cumulus NetQ API provides endpoints for:

- **Network routing protocols**: BGP, EVPN, LLDP, CLAG, MSTP, Neighbors, NTP, Routes
- **Virtual networks**: VLAN
- **Services**: Services
- **Interfaces**: Interface, Port
- **Inventory and Devices**: Address, Inventory, MAC Address tables, Node, Sensors
- **Events**: Events

Each endpoint has its own API. You can make requests for all data and
all devices or you can filter the request by a given hostname.

Each API returns a predetermined set of data as defined in the API
models.

## Get Started

You can access the API gateway and execute requests from a terminal
interface against your NetQ Platform or NetQ Appliance through port
32708.

### Log In and Authentication

Use your login credentials that were provided as part of the
installation process. For this release, the default is username *admin*
and password *admin*.

To log in and obtain authorization:

1.  Open a terminal window.
2.  Enter the following curl command.

        <computer-name>:~ <username>$ curl --insecure -X POST "https://<netq.domain>:32708/netq/auth/v1/login" -H "Content-Type: application/json" -d '{"username":"admin","password":"admin"}'
        {"premises":[{"opid":0,"name":"OPID0"}],"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJvcGlkIjowLCJyb2xlIjoiYWRtaW4iLCJleHBpcmVzQXQiOjE1NTYxMjUzNzgyODB9.\_D2Ibhmo_BWSfAMnF2FzddjndTn8LP8CAFFGIj5tn0A","customer_id":0,"id":"admin","expires_at":1556125378280,"terms_of_use_accepted":true}

3.  Copy the access token for use in making data requests.

### API Requests

We will use curl to execute our requests. Each request contains an API
method (GET, POST, etc.), the address and API object to query, a variety
of headers, and sometimes a body. In the log in step you used above:

- API method = POST
- Address and API object = "https://\<netq.domain\>:32708/netq/auth/v1/login"
- Headers = -H "Content-Type: application/json"
- Body = -d '{"username":"admin","password":"admin"}'

{{%notice note%}}

We have used the *insecure* option to work around any certificate issues
with our development configuration. You would likely not use this
option.

{{%/notice%}}

### API Responses

A NetQ API response is comprised of a status code, any relevant error
codes (if unsuccessful), and the collected data (if successful).

The following HTTP status codes might be presented in the API responses:

| Code | Name                  | Description                                                                   | Action                                                                          |
| ---- | --------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 200  | Success               | Request was successfully processed.                                           | Review response                                                                 |
| 400  | Bad Request           | Invalid input was detected in request.                                        | Check the syntax of your request and make sure it matches the schema            |
| 401  | Unauthorized          | Authentication has failed or credentials were not provided.                   | Provide or verify your credentials, or request access from your administrator   |
| 403  | Forbidden             | Request was valid, but user may not have needed permissions.                  | Verify your credentials or request an account from your administrator           |
| 404  | Not Found             | Requested resource could not be found.                                        | Try the request again after a period of time or verify status of resource       |
| 409  | Conflict              | Request cannot be processed due to conflict in current state of the resource. | Verify status of resource and remove conflict                                   |
| 500  | Internal Server Error | Unexpected condition has occurred.                                            | Perform general troubleshooting and try the request again                       |
| 503  | Service Unavailable   | The service being requested is currently unavailable.                         | Verify the status of the NetQ Platform or Appliance, and the associated service |

## Example Requests and Responses

Some command requests and their responses are shown here, but feel free
to run your own requests. To run a request, you will need your
authorization token. We have piped our responses through a python tool
to make the responses more readable. You may chose to do so as well or
not.

To view all of the endpoints and their associated requests and
responses, refer to {{<link title="#View the API">}}.

### Get Network-wide Status of the BGP Service

Make your request to the *bgp* endpoint to obtain status information
from all nodes running the BGP service, as follows:

    curl --insecure -X GET "<https://<netq.domain>:32708/netq/telemetry/v1/object/bgp " -H "Content-Type: application/json " -H "Authorization: <auth-token> " | python -m json.tool
     
    [
      {
        "ipv6_pfx_rcvd": 0,
        "peer_router_id": "0.0.0.0",
        "objid": "",
        "upd8_tx": 0,
        "hostname": "exit-1",
        "timestamp": 1556037420723,
        "peer_asn": 0,
        "state": "NotEstd",
        "vrf": "DataVrf1082",
        "rx_families": [],
        "ipv4_pfx_rcvd": 0,
        "conn_dropped": 0,
        "db_state": "Update",
        "up_time": 0,
        "last_reset_time": 0,
        "tx_families": [],
        "reason": "N/A",
        "vrfid": 13,
        "asn": 655536,
        "opid": 0,
        "peer_hostname": "",
        "upd8_rx": 0,
        "peer_name": "swp7.4",
        "evpn_pfx_rcvd": 0,
        "conn_estd": 0
      },
      {
        "ipv6_pfx_rcvd": 0,
        "peer_router_id": "0.0.0.0",
        "objid": "",
        "upd8_tx": 0,
        "hostname": "exit-1",
        "timestamp": 1556037420674,
        "peer_asn": 0,
        "state": "NotEstd",
        "vrf": "default",
        "rx_families": [],
        "ipv4_pfx_rcvd": 0,
        "conn_dropped": 0,
        "db_state": "Update",
        "up_time": 0,
        "last_reset_time": 0,
        "tx_families": [],
        "reason": "N/A",
        "vrfid": 0,
        "asn": 655536,
        "opid": 0,
        "peer_hostname": "",
        "upd8_rx": 0,
        "peer_name": "swp7",
        "evpn_pfx_rcvd": 0,
        "conn_estd": 0
      },
      {
        "ipv6_pfx_rcvd": 24,
        "peer_router_id": "27.0.0.19",
        "objid": "",
        "upd8_tx": 314,
        "hostname": "exit-1",
        "timestamp": 1556037420665,
        "peer_asn": 655435,
        "state": "Established",
        "vrf": "default",
        "rx_families": [
          "ipv4",
          "ipv6",
          "evpn"
        ],
        "ipv4_pfx_rcvd": 26,
        "conn_dropped": 0,
        "db_state": "Update",
        "up_time": 1556036850000,
        "last_reset_time": 0,
        "tx_families": [
          "ipv4",
          "ipv6",
          "evpn"
        ],
        "reason": "N/A",
        "vrfid": 0,
        "asn": 655536,
        "opid": 0,
        "peer_hostname": "spine-1",
        "upd8_rx": 321,
        "peer_name": "swp3",
        "evpn_pfx_rcvd": 354,
        "conn_estd": 1
      },
    ...

### Get Status of EVPN on a Specific Switch

Make your request to the *evpn/hostname* endpoint to view the status of
all EVPN sessions running on that node. This example uses the *server01*
node.

    curl -X GET "https://<netq.domain>:32708/netq/telemetry/v1/object/evpn/hostname/server01" -H "Content-Type: application/json" -H "Authorization: <auth-token>" | python -m json.tool
     
    [
      {
        "import_rt": "[\"197:42\"]",
        "vni": 42,
        "rd": "27.0.0.22:2",
        "hostname": "server01",
        "timestamp": 1556037403853,
        "adv_all_vni": true,
        "export_rt": "[\"197:42\"]",
        "db_state": "Update",
        "in_kernel": true,
        "adv_gw_ip": "Disabled",
        "origin_ip": "27.0.0.22",
        "opid": 0,
        "is_l3": false
      },
      {
        "import_rt": "[\"197:37\"]",
        "vni": 37,
        "rd": "27.0.0.22:8",
        "hostname": "server01",
        "timestamp": 1556037403811,
        "adv_all_vni": true,
        "export_rt": "[\"197:37\"]",
        "db_state": "Update",
        "in_kernel": true,
        "adv_gw_ip": "Disabled",
        "origin_ip": "27.0.0.22",
        "opid": 0,
        "is_l3": false
      },
      {
        "import_rt": "[\"197:4001\"]",
        "vni": 4001,
        "rd": "6.0.0.194:5",
        "hostname": "server01",
        "timestamp": 1556036360169,
        "adv_all_vni": true,
        "export_rt": "[\"197:4001\"]",
        "db_state": "Refresh",
        "in_kernel": true,
        "adv_gw_ip": "Disabled",
        "origin_ip": "27.0.0.22",
        "opid": 0,
        "is_l3": true
      },
    ...

### Get Status on All Interfaces at a Given Time

Make your request to the *interfaces* endpoint to view the status of all
interfaces. By specifying the *eq-timestamp* option and entering a date
and time in epoch format, you indicate the data for that time (versus in
the last hour by default), as follows:

    curl -X GET "https://<netq.domain>:32708/netq/telemetry/v1/object/interface?eq_timestamp=1556046250" -H "Content-Type: application/json" -H "Authorization: <auth-token>" | python -m json.tool
     
    [
      {
        "hostname": "exit-1",
        "timestamp": 1556046270494,
        "state": "up",
        "vrf": "DataVrf1082",
        "last_changed": 1556037405259,
        "ifname": "swp3.4",
        "opid": 0,
        "details": "MTU: 9202",
        "type": "vlan"
      },
      {
        "hostname": "exit-1",
        "timestamp": 1556046270496,
        "state": "up",
        "vrf": "DataVrf1081",
        "last_changed": 1556037405320,
        "ifname": "swp7.3",
        "opid": 0,
        "details": "MTU: 9202",
        "type": "vlan"
      },
      {
        "hostname": "exit-1",
        "timestamp": 1556046270497,
        "state": "up",
        "vrf": "DataVrf1080",
        "last_changed": 1556037405310,
        "ifname": "swp7.2",
        "opid": 0,
        "details": "MTU: 9202",
        "type": "vlan"
      },
      {
        "hostname": "exit-1",
        "timestamp": 1556046270499,
        "state": "up",
        "vrf": "",
        "last_changed": 1556037405315,
        "ifname": "DataVrf1081",
        "opid": 0,
        "details": "table: 1081, MTU: 65536, Members:  swp7.3,  DataVrf1081,  swp4.3,  swp6.3,  swp5.3,  swp3.3, ",
        "type": "vrf"
      },
    ...

### Get a List of All Devices Being Monitored

Make your request to the *inventory* endpoint to get a listing of all
monitored nodes and their configuration information, as follows:

    curl -X GET "https://<netq.domain>:32708/netq/telemetry/v1/object/inventory" -H "Content-Type: application/json" -H "Authorization: <auth-token>" | python -m json.tool
     
    [
      {
        "hostname": "exit-1",
        "timestamp": 1556037425658,
        "asic_model": "A-Z",
        "agent_version": "2.1.1-cl3u16~1556035513.afedb69",
        "os_version": "A.2.0",
        "license_state": "ok",
        "disk_total_size": "10 GB",
        "os_version_id": "A.2.0",
        "platform_model": "A_VX",
        "memory_size": "2048.00 MB",
        "asic_vendor": "AA Inc",
        "cpu_model": "A-SUBLEQ",
        "asic_model_id": "N/A",
        "platform_vendor": "A Systems",
        "asic_ports": "N/A",
        "cpu_arch": "x86_64",
        "cpu_nos": "2",
        "platform_mfg_date": "N/A",
        "platform_label_revision": "N/A",
        "agent_state": "fresh",
        "cpu_max_freq": "N/A",
        "platform_part_number": "3.7.6",
        "asic_core_bw": "N/A",
        "os_vendor": "CL",
        "platform_base_mac": "00:01:00:00:01:00",
        "platform_serial_number": "00:01:00:00:01:00"
      },
      {
        "hostname": "exit-2",
        "timestamp": 1556037432361,
        "asic_model": "C-Z",
        "agent_version": "2.1.1-cl3u16~1556035513.afedb69",
        "os_version": "C.2.0",
        "license_state": "N/A",
        "disk_total_size": "30 GB",
        "os_version_id": "C.2.0",
        "platform_model": "C_VX",
        "memory_size": "2048.00 MB",
        "asic_vendor": "CC Inc",
        "cpu_model": "C-CRAY",
        "asic_model_id": "N/A",
        "platform_vendor": "C Systems",
        "asic_ports": "N/A",
        "cpu_arch": "x86_64",
        "cpu_nos": "2",
        "platform_mfg_date": "N/A",
        "platform_label_revision": "N/A",
        "agent_state": "fresh",
        "cpu_max_freq": "N/A",
        "platform_part_number": "3.7.6",
        "asic_core_bw": "N/A",
        "os_vendor": "CL",
        "platform_base_mac": "00:01:00:00:02:00",
        "platform_serial_number": "00:01:00:00:02:00"
      },
      {
        "hostname": "firewall-1",
        "timestamp": 1556037438002,
        "asic_model": "N/A",
        "agent_version": "2.1.0-ub16.04u15~1555608012.1d98892",
        "os_version": "16.04.1 LTS (Xenial Xerus)",
        "license_state": "N/A",
        "disk_total_size": "3.20 GB",
        "os_version_id": "(hydra-poc-01 /tmp/purna/Kleen-Gui1/)\"16.04",
        "platform_model": "N/A",
        "memory_size": "4096.00 MB",
        "asic_vendor": "N/A",
        "cpu_model": "QEMU Virtual  version 2.2.0",
        "asic_model_id": "N/A",
        "platform_vendor": "N/A",
        "asic_ports": "N/A",
        "cpu_arch": "x86_64",
        "cpu_nos": "2",
        "platform_mfg_date": "N/A",
        "platform_label_revision": "N/A",
        "agent_state": "fresh",
        "cpu_max_freq": "N/A",
        "platform_part_number": "N/A",
        "asic_core_bw": "N/A",
        "os_vendor": "Ubuntu",
        "platform_base_mac": "N/A",
        "platform_serial_number": "N/A"
      },
    ...

## View the API

For simplicity, all of the endpoint APIs are combined into a single
json-formatted file. There have been no changes to the file in the NetQ 3.0.0 release.

{{< expand "netq-300.json"  >}}

```
{
  "swagger": "2.0",
  "info": {
    "description": "This API is used to gain access to data collected by the Cumulus NetQ Platform and Agents for integration with third-party monitoring and analytics  software. Integrators can pull data for daily monitoring of network protocols and services performance, inventory status, and system-wide events.",
    "version": "1.1",
    "title": "Cumulus NetQ 3.0.0 API",
    "termsOfService": "https://cumulusnetworks.com/legal/"
  },
  "host": "<netq-platform-or-appliance-ipaddress>:32708",
  "basePath": "/netq/telemetry/v1",
  "externalDocs": {
    "description": "API Documentation",
    "url": "https://docs.nvidia.com/networking-ethernet-software/cumulus-netq/Cumulus-NetQ-Integration-Guide/API-User-Guide/"
  },
  "schemes": [
    "https"
  ],
  "paths": {
    "/object/address": {
      "get": {
        "tags": [
          "address"
        ],
        "summary": "Get all addresses for all network devices",
        "description": "Retrieves all IPv4, IPv6 and MAC addresses deployed on switches and hosts in your network running NetQ Agents.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Address"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/address/hostname/{hostname}": {
      "get": {
        "tags": [
          "address"
        ],
        "summary": "Get all addresses for a given network device by hostname",
        "description": "Retrieves IPv4, IPv6, and MAC addresses of a network device (switch or host) specified by its hostname.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Address"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/login": {
      "post": {
        "tags": [
          "auth"
        ],
        "summary": "Perform authenticated user login to NetQ",
        "description": "Sends user-provided login credentials (username and password) to the NetQ Authorization service for validation. Grants access to the NetQ platform and software if user credentials are valid.",
        "operationId": "login",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "in": "body",
            "name": "body",
            "description": "User credentials provided for login request; username and password.",
            "required": true,
            "schema": {
              "$ref": "#/definitions/LoginRequest"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/LoginResponse"
            }
          },
          "401": {
            "description": "Invalid credentials",
            "schema": {
              "$ref": "#/definitions/ErrorResponse"
            }
          }
        }
      }
    },
    "/object/bgp": {
      "get": {
        "tags": [
          "bgp"
        ],
        "summary": "Get all BGP session information for all network devices",
        "description": "For every Border Gateway Protocol (BGP) session running on the network, retrieves local node hostname, remote peer hostname, interface, router ID, and ASN, timestamp, VRF, connection state, IP and EVPN prefixes, and so forth. Refer to the BGPSession model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/BgpSession"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/bgp/hostname/{hostname}": {
      "get": {
        "tags": [
          "bgp"
        ],
        "summary": "Get all BGP session information for a given network device by hostname",
        "description": "For every BGP session running on the network device, retrieves local node hostname, remote peer hostname, interface, router ID, and ASN, timestamp, VRF, connection state, IP and EVPN prefixes, and so forth. Refer to the BGPSession model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/BgpSession"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/clag": {
      "get": {
        "tags": [
          "clag"
        ],
        "summary": "Get all CLAG session information for all network devices",
        "description": "For every Cumulus multiple Link Aggregation (CLAG) session running on the network, retrieves local node hostname, CLAG sysmac, remote peer role, state, and interface, backup IP address, bond status, and so forth. Refer to the ClagSessionInfo model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/ClagSessionInfo"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/clag/hostname/{hostname}": {
      "get": {
        "tags": [
          "clag"
        ],
        "summary": "Get all CLAG session information for a given network device by hostname",
        "description": "For every CLAG session running on the network device, retrieves local node hostname, CLAG sysmac, remote peer role, state, and interface, backup IP address, bond status, and so forth. Refer to the ClagSessionInfo model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/ClagSessionInfo"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/events": {
      "get": {
        "tags": [
          "events"
        ],
        "summary": "Get all events from across the entire network",
        "description": "Retrieves all alarm (critical severity) and informational (warning, info and debug severity) events from all network devices and services.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "gt_timestamp",
            "in": "query",
            "description": "Used in combination with lt_timestamp, sets the lower limit of the time range to display. Uses Epoch format. Cannot be used with eq_timestamp. For example, to display events between Monday February 11, 2019 at 1:00am and Tuesday February 12, 2019 at 1:00am, lt_timestamp would be entered as 1549864800 and gt_timestamp would be entered as 1549951200.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "lt_timestamp",
            "in": "query",
            "description": "Used in combination with gt_timestamp, sets the upper limit of the time range to display. Uses Epoch format. Cannot be used with eq_timestamp. For example, to display events between Monday February 11, 2019 at 1:00am and Tuesday February 12, 2019 at 1:00am, lt_timestamp would be entered as 1549864800 and gt_timestamp would be entered as 1549951200.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/evpn": {
      "get": {
        "tags": [
          "evpn"
        ],
        "summary": "Get all EVPN session information from across the entire network",
        "description": "For every Ethernet Virtual Private Network (EVPN) session running on the network, retrieves hostname, VNI status, origin IP address, timestamp, export and import routes, and so forth. Refer to the Evpn model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Evpn"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/evpn/hostname/{hostname}": {
      "get": {
        "tags": [
          "evpn"
        ],
        "summary": "Get all EVPN session information from a given network device by hostname",
        "description": "For every EVPN session running on the network device, retrieves hostname, VNI status, origin IP address, timestamp, export and import routes, and so forth. Refer to the Evpn model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Evpn"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/interface": {
      "get": {
        "tags": [
          "interface"
        ],
        "summary": "Get software interface information for all network devices",
        "description": "Retrieves information about all software interfaces, including type and name of the interfaces, the hostnames of the device where they reside, state, VRF, and so forth. Refer to the Interface model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Interface"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/interface/hostname/{hostname}": {
      "get": {
        "tags": [
          "interface"
        ],
        "summary": "Get software interface information for a given network device by hostname",
        "description": "Retrieves information about all software interfaces on a network device, including type and name of the interfaces, state, VRF, and so forth. Refer to the Interface model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Interface"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/inventory": {
      "get": {
        "tags": [
          "inventory"
        ],
        "summary": "Get component inventory information from all network devices",
        "description": "Retrieves the hardware and software component information, such as ASIC, platform, and OS vendor and version information, for all switches and hosts in your network. Refer to the InventoryOutput model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/InventoryOutput"
            }
          },
          "400": {
            "description": "Invalid Input"
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/inventory/hostname/{hostname}": {
      "get": {
        "tags": [
          "inventory"
        ],
        "summary": "Get component inventory information from a given network device by hostname",
        "description": "Retrieves the hardware and software component information, such as ASIC, platform, and OS vendor and version information, for the given switch or host in your network. Refer to the InventoryOutput model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "$ref": "#/definitions/InventoryOutput"
            }
          },
          "400": {
            "description": "Invalid Input"
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/lldp": {
      "get": {
        "tags": [
          "lldp"
        ],
        "summary": "Get LLDP information for all network devices",
        "description": "Retrieves Link Layer Discovery Protocol (LLDP) information, such as hostname, interface name, peer hostname, interface name, bridge, router, OS, timestamp, for all switches and hosts in the network. Refer to the LLDP model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/LLDP"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/lldp/hostname/{hostname}": {
      "get": {
        "tags": [
          "lldp"
        ],
        "summary": "Get LLDP information for a given network device by hostname",
        "description": "Retrieves Link Layer Discovery Protocol (LLDP) information, such as hostname, interface name, peer hostname, interface name, bridge, router, OS, timestamp, for the given switch or host. Refer to the LLDP model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/LLDP"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/macfdb": {
      "get": {
        "tags": [
          "macfdb"
        ],
        "summary": "Get all MAC FDB information for all network devices",
        "description": "Retrieves all MAC address forwarding database (MACFDB) information for all switches and hosts in the network, such as MAC address, timestamp, next hop, destination, port, and VLAN. Refer to MacFdb model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/MacFdb"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/macfdb/hostname/{hostname}": {
      "get": {
        "tags": [
          "macfdb"
        ],
        "summary": "Get all MAC FDB information for a given network device by hostname",
        "description": "Retrieves all MAC address forwarding database (MACFDB) information for a given switch or host in the network, such as MAC address, timestamp, next hop, destination, port, and VLAN. Refer to MacFdb model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/MacFdb"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/mstp": {
      "get": {
        "tags": [
          "mstp"
        ],
        "summary": "Get all MSTP information from all network devices",
        "description": "Retrieves all Multiple Spanning Tree Protocol (MSTP) information, including bridge and port information, changes made to topology, and so forth for all switches and hosts in the network. Refer to MstpInfo model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/MstpInfo"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/mstp/hostname/{hostname}": {
      "get": {
        "tags": [
          "mstp"
        ],
        "summary": "Get all MSTP information from a given network device by hostname",
        "description": "Retrieves all MSTP information, including bridge and port information, changes made to topology, and so forth for a given switch or host in the network.  Refer to MstpInfo model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/MstpInfo"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/neighbor": {
      "get": {
        "tags": [
          "neighbor"
        ],
        "summary": "Get neighbor information for all network devices",
        "description": "Retrieves neighbor information, such as hostname, addresses, VRF, interface name and index, for all switches and hosts in the network.  Refer to Neighbor model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Neighbor"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/neighbor/hostname/{hostname}": {
      "get": {
        "tags": [
          "neighbor"
        ],
        "summary": "Get neighbor information for a given network device by hostname",
        "description": "Retrieves neighbor information, such as hostname, addresses, VRF, interface name and index, for a given switch or host in the network.  Refer to Neighbor model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Neighbor"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/node": {
      "get": {
        "tags": [
          "node"
        ],
        "summary": "Get device status for all network devices",
        "description": "Retrieves hostname, uptime, last update, boot and re-initialization time, version, NTP and DB state, timestamp, and its current state (active or not) for all switches and hosts in the network.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/NODE"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/node/hostname/{hostname}": {
      "get": {
        "tags": [
          "node"
        ],
        "summary": "Get device status for a given network device by hostname",
        "description": "Retrieves hostname, uptime, last update, boot and re-initialization time, version, NTP and DB state, timestamp, and its current state (active or not) for a given switch or host in the network.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/NODE"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/ntp": {
      "get": {
        "tags": [
          "ntp"
        ],
        "summary": "Get all NTP information for all network devices",
        "description": "Retrieves all Network Time Protocol (NTP) configuration and status information, such as whether the service is running and if it is in time synchronization, for all switches and hosts in the network. Refer to the NTP model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/NTP"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/ntp/hostname/{hostname}": {
      "get": {
        "tags": [
          "ntp"
        ],
        "summary": "Get all NTP information for a given network device by hostname",
        "description": "Retrieves all Network Time Protocol (NTP) configuration and status information, such as whether the service is running and if it is in time synchronization, for a given switch or host in the network. Refer to the NTP model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/NTP"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/port": {
      "get": {
        "tags": [
          "port"
        ],
        "summary": "Get all information for all physical ports on all network devices",
        "description": "Retrieves all physical port information, such as speed, connector, vendor, part and serial number, and FEC support, for all network devices. Refer to Port model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Port"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/port/hostname/{hostname}": {
      "get": {
        "tags": [
          "port"
        ],
        "summary": "Get all information for all physical ports on a given network device by hostname",
        "description": "Retrieves all physical port information, such as speed, connector, vendor, part and serial number, and FEC support, for a given switch or host in the network. Refer to Port model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Port"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/route": {
      "get": {
        "tags": [
          "route"
        ],
        "summary": "Get all route information for all network devices",
        "description": "Retrieves route information, such as VRF, source, next hops, origin, protocol, and prefix, for all switches and hosts in the network. Refer to Route model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Route"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/route/hostname/{hostname}": {
      "get": {
        "tags": [
          "route"
        ],
        "summary": "Get all route information for a given network device by hostname",
        "description": "Retrieves route information, such as VRF, source, next hops, origin, protocol, and prefix, for a given switch or host in the network. Refer to Route model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Route"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/sensor": {
      "get": {
        "tags": [
          "sensor"
        ],
        "summary": "Get all sensor information for all network devices",
        "description": "Retrieves data from fan, temperature, and power supply unit sensors, such as their name, state, and threshold status, for all switches and hosts in the network. Refer to Sensor model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Sensor"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/sensor/hostname/{hostname}": {
      "get": {
        "tags": [
          "sensor"
        ],
        "summary": "Get all sensor information for a given network device by hostname",
        "description": "Retrieves data from fan, temperature, and power supply unit sensors, such as their name, state, and threshold status, for a given switch or host in the network. Refer to Sensor model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Sensor"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/services": {
      "get": {
        "tags": [
          "services"
        ],
        "summary": "Get all services information for all network devices",
        "description": "Retrieves services information, such as XXX, for all switches and hosts in the network. Refer to Services for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Services"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/services/hostname/{hostname}": {
      "get": {
        "tags": [
          "services"
        ],
        "summary": "Get all services information for a given network device by hostname",
        "description": "Retrieves services information, such as XXX, for a given switch or host in the network. Refer to Services for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Services"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/vlan": {
      "get": {
        "tags": [
          "vlan"
        ],
        "summary": "Get all VLAN information for all network devices",
        "description": "Retrieves VLAN information, such as hostname, interface name, associated VLANs, ports, and time of last change, for all switches and hosts in the network. Refer to Vlan model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Vlan"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    },
    "/object/vlan/hostname/{hostname}": {
      "get": {
        "tags": [
          "vlan"
        ],
        "summary": "Get all VLAN information for a given network device by hostname",
        "description": "Retrieves VLAN information, such as hostname, interface name, associated VLANs, ports, and time of last change, for a given switch or  host in the network. Refer to Vlan model for all data collected.",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "hostname",
            "in": "path",
            "description": "User-specified name for a network switch or host. For example, leaf01, spine04, host-6, engr-1, tor-22.",
            "required": true,
            "type": "string"
          },
          {
            "name": "eq_timestamp",
            "in": "query",
            "description": "Display results for a given time. Time must be entered in Epoch format. For example, to display the results for Monday February 13, 2019 at 1:25 pm, use a time converter and enter 1550082300.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "count",
            "in": "query",
            "description": "Number of entries to display starting from the offset value. For example, a count of 100 displays 100 entries at a time.",
            "required": false,
            "type": "integer"
          },
          {
            "name": "offset",
            "in": "query",
            "description": "Used in combination with count, offset specifies the starting location within the set of entries returned. For example, an offset of 100 would display results beginning with entry 101.",
            "required": false,
            "type": "integer"
          }
        ],
        "responses": {
          "200": {
            "description": "successful operation",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Vlan"
              }
            }
          }
        },
        "security": [
          {
            "jwt": []
          }
        ]
      }
    }
  },
  "securityDefinitions": {
    "jwt": {
      "type": "apiKey",
      "name": "Authorization",
      "in": "header"
    }
  },
  "definitions": {
    "Address": {
      "description": "This model contains descriptions of the data collected and returned by the Address endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "ifname": {
          "type": "string",
          "description": "Name of a software (versus physical) interface"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "prefix": {
          "type": "string",
          "description": "Address prefix for IPv4, IPv6, or EVPN traffic"
        },
        "mask": {
          "type": "integer",
          "format": "int32",
          "description": "Address mask for IPv4, IPv6, or EVPN traffic"
        },
        "is_ipv6": {
          "type": "boolean",
          "description": "Indicates whether address is an IPv6 address (true) or not (false)"
        },
        "vrf": {
          "type": "string",
          "description": "Virtual Route Forwarding interface name"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "BgpSession": {
      "description": "This model contains descriptions of the data collected and returned by the BGP endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "peer_name": {
          "type": "string",
          "description": "Interface name or hostname for a peer device"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "state": {
          "type": "string",
          "description": "Current state of the BGP session. Values include established and not established."
        },
        "peer_router_id": {
          "type": "string",
          "description": "If peer is a router, IP address of router"
        },
        "peer_asn": {
          "type": "integer",
          "format": "int64",
          "description": "Peer autonomous system number (ASN), identifier for a collection of IP networks and routers"
        },
        "peer_hostname": {
          "type": "string",
          "description": "User-defined name for the peer device"
        },
        "asn": {
          "type": "integer",
          "format": "int64",
          "description": "Host autonomous system number (ASN), identifier for a collection of IP networks and routers"
        },
        "reason": {
          "type": "string",
          "description": "Text describing the cause of, or trigger for, an event"
        },
        "ipv4_pfx_rcvd": {
          "type": "integer",
          "format": "int32",
          "description": "Address prefix received for an IPv4 address"
        },
        "ipv6_pfx_rcvd": {
          "type": "integer",
          "format": "int32",
          "description": "Address prefix received for an IPv6 address"
        },
        "evpn_pfx_rcvd": {
          "type": "integer",
          "format": "int32",
          "description": "Address prefix received for an EVPN address"
        },
        "last_reset_time": {
          "type": "number",
          "format": "float",
          "description": "Date and time at which the session was last established or reset"
        },
        "up_time": {
          "type": "number",
          "format": "float",
          "description": "Number of seconds the session has been established, in EPOCH notation"
        },
        "conn_estd": {
          "type": "integer",
          "format": "int32",
          "description": "Number of connections established for a given session"
        },
        "conn_dropped": {
          "type": "integer",
          "format": "int32",
          "description": "Number of dropped connections for a given session"
        },
        "upd8_rx": {
          "type": "integer",
          "format": "int32",
          "description": "Count of protocol messages received"
        },
        "upd8_tx": {
          "type": "integer",
          "format": "int32",
          "description": "Count of protocol messages transmitted"
        },
        "vrfid": {
          "type": "integer",
          "format": "int32",
          "description": "Integer identifier of the VRF interface when used"
        },
        "vrf": {
          "type": "string",
          "description": "Name of the Virtual Route Forwarding interface"
        },
        "tx_families": {
          "type": "string",
          "description": "Address families supported for the transmit session channel. Values include ipv4, ipv6, and evpn."
        },
        "rx_families": {
          "type": "string",
          "description": "Address families supported for the receive session channel. Values include ipv4, ipv6, and evpn."
        }
      }
    },
    "ClagSessionInfo": {
      "description": "This model contains descriptions of the data collected and returned by the CLAG endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "clag_sysmac": {
          "type": "string",
          "description": "Unique MAC address for each bond interface pair. This must be a value between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff."
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time the CLAG session was started, deleted, updated, or marked dead (device went down)"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "peer_role": {
          "type": "string",
          "description": "Role of the peer device. Values include primary and secondary."
        },
        "peer_state": {
          "type": "boolean",
          "description": "Indicates if peer device is up (true) or down (false)"
        },
        "peer_if": {
          "type": "string",
          "description": "Name of the peer interface used for the session"
        },
        "backup_ip_active": {
          "type": "boolean",
          "description": "Indicates whether the backup IP address has been specified and is active (true) or not (false)"
        },
        "backup_ip": {
          "type": "string",
          "description": "IP address of the interface to use if the peerlink (or bond) goes down"
        },
        "single_bonds": {
          "type": "string",
          "description": "Identifies a set of interfaces connecting to only one of the two switches in the bond"
        },
        "dual_bonds": {
          "type": "string",
          "description": "Identifies a set of interfaces connecting to both switches in the bond"
        },
        "conflicted_bonds": {
          "type": "string",
          "description": "Identifies the set of interfaces in a bond that do not match on each end of the bond"
        },
        "proto_down_bonds": {
          "type": "string",
          "description": "Interface on the switch brought down by the clagd service. Value is blank if no interfaces are down due to the clagd service."
        },
        "vxlan_anycast": {
          "type": "string",
          "description": "Anycast IP address used for VXLAN termination"
        },
        "role": {
          "type": "string",
          "description": "Role of the host device. Values include primary and secondary."
        }
      }
    },
    "ErrorResponse": {
      "description": "Standard error response",
      "type": "object",
      "properties": {
        "message": {
          "type": "string",
          "description": "One or more errors have been encountered during the processing of the associated request"
        }
      }
    },
    "Evpn": {
      "description": "This model contains descriptions of the data collected and returned by the EVPN endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "vni": {
          "type": "integer",
          "format": "int32",
          "description": "Name of the virtual network instance (VNI) where session is running"
        },
        "origin_ip": {
          "type": "string",
          "description": "Host device's local VXLAN tunnel IP address for the EVPN instance"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time the session was started, deleted, updated or marked as dead (device is down)"
        },
        "rd": {
          "type": "string",
          "description": "Route distinguisher used in the filtering mechanism for BGP route exchange"
        },
        "export_rt": {
          "type": "string",
          "description": "IP address and port of the export route target used in the filtering mechanism for BGP route exchange"
        },
        "import_rt": {
          "type": "string",
          "description": "IP address and port of the import route target used in the filtering mechanism for BGP route exchange"
        },
        "in_kernel": {
          "type": "boolean",
          "description": "Indicates whether the associated VNI is in the kernel (in kernel) or not (not in kernel)"
        },
        "adv_all_vni": {
          "type": "boolean",
          "description": "Indicates whether the VNI state is advertising all VNIs (true) or not (false)"
        },
        "adv_gw_ip": {
          "type": "string",
          "description": "Indicates whether the host device is advertising the gateway IP address (true) or not (false)"
        },
        "is_l3": {
          "type": "boolean",
          "description": "Indicates whether the session is part of a layer 3 configuration (true) or not (false)"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "Field": {
      "type": "object",
      "required": [
        "aliases",
        "defaultValue",
        "doc",
        "jsonProps",
        "name",
        "objectProps",
        "order",
        "props",
        "schema"
      ],
      "properties": {
        "props": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "name": {
          "type": "string"
        },
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "doc": {
          "type": "string"
        },
        "defaultValue": {
          "$ref": "#/definitions/JsonNode"
        },
        "order": {
          "type": "string",
          "enum": [
            "ASCENDING",
            "DESCENDING",
            "IGNORE"
          ]
        },
        "aliases": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "type": "string"
          }
        },
        "jsonProps": {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/JsonNode"
          }
        },
        "objectProps": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "properties": {}
          }
        }
      }
    },
    "Interface": {
      "description": "This model contains descriptions of the data collected and returned by the Interface endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "type": {
          "type": "string",
          "description": "Identifier of the kind of interface. Values include bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, and vxlan."
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time the data was collected"
        },
        "last_changed": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time the interface was started, deleted, updated or marked as dead (device is down)"
        },
        "ifname": {
          "type": "string",
          "description": "Name of the interface"
        },
        "state": {
          "type": "string",
          "description": "Indicates whether the interface is up or down"
        },
        "vrf": {
          "type": "string",
          "description": "Name of the virtual route forwarding (VRF) interface, if present"
        },
        "details": {
          "type": "string",
          "description": ""
        }
      }
    },
    "InventoryModel": {
      "type": "object",
      "required": [
        "label",
        "value"
      ],
      "properties": {
        "label": {
          "type": "string"
        },
        "value": {
          "type": "integer",
          "format": "int32"
        }
      }
    },
    "InventoryOutput": {
      "type": "object",
      "properties": {
        "data": {
          "$ref": "#/definitions/InventorySampleClass"
        }
      }
    },
    "InventorySampleClass": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer",
          "format": "int32",
          "example": 100,
          "description": "total number of devices"
        },
        "os_version": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "os_vendor": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "asic": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "asic_vendor": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "asic_model": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "cl_license": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "agent_version": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "agent_state": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "platform": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "platform_vendor": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "disk_size": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "memory_size": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "platform_model": {
          "$ref": "#/definitions/InventorySuperModel"
        },
        "interface_speeds": {
          "$ref": "#/definitions/InventorySuperModel"
        }
      }
    },
    "InventorySuperModel": {
      "type": "object",
      "required": [
        "data",
        "label"
      ],
      "properties": {
        "label": {
          "type": "string"
        },
        "data": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/InventoryModel"
          }
        }
      }
    },
    "IteratorEntryStringJsonNode": {
      "type": "object"
    },
    "IteratorJsonNode": {
      "type": "object"
    },
    "IteratorString": {
      "type": "object"
    },
    "JsonNode": {
      "type": "object",
      "required": [
        "array",
        "bigDecimal",
        "bigInteger",
        "bigIntegerValue",
        "binary",
        "binaryValue",
        "boolean",
        "booleanValue",
        "containerNode",
        "decimalValue",
        "double",
        "doubleValue",
        "elements",
        "fieldNames",
        "fields",
        "floatingPointNumber",
        "int",
        "intValue",
        "integralNumber",
        "long",
        "longValue",
        "missingNode",
        "null",
        "number",
        "numberType",
        "numberValue",
        "object",
        "pojo",
        "textValue",
        "textual",
        "valueAsBoolean",
        "valueAsDouble",
        "valueAsInt",
        "valueAsLong",
        "valueAsText",
        "valueNode"
      ],
      "properties": {
        "elements": {
          "$ref": "#/definitions/IteratorJsonNode"
        },
        "fieldNames": {
          "$ref": "#/definitions/IteratorString"
        },
        "binary": {
          "type": "boolean"
        },
        "intValue": {
          "type": "integer",
          "format": "int32"
        },
        "object": {
          "type": "boolean"
        },
        "int": {
          "type": "boolean"
        },
        "long": {
          "type": "boolean"
        },
        "double": {
          "type": "boolean"
        },
        "bigDecimal": {
          "type": "boolean"
        },
        "bigInteger": {
          "type": "boolean"
        },
        "textual": {
          "type": "boolean"
        },
        "boolean": {
          "type": "boolean"
        },
        "valueNode": {
          "type": "boolean"
        },
        "containerNode": {
          "type": "boolean"
        },
        "missingNode": {
          "type": "boolean"
        },
        "pojo": {
          "type": "boolean"
        },
        "number": {
          "type": "boolean"
        },
        "integralNumber": {
          "type": "boolean"
        },
        "floatingPointNumber": {
          "type": "boolean"
        },
        "numberValue": {
          "$ref": "#/definitions/Number"
        },
        "numberType": {
          "type": "string",
          "enum": [
            "INT",
            "LONG",
            "BIG_INTEGER",
            "FLOAT",
            "DOUBLE",
            "BIG_DECIMAL"
          ]
        },
        "longValue": {
          "type": "integer",
          "format": "int64"
        },
        "bigIntegerValue": {
          "type": "integer"
        },
        "doubleValue": {
          "type": "number",
          "format": "double"
        },
        "decimalValue": {
          "type": "number"
        },
        "booleanValue": {
          "type": "boolean"
        },
        "binaryValue": {
          "type": "array",
          "items": {
            "type": "string",
            "format": "byte",
            "pattern": "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$"
          }
        },
        "valueAsInt": {
          "type": "integer",
          "format": "int32"
        },
        "valueAsLong": {
          "type": "integer",
          "format": "int64"
        },
        "valueAsDouble": {
          "type": "number",
          "format": "double"
        },
        "valueAsBoolean": {
          "type": "boolean"
        },
        "textValue": {
          "type": "string"
        },
        "valueAsText": {
          "type": "string"
        },
        "array": {
          "type": "boolean"
        },
        "fields": {
          "$ref": "#/definitions/IteratorEntryStringJsonNode"
        },
        "null": {
          "type": "boolean"
        }
      }
    },
    "LLDP": {
      "description": "This model contains descriptions of the data collected and returned by the LLDP endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for the host device"
        },
        "ifname": {
          "type": "string",
          "description": "Name of the host interface where the LLDP service is running"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time that the session was started, deleted, updated, or marked dead (device is down)"
        },
        "peer_hostname": {
          "type": "string",
          "description": "User-defined name for the peer device"
        },
        "peer_ifname": {
          "type": "string",
          "description": "Name of the peer interface where the session is running"
        },
        "lldp_peer_bridge": {
          "type": "boolean",
          "description": "Indicates whether the peer device is a bridge (true) or not (false)"
        },
        "lldp_peer_router": {
          "type": "boolean",
          "description": "Indicates whether the peer device is a router (true) or not (false)"
        },
        "lldp_peer_station": {
          "type": "boolean",
          "description": "Indicates whether the peer device is a station (true) or not (false)"
        },
        "lldp_peer_os": {
          "type": "string",
          "description": "Operating system (OS) used by peer device. Values include Cumulus Linux, RedHat, Ubuntu, and CentOS."
        },
        "lldp_peer_osv": {
          "type": "string",
          "description": "Version of the OS used by peer device. Example values include 3.7.3, 2.5.x, 16.04, 7.1."
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "LogicalType": {
      "type": "object",
      "required": [
        "name"
      ],
      "properties": {
        "name": {
          "type": "string"
        }
      }
    },
    "LoginRequest": {
      "description": "User-entered credentials used to validate if user is allowed to access NetQ",
      "type": "object",
      "required": [
        "password",
        "username"
      ],
      "properties": {
        "username": {
          "type": "string"
        },
        "password": {
          "type": "string"
        }
      }
    },
    "LoginResponse": {
      "description": "Response to user login request",
      "type": "object",
      "required": [
        "id"
      ],
      "properties": {
        "terms_of_use_accepted": {
          "type": "boolean",
          "description": "Indicates whether user has accepted the terms of use"
        },
        "access_token": {
          "type": "string",
          "description": "Grants jason web token (jwt) access token. The access token also contains the NetQ Platform or Appliance (opid) which the user is permitted to access. By default, it is the primary opid given by the user."
        },
        "expires_at": {
          "type": "integer",
          "format": "int64",
          "description": "Number of hours the access token is valid before it automatically expires, epoch miliseconds. By default, tokens are valid for 24 hours."
        },
        "id": {
          "type": "string"
        },
        "premises": {
          "type": "array",
          "description": "List of premises that this user is authorized to view",
          "items": {
            "$ref": "#/definitions/Premises"
          }
        },
        "customer_id": {
          "type": "integer",
          "format": "int32",
          "description": "customer id of this user"
        }
      }
    },
    "MacFdb": {
      "description": "This model contains descriptions of the data collected and returned by the MacFdb endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "mac_address": {
          "type": "string",
          "description": "Media access control address for a device reachable via the local bridge member port 'nexthop' or via remote VTEP with IP address of 'dst'"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "dst": {
          "type": "string",
          "description": "IP address of a remote VTEP from which this MAC address is reachable"
        },
        "nexthop": {
          "type": "string",
          "description": "Interface where the MAC address can be reached"
        },
        "is_remote": {
          "type": "boolean",
          "description": "Indicates if the MAC address is reachable locally on 'nexthop' (false) or remotely via a VTEP with address 'dst' (true)"
        },
        "port": {
          "type": "string",
          "description": "Currently unused"
        },
        "vlan": {
          "type": "integer",
          "format": "int32",
          "description": "Name of associated VLAN"
        },
        "is_static": {
          "type": "boolean",
          "description": "Indicates if the MAC address is a static address (true) or dynamic address (false)"
        },
        "origin": {
          "type": "boolean",
          "description": "Indicates whether the MAC address is one of the host's interface addresses (true) or not (false)"
        },
        "active": {
          "type": "boolean",
          "description": "Currently unused"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "MstpInfo": {
      "description": "This model contains descriptions of the data collected and returned by the MSTP endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "bridge_name": {
          "type": "string",
          "description": "User-defined name for a bridge"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "state": {
          "type": "boolean",
          "description": "Indicates whether MSTP is enabled (true) or not (false)"
        },
        "root_port_name": {
          "type": "string",
          "description": "Name of the physical interface (port) that provides the minimum cost path from the Bridge to the MSTI Regional Root"
        },
        "root_bridge": {
          "type": "string",
          "description": "Name of the CIST root for the bridged LAN"
        },
        "topo_chg_ports": {
          "type": "string",
          "description": "Names of ports that were part of the last topology change event"
        },
        "time_since_tcn": {
          "type": "integer",
          "format": "int64",
          "description": "Amount of time, in seconds, since the last topology change notification"
        },
        "topo_chg_cntr": {
          "type": "integer",
          "format": "int64",
          "description": "Number of times topology change notifications have been sent"
        },
        "bridge_id": {
          "type": "string",
          "description": "Spanning Tree bridge identifier for current host"
        },
        "edge_ports": {
          "type": "string",
          "description": "List of port names that are Spanning Tree edge ports"
        },
        "network_ports": {
          "type": "string",
          "description": "List of port names that are Spanning Tree network ports"
        },
        "disputed_ports": {
          "type": "string",
          "description": "List of port names that are in Spanning Tree dispute state"
        },
        "bpduguard_ports": {
          "type": "string",
          "description": "List of port names where BPDU Guard is enabled"
        },
        "bpduguard_err_ports": {
          "type": "string",
          "description": "List of port names where BPDU Guard violation occurred"
        },
        "ba_inconsistent_ports": {
          "type": "string",
          "description": "List of port names where Spanning Tree Bridge Assurance is failing"
        },
        "bpdufilter_ports": {
          "type": "string",
          "description": "List of port names where Spanning Tree BPDU Filter is enabled"
        },
        "ports": {
          "type": "string",
          "description": "List of port names in the Spanning Tree instance"
        },
        "is_vlan_filtering": {
          "type": "boolean",
          "description": "Indicates whether the bridge is enabled with VLAN filtering (is VLAN-aware) (true) or not (false)"
        }
      }
    },
    "Neighbor": {
      "description": "This model contains descriptions of the data collected and returned by the Neighbor endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name of a device"
        },
        "ifname": {
          "type": "string",
          "description": "User-defined name of an software interface on a device"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time when data was collected"
        },
        "vrf": {
          "type": "string",
          "description": "Name of virtual route forwarding (VRF) interface, when applicable"
        },
        "is_remote": {
          "type": "boolean",
          "description": "Indicates if the neighbor is reachable through a local interface (false) or remotely (true)"
        },
        "ifindex": {
          "type": "integer",
          "format": "int32",
          "description": "IP address index for the neighbor device"
        },
        "mac_address": {
          "type": "string",
          "description": "MAC address for the neighbor device"
        },
        "is_ipv6": {
          "type": "boolean",
          "description": "Indicates whether the neighbor's IP address is version six (IPv6) (true) or version four (IPv4) (false)"
        },
        "message_type": {
          "type": "string",
          "description": "Network protocol or service identifier used in neighbor-related events. Value is neighbor."
        },
        "ip_address": {
          "type": "string",
          "description": "IPv4 or IPv6 address for the neighbor device"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "NODE": {
      "description": "This model contains descriptions of the data collected and returned by the Node endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name of the device"
        },
        "sys_uptime": {
          "type": "integer",
          "format": "int64",
          "description": "Amount of time this device has been powered up"
        },
        "lastboot": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time this device was last booted"
        },
        "last_reinit": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time this device was last initialized"
        },
        "active": {
          "type": "boolean",
          "description": "Indicates whether this device is active (true) or not (false)"
        },
        "version": {
          "type": "string",
          "description": ""
        },
        "ntp_state": {
          "type": "string",
          "description": "Status of the NTP service running on this device; in sync, not in sync, or unknown"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "last_update_time": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time the device was last updated"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "NTP": {
      "description": "This model contains descriptions of the data collected and returned by the NTP endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name of device running NTP service"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "ntp_sync": {
          "type": "string",
          "description": "Status of the NTP service running on this device; in sync, not in sync, or unknown"
        },
        "stratum": {
          "type": "integer",
          "format": "int32",
          "description": ""
        },
        "ntp_app": {
          "type": "string",
          "description": "Name of the NTP service
        },
        "message_type": {
          "type": "string",
          "description": "Network protocol or service identifier used in NTP-related events. Value is ntp."
        },
        "current_server": {
          "type": "string",
          "description": "Name or address of server providing time synchronization"
        },
        "active": {
          "type": "boolean",
          "description": "Indicates whether NTP service is running (true) or not (false)"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "Number": {
      "type": "object",
      "description": " "
    },
    "Port": {
      "description": "This model contains descriptions of the data collected and returned by the Port endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for the device with this port"
        },
        "ifname": {
          "type": "string",
          "description": "User-defined name for the software interface on this port"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "speed": {
          "type": "string",
          "description": "Maximum rating for port. Examples include 10G, 25G, 40G, unknown."
        },
        "identifier": {
          "type": "string",
          "description": "Identifies type of port module if installed. Example values include empty, QSFP+, SFP, RJ45"
        },
        "autoneg": {
          "type": "string",
          "description": "Indicates status of the auto-negotiation feature. Values include on and off."
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "transreceiver": {
          "type": "string",
          "description": "Name of installed transceiver. Example values include 40G Base-CR4, 10Gtek."
        },
        "connector": {
          "type": "string",
          "description": "Name of installed connector. Example values include LC, copper pigtail, RJ-45, n/a."
        },
        "vendor_name": {
          "type": "string",
          "description": "Name of the port vendor. Example values include OEM, Mellanox, Amphenol, Finisar, Fiberstore, n/a."
        },
        "part_number": {
          "type": "string",
          "description": "Manufacturer part number"
        },
        "serial_number": {
          "type": "string",
          "description": "Manufacturer serial number"
        },
        "length": {
          "type": "string",
          "description": "Length of cable connected. Example values include 1m, 2m, n/a."
        },
        "supported_fec": {
          "type": "string",
          "description": "List of forward error correction (FEC) algorithms supported on this port. Example values include BaseR, RS, Not reported, None."
        },
        "advertised_fec": {
          "type": "string",
          "description": "Type of FEC advertised by this port"
        },
        "fec": {
          "type": "string",
          "description": "Forward error correction"
        },
        "message_type": {
          "type": "string",
          "description": "Network protocol or service identifier used in port-related events. Value is port."
        },
        "state": {
          "type": "string",
          "description": "Status of the port, either up or down."
        }
      }
    },
    "Premises": {
      "type": "object",
      "required": [
        "name",
        "opid"
      ],
      "properties": {
        "opid": {
          "type": "integer",
          "format": "int32"
        },
        "name": {
          "type": "string"
        }
      },
      "description": "Premises"
    },
    "Route": {
      "description": "This module contains descirptions of the data collected and returned by the Route endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "vrf": {
          "type": "string",
          "description": "Name of associated virtual route forwarding (VRF) interface, if applicable"
        },
        "message_type": {
          "type": "string",
          "description": "Network protocol or service identifier used in route-related events. Value is route."
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "is_ipv6": {
          "type": "boolean",
          "description": "Indicates whether the IP address for this route is an IPv6 address (true) or an IPv4 address (false)"
        },
        "rt_table_id": {
          "type": "integer",
          "format": "int32",
          "description": "Routing table identifier for this route"
        },
        "src": {
          "type": "string",
          "description": "Hostname of device where this route originated"
        },
        "nexthops": {
          "type": "string",
          "description": "List of hops remaining to reach destination"
        },
        "route_type": {
          "type": "integer",
          "format": "int32",
          "description": ""
        },
        "origin": {
          "type": "boolean",
          "description": "Indicates whether the source of this route is on the  device indicated by 'hostname'"
        },
        "protocol": {
          "type": "string",
          "description": "Protocol used for routing. Example values include BGP, OSPF."
        },
        "prefix": {
          "type": "string",
          "description": "Address prefix for this route"
        }
      }
    },
    "Schema": {
      "type": "object",
      "required": [
        "aliases",
        "doc",
        "elementType",
        "enumSymbols",
        "error",
        "fields",
        "fixedSize",
        "fullName",
        "hashCode",
        "jsonProps",
        "logicalType",
        "name",
        "namespace",
        "objectProps",
        "props",
        "type",
        "types",
        "valueType"
      ],
      "properties": {
        "props": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "type": {
          "type": "string",
          "enum": [
            "RECORD",
            "ENUM",
            "ARRAY",
            "MAP",
            "UNION",
            "FIXED",
            "STRING",
            "BYTES",
            "INT",
            "LONG",
            "FLOAT",
            "DOUBLE",
            "BOOLEAN",
            "NULL"
          ]
        },
        "logicalType": {
          "$ref": "#/definitions/LogicalType"
        },
        "hashCode": {
          "type": "integer",
          "format": "int32"
        },
        "elementType": {
          "$ref": "#/definitions/Schema"
        },
        "aliases": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "type": "string"
          }
        },
        "namespace": {
          "type": "string"
        },
        "fields": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Field"
          }
        },
        "types": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/Schema"
          }
        },
        "fullName": {
          "type": "string"
        },
        "enumSymbols": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "doc": {
          "type": "string"
        },
        "valueType": {
          "$ref": "#/definitions/Schema"
        },
        "fixedSize": {
          "type": "integer",
          "format": "int32"
        },
        "name": {
          "type": "string"
        },
        "error": {
          "type": "boolean"
        },
        "jsonProps": {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/definitions/JsonNode"
          }
        },
        "objectProps": {
          "type": "object",
          "additionalProperties": {
            "type": "object",
            "properties": {}
          }
        }
      }
    },
    "Sensor": {
      "description": "This model contains descriptions of the data collected and returned from the Sensor endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name of the device where the sensor resides"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "s_prev_state": {
          "type": "string",
          "description": "Previous state of a fan or power supply unit (PSU) sensor. Values include OK, absent, and bad."
        },
        "s_name": {
          "type": "string",
          "description": "Type of sensor. Values include fan, psu, temp."
        },
        "s_state": {
          "type": "string",
          "description": "Current state of a fan or power supply unit (PSU) sensor. Values include OK, absent, and bad."
        },
        "s_input": {
          "type": "number",
          "format": "float",
          "description": "Sensor input"
        },
        "message_type": {
          "type": "string",
          "description": "Network protocol or service identifier used in sensor-related events. Value is sensor."
        },
        "s_msg": {
          "type": "string",
          "description": "Sensor message"
        },
        "s_desc": {
          "type": "string",
          "description": "User-defined name of sensor. Example values include fan1, fan-2, psu1, psu02, psu1temp1, temp2."
        },
        "s_max": {
          "type": "integer",
          "format": "int32",
          "description": "Current maximum temperature threshold value"
        },
        "s_min": {
          "type": "integer",
          "format": "int32",
          "description": "Current minimum temperature threshold value"
        },
        "s_crit": {
          "type": "integer",
          "format": "int32",
          "description": "Current critical high temperature threshold value"
        },
        "s_lcrit": {
          "type": "integer",
          "format": "int32",
          "description": "Current critical low temperature threshold value"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "active": {
          "type": "boolean",
          "description": "Indicates whether the identified sensor is operating (true) or not (false)"
        },
        "deleted": {
          "type": "boolean",
          "description": "Indicates whether the sensor has been deleted (true) or not (false)"
        }
      }
    },
    "Services": {
      "description": "This model contains descriptions of the data collected and returned from the Sensor endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name of the device where the network services are running."
        },
        "name": {
          "type": "string",
          "description": "Name of the service; for example, BGP, OSPF, LLDP, NTP, and so forth."
        },
        "vrf": {
          "type": "string",
          "description": "Name of the Virtual Route Forwarding (VRF) interface if employed."
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "is_enabled": {
          "type": "boolean",
          "description": "Indicates whether the network service is enabled."
        },
        "is_active": {
          "type": "boolean",
          "description": "Indicates whether the network service is currently active."
        },
        "is_monitored": {
          "type": "boolean",
          "description": "Indicates whether the network service is currently being monitored."
        },
        "status": {
          "type": "integer",
          "format": "int32",
          "description": "Status of the network service connection; up or down."
        },
        "start_time": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time that the network service was most recently started."
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        }
      }
    },
    "Vlan": {
      "description": "This model contains descriptions of the data collected and returned by the VLAN endpoint.",
      "type": "object",
      "required": [
        "schema"
      ],
      "properties": {
        "schema": {
          "$ref": "#/definitions/Schema"
        },
        "opid": {
          "type": "integer",
          "format": "int32",
          "description": "Internal use only"
        },
        "hostname": {
          "type": "string",
          "description": "User-defined name for a device"
        },
        "ifname": {
          "type": "string",
          "description": "User-defined name for a software interface"
        },
        "timestamp": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time data was collected"
        },
        "last_changed": {
          "type": "integer",
          "format": "int64",
          "description": "Date and time the VLAN configuration was changed (updated, deleted)"
        },
        "vlans": {
          "type": "string",
          "description": "List of other VLANs known to this VLAN or on this device"
        },
        "svi": {
          "type": "string",
          "description": "Switch virtual interface (SVI) associated with this VLAN"
        },
        "db_state": {
          "type": "string",
          "description": "Internal use only"
        },
        "ports": {
          "type": "string",
          "description": "Names of ports on the device associated with this VLAN"
        }
      }
    }
  }
}

```

{{< /expand >}}
