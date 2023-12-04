---
title: Install NIC and DPU Agents
author: NVIDIA
weight: 340
toc: 5
---

Installing NetQ telemetry agents on your hosts with {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-adapters/" text="NVIDIA ConnectX adapters">}} and {{<exlink url="https://www.nvidia.com/en-us/networking/products/data-processing-unit/" text="NVIDIA BlueField data processing units">}} (DPUs) allows you to track inventory data and statistics across devices. The DOCA Telemetry Service (DTS) is the agent that runs on hosts and DPUs to collect data.

{{%notice note%}}
- NIC telemetry for ConnectX adapters is supported only for on-premises NetQ deployments.
- ConnectX telemetry is supported on DTS version 1.14.2 and later.
{{%/notice%}}

## Install DTS on ConnectX Hosts

To install and configure the {{<exlink url="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/doca/containers/doca_telemetry" text="DOCA Telemetry Service">}} container on a host with ConnectX adapters, perform the following steps:

1. Obtain the latest DTS container image path from {{<exlink url="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/doca/containers/doca_telemetry" text="the NGC catalog">}}. Select **Get Container** and copy the image path.

2. Run the DTS container with Docker on the host. Use the image path obtained in the previous step for the **DTS_IMAGE** variable and configure the IP address of your NetQ server for the `-i` option:

```
export DTS_IMAGE=nvcr.io/nvidia/doca/doca_telemetry:1.14.2-doca2.2.0-host
docker run -v "/opt/mellanox/doca/services/telemetry/config:/config" --rm --name doca-telemetry-init -ti $DTS_IMAGE /bin/bash -c "DTS_CONFIG_DIR=host_netq /usr/bin/telemetry-init.sh && /usr/bin/enable-fluent-forward.sh -i=10.10.10.1 -p=30001"
docker run -d --net=host                                                              \
              --privileged                                                            \
              -v "/opt/mellanox/doca/services/telemetry/config:/config"               \
              -v "/opt/mellanox/doca/services/telemetry/ipc_sockets:/tmp/ipc_sockets" \
              -v "/opt/mellanox/doca/services/telemetry/data:/data"                   \
              --rm --name doca-telemetry -it $DTS_IMAGE /usr/bin/telemetry-run.sh
```

### Configure Prometheus Targets for ConnectX Adapters

The Prometheus adapter pod in NetQ collects statistics from ConnectX adapters in your network. To add adapters as a target for data collection, perform the following steps:

1. On your NetQ VM, edit the `targets-config` ConfigMap with the `kubectl edit cm targets-config` command.

Add the desired host IP addresses to the `targets` stanza, maintaining `yaml` indentation. Multiple entries must be separated by commas, and the port is 9100:

```
data:
  targets.json: |-
    [
      {
        "labels": {
        "job": "node"
      },
      "targets": [
         "10.10.10.10:9100","10.10.10.11:9100"
        ]
      }
    ]
```

2. Restart the `netq-prom-adapter` pod.

Retrieve the current pod name with the `kubectl get pods | grep netq-prom` command:

```
cumulus@netq-server:~$ kubectl get pods | grep netq-prom
netq-prom-adapter-ffd9b874d-hxhbz                    2/2     Running   0          3h50m
```
Restart the pod by deleting the running pod:

```
kubectl delete pod netq-prom-adapter-ffd9b874d-hxhbz
```

## Install DTS on DPUs

To install and configure the DOCA Telemetry Service container on a DPU, perform the following steps:

1. Obtain the latest DTS container image path from {{<exlink url="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/doca/containers/doca_telemetry" text="the NGC catalog">}}. Select **Get Container** and copy the image path.

2. Retrieve the container `yaml` configuration file onto the host. Use the path specified in the *Adjusting the .yaml Configuration* section in the {{<exlink url="https://catalog.ngc.nvidia.com/orgs/nvidia/teams/doca/containers/doca_telemetry" text="NGC instructions">}}. Copy it to `/etc/kubelet.d/doca_telemetry_standalone.yaml`:

```
wget --content-disposition https://api.ngc.nvidia.com/v2/resources/nvidia/doca/doca_container_configs/versions/2.0.2v1/files/configs/2.0.2/doca_telemetry.yaml
```

3. Edit the `command` in the `initContainers` section of the `/etc/kubelet.d/doca_telemetry_standalone.yaml` file to set the `DTS_CONFIG_DIR` parameter to `inventory_netq` and configure the fluent forwarding `-i` option to your NetQ server IP address and the `-p` option to 30001:

```
  initContainers:
...
      command: ["/bin/bash", "-c", "DTS_CONFIG_DIR=inventory_netq /usr/bin/telemetry-init.sh && /usr/bin/enable-fluent-forward.sh -i=10.10.10.1 -p=30001"]
```

{{%notice note%}}
This step replaces the default configuration of `command: ["/bin/bash", "-c", "/usr/bin/telemetry-init.sh && /usr/bin/enable-fluent-forward.sh"]`.
{{%/notice%}}

4. Restart the DPE service with the `service restart dpe` command.

## Related Information

- {{<link title="DPU Inventory" text="DPU inventory">}} and {{<link title="DPUs" text="monitoring">}}
- {{<link title="NIC Inventory" text="NIC inventory">}} and {{<link title="NICs" text="monitoring">}}