---
title: NetQ CLI Changes
author: NVIDIA
weight: 20
toc: 4
---

A number of commands have changed in this release to accommodate the addition of new options or to simplify their syntax. Additionally, new commands have been added and others have been removed. A summary of those changes is provided here.

## New Commands

The following table summarizes the new commands available with this release.

| Command | Summary | Version |
| ------- | ------- | ------- |
| netq [&lt;hostname>] show interfaces alias [&lt;remote-interface>] [around &lt;text-time>] [json] | Displays the aliases set for any interfaces on a specific switch or all switches on the network. | 3.3.0 |
| netq config (add\|del) agent wjh-drop-filter drop-type &lt;text-wjh-drop-type> [drop-reasons &lt;text-wjh-drop-reasons>] [severity &lt;text-drop-severity-list>] | Creates a filter for WJH events based on drop type. | 3.3.0 |
| netq lcm discover (ip-range &lt;text-ip-range> \| csv-file &lt;text-csv-file-path>) | Creates a lifecycle management (LCM) switch discovery job. The job searches the specified IP address, range of IP addresses or the switch information listed in the specified CSV file. | 3.3.0 |
| netq lcm add default-version cl-images &lt;text-cumulus-linux-version> | Configure a Cumulus Linux disk image as the default image. | 3.3.0 |
| netq lcm add default-version netq-images &lt;text-netq-version> | Configure a NetQ disk image as the default image. | 3.3.0 |
| netq lcm show default-version cl-images [json] | Displays the default disk image for NVIDIA Cumulus Linux on the NetQ appliance. | 3.3.0 |
| netq lcm show default-version netq-images [json] | Displays the default disk images for the NVIDIA NetQ agent and CLI on the NetQ appliance. | 3.3.0 |
| netq lcm show discovery-job &lt;text-discovery-job-id> [json] | Displays the results of a switch discovery job, including a summary of the job itself and information about any switches discovered, including hostname, IP address, MAC address, CPU, Cumulus Linux and NetQ versions, configuration profile, discovery status and upgrade status. | 3.3.0 |
| netq lcm upgrade netq-image name &lt;text-job-name> [netq-version &lt;text-netq-version>] <!-- vale off -->[upgrade-cli True \| upgrade-cli False] <!-- vale on -->hostnames &lt;text-switch-hostnames> [config_profile &lt;text-config-profile>] | Upgrades NetQ. | 3.3.0 |
| netq lcm show netq-config [json] | Displays the NetQ LCM configuration profiles. | 3.3.0 |

## Modified Commands

The following table summarizes the commands that have been changed with this release.

| Updated Command | Old Command | What Changed | Version |
| --------------- | ----------- | ------------ | ------- |
| netq lcm upgrade [cl-image] name &lt;text-job-name> cl-version &lt;text-cumulus-linux-version> netq-version &lt;text-netq-version> hostnames &lt;text-switch-hostnames> [run-restore-on-failure] [run-before-after] | netq lcm upgrade name &lt;text-job-name> cl-version &lt;text-cumulus-linux-version> netq-version &lt;text-netq-version> hostnames &lt;text-switch-hostnames> [run-restore-on-failure] [run-before-after] | Added ability to optionally specify an NVIDIA Cumulus Linux disk image. | 3.3.0 |
| netq lcm show status cl-image &lt;text-lcm-job-id> [json]<br />netq lcm show status netq-image &lt;text-netq-upgrade-job-id> [json] | netq lcm show status &lt;text-lcm-job-id> [json] | Added ability to show only Cumulus Linux or NetQ upgrade jobs. | 3.3.0 |
| netq lcm add netq-image &lt;text-netq-image-path> | netq lcm add netq-image &lt;text-image-path> | Changed variable name from `<text-image-path>` to `<text-netq-image-path>.` | 3.3.0 |
| netq lcm del cl-image &lt;text-image-id> <br />netq lcm del netq-image &lt;text-image-id> | netq lcm del image &lt;text-image-id> | Changed command option from `image` to `cl-image` or `netq-image` to specify a Cumulus Linux or NetQ image to delete. | 3.3.0 |
| netq lcm show cl-images [&lt;text-image-id>] [json]<br />netq lcm show netq-images [&lt;text-image-id>] [json] | netq lcm show images [&lt;text-image-id>] [json] | Changed command option from `images` to `cl-images` or `netq-images`, depending on whether you want to show a Cumulus Linux or NetQ disk image. | 3.3.0 |
| netq lcm show upgrade-jobs cl-image [json]<br/>netq lcm show upgrade-jobs netq-image [json] | netq lcm show upgrade-jobs [json] | Added ability to specify a Cumulus Linux or NetQ upgrade job. | 3.3.0 |
