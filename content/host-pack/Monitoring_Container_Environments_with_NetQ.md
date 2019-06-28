---
title: Monitoring Container Environments with NetQ
author: Cumulus Networks
weight: 25
aliases:
 - /display/HOSTPACK/Monitoring+Container+Environments+with+NetQ
 - /pages/viewpage.action?pageId=7110909
pageID: 7110909
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
---
The NetQ Agent monitors container environments the same way it monitors
[physical
servers](https://docs.cumulusnetworks.com/display/NETQ/Monitor+Linux+Hosts).
There is no special implementation. The NetQ Agent pulls data from the
container as it would pull data from a Cumulus Linux switch or Linux
host.

NetQ interacts with containers managed by both Docker Swarm and
Kubernetes.

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

## <span>NetQ with Kubernetes Clusters</span>

### <span>NetQ Kubernetes Support</span>

The NetQ Agent supports Kubernetes version 1.9.2 or later.

NetQ 1.3 and later releases support integrations with Kubernetes. The
NetQ agent interfaces with Kubernetes API server and listens to
Kubernetes events. The agent monitors network identity and physical
network connectivity of Kubernetes resources like Pods, Daemon sets,
Service etc. NetQ works with any container network interface (CNI)
you're using, such as Calico or Flannel.

The NetQ Kubernetes integration enables network administrators to:

  - Identify and locate pods, deployment, replica-set and services
    deployed within the network using IP, name, label, and so forth.

  - Track network connectivity of all pods of a service, deployment and
    replica set.

  - Locate what pods have been deployed adjacent to a top of rack (ToR)
    switch.

  - Check what pod, services, replica set or deployment can be impacted
    by a specific ToR switch.

NetQ helps the infrastructure administrator determine how Kubernetes
workloads are distributed within a network.

The NetQ analytics with time machine helps network administrators view
changes within a Kubernetes cluster and identify if such changes had
adverse effect on the network performance (caused by noisy neighbor
etc).

All NetQ commands provide the ability for JSON output (by appending
`json` to the NetQ command).

### <span>Telemetry Server Memory Requirement</span>

Due to the higher memory requirements to run containers, Cumulus
Networks recommends you run the NetQ Telemetry Server on a host with at
least 32G RAM. For more information, read the [NetQ user
guide](https://docs.cumulusnetworks.com/display/NETQ/Methods+for+Diagnosing+Network+Issues#MethodsforDiagnosingNetworkIssues-matrixHowFarBackinTimeCanYouTravel?).

### <span id="src-7110909_MonitoringContainerEnvironmentswithNetQ-enable_k8s" class="confluence-anchor-link"></span><span>Enable Monitoring of Kubernetes</span>

In order for NetQ to be able to monitor the containers on a host, you
need to do the following on the master node only:

1.  Configure the host to point to the telemetry server by its IP
    address. See the [NetQ user
    guide](https://docs.cumulusnetworks.com/display/NETQ/Monitor+Container+Environments)
    for details.

2.  Enable Kubernetes monitoring by NetQ. You can specify a polling
    period between 10 and 120 seconds; 15 seconds is the default.
    
        cumulus@hostd-11:~$ netq config add agent kubernetes-monitor poll-period 20
        Successfully added kubernetes monitor. Please restart netq-agent.

3.  Restart the NetQ agent:
    
        cumulus@server01:~$ netq config restart agent

You still need to [enable the NetQ
Agent](/host-pack/Installing_NetQ_on_the_Host) on all the worker nodes
for complete insight into your container network.

### <span>Show Kubernetes Clusters</span>

You can get the status of all Kubernetes clusters in the fabric using
the `netq show kubernetes cluster` command:

    cumulus@hostd-11:~$ netq show kubernetes cluster 
    Matching kube_cluster records:
    Master                   Cluster Name     Controller Status    Scheduler Status Nodes
    ------------------------ ---------------- -------------------- ---------------- --------------------
    hostd-11:3.0.0.68        default          Healthy              Healthy          hostd-11 hostd-13 ho
                                                                                    std-22 hosts-11 host
                                                                                    s-12 hosts-23 hosts-
                                                                                    24
    hostd-12:3.0.0.69        default          Healthy              Healthy          hostd-12 hostd-21 ho
                                                                                    std-23 hosts-13 host
                                                                                    s-14 hosts-21 hosts-
                                                                                    22

You can output the results to JSON:

    cumulus@hostd-11:~$ netq show kubernetes cluster json
    {
        "kube_cluster":[
            {
                "clusterName":"default",
                "schedulerStatus":"Healthy",
                "master":"hostd-12:3.0.0.69",
                "nodes":"hostd-12 hostd-21 hostd-23 hosts-13 hosts-14 hosts-21 hosts-22",
                "controllerStatus":"Healthy"
            },
            {
                "clusterName":"default",
                "schedulerStatus":"Healthy",
                "master":"hostd-11:3.0.0.68",
                "nodes":"hostd-11 hostd-13 hostd-22 hosts-11 hosts-12 hosts-23 hosts-24",
                "controllerStatus":"Healthy"
        }
        ],
        "truncatedResult":false
    }

You can see the changes made to the cluster:

    cumulus@hostd-11:~$ netq show kubernetes cluster changes 
    Matching kube_cluster records:
    Master                   Cluster Name     Controller Status    Scheduler Status Nodes                                    DBState  Last changed
    ------------------------ ---------------- -------------------- ---------------- ---------------------------------------- -------- ----------------
    hostd-11:3.0.0.68        default          Healthy              Healthy          hostd-11 hostd-13 hostd-22 hosts-11 host Add      2d:13h:54m:26s
                                                                                    s-12 hosts-23 hosts-24
    hostd-12:3.0.0.69        default          Healthy              Healthy          hostd-12 hostd-21 hostd-23 hosts-13 host Add      2d:13h:54m:35s
                                                                                    s-14 hosts-21 hosts-22
    hostd-12:3.0.0.69        default          Healthy              Healthy          hostd-12 hostd-21 hostd-23 hosts-13      Add      2d:13h:54m:50s
    hostd-11:3.0.0.68        default          Healthy              Healthy          hostd-11                                 Add      2d:13h:54m:57s
    hostd-12:3.0.0.69        default          Healthy              Healthy          hostd-12                                 Add      2d:13h:55m:50s

To filter the list, you can specify the hostname of the master before
the `show` command:

    cumulus@redis-1:~$ netq hostd-11 show kubernetes cluster
    Matching kube_cluster records:
    Master                   Cluster Name     Controller Status    Scheduler Status Nodes
    ------------------------ ---------------- -------------------- ---------------- --------------------
    hostd-11:3.0.0.68        default          Healthy              Healthy          hostd-11 hostd-13 ho
                                                                                    std-22 hosts-11 host
                                                                                    s-12 hosts-23 hosts-
                                                                                    24

### <span>Show Kubernetes Pod Information</span>

You can show the pods in a cluster:

    cumulus@hostd-11:~$ netq show kubernetes pod 
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    hostd-11:3.0.0.68        default      cumulus-frr-8vssx    3.0.0.70         hostd-13     pod-template-generat Running  cumulus-frr:f8cac70bb217 2d:13h:54m:1s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-11:3.0.0.68        default      cumulus-frr-dkkgp    3.0.5.135        hosts-24     pod-template-generat Running  cumulus-frr:577a60d5f40c 2d:13h:54m:1s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-11:3.0.0.68        default      cumulus-frr-f4bgx    3.0.3.196        hosts-11     pod-template-generat Running  cumulus-frr:1bc73154a9f5 2d:13h:54m:1s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-11:3.0.0.68        default      cumulus-frr-gqqxn    3.0.2.5          hostd-22     pod-template-generat Running  cumulus-frr:3ee0396d126a 2d:13h:54m:1s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-11:3.0.0.68        default      cumulus-frr-kdh9f    3.0.3.197        hosts-12     pod-template-generat Running  cumulus-frr:94b6329ecb50 2d:13h:54m:1s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-11:3.0.0.68        default      cumulus-frr-mvv8m    3.0.5.134        hosts-23     pod-template-generat Running  cumulus-frr:b5845299ce3c 2d:13h:54m:1s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-11:3.0.0.68        default      httpd-5456469bfd-bq9 10.244.49.65     hostd-22     app:httpd            Running  httpd:79b7f532be2d       2d:13h:48m:18s
                                          zm
    hostd-11:3.0.0.68        default      influxdb-6cdb566dd-8 10.244.162.128   hostd-13     app:influx           Running  influxdb:15dce703cdec    2d:13h:48m:18s
                                          9lwn
    hostd-11:3.0.0.68        default      nginx-8586cf59-26pj5 10.244.9.193     hosts-24     run:nginx            Running  nginx:6e2b65070c86       2d:13h:53m:29s
    hostd-11:3.0.0.68        default      nginx-8586cf59-c82ns 10.244.40.128    hosts-12     run:nginx            Running  nginx:01b017c26725       2d:13h:53m:29s
    hostd-11:3.0.0.68        default      nginx-8586cf59-wjwgp 10.244.49.64     hostd-22     run:nginx            Running  nginx:ed2b4254e328       2d:13h:53m:29s
    hostd-11:3.0.0.68        kube-system  calico-etcd-pfg9r    3.0.0.68         hostd-11     k8s-app:calico-etcd  Running  calico-etcd:f95f44b745a7 2d:13h:55m:59s
                                                                                             pod-template-generat
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:142071906
                                                                                             5
    hostd-11:3.0.0.68        kube-system  calico-kube-controll 3.0.2.5          hostd-22     k8s-app:calico-kube- Running  calico-kube-controllers: 2d:13h:54m:56s
                                          ers-d669cc78f-4r5t2                                controllers                   3688b0c5e9c5
    hostd-11:3.0.0.68        kube-system  calico-node-4px69    3.0.2.5          hostd-22     k8s-app:calico-node  Running  calico-node:1d01648ebba4 2d:13h:55m:41s
                                                                                             pod-template-generat          install-cni:da350802a3d2
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  calico-node-bt8w6    3.0.3.196        hosts-11     k8s-app:calico-node  Running  calico-node:9b3358a07e5e 2d:13h:55m:38s
                                                                                             pod-template-generat          install-cni:d38713e6fdd8
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  calico-node-gtmkv    3.0.3.197        hosts-12     k8s-app:calico-node  Running  calico-node:48fcc6c40a6b 2d:13h:55m:34s
                                                                                             pod-template-generat          install-cni:f0838a313eff
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  calico-node-mvslq    3.0.5.134        hosts-23     k8s-app:calico-node  Running  calico-node:7b361aece76c 2d:13h:55m:33s
                                                                                             pod-template-generat          install-cni:f2da6bc36bf8
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  calico-node-sjj2s    3.0.5.135        hosts-24     k8s-app:calico-node  Running  calico-node:6e13b2b73031 2d:13h:55m:29s
                                                                                             pod-template-generat          install-cni:fa4b2b17fba9
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  calico-node-vdkk5    3.0.0.70         hostd-13     k8s-app:calico-node  Running  calico-node:fb3ec9429281 2d:13h:55m:36s
                                                                                             pod-template-generat          install-cni:b56980da7294
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  calico-node-zzfkr    3.0.0.68         hostd-11     k8s-app:calico-node  Running  calico-node:c1ac399dd862 2d:13h:55m:59s
                                                                                             pod-template-generat          install-cni:60a779fdc47a
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  etcd-hostd-11        3.0.0.68         hostd-11     tier:control-plane c Running  etcd:dde63d44a2f5        2d:13h:56m:44s
                                                                                             omponent:etcd
    hostd-11:3.0.0.68        kube-system  kube-apiserver-hostd 3.0.0.68         hostd-11     tier:control-plane c Running  kube-apiserver:0cd557bbf 2d:13h:56m:44s
                                          -11                                                omponent:kube-apiser          2fe
                                                                                             ver
    hostd-11:3.0.0.68        kube-system  kube-controller-mana 3.0.0.68         hostd-11     tier:control-plane c Running  kube-controller-manager: 2d:13h:56m:44s
                                          ger-hostd-11                                       omponent:kube-contro          89b2323d09b2
                                                                                             ller-manager
    hostd-11:3.0.0.68        kube-system  kube-dns-6f4fd4bdf-p 10.244.34.64     hosts-23     k8s-app:kube-dns     Running  dnsmasq:284d9d363999 kub 2d:13h:54m:56s
                                          lv7p                                                                             edns:bd8bdc49b950 sideca
                                                                                                                           r:fe10820ffb19
    hostd-11:3.0.0.68        kube-system  kube-proxy-4cx2t     3.0.3.197        hosts-12     k8s-app:kube-proxy p Running  kube-proxy:49b0936a4212  2d:13h:55m:34s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-proxy-7674k     3.0.3.196        hosts-11     k8s-app:kube-proxy p Running  kube-proxy:5dc2f5fe0fad  2d:13h:55m:38s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-proxy-ck5cn     3.0.2.5          hostd-22     k8s-app:kube-proxy p Running  kube-proxy:6944f7ff8c18  2d:13h:55m:41s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-proxy-f9dt8     3.0.0.68         hostd-11     k8s-app:kube-proxy p Running  kube-proxy:032cc82ef3f8  2d:13h:55m:59s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-proxy-j6qw6     3.0.5.135        hosts-24     k8s-app:kube-proxy p Running  kube-proxy:10544e43212e  2d:13h:55m:29s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-proxy-lq8zz     3.0.5.134        hosts-23     k8s-app:kube-proxy p Running  kube-proxy:1bcfa09bb186  2d:13h:55m:33s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-proxy-vg7kj     3.0.0.70         hostd-13     k8s-app:kube-proxy p Running  kube-proxy:8fed384b68e5  2d:13h:55m:36s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-scheduler-hostd 3.0.0.68         hostd-11     tier:control-plane c Running  kube-scheduler:c262a8071 2d:13h:56m:44s
                                          -11                                                omponent:kube-schedu          3cb
                                                                                             ler
    hostd-12:3.0.0.69        default      cumulus-frr-2gkdv    3.0.2.4          hostd-21     pod-template-generat Running  cumulus-frr:25d1109f8898 2d:13h:54m:39s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-12:3.0.0.69        default      cumulus-frr-b9dm5    3.0.3.199        hosts-14     pod-template-generat Running  cumulus-frr:45063f9a095f 2d:13h:54m:39s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-12:3.0.0.69        default      cumulus-frr-rtqhv    3.0.2.6          hostd-23     pod-template-generat Running  cumulus-frr:63e802a52ea2 2d:13h:54m:39s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-12:3.0.0.69        default      cumulus-frr-tddrg    3.0.5.133        hosts-22     pod-template-generat Running  cumulus-frr:52dd54e4ac9f 2d:13h:54m:39s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-12:3.0.0.69        default      cumulus-frr-vx7jp    3.0.5.132        hosts-21     pod-template-generat Running  cumulus-frr:1c20addfcbd3 2d:13h:54m:39s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-12:3.0.0.69        default      cumulus-frr-x7ft5    3.0.3.198        hosts-13     pod-template-generat Running  cumulus-frr:b0f63792732e 2d:13h:54m:39s
                                                                                             ion:1 name:cumulus-f
                                                                                             rr controller-revisi
                                                                                             on-hash:3710533951
    hostd-12:3.0.0.69        kube-system  calico-etcd-btqgt    3.0.0.69         hostd-12     k8s-app:calico-etcd  Running  calico-etcd:72b1a16968fb 2d:13h:56m:52s
                                                                                             pod-template-generat
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:142071906
                                                                                             5
    hostd-12:3.0.0.69        kube-system  calico-kube-controll 3.0.5.132        hosts-21     k8s-app:calico-kube- Running  calico-kube-controllers: 2d:13h:54m:49s
                                          ers-d669cc78f-bdnzk                                controllers                   6821bf04696f
    hostd-12:3.0.0.69        kube-system  calico-node-4g6vd    3.0.3.198        hosts-13     k8s-app:calico-node  Running  calico-node:1046b559a50c 2d:13h:55m:53s
                                                                                             pod-template-generat          install-cni:0a136851da17
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  calico-node-4hg6l    3.0.0.69         hostd-12     k8s-app:calico-node  Running  calico-node:4e7acc83f8e8 2d:13h:56m:52s
                                                                                             pod-template-generat          install-cni:a26e76de289e
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  calico-node-4p66v    3.0.2.6          hostd-23     k8s-app:calico-node  Running  calico-node:a7a44072e4e2 2d:13h:56m:0s
                                                                                             pod-template-generat          install-cni:9a19da2b2308
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  calico-node-5z7k4    3.0.5.133        hosts-22     k8s-app:calico-node  Running  calico-node:9878b0606158 2d:13h:55m:45s
                                                                                             pod-template-generat          install-cni:489f8f326cf9
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  calico-node-885s6    3.0.5.132        hosts-21     k8s-app:calico-node  Running  calico-node:24a696f0406c 2d:13h:55m:48s
                                                                                             pod-template-generat          install-cni:15f626e44a6d
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  calico-node-c8wjf    3.0.3.199        hosts-14     k8s-app:calico-node  Running  calico-node:597c8b2053f4 2d:13h:55m:50s
                                                                                             pod-template-generat          install-cni:646e8df27be8
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  calico-node-gkkgk    3.0.2.4          hostd-21     k8s-app:calico-node  Running  calico-node:73806361f929 2d:13h:56m:5s
                                                                                             pod-template-generat          install-cni:2f9fedf26968
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:490828062
    hostd-12:3.0.0.69        kube-system  etcd-hostd-12        3.0.0.69         hostd-12     tier:control-plane c Running  etcd:cba8d4559e7f        2d:13h:57m:52s
                                                                                             omponent:etcd
    hostd-12:3.0.0.69        kube-system  kube-apiserver-hostd 3.0.0.69         hostd-12     tier:control-plane c Running  kube-apiserver:bbb852aed 2d:13h:57m:52s
                                          -12                                                omponent:kube-apiser          a1e
                                                                                             ver
    hostd-12:3.0.0.69        kube-system  kube-controller-mana 3.0.0.69         hostd-12     tier:control-plane c Running  kube-controller-manager: 2d:13h:57m:52s
                                          ger-hostd-12                                       omponent:kube-contro          f3d5501adbf3
                                                                                             ller-manager
    hostd-12:3.0.0.69        kube-system  kube-dns-6f4fd4bdf-5 10.245.104.128   hosts-22     k8s-app:kube-dns     Running  dnsmasq:b9149784c5d0 kub 2d:13h:54m:49s
                                          psn4                                                                             edns:370104ad260c sideca
                                                                                                                           r:2dc9ac7eb34b
    hostd-12:3.0.0.69        kube-system  kube-proxy-56dq8     3.0.5.132        hosts-21     k8s-app:kube-proxy p Running  kube-proxy:c3f9944efcac  2d:13h:55m:48s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-proxy-5c9rx     3.0.2.4          hostd-21     k8s-app:kube-proxy p Running  kube-proxy:7266de023ad9  2d:13h:56m:5s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-proxy-5pznh     3.0.3.198        hosts-13     k8s-app:kube-proxy p Running  kube-proxy:846a571b6fd2  2d:13h:55m:53s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-proxy-8mt6w     3.0.2.6          hostd-23     k8s-app:kube-proxy p Running  kube-proxy:9de8b5c76565  2d:13h:56m:0s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-proxy-9qngl     3.0.3.199        hosts-14     k8s-app:kube-proxy p Running  kube-proxy:638ffdb9ed51  2d:13h:55m:50s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-proxy-k568l     3.0.0.69         hostd-12     k8s-app:kube-proxy p Running  kube-proxy:a0e081e5a141  2d:13h:56m:52s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-proxy-mwf6s     3.0.5.133        hosts-22     k8s-app:kube-proxy p Running  kube-proxy:55d80158e5fc  2d:13h:55m:45s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-12:3.0.0.69        kube-system  kube-scheduler-hostd 3.0.0.69         hostd-12     tier:control-plane c Running  kube-scheduler:d941808cd 2d:13h:57m:52s
                                          -12                                                omponent:kube-schedu          f2a
                                                                                             ler

You can get more information about a pod:

    cumulus@hostd-11:~$ netq show kubernetes pod node hostd-11
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    hostd-11:3.0.0.68        kube-system  calico-etcd-pfg9r    3.0.0.68         hostd-11     k8s-app:calico-etcd  Running  calico-etcd:f95f44b745a7 2d:14h:0m:59s
                                                                                             pod-template-generat
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:142071906
                                                                                             5
    hostd-11:3.0.0.68        kube-system  calico-node-zzfkr    3.0.0.68         hostd-11     k8s-app:calico-node  Running  calico-node:c1ac399dd862 2d:14h:0m:59s
                                                                                             pod-template-generat          install-cni:60a779fdc47a
                                                                                             ion:1 controller-rev
                                                                                             ision-hash:324404111
                                                                                             9
    hostd-11:3.0.0.68        kube-system  etcd-hostd-11        3.0.0.68         hostd-11     tier:control-plane c Running  etcd:dde63d44a2f5        2d:14h:1m:44s
                                                                                             omponent:etcd
    hostd-11:3.0.0.68        kube-system  kube-apiserver-hostd 3.0.0.68         hostd-11     tier:control-plane c Running  kube-apiserver:0cd557bbf 2d:14h:1m:44s
                                          -11                                                omponent:kube-apiser          2fe
                                                                                             ver
    hostd-11:3.0.0.68        kube-system  kube-controller-mana 3.0.0.68         hostd-11     tier:control-plane c Running  kube-controller-manager: 2d:14h:1m:44s
                                          ger-hostd-11                                       omponent:kube-contro          89b2323d09b2
                                                                                             ller-manager
    hostd-11:3.0.0.68        kube-system  kube-proxy-f9dt8     3.0.0.68         hostd-11     k8s-app:kube-proxy p Running  kube-proxy:032cc82ef3f8  2d:14h:0m:59s
                                                                                             od-template-generati
                                                                                             on:1 controller-revi
                                                                                             sion-hash:3953509896
    hostd-11:3.0.0.68        kube-system  kube-scheduler-hostd 3.0.0.68         hostd-11     tier:control-plane c Running  kube-scheduler:c262a8071 2d:14h:1m:44s
                                          -11                                                omponent:kube-schedu          3cb
                                                                                             ler

### <span>Monitor Kubernetes Nodes</span>

You can view a lot of information about a node, including the pod CIDR
and kubelet status.

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes node
    Matching kube_cluster records:
    Master                   Cluster Name     Node Name            Role       Status           Labels               Pod CIDR                 Last Changed
    ------------------------ ---------------- -------------------- ---------- ---------------- -------------------- ------------------------ ----------------
    hostd-11:3.0.0.68        default          hostd-11             master     KubeletReady     node-role.kubernetes 10.224.0.0/24            14h:23m:46s
                                                                                               .io/master: kubernet
                                                                                               es.io/hostname:hostd
                                                                                               -11 beta.kubernetes.
                                                                                               io/arch:amd64 beta.k
                                                                                               ubernetes.io/os:linu
                                                                                               x
    hostd-11:3.0.0.68        default          hostd-13             worker     KubeletReady     kubernetes.io/hostna 10.224.3.0/24            14h:19m:56s
                                                                                               me:hostd-13 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    hostd-11:3.0.0.68        default          hostd-22             worker     KubeletReady     kubernetes.io/hostna 10.224.1.0/24            14h:24m:31s
                                                                                               me:hostd-22 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    hostd-11:3.0.0.68        default          hosts-11             worker     KubeletReady     kubernetes.io/hostna 10.224.2.0/24            14h:24m:16s
                                                                                               me:hosts-11 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    hostd-11:3.0.0.68        default          hosts-12             worker     KubeletReady     kubernetes.io/hostna 10.224.4.0/24            14h:24m:16s
                                                                                               me:hosts-12 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    hostd-11:3.0.0.68        default          hosts-23             worker     KubeletReady     kubernetes.io/hostna 10.224.5.0/24            14h:24m:16s
                                                                                               me:hosts-23 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux
    hostd-11:3.0.0.68        default          hosts-24             worker     KubeletReady     kubernetes.io/hostna 10.224.6.0/24            14h:24m:1s
                                                                                               me:hosts-24 beta.kub
                                                                                               ernetes.io/arch:amd6
                                                                                               4 beta.kubernetes.io
                                                                                               /os:linux

To display the kubelet or Docker version, append `components` to the
above command. The output below includes all the details of all master
and worker nodes because the master's hostname — *hostd-11* in this case
— was included in the query.

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes node components 
     
     
    Matching kube_cluster records:
                             Master           Cluster Name         Node Name    Kubelet      KubeProxy         Container Runt
                                                                                                               ime
    ------------------------ ---------------- -------------------- ------------ ------------ ----------------- --------------
    hostd-11:3.0.0.68        default          hostd-11             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    hostd-11:3.0.0.68        default          hostd-13             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    hostd-11:3.0.0.68        default          hostd-22             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    hostd-11:3.0.0.68        default          hosts-11             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    hostd-11:3.0.0.68        default          hosts-12             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    hostd-11:3.0.0.68        default          hosts-23             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady
    hostd-11:3.0.0.68        default          hosts-24             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady

To view only the details for a worker node, specify the hostname at the
end of the command after the `name` command:

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes node components name hostd-13
     
    Matching kube_cluster records:
                             Master           Cluster Name         Node Name    Kubelet      KubeProxy         Container Runt
                                                                                                               ime
    ------------------------ ---------------- -------------------- ------------ ------------ ----------------- --------------
    hostd-11:3.0.0.68        default          hostd-13             v1.9.2       v1.9.2       docker://17.3.2   KubeletReady

You can view information about the replica set:

     
    cumulus@hostd-11:~$ netq hostd-11 show kubernetes replica-set
     
     
    Matching kube_replica records:
    Master                   Cluster Name Namespace        Replication Name               Labels               Replicas                           Ready Replicas Last Changed
    ------------------------ ------------ ---------------- ------------------------------ -------------------- ---------------------------------- -------------- ----------------
    hostd-11:3.0.0.68        default      default          influxdb-6cdb566dd             app:influx           1                                  1              14h:19m:28s
    hostd-11:3.0.0.68        default      default          nginx-8586cf59                 run:nginx            3                                  3              14h:24m:39s
    hostd-11:3.0.0.68        default      default          httpd-5456469bfd               app:httpd            1                                  1              14h:19m:28s
    hostd-11:3.0.0.68        default      kube-system      kube-dns-6f4fd4bdf             k8s-app:kube-dns     1                                  1              14h:27m:9s
    hostd-11:3.0.0.68        default      kube-system      calico-kube-controllers-d669cc k8s-app:calico-kube- 1                                  1              14h:27m:9s
                                                           78f                            controllers

You can view information about the daemon set:

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes daemon-set namespace default
    Matching kube_daemonset records:
    Master                   Cluster Name Namespace        Daemon Set Name                Labels               Desired Count Ready Count Last Changed
    ------------------------ ------------ ---------------- ------------------------------ -------------------- ------------- ----------- ----------------
    hostd-11:3.0.0.68        default      default          cumulus-frr                    k8s-app:cumulus-frr  6             6           14h:25m:37s

You can view information about the pod:

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes pod namespace default label nginx
     
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    hostd-11:3.0.0.68        default      nginx-8586cf59-26pj5 10.244.9.193     hosts-24     run:nginx            Running  nginx:6e2b65070c86       14h:25m:24s
    hostd-11:3.0.0.68        default      nginx-8586cf59-c82ns 10.244.40.128    hosts-12     run:nginx            Running  nginx:01b017c26725       14h:25m:24s
    hostd-11:3.0.0.68        default      nginx-8586cf59-wjwgp 10.244.49.64     hostd-22     run:nginx            Running  nginx:ed2b4254e328       14h:25m:24s
     
    cumulus@hostd-11:~$ netq hostd-11 show kubernetes pod namespace default label app
     
    Matching kube_pod records:
    Master                   Namespace    Name                 IP               Node         Labels               Status   Containers               Last Changed
    ------------------------ ------------ -------------------- ---------------- ------------ -------------------- -------- ------------------------ ----------------
    hostd-11:3.0.0.68        default      httpd-5456469bfd-bq9 10.244.49.65     hostd-22     app:httpd            Running  httpd:79b7f532be2d       14h:20m:34s
                                          zm
    hostd-11:3.0.0.68        default      influxdb-6cdb566dd-8 10.244.162.128   hostd-13     app:influx           Running  influxdb:15dce703cdec    14h:20m:34s
                                          9lwn

You can view information about the replication controller:

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes replication-controller 
     
     
    No matching kube_replica records found

You can view information about a deployment:

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes deployment name nginx
    Matching kube_deployment records:
    Master                   Namespace       Name                 Replicas                           Ready Replicas Labels                         Last Changed
    ------------------------ --------------- -------------------- ---------------------------------- -------------- ------------------------------ ----------------
    hostd-11:3.0.0.68        default         nginx                3                                  3              run:nginx                      14h:27m:20s

You can search for information using labels as well. The label search is
similar to a "contains" regular expression search. In the following
example, we are looking for all nodes that contain *kube* in the
replication set name or label:

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes replica-set label kube
     
    Matching kube_replica records:
    Master                   Cluster Name Namespace        Replication Name               Labels               Replicas                           Ready Replicas Last Changed
    ------------------------ ------------ ---------------- ------------------------------ -------------------- ---------------------------------- -------------- ----------------
    hostd-11:3.0.0.68        default      kube-system      kube-dns-6f4fd4bdf             k8s-app:kube-dns     1                                  1              14h:30m:41s
    hostd-11:3.0.0.68        default      kube-system      calico-kube-controllers-d669cc k8s-app:calico-kube- 1                                  1              14h:30m:41s
                                                           78f                            controllers

### <span>Show Container Connectivity</span>

You can view the connectivity graph of a Kubernetes pod, seeing its
replica set, deployment or service level. The impact/connectivity graph
starts with the server where the pod is deployed, and shows the peer for
each server interface.

    cumulus@hostd-11:~$ netq hostd-11 show kubernetes deployment name nginx connectivity
    nginx -- nginx-8586cf59-wjwgp -- hostd-22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- hostd-22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- hostd-22:swp3:NetQBond-2 -- swp20:NetQBond-20:noc-pr
                                  -- hostd-22:swp4:NetQBond-2 -- swp20:NetQBond-20:noc-se
          -- nginx-8586cf59-c82ns -- hosts-12:swp2:NetQBond-1 -- swp23:NetQBond-23:noc-pr
                                  -- hosts-12:swp3:NetQBond-1 -- swp23:NetQBond-23:noc-se
                                  -- hosts-12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-26pj5 -- hosts-24:swp2:NetQBond-1 -- swp29:NetQBond-29:noc-pr
                                  -- hosts-24:swp3:NetQBond-1 -- swp29:NetQBond-29:noc-se
                                  -- hosts-24:swp1:swp1 -- swp8:VlanA-1:tor-2

### <span>Show Kubernetes Service Connectivity and Impact</span>

You can show the Kubernetes services in a cluster:

    cumulus@hostd-11:~$ netq show kubernetes service 
    Matching kube_service records:
    Master                   Namespace        Service Name         Labels       Type       Cluster IP       External IP      Ports                               Last Changed
    ------------------------ ---------------- -------------------- ------------ ---------- ---------------- ---------------- ----------------------------------- ----------------
    hostd-11:3.0.0.68        default          kubernetes                        ClusterIP  10.96.0.1                         TCP:443                             2d:13h:45m:30s
    hostd-11:3.0.0.68        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:45m:27s
                                                                   co-etcd
    hostd-11:3.0.0.68        kube-system      kube-dns             k8s-app:kube ClusterIP  10.96.0.10                        UDP:53 TCP:53                       2d:13h:45m:28s
                                                                   -dns
    hostd-12:3.0.0.69        default          kubernetes                        ClusterIP  10.96.0.1                         TCP:443                             2d:13h:46m:24s
    hostd-12:3.0.0.69        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:46m:20s
                                                                   co-etcd
    hostd-12:3.0.0.69        kube-system      kube-dns             k8s-app:kube ClusterIP  10.96.0.10                        UDP:53 TCP:53                       2d:13h:46m:20s
                                                                   -dns

And get detailed information about a Kubernetes service:

    cumulus@hostd-11:~$ netq show kubernetes service name calico-etcd 
    Matching kube_service records:
    Master                   Namespace        Service Name         Labels       Type       Cluster IP       External IP      Ports                               Last Changed
    ------------------------ ---------------- -------------------- ------------ ---------- ---------------- ---------------- ----------------------------------- ----------------
    hostd-11:3.0.0.68        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:48m:10s
                                                                   co-etcd
    hostd-12:3.0.0.69        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:49m:3s
                                                                   co-etcd

To see the connectivity of a given Kubernetes service, run:

    cumulus@hostd-11:~$ netq show kubernetes service name calico-etcd 
    Matching kube_service records:
    Master                   Namespace        Service Name         Labels       Type       Cluster IP       External IP      Ports                               Last Changed
    ------------------------ ---------------- -------------------- ------------ ---------- ---------------- ---------------- ----------------------------------- ----------------
    hostd-11:3.0.0.68        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:48m:10s
                                                                   co-etcd
    hostd-12:3.0.0.69        kube-system      calico-etcd          k8s-app:cali ClusterIP  10.96.232.136                     TCP:6666                            2d:13h:49m:3s
                                                                   co-etcd
    cumulus@hostd-11:~$ netq show kubernetes service name calico-etcd connectivity 
    calico-etcd -- calico-etcd-pfg9r -- hostd-11:swp1:torbond1 -- swp6:hostbond2:torc-11
                                     -- hostd-11:swp2:torbond1 -- swp6:hostbond2:torc-12
                                     -- hostd-11:swp3:NetQBond-2 -- swp16:NetQBond-16:noc-pr
                                     -- hostd-11:swp4:NetQBond-2 -- swp16:NetQBond-16:noc-se
    calico-etcd -- calico-etcd-btqgt -- hostd-12:swp1:torbond1 -- swp7:hostbond3:torc-11
                                     -- hostd-12:swp2:torbond1 -- swp7:hostbond3:torc-12
                                     -- hostd-12:swp3:NetQBond-2 -- swp17:NetQBond-17:noc-pr
                                     -- hostd-12:swp4:NetQBond-2 -- swp17:NetQBond-17:noc-se

To see the impact of a given Kubernetes service, run:

    cumulus@hostd-11:~$ netq hostd-11 show impact kubernetes service name calico-etcd 
    calico-etcd -- calico-etcd-pfg9r -- hostd-11:swp1:torbond1 -- swp6:hostbond2:torc-11
                                     -- hostd-11:swp2:torbond1 -- swp6:hostbond2:torc-12
                                     -- hostd-11:swp3:NetQBond-2 -- swp16:NetQBond-16:noc-pr
                                     -- hostd-11:swp4:NetQBond-2 -- swp16:NetQBond-16:noc-se

### <span>Use the NetQ Time Machine Functionality</span>

You can use the ["time machine"
features](https://docs.cumulusnetworks.com/display/NETQ/Methods+for+Diagnosing+Network+Issues#MethodsforDiagnosingNetworkIssues-time_machine)
of NetQ on a Kubernetes cluster, using the `around` and `changes`
commands to go back in time to check the network status and identify any
changes that occurred on the network.

The example below shows the current state of the network. Notice there
is a node named *hosts-23*. hosts-23 is there because the node
*hostd-22* went down and Kubernetes spun up a third replica on a
different host to satisfy the deployment requirement.

    cumulus@redis-1:~$ netq hostd-11 show kubernetes deployment name nginx connectivity
    nginx -- nginx-8586cf59-fqtnj -- hosts-12:swp2:NetQBond-1 -- swp23:NetQBond-23:noc-pr
                                  -- hosts-12:swp3:NetQBond-1 -- swp23:NetQBond-23:noc-se
                                  -- hosts-12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-8g487 -- hosts-24:swp2:NetQBond-1 -- swp29:NetQBond-29:noc-pr
                                  -- hosts-24:swp3:NetQBond-1 -- swp29:NetQBond-29:noc-se
                                  -- hosts-24:swp1:swp1 -- swp8:VlanA-1:tor-2
          -- nginx-8586cf59-2hb8t -- hosts-23:swp1:swp1 -- swp7:VlanA-1:tor-2
                                  -- hosts-23:swp2:NetQBond-1 -- swp28:NetQBond-28:noc-pr
                                  -- hosts-23:swp3:NetQBond-1 -- swp28:NetQBond-28:noc-se

You can see this by going back in time 10 minutes. *hosts-23* was not
present, whereas *hostd-22* **was** present:

    cumulus@redis-1:~$ netq hostd-11 show kubernetes deployment name nginx connectivity around 10m
    nginx -- nginx-8586cf59-fqtnj -- hosts-12:swp2:NetQBond-1 -- swp23:NetQBond-23:noc-pr
                                  -- hosts-12:swp3:NetQBond-1 -- swp23:NetQBond-23:noc-se
                                  -- hosts-12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-2xxs4 -- hostd-22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- hostd-22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- hostd-22:swp3:NetQBond-2 -- swp20:NetQBond-20:noc-pr
                                  -- hostd-22:swp4:NetQBond-2 -- swp20:NetQBond-20:noc-se
          -- nginx-8586cf59-8g487 -- hosts-24:swp2:NetQBond-1 -- swp29:NetQBond-29:noc-pr
                                  -- hosts-24:swp3:NetQBond-1 -- swp29:NetQBond-29:noc-se
                                  -- hosts-24:swp1:swp1 -- swp8:VlanA-1:tor-2
     

You can determine the impact on the Kubernetes deployment in the event a
host or switch goes down. The output is color coded (not shown in the
example below) so you can clearly see the impact: green shows no impact,
yellow shows partial impact, and red shows full impact.

    cumulus@hostd-11:~$ netq torc-21 show impact kubernetes deployment name nginx
    nginx -- nginx-8586cf59-wjwgp -- hostd-22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- hostd-22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- hostd-22:swp3:NetQBond-2 -- swp20:NetQBond-20:noc-pr
                                  -- hostd-22:swp4:NetQBond-2 -- swp20:NetQBond-20:noc-se
          -- nginx-8586cf59-c82ns -- hosts-12:swp2:NetQBond-1 -- swp23:NetQBond-23:noc-pr
                                  -- hosts-12:swp3:NetQBond-1 -- swp23:NetQBond-23:noc-se
                                  -- hosts-12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-26pj5 -- hosts-24:swp2:NetQBond-1 -- swp29:NetQBond-29:noc-pr
                                  -- hosts-24:swp3:NetQBond-1 -- swp29:NetQBond-29:noc-se
                                  -- hosts-24:swp1:swp1 -- swp8:VlanA-1:tor-2
    cumulus@hostd-11:~$ netq hosts-12 show impact kubernetes deployment name nginx
    nginx -- nginx-8586cf59-wjwgp -- hostd-22:swp1:torbond1 -- swp7:hostbond3:torc-21
                                  -- hostd-22:swp2:torbond1 -- swp7:hostbond3:torc-22
                                  -- hostd-22:swp3:NetQBond-2 -- swp20:NetQBond-20:noc-pr
                                  -- hostd-22:swp4:NetQBond-2 -- swp20:NetQBond-20:noc-se
          -- nginx-8586cf59-c82ns -- hosts-12:swp2:NetQBond-1 -- swp23:NetQBond-23:noc-pr
                                  -- hosts-12:swp3:NetQBond-1 -- swp23:NetQBond-23:noc-se
                                  -- hosts-12:swp1:swp1 -- swp6:VlanA-1:tor-1
          -- nginx-8586cf59-26pj5 -- hosts-24:swp2:NetQBond-1 -- swp29:NetQBond-29:noc-pr
                                  -- hosts-24:swp3:NetQBond-1 -- swp29:NetQBond-29:noc-se

## <span>NetQ with Docker Swarm</span>

### <span>NetQ Docker Swarm Support</span>

The NetQ Agent supports Docker version 1.13 (Jan 2017), 17.03 or later,
including Docker Swarm.

The NetQ Agent parses the following Docker events:

  - Image: pull and delete

  - Container: run, stop, start, restart, attach and detach

  - Network: create, connect, disconnect and destroy

Currently, the NetQ Agent does not support:

  - Monitoring Docker volume mount and unmount events

  - Plugin install and deletes

  - Third party network configuration through plugins like Calico

### <span>Telemetry Server Memory Requirement</span>

Due to the higher memory requirements to run containers, Cumulus
Networks recommends you run the NetQ Telemetry Server on a host with at
least 32G RAM. For more information, read the [NetQ user
guide](https://docs.cumulusnetworks.com/display/NETQ/Methods+for+Diagnosing+Network+Issues#MethodsforDiagnosingNetworkIssues-matrixHowFarBackinTimeCanYouTravel?).

### <span id="src-7110909_MonitoringContainerEnvironmentswithNetQ-enable" class="confluence-anchor-link"></span><span>Enable the Monitoring of Docker Containers</span>

In order for NetQ to be able to monitor the containers on a host, you
need to do the following on the host:

1.  Configure the host to point to the telemetry server by its IP
    address. See the [NetQ user
    guide](https://docs.cumulusnetworks.com/display/NETQ/Monitor+Container+Environments)
    for details.

2.  Enable Docker monitoring by NetQ. You can specify a polling period
    between 10 and 120 seconds; 15 seconds is the default.
    
        cumulus@hostd-11:~$ netq config add agent docker-monitor poll-period 20
        Successfully added docker monitor. Please restart netq-agent.

3.  Restart the NetQ agent:
    
        cumulus@server01:~$ netq config restart agent

### <span>Show Container Summary Information</span>

To see a high level view of the network, including the number of
containers installed and running on the network, run `netq show docker
summary`:

    cumulus@server01:~$ netq show docker summary 
    Hostname    Version     Installed    Running    Images    Swarm Cluster    Networks
    ----------  ----------  -----------  ---------  --------  ---------------  ----------
    exit01      17.06.0-ce           26         26         1                            3
    exit02      17.06.0-ce            1          0         3                            3
    server01    17.06.0-ce           14         14         4  default                   5
    server02    17.06.0-ce            0          0         0                            3
    server03    17.06.0-ce            0          0         0                            3
    server04    17.06.0-ce            0          0         0                            3
    server01    17.06.0-ce           13         13         1  default                   3
    server02    17.06.0-ce            0          0         0                            3

### <span>Identify Containers on the Network</span>

To view the different container networks and the containers in them, run
`netq show docker network`:

``` 
cumulus@server01:~$ netq show docker network
Network Name     Hostname   subnet          gateway         ipv6      ip masq. 
---------------- ---------- --------------- --------------- --------- -------- 
bridge           exit01     172.17.0.0/16                   Disabled  True     
bridge           exit02     172.17.0.0/16                   Disabled  True     
bridge           server01   172.17.0.0/16                   Disabled  True     
bridge           server02   172.17.0.0/16                   Disabled  True     
bridge           server03   172.17.0.0/16                   Disabled  True     
bridge           server04   172.17.0.0/16                   Disabled  True     
bridge           server01   172.17.0.0/16                   Disabled  True     
bridge           server02   172.17.0.0/16                   Disabled  True     
bridge           server03   172.17.0.0/16                   Disabled  True     
bridge           server04   172.17.0.0/16                   Disabled  True    
host             exit01                                     Disabled  False    
host             exit02                                     Disabled  False    
host             server01                                   Disabled  False    
host             server02                                   Disabled  False    
host             server03                                   Disabled  False   
host             server04                                   Disabled  False   
host             server01                                   Disabled  False    
host             server02                                   Disabled  False    
host             server03                                   Disabled  False    
host             server04                                   Disabled  False    
none             exit01                                     Disabled  False    
none             exit02                                     Disabled  False    
none             server01                                   Disabled  False    
none             server02                                   Disabled  False    
none             server03                                   Disabled  False    
none             server04                                   Disabled  False    
none             server01                                   Disabled  False    
none             server02                                   Disabled  False    
none             server03                                   Disabled  False    
none             server04                                   Disabled  False    
```

To view all the hosts using a specific container network driver, use
`netq show docker network driver NAME`. Use the `brief` keyword for a
shorter summary. Docker supports many network drivers.

    cumulus@server01:~$ netq show docker network driver bridge brief 
    Network Name     Hostname   Driver    subnet          gateway         IP Masq  Containers
    ---------------- ---------- --------- --------------- --------------- -------- -------------------------
    bridge           exit01     bridge    172.17.0.0/16                   True     Name:netcat-8085 IPv4:172
                                                                                   .17.0.7/16,
                                                                                   Name:netcat-8082 IPv4:172
                                                                                   .17.0.4/16,
                                                                                   Name:netcat-8083 IPv4:172
                                                                                   .17.0.5/16,
                                                                                   Name:netcat-8089 IPv4:172
                                                                                   .17.0.11/16,
                                                                                   Name:netcat-8081 IPv4:172
                                                                                   .17.0.3/16,
                                                                                   Name:netcat-8084 IPv4:172
                                                                                   .17.0.6/16,
                                                                                   Name:netcat-8090 IPv4:172
                                                                                   .17.0.12/16,
                                                                                   Name:netcat-8080 IPv4:172
                                                                                   .17.0.2/16,
                                                                                   Name:netcat-8091 IPv4:172
                                                                                   .17.0.13/16,
                                                                                   Name:netcat-8092 IPv4:172
                                                                                   .17.0.14/16,
                                                                                   Name:netcat-8088 IPv4:172
                                                                                   .17.0.10/16,
                                                                                   Name:netcat-8087 IPv4:172
                                                                                   .17.0.9/16,
                                                                                   Name:netcat-8086 IPv4:172
                                                                                   .17.0.8/16
    bridge           exit02     bridge    172.17.0.0/16                   True     
    bridge           server01   bridge    172.17.0.0/16                   True     
    bridge           server02   bridge    172.17.0.0/16                   True     
    bridge           server03   bridge    172.17.0.0/16                   True     
    bridge           server04   bridge    172.17.0.0/16                   True     
    bridge           server01   bridge    172.17.0.0/16                   True     Name:netcat-8082 IPv4:172
                                                                                   .17.0.4/16,
                                                                                   Name:netcat-8085 IPv4:172
                                                                                   .17.0.7/16,
                                                                                   Name:netcat-8083 IPv4:172
                                                                                   .17.0.5/16,
                                                                                   Name:netcat-8086 IPv4:172
                                                                                   .17.0.8/16,
                                                                                   Name:netcat-8089 IPv4:172
                                                                                   .17.0.11/16,
                                                                                   Name:netcat-8084 IPv4:172
                                                                                   .17.0.6/16,
                                                                                   Name:netcat-8092 IPv4:172
                                                                                   .17.0.14/16,
                                                                                   Name:netcat-8087 IPv4:172
                                                                                   .17.0.9/16,
                                                                                   Name:netcat-8080 IPv4:172
                                                                                   .17.0.2/16,
                                                                                   Name:netcat-8081 IPv4:172
                                                                                   .17.0.3/16,
                                                                                   Name:netcat-8090 IPv4:172
                                                                                   .17.0.12/16,
                                                                                   Name:netcat-8091 IPv4:172
                                                                                   .17.0.13/16,
                                                                                   Name:netcat-8088 IPv4:172
                                                                                   .17.0.10/16
    bridge           server02   bridge    172.17.0.0/16                   True
    bridge           server03   bridge    172.17.0.0/16                   True
    bridge           server04   bridge    172.17.0.0/16                   True

To see all the containers on a given container network, run the
following command, where the container network is named *host*:

    cumulus@server01:~$ netq show docker container network host 
    Container Name       Hostname   Container IP      IP Masq  Network Name   Service Name    UpTime
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    netcat-9080          exit01     45.0.0.17/26,     False    host                           0:29:42
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9081          exit01     45.0.0.17/26,     False    host                           0:29:41
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9082          exit01     45.0.0.17/26,     False    host                           0:29:42
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9083          exit01     45.0.0.17/26,     False    host                           0:29:39
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9084          exit01     45.0.0.17/26,     False    host                           0:29:40
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9085          exit01     45.0.0.17/26,     False    host                           0:29:40
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9086          exit01     45.0.0.17/26,     False    host                           0:29:39
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9087          exit01     45.0.0.17/26,     False    host                           0:29:38
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9088          exit01     45.0.0.17/26,     False    host                           0:29:37
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9089          exit01     45.0.0.17/26,     False    host                           0:29:38
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9090          exit01     45.0.0.17/26,     False    host                           0:29:36
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9091          exit01     45.0.0.17/26,     False    host                           0:29:37
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9092          exit01     45.0.0.17/26,     False    host                           0:29:38
                                    27.0.0.3/32,
                                    192.168.0.15/24

The Service Name column is populated when a container is created by
Docker Swarm for a service:

    cumulus@leaf01:mgmt-vrf:~$ netq show docker container
    Matching container records are:
    Container Name       Hostname   Container IP      IP Masq  Network Name   Service Name    UpTime
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    Web.3.xm2jjbe1l60eje hostd-11   10.255.0.9        False    ingress        Web             16:30:47 
    sgpx8rlq5pf 
    redis2.nh7ouztl2ap79 hostd-21   172.17.0.2        True     bridge         redis2          16:36:52 
    2iyycl5bukfh.lznwsxh
    8jepg65hr16kccxeau 
    redis2.rx8uywzrkm9pj hostd-11   172.17.0.2        True     bridge         redis2          16:36:52 
    e9a81613gfpm.s6fhc09
    1xwoqmkjdi3y1kxm7z 
    Web.1.m72ghox4y2bfeg hosts-21   10.255.0.7        False    ingress        Web             16:30:47
    f1ukeocjhgn
    Web.2.9t9yuv9za28taz hosts-11   10.255.0.8        False    ingress        Web             16:30:46
    3mee6pr8d11
    Web.3.kv0icnnh7fxb45 hosts-21   10.255.0.11       False    ingress        Web             14:31:58

### <span>Show Container Adjacency</span>

NetQ can list all the containers running on hosts adjacent to a top of
rack switch. This helps in analyzing what impact the ToR switch can have
on an application

To identify all the containers that may have been launched on hosts that
are adjacent to a given node, run `netq NODE show docker container
adjacent`:

    cumulus@leaf01:~$ netq leaf01 show docker container adjacent
    Interface            Peer Node  Peer Interface        Container Name       IP                   Network    Service Name
    -------------------- ---------- --------------------- -------------------- -------------------- ---------- ---------------
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9090                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9082                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9091                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9086                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9081                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9083                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9087                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9088                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9085                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9080                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9084                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9089                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9092                               host
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8089          172.17.0.11          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8084          172.17.0.6           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8092          172.17.0.14          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8083          172.17.0.5           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8085          172.17.0.7           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8081          172.17.0.3           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8080          172.17.0.2           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8086          172.17.0.8           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8088          172.17.0.10          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8082          172.17.0.4           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8091          172.17.0.13          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8090          172.17.0.12          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8091          172.17.0.13          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8083          172.17.0.5           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8082          172.17.0.4           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8080          172.17.0.2           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8092          172.17.0.14          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8086          172.17.0.8           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8084          172.17.0.6           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8088          172.17.0.10          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8090          172.17.0.12          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8085          172.17.0.7           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8089          172.17.0.11          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8081          172.17.0.3           bridge

You can filter this output for a given interface:

    cumulus@leaf01:~$ netq leaf01 show docker container adjacent interfaces swp6
    Interface            Peer Node  Peer Interface        Container Name       IP                   Network    Service Name
    -------------------- ---------- --------------------- -------------------- -------------------- ---------- ---------------
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9090                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9082                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9091                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9086                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9081                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9083                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9087                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9088                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9085                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9080                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9084                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9089                               host                                7
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9092                               host

### <span>Show Container-specific Information</span>

You can see information about a given container by running `netq show
docker container name NAME`:

    cumulus@server01:~$ netq show docker container name netcat-9092
    Name                 Node       IP                IP Masq. Network        Service Name    Up time
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    netcat-9092          exit01     45.0.0.17/26,     False    host                           0:34:15
                                    27.0.0.3/32,
                                    192.168.0.15/24

### <span>Show Containers with a Specific Image</span>

To search for all the containers on the network with a specific Docker
image, run `netq show docker container image IMAGE_NAME`:

    cumulus@server01:~$ netq show docker container image chilcano/netcat:jessie 
    Name                 Node       IP                IP Masq. Network        Service Name    Up time
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    netcat-8080          exit01     172.17.0.2        True     bridge                         0:32:09
    netcat-8080          server01   172.17.0.2        True     bridge                         0:23:11
    netcat-8081          exit01     172.17.0.3        True     bridge                         0:32:07
    netcat-8081          server01   172.17.0.3        True     bridge                         0:23:10
    netcat-8082          exit01     172.17.0.4        True     bridge                         0:32:08
    netcat-8082          server01   172.17.0.4        True     bridge                         0:23:08
    netcat-8083          exit01     172.17.0.5        True     bridge                         0:32:07
    netcat-8083          server01   172.17.0.5        True     bridge                         0:23:07
    netcat-8084          exit01     172.17.0.6        True     bridge                         0:32:07
    netcat-8084          server01   172.17.0.6        True     bridge                         0:23:09
    netcat-8085          exit01     172.17.0.7        True     bridge                         0:32:05
    netcat-8085          server01   172.17.0.7        True     bridge                         0:23:06
    netcat-8086          exit01     172.17.0.8        True     bridge                         0:32:06
    netcat-8086          server01   172.17.0.8        True     bridge                         0:23:06
    netcat-8087          exit01     172.17.0.9        True     bridge                         0:32:05
    netcat-8087          server01   172.17.0.9        True     bridge                         0:23:06
    netcat-8088          exit01     172.17.0.10       True     bridge                         0:32:04
    netcat-8088          server01   172.17.0.10       True     bridge                         0:23:06
    netcat-8089          exit01     172.17.0.11       True     bridge                         0:32:02
    netcat-8089          server01   172.17.0.11       True     bridge                         0:23:03
    netcat-8090          exit01     172.17.0.12       True     bridge                         0:32:01
    netcat-8090          server01   172.17.0.12       True     bridge                         0:23:05
    netcat-8091          exit01     172.17.0.13       True     bridge                         0:32:03
    netcat-8091          server01   172.17.0.13       True     bridge                         0:23:04
    netcat-8092          exit01     172.17.0.14       True     bridge                         0:31:59
    netcat-8092          server01   172.17.0.14       True     bridge                         0:23:03
    netcat-9080          exit01     45.0.0.17/26,     False    host                           0:31:51
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9081          exit01     45.0.0.17/26,     False    host                           0:31:51
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9082          exit01     45.0.0.17/26,     False    host                           0:31:52
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9083          exit01     45.0.0.17/26,     False    host                           0:31:49
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9084          exit01     45.0.0.17/26,     False    host                           0:31:50
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9085          exit01     45.0.0.17/26,     False    host                           0:31:50
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9086          exit01     45.0.0.17/26,     False    host                           0:31:48
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9087          exit01     45.0.0.17/26,     False    host                           0:31:48
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9088          exit01     45.0.0.17/26,     False    host                           0:31:47
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9089          exit01     45.0.0.17/26,     False    host                           0:31:48
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9090          exit01     45.0.0.17/26,     False    host                           0:31:46
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9091          exit01     45.0.0.17/26,     False    host                           0:31:47
                                    27.0.0.3/32,
                                    192.168.0.15/24
    netcat-9092          exit01     45.0.0.17/26,     False    host                           0:31:47
                                    27.0.0.3/32,
                                    192.168.0.15/24

### <span>Show Container Connectivity</span>

To determine how a particular container is attached to a network, run
`netq HOST show docker container network NAME connectivity`. The output
tells you what host it's launched on, adjacent nodes, adjacent ports.

    cumulus@leaf01:~$ netq server01 show docker container network host connectivity 
    Name            Swarm Service Cont IP         Network    Node       Port                 Peer Node  Peer Port
    --------------- ------------- --------------- ---------- ---------- -------------------- ---------- --------------------
    netcat-9080                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9080                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9080                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9081                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9081                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9081                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9082                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9082                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9082                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9083                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9083                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9083                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9084                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9084                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9084                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9085                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9085                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9085                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9086                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9086                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9086                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9087                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9087                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9087                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9088                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9088                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9088                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9089                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9089                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9089                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9090                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9090                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9090                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9091                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9091                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9091                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1
    netcat-9092                                   host       server01   swp2:NetQBond-1      noc-pr     swp21:NetQBond-19
    netcat-9092                                   host       server01   swp3:NetQBond-1      noc-se     swp21:NetQBond-19
    netcat-9092                                   host       server01   swp1:swp1            tor-1      Local Node tor-1 and
                                                                                                        Ports swp6 <==> Remo
                                                                                                        te  Node/s hosts-11
                                                                                                        and Ports swp1

### <span>Show Network Traffic over a Given Protocol</span>

You can specify either the TCP or UDP protocol when you observe a given
flow of traffic on the network and want to identify which container sent
or received traffic using that protocol from a given port.

    cumulus@tor-1:mgmt-vrf:~$ netq hosts-11 show docker container 6.0.1.5 tcp 
    Container Name       Node       Proto  Port     Cont IP           Network        Host IP               Host Port
    -------------------- ---------- ------ -------- ----------------- -------------- --------------------- ------------
    netcat-9080          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9080          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9081          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9081          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9082          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9082          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9083          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9083          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9084          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9084          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9085          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9085          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9086          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9086          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9087          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9087          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9088          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9088          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9089          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9089          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9090          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9090          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9091          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9091          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182
    netcat-9092          server01   tcp    9192                       host           6.0.1.5/26:swp1.1004  9192
    netcat-9092          server01   tcp    8182                       host           6.0.1.5/26:swp1.1004  8182

### <span>Show Docker Swarm Clusters and Networks</span>

To see the elements of a Docker Swarm cluster, run:

    cumulus@server05:~$ netq show docker swarm cluster
    Matching swarm records are:
    Cluster Name    Num Nodes Manager Nodes                            Worker Nodes
    --------------- --------- ---------------------------------------- ------------------------------
    default         3         server01:45.0.0.20:2377,                 server01, server02, server03
                              server02:45.0.0.24:2377
    default         2         server05:45.0.0.27:2377                  server04, server05

You can output the results to JSON:

    cumulus@server01:~$ netq show docker swarm cluster json
    {
        "swarm": [
            {
                "clusterName": "default",
                "managerNodes": "server01:45.0.0.20:2377, server02:45.0.0.24:2377",
                "workerNodes": "server01, server02, server03",
                "numNodes": 3
            },
            {
                "clusterName": "default",
                "managerNodes": "server05:45.0.0.27:2377",
                "workerNodes": "server04, server05",
                "numNodes": 2
            }
        ],
        "truncatedResult": false
    }

You can see the changes made to the cluster:

    cumulus@server05:~$ netq server01 show docker swarm cluster changes
    Matching swarm records are:
    Hostname    Cluster Name    Num Nodes  Manager Nodes                            Worker Nodes                   DBState    Last changed
    ------------ --------------- --------- ---------------------------------------- ------------------------------ ---------- --------------------
    server01    default         3          server01:45.0.0.20:2377,                 server01, server02, server03   Add        12:54.9260 ago
                                           server02:45.0.0.24:2377
    server01    default         2          server01:45.0.0.20:2377,                 server01, server02             Add        14:10.5203 ago
                                           server02:45.0.0.24:2377

You can show the nodes in a swarm:

    cumulus@server05:~$ netq show docker swarm node
    Matching swarm records are:
    Swarm Node    Node Id                    Cluster Name    Role     Docker Version    State    Availability
    ------------  -------------------------  --------------  -------  ----------------  -------  --------------
    server01      knyao3pkk8h872cep3vabrpum  default         manager  17.06.1-ce        ready    active
    server02      jatmsbs71rv9nmqw5grqncqw2  default         manager  17.06.1-ce        ready    active
    server03      tqrj8ro7b1ycymihquawr1szr  default         worker   17.06.1-ce        ready    active
    server04      gwp89587uujywot6d2fo5vi3e  default         worker   17.06.1-ce        ready    active
    server05      26boo6bak3exgi6nox8dmm2o2  default         manager  17.06.1-ce        ready    active

You can drill down to get information about a specific node in a swarm:

    cumulus@server05:~$ netq show docker swarm cluster node-name server04
    Matching swarm records are:
    Cluster Name    Num Nodes Manager Nodes                            Worker Nodes
    --------------- --------- ---------------------------------------- ------------------------------
    default         2         server05:45.0.0.27:2377                  server04, server05
     

To travel back in time, run:

    cumulus@server05:~$ netq show docker swarm cluster node-name server04 around 10m
    Matching swarm records are:
    Cluster Name    Num Nodes Manager Nodes                            Worker Nodes
    --------------- --------- ---------------------------------------- ------------------------------
    default         2         server05:45.0.0.27:2377                  server04, server05

For details about a Docker Swarm network, run:

    cumulus@server01:~$ netq show docker swarm network nginx
    Matching swarm records are:
    Service Name    Port Mapping               Virtual IP      Network Name
    --------------  -------------------------  --------------  --------------
    nginx           tcp:9080:80, tcp:9443:443  10.255.0.12/16  ingress

### <span>Show Docker Service Connectivity and Impact</span>

You can show the Docker services in a cluster:

    cumulus@server02:~$ netq show docker service
    Matching service records are:
    Service Name    Manager    Cluster    Mode        Replicas    Running
    --------------  ---------  ---------  ----------  ----------  ---------
    redis           server01   default    Replicated           6          6
    redis           server02   default    Replicated           6          6

And get detailed information about a Docker service:

    cumulus@server01:~$ netq show docker container service redis
    Matching container records are:
    Container Name       Hostname   Container IP      IP Masq  Network Name   Service Name    UpTime
    -------------------- ---------- ----------------- -------- -------------- --------------- ---------------
    redis.1.d3k6fyx3cmdn server01   10.255.0.6        False    ingress        redis           0:07:11
    3y5tr0uveuenk
    redis.2.qcs7kt3si79i server02   10.255.0.11       False    ingress        redis           0:06:42
    s98tdkbid9k03
    redis.3.kh4bvgcpmnfg server02   10.255.0.7        False    ingress        redis           0:06:41
    hvihbx2oi9xb0
    redis.4.48h1jm5gq3u9 server03   10.255.0.8        False    ingress        redis           0:06:42
    rmtb68lzap6kp
    redis.5.kz1djm3gczst server03   10.255.0.9        False    ingress        redis           0:06:42
    w8xf34oa9592z
    redis.6.jicycmsbe8qj server01   10.255.0.10       False    ingress        redis           0:06:50
    kw2m5c1mn7dxb

To see the connectivity of a given Docker service, run:

    cumulus@server01:~$ netq show docker service name redis connectivity
    redis -- redis.3.kh4bvgcpmnfghvihbx2oi9xb0 -- server02 -- leaf01
                                                        -- exit01
                                                        -- leaf05
        -- redis.5.kz1djm3gczstw8xf34oa9592z -- server03 -- leaf05
                                                        -- leaf01
                                                        -- exit01
        -- redis.1.d3k6fyx3cmdn3y5tr0uveuenk -- server01 -- leaf03
                                                        -- leaf02
                                                        -- leaf01
                                                        -- exit01
        -- redis.6.jicycmsbe8qjkw2m5c1mn7dxb -- server01 -- leaf03
                                                        -- leaf02
                                                        -- leaf01
                                                        -- exit01
        -- redis.4.48h1jm5gq3u9rmtb68lzap6kp -- server03 -- leaf05
                                                        -- leaf01
                                                        -- exit01
        -- redis.2.qcs7kt3si79is98tdkbid9k03 -- server02 -- leaf01
                                                        -- exit01
                                                        -- leaf05

To see the impact of a given Docker service, run:

    cumulus@server01:~$ netq leaf05 show impact docker service redis
    redis -- redis.3.kh4bvgcpmnfghvihbx2oi9xb0 -- server02 -- leaf01
                                                        -- exit01
                                                        -- leaf05
        -- redis.5.kz1djm3gczstw8xf34oa9592z -- server03 -- leaf05
                                                        -- leaf01
                                                        -- exit01
        -- redis.1.d3k6fyx3cmdn3y5tr0uveuenk -- server01 -- leaf03
                                                        -- leaf02
                                                        -- leaf01
                                                        -- exit01
        -- redis.6.jicycmsbe8qjkw2m5c1mn7dxb -- server01 -- leaf03
                                                        -- leaf02
                                                        -- leaf01
                                                        -- exit01
        -- redis.4.48h1jm5gq3u9rmtb68lzap6kp -- server03 -- leaf05
                                                        -- leaf01
                                                        -- exit01
        -- redis.2.qcs7kt3si79is98tdkbid9k03 -- server02 -- leaf01
                                                        -- exit01
                                                        -- leaf05

### <span>Use the NetQ Time Machine Functionality</span>

You can use the ["time machine"
features](https://docs.cumulusnetworks.com/display/NETQ/Methods+for+Diagnosing+Network+Issues#MethodsforDiagnosingNetworkIssues-time_machine)
of NetQ on a Docker container, using the `around` and `changes` commands
to go back in time to check the network status and identify any changes
that occurred on the network.

The example below shows the state of the network one hour earlier.

    cumulus@leaf01:~$ netq leaf01 show docker container adjacent around 1h
    Interface            Peer Node  Peer Interface        Container Name       IP                   Network    Service Name
    -------------------- ---------- --------------------- -------------------- -------------------- ---------- ---------------
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9090                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9082                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9091                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9086                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9081                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9083                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9087                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9088                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9085                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9080                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9084                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9089                               host
    swp6:VlanA-1         server01   mac:00:02:00:00:00:27 netcat-9092                               host
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8089          172.17.0.11          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8084          172.17.0.6           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8092          172.17.0.14          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8083          172.17.0.5           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8085          172.17.0.7           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8081          172.17.0.3           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8080          172.17.0.2           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8086          172.17.0.8           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8088          172.17.0.10          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8082          172.17.0.4           bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8091          172.17.0.13          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8090          172.17.0.12          bridge
    swp7:VlanA-1         server02   mac:00:02:00:00:00:2a netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8091          172.17.0.13          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8083          172.17.0.5           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8087          172.17.0.9           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8082          172.17.0.4           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8080          172.17.0.2           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8092          172.17.0.14          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8086          172.17.0.8           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8084          172.17.0.6           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8088          172.17.0.10          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8090          172.17.0.12          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8085          172.17.0.7           bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8089          172.17.0.11          bridge
    swp8:VlanA-1         server03   mac:00:02:00:00:00:2d netcat-8081          172.17.0.3           bridge
