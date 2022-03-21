---
title: ONYX Image Uninstall
author: Nvidia
weight: 252
toc: 4
---

If you are migrating from {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/onyx/" text="ONYX">}} to Cumulus Linux, firest you have to uninstall the ONYX image from the switch. 

Follow these step-by-step uninstallation proccess:

1. Login into the ONYX switch and reboot it using the `reload` command

{{< img src = "/images/knowledge-base/onyx-uninstall/onyx-reload.PNG" >}}

2. On switch boot, select the `ONIE: Uninstall OS` from the ONIE grub menu and hit `Enter`

{{< img src = "/images/knowledge-base/onyx-uninstall/onie-uninstall.PNG" >}}

{{%notice note%}}
On very old ONYX versions, which was previously called *MLNX OS*, you may see a different grub menu. In that case, select `ONIE` and hit `Enter`
{{< img src = "/images/knowledge-base/onyx-uninstall/old-onyx.PNG" >}}

You will be prompted to confirm uninstallation, type `YES` and hit `Enter` (similar to the next step). This process could take 60-90 minutes.

{{< img src = "/images/knowledge-base/onyx-uninstall/old-onyx2.PNG" >}}

{{%/notice%}}

3. Once you select the *onie-uninstall os* mode, you will be prompted to confirm the ONYX NOS uninstallation, type `YES` and hit `Enter`

{{< img src = "/images/knowledge-base/onyx-uninstall/onie-yes.PNG" >}}

4. Now, the uninstallation process will start. It could take a few minutes (but usually several seconds). At the end of the process, the switch reboots automatically and will boot into ONIE again.

{{< img src = "/images/knowledge-base/onyx-uninstall/onie-uninstall-start.PNG" >}}

5. Once the switch booted back to the ONIE grub menu, select `ONIE: Install OS` and hit `Enter` (this is an automatic selection)

{{< img src = "/images/knowledge-base/onyx-uninstall/onie-install-os.PNG" >}}

6. After the switch enters into the OS installation mode, it will start the auto-discovery process

{{< img src = "/images/knowledge-base/onyx-uninstall/install mode.PNG" >}}

7. You can stop the process by hitting `Enter` and executing the the `onie-discovery-stop` command

{{< img src = "/images/knowledge-base/onyx-uninstall/discovery stop.PNG" >}}

8. Now, you can follow the Cumulus Linux image installation steps described in the [Installing a New Cumulus Linux Image]({{<ref "/cumulus-linux-50/Installation-Management/Installing-a-New-Cumulus-Linux-Image.md" >}}) page. 

{{%notice info%}}

If the switch was shipped with ONYX from the factory, its platform identifier (PSID) code is restricted to ONYX. Hence only NVIDIA optics will be supported on it. 
Cumulus Linux does not have this restriction, so when migrating ONYX to Cumulus Linux, the PSID must be changed in order to remove this lock and enable all non-NVIDIA optics.</
In future releases, this will be done automatically. For more information and assistance in this proccess, contact NVIDIA support.

{{%/notice%}}

To make the transition from ONYX to NVUE configuration easier, you can use this {{<exlink url="https://air.nvidia.com/migrate/" text="NVUE Migration Tool">}} to convert your ONYX to NVUE configuration by uploading the running-configuration file from ONYX switch.
