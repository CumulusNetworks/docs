---
title: Uninstall the Onyx Image
author: Nvidia
weight: 252
toc: 4
---

If you want to migrate from {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/onyx/" text="Onyx">}} to Cumulus Linux, you must uninstall the ONYX image from the switch before you install Cumulus Linux.

{{%notice info%}}

This uninstallation method is intensive to the disk and should not be undertaken frequently, or the disk's life may be shortened.

{{%/notice%}}

Follow this procedure:

1. Log in to the Onyx switch, then run the `reload` command to reboot the switch.

{{< img src = "/images/knowledge-base/uninstall-onyx/onyx-reload.png" >}}

2. In the grub menu, select `ONIE`

{{< img src = "/images/knowledge-base/uninstall-onyx/2_onyx_ONIE.png" >}}

3. To confirm that you want to uninstall the Onyx network operating system, type `YES` at the prompt, then press `Enter`.

{{< img src = "/images/knowledge-base/uninstall-onyx/3_onyx_uninstall_YES.png" >}}

4. When the switch boots, select `ONIE: Uninstall OS` from the ONIE GRUB menu and press `Enter`.

{{< img src = "/images/knowledge-base/uninstall-onyx/onie-uninstall.png" >}}

5. The uninstallation process starts and can take up to 90 minutes. At the end of the process, the switch reboots automatically, then boots into ONIE again.

{{< img src = "/images/knowledge-base/uninstall-onyx/onie-uninstall-start.png" >}}

6. Select `ONIE: Install OS` and press `Enter`.

{{< img src = "/images/knowledge-base/uninstall-onyx/onie-install-os.png" >}}

7. After the switch enters ONIE: OS Install Mode, the ONIE Service Discovery process starts.

{{< img src = "/images/knowledge-base/uninstall-onyx/install mode.png" >}}

If you need to stop the process, press `Enter` and run the `onie-discovery-stop` command (or `onie-stop` in newer ONIE releases).

{{< img src = "/images/knowledge-base/uninstall-onyx/discovery stop.png" >}}

8. Install the Cumulus Linux image. Refer to [Installing a New Cumulus Linux Image]({{<ref "/cumulus-linux-50/Installation-Management/Installing-a-New-Cumulus-Linux-Image.md" >}}).

{{%notice info%}}

If the switch ships with Onyx from the factory, the platform identifier (PSID) code restricts the switch to Onyx and the switch only supports NVIDIA optics. When migrating from Onyx with version lower than 3.9.2400 to Cumulus Linux, you must change the PSID to remove this lock and enable all non-NVIDIA optics. Moreover, outdated PSID causes physical interfaces not to come up in Cumulus Linux. Also, if the PSID was incorrectly updated, the switch could not be operational at all and will not work without advanced support or even RMA. For more information, contact NVIDIA support.

{{%/notice%}}

To ease the transition from Onyx to NVUE, you can upload the running configuration file from the Onyx switch with this {{<exlink url="https://air.nvidia.com/migrate/" text="NVUE Migration Tool">}}.

<!--


## Advanced Uninstallation Procedure

Another method of Onyx NOS uninstallation is by re-installing ONIE using the *ONIE: Rescue* or *ONIE: Embed ONIE* mode.

{{%notice info%}}

Make sure to involve NVIDIA support or professional services for assistance to perform this method. 

{{%/notice%}}

Follow steps 1-3 showen above. 

4. Select `ONIE: Rescue` or `ONIE: Embed ONIE`. These two options will allow you to re-install ONIE on the switch using the onie-updater file. 

{{< img src = "/images/knowledge-base/uninstall-onyx/4_onyx_ONIE_rescue.png" >}}

{{< img src = "/images/knowledge-base/uninstall-onyx/4_onyx_ONIE_embed.png" >}}

{{%notice note%}}

Place the onie-updater file on a local HTTP/FTP/TFTP server or on the switch itself.

{{%/notice%}}

5. Run the `onie-self-update` with `-e` flag to embed ONIE in the hard disk and select the *onie-updater* file to re-install ONIE.
```
ONIE:/ # onie-self-update -e [path to onie-updater]
```
e.g. 
```
ONIE:/ # onie-self-update -e http://10.1.0.250/onie-updater-x86
ONIE:/ # onie-self-update -e /tmp/onie-updater
```
Once ONIE re-installed and the switch rebooted, continue with steps 6-8 showen above.

-->






