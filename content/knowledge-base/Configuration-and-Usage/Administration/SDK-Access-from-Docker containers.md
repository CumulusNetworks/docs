---
title: SDK Access from Docker Containers
author: NVIDIA
weight: 320
toc: 4
---
Because Cumulus Linux is Linux, you can install and run containers on the system with full access to popular container management ecosystems. As long as system memory, storage, and CPU capacities are proportional to the application needs, there are no limitations. To protect the primary functions of the system (such as network control and dataplane) from resource contention with other applications, you can define resource caps.

To install the Docker engine, refer to [Docker on Cumulus Linux]({{<ref "/cumulus-linux-43/Network-Solutions/Docker-on-Cumulus-Linux" >}}).

{{%notice note%}}
The Docker engine installation procedure depends on the Cumulus Linux release you are running. For an NVIDIA Spectrum switch running Cumulus Linux 4.3.0 and later, the installation or upgrade process installs a Docker package. The Docker package includes Docker Engine, and dependencies and configuration files required to run the Docker service.
{{%/notice%}}

## Applications that Require Integration with the Networking Dataplane

Two main classes of applications require integration with the networking dataplane:

- Applications that interact with the system through standard interfaces; for example, installing routes or ACLs in the Linux kernel through `netlink` or command lines (Linux tools such as `iproute2`). `switchd` offloads the kernel dataplane settings      to the ASIC. Using standard interfaces allows for more portable applications.
- Applications that require more native access to the forwarding ASIC through the ASIC SDK to access hardware capabilities that are not exposed through the Linux kernel and other standard interfaces.

## Direct Application Access to the ASIC SDK

The NVIDIA Spectrum `sx_sdk` is a standalone process, which supports access from multiple application clients simultaneously through the `sx_api` library with IPC communications. For a containerized application to get access to the SDK, you need to make the `sx_api` and a few other files available to the container while the SDK process continues to run natively on the container host.

Cumulus Linux provides two options. You can either:
- Copy the required files to the container at runtime.
- Patch the container image.

### Copy Files to the Container at Runtime

To copy the necessary files to the container at runtime, follow these steps:

1. Start the container.

   - Specify the bind mount points.
   - If you need to expose all the Linux interfaces to the application, start the container with the `–net=host` option.
   - If you are using the `sx_api_xxx` python scripts that come with the SDK installation, include the `PYTHONPATH` environment setting.

   ```
   cumulus@switch:mgmt:~$ sudo docker run -d --name=myapp -it --net=host --mount type=bind,source=/var/run/sx_api.sock,target=/var/run/sx_api.sock --mount type=bind,source=/dev/shm/dpt,target=/dev/shm/dpt --mount type=bind,source=/dev/shm/wjh_acl,target=/dev/shm/wjh_acl --mount type=bind,source=/dev/shm/lag,target=/dev/shm/lag --env PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages myimage
   ```

2. Copy the required files to the container by running a script called `sdk_prep`:

   ```
   cumulus@switch:mgmt:~$ sudo ./sdk_prep myapp
   #!/bin/bash
   DOCKER_TMP_DIR=/tmp/docker-prep
   test -f $DOCKER_TMP_DIR || mkdir -p $DOCKER_TMP_DIR || (echo "Failed to create prep directory" && exit)
   cp -P --parents /usr/bin/sx*.py ${DOCKER_TMP_DIR}
   cp -P --parents /usr/bin/test_infra_common.py ${DOCKER_TMP_DIR}
   cp -RP --parents /usr/lib/python2.7/dist-packages/python_sdk_api/ ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libsx* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libsdk* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libsw* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libpolicer* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libbridge* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/librouter* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libcraccess* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libautoreg* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libwjh* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/lib/libscew* ${DOCKER_TMP_DIR}
   cp -P --parents /usr/etc/wjh_lib_conf.xml ${DOCKER_TMP_DIR}
   cp -P --parents /usr/sbin/ip ${DOCKER_TMP_DIR}
   # copy files to container's / (name given in $1)
   docker cp $DOCKER_TMP_DIR/* $1:/
   rm -r $DOCKER_TMP_DIR
   ```

3. Verify SDK access from the container:

   ```
   cumulus@switch:mgmt:~$ sudo docker exec -it myapp sx_api_port.py
   [+] opening sdk
   sx_api_open handle:0x55b1a7fab824 , rc 0
   [0x16100, 0x16200, 0x16300, 0x16400, 0x16500, 0x16600, 0x16700, 0x16800]
   sx_api_port_init_set log_port 0x16100 , rc 0
   sx_api_port_swid_list_get swid_cnt:1 , rc 0, swid table:
   [0] swid 0
   sx_api_port_swid_port_list_get port_cnt:38 , rc 0, port table:
   [0] port 0x10100
   [1] port 0x10500
   [2] port 0x10900
   [3] port 0x10d00
   [4] port 0x11100
   ```

### Patch the Container Image

You can write the SDK files to the container image. However, you might need to patch the container again when there is an SDK upgrade.

## Exclusive SDK access to the Container

The above workflow assumes `switchd` continues to run on the system, and `switchd` and the containerized application both share SDK access.

One advantage of this shared access arrangement is that Cumulus Linux and `switchd` take care of SDK initialization, including linux interface creation, hardware port breakout, and full forwarding ASIC initialization. Cumulus Linux can continue to handle all network configuration and forwarding ASIC programming, while the container application focuses on specific use cases and specific ASIC resource management, such as installing ACL rules.

One disadvantage of this shared access arrangement is that if the application needs to write to the same ASIC resources that `switchd` needs to access, potential conflicts can arise. It might be possible to compartmentalize some resources (ACL regions), but this is not possible for all resources.

If you require exclusive SDK access for the containerized application, you must disable `switchd` and `update-ports` services on Cumulus Linux so that the application is fully responsible for handling Linux interface life cycle, port breakout, and ASIC initialization.

```
cumulus@switch:mgmt:~$ sudo systemctl disable switchd.service
Removed /etc/systemd/system/basic.target.wants/switchd.service.
[Sep-18-00:18:20] cumulus@mlx-3700c-51:~# sudo systemctl disable update-ports.service
Removed /etc/systemd/system/basic.target.wants/update-ports.service.
Removed /etc/systemd/system/switchd.service.wants/update-ports.service.
```

## Security Considerations

With Cumulus Linux, an administrator has full access to all the security measures and tools that are available in the container ecosystems to secure containers and protect the container host. For example, the docker daemon architecture allows for an authorization plugin that can provide fine grain capability and access control to what a container can and cannot do. One such plugin provider is {{<exlink url="https://www.openpolicyagent.org/docs/latest/docker-authorization/" text="Open Policy Agent">}}.

A configuration like the one below, together with an enabled authorization plugin in the `docker.conf` file, ensures no container can run with the `–privilege` option:

```
cumulus@switch:mgmt:~$ cat /etc/docker/policies/authz.rego
package docker.authz

default allow = false

allow {
  not deny
}

deny {
   privileged_access
}

privileged_access {
   input.Body.HostConfig.Privileged == true
}
```

```
cumulus@switch:mgmt:~$ cat /etc/docker/daemon.json
{
   "iptables": false,
   "ip-forward": false,
   "ip-masq": false,
   "exec-opts": ["native.cgroupdriver=systemd"],
   "authorization-plugins": ["openpolicyagent/opa-docker-authz-v2:0.4"]
}
```

```
cumulus@switch:mgmt:~$ sudo docker run -d --name=myapp -it --net=host --privileged python:2
docker: Error response from daemon: authorization denied by plugin openpolicyagent/opa-docker-authz-v2:0.4: request rejected by administrative policy.
```
