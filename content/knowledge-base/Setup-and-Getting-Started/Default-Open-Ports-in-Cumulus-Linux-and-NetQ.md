---
title: Default Open Ports in Cumulus Linux and NetQ
author: NVIDIA
weight: 106
toc: 3
---

## Cumulus Linux Ports

When a switch running Cumulus Linux 3.2 or later boots up, it opens the following ports:

| Internet Protocol | Port | Protocol |
| ----------------- | ---- | -------- |
| TCP  | 22             | Secure Shell (ssh)                                 |
| TCP  | 53             | DNS forwarder and DHCP server (dnsmasq) (RMP only) |
| TCP6 | 22             | Secure Shell (ssh)                                 |
| TCP6 | 53             | DNS forwarder and DHCP server (dnsmasq) (RMP Only) |
| UDP  | 53             | DNS forwarder and DHCP server (dnsmasq) (RMP Only) |
| UDP  | 68\*           | DHCP client (dhclient)                             |
| UDP  | 123            | Network Time Protocol (ntp)                        |
| UDP  | 3784/3785/4784 | Prescriptive Topology Manager (ptm)                |
| UDP6 | 53             | DNS forwarder and DHCP server (dnsmasq) (RMP Only) |
| UDP6 | 123            | Network Time Protocol (ntp)                        |
| UDP6 | 3784/4784      | Prescriptive Topology Manager (ptm)                |
| UDP6 | \*             | DHCP client (dhclient)                             |

*\*Has a dynamically assigned port.*

You can see the ports with the following command:

    cumulus@switch:~$ sudo netstat -nlp --inet --inet6

## Active Internet Connections (only servers)

| Protocol | Recv-Q | Send-Q | Local Address           | Foreign Address | State  | PID/Program name |
| -------- | ------ | ------ | ----------------------- | --------------- | ------ | ---------------- |
| tcp      | 0      | 0      | 0.0.0.0:53              | 0.0.0.0:\*      | LISTEN | 444/dnsmasq      |
| tcp      | 0      | 0      | 0.0.0.0:22              | 0.0.0.0:\*      | LISTEN | 874/sshd         |
| tcp6     | 0      | 0      | :::53                   | :::\*           | LISTEN | 444/dnsmasq      |
| tcp6     | 0      | 0      | :::22                   | :::\*           | LISTEN | 874/sshd         |
| udp      | 0      | 0      | 0.0.0.0:28450           | 0.0.0.0:\*      |        | 839/dhclient     |
| udp      | 0      | 0      | 0.0.0.0:53              | 0.0.0.0:\*      |        | 444/dnsmasq      |
| udp      | 0      | 0      | 0.0.0.0:68              | 0.0.0.0:\*      |        | 839/dhclient     |
| udp      | 0      | 0      | 192.168.0.42:123        | 0.0.0.0:\*      |        | 907/ntpd         |
| udp      | 0      | 0      | 127.0.0.1:123           | 0.0.0.0:\*      |        | 907/ntpd         |
| udp      | 0      | 0      | 0.0.0.0:123             | 0.0.0.0:\*      |        | 907/ntpd         |
| udp      | 0      | 0      | 0.0.0.0:4784            | 0.0.0.0:\*      |        | 909/ptmd         |
| udp      | 0      | 0      | 0.0.0.0:3784            | 0.0.0.0:\*      |        | 909/ptmd         |
| udp      | 0      | 0      | 0.0.0.0:3785            | 0.0.0.0:\*      |        | 909/ptmd         |
| udp6     | 0      | 0      | :::58352                | :::\*           |        | 839/dhclient     |
| udp6     | 0      | 0      | :::53                   | :::\*           |        | 444/dnsmasq      |
| udp6     | 0      | 0      | fe80::a200:ff:fe00::123 | :::\*           |        | 907/ntpd         |
| udp6     | 0      | 0      | ::1:123                 | :::\*           |        | 907/ntpd         |
| udp6     | 0      | 0      | :::123                  | :::\*           |        | 907/ntpd         |
| udp6     | 0      | 0      | :::4784                 | :::\*           |        | 909/ptmd         |
| udp6     | 0      | 0      | :::3784                 | :::\*           |        | 909/ptmd         |

*\*Has a dynamically assigned port.*

## NetQ Ports

The following ports must be open to use the NetQ 2.4 and later software:

| Port     | Protocol     | Access                   |
| -------- | ------------ | ------------------------ |
| 31980    | TCP          | NetQ Agent Communication |
| 443      | TCP          | NetQ UI                  |
| 8443     | TCP          | Admin UI                 |
| 32708    | TCP          | API Gateway              |
| 22       | TCP          | SSH                      |

For cluster-based deployments, the following ports must also be open for internal cluster communication:

| Port     | Protocol     | Access                          |
| -------- | ------------ | ------------------------------- |
| 8080     | TCP          | Admin API                       |
| 5000     | TCP          | Docker Registry                 |
| 8472     | UDP          | Flannel port for VXLAN          |
| 6443     | TCP          | Kubernetes API server           |
| 10250    | TCP          | Kubelet health probe            |
| 2379     | TCP          | etcd                            |
| 2380     | TCP          | etcd                            |
| 7072     | TCP          | Kafka JMX monitoring            |
| 9092     | TCP          | Kafka client                    |
| 7071     | TCP          | Cassandra JMX monitoring        |
| 7000     | TCP          | Cassandra cluster communication |
| 9042     | TCP          | Cassandra client                |
| 7073     | TCP          | Zookeeper JSM monitoring        |
| 2888     | TCP          | Zookeeper cluster communication |
| 3888     | TCP          | Zookeeper cluster communication |
| 2181     | TCP          | Zookeeper client                |
