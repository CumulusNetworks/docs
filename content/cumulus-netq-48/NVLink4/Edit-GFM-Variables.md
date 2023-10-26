---
title: Edit GFM Variables
author: NVIDIA
weight: 1160
toc: 3

---

After creating a new domain, you can manually adjust GFM variables in the fabric manager configuration file, `fabricmanager.cfg`. This section contains an example configuration and a complete reference of variables that you can adjust.

You can only edit domains that have already been created. To get started, {{<link title="Domain Management/#create-a-domain" text="create a domain">}}, then return to this section. 

## Example

In the following example, we'll adjust the `GFM_WAIT_TIMEOUT` variable from 20 seconds to 15 seconds.

1. After creating a new domain, run the following command to display the current configuration. The output indicates that the wait time is currently set to 20 seconds.

```
cumulus@netq-appliance:~$ kubectl exec -it netq-app-nvl4-controller-12-deploy-0 -c gfm  cat /usr/share/nvidia/nvswitch/fabricmanager.cfg | grep GFM
GFM_WAIT_TIMEOUT=20
```

2. On your NetQ server, edit the configuration with the `kubectl edit netqapps netqapps-nvl4` command. In the example below, the `gfm_wait_timeout` variable is adjusted to 15 seconds. Note that this command displays variables in lower case; the same variables are written in upper case in the fabric manager configuration file, `fabricmanager.cfg`.

```
cumulus@netq-appliance:~$ kubectl edit netqapps netqapps-nvl4
domains:
    "12"
        created_by: admin
        domain_name: test
        fabric_configuration_id: 23
        fabric_mode: 0
        gfm_wait_timeout: 15
        log_level: 4
        multi_node_enable_all_node_partition: 0
        opid: 0
        topology_id: 21
```
3. Save the new configuration and exit. Then restart the pods. <!--how????-->

4. Retrieve the pod name with the `kubectl get pods | grep nvl4` command:

```
cumulus@netq-appliance:~$ kubectl get pods | grep nvl4
netq-app-nvl4-controller-12-deploy-0
```
5. Check the fabric manager configuration file, `fabricmanager.cfg`, to confirm that the values updated to reflect the new configuration:
```
$ kubectl exec -it netq-app-nvl4-controller-12-deploy-0 -c gfm  cat /usr/share/nvidia/nvswitch/fabricmanager.cfg | grep GFM
GFM_WAIT_TIMEOUT=15
```
## Variables Reference

```
LOG_LEVEL=${LOG_LEVEL}
Description: Fabric Manager logging levels
Possible Values:
	0  - All the logging is disabled
	1  - Set log level to CRITICAL and above
	2  - Set log level to ERROR and above
	3  - Set log level to WARNING and above
	4  - Set log level to INFO and above

LOG_FILE_NAME=/var/log/fabricmanager.log
Description: Filename for Fabric Manager logs
Possible Values:
    Full path/filename string (max length of 256). Logs will be redirected to console(stderr) if the specified log file can't be opened or the path is empty.

LOG_APPEND_TO_LOG=${LOG_APPEND_TO_LOG}
Description: Append to an existing log file or overwrite the logs
Possible Values:
    0  - No (Log file will be overwritten)
    1  - Yes (Append to existing log)

LOG_FILE_MAX_SIZE=${LOG_FILE_MAX_SIZE}
Description: Max size of log file (in MB)
Possible Values:
	Any integer values

LOG_USE_SYSLOG=${LOG_USE_SYSLOG}
Description: Redirect all the logs to syslog instead of logging to file
Possible Values:
	0  - No
	1  - Yes

DAEMONIZE=${DAEMONIZE}
Description: daemonize Fabric Manager on start-up
Possible Values:
    0  - No (Do not daemonize and run fabric manager as a normal process)
    1  - Yes (Run Fabric Manager process as Unix daemon

BIND_INTERFACE_IP=${BIND_INTERFACE_IP}
Description: Network interface to listen for Global and Local Fabric Manager communication
Possible Values:
	A valid IPv4 address. By default, uses loopback (127.0.0.1) interface

STARTING_TCP_PORT=${STARTING_TCP_PORT}
Description: Starting TCP port number for Global and Local Fabric Manager communication
Possible Values:
	Any value between 0 and 65535

UNIX_SOCKET_PATH=${UNIX_SOCKET_PATH}
Description: Use Unix sockets instead of TCP Socket for Global and Local Fabric Manager communication
Possible Values:
	Unix domain socket path (max length of 256)
Default Value: 
	Empty String (TCP socket will be used instead of Unix sockets)

FABRIC_MODE=${FABRIC_MODE}
Description: Fabric Manager Operating Mode
Possible Values:
    0  - Start Fabric Manager in Bare metal or Full pass through virtualization mode
    1  - Start Fabric Manager in Shared NVSwitch multitenancy mode. 
    2  - Start Fabric Manager in vGPU based multitenancy mode.

FABRIC_MODE_RESTART=${FABRIC_MODE_RESTART}
Description: Restart Fabric Manager after exit. Applicable only in Shared NVSwitch or vGPU based multitenancy mode
Possible Values:
    0  - Start Fabric Manager and follow full initialization sequence
    1  - Start Fabric Manager and follow Shared NVSwitch or vGPU based multitenancy mode resiliency/restart sequence.

STATE_FILE_NAME=${STATE_FILE_NAME}
Description: Specify the filename to be used to save Fabric Manager states. Valid only if Shared NVSwitch or vGPU based multitenancy mode is enabled
Possible Values:
	Full path/filename string (max length of 256)

FM_CMD_BIND_INTERFACE=${FM_CMD_BIND_INTERFACE}
Description: Network interface to listen for Fabric Manager SDK/API to communicate with running FM instance.
Possible Values:
	A valid IPv4 address. By default, uses loopback (127.0.0.1) interface

FM_CMD_PORT_NUMBER=${FM_CMD_PORT_NUMBER}
Description: TCP port number for Fabric Manager SDK/API to communicate with running FM instance.
Possible Values:
	Any value between 0 and 65535

FM_CMD_UNIX_SOCKET_PATH=${FM_CMD_UNIX_SOCKET_PATH}
Description: Use Unix sockets instead of TCP Socket for Fabric Manager SDK/API communication
Possible Values:
		Unix domain socket path (max length of 256)
Default Value: 
		Empty string (TCP socket will be used instead of Unix sockets)


FM_STAY_RESIDENT_ON_FAILURES=${FM_STAY_RESIDENT_ON_FAILURES}
Description: Fabric Manager does not exit when facing failures
Possible Values:
    0 – Fabric Manager service will terminate on errors such as, NVSwitch and GPU config failure, typical software errors, etc.  
    1 – Fabric Manager service will stay running on errors such as, NVSwitch and GPU config failure, typical software errors etc. However, the system will be uninitialized and CUDA application launch will fail. 

ACCESS_LINK_FAILURE_MODE=${ACCESS_LINK_FAILURE_MODE}
Description: Degraded Mode options when there is an Access Link Failure (GPU to NVSwitch NVLink failure)
Possible Values:
    In bare metal or full passthrough virtualization mode
    0  - Remove the GPU with the Access NVLink failure from NVLink P2P capability
    1  - Disable the NVSwitch and its peer NVSwitch, which reduces NVLink P2P bandwidth

    In Shared NVSwitch or vGPU based multitenancy mode
    0  - Disable partitions which are using the Access Link failed GPU
    1  - Disable the NVSwitch and its peer NVSwitch, all partitions will be available but with reduced NVLink P2P bandwidth

TRUNK_LINK_FAILURE_MODE=${TRUNK_LINK_FAILURE_MODE}
Description: Degraded Mode options when there is a Trunk Link Failure (NVSwitch to NVSwitch NVLink failure)
Possible Values:
    In bare metal or full passthrough virtualization mode
    0  - Exit Fabric Manager and leave the system/NVLinks uninitialized
    1  - Disable the NVSwitch and its peer NVSwitch, which reduces NVLink P2P bandwidth

    In Shared NVSwitch or vGPU based multitenancy mode
    0  - Remove partitions that are using the Trunk NVLinks
    1  - Disable the NVSwitch and its peer NVSwitch,
            all partitions will be available but with reduced NVLink P2P bandwidth

NVSWITCH_FAILURE_MODE=${NVSWITCH_FAILURE_MODE}
Description: Degraded Mode options when there is a NVSwitch failure or an NVSwitch is excluded
Possible Values:
    In bare metal or full passthrough virtualization mode
    0  - Abort Fabric Manager
    1  - Disable the NVSwitch and its peer NVSwitch, which reduces P2P bandwidth

    In Shared NVSwitch or vGPU based multitenancy mode
    0  - Disable partitions that are using the NVSwitch
    1  - Disable the NVSwitch and its peer NVSwitch,
           all partitions will be available but with reduced NVLink P2P bandwidth

ABORT_CUDA_JOBS_ON_FM_EXIT=${ABORT_CUDA_JOBS_ON_FM_EXIT}
Description: Control running CUDA jobs behavior when Fabric Manager service is stopped or terminated
Possible Values:
    0  - Do not abort running CUDA jobs when Fabric Manager exits. However new CUDA job launch will fail.
    1  - Abort all running CUDA jobs when Fabric Manager exits.

TOPOLOGY_FILE_PATH=${TOPOLOGY_FILE_PATH}
Description: Absolute directory path containing Fabric Manager topology files
Possible Values:
    A valid directory path string (max length of 256)

ENABLE_LOCALFM=${ENABLE_LOCALFM}

GFM_WAIT_TIMEOUT=${GFM_WAIT_TIMEOUT}
Time in Seconds. Negative value for gfmWaitTimeout denotes an infinite wait time.

ENABLE_TOPOLOGY_VALIDATION=${ENABLE_TOPOLOGY_VALIDATION}

FABRIC_NODE_CONFIG_FILE=/usr/share/nvidia/nvswitch/${FABRIC_NODE_CONFIG}

MULTI_NODE_TOPOLOGY=${MULTI_NODE_TOPOLOGY}
Filename of active multi-node-topology

MULTI_NODE_ENABLE_ALL_NODE_PARTITION=${MULTI_NODE_ENABLE_ALL_NODE_PARTITION}
Description: Indicates that all nodes are by default in a single default partition
Possible Values:
   0 -  No default partition is enabled
   1 -  default partition is enabled

