---
title: Integrate NetQ with Grafana
author: NVIDIA
weight: 550
toc: 3
---

The NetQ integration with Grafana allows you to create customized dashboards and to visualize metrics across your network's hardware. You can create your own dashboards from scratch or import a dashboard template to get started.
<!--
{{<figure src="/images/netq/grafana-dash-415.png" alt="Grafana dashboard displaying GPU statistics" width="1200">}}
-->

## Requirements and Support Information

- The NetQ Grafana integration is supported for on-premises deployments only
- Switches must have a Spectrum-2 or later ASIC, with Cumulus Linux version x.x or later
- Before you get started with the steps below, you must {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/installation/" text="install Grafana">}} and {{<exlink url="https://grafana.com/docs/grafana/latest/setup-grafana/start-restart-grafana/" text="start the Grafana server">}}

## Configure and Enable OpenTelemetry on Devices

Configure your client devices to send OpenTelemetry (OTLP) data to NetQ.

{{<tabs "TabID23" >}}

{{<tab "CL switches">}}

1. From the NetQ server, display the CA certificate using `netq show otlp tls-ca-cert dump` command. Copy the certificate from the output.

2. On the switch, import the CA certificate file, with the `nv action import system security ca-certificate <cert-id>` command. Replace `<cert-id>` with the certificate you generated in the preceding step.

3. Configure an X.509 certificate to secure the gRPC connection:

   ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc cert-id <ca-certificate>
   cumulus@switch:~$ nv config apply
   ```

4. Next, disable `insecure` mode and apply the change:
    
    ```
   cumulus@switch:~$ nv set system telemetry export otlp grpc insecure disabled
   cumulus@switch:~$ nv config apply
   ```
5. Run `nv show system telemetry health` to display port and IP address information, along with the connectivity status.

6. Next, enable OpenTelemetry for each metric that you want to monitor, as described in the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Monitoring-and-Troubleshooting/Open-Telemetry-Export/" text="Cumulus Linux documentation">}}.

{{<notice info>}}
NVIDIA recommends setting the <code>sample-interval</code> option to 10 seconds for each metric that allows you to set a sample interval.
{{</notice>}}

{{</tab>}}

{{<tab "DPUs" >}}

1. 

2. 

{{</tab>}}

{{</tabs>}}

## Configure the Time Series Database on the NetQ Server

1. Add the OTLP endpoint: <!--need to eplain this-->

`netq add otlp endpoint tsdb-name <text-tsdb-endpoint> tsdb-url <text-tsdb-endpoint-url> [export true | export false] [security-mode <text-mode>]`


## Configure the Data Sources in Grafana

1. Generate and copy an authentication token using the NetQ CLI. The default setting creates a token that expires after 5 days. You can adjust the time with the `expiry` option. For example, the following command generates a token that expires after 40 days. The maximum number of days allowed is 180.

```
netq show vm-token expiry 40
```

2. Navigate to your Grafana dashboard. From the menu, select **Connections** and then **Data sources**. In the *Connection* field, enter the IP address of your NetQ telemetry server, followed by */api/netq/vm/*. In a cluster deployment, enter the virtual IP address (VIP) in this field:

<!--insert pic-->

3. On the same page, navigate to the *Authentication* section. In the *HTTP headers* section, select **Add header**. In the *Header* field, enter **Authorization**. In the *Value* field, enter the token that you generated in step one of this section.

4. Select **Save & test**.



## Import a Dashboard Template

To import a preconfigured dashboard into your Grafana instance, following the steps in the {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/import-dashboards/" text="Grafana documentation">}}. You can download the dashboard JSON files from the NetQ Grafana Dashboard Github repo.

## Troubleshooting

- If your dashboard data is loading slowly, you may need to add an interval variable as described in the {{<exlink url="https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/#add-an-interval-variable" text="Grafana documentation">}}.