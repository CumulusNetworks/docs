---
title: Prescriptive Topology Manager - PTM
author: NVIDIA
weight: 370
toc: 3
---
In data center topologies, right cabling is time consuming and error prone. <span style="background-color:#F5F5DC">[PTM](## "Prescriptive Topology Manager")</span> is a dynamic cabling verification tool that can detect and eliminate errors. PTM uses a Graphviz-DOT specified network cabling plan in a `topology.dot` file and couples it with runtime information from LLDP to verify that the cabling matches the specification. The check occurs on every link transition on each node in the network.

You can customize the `topology.dot` file to control `ptmd` at both the global/network level and the node/port level.

PTM runs as a daemon, named `ptmd`.

## Supported Features

- Topology verification using <span style="background-color:#F5F5DC">[LLDP](## "Link Layer Discovery Protocol")</span>. `ptmd` creates a client connection to the LLDP daemon, `lldpd`, and retrieves the neighbor relationship between the nodes/ports in the network and compares them against the prescribed topology specified in the `topology.dot` file.
- PTM only supports physical interfaces, such as swp1 or eth0. You cannot specify virtual interfaces, such as bonds or subinterfaces in the topology file.
- Cumulus Linux does not support forwarding path failure detection using {{<exlink url="http://tools.ietf.org/html/rfc5880" text="Bidirectional Forwarding Detection">}} (BFD); however, you can use demand mode. For more information on how BFD operates in Cumulus Linux, refer to {{<link title="Bidirectional Forwarding Detection - BFD">}} and `man ptmd(8)`.
- Integration with <span style="background-color:#F5F5DC">[FRR](## "FRRouting")</span> (PTM to FRR notification).
- Client management: `ptmd` creates an abstract named socket `/var/run/ptmd.socket` on startup. Other applications can connect to this socket to receive notifications and send commands.
- Event notifications: see Scripts below.
- User configuration through a `topology.dot` file; {{<link url="#configure-ptm" text="see below">}}.

## Configure PTM

`ptmd` verifies the physical network topology against a DOT-specified network graph file, `/etc/ptm.d/topology.dot`.

PTM supports {{<exlink url="http://en.wikipedia.org/wiki/DOT_%28graph_description_language%29" text="undirected graphs">}}.

At startup, `ptmd` connects to `lldpd` (the LLDP daemon) over a Unix socket and retrieves the neighbor name and port information. It then compares the retrieved port information with the configuration information that it reads from the topology file. If there is a match, it is a PASS, otherwise it is a FAIL.

{{%notice note%}}
PTM performs its LLDP neighbor check using the PortID ifname TLV information.
{{%/notice%}}

## ptmd Scripts

`ptmd` executes scripts at `/etc/ptm.d/if-topo-pass` and `/etc/ptm.d/if-topo-fail`for each interface that goes through a change and runs `if-topo-pass` when an LLDP or BFD check passes or `if-topo-fails` when the check fails. The scripts receive an argument string that is the result of the `ptmctl` command; see {{%link url="#ptmd-service-commands" text="`ptmd` commands below"%}}.

You can modify these default scripts.

## Configuration Parameters

You can configure `ptmd` parameters in the topology file. The parameters are host-only, global, per-port/node and templates.

<!-- vale off -->
<!-- Vale issue #253 -->
### Host-only Parameters
<!-- vale on -->
*Host-only parameters* apply to the entire host on which PTM is running. You can include the `hostnametype` host-only parameter, which specifies if PTM uses only the hostname (`hostname`) or the fully qualified domain name (`fqdn`) while looking for the `self-node` in the graph file. For example, in the graph file below PTM ignores the FQDN and only looks for *switch04* because that is the hostname of the switch on which it is running:

{{%notice tip%}}
- Always wrap the hostname in double quotes; for example, `"www.example.com"` to prevent `ptmd` from failing.
- To avoid errors when starting the `ptmd` process, make sure that `/etc/hosts` and `/etc/hostname` both reflect the hostname you are using in the `topology.dot` file.
{{%/notice%}}

```
graph G {
          hostnametype="hostname"
          BFD="upMinTx=150,requiredMinRx=250"
          "cumulus":"swp44" -- "switch04.cumulusnetworks.com":"swp20"
          "cumulus":"swp46" -- "switch04.cumulusnetworks.com":"swp22"
}
```

In this next example, PTM compares using the FQDN and looks for *switch05.cumulusnetworks.com*, which is the FQDN of the switch ion which it is running:

```
graph G {
          hostnametype="fqdn"
          "cumulus":"swp44" -- "switch05.cumulusnetworks.com":"swp20"
          "cumulus":"swp46" -- "switch05.cumulusnetworks.com":"swp22"
}
```

### Global Parameters

*Global parameters* apply to every port in the topology file. There are two global parameters: LLDP and BFD. LLDP is on by default; if no keyword is present, PTM uses the default values for all ports. However, BFD is off if no keyword is present unless a per-port override exists. For example:

```
graph G {
          LLDP=""
          BFD="upMinTx=150,requiredMinRx=250,afi=both"
          "cumulus":"swp44" -- "qct-ly2-04":"swp20"
          "cumulus":"swp46" -- "qct-ly2-04":"swp22"
}
```

<!-- vale off -->
<!-- Vale issue #253 -->
### Per-port Parameters
<!-- vale on -->
*Per-port parameters* provide finer-grained control at the port level. These parameters override any global or compiled defaults. For example:

```
graph G {
          LLDP=""
          BFD="upMinTx=300,requiredMinRx=100"
          "cumulus":"swp44" -- "qct-ly2-04":"swp20" [BFD="upMinTx=150,requiredMinRx=250,afi=both"]
          "cumulus":"swp46" -- "qct-ly2-04":"swp22"
}
```

### Templates

*Templates* provide flexibility in choosing different parameter combinations and applying them to a given port. A template instructs `ptmd` to reference a named parameter string instead of a default one. There are two parameter strings `ptmd` supports:

- `bfdtmpl` specifies a custom parameter tuple for BFD.
- `lldptmpl` specifies a custom parameter tuple for LLDP.

For example:

```
graph G {
          LLDP=""
          BFD="upMinTx=300,requiredMinRx=100"
          BFD1="upMinTx=200,requiredMinRx=200"
          BFD2="upMinTx=100,requiredMinRx=300"
          LLDP1="match_type=ifname"
          LLDP2="match_type=portdescr"
          "cumulus":"swp44" -- "qct-ly2-04":"swp20" [BFD="bfdtmpl=BFD1", LLDP="lldptmpl=LLDP1"]
          "cumulus":"swp46" -- "qct-ly2-04":"swp22" [BFD="bfdtmpl=BFD2", LLDP="lldptmpl=LLDP2"]
          "cumulus":"swp46" -- "qct-ly2-04":"swp22"
}
```

In this template, LLDP1 and LLDP2 are templates for LLDP parameters. BFD1 and BFD2 are templates for BFD parameters.

### Supported BFD and LLDP Parameters

`ptmd` supports the following <span style="background-color:#F5F5DC">[BFD](## "Bidirectional Forwarding Detection")</span> parameters:

- `upMinTx` is the minimum transmit interval, which defaults to *300ms*, specified in milliseconds.
- `requiredMinRx` is the minimum interval between received BFD packets, which defaults to *300ms*, specified in milliseconds.
- `detectMult` is the detect multiplier, which defaults to *3*, and can be any non-zero value.
- `afi` is the address family for the edge. The address family must be one of the following:
  - *v4*: BFD sessions build for only IPv4 connected peers. This is the default value.
  - *v6*: BFD sessions build for only IPv6 connected peers.
  - *both*: BFD sessions builds for both IPv4 and IPv6 connected peers.

The following is an example of a topology with BFD at the port level:

```
graph G {
          "cumulus-1":"swp44" -- "cumulus-2":"swp20" [BFD="upMinTx=300,requiredMinRx=100,afi=v6"]
          "cumulus-1":"swp46" -- "cumulus-2":"swp22" [BFD="detectMult=4"]
}
```

`ptmd` supports the following LLDP parameters:
- `match_type`, which defaults to the interface name (`ifname`), but can accept a port description (`portdescr`) instead if you want `lldpd` to compare the topology against the port description instead of the interface name. You can set this parameter globally or at the per-port level.
- `match_hostname`, which defaults to the hostname (`hostname`), but enables PTM to match the topology using the fully qualified domain name (`fqdn`) supplied by LLDP.

The following is an example of a topology with LLDP at the port level:

```
graph G {
          "cumulus-1":"swp44" -- "cumulus-2":"swp20" [LLDP="match_hostname=fqdn"]
          "cumulus-1":"swp46" -- "cumulus-2":"swp22" [LLDP="match_type=portdescr"]
}
```

{{%notice note%}}
When you specify `match_hostname=fqdn`, `ptmd` matches the entire FQDN, (*cumulus-2.domain.com* in the example below). If you do not specify anything for `match_hostname`, `ptmd` matches based on hostname only, (*cumulus-3* below), and ignores the rest of the URL:

```
graph G {
          "cumulus-1":"swp44" -- "cumulus-2.domain.com":"swp20" [LLDP="match_hostname=fqdn"]
          "cumulus-1":"swp46" -- "cumulus-3":"swp22" [LLDP="match_type=portdescr"]
}
```
{{%/notice%}}

## BFD

<span style="background-color:#F5F5DC">[BFD](## "Bidirectional Forwarding Detection")</span> provides low overhead and rapid detection of failures in the paths between two network devices. It provides a unified mechanism for link detection over all media and protocol layers. Use BFD to detect failures for IPv4 and IPv6 single or multihop paths between any two network devices, including unidirectional path failure detection. For information about configuring BFD using PTM, see {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}}.

## Check Link State

You can enable PTM to perfom additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that `ptmd` defines.

{{%notice note%}}
You only need to enable PTM to check link state. You do not need to enable PTM to determine BFD status.
{{%/notice%}}

{{< tabs "TabID185 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router ptm enable
cumulus@switch:~$ nv config apply
```

To disable the check link state:

```
cumulus@switch:~$ nv unset router ptm enable
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# ptm-enable
switch(config)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

To disable the check link state, set the `no ptm-enable` parameter:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# no ptm-enable
switch(config)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

To check PTM status on an interface, run the `net show interface <interface>` command or the vtysh `show interface <interface>` command.

```
cumulus@switch:~$ net show interface swp4
       Name  MAC                Speed  MTU   Mode
-----  ----  -----------------  -----  ----  -------------
ADMDN  swp4  48:b0:2d:59:0a:de  N/A    1500  NotConfigured

Routing
-------
Interface swp4 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
  vrf: default
  index 3 metric 0 mtu 1550 speed 4294967295
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  Type: Ethernet
  HWaddr: c4:54:44:bd:01:41
...
```

## ptmd Service Commands

PTM sends client notifications in CSV format.

To start or restart the `ptmd` service, run the following command. The `topology.dot` file must be present for the service to start.

```
cumulus@switch:~$ sudo systemctl start|restart|force-reload ptmd.service
```

To instruct `ptmd` to read the `topology.dot` file again to apply the new configuration to the running state without restarting:

```
cumulus@switch:~$ sudo systemctl reload ptmd.service
```

To stop the `ptmd` service:

```
cumulus@switch:~$ sudo systemctl stop ptmd.service
```

To retrieve the current running state of `ptmd`:

```
cumulus@switch:~$ sudo systemctl status ptmd.service
```

## ptmctl Commands

`ptmctl` is a client of `ptmd` that retrieves the operational state of the ports configured on the switch and information about BFD sessions from `ptmd`. `ptmctl` parses the CSV notifications sent by `ptmd`. See `man ptmctl` for more information.

### ptmctl Examples

The examples below contain the following keywords in the output of the `cbl status` column:

| `cbl` status Keyword<img width=200/> | Definition<img width=400/> |
|-------- |-------- |
| pass | The topology file defines the interface, the interface receives LLDP information, and the LLDP information for the interface matches the information in the topology file. |
| fail | The topology file defines the interface, the interface receives LLDP information, and the LLDP information for the interface does not match the information in the topology file. |
| N/A | The topology file defines the interface but the interface does not receive LLDP information. The interface might be down or disconnected, or the neighbor is not sending LLDP packets.<br>The `N/A` and `fail` status might indicate a wiring problem to investigate.<br>The `N/A` status does not show when you use the `-l` option with `ptmctl`; The output shows only interfaces that are receiving LLDP information. |

For basic output, use `ptmctl` without any options:

```
cumulus@switch:~$ sudo ptmctl

-------------------------------------------------------------
port  cbl     BFD     BFD                  BFD    BFD
      status  status  peer                 local  type
-------------------------------------------------------------
swp1  pass    pass    11.0.0.2             N/A    singlehop
swp2  pass    N/A     N/A                  N/A    N/A
swp3  pass    N/A     N/A                  N/A    N/A
```

For more detailed output, use the `-d` option:

```
cumulus@switch:~$ sudo ptmctl -d

--------------------------------------------------------------------------------------
port  cbl    exp     act      sysname  portID  portDescr  match  last    BFD   BFD
      status nbr     nbr                                  on     upd     Type  state
--------------------------------------------------------------------------------------
swp45 pass   h1:swp1 h1:swp1  h1       swp1    swp1       IfName 5m: 5s  N/A   N/A
swp46 fail   h2:swp1 h2:swp1  h2       swp1    swp1       IfName 5m: 5s  N/A   N/A

#continuation of the output
-------------------------------------------------------------------------------------------------
BFD   BFD       det_mult  tx_timeout  rx_timeout  echo_tx_timeout  echo_rx_timeout  max_hop_cnt
peer  DownDiag
-------------------------------------------------------------------------------------------------
N/A   N/A       N/A       N/A         N/A         N/A              N/A              N/A
N/A   N/A       N/A       N/A         N/A         N/A              N/A              N/A
```

To return information on active BFD sessions `ptmd` is tracking, use the `-b` option:

```
cumulus@switch:~$ sudo ptmctl -b

----------------------------------------------------------
port  peer        state  local         type       diag

----------------------------------------------------------
swp1  11.0.0.2    Up     N/A           singlehop  N/A
N/A   12.12.12.1  Up     12.12.12.4    multihop   N/A
```

To return LLDP information, use the `-l` option. The output returns only the active neighbors that `ptmd` is tracking.

```
cumulus@switch:~$ sudo ptmctl -l

---------------------------------------------
port  sysname  portID  port   match  last
                       descr  on     upd
---------------------------------------------
swp45 h1       swp1    swp1   IfName 5m:59s
swp46 h2       swp1    swp1   IfName 5m:59s
```

To return detailed information on active BFD sessions `ptmd` is tracking, use the `-b` and `-d` option (results are for an IPv6-connected peer):

```
cumulus@switch:~$ sudo ptmctl -b -d

----------------------------------------------------------------------------------------
port  peer                 state  local  type       diag  det   tx_timeout  rx_timeout
                                                          mult
----------------------------------------------------------------------------------------
swp1  fe80::202:ff:fe00:1  Up     N/A    singlehop  N/A   3     300         900
swp1  3101:abc:bcad::2     Up     N/A    singlehop  N/A   3     300         900

#continuation of output
---------------------------------------------------------------------
echo        echo        max      rx_ctrl  tx_ctrl  rx_echo  tx_echo
tx_timeout  rx_timeout  hop_cnt
---------------------------------------------------------------------
0           0           N/A      187172   185986   0        0
0           0           N/A      501      533      0        0
```

### ptmctl Error Outputs

If there are errors in the topology file or there is no session, PTM returns appropriate outputs. Typical error strings are:

```
Topology file error [/etc/ptm.d/topology.dot] [cannot find node cumulus] -
please check /var/log/ptmd.log for more info

Topology file error [/etc/ptm.d/topology.dot] [cannot open file (errno 2)] -
please check /var/log/ptmd.log for more info

No Hostname/MgmtIP found [Check LLDPD daemon status] -
please check /var/log/ptmd.log for more info

No BFD sessions . Check connections

No LLDP ports detected. Check connections

Unsupported command
```

For example:

```
cumulus@switch:~$ sudo ptmctl
-------------------------------------------------------------------------
cmd         error
-------------------------------------------------------------------------
get-status  Topology file error [/etc/ptm.d/topology.dot]
            [cannot open file (errno 2)] - please check /var/log/ptmd.log
            for more info
```

{{%notice tip%}}
If you encounter errors with the `topology.dot` file, you can use `dot` (included in the Graphviz package) to validate the syntax of the topology file.

Open the topology file with Graphviz to ensure that it is readable and that the file format is correct.

If you edit `topology.dot` file from a Windows system, be sure to double check the file formatting; there might be extra characters that keep the graph from working correctly.
{{%/notice%}}

## Basic Topology Example

The following example shows a basic example DOT file and its corresponding topology diagram. Use the same `topology.dot` file on all switches and do not split the file for each device to allow for easy automation by using the same exact file on each device.

```
graph G {
    "spine1":"swp1" -- "leaf1":"swp1";
    "spine1":"swp2" -- "leaf2":"swp1";
    "spine2":"swp1" -- "leaf1":"swp2";
    "spine2":"swp2" -- "leaf2":"swp2";
    "leaf1":"swp3" -- "leaf2":"swp3";
    "leaf1":"swp4" -- "leaf2":"swp4";
    "leaf1":"swp5s0" -- "server1":"eth1";
    "leaf2":"swp5s0" -- "server2":"eth1";
}
```

{{< img src = "/images/cumulus-linux/ptm-dot.png" >}}

## Considerations

### ptmd Is in an Incorrect Failure State

When `ptmd` is in an incorrect failure state and you enable the Zebra interface, PIF BGP sessions do not establish the route but the subinterface does establish routes.

If the subinterface is on the physical interface and PTM marks the physical interface in a PTM FAIL state, FRR does not process routes on the physical interface, but the subinterface is working.

### Commas in Port Descriptions

If an LLDP neighbor advertises a `PortDescr` that contains commas, `ptmctl -d` splits the string on the commas and misplaces its components in other columns. Do not use commas in your port descriptions.

## Related Information

- {{<exlink url="http://tools.ietf.org/html/rfc5880" text="Bidirectional Forwarding Detection (BFD)">}}
- {{<exlink url="http://www.graphviz.org" text="Graphviz">}}
- {{<exlink url="http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol" text="LLDP on Wikipedia">}}
- {{<exlink url="https://github.com/CumulusNetworks/ptm" text="PTMd GitHub repo">}}
