---
title: Taking Preventative Steps with Your Network
author: Cumulus Networks
weight: 15
aliases:
 - /display/NETQ10/Taking+Preventative+Steps+with+Your+Network
 - /pages/viewpage.action?pageId=6488223
pageID: 6488223
product: Cumulus NetQ
version: 1.0.0
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
---
NetQ provides quality assurance capabilities to detect erroneous or
undesired network configurations before the changes are rolled into
production. NetQ can be used to test existing or design topologies,
validate configuration changes, and review the state of the network in
real time, allowing it to integrate effectively with CI/CD environments.
NetQ commands can also be run in an automation tool; depending on the
outcome of the automation tests, the script can either continue the
deployment, or roll back the changes until the issues are addressed.

In addition, [NetQ
Virtual](/version/cumulus-netq-10/Configuring-the-NetQ-Virtual-Environment)
provides users with a Cumulus VX topology to serve as a virtual
representation of your production network; once the network is verified
in NetQ Virtual, the topology can then be rolled into production.

## netq check and netq show</span>

The `netq check` and `netq show` commands validate network state before
and after configuration changes. Based on results returned by NetQ, you
or your automation script can either roll back the configuration change
or continue deploying it:

    cumulus@leaf01:~$ netq check 
        agents   :  netq agent
        bgp      :  BGP info
        clag     :  Multi-chassis LAG (CLAG) info
        license  :  License
        lnv      :  Lightweight Network Virtualization info
        mtu      :  Link MTU
        ospf     :  OSPF info
        sensors  :  Temperature/Fan/PSU sensors
        vlan     :  VLAN
        vxlan    :  VxLAN dataplane info
     
    Commands:
    netq check (vlan|mtu) [unverified] [around <text-time>] [json]
    netq check (agents|clag|ospf|vxlan|lnv|sensors|license) [around <text-time>] [json]
    netq check bgp [vrf <vrf>] [around <text-time>] [json]

Here are some example check commands:

    cumulus@leaf01:~$ netq check agents around 10m
    Checked nodes: 25, Rotten nodes: 0

NetQ check enables users to review the state of the network at specific
moments in time by specifying the `around text-time` option.

    cumulus@leaf01:~$ netq check bgp vrf DataVrf1081
    Total Nodes: 25, Failed Nodes: 1, Total Sessions: 52 , Failed Sessions: 2, 
    Node   Neighbor   Peer ID    Reason   Time
    ------ ---------- ---------- -------- ---------
    exit-1 swp6.3     firewall-1 Idle     Yesterday
    exit-1 swp7.3     firewall-2 Idle     Yesterday

    cumulus@leaf01:~$ netq check lnv around 10m
    Checked Nodes: 9, Warning Nodes: 0, Failed Nodes: 0

    cumulus@leaf01:~$ netq check sensors around 14m
    Total Nodes: 25, Failed Nodes: 0, Checked Sensors: 221, Failed Sensors: 0

The `netq show` command displays a wide variety of content from the
network:

    cumulus@leaf01:~$ netq show 
        agents      :  netq agent
        bgp         :  BGP info
        changes     :  How this infomation has changed with time
        clag        :  Multi-chassis LAG (CLAG) info
        docker      :  Docker Info
        interfaces  :  Network interface
        inventory   :  Inventory information
        ip          :  IPv4 related info
        ipv6        :  IPv6 related info
        lldp        :  LLDP based neighbor info
        lnv         :  Lightweight Network Virtualization info
        macs        :  Mac table entries
        sensors     :  Temperature/Fan/PSU sensors
        services    :  System services

### netq show agents</span>

To get the health of the NetQ agents running in the fabric, run `netq
show agents`. A *Fresh* status indicates the agent is running as
expected. The agent sends a heartbeat every 30 seconds, and if 3
consecutive heartbeats are missed, its status changes to *Rotten*.

    cumulus@leaf01:~$ netq show agents 
     
    Node Name    Status   Connect Time         Last Connect  
    -----------  -------- -------------------  --------------  
    exit01       Fresh    2017-06-01 00:53:23  22s ago
    exit02       Fresh    2017-06-01 00:53:24  20s ago
    leaf01       Fresh    2017-06-01 00:53:22  23s ago
    leaf02       Fresh    2017-06-01 00:53:23  22s ago
    leaf03       Fresh    2017-06-01 00:53:22  21s ago
    leaf04       Fresh    2017-06-01 00:53:22  21s ago
    spine01      Fresh    2017-06-01 00:53:25  20s ago
    spine02      Fresh    2017-06-01 00:53:25  19s ago

## Using NetQ with Automation</span>

Using NetQ for preventative care of your network pairs well with
automation scripts and playbooks to prevent errors on your network
before deploying the configuration to production.

NetQ works with Ansible, Chef and Puppet.

For example, you can use NetQ in your Ansible playbook to help you
configure your network topology. The playbook could pull in BGP data in
JSON format before it starts creating the topology:

    - hosts: localhost leaf spine
      gather_facts: False
      tasks:
         - name: Gather BGP Adjanceny info in JSON format
           local_action: command netq show bgp json
           register: result
           #delegate_to: localhost
           run_once: true

Based on the outcome, the playbook can then respond appropriately.
Later, it can check IP addresses to verify the connections:

    #ipv6 address check
         - name: run ipv6check on broken_dict
           command: netq show ipv6 addresses {{item.key}} {{item.value}} json
           with_dict: "{{broken_dict}}"
           register: command_outputs
           delegate_to: localhost
           run_once: true

## Using NetQ Virtual</span>

The NetQ Virtual environment provides another way for you to verify your
network configuration before deploying it into production. For more
information, see [Configuring the NetQ Virtual
Environment](/version/cumulus-netq-10/Configuring-the-NetQ-Virtual-Environment).

