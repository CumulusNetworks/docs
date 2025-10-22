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

## Collect Slurm Telemetry

{{<exlink url="https://slurm.schedmd.com/quickstart.html" text="Slurm">}} (Simple Linux Utility for Resource Management) is an open-source job scheduler used in high-performance computing (HPC) environments. It manages and allocates compute resources, schedules jobs, and distributes workloads across a cluster.

To view and filter Slurm jobs in Grafana, you must have an {{<exlink url="https://www.nvidia.com/en-us/data-center/base-command/manager/" text="NVIDIA Base Command Manager">}} deployment running BCM v11 or later. 

1. Authenticate into BCM using either basic authentication (username and password) or certificate-based authentication.

{{<tabs "BCM auth">}}

{{<tab "Basic Authentication">}}

Two versions of this command exist. Specify either the Base Command Manager IP address in `ip-address` or the domain name in `hostname`. Replace `port-text` with the port that BCM uses. You can run this command from any node in your cluster.

```
nvidia@netq-server:~$ netq add bcm auth-type basic user <username> pass <password> ip <ip-address> port <port-text>  
nvidia@netq-server:~$ netq add bcm auth-type basic user <username> pass <password> hostname <hostname> port <port-text> 
```
For example:
```
nvidia@netq-server:~$ netq add bcm auth-type basic user admin pass secretpass123 ip 192.168.1.100 port 8082
```
{{</tab>}}

{{<tab "Certificate-based Authentication" >}}

Two versions of this command exist. Specify either the Base Command Manager IP address in `ip-address` or the domain name in `hostname`. Replace `port-text` with the port that BCM uses.

Specify the full path to both the certificate and key files. These are typically located in the `/mnt/bcm/` directory.

```
nvidia@netq-server:~$ netq add bcm auth-type cert cert-file <certificate-path> key-file <key-path> ip <ip-address> port <port-text> 
nvidia@netq-server:~$ netq add bcm auth-type cert cert-file <certificate-path> key-file <key-path> hostname <hostname> port <port-text> 
```
For example:
```
nvidia@netq-server:~$ netq add bcm auth-type cert cert-file /mnt/bcm/bcm.crt key-file /mnt/bcm/bcm.key ip 192.168.1.100 port 8082 
```
{{</tab>}}

{{</tab>}}

2. Verify that your credentials are correct and check for BCM version compatibility:

```
nvidia@netq-server:~$ netq show bcm auth-status
```

You will configure the Slurm data source in the next section using the `slurm-nodes-and-jobs-dashboard` JSON file.

{{< expand "slurm-nodes-and-jobs-dashboard.json" >}}
```
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 14,
  "links": [],
  "panels": [
    {
      "fieldConfig": {
        "defaults": {},
        "overrides": []
      },
      "gridPos": {
        "h": 20,
        "w": 4,
        "x": 0,
        "y": 0
      },
      "id": 13,
      "options": {
        "code": {
          "language": "plaintext",
          "showLineNumbers": false,
          "showMiniMap": false
        },
        "content": "<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Slurm_logo.svg/590px-Slurm_logo.svg.png style=\"background-color:white;\" width=\"430\" height=\"320\">",
        "mode": "html"
      },
      "pluginVersion": "12.0.1",
      "title": "Panel Title",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisPlacement": "auto",
            "fillOpacity": 70,
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineWidth": 0,
            "spanNulls": 300000
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bool_on_off"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 10,
        "w": 20,
        "x": 4,
        "y": 0
      },
      "id": 10,
      "options": {
        "alignValue": "left",
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "mergeValues": true,
        "rowHeight": 0.9,
        "showValue": "never",
        "tooltip": {
          "hideZeros": false,
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "builder",
          "exemplar": false,
          "expr": "min by(pretty_name) (slurm_job_per_node{wlm=~\"$wlm\"})",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "SLURM Timeline",
      "type": "state-timeline"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "fillOpacity": 80,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineWidth": 1,
            "scaleDistribution": {
              "type": "linear"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "decimals": 0,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/Pod 2.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "yellow",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "Value (lastNotNull)"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 10,
        "w": 20,
        "x": 4,
        "y": 10
      },
      "id": 20,
      "options": {
        "barRadius": 0,
        "barWidth": 0.97,
        "fullHighlight": false,
        "groupWidth": 0.7,
        "legend": {
          "calcs": [],
          "displayMode": "table",
          "placement": "right",
          "showLegend": false
        },
        "orientation": "horizontal",
        "showValue": "auto",
        "stacking": "none",
        "tooltip": {
          "hideZeros": false,
          "maxHeight": 600,
          "mode": "single",
          "sort": "none"
        },
        "xTickLabelRotation": 0,
        "xTickLabelSpacing": 0
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "builder",
          "exemplar": false,
          "expr": "sort_desc(count by(pretty_name) (slurm_job_per_node{wlm=~\"$wlm\"}))",
          "format": "table",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "SLURM Node Allocation",
      "transformations": [
        {
          "id": "groupBy",
          "options": {
            "fields": {
              "Value": {
                "aggregations": [
                  "lastNotNull"
                ],
                "operation": "aggregate"
              },
              "pod": {
                "aggregations": []
              },
              "pod_su": {
                "aggregations": [],
                "operation": "groupby"
              },
              "pretty_name": {
                "aggregations": [],
                "operation": "groupby"
              },
              "su": {
                "aggregations": [],
                "operation": "groupby"
              }
            }
          }
        },
        {
          "id": "groupingToMatrix",
          "options": {
            "columnField": "pod_su",
            "rowField": "pretty_name",
            "valueField": "Value (lastNotNull)"
          }
        }
      ],
      "type": "barchart"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            }
          },
          "mappings": []
        },
        "overrides": [
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*mixed.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "light-orange",
                  "mode": "shades"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*down.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*reserved.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "blue",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*idle.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "yellow",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*inval.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*allocate.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*complet.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "orange",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 0,
        "y": 20
      },
      "id": 18,
      "options": {
        "displayLabels": [
          "value",
          "name"
        ],
        "legend": {
          "displayMode": "table",
          "placement": "right",
          "showLegend": true,
          "sortBy": "Value",
          "sortDesc": true,
          "values": [
            "value"
          ]
        },
        "pieType": "pie",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "count by(state) (count by(state, node) (count_over_time((slurm_nodes{wlm=~\"$wlm\"} != 0)[${__range_s}s]) > 0))",
          "fullMetaSearch": false,
          "hide": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "B",
          "useBackend": false
        }
      ],
      "title": "Slurm Node Status - Over Time",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "fixed"
          },
          "custom": {
            "align": "center",
            "cellOptions": {
              "applyToRow": true,
              "mode": "basic",
              "type": "color-background",
              "wrapText": false
            },
            "filterable": true,
            "inspect": false
          },
          "fieldMinMax": false,
          "mappings": [
            {
              "options": {
                "idle": {
                  "color": "dark-yellow",
                  "index": 8
                }
              },
              "type": "value"
            },
            {
              "options": {
                "pattern": ".*drain.*",
                "result": {
                  "color": "purple",
                  "index": 0
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*down.*",
                "result": {
                  "color": "red",
                  "index": 1
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*reserved.*",
                "result": {
                  "color": "blue",
                  "index": 2
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*idle,.*",
                "result": {
                  "color": "yellow",
                  "index": 3
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*inval.*",
                "result": {
                  "color": "red",
                  "index": 4
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*allocate.*",
                "result": {
                  "color": "green",
                  "index": 5
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*complet.*",
                "result": {
                  "color": "orange",
                  "index": 6
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*mix.*",
                "result": {
                  "color": "semi-dark-orange",
                  "index": 7
                }
              },
              "type": "regex"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": [
              {
                "id": "custom.width"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 12,
        "y": 20
      },
      "id": 1,
      "options": {
        "cellHeight": "md",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Node"
          }
        ],
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "(count by(state, node) (count_over_time((slurm_nodes{wlm=~\"$wlm\"} != 0)[${__range_s}s]) > 0))",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Slurm Nodes Status",
      "transformations": [
        {
          "id": "seriesToRows",
          "options": {}
        },
        {
          "id": "extractFields",
          "options": {
            "format": "kvp",
            "keepTime": false,
            "replace": true,
            "source": "Metric"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "cluster": true,
              "opid": true,
              "reason": true,
              "service.name": true,
              "telemetry.sdk.language": true,
              "telemetry.sdk.name": true,
              "telemetry.sdk.version": true,
              "wlm": true
            },
            "includeByName": {},
            "indexByName": {},
            "renameByName": {
              "node": "Node",
              "state": "State"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            }
          },
          "mappings": []
        },
        "overrides": [
          {
            "matcher": {
              "id": "byRegexp",
              "options": "/.*Not.*/"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 0,
        "y": 34
      },
      "id": 3,
      "options": {
        "legend": {
          "displayMode": "table",
          "placement": "right",
          "showLegend": true,
          "values": [
            "value"
          ]
        },
        "pieType": "pie",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "count by(reason) (slurm_nodes{wlm=~\"$wlm\"} == 0)",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Errors Count",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "center",
            "cellOptions": {
              "applyToRow": true,
              "mode": "basic",
              "type": "color-background",
              "wrapText": false
            },
            "filterable": true,
            "inspect": false
          },
          "fieldMinMax": false,
          "mappings": [
            {
              "options": {
                "drained": {
                  "color": "red",
                  "index": 1
                }
              },
              "type": "value"
            },
            {
              "options": {
                "pattern": ".*drained.*",
                "result": {
                  "color": "red",
                  "index": 0
                }
              },
              "type": "regex"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "red"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Node"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 234
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 107
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Reason"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 238
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 12,
        "y": 34
      },
      "id": 2,
      "options": {
        "cellHeight": "md",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Node"
          }
        ]
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "min_over_time((slurm_nodes{wlm=~\"$wlm\"} == 0)[${__range_s}s])",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Drained Slurm Nodes  ",
      "transformations": [
        {
          "id": "seriesToRows",
          "options": {}
        },
        {
          "id": "extractFields",
          "options": {
            "format": "kvp",
            "keepTime": false,
            "replace": true,
            "source": "Metric"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "__name__": true,
              "cluster": true,
              "group": true,
              "hostname": true,
              "instance": true,
              "job": true,
              "service.name": true,
              "state": false,
              "telemetry.sdk.language": true,
              "telemetry.sdk.name": true,
              "telemetry.sdk.version": true,
              "wlm": true
            },
            "includeByName": {},
            "indexByName": {
              "__name__": 0,
              "group": 1,
              "hostname": 2,
              "instance": 3,
              "job": 4,
              "node": 5,
              "reason": 7,
              "state": 6
            },
            "renameByName": {
              "node": "Node",
              "reason": "Reason",
              "state": "State"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 100,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 0,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "normal"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "allocate"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "drained"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "idle"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "inval"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Allocated"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Drain"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "red",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Idle"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "blue",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 0,
        "y": 48
      },
      "id": 19,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "count(slurm_nodes{state=~\"down|drained|draining|inval\", wlm=~\"$wlm\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Drain",
          "range": true,
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "count(slurm_nodes{state=~\"allocate|planned|reserved\", wlm=~\"$wlm\"})",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "instant": false,
          "legendFormat": "Allocated",
          "range": true,
          "refId": "A",
          "useBackend": false
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "count(slurm_nodes{state=~\"idle\", wlm=~\"$wlm\"})",
          "hide": false,
          "instant": false,
          "legendFormat": "Idle",
          "range": true,
          "refId": "C"
        }
      ],
      "title": "Slurm Node Status - Over Time",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "fieldMinMax": false,
          "mappings": [
            {
              "options": {
                "down": {
                  "color": "red",
                  "index": 0
                }
              },
              "type": "value"
            },
            {
              "options": {
                "pattern": ".*drained.*",
                "result": {
                  "color": "red",
                  "index": 1
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*down.*",
                "result": {
                  "color": "red",
                  "index": 2
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*reserved.*",
                "result": {
                  "color": "green",
                  "index": 3
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*idle.*",
                "result": {
                  "color": "green",
                  "index": 4
                }
              },
              "type": "regex"
            },
            {
              "options": {
                "pattern": ".*inval.*",
                "result": {
                  "color": "red",
                  "index": 5
                }
              },
              "type": "regex"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": []
          },
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "root - avia_test_2"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 14,
        "w": 12,
        "x": 12,
        "y": 48
      },
      "id": 6,
      "options": {
        "legend": {
          "calcs": [
            "last"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true,
          "sortBy": "Name",
          "sortDesc": false
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "builder",
          "exemplar": false,
          "expr": "slurm_jobs_node_count{wlm=~\"$wlm\"}",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": false,
          "legendFormat": "{{user}} - {{job_name}}",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Nodes Per Job",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "align": "center",
            "cellOptions": {
              "applyToRow": true,
              "mode": "basic",
              "type": "color-background",
              "wrapText": false
            },
            "inspect": false
          },
          "fieldMinMax": false,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "State"
            },
            "properties": [
              {
                "id": "custom.width"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Nodes List"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 300
              },
              {
                "id": "custom.cellOptions",
                "value": {
                  "type": "color-text",
                  "wrapText": false
                }
              },
              {
                "id": "custom.inspect",
                "value": true
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 15,
        "w": 24,
        "x": 0,
        "y": 62
      },
      "id": 5,
      "options": {
        "cellHeight": "md",
        "footer": {
          "countRows": false,
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "Job ID"
          }
        ],
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "exemplar": false,
          "expr": "slurm_jobs{wlm=~\"$wlm\"}",
          "format": "time_series",
          "fullMetaSearch": false,
          "includeNullMetadata": false,
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Slurm Jobs Status",
      "transformations": [
        {
          "id": "seriesToRows",
          "options": {}
        },
        {
          "id": "extractFields",
          "options": {
            "format": "kvp",
            "keepTime": false,
            "replace": true,
            "source": "Metric"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "__name__": true,
              "group": true,
              "hostname": true,
              "instance": true,
              "job": true,
              "service.name": true,
              "telemetry.sdk.language": true,
              "telemetry.sdk.name": true,
              "telemetry.sdk.version": true,
              "wlm": true
            },
            "includeByName": {},
            "indexByName": {
              "__name__": 0,
              "group": 1,
              "hostname": 2,
              "instance": 3,
              "job": 4,
              "job_id": 6,
              "job_name": 5,
              "nodelist": 7,
              "nodes_count": 8,
              "time_limit": 9,
              "user": 10
            },
            "renameByName": {
              "cluster": "Cluster",
              "job_id": "Job ID",
              "job_name": "Job Name",
              "node": "Node",
              "nodelist": "Nodes List",
              "nodes_count": "Nodes Count",
              "opid": "OPID",
              "run_time": "Run Time",
              "start_time": "Start Time",
              "state": "State",
              "submit_time": "Submit Time",
              "time_limit": "Run Time",
              "user": "User"
            }
          }
        },
        {
          "id": "groupBy",
          "options": {
            "fields": {
              "Cluster": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Job ID": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Job Name": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Nodes Count": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Nodes List": {
                "aggregations": [],
                "operation": "groupby"
              },
              "OPID": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Run Time": {
                "aggregations": [],
                "operation": "groupby"
              },
              "Start Time": {
                "aggregations": [],
                "operation": "groupby"
              },
              "State": {
                "aggregations": [],
                "operation": "groupby"
              },
              "User": {
                "aggregations": [],
                "operation": "groupby"
              }
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Time"
            },
            "properties": []
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 77
      },
      "id": 21,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto"
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "disableTextWrap": false,
          "editorMode": "code",
          "expr": "group by(job_id) (slurm_jobs{wlm=~\"$wlm\"})",
          "fullMetaSearch": false,
          "includeNullMetadata": true,
          "legendFormat": "{{label_name}}",
          "range": true,
          "refId": "A",
          "useBackend": false
        }
      ],
      "title": "Active Jobs Count",
      "transformations": [
        {
          "id": "reduce",
          "options": {
            "reducers": [
              "first"
            ]
          }
        },
        {
          "id": "reduce",
          "options": {
            "reducers": [
              "sum"
            ]
          }
        }
      ],
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_SLURM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green"
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 77
      },
      "id": 22,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "hideZeros": false,
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "12.0.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_SLURM}"
          },
          "editorMode": "code",
          "expr": "sum by(state) (slurm_jobs{wlm=~\"$wlm\"})",
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Active Jobs Count Over Time",
      "type": "timeseries"
    }
  ],
  "preload": false,
  "schemaVersion": 41,
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {
          "text": "All",
          "value": "$__all"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_SLURM}"
        },
        "definition": "label_values(slurm_nodes, wlm)",
        "includeAll": true,
        "label": "Workload Manager",
        "name": "wlm",
        "options": [],
        "query": {
          "query": "label_values(slurm_nodes, wlm)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "sort": 1,
        "type": "query"
      },
      {
        "allowCustomValue": false,
        "current": {
          "text": "slurm_dashboard",
          "value": "dewrawgm6mkn4d"
        },
        "hide": 2,
        "label": "Slurm Data Source",
        "name": "DS_SLURM",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "/^slurm/",
        "type": "datasource"
      }
    ]
  },
  "time": {
    "from": "now-5m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "browser",
  "title": "Slurm Nodes & Jobs",
  "uid": "bdv6i9jduoe80f8",
  "version": 17
}
```
{{< /expand >}}

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

### Import a Dashboard Template

To import a preconfigured dashboard into your Grafana instance:

1. From the side menu, select **Dashboards**.

2. Click **New** and select **Import** from the drop-down menu.

3. Paste the dashboard JSON text into the text area.

4. (Optional) Change the dashboard name, folder, or UID.

5. Click **Import**.

### Grafana Best Practices

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



