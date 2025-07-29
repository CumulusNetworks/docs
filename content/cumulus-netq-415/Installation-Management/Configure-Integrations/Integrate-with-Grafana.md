---
title: Integrate NetQ with Grafana
author: NVIDIA
weight: 550
toc: 3
---

The NetQ integration with Grafana allows you to create customized dashboards and to visualize metrics across your network's hardware. To view data in Grafana, first configure OpenTelemetry (OTel) on your hardware devices, then configure the time series database on the NetQ server, and finally configure the data sources in Grafana. <!--You can create your own dashboards from scratch or import a dashboard template to get started.-->

{{%notice note%}}
The Grafana integration is in beta and supported for on-premises deployments only.
{{%/notice%}}

## Requirements and Support

- Switches must have a Spectrum-2 or later ASIC
- DPUs and ConnectX hosts must be running DOCA Telemetry Service (DTS) version 1.18-1.20
- Before you get started with the steps below, {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/installation/" text="install Grafana">}} and {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/start-restart-grafana/" text="start the Grafana server">}}
- Data is typically stored for seven days
- High availability is not supported: all nodes must be up and running for Grafana to display data


## Configure and Enable OpenTelemetry on Devices

Configure your client devices to send OpenTelemetry data to NetQ.

{{<tabs "TabID23" >}}

{{<tab "CL switches">}}

Configure OpenTelemetry to run on the switch in secure mode with a self-signed certificate:

1. From the NetQ server, display the CA certificate using `netq show otlp tls-ca-cert dump` command. Copy the certificate from the output.

2. On the switch, import the CA certificate file, with the `nv action import system security ca-certificate <cert-id> data <data>` command. Define the name of the certificate in `<cert-id>` and replace `<data>` with the certificate you generated in the preceding step.

3. Configure an X.509 certificate to secure the OTel connection. Replace `ca-certificate` with the name of your certificate; this is the `<cert-id>` from the previous step.

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

6. Next, enable OpenTelemetry for each metric that you want to monitor, as described in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/" text="Cumulus Linux documentation">}}. <!--should I move this to the beginning of this section?-->

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

## Configure the Time Series Database on the NetQ Server

1. From the NetQ server, add the OTel endpoint of your time series database (TSDB). Replace `text-tsdb-endpoint` and `text-tsdb-endpoint-url` with the name and IP address of your TSDB, respectively. Include the `export true` option to begin exporting data immediately. You can optionally set `security-mode` to `tls` to enable TLS.

```
nvidia@netq-server:~$ netq add otlp endpoint tsdb-name <text-tsdb-endpoint> tsdb-url <text-tsdb-endpoint-url> [export true | export false] [security-mode <text-mode>]
```

2. If you set the `export` option to `true` in the previous step, the TSDB will begin receiving the time series data for the metrics that you configured on the switch. Use the `netq show otlp endpoint` command to view the TSDB endpoint configuration.


## Configure Data Sources in Grafana

1. Generate and copy an authentication token using the NetQ CLI. You can adjust time at which the token will expire with the `expiry` option. For example, the following command generates a token that expires after 40 days. If you do not set an `expiry` option, the token expires after 5 days. The maximum number of days allowed is 180.

```
nvidia@netq-server:~$ netq show vm-token expiry 40
```

2. Navigate to your Grafana dashboard. From the menu, select **Connections** and then **Data sources**. Select **Add new data source** and add the Prometheus TSDB:

{{<figure src="/images/netq/grafana-prom-415.png" alt="" width="1200">}}

3. Continue through the steps to configure the data source. In the *Connection* field, enter the IP address of your NetQ server followed by `/api/netq/vm/`, for example `https://10.255.255.255/api/netq/vm/`. In a cluster deployment, enter the virtual IP address in this field (followed by `/api/netq/vm/`). 

<!--insert pic-->

4. On the same page, navigate to the *Authentication* section. In the *HTTP headers* section, select **Add header**. In the *Header* field, enter **Authorization**. In the *Value* field, enter the token that you generated in step one of this section.

{{<figure src="/images/netq/grafana-header-415.png" alt="" width="1000">}}

5. Select **Save & test**. If the operation was successful, you will begin to see metrics in your Grafana dashboard. 

<!--
## Import a Dashboard Template

To import a preconfigured dashboard into your Grafana instance, following the steps in the {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/import-dashboards/" text="Grafana documentation">}}. You can download the dashboard JSON files from the NetQ Grafana Dashboard Github repo.

-->

## Grafana Best Practices

If Grafana is slow or laggy, you might need to adjust your dashboard settings. Fabric-wide queries on large networks (over 1000 switches) can generate millions of data points, which can significantly degrade performance. You can improve performance by optimizing queries, reducing data volume, and simplifying panel rendering.

Avoid plotting all time-series data at once. To visualize the data in different ways:
   - {{<exlink url="https://grafana.com/docs/grafana/latest/fundamentals/timeseries/#aggregating-time-series" text="Aggregate time series data">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/fundamentals/timeseries/#aggregating-time-series" text="Add labels to your time series data">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Add interval variables">}}
   - {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Use aggregation operators">}} such as `count` and `topk`

{{<notice tip>}}
If Grafana displays "No Data", verify that all VMs in your cluster are operational. You can check the node status using the <code>kubectl get nodes</code> command. A node will show as <code>NotReady</code> if it is down. When the VM is restored, data collection will resume and will be displayed within 20 minutes of restoration.
{{</notice>}}

## Export TSDB Data With APIs

If you want to view or export the time series database data without using Grafana, you can use curl commands to directly query VictoriaMetrics. These commands typically complete in fewer than 30 seconds.

1. Generate an access token using the login API. Replace `<username>` and `<password>` with your NetQ username and password. Copy the access token generated by this command. You will use it in the next step. 
```
curl 'https://10.237.212.61/api/netq/auth/v1/login' -H 'content-type: application/json' --data-raw '{"username":"<username>","password":"<password>"}' --insecure 
```
 2. Generate a VictoriaMetrics token using the VM login API. Replace `<access_token>` with the token generated from the previous step. Copy the VictoriaMetrics access token generated by this command. You will use it in the next step. 
```
curl -k -X GET "https://10.237.212.61/api/netq/auth/v1/vm-access-token?expiryDays=10" -H "Authorization: Bearer <access_token>" 
```
 
3. Fetch a complete list of metrics using the VM metrics API. Replace `<vm-jwt>` with the token generated from the previous step. You can use this list to create queries based on metrics you're interested in.

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



