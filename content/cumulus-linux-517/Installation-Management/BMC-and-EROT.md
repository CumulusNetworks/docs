---
title: BMC and eRoT
author: NVIDIA
weight: 62
toc: 3
draft: true
---
The Spectrum-6 switch requires you to install the <span class="a-tooltip">[BMC](## "Baseboard Management Controller")</span> and <span class="a-tooltip">[eRoT](## "Embedded Root of Trust")</span> components.
- BMC is a dedicated microcontroller on the switch motherboard that provides out-of-band management so that you can monitor and control the switch even when the main CPU or OS is down.
- eRoT is the hardware security component that guarantees that only signed images can boot and that the update process is secure, and provides key revocation and device attestation.

To download BMC and eRoT on a Spectrum-6 switch:

1. Go to ADD WEBSITE HERE

2. Download ....

3. ???

After downloading both components, follow the steps below to install them on the switch.

To install BMC and eRoT:

1. Create a `updparameters.json` file with the following contents:

   ```
   {
       "Targets" :["/redfish/v1/UpdateService/FirmwareInventory/EROT_BMC_0"]
   }
   ```

2. Update the firmware with the following command:

   ```
   nvfwupd -t ip=<bmc-ip-address> user=admin password=admin update_fw \
     -p nvfw_DGX_251212.1.0.fwpkg -y -s updparameters.json
   ```

   Example Output:

   ```
   FW recipe: ['nvfw_DGX_251212.1.0.fwpkg]
   {"@odata.type": "#UpdateService.v1_6_0.UpdateService", "Messages": [{"@odata.type": "#Message.v1_0_8.Message",    "Message": "A new task /redfish/v1/TaskService/Tasks/1 was created.", "MessageArgs": ["/redfish/v1/TaskService/Tasks/   1"], "MessageId": "Task.1.0.New", "Resolution": "None", "Severity": "OK"}, {"@odata.type": "#Message.v1_0_8.   Message", "Message": "The action UpdateService.MultipartPush was submitted to do firmware update.", "MessageArgs":    ["UpdateService.MultipartPush"], "MessageId": "UpdateService.1.0.StartFirmwareUpdate", "Resolution": "None",    "Severity": "OK"}]}
    FW update started, Task Id: 1
   Wait for Firmware Update to Start...
   Wait for Firmware Update to Start...
    TaskState: Completed
    PercentComplete: 100
    TaskStatus: OK
   Firmware update successful!
    Overall Time Taken: 0:00:09
   Refer to 'DGX H100 Firmware Update Document' on activation steps for new firmware to take effect.
   ```

3. Perform an AC power cycle on the system:

   a. Ensure the chassis is powered off from the BMC.

   b. Unplug all power supplies for five to six minutes to allow the power to drain.

   c. Reconnect the power supplies (manually or through an external PDU).
