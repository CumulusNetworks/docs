---
title: Collect KPIs
author: NVIDIA
weight: 850
toc: 4
---

The KPI REST endpoint provides key performance indicators (KPIs) that summarize your network cluster’s overall health while also allowing you to examine specific events in greater detail. KPIs reflect aggregated data across all domains. To troubleshoot a specific domain, use the compute-node or switch-node REST API endpoints.

## Access the API

In the following examples, replace `<username>` with either `rw-user` (read-write access) or `ro-user` (read-only access). Replace `<password>` with the actual password associated with the user. <!--4.15 does this work with nvidia, nvidia?-->

{{<tabs "KPI access">}}

{{<tab "cURL">}}
```
curl --request GET \
  --url https://xxxx.xxxx.xxxx.xxxx/nmx/v1/kpis \
  --user "<username>:<password>" --insecure 
```

{{</tab>}}
{{<tab "wget" >}}
```
wget --quiet \
  --method GET \
  --user '<username>' \
  --password '<password>' \
  --output-document \
  - https://xxxx.xxxx.xxxx.xxxx/nmx/v1/kpis --no-check-certificate
```
{{</tab>}}
{{</tabs>}}

## API Filters

The REST API supports filtering based on health or inventory information. To use these filters, append the filter parameter to the endpoint, for example `kpis?filter=HEALTH`. Filter values include:

Health filters:
- HEALTH
- SWITCH_HEALTH
- GPU_HEALTH
- DOMAIN_HEALTH
- COMPUTE_HEALTH

Inventory filters:
- INVENTORY
- COMPUTE_ALLOCATION
- CONNECTION_COUNT
- CABLE_TYPE
- CABLE_PN
- CABLE_FW_VERSION
- PORT_COUNT
- LINK_UP_COUNT
- LINKDOWN_FREQUENCY
- LINKDOWN_RATE
- CHIP_TEMPERATURE
- EFF_BER
- SYMBOL_BER
- RAW_BER

{{< expand "cURL example with filtering" >}}

Make a GET request to the `/v1/kpis` endpoint using a filter:
```
curl --request GET --url https://xxx.xxx.xx/nmx/v1/kpis?filter=SWITCH_HEALTH --user "<username>:<password>" --insecure
```
Example response:
```
{
    "Data": [
        {
            "HEALTHY": 18
        },
        {
            "MISSING_NVLINK": 0
        },
        {
            "UNHEALTHY": 0
        },
        {
            "UNKNOWN": 0
        }
    ],
    "Description": "Number of switch instances per health state",
    "Title": "Switch Health Count",
    "Type": "histogram"
}
```

{{< /expand >}}

{{< expand "cURL example without filtering" >}}

Make a GET request to the `/v1/kpis` endpoint without using a filter:
```
curl --request GET --url https://xxxx.xxxx.xxxx.xxxx/nmx/v1/kpis --user "<username>:<password>" --insecure
```
Example response:
```
{
    "Health": {
        "compute-health": {
            "Data": [
                {
                    "UNKNOWN": 0
                },
                {
                    "HEALTHY": 9
                },
                {
                    "DEGRADED": 0
                },
                {
                    "UNHEALTHY": 0
                }
            ],
            "Description": "Number of compute nodes per health state",
            "Title": "Compute Health Count",
            "Type": "histogram"
        },
        "domain-health": {
            "Data": [
                {
                    "UNKNOWN": 0
                },
                {
                    "HEALTHY": 1
                },
                {
                    "DEGRADED": 0
                },
                {
                    "UNHEALTHY": 0
                }
            ],
            "Description": "Number of domains per health state",
            "Title": "Domain Health Count",
            "Type": "histogram"
        },
        "gpu-health": {
            "Data": [
                {
                    "DEGRADED": 0
                },
                {
                    "NONVLINK": 0
                },
                {
                    "UNKNOWN": 0
                },
                {
                    "DEGRADED_BW": 0
                },
                {
                    "HEALTHY": 36
                }
            ],
            "Description": "Number of GPU instances per health state",
            "Title": "GPU Health Count",
            "Type": "histogram"
        },
        "switch-health": {
            "Data": [
                {
                    "MISSING_NVLINK": 0
                },
                {
                    "UNHEALTHY": 0
                },
                {
                    "UNKNOWN": 0
                },
                {
                    "HEALTHY": 18
                }
            ],
            "Description": "Number of switch instances per health state",
            "Title": "Switch Health Count",
            "Type": "histogram"
        }
    },
    "Inventory": {
        "cable-fw-version": {
            "Data": [
                {
                    "N/A": 1296
                }
            ],
            "Description": "Count the number of entries for each FWVersion.",
            "Title": "Cable FWVersion Count",
            "Type": "histogram"
        },
        "cable-pn": {
            "Data": [
                {
                    "N/A": 1296
                }
            ],
            "Description": "Count the number of entries for each PN.",
            "Title": "Cable PN Count",
            "Type": "histogram"
        },
        "cable-type": {
            "Data": [
                {
                    "850 nm VCSEL": 558
                }
            ],
            "Description": "Count the number of entries for each cable type.",
            "Title": "Cable Type Count",
            "Type": "histogram"
        },
        "chip-temperature": {
            "Data": [
                {
                    "30-40": 50
                }
            ],
            "Description": "Number of instances per temperature",
            "Title": "Chip Temperature Count",
            "Type": "histogram"
        },
        "compute-allocation": {
            "Data": [
                {
                    "FULL": 9
                },
                {
                    "PARTIAL": 0
                },
                {
                    "ALL": 9
                },
                {
                    "FREE": 0
                }
            ],
            "Description": "Number of compute nodes with its GPU instances in allocation state",
            "Title": "Compute GPU Allocation Count",
            "Type": "histogram"
        },
        "connection-count": {
            "Data": [
                {
                    "DISCOVERED": 0
                },
                {
                    "EXPECTED": 0
                },
                {
                    "EXPECTED_ACTIVE": 0
                },
                {
                    "EXPECTED_INACTIVE": 0
                },
                {
                    "UNEXPECTED": 0
                }
            ],
            "Description": "Number of connection count per connection attribute",
            "Title": "Topology connection Count",
            "Type": "histogram"
        },
        "effective-ber": {
            "Data": [
                {
                    "effective_ber": 0,
                    "node_guid": "0xb0cf0e0300db1be0",
                    "port_guid": "0x00000002251f681b"
                },
                {
                    "effective_ber": 0,
                    "node_guid": "0xb0cf0e0300db19a0",
                    "port_guid": "0x00000002251f681b"
                },
                {
                    "effective_ber": 0,
                    "node_guid": "0xb0cf0e0300db1be0",
                    "port_guid": "0x00000002251f681b"
                }
            ],
            "Description": "List of top 100 port that has the highest EFFECTIVE BER readings",
            "Title": "Top 100 EFFECTIVE BER Ports",
            "Type": "histogram"
        },
        "link-down-frequency": {
            "Data": [
                {
                    "SWITCH": 0.00020169558757286254
                }
            ],
            "Description": "Average time between link down events",
            "Title": "Link Down Frequency",
            "Type": "counter"
        },
        "link-down-rate": {
            "Data": [
                {
                    "link_down_rate": 16.616666666666685,
                    "node_guid": "0xb0cf0e0300dafa00",
                    "port_guid": "0x00000002251f681b"
                },
                {
                    "link_down_rate": 16.58333333333335,
                    "node_guid": "0xdf5abd57894e3a50",
                    "port_guid": "0x00000002251f681b"
                },
                {
                    "link_down_rate": 16.53333333333335,
                    "node_guid": "0xdf5abd57894e3a50",
                    "port_guid": "0x00000002251f681b"
                }
            ],
            "Description": "List of top 100 port that has the highest link down events",
            "Title": "Top 100 Link Down Ports",
            "Type": "histogram"
        },
        "link-up-count": {
            "Data": [
                {
                    "current": 1296
                },
                {
                    "min": 0
                },
                {
                    "max": 1296
                }
            ],
            "Description": "Number of links in UP state out of total link number.",
            "Title": "Link UP Count",
            "Type": "histogram"
        },
        "port-count": {
            "Data": [
                {
                    "GPU": 648
                },
                {
                    "SWITCH_ACCESS": 648
                },
                {
                    "SWITCH_TRUNK": 0
                },
                {
                    "UNDEFINED": 0
                }
            ],
            "Description": "Number of ports per device type.",
            "Title": "Port Type Count",
            "Type": "histogram"
        },
        "raw-ber": {
            "Data": [
                {
                    "node_guid": "0xb0cf0e0300dafb60",
                    "port_guid": "0x00000002251f681b",
                    "raw_ber": 0
                },
                {
                    "node_guid": "0xb0cf0e0300db1be0",
                    "port_guid": "0x00000002251f681b",
                    "raw_ber": 0
                },
                {
                    "node_guid": "0xfdece0e67e59176f",
                    "port_guid": "0x00000002251f681b",
                    "raw_ber": 0
                }
            ],
            "Description": "List of top 100 port that has the highest RAW BER readings",
            "Title": "Top 100 RAW BER Ports",
            "Type": "histogram"
        },
        "symbol-ber": {
            "Data": [
                {
                    "node_guid": "0x7e4c3b753098777c",
                    "port_guid": "0x00000002251f681b",
                    "symbol_ber": 0
                },
                {
                    "node_guid": "0xb0cf0e0300db1940",
                    "port_guid": "0x00000002251f681b",
                    "symbol_ber": 0
                },
                {
                    "node_guid": "0xb0cf0e0300dafa40",
                    "port_guid": "0x00000002251f681b",
                    "symbol_ber": 0
                }
            ],
            "Description": "List of top 100 port that has the highest SYMBOL BER readings",
            "Title": "Top 100 SYMBOL BER Ports",
            "Type": "histogram"
        }
    }
}
```
{{< /expand >}}

## View KPIs in Grafana

To view KPIs in Grafana, first {{<link title="Integrate NetQ with Grafana/#configure-data-sources-in-grafana" text="download Grafana and configure the data sources">}}. When you are ready to import the dashboard template, copy the contents of the `kpi-dashboard` JSON file and paste them in Grafana.

{{< expand "kpi-dashboard.json" >}}
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
  "id": 25,
  "links": [],
  "panels": [
    {
      "datasource": {
        "type": "marcusolsson-json-datasource",
        "uid": "${DS_KPI}"
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
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 5,
      "options": {
        "displayLabels": [
          "name",
          "value"
        ],
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
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
          "fields": "/.*/",
          "values": false
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "11.4.0",
      "targets": [
        {
          "cacheDurationSeconds": 300,
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "${DS_KPI}"
          },
          "fields": [
            {
              "jsonPath": "$.Health.compute-health.Data[*].HEALTHY"
            },
            {
              "jsonPath": "$.Health.compute-health.Data[*].DEGRADED",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.compute-health.Data[*].UNHEALTHY",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.compute-health.Data[*].UNKNOWN",
              "language": "jsonpath",
              "name": ""
            }
          ],
          "method": "GET",
          "queryParams": "",
          "refId": "A",
          "urlPath": ""
        }
      ],
      "title": "Compute Health",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "marcusolsson-json-datasource",
        "uid": "${DS_KPI}"
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
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 0
      },
      "id": 1,
      "options": {
        "displayLabels": [
          "name",
          "value"
        ],
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
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
          "fields": "/.*/",
          "values": false
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.4.0",
      "targets": [
        {
          "cacheDurationSeconds": 300,
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "${DS_KPI}"
          },
          "fields": [
            {
              "jsonPath": "$.Inventory.compute-allocation.Data[*].ALL"
            },
            {
              "jsonPath": "$.Inventory.compute-allocation.Data[*].FREE",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Inventory.compute-allocation.Data[*].FULL",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Inventory.compute-allocation.Data[*].PARTIAL",
              "language": "jsonpath",
              "name": ""
            }
          ],
          "method": "GET",
          "queryParams": "",
          "refId": "A",
          "urlPath": ""
        }
      ],
      "title": "Compute Node Allocation",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "marcusolsson-json-datasource",
        "uid": "${DS_KPI}"
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
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 8
      },
      "id": 4,
      "options": {
        "displayLabels": [
          "name",
          "value"
        ],
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
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
          "fields": "/.*/",
          "values": false
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.4.0",
      "targets": [
        {
          "cacheDurationSeconds": 300,
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "${DS_KPI}"
          },
          "fields": [
            {
              "jsonPath": "$.Health.domain-health.Data[*].HEALTHY"
            },
            {
              "jsonPath": "$.Health.domain-health.Data[*].DEGRADED",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.domain-health.Data[*].UNHEALTHY",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.domain-health.Data[*].UNKNOWN",
              "language": "jsonpath",
              "name": ""
            }
          ],
          "method": "GET",
          "queryParams": "",
          "refId": "A",
          "urlPath": ""
        }
      ],
      "title": "Domain Health",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "marcusolsson-json-datasource",
        "uid": "${DS_KPI}"
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
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 8
      },
      "id": 2,
      "options": {
        "displayLabels": [
          "name",
          "value"
        ],
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
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
          "fields": "/.*/",
          "values": false
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.4.0",
      "targets": [
        {
          "cacheDurationSeconds": 300,
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "${DS_KPI}"
          },
          "fields": [
            {
              "jsonPath": "$.Health.compute-health.Data[*].HEALTHY"
            },
            {
              "jsonPath": "$.Health.compute-health.Data[*].DEGRADED",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.compute-health.Data[*].UNHEALTHY",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.compute-health.Data[*].UNKNOWN",
              "language": "jsonpath",
              "name": ""
            }
          ],
          "method": "GET",
          "queryParams": "",
          "refId": "A",
          "urlPath": ""
        }
      ],
      "title": "Switch Health",
      "type": "piechart"
    },
    {
      "datasource": {
        "type": "marcusolsson-json-datasource",
        "uid": "${DS_KPI}"
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
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 16
      },
      "id": 3,
      "options": {
        "displayLabels": [
          "name",
          "value"
        ],
        "legend": {
          "displayMode": "list",
          "placement": "bottom",
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
          "fields": "/.*/",
          "values": false
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "11.4.0",
      "targets": [
        {
          "cacheDurationSeconds": 300,
          "datasource": {
            "type": "marcusolsson-json-datasource",
            "uid": "${DS_KPI}"
          },
          "fields": [
            {
              "jsonPath": "$.Health.gpu-health.Data[*].HEALTHY"
            },
            {
              "jsonPath": "$.Health.gpu-health.Data[*].NONVLINK",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.gpu-health.Data[*].DEGRADED",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.gpu-health.Data[*].UNKNOWN",
              "language": "jsonpath",
              "name": ""
            },
            {
              "jsonPath": "$.Health.gpu-health.Data[*].DEGRADED_BW",
              "language": "jsonpath",
              "name": ""
            }
          ],
          "method": "GET",
          "queryParams": "",
          "refId": "A",
          "urlPath": ""
        }
      ],
      "title": "GPU Health",
      "type": "piechart"
    }
  ],
  "preload": false,
  "schemaVersion": 40,
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {},
        "hide": 1,
        "label": "Kpi Data Source",
        "name": "DS_KPI",
        "options": [],
        "query": "marcusolsson-json-datasource",
        "refresh": 1,
        "regex": "/^kpi/",
        "type": "datasource"
      }
    ]
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "browser",
  "title": "KPI",
  "uid": "debcjtlze6pdsd",
  "version": 9,
  "weekStart": ""
}
```
{{< /expand >}}