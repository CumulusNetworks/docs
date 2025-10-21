---
title: Integrate NetQ with Grafana
author: NVIDIA
weight: 550
toc: 3
---

The NetQ integration with Grafana allows you to create customized dashboards and to visualize metrics across your network devices. To view data in Grafana, first configure security between NetQ and OTel clients, configure OpenTelemetry (OTel) on the devices in your network, then configure the data sources in Grafana. <!--You can create your own dashboards from scratch or import a dashboard template to get started.-->

{{%notice note%}}
The Grafana integration is in beta and supported for on-premises deployments only.
{{%/notice%}}

## Requirements and Support

- Switches must have a Spectrum-2 or later ASIC. The number of supported switches varies based on the deployment model and reflects an environment where each switch is configured with OpenTelemetry and running the NetQ agent.
   - Standalone: 5 switches
   - Cluster: 50 switches
   - 3-node scale cluster: 500 switches
   - 5-node scale cluster: 1,000 switches
- For switches, you must enable OpenTelemetry to collect and export each metric that you want to monitor, as described in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/" text="Cumulus Linux documentation">}}.
   - NetQ does not support OpenTelemetry collection from switches with {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/#buffer-statistics" text="buffer statistics">}} enabled. 
- DPUs and ConnectX hosts must be running DOCA Telemetry Service (DTS) version 1.18-1.20.
- Before you get started with the steps below, {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/installation/" text="install Grafana">}} and {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/start-restart-grafana/" text="start the Grafana server">}}.
- NetQ allows you to retrieve data from up to seven days in the past.

## Secure OpenTelemetry Export

NetQ is configured with OTLP secure mode with TLS by default and expects clients to secure data with a certificate. You can configure NetQ and your client devices to use your own generated CA certificate, NetQ's self-signed certificate, or set the connections to insecure mode.

{{%notice note%}}
OpenTelemetry on host DPUs and NICs only supports insecure mode.
{{%/notice%}}

{{<tabs "certifcate options">}}

{{<tab "TLS with a CA Certificate">}}
### TLS with a CA Certificate

NVIDIA recommends using your own generated CA certificate. To configure a CA certificate:

1. Copy your certificate files to the NetQ server in the `/mnt/admin` directory. For example, copy the certificate and key to `/mnt/admin/certs/server.crt` and `/mnt/admin/certs/server.key` 

2. Import your certificate on your switches using the `nv action import system security ca-certificate <cert-id> [data <data> | uri <path>]` command. Define the name of the certificate in `<cert-id>` and either provide the raw PEM string of the certificate as `<data>` or provide a path to the certificate file containing the public key as `<path>`.

3. After importing your certificate, set OTLP insecure mode to `disabled` on your switches:

    ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   nvidia@switch:~$ nv config apply
   ```

{{</tab>}}

{{<tab "TLS with NetQ's Self-signed Certificate" >}}
### TLS with NetQ's Self-signed Certificate

To run on the switch in secure mode with NetQ's self-signed certificate:

1. From the NetQ server, display the certificate using `netq show otlp tls-ca-cert dump` command. Copy the certificate from the output.

2. On the switch, import the certificate with the `nv action import system security ca-certificate <cert-id> data <data>` command. Define the name of the certificate in `<cert-id>` and replace `<data>` with the certificate data you generated in the preceding step.

3. Configure the certificate to secure the OTel connection. Replace `ca-certificate` with the name of your certificate; this is the `<cert-id>` from the previous step.

   ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc cert-id <ca-certificate>
   nvidia@switch:~$ nv config apply
   ```

4. Next, disable `insecure` mode and apply the change:
    
    ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   nvidia@switch:~$ nv config apply
   ```
5. Run `nv show system telemetry health` to display the destination port and IP address, along with connectivity status.

{{</tab>}}

{{<tab "Insecure Mode" >}}
### Insecure Mode

To use insecure mode and disable TLS:

1. On your NetQ server, run the `netq set otlp security-mode insecure` command.

2. On your switches, configure insecure mode:

    ```
   nvidia@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   nvidia@switch:~$ nv config apply
   ```
{{</tab>}}

{{</tabs>}}
## Configure and Enable OpenTelemetry on Devices

Configure your client devices to send OpenTelemetry data to NetQ.

{{<tabs "TabID23" >}}

{{<tab "Cumulus Linux Switches">}}

Enable OpenTelemetry for each metric that you want to monitor, as described in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/" text="Cumulus Linux documentation">}}. Use your NetQ server or cluster’s IP address and port 30008 when configuring the OTLP export destination.

{{<notice info>}}
NVIDIA recommends setting the <code>sample-interval</code> option to 10 seconds for each metric that allows you to set a sample interval.
{{</notice>}}

{{</tab>}}

{{<tab "DPUs and NICs" >}}

1. {{<link title="Install NIC and DPU Agents" text="Install DOCA Telemetry Service (DTS)">}} on your ConnectX hosts or DPUs. 

2. Configure the DPU to send OpenTelemetry data by editing the `/opt/mellanox/doca/services/telemetry/config/dts_config.ini` file. Add the following line under the `IPC transport` section. Replace `TS-IP` with the IP address of your telemetry receiver. 

```
open-telemetry-receiver=http://<TS-IP>:30009/v1/metrics
```
{{%notice note%}}
It can take up to a minute for the device to restart and apply the changes.
{{%/notice%}}

Read more about OpenTelemetry and DTS configurations in the {{<exlink url="https://docs.nvidia.com/doca/archive/2-9-3/doca+telemetry+service+guide/index.html#src-3382565608_id-.DOCATelemetryServiceGuidev2.9.1-OpenTelemetryExporter" text="DOCA Telemetry Service guide">}}.

{{</tab>}}

{{</tabs>}}


## Configure an External TSDB

OpenTelemetry data is stored in the NetQ TSDB. In addition to NetQ's local storage, you can configure NetQ to also send the collected data to your own external TSDB:

1. If the connection to your external TSDB is secured with TLS, copy the certificate to the NetQ server in the `/mnt/admin/` directory, and reference the full path to the file with the `netq set otlp endpoint-ca-cert tsdb-name <text-tsdb-endpoint> ca-cert <text-path-to-ca-crt>` command.

2. From the NetQ server, add the OTel endpoint of your time-series database (TSDB). Replace `text-tsdb-endpoint` and `text-tsdb-endpoint-url` with the name and IP address of your TSDB, respectively. Include the `export true` option to begin exporting data immediately. Set `security-mode` to `tls` if you configured a certificate to secure the connection, otherwise use `security-mode insecure`.

```
nvidia@netq-server:~$ netq add otlp endpoint tsdb-name <text-tsdb-endpoint> tsdb-url <text-tsdb-endpoint-url> [export true | export false] [security-mode <text-mode>]
```

3. If you set the `export` option to `true` in the previous step, the TSDB will begin receiving the time-series data for the metrics that you configured on the switch. Use the `netq show otlp endpoint` command to view the TSDB endpoint configuration.


## Configure Data Sources in Grafana

1. Generate and copy an authentication token using the NetQ CLI. You can adjust time at which the token will expire with the `expiry` option. For example, the following command generates a token that expires after 40 days. If you do not set an `expiry` option, the token expires after 5 days. The maximum number of days allowed is 180.

```
nvidia@netq-server:~$ netq show vm-token expiry 40
```

2. Navigate to your Grafana dashboard. From the menu, select **Connections** and then **Data sources**. Select **Add new data source** and add the Prometheus TSDB:

{{<figure src="/images/netq/grafana-prom-415.png" alt="" width="1200">}}

3. Continue through the steps to configure the data source:

- In the *Name* field, enter the name of the data source. The name should be lowercase and begin with the data source name (for example, `slurm_dashboard`).
- In the *Connection* field, enter the IP address of your NetQ server followed by `/api/netq/vm/`, for example `https://10.255.255.255/api/netq/vm/`. In a cluster deployment, enter the virtual IP address in this field (followed by `/api/netq/vm/`). 
- In the *Authentication* section, select **Forward OAuth identity** from the dropdown menu. 
   - In *TLS settings*, select **Skip TLS certificate validation**.
   - In the *HTTP headers* section, select **Add header**. In the *Header* field, enter **Authorization**. In the *Value* field, enter the token that you generated in step one of this section.

{{<figure src="/images/netq/grafana-header-415.png" alt="" width="1000">}}

5. Select **Save & test**. If the operation was successful, you will begin to see metrics in your Grafana dashboard. 

<!--
## Import a Dashboard Template

To import a preconfigured dashboard into your Grafana instance, following the steps in the {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/import-dashboards/" text="Grafana documentation">}}. You can download the dashboard JSON files from the NetQ Grafana Dashboard Github repo.

-->

## Grafana Best Practices

If data retrieval with Grafana is slow, you might need to adjust your dashboard settings. Fabric-wide queries on large networks (over 1000 switches) can generate millions of data points, which can significantly degrade performance. You can improve performance by optimizing queries, reducing data volume, and simplifying panel rendering.

Avoid plotting all time-series data at once. To visualize the data in different ways:
   - {{<exlink url="https://grafana.com/docs/grafana/latest/fundamentals/timeseries/#aggregating-time-series" text="Aggregate time-series data">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/fundamentals/timeseries/#aggregating-time-series" text="Add labels to your time-series data">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Add interval variables">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Use aggregation operators">}} such as `count` and `topk`

{{<notice tip>}}
If Grafana displays "No Data", verify that all VMs in your cluster are operational. You can check the node status using the <code>kubectl get nodes</code> command. A node will show as <code>NotReady</code> if it is down. When the VM is restored, data collection will resume and will be displayed within 20 minutes of restoration.
{{</notice>}}

## Retrieve Metrics with the NetQ API

If you want to view or export the time-series database data without using Grafana, you can use curl commands to directly query the NetQ TSDB. These commands typically complete in fewer than 30 seconds, whereas Grafana can take longer to process and display data.

1. Generate an access token. Replace `<username>` and `<password>` with your NetQ username and password. Copy the access token generated by this command. You will use it in the next step. 
```
curl 'https://10.237.212.61/api/netq/auth/v1/login' -H 'content-type: application/json' --data-raw '{"username":"<username>","password":"<password>"}' --insecure 
```
 2. Generate a JSON Web Token (JWT). Replace `<access_token>` with the token generated from the previous step. Copy the resulting token generated by this command. You will use it in the next step. 
```
curl -k -X GET "https://10.237.212.61/api/netq/auth/v1/vm-access-token?expiryDays=10" -H "Authorization: Bearer <access_token>" 
```
 
3. Fetch a complete list of metrics. Replace `<vm-jwt>` with the token generated from the previous step. You can use this list to create queries based on metrics you're interested in.

```
export token=<vm-jwt> 
curl -k "https://10.237.212.61/api/netq/vm/api/v1/label/__name__/values" -H "Authorization: Bearer $token" 
```
 
{{< expand "Examples queries" >}}

The following example uses the VM query API to retrieve data related to `rx_errors`.

```
export token=<vm-jwt> 
curl -k "https://10.237.212.61/api/netq/vm/api/v1/query" -H "Authorization: Bearer $token" --get --data-urlencode 'query=rx_errors' 
```
 
This example is similar to the one above, but specifies a time range (`rx_errors` from the past 15 minutes):

```
export token=<vm-jwt>  
curl -k "https://10.237.212.61/api/netq/vm/api/v1/query_range" -H "Authorization: Bearer $token" --get --data-urlencode 'query= rx_errors' --data-urlencode "start=$(date -u -d '15 minutes ago' +%Y-%m-%dT%H:%M:%SZ)" --data-urlencode "end=$(date -u +%Y-%m-%dT%H:%M:%SZ)" --data-urlencode 'step=60s' 
```
{{< /expand >}}

## Additional Commands

- {{<link title="modify/#netq modify otlp endpoint" text="netq modify otlp endpoint">}}
- {{<link title="show/#netq show otlp" text="netq show otlp">}} commands



