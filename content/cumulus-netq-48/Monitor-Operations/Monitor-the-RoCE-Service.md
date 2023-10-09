---
title: RoCE
author: NVIDIA
weight: 940
toc: 3
---

Use the UI or CLI to monitor RDMA over Converged Ethernet (RoCE) for Spectrum switches, BlueField DPUs, and ConnectX SmartNICs.

## RoCE Commands

The following commands display your network's RoCE configuration, RoCE counters and counter pools, and RoCE-related events. See the {{<link title="show/#netq-show-roce-config" text="command line reference">}} for additional options, definitions, and examples.

```
netq show roce-config 
netq show roce-counters  
netq show roce-counters pool
netq show events message_type tca_roce
netq show events message_type roceconfig
```

The {{<link title="check/#netq check roce" text="netq check roce">}} command checks for consistent RoCE and QoS configurations across all nodes in your network fabric.

```
netq check roce
```

## View RoCE Counters Networkwide in the UI

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network heading, select **RoCE counters**. Use the tabs to view receive (Rx), transmit (Tx), and pool counters networkwide.
## View RoCE Counters for a Given Switch

You can view the following RoCE counters for a given switch:

- Receive and transmit counters
- General, CNP, and RoCE-specific counters
- Counter pools
- Port-specific counters

To view RoCE counters on a switch, navigate to the header and select {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices**, then click **Open a device card**. Select the large card, then click the RoCE icon {{<img src="/images/netq/roce-icon.svg" width="18px">}} at the top of the card to view RoCE counters and their associated ports:

{{<figure src="/images/netq/roce-l3-card-4.0.0.png" alt="switch card displaying list of ports" width="500">}}

Expand the card to the largest size, then select **RoCE counters** from the side menu. Use the controls above the table to view, filter, or export counter statistics by Rx, Tx, or Pool:

{{<figure src="/images/netq/roce-rx-counters-fs-4.0.0.png" alt="full-size switch card with RoCe Counters tab selected" width="1100">}}

## Disable RoCE Monitoring

To disable RoCE monitoring:

1. Edit `/etc/netq/commands/cl4-netq-commands.yml` and comment out the following lines:

        cumulus@netq-ts:~$ sudo nano /etc/netq/commands/cl4-netq-commands.yml

        #- period: "60"
        #  key: "roce"
        #  isactive: true
        #  command: "/usr/lib/cumulus/mlxcmd --json roce counters"
        #  parser: "local"

1. Delete the `/var/run/netq/netq_commands.yml` file:

        cumulus@netq-ts:~$ sudo rm /var/run/netq/netq_commands.yml

1. Restart the NetQ Agent:

       cumulus@netq-ts:~$ netq config agent restart

## Related Information

- {{<link title="Threshold-Crossing Events Reference#roce" text="RoCE threshold-crossing events reference">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/" text="RoCE and Cumulus Linux">}}
