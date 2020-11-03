---
title: OSPF Configuration Example
author: Cumulus Networks
weight: 840
toc: 3
---
This section shows an OSPF configuration example based on the reference topology. The example configures OSPF *unnumbered* on all leafs and spines. MLAG is configured on leaf01 and leaf02, and on leaf03 and leaf04.

{{< img src = "/images/cumulus-linux/ospf-example-top.png" >}}

### /etc/network/interfaces

{{< tabs "TabID901 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/network/interfaces

```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/network/interfaces

```

{{< /tab >}}

{{< tab "leaf03 ">}}

```

```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/network/interfaces

```

{{< /tab >}}

{{< tab "spine01 ">}}

```

```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/network/interfaces

```

{{< /tab >}}

{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces

```

{{< /tab >}}

{{< tab "border02 ">}}

```
cumulus@border01:~$ sudo cat /etc/network/interfaces

```

{{< /tab >}}

{{< /tabs >}}

**/etc/frr/frr.conf**

{{< tabs "TabID944 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!

```

{{< /tab >}}

{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!

```

{{< /tab >}}

{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!

```

{{< /tab >}}

{{< tab "leaf04 ">}}

```
cumulus@leaf04:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!

```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!

```

{{< /tab >}}

{{< tab "spine02 ">}}

```
cumulus@spine02:~$ sudo cat /etc/frr/frr.conf
...
log syslog informational
!

```

{{< /tab >}}

{{< tab "border01 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf

```

{{< /tab >}}

{{< tab "border02 ">}}

```
cumulus@border01:~$ sudo cat /etc/frr/frr.conf

```

{{< /tab >}}

{{< /tabs >}}
