---
title: Prescriptive Topology Manager - PTM
author: NVIDIA
weight: 370
toc: 3
---
<span class="a-tooltip">[PTM](## "Prescriptive Topology Manager")</span> is a dynamic cabling verification tool that can detect and eliminate errors. PTM uses a Graphviz-DOT specified network cabling plan in a `topology.dot` file and couples it with runtime information from LLDP to verify that the cabling matches the specification. The check occurs on every link transition on each node in the network.

You can customize the `topology.dot` file to control the PTM service (`ptmd`) at both the global and network level, and the node and port level.

## Supported Features

- Topology verification using <span class="a-tooltip">[LLDP](## "Link Layer Discovery Protocol")</span>. The `ptmd` service creates a client connection to the LLDP service (`lldpd`), and retrieves the neighbor relationship between the nodes or ports in the network and compares them against the prescribed topology specified in the `topology.dot` file.
- PTM only supports physical interfaces, such as swp1 or eth0. You cannot specify virtual interfaces, such as bonds or subinterfaces in the topology file.
- Integration with <span class="a-tooltip">[FRR](## "FRRouting")</span> (PTM to FRR notification for BFD status).
- Client management; the `ptmd` service creates an abstract named socket `/var/run/ptmd.socket` on startup. Other applications can connect to this socket to receive notifications and send commands.
- Event notifications.
- Configuration with a `topology.dot` file; {{<link url="#configure-ptm" text="see below">}}.

## Configure PTM

The `ptmd` service verifies the physical network topology against a DOT-specified network graph file, `/etc/ptm.d/topology.dot`.

PTM supports {{<exlink url="http://en.wikipedia.org/wiki/DOT_%28graph_description_language%29" text="undirected graphs">}}.

At startup, the `ptmd` service connects to the `lldpd` service over a Unix socket and retrieves the neighbor name and port information. It then compares the retrieved port information with the configuration information that it reads from the topology file. If there is a match, it is a `PASS`, otherwise it is a `FAIL`.

{{%notice note%}}
PTM performs its LLDP neighbor check using the PortID ifname TLV information.
{{%/notice%}}

## ptmd Scripts

The `ptmd` service executes scripts at `/etc/ptm.d/if-topo-pass` and `/etc/ptm.d/if-topo-fail` for each interface that goes through a change and runs `if-topo-pass` when an LLDP or BFD check passes, or `if-topo-fails` when the check fails. The scripts receive an argument string that is the result of the `ptmctl` command; see {{%link url="#ptmd-service-commands" text="`ptmd` commands below"%}}.

You can modify these default scripts.

## Configuration Parameters

You can configure `ptmd` parameters in the topology file. The parameters are host-only, global, per-port or node and templates.

<!-- vale off -->
<!-- Vale issue #253 -->
### Host-only Parameters
<!-- vale on -->
*Host-only parameters* apply to the entire host on which PTM is running. You can include the `hostnametype` host-only parameter that specifies if PTM uses only the hostname (`hostname`) or the fully qualified domain name (`fqdn`) while looking for the `self-node` in the graph file. For example, in the graph file below PTM ignores the FQDN and only looks for *switch04* because that is the hostname of the switch on which it is running:

{{%notice tip%}}
- Always wrap the hostname in double quotes; for example, `"www.example.com"` to prevent `ptmd` from failing.
- To avoid errors when starting the `ptmd` service, make sure that `/etc/hosts` and `/etc/hostname` both reflect the hostname you are using in the `topology.dot` file.
{{%/notice%}}

```
graph G {
          hostnametype="hostname"
          "cumulus":"swp44" -- "switch04.cumulusnetworks.com":"swp20"
          "cumulus":"swp46" -- "switch04.cumulusnetworks.com":"swp22"
}
```

In this next example, PTM compares using the FQDN and looks for *switch05.cumulusnetworks.com*, which is the FQDN of the switch on which it is running:

```
graph G {
          hostnametype="fqdn"
          "cumulus":"swp44" -- "switch05.cumulusnetworks.com":"swp20"
          "cumulus":"swp46" -- "switch05.cumulusnetworks.com":"swp22"
}
```

### Global Parameters

*Global parameters* apply to every port in the topology file. LLDP is on by default; if no keyword is present, PTM uses the default values for all ports.

```
graph G {
          LLDP=""
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
          "cumulus":"swp44" -- "qct-ly2-04":"swp20"
          "cumulus":"swp46" -- "qct-ly2-04":"swp22"
}
```

### Templates

*Templates* provide flexibility so that you can choose different parameter combinations and apply them to a given port. A template instructs `ptmd` to reference a named parameter string instead of a default one. In the following configuration, LLDP1 and LLDP2 are templates for LLDP parameters:

For example:

```
graph G {
          LLDP=""
          LLDP1="match_type=ifname"
          LLDP2="match_type=portdescr"
          "cumulus":"swp44" -- "qct-ly2-04":"swp20" [LLDP="lldptmpl=LLDP1"]
          "cumulus":"swp46" -- "qct-ly2-04":"swp22" [LLDP="lldptmpl=LLDP2"]
          "cumulus":"swp46" -- "qct-ly2-04":"swp22"
}
```



### Supported LLDP Parameters

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
When you specify `match_hostname=fqdn`, PTM matches the entire FQDN, (*cumulus-2.domain.com* in the example below). If you do not specify a value for `match_hostname`, PTM matches based on hostname only, (*cumulus-3* below), and ignores the rest of the URL:

```
graph G {
          "cumulus-1":"swp44" -- "cumulus-2.domain.com":"swp20" [LLDP="match_hostname=fqdn"]
          "cumulus-1":"swp46" -- "cumulus-3":"swp22" [LLDP="match_type=portdescr"]
}
```
{{%/notice%}}

## BFD

<span class="a-tooltip">[BFD](## "Bidirectional Forwarding Detection")</span> provides low overhead and rapid detection of failures in the paths between two network devices. PTM provides a unified mechanism for link detection over all media and protocol layers and integrated with FRR to enable BFD. Use BFD to detect failures for IPv4 and IPv6 single or multihop paths between any two network devices, including unidirectional path failure detection. For information about configuring BFD, see {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}}.

## Check Link State

You can enable PTM to perform additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that PTM defines.

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

To check PTM status on an interface, run the vtysh `show interface <interface>` command.

```
cumulus@switch:~$ show interface swp51
Interface swp51 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
...
```

## ptmd Service Commands

PTM sends client notifications in CSV format.

To start the `ptmd` service, run the `sudo systemctl start ptmd.service` command. The `topology.dot` file must be present for the service to start.

```
cumulus@switch:~$ sudo systemctl start ptmd.service
```

To restart the `ptmd` service, run the `sudo systemctl restart ptmd.service` command:

```
cumulus@switch:~$ sudo systemctl restart ptmd.service
```

To instruct the `ptmd` service to read the `topology.dot` file again to apply the new configuration to the running state without restarting, run the `sudo systemctl reload ptmd.service` command:

```
cumulus@switch:~$ sudo systemctl reload ptmd.service
```

To stop the `ptmd` service, run the `sudo systemctl stop ptmd.service` command:

```
cumulus@switch:~$ sudo systemctl stop ptmd.service
```

To retrieve the current running state of the `ptmd` service, run the `sudo systemctl status ptmd.service` command:

```
cumulus@switch:~$ sudo systemctl status ptmd.service
```

## ptmctl Commands

`ptmctl` is a client of the `ptmd` service that retrieves the operational state of the ports configured on the switch and information about BFD sessions from `ptmd`. `ptmctl` parses the CSV notifications sent by `ptmd`. See `man ptmctl` for more information.

### ptmctl Examples

The examples below contain the following keywords in the output of the `cbl status` column:

| `cbl` status Keyword<img width=200/> | Definition<img width=400/> |
|-------- |-------- |
| `pass` | The topology file defines the interface, the interface receives LLDP information, and the LLDP information for the interface matches the information in the topology file. |
| `fail` | The topology file defines the interface, the interface receives LLDP information, and the LLDP information for the interface does not match the information in the topology file. |
| `N/A` | The topology file defines the interface, but the interface does not receive LLDP information. The interface might be down or disconnected, or the neighbor is not sending LLDP packets.<br>The `N/A` and `fail` status might indicate a wiring problem to investigate.<br>The `N/A` status does not show when you use the `-l` option with `ptmctl`; the output shows only interfaces that are receiving LLDP information. |

For basic output, use `ptmctl` without any options:

{{%notice note%}}
PTM show command output displays BFD status when you configure {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}} through integration with FRR.
{{%/notice%}}

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

To show information about the active BFD sessions that the `ptmd` serice is tracking, use the `-b` option:

```
cumulus@switch:~$ sudo ptmctl -b

----------------------------------------------------------
port  peer        state  local         type       diag

----------------------------------------------------------
swp1  11.0.0.2    Up     N/A           singlehop  N/A
N/A   12.12.12.1  Up     12.12.12.4    multihop   N/A
```

To show LLDP information, use the `-l` option. The output shows only the active neighbors that the `ptmd` service is tracking.

```
cumulus@switch:~$ sudo ptmctl -l

---------------------------------------------
port  sysname  portID  port   match  last
                       descr  on     upd
---------------------------------------------
swp45 h1       swp1    swp1   IfName 5m:59s
swp46 h2       swp1    swp1   IfName 5m:59s
```

To show detailed information about the active BFD sessions that the `ptmd` service is tracking, use the `-b` and `-d` option:

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

If you edit the `topology.dot` file from a Windows system, be sure to doublecheck the file formatting; there might be extra characters that keep the graph from working correctly.
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
### Commas in Port Descriptions

If an LLDP neighbor advertises a `PortDescr` that contains commas, `ptmctl -d` splits the string on the commas and misplaces its components in other columns. Do not use commas in your port descriptions.

## Related Information

- {{<exlink url="http://tools.ietf.org/html/rfc5880" text="Bidirectional Forwarding Detection (BFD)">}}
- {{<exlink url="http://www.graphviz.org" text="Graphviz">}}
- {{<exlink url="http://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol" text="LLDP on Wikipedia">}}
- {{<exlink url="https://github.com/CumulusNetworks/ptm" text="PTMd GitHub repo">}}
