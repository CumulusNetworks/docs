---
title: Monitor Container Environments
author: Cumulus Networks
weight: 47
aliases:
 - /display/NETQ/Monitor+Container+Environments
 - /pages/viewpage.action?pageId=10456368
pageID: 10456368
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
The NetQ Agent monitors container environments the same way it monitors
[physical
servers](/cumulus-netq/Cumulus_NetQ_CLI_User_Guide/Monitor_Linux_Hosts).
There is no special implementation. The NetQ Agent pulls data from the
container as it would pull data from a Cumulus Linux switch or Linux
host. It can be installed on a Linux server or in a Linux VM. NetQ Agent
integrates with the Kubernetes container orchestrator.

NetQ monitors many aspects of containers on your network, including
their:

  - **Identity**: The NetQ agent tracks every container's IP and MAC
    address, name, image, and more. NetQ can locate containers across
    the fabric based on a container's name, image, IP or MAC address,
    and protocol and port pair.

  - **Port mapping on a network**: The NetQ agent tracks protocol and
    ports exposed by a container. NetQ can identify containers exposing
    a specific protocol and port pair on a network.

  - **Connectivity**: NetQ can provide information on network
    connectivity for a container, including adjacency, and can identify
    containers that can be affected by a top of rack switch.

NetQ helps answer questions such as:

  - Where is this container located?

  - Open ports? What image is being used?

  - Which containers are part of this service? How are they connected?

## <span>Use NetQ with Kubernetes Clusters</span>

The NetQ Agent interfaces with a Kubernetes API server and listens to
Kubernetes events. The NetQ Agent monitors network identity and physical
network connectivity of Kubernetes resources like Pods, Daemon sets,
Service, and so forth. NetQ works with any container network interface
(CNI), such as Calico or Flannel.

The NetQ Kubernetes integration enables network administrators to:

  - Identify and locate pods, deployment, replica-set and services
    deployed within the network using IP, name, label, and so forth.

  - Track network connectivity of all pods of a service, deployment and
    replica set.

  - Locate what pods have been deployed adjacent to a top of rack (ToR)
    switch.

  - Check what pod, services, replica set or deployment can be impacted
    by a specific ToR switch.

NetQ also helps network administrators identify changes within a
Kubernetes cluster and determine if such changes had an adverse effect
on the network performance (caused by a noisy neighbor for example).
Additionally, NetQ helps the infrastructure administrator determine how
Kubernetes workloads are distributed within a network.

### <span>Requirements</span>

The NetQ Agent supports Kubernetes version 1.9.2 or later.

Due to the higher memory requirements to run containers, Cumulus
Networks recommends you run the NetQ Platform on a host with at least
64G RAM.

### <span>Command Summary</span>

There is a large set of commands available to monitor Kubernetes
configurations, including the ability to monitor clusters, nodes,
daemon-set, deployment, pods, replication, and services. Run `netq show
kubernetes help` to see all the possible commands:

    netq [<hostname>] show kubernetes cluster [name <kube-cluster-name>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes node [components] [name <kube-node-name>] [cluster <kube-cluster-name> ] [label <kube-node-label>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] connectivity [around <text-time>] [json]
    netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] connectivity [around <text-time>] [json]
    netq [<hostname>] show kubernetes pod [name <kube-pod-name>] [cluster <kube-cluster-name> ] [namespace <namespace>] [label <kube-pod-label>] [pod-ip <kube-pod-ipaddress>] [node <kube-node-name>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes replication-controller [name <kube-rc-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rc-label>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] connectivity [around <text-time>] [json]
    netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] [around <text-time>] [json]
    netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] connectivity [around <text-time>] [json]
    netq <hostname> show impact kubernetes service [master <kube-master-node>] [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] [around <text-time>] [json]
    netq <hostname> show impact kubernetes replica-set [master <kube-master-node>] [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] [around <text-time>] [json]
    netq <hostname> show impact kubernetes deployment [master <kube-master-node>] [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] [around <text-time>] [json]
    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor
    netq config show agent kubernetes-monitor [json]

### <span id="src-10456368_MonitorContainerEnvironments-enable_k8s" class="confluence-anchor-link"></span><span>Enable Kubernetes Monitoring</span>

For NetQ to monitor the containers on a host, you must configure the
following on the Kubernetes master node:

1.  Configure the host to point to the NetQ Platform by its IP address.
    See the [Install NetQ (2.1.0
    version)](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=10456209)
    topic for details.

2.  Enable Kubernetes monitoring by NetQ. You can specify a polling
    period between 10 and 120 seconds; 15 seconds is the default.
    
        cumulus@host:~$ netq config add agent kubernetes-monitor poll-period 20
        Successfully added kubernetes monitor. Please restart netq-agent.

3.  Restart the NetQ agent:
    
        cumulus@server01:~$ netq config restart agent

Next, you must enable the NetQ Agent on all the worker nodes, as
described in the [Install
NetQ](https://docs.cumulusnetworks.com/display/NETQ140DRAFT/Install+NetQ)
topic, for complete insight into your container network.

### <span>View Status of Kubernetes Clusters</span>

You can get the status of all Kubernetes clusters in the fabric using
the `netq show kubernetes cluster` command:

    cumulus@switch:~$ netq show kubernetes cluster 
    Matching kube_cluster records:
    Master                   Cluster Name     Controller Status    Scheduler Status Nodes
    ------------------------ ---------------- -------------------- ---------------- --------------------
    server11:3.0.0.68        default          Healthy              Healthy          server11 server13 se
                                                                                    rver22 server11 serv
                                                                                    er12 server23 server
                                                                                    24
    server12:3.0.0.69        default          Healthy              Healthy          server12 server21 se
                                                                                    rver23 server13 serv
                                                                                    er14 server21 server
                                                                                    22

To filter the list, you can specify the hostname of the master before
the `show` command:

    cumulus@switch:~$ netq server11 show kubernetes cluster
    Matching kube_cluster records:
    Master                   Cluster Name     Controller Status    Scheduler Status Nodes
    ------------------------ ---------------- -------------------- ---------------- --------------------
    server11:3.0.0.68        default          Healthy              Healthy          server11 server13 se
                                                                                    rver22 server11 serv
                                                                                    er12 server23 server
                                                                                    24

Optionally, you can output the results in JSON format:

    cumulus@server11:~$ netq show kubernetes cluster json
    {
        "kube_cluster":[
            {
                "clusterName":"default",
                "schedulerStatus":"Healthy",
                "master":"server12:3.0.0.69",
                "nodes":"server12 server21 server23 server13 server14 server21 server22",
                "controllerStatus":"Healthy"
            },
            {
                "clusterName":"default",
                "schedulerStatus":"Healthy",
                "master":"server11:3.0.0.68",
                "nodes":"server11 server13 server22 server11 server12 server23 server24",
                "controllerStatus":"Healthy"
        }
        ],
        "truncatedResult":false
    }

### <span>View Changes to a Cluster</span>

If data collection from the NetQ Agents is not occurring as it once was,
you can verify that no changes have been made to the Kubernetes cluster
configuration using the *around* keyword. This example shows the changes
that have been made in the last hour.

    cumulus@server11:~$ netq show kubernetes cluster around 1h 
    Matching kube_cluster records:
    Master                   Cluster Name     Controller Status    Scheduler Status Nodes                                    DBState  Last changed
    ------------------------ ---------------- -------------------- ---------------- ---------------------------------------- -------- -------------------------
    server11:3.0.0.68        default          Healthy              Healthy          server11 server13 server22 server11 serv Add      Fri Feb  8 01:50:50 2019
                                                                                    er12 server23 server24
    server12:3.0.0.69        default          Healthy              Healthy          server12 server21 server23 server13 serv Add      Fri Feb  8 01:50:50 2019
                                                                                    er14 server21 server22
    server12:3.0.0.69        default          Healthy              Healthy          server12 server21 server23 server13      Add      Fri Feb  8 01:50:50 2019
    server11:3.0.0.68        default          Healthy              Healthy          server11                                 Add      Fri Feb  8 01:50:50 2019
    server12:3.0.0.69        default          Healthy              Healthy          server12                                 Add      Fri Feb  8 01:50:50 2019

<span style="color: #36424a;">  
View Kubernetes Pod Information </span>

You can show configuration and status of the pods in a cluster,
including the names, labels, addresses, associated cluster and
containers, and whether the pod is running. This example shows pods for
FRR, Nginx, Calico, various Kubernetes components sorted by master node.

    cumulus@server11:~$ netq show kubernetes pod 
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    server11:3.0.0.68        default      cumulus-frr-8vssx    3.0.0.70         server13     pod-template-generat Running  cumulus-frr:f8cac70bb217 Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server11:3.0.0.68        default      cumulus-frr-dkkgp    3.0.5.135        server24     pod-template-generat Running  cumulus-frr:577a60d5f40c Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server11:3.0.0.68        default      cumulus-frr-f4bgx    3.0.3.196        server11     pod-template-generat Running  cumulus-frr:1bc73154a9f5 Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server11:3.0.0.68        default      cumulus-frr-gqqxn    3.0.2.5          server22     pod-template-generat Running  cumulus-frr:3ee0396d126a Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server11:3.0.0.68        default      cumulus-frr-kdh9f    3.0.3.197        server12     pod-template-generat Running  cumulus-frr:94b6329ecb50 Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server11:3.0.0.68        default      cumulus-frr-mvv8m    3.0.5.134        server23     pod-template-generat Running  cumulus-frr:b5845299ce3c Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server11:3.0.0.68        default      httpd-5456469bfd-bq9 10.244.49.65     server22     app:httpd            Running  httpd:79b7f532be2d       Fri Feb  8 01:50:50 2019
                                          zm
    server11:3.0.0.68        default      influxdb-6cdb566dd-8 10.244.162.128   server13     app:influx           Running  influxdb:15dce703cdec    Fri Feb  8 01:50:50 2019
                                          9lwn
    server11:3.0.0.68        default      nginx-8586cf59-26pj5 10.244.9.193     server24     run:nginx            Running  nginx:6e2b65070c86       Fri Feb  8 01:50:50 2019
    server11:3.0.0.68        default      nginx-8586cf59-c82ns 10.244.40.128    server12     run:nginx            Running  nginx:01b017c26725       Fri Feb  8 01:50:50 2019
    server11:3.0.0.68        default      nginx-8586cf59-wjwgp 10.244.49.64     server22     run:nginx            Running  nginx:ed2b4254e328       Fri Feb  8 01:50:50 2019
    server11:3.0.0.68        kube-system  calico-etcd-pfg9r    3.0.0.68         server11     k8s-app:calico-etcd  Running  calico-etcd:f95f44b745a7 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:142071906
                                                                                             5
    server11:3.0.0.68        kube-system  calico-kube-controll 3.0.2.5          server22     k8s-app:calico-kube- Running  calico-kube-controllers: Fri Feb  8 01:50:50 2019
                                          ers-d669cc78f-4r5t2                                controllers                   3688b0c5e9c5
    server11:3.0.0.68        kube-system  calico-node-4px69    3.0.2.5          server22     k8s-app:calico-node  Running  calico-node:1d01648ebba4 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:da350802a3d2
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  calico-node-bt8w6    3.0.3.196        server11     k8s-app:calico-node  Running  calico-node:9b3358a07e5e Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:d38713e6fdd8
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  calico-node-gtmkv    3.0.3.197        server12     k8s-app:calico-node  Running  calico-node:48fcc6c40a6b Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:f0838a313eff
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  calico-node-mvslq    3.0.5.134        server23     k8s-app:calico-node  Running  calico-node:7b361aece76c Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:f2da6bc36bf8
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  calico-node-sjj2s    3.0.5.135        server24     k8s-app:calico-node  Running  calico-node:6e13b2b73031 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:fa4b2b17fba9
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  calico-node-vdkk5    3.0.0.70         server13     k8s-app:calico-node  Running  calico-node:fb3ec9429281 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:b56980da7294
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  calico-node-zzfkr    3.0.0.68         server11     k8s-app:calico-node  Running  calico-node:c1ac399dd862 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:60a779fdc47a
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  etcd-server11        3.0.0.68         server11     tier:control-plane c Running  etcd:dde63d44a2f5        Fri Feb  8 01:50:50 2019
                                                                                             omponent:etcd
    server11:3.0.0.68        kube-system  kube-apiserver-hostd 3.0.0.68         server11     tier:control-plane c Running  kube-apiserver:0cd557bbf Fri Feb  8 01:50:50 2019
                                          -11                                                omponent:kube-apiser          2fe
                                                                                             ver
    server11:3.0.0.68        kube-system  kube-controller-mana 3.0.0.68         server11     tier:control-plane c Running  kube-controller-manager: Fri Feb  8 01:50:50 2019
                                          ger-server11                                       omponent:kube-contro          89b2323d09b2
                                                                                             ller-manager
    server11:3.0.0.68        kube-system  kube-dns-6f4fd4bdf-p 10.244.34.64     server23     k8s-app:kube-dns     Running  dnsmasq:284d9d363999 kub Fri Feb  8 01:50:50 2019
                                          lv7p                                                                             edns:bd8bdc49b950 sideca
                                                                                                                           r:fe10820ffb19
    server11:3.0.0.68        kube-system  kube-proxy-4cx2t     3.0.3.197        server12     k8s-app:kube-proxy p Running  kube-proxy:49b0936a4212  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-proxy-7674k     3.0.3.196        server11     k8s-app:kube-proxy p Running  kube-proxy:5dc2f5fe0fad  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-proxy-ck5cn     3.0.2.5          server22     k8s-app:kube-proxy p Running  kube-proxy:6944f7ff8c18  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-proxy-f9dt8     3.0.0.68         server11     k8s-app:kube-proxy p Running  kube-proxy:032cc82ef3f8  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-proxy-j6qw6     3.0.5.135        server24     k8s-app:kube-proxy p Running  kube-proxy:10544e43212e  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-proxy-lq8zz     3.0.5.134        server23     k8s-app:kube-proxy p Running  kube-proxy:1bcfa09bb186  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-proxy-vg7kj     3.0.0.70         server13     k8s-app:kube-proxy p Running  kube-proxy:8fed384b68e5  Fri Feb  8 01:50:50 2019
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-scheduler-hostd 3.0.0.68         server11     tier:control-plane c Running  kube-scheduler:c262a8071 Fri Feb  8 01:50:50 2019
                                          -11                                                omponent:kube-schedu          3cb
                                                                                             ler
    server12:3.0.0.69        default      cumulus-frr-2gkdv    3.0.2.4          server21     pod-template-generat Running  cumulus-frr:25d1109f8898 Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server12:3.0.0.69        default      cumulus-frr-b9dm5    3.0.3.199        server14     pod-template-generat Running  cumulus-frr:45063f9a095f Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server12:3.0.0.69        default      cumulus-frr-rtqhv    3.0.2.6          server23     pod-template-generat Running  cumulus-frr:63e802a52ea2 Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server12:3.0.0.69        default      cumulus-frr-tddrg    3.0.5.133        server22     pod-template-generat Running  cumulus-frr:52dd54e4ac9f Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server12:3.0.0.69        default      cumulus-frr-vx7jp    3.0.5.132        server21     pod-template-generat Running  cumulus-frr:1c20addfcbd3 Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server12:3.0.0.69        default      cumulus-frr-x7ft5    3.0.3.198        server13     pod-template-generat Running  cumulus-frr:b0f63792732e Fri Feb  8 01:50:50 2019
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    server12:3.0.0.69        kube-system  calico-etcd-btqgt    3.0.0.69         server12     k8s-app:calico-etcd  Running  calico-etcd:72b1a16968fb Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:142071906
                                                                                             5
    server12:3.0.0.69        kube-system  calico-kube-controll 3.0.5.132        server21     k8s-app:calico-kube- Running  calico-kube-controllers: Fri Feb  8 01:50:50 2019
                                          ers-d669cc78f-bdnzk                                controllers                   6821bf04696f
    server12:3.0.0.69        kube-system  calico-node-4g6vd    3.0.3.198        server13     k8s-app:calico-node  Running  calico-node:1046b559a50c Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:0a136851da17
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    server12:3.0.0.69        kube-system  calico-node-4hg6l    3.0.0.69         server12     k8s-app:calico-node  Running  calico-node:4e7acc83f8e8 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:a26e76de289e
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    server12:3.0.0.69        kube-system  calico-node-4p66v    3.0.2.6          server23     k8s-app:calico-node  Running  calico-node:a7a44072e4e2 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:9a19da2b2308
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    server12:3.0.0.69        kube-system  calico-node-5z7k4    3.0.5.133        server22     k8s-app:calico-node  Running  calico-node:9878b0606158 Fri Feb  8 01:50:50 2019
                                                                                             pod-template-generat          install-cni:489f8f326cf9
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    ...

You can filter this information to focus on a particular pod:

    cumulus@server11:~$ netq show kubernetes pod node server11
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    server11:3.0.0.68        kube-system  calico-etcd-pfg9r    3.0.0.68         server11     k8s-app:calico-etcd  Running  calico-etcd:f95f44b745a7 2d:14h:0m:59s
                                                                                             pod-template-generat
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:142071906
                                                                                             5
    server11:3.0.0.68        kube-system  calico-node-zzfkr    3.0.0.68         server11     k8s-app:calico-node  Running  calico-node:c1ac399dd862 2d:14h:0m:59s
                                                                                             pod-template-generat          install-cni:60a779fdc47a
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    server11:3.0.0.68        kube-system  etcd-server11        3.0.0.68         server11     tier:control-plane c Running  etcd:dde63d44a2f5        2d:14h:1m:44s
                                                                                             omponent:etcd
    server11:3.0.0.68        kube-system  kube-apiserver-serve 3.0.0.68         server11     tier:control-plane c Running  kube-apiserver:0cd557bbf 2d:14h:1m:44s
                                          r11                                                omponent:kube-apiser          2fe
                                                                                             ver
    server11:3.0.0.68        kube-system  kube-controller-mana 3.0.0.68         server11     tier:control-plane c Running  kube-controller-manager: 2d:14h:1m:44s
                                          ger-server11                                       omponent:kube-contro          89b2323d09b2
                                                                                             ller-manager
    server11:3.0.0.68        kube-system  kube-proxy-f9dt8     3.0.0.68         server11     k8s-app:kube-proxy p Running  kube-proxy:032cc82ef3f8  2d:14h:0m:59s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    server11:3.0.0.68        kube-system  kube-scheduler-serve 3.0.0.68         server11     tier:control-plane c Running  kube-scheduler:c262a8071 2d:14h:1m:44s
                                          r11                                                omponent:kube-schedu          3cb
                                                                                             ler

### <span>View Kubernetes Node Information</span>

You can view a lot of information about a node, including the pod CIDR
and kubelet status.

    cumulus@host:~$ netq server11 show kubernetes node
    Matching kube_cluster records:
    Master                   Cluster Name     Node Name            Role       Status           Labels               Pod CIDR                 Last Changed
    ------------------------ ---------------- -------------------- ---------- ---------------- -------------------- ------------------------ ----------------
    server11:3.0.0.68        default          server11             master     KubeletReady     node-role.kubernetes 10.224.0.0/24            14h:23m:46s
                                                                                               .io/master: kubernet
                                                                                               es.io/hostname:hostd
                                                                                               -11 beta.kubernetes.
                                                                                               io/arch:amd64 beta.k
                                                                                               ubernetes.io/os:linu
                                                                                               x
    server11:3.0.0.68        default          server13             worker     KubeletReady     kubernetes.io/hostna 10.224.3.0/24            14h:19m:56s
                                                                                               me:server13 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    server11:3.0.0.68        default          server22             worker     KubeletReady     kubernetes.io/hostna 10.224.1.0/24            14h:24m:31s
                                                                                               me:server22 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    server11:3.0.0.68        default          server11             worker     KubeletReady     kubernetes.io/hostna 10.224.2.0/24            14h:24m:16s
                                                                                               me:server11 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    server11:3.0.0.68        default          server12             worker     KubeletReady     kubernetes.io/hostna 10.224.4.0/24            14h:24m:16s
                                                                                               me:server12 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    server11:3.0.0.68        default          server23             worker     KubeletReady     kubernetes.io/hostna 10.224.5.0/24            14h:24m:16s
                                                                                               me:server23 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    server11:3.0.0.68        default          server24             worker     KubeletReady     kubernetes.io/hostna 10.224.6.0/24            14h:24m:1s
                                                                                               me:server24 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux

To display the kubelet or Docker version, append `components` to the
above command. This example lists all the details of all master and
worker nodes because the master's hostname — *server11* in this case —
was included in the query.

    cumulus@server11:~$ netq server11 show kubernetes node components 
    Matching kube_cluster records:
                             Master           Cluster Name         Node Name    Kubelet      KubeProxy         Container Runt
                                                                                                               ime
    ------------------------ ---------------- -------------------- ------------ ------------ ----------------- --------------
    server11:3.0.0.68        default          server11             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    server11:3.0.0.68        default          server13             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    server11:3.0.0.68        default          server22             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    server11:3.0.0.68        default          server11             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    server11:3.0.0.68        default          server12             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    server11:3.0.0.68        default          server23             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    server11:3.0.0.68        default          server24             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady

To view only the details for a worker node, specify the hostname at the
end of the command after the `name` command:

    cumulus@server11:~$ netq server11 show kubernetes node components name server13
    Matching kube_cluster records:
                             Master           Cluster Name         Node Name    Kubelet      KubeProxy         Container Runt
                                                                                                               ime
    ------------------------ ---------------- -------------------- ------------ ------------ ----------------- --------------
    server11:3.0.0.68        default          server13             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady

You can view information about the replica set:

    cumulus@server11:~$ netq server11 show kubernetes replica-set
    Matching kube_replica records:
    Master                   Cluster Name Namespace        Replication Name               Labels               Replicas                           Ready Replicas Last Changed
    ------------------------ ------------ ---------------- ------------------------------ -------------------- ---------------------------------- -------------- ----------------
    server11:3.0.0.68        default      default          influxdb-6cdb566dd             app:influx           1                                  1              14h:19m:28s
    server11:3.0.0.68        default      default          nginx-8586cf59                 run:nginx            3                                  3              14h:24m:39s
    server11:3.0.0.68        default      default          httpd-5456469bfd               app:httpd            1                                  1              14h:19m:28s
    server11:3.0.0.68        default      kube-system      kube-dns-6f4fd4bdf             k8s-app:kube-dns     1                                  1              14h:27m:9s
    server11:3.0.0.68        default      kube-system      calico-kube-controllers-d669cc k8s-app:calico-kube- 1                                  1              14h:27m:9s
                                                           78f                            controllers

You can view information about the daemon set:

    cumulus@server11:~$ netq server11 show kubernetes daemon-set namespace default
    Matching kube_daemonset records:
    Master                   Cluster Name Namespace        Daemon Set Name                Labels               Desired Count Ready Count Last Changed
    ------------------------ ------------ ---------------- ------------------------------ -------------------- ------------- ----------- ----------------
    server11:3.0.0.68        default      default          cumulus-frr                    k8s-app:cumulus-frr  6             6           14h:25m:37s

You can view information about the pod:

    cumulus@server11:~$ netq server11 show kubernetes pod namespace default label nginx
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    server11:3.0.0.68        default      nginx-8586cf59-26pj5 10.244.9.193     server24     run:nginx            Running  nginx:6e2b65070c86       14h:25m:24s
    server11:3.0.0.68        default      nginx-8586cf59-c82ns 10.244.40.128    server12     run:nginx            Running  nginx:01b017c26725       14h:25m:24s
    server11:3.0.0.68        default      nginx-8586cf59-wjwgp 10.244.49.64     server22     run:nginx            Running  nginx:ed2b4254e328       14h:25m:24s
     
    cumulus@server11:~$ netq server11 show kubernetes pod namespace default label app
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    server11:3.0.0.68        default      httpd-5456469bfd-bq9 10.244.49.65     server22     app:httpd            Running  httpd:79b7f532be2d       14h:20m:34s
                                          zm
    server11:3.0.0.68        default      influxdb-6cdb566dd-8 10.244.162.128   server13     app:influx           Running  influxdb:15dce703cdec    14h:20m:34s
                                          9lwn

You can view information about the replication controller:

    cumulus@server11:~$ netq server11 show kubernetes replication-controller 
    No matching kube_replica records found

You can view information about a deployment:

    cumulus@server11:~$ netq server11 show kubernetes deployment name nginx
    Matching kube_deployment records:
    Master                   Namespace       Name                 Replicas                           Ready Replicas Labels                         Last Changed
    ------------------------ --------------- -------------------- ---------------------------------- -------------- ------------------------------ ----------------
    server11:3.0.0.68        default         nginx                3                                  3              run:nginx                      14h:27m:20s

You can search for information using labels as well. The label search is
similar to a "contains" regular expression search. In the following
example, we are looking for all nodes that contain *kube* in the
replication set name or label:

    cumulus@server11:~$ netq server11 show kubernetes replica-set label kube
    Matching kube_replica records:
    Master                   Cluster Name Namespace        Replication Name               Labels               Replicas                           Ready Replicas Last Changed
    ------------------------ ------------ ---------------- ------------------------------ -------------------- ---------------------------------- -------------- ----------------
    server11:3.0.0.68        default      kube-system      kube-dns-6f4fd4bdf             k8s-app:kube-dns     1                                  1              14h:30m:41s
    server11:3.0.0.68        default      kube-system      calico-kube-controllers-d669cc k8s-app:calico-kube- 1                                  1              14h:30m:41s
                                                           78f                            controllers

### <span>View Container Connectivity</span>

You can view the connectivity graph of a Kubernetes pod, seeing its
replica set, deployment or service level. The impact/connectivity graph
starts with the server where the pod is deployed, and shows the peer for
each server interface.

    cumulus@server11:~$ netq server11 show kubernetes deployment name nginx connectivity
    nginx -- nginx-8586cf59-wjwgp -- server22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- server22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- server22:swp3:NetQBond-2 -- swp20:NetQBond-20:edge01
                                  -- server22:swp4:NetQBond-2 -- swp20:NetQBond-20:edge02
          -- nginx-8586cf59-c82ns -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                  -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                  -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-26pj5 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                  -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
                                  -- server24:swp1:swp1 -- swp8:VlanA-1:tor-2

### <span>View Kubernetes Service Connectivity and Impact</span>

You can show the Kubernetes services in a cluster:

    cumulus@server11:~$ netq show kubernetes service 
    Matching kube_service records:
    Master                   Namespace        Service Name         Labels       Type       Cluster IP       External IP      Ports                               Last Changed
    ------------------------ ---------------- -------------------- ------------ ---------- ---------------- ---------------- ----------------------------------- ----------------
    server11:3.0.0.68        default          kubernetes                        ClusterIP  10.96.0.1                         TCP:443                             2d:13h:45m:30s
    server11:3.0.0.68        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:45m:27s
                                                                   co-etcd
    server11:3.0.0.68        kube-system      kube-dns             k8s-app:kube ClusterIP  10.96.0.10                        UDP:53 TCP:53                       2d:13h:45m:28s
                                                                   -dns
    server12:3.0.0.69        default          kubernetes                        ClusterIP  10.96.0.1                         TCP:443                             2d:13h:46m:24s
    server12:3.0.0.69        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:46m:20s
                                                                   co-etcd
    server12:3.0.0.69        kube-system      kube-dns             k8s-app:kube ClusterIP  10.96.0.10                        UDP:53 TCP:53                       2d:13h:46m:20s
                                                                   -dns

And get detailed information about a Kubernetes service:

    cumulus@server11:~$ netq show kubernetes service name calico-etcd 
    Matching kube_service records:
    Master                   Namespace        Service Name         Labels       Type       Cluster IP       External IP      Ports                               Last Changed
    ------------------------ ---------------- -------------------- ------------ ---------- ---------------- ---------------- ----------------------------------- ----------------
    server11:3.0.0.68        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:48m:10s
                                                                   co-etcd
    server12:3.0.0.69        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:49m:3s
                                                                   co-etcd

To see the connectivity of a given Kubernetes service, run:

    cumulus@server11:~$ netq show kubernetes service name calico-etcd connectivity 
    calico-etcd -- calico-etcd-pfg9r -- server11:swp1:torbond1 -- swp6:hostbond2:torc-11
                                     -- server11:swp2:torbond1 -- swp6:hostbond2:torc-12
                                     -- server11:swp3:NetQBond-2 -- swp16:NetQBond-16:edge01
                                     -- server11:swp4:NetQBond-2 -- swp16:NetQBond-16:edge02
    calico-etcd -- calico-etcd-btqgt -- server12:swp1:torbond1 -- swp7:hostbond3:torc-11
                                     -- server12:swp2:torbond1 -- swp7:hostbond3:torc-12
                                     -- server12:swp3:NetQBond-2 -- swp17:NetQBond-17:edge01
                                     -- server12:swp4:NetQBond-2 -- swp17:NetQBond-17:edge02

To see the impact of a given Kubernetes service, run:

    cumulus@server11:~$ netq server11 show impact kubernetes service name calico-etcd 
    calico-etcd -- calico-etcd-pfg9r -- server11:swp1:torbond1 -- swp6:hostbond2:torc-11
                                     -- server11:swp2:torbond1 -- swp6:hostbond2:torc-12
                                     -- server11:swp3:NetQBond-2 -- swp16:NetQBond-16:edge01
                                     -- server11:swp4:NetQBond-2 -- swp16:NetQBond-16:edge02

### <span>View Kubernetes Cluster Configuration in the Past</span>

You can use the ["time machine"
features](/cumulus-netq/Cumulus_NetQ_CLI_User_Guide/Resolve_Issues/Methods_for_Diagnosing_Network_Issues)
of NetQ on a Kubernetes cluster, using the `around` keyword to go back
in time to check the network status and identify any changes that
occurred on the network.

This example shows the current state of the network. Notice there is a
node named *server23*. server23 is there because the node *server22*
went down and Kubernetes spun up a third replica on a different host to
satisfy the deployment requirement.

    cumulus@redis-1:~$ netq server11 show kubernetes deployment name nginx connectivity
    nginx -- nginx-8586cf59-fqtnj -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                  -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                  -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-8g487 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                  -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
                                  -- server24:swp1:swp1 -- swp8:VlanA-1:tor-2
          -- nginx-8586cf59-2hb8t -- server23:swp1:swp1 -- swp7:VlanA-1:tor-2
                                  -- server23:swp2:NetQBond-1 -- swp28:NetQBond-28:edge01
                                  -- server23:swp3:NetQBond-1 -- swp28:NetQBond-28:edge02

You can see this by going back in time 10 minutes. *server23* was not
present, whereas *server22* **was** present:

    cumulus@redis-1:~$ netq server11 show kubernetes deployment name nginx connectivity around 10m
    nginx -- nginx-8586cf59-fqtnj -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                  -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                  -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-2xxs4 -- server22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- server22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- server22:swp3:NetQBond-2 -- swp20:NetQBond-20:edge01
                                  -- server22:swp4:NetQBond-2 -- swp20:NetQBond-20:edge02
          -- nginx-8586cf59-8g487 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                  -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
                                  -- server24:swp1:swp1 -- swp8:VlanA-1:tor-2

You can determine the impact on the Kubernetes deployment in the event a
host or switch goes down. The output is color coded (not shown in the
example below) so you can clearly see the impact: green shows no impact,
yellow shows partial impact, and red shows full impact.

    cumulus@server11:~$ netq torc-21 show impact kubernetes deployment name nginx
    nginx -- nginx-8586cf59-wjwgp -- server22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- server22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- server22:swp3:NetQBond-2 -- swp20:NetQBond-20:edge01
                                  -- server22:swp4:NetQBond-2 -- swp20:NetQBond-20:edge02
          -- nginx-8586cf59-c82ns -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                  -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                  -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-26pj5 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                  -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
                                  -- server24:swp1:swp1 -- swp8:VlanA-1:tor-2
    cumulus@server11:~$ netq server12 show impact kubernetes deployment name nginx
    nginx -- nginx-8586cf59-wjwgp -- server22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- server22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- server22:swp3:NetQBond-2 -- swp20:NetQBond-20:edge01
                                  -- server22:swp4:NetQBond-2 -- swp20:NetQBond-20:edge02
          -- nginx-8586cf59-c82ns -- server12:swp2:NetQBond-1 -- swp23:NetQBond-23:edge01
                                  -- server12:swp3:NetQBond-1 -- swp23:NetQBond-23:edge02
                                  -- server12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-26pj5 -- server24:swp2:NetQBond-1 -- swp29:NetQBond-29:edge01
                                  -- server24:swp3:NetQBond-1 -- swp29:NetQBond-29:edge02
