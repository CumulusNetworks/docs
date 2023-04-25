---
title: Install On-switch OPTA
author: NVIDIA
weight: 280
toc: 4
---
## Configure the On-switch OPTA

Instead of installing a dedicated OPTA VM, you can enable the OPTA service on one or more switches in your environment to send data to the NetQ Cloud. 

On-switch OPTA (on-premises telemetry aggregator) is intended for use in small NetQ Cloud deployments where a dedicated OPTA VM might not be necessary. If you need help assessing the correct OPTA configuration for your deployment, {{<exlink url="https://www.nvidia.com/en-us/contact/sales/" text="contact your NVIDIA">}} sales team.

To configure a switch for OPTA functionality, install the `netq-opta` package. To obtain the package, add or uncomment the NetQ repository in `/etc/apt/sources.list` as needed:

```
cumulus@switch:~$ sudo nano /etc/apt/sources.list
...
deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-{{<version>}}
...
```

{{<notice tip>}}
You can use the <code>deb https://apps3.cumulusnetworks.com/repos/deb CumulusLinux-4 netq-latest</code> repository if you want to always retrieve the latest posted version of NetQ.
{{</notice>}}

After adding the repository, install the `netq-opta` package with the following commands:

```
sudo apt-get update
sudo apt-get install netq-opta
```

After the `netq-opta` package is installed, add your OPTA configuration key. Run the following command with the `config-key` obtained from the email you received from NVIDIA titled _NetQ Access Link_. You can also obtain the configuration key through the NetQ UI in the {{<link title="Configure Premises" text="premises management configuration">}}.

```
sudo netq config add opta config-key <config_key> [vrf <vrf_name>] [proxy-host <text-proxy-host> proxy-port <text-proxy-port>] 
```

The VRF name should be the VRF used to communicate with the NetQ Cloud. Specifying a proxy host and port is optional. For example:

```
sudo netq config add opta config-key tHkSI2d3LmRldjMubmV0cWRldi5jdW11bHVasdf29ya3MuY29tGLsDIiwzeUpNc3BwK1IyUjVXY2p2dDdPL3JHS3ZrZ1dDUkpFY2JkMVlQOGJZUW84PTIEZGV2MzoHbmV0cWRldr vrf mgmt
```

You can also add a proxy host separately with the following command:

```
sudo netq config add opta proxy-host <text-proxy-host> proxy-port <text-proxy-port>
```

After adding the `config-key`, restart the OPTA service:

```
sudo netq config restart opta
```

## Connect NetQ Agents to the OPTA Service

The final step is configuring NetQ Agents to connect to the OPTA service. To configure the agent on a switch to connect locally to the OPTA service running on that switch, configure the agent to connect to `localhost` with the following command:

```
sudo netq config add agent server localhost vrf mgmt
sudo netq config restart agent
```

To configure the agent on a switch to connect to the OPTA service on another switch in your network, configure the agent to connect to the IP address of the switch running the OPTA service:

```
sudo netq config add agent server 192.168.1.254 vrf mgmt
sudo netq config restart agent
```

## Configure the LCM Executor

When the LCM executor is configured, the on-switch OPTA service supports the following {{<link title="Lifecycle Management" text="lifecycle management">}} functions:

- Switch discovery
- NetQ Agent and CLI installation
- Switch upgrade and configuration restoration
- Switch decommission
- Flow analysis

The {{<link title="Install On-switch OPTA/#connect-netq-agents-to-the-opta-service" text="NetQ Agent must be running">}} for lifecycle management to work properly. 

{{<notice note>}}
LCM with the on-switch OPTA service is supported on NVIDIA Spectrum-2 platforms and above.
{{</notice>}}

After installing and configuring the `netq-opta` package, enable the LCM executor with the following commands:

```
sudo netq config add opta executor-enabled true
sudo netq config restart lcm-executor
```
### Considerations

- You cannot enable the LCM executor on more than one switch running the OPTA service.
- You cannot decommission a switch from the NetQ UI while it is running the OPTA service. To decommission a switch running the OPTA service, stop services with the `sudo netq config stop opta` and `sudo netq config stop lcm-executor` commands. Then reconfigure any NetQ Agents to connect to a different OPTA before decommissioning the switch.
- You cannot upgrade a switch using NetQ LCM if it is the only switch in your network running the OPTA service with the LCM executor enabled. To upgrade the switch, reconfigure OPTA and the LCM executor on a different switch and redirect NetQ Agents to the new OPTA before upgrading the original switch.

## Disable the LCM Executor

Disable the LCM executor by stopping it, then restarting the OPTA service:

```
sudo netq config stop lcm-executor
sudo netq config add opta executor-enabled false
sudo netq config restart opta
```
