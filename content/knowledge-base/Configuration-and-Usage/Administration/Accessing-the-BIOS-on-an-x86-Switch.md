---
title: Accessing the BIOS on an x86 Switch
author: NVIDIA
weight: 317
toc: 4
---

For x86 switches, if you need to access the BIOS, use the following steps (for example, if you need to change the serial console baud rate in the BIOS, if your switch's default rate is different than the Cumulus Linux default of 115200).

The procedure varies with the switch manufacturer, so follow the appropriate steps for your switch.

## Accessing the BIOS on a Dell S6000 Switch

You might need to access the BIOS on a Dell S6000 switch because you want to access the BIOS over the [serial console]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/#configure-the-serial-console-on-x86-switches" >}}). To do so, you need to adjust the baud rate of the console in the BIOS, because it differs from the Cumulus Linux default baud rate of 115200.

To access the BIOS on a Dell S6000 switch, complete the following steps:

1. Power on the switch. Enter the BIOS setup by pressing the *\<del\>* key from a Windows console, or *fn+delete* from a Mac console. Your screen should look like this:  

   {{<img src="/images/knowledge-base/access-x86-bios-dellS6000-bios.png" alt="Aptio BIOS screen">}}

2. To configure the serial console, choose **Advanced** > **Serial Port Console Redirection** > **COM0_Console Redirection Settings** and set **Bits per second** to _115200_.

3. Reboot the switch and adjust your console server to the new baud rate.
