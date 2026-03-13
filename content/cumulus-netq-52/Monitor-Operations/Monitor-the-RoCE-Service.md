---
title: RoCE
author: NVIDIA
weight: 940
toc: 3
---

Use the UI or CLI to monitor RDMA over Converged Ethernet (RoCE) for Spectrum switches and BlueField DPUs.

{{%notice note%}}
NetQ supports RoCE lossless and lossy modes; NetQ monitoring and validation checks do not support the single shared buffer mode, `lossless-single-ipool`.
{{%/notice%}}


## RoCE Commands

- {{<link title="show/#netq-show-roce-config" text="netq show roce-config">}}
- {{<link title="show/#netq-show-roce-counters" text="netq show roce-counters">}}
- {{<link title="show/#netq-show-events" text="netq show events message_type roceconfig">}}
- {{<link title="show/#netq-show-events" text="netq show events message_type tca_roce">}}
- {{<link title="show/#netq-show-events-config" text="netq show events-config message_type roceconfig">}}
- {{<link title="check/#netq check roce" text="netq check roce">}} 


## View RoCE Counters Networkwide in the UI

**RoCE switches** displays transmit (Tx) and receive (Rx) counters as well as counter pools for all switches running RoCE in your network. **RoCE DPUs** displays physical port, priority port, RoCE extended, RoCE, and peripheral component interconnect (PCI) information for all DPUs running RoCE in your network.

1. From the header or {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu, select **Spectrum-X**, then **RoCE**.

2. Select either **RoCE switches** or **RoCE DPUs**. The following displays a list of all switches running RoCE across a network.

{{<figure src="/images/netq/roce-switches-413.png" alt="" width="1100">}}


## View RoCE Counters for a Given Switch

You can view the following RoCE counters for a given switch:

- Receive and transmit counters
- General, CNP, and RoCE-specific counters
- Counter pools
- Port-specific counters

To view RoCE counters on a switch, search for the device’s hostname in the global search field or from the header select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Device card**. Select a switch that is running RoCE and open the large card on your workbench. Click the {{<img src="/images/netq/roce-icon.svg" width="18px">}} **RoCE** tab to view RoCE counters and their associated ports:

{{<figure src="/images/netq/roce-isr1-413.png" alt="switch card displaying RoCE transmit nd receive data" width="500">}}

Expand the card to the largest size, then select **RoCE counters** from the side menu. Use the controls above the table to view, filter, or export counter statistics by Rx, Tx, or Pool.

## Disable RoCE Monitoring

To disable RoCE monitoring:

1. (Optional) Verify that the NetQ agent is monitoring the RoCE service with `netq config show agent commands`. The `Active` column displays a `yes` status for the following services if RoCE monitoring is enabled:

```
nvidia@switch:~$ sudo netq config show agent commands
Service Key               Period  Active       Command                                                        Timeout
-----------------------  --------  --------  --------------------------------------------------------------  ---------
roce                           60  yes        Netq Predefined Command                                         None
roce-config                   300  yes        Netq Predefined Command                                         None
nvue-roce-config              300  yes        Netq Predefined Command                                         None
```

2. Disable each of the three RoCE service keys individually with `netq config add agent command service-key`:

```
nvidia@switch~$ sudo netq config add agent command service-key roce enable False
Command Service roce is disabled
nvidia@switch:~$ sudo netq config add agent command service-key roce-config enable False
Command Service roce-config is disabled
nvidia@switch:~$ sudo netq config add agent command service-key nvue-roce-config enable False
Command Service nvue-roce-config is disabled
```
<!--does the user need to restart the NetQ Agent?-->

3. Verify that NetQ is no longer monitoring the RoCE service with `netq config show agent commands`. The `Active` column displays a `no` status for the disabled services:

```
nvidia@switch:~$ sudo netq config show agent commands
Service Key               Period  Active       Command                                                        Timeout
-----------------------  --------  --------  --------------------------------------------------------------  ---------
roce                           60  no         Netq Predefined Command                                         None
roce-config                   300  no         Netq Predefined Command                                         None
nvue-roce-config              300  no         Netq Predefined Command                                         None
```


## Related Information

- {{<link title="Threshold-Crossing Events Reference#roce" text="RoCE threshold-crossing events reference">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/" text="RoCE and Cumulus Linux">}}
