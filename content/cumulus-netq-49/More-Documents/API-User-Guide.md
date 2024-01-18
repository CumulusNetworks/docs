---
title: Integrate NetQ API with Your Applications
author: NVIDIA
weight: 1130
toc: 3
---
The NetQ API provides data about the performance and operation of your network and its devices. You can view the data with your internal tools or with third-party analytic tools. The API displays the health of individual switches, network protocols and services, trace and validation results, as well as networkwide inventory and events.

This guide provides an overview of the NetQ API framework, including the basics of using Swagger UI 2.0 or `bash` plus `curl` to view and test the APIs. Descriptions of each endpoint and model parameter are in individual API JSON files.

## API Organization

The NetQ API provides endpoints for:

- **Network protocols**: BGP, EVPN, LLDP, CLAG, MSTP, Neighbors, NTP, Routes
- **Virtual networks**: VLAN
- **Services**: Services
- **Interfaces**: Interface, Port
- **Trace and validation**: Trace, Check
- **Inventory and Devices**: Address, Inventory, MAC Address tables, Node, Sensors
- **Events**: Events

Each endpoint has its own API. You can make requests for all data and all devices or you can filter the request by a given hostname. Each API returns a predetermined set of data as defined in the API models.

{{%notice info%}}

The Swagger interface displays both public and internal APIs. Public APIs do not have *internal* in their name. Internal APIs are not supported for public use and subject to change without notice.

{{%/notice%}}

## Get Started

You can access the API gateway and execute requests from the Swagger UI or a terminal interface. If you are using a terminal window, proceed to the next section.

{{<tabs "Access API Gateway">}}

{{<tab "Swagger UI">}}

1. Open the Swagger interface by entering one of the following in your browser's address bar:

    - Cloud deployments:  https://api.netq.nvidia.com/swagger/
    - On-premises deployments: https://\<hostname-or-ipaddr\>/swagger/
    - NVIDIA Air: https://api.air.netq.nvidia.com/swagger/

2. Select *auth* from the **Select a definition** dropdown at the top right of the window. This opens the authorization API.

    {{<figure src="/images/netq/api-swagger-onopen-320.png" alt="" width="700">}}

{{</tab>}}

{{</tabs>}}

### Log In

Although you can view the API endpoints without authorization, you can only execute the API endpoints if you have been authorized.

{{<tabs "Log In">}}

{{<tab "Swagger UI">}}

You must first obtain an access key and then use that key to authorize your access to the API.

1. Click **POST/login**.

    {{<figure src="/images/netq/api-swagger-login-selection-320.png" width="700">}}

2. Click **Try it out**.

    {{<figure src="/images/netq/api-swagger-login-tryitout-320.png" width="700">}}

3. Enter the username and password you used to install NetQ. For this release, the default is username *admin* and password *admin*. Do not change the `access-key` value.

    {{<figure src="/images/netq/api-swagger-login-execute-320.png" width="700">}}

4. Click **Execute**.

5. Scroll down to view the **Responses**. In the **Server response** section, in the Response body of the **200** code response, copy the access token in the top line.

    {{<figure src="/images/netq/api-swagger-login-access-token-320.png" width="700">}}

6. Click **Authorize**.

    {{<figure src="/images/netq/api-swagger-login-authorize-320.png" width="450">}}

7. Paste the access key into the **Value** field, and click **Authorize**.

8. Click **Close**.

{{</tab>}}

{{<tab "Terminal Window">}}

To log in and obtain authorization:

1. Open a terminal window.

2. Log in to obtain the access token. You will need the following information:
    - Hostname or IP address, and port (443 for cloud deployments, 32708 for on-premises deployments) of your API gateway
    - Your login credentials that were provided as part of the NetQ installation process. For this release, the default is username *admin* and password *admin*.

    This example uses an IP address of 192.168.0.10, port of 443, and the default credentials:

    ```
    <computer-name>:~ <username>$ curl -X POST "https://api.192.168.0.10.netq.nvidia.com:443/netq/auth/v1/login" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"username\": \"admin\", \"password\": \"admin\", \"access_key\": \"string\"}"
    ```

    The output provides the access token as the first parameter.

    ```
    {"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9....","customer_id":0,"expires_at":1597200346504,"id":"admin","is_cloud":true,"premises":[{"name":"OPID0","namespace":"NAN","opid":0},{"name":"ea-demo-dc-1","namespace":"ea1","opid":30000},{"name":"ea-demo-dc-2","namespace":"ea1","opid":30001},{"name":"ea-demo-dc-3","namespace":"ea1","opid":30002},{"name":"ea-demo-dc-4","namespace":"ea1","opid":30003},{"name":"ea-demo-dc-5","namespace":"ea1","opid":30004},{"name":"ea-demo-dc-6","namespace":"ea1","opid":30005},{"name":"ea-demo-dc-7","namespace":"ea1","opid":80006},{"name":"Cumulus Data Center","namespace":"NAN","opid":1568962206}],"reset_password":false,"terms_of_use_accepted":true}
    ```

3. Copy the access token to a text file. You will need this token to make API data requests.

{{</tab>}}

{{</tabs>}}

You are now able to create and execute API requests against the endpoints.

{{<notice tip>}}
By default, authorization is valid for 24 hours, after which users must sign in again and reauthorize their account.
{{</notice>}}

### API Requests

You can use either the Swagger UI or a terminal window with `bash` and `curl` commands to create and execute API requests.

{{<tabs "TabID133" >}}

{{<tab "Swagger UI" >}}

1. Select the endpoint from the definition dropdown at the top right of the application.

    This example shows the BGP endpoint selected:

    {{<figure src="/images/netq/api-swagger-bgp-endpoint-selection-320.png" width="500">}}

2. Select the endpoint object.

    This example shows the results of selecting the GET bgp object:

    {{<figure src="/images/netq/api-swagger-bgp-object-320.png" width="700">}}

<div style="padding-left: 18px">A description is provided for each object and the various parameters that can be specified. In the <strong>Responses</strong> section, you can see the data that is returned when the request is successful.</div>

3. Click **Try it out**.

4. Enter values for the required parameters.

5. Click **Execute**.

{{</tab>}}

{{<tab "Terminal Window">}}

In a terminal window, use `bash` plus `curl` to execute requests. Each request contains an API method (GET, POST, etc.), the address and API endpoint object to query, a variety of headers, and sometimes a body. For example, in the log in step above:

- API method = POST
- Address and API object = "https://\<netq.domain\>:443/netq/auth/v1/login"
- Headers = -H "accept: application/json" and -H "Content-Type: application/json"
- Body = -d "{ \"username\": \"admin\", \"password\": \"admin\", \"access_key\": \"string\"}"

{{</tab>}}

{{</tabs>}}

### API Responses

A NetQ API response comprises a status code, any relevant error codes (if unsuccessful), and the collected data (if successful).

The following HTTP status codes might be presented in the API responses:

| Code | Name | Description | Action |
| ---- | ---- | ----| ---- |
| 200 | Success | Request was successfully processed. | Review response. |
| 400  | Bad Request | Invalid input was detected in request. | Check the syntax of your request and make sure it matches the schema. |
| 401  | Unauthorized | Authentication has failed or credentials were not provided. | Provide or verify your credentials, or request access from your administrator. |
| 403  | Forbidden | Request was valid, but user might not have the needed permissions. | Verify your credentials or request an account from your administrator. |
| 404  | Not Found | Requested resource could not be found. | Try the request again after a period of time or verify status of resource. |
| 409  | Conflict | Request cannot be processed due to conflict in current state of the resource. | Verify status of resource and remove conflict. |
| 500  | Internal Server Error | Unexpected condition has occurred. | Perform general troubleshooting and try the request again. |
| 503  | Service Unavailable | The service being requested is currently unavailable. | Verify the status of the NetQ Platform or appliance, and the associated service. |

## Example Requests and Responses

Some command requests and their responses are shown here, but feel free to run your own requests. To run a request, you will need your authorization token. When using the `curl` commands, the responses have been piped through a python tool to make them more readable. You can choose to do so as well.

### Validate Networkwide Status of the BGP Service

Make your request to the *bgp* endpoint to obtain validate the operation of the BGP service on all nodes running the service.

{{<tabs "Validate BGP Service">}}

{{<tab "Swagger UI">}}

1. Open the check endpoint.

    {{<figure src="/images/netq/api-swagger-check-endpoint-selection-320.png" width="400">}}

2. Open the check object.

    {{<figure src="/images/netq/api-swagger-bgp-check-object-selection-320.png" width="700">}}

3. Click **Try it out**.

4. Enter values for `time`, `duration`, `by`, and `proto` parameters.

    In this example, time=1597256560, duration=24, by=scheduled, and proto=bgp.

5. Click **Execute**, then scroll down to see the results under **Server response**.

    {{<figure src="/images/netq/api-swagger-ex-bgp-200-response-320.png" width="700">}}

{{</tab>}}

{{<tab "Terminal Window">}}

Run the following `curl` command, entering values for the various parameters. In this example, *time=1597256560*, *duration=24* (hours), *by=scheduled*, and *proto=bgp*.

```
curl -X GET "<https://<netq.domain>:<port>/netq/telemetry/v1/object/check?time=1597256560&duration=24&by=scheduled&proto=bgp" -H "accept: application/json" -H  "Authorization: <auth-token> " | python -m json.tool
```

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 22869  100 22869    0     0  34235      0 --:--:-- --:--:-- --:--:-- 34183
{
    "count": 24,
    "data": [
        {
            "additional_summary": {
                "failed_sessions": 0,
                "total_sessions": 0
            },
            "failed_node_set": [],
            "jobid": "c5c046d1-3cc5-4c8b-b4e8-cf2bbfb050e6",
            "res_timestamp": 1597254743280,
            "rotten_node_set": [],
            "summary": {
                "checkedNodeCount": 0,
                "failedNodeCount": 0,
                "failedSessionCount": 0,
                "rottenNodeCount": 0,
                "totalNodeCount": 0,
                "totalSessionCount": 0,
                "warningNodeCount": 0
            },
...
```

{{</tab>}}

{{</tabs>}}

### Get Status of EVPN on a Specific Switch

Make your request to the *evpn/hostname* endpoint to view the status of all EVPN sessions running on that node.

{{<tabs "EVPN Status">}}

{{<tab "Swagger UI">}}

This example uses the *server01* switch.

1. Open the EVPN endpoint.

    {{<figure src="/images/netq/api-swagger-evpn-endpoint-selection-320.png" width="400">}}

2. Open the hostname object.

    {{<figure src="/images/netq/api-swagger-evpn-hostname-object-selection-320.png" width="700">}}

3. Click **Try it out**.

4. Enter a value for `hostname`, and optional values for `eq_timestamp`, `count`, and `offset` parameters.

    In this example, time=1597256560, duration=24, by=scheduled, and proto=bgp.

5. Click **Execute**, then scroll down to see the results under **Server response**.

    {{<figure src="/images/netq/api-swagger-ex-bgp-200-response-320.png" width="700">}}

{{</tab>}}

{{<tab "Terminal Window">}}

This example uses the *server01* switch in an on-premises network deployment.

```
curl -X GET "https://<netq.domain>:32708/netq/telemetry/v1/object/evpn/hostname/spine01" -H "accept: application/json" -H "Authorization: <auth-token>" | python -m json.tool
```

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100     2    0     2    0     0      3      0 --:--:-- --:--:-- --:--:--     3
[]


<!-- old output -->

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
```

{{</tab>}}

{{</tabs>}}

### Get Status on All Interfaces at a Given Time

Make your request to the *interfaces* endpoint to view the status of all interfaces. By specifying the *eq-timestamp* option and entering a date and time in epoch format, you indicate the data for that time (versus in the last hour by default), as follows:

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

<!-- vale off -->
### Get a List of All Devices Being Monitored
<!-- vale on -->

Make your request to the *inventory* endpoint to get a listing of all monitored nodes and their configuration information, as follows:

    curl -X GET "https://<netq.domain>:32708/netq/telemetry/v1/object/inventory" -H "Content-Type: application/json" -H "Authorization: <auth-token>" | python -m json.tool
     
    [
      {
        "hostname": "border01",
        "timestamp": 1556037425658,
        "asic_model": "A-Z",
        "agent_version": "3.2.0-cl4u30~1601403318.104fb9ed",
        "os_version": "A.2.0",
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
        "agent_version": "3.2.0-cl4u30~1601403318.104fb9ed",
        "os_version": "C.2.0",
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
