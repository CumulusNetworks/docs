---
title: Digital Optics
author: NVIDIA
weight: 808
toc: 3
---

With the NetQ UI and NetQ CLI, you can monitor the health of digital optics modules, including laser Tx and Rx power, laser bias current, module temperature and voltage, and bit error rates.

## Digital Optics Commands

Use the {{<link title="show/#netq show dom" text="netq show dom">}} commands to monitor performance degradations or outages of any digital optics modules (DOMs) on a given device. The output of the DOM commands indicate if a digital optics module's {{<link title="Threshold-Crossing Events Reference/#digital-optics" text="threshold value ">}} has been crossed:

```
netq [<hostname>] show dom type (laser_rx_power|laser_output_power|laser_bias_current)
netq [<hostname>] show dom type (module_temp|module_voltage)
netq <hostname> show dom ber 
```

## View Digital Optics in the UI

To view digital optics information at the network level, select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then **Digital optics**.

## View Bit Error Rates on a Switch

1. Search for the device’s hostname in the global search field or from the header select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Device card**.

2. Select a switch and navigate to the **Digital optics** tab.

3. Above the table, select **Diagnostic info** to view a list of interfaces with their respective raw and effective bit error rates (BERs):

{{<figure src="/images/netq/dom-ber-413.png" alt="full screen graph of a switch's BER attributes" width="1200">}}

## Related Information

 - {{<link title="Threshold-Crossing Events Reference/#digital-optics" text="Threshold Crossing Rules for Digital Optics">}} 