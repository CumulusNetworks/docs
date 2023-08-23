---
title: Throughput Testing and Troubleshooting
author: NVIDIA
weight: 371
toc: 4
---

## Traffic Profile

First you need to understand the traffic profile. You need to gather the following information:

- What is the source/destination of the connection?
    - Bare metal or VM?
    - OS
    - IP address
    - MAC address
    - CPU information
    - RAM
- What is the full traffic path of the connection?
    - Layer 1 connections
    - Layer 2 hops
    - Layer 3 hops
- What service, protocol and ports is the connection using?
    - TCP/UDP
    - Non-standard ports
    - Common throughput testing - HTTP, FTP, high port TCP
- How many established concurrent connections are between the client and server?
- What is the average packet size?
- TCP specific questions:
    - What is the window?
    - Is there any packet reordering?
    - Is there packet loss and what is the recovery mechanism?
    - Are you using SACK or normal ACK?
- How much other traffic is going through the Cumulus Linux switch?
    - What is the speed of the port?

## Network Testing with Open Source Tools

Testing network performance requires generating traffic at various rates and measuring throughput, loss, latency, jitter, and so forth. This article covers multiple open source network test tools, which are available for free. Running the software is only half of the story however. Tuning the host to efficiently generate and receive network traffic as well as monitoring the hardware load is equally important. All the tools explored here have different features, statistics reporting and operation.

Generating traffic at data rates above 1Gbps requires powerful server hardware. Without going into the depths of computer architecture, the CPU, memory, PCI bus and network interface controller (NIC) all play a part in generating and receiving network data. Typically the bottleneck is the CPU core executing the client or server processes. The PCI bus might also constrain the performance depending on the PCI version. Finally, the NIC must be able to support the traffic it is attempting to send.

Many of the examples and tuning information came from {{<exlink url="https://fasterdata.es.net/host-tuning/" text="Energy Sciences Network">}}. They go into a lot more detail about the host tuning and the various capabilities of the different tools.

### iPerf3

This is a complete rewrite of the original iPerf tool. It has many of the same features, although it does not yet do multicast. Below are some basic commands to get started, which are the same options available in version 2. For bandwidth testing, iPerf3 is preferable over iPerf1 or 2.

{{%notice note%}}

NVIDIA tested iPerf3 and identified some functionality issues on Debian Wheezy 7.9, while NVIDIA noticed no issues on Debian Jessie 8.3. iPerf versions 1 and 2 work on Debian Wheezy. Nvidia does not provide support for installation or usage of 3rd party tools.  The information here is provided as a courtesy.

{{%/notice%}}

#### Server Commands

Start the server on the default port for IPv4 (default):

    iperf3 -s 

Start the server in daemon mode:

    iperf3 -s -D

Start the server on port 5003:

    iperf3 -s -p 5003

Start using 0.5 second interval times:

    iperf3 -s -i 0.5

#### Client Commands

Run a 30 second test, giving results every 1 second:

    iperf3 -c <dst-ip> -i 1 -t 30 

{{%notice note%}}

Using granular interval reporting counters can help provide greater information when examining why a specific throughput test is slow.

{{%/notice%}}

Run a test from remotehost to localhost:

    iperf3 -c <dst-ip> -i 1 -t 20 -R 

Run a test with 4 parallel streams, and with a 32M TCP buffer

    iperf3 -c <dst-ip> -w 32M -P 4 

{{%notice note%}}

Window size is very important for TCP tests. The TCP window dictates how many bytes and packets can be in flight before receiving an ACK. A small window might result in high speeds for a directly connected server and client, but low speeds for a server and client across a network with high latency between the client and server. As RTT increases, the time between packet and ACK increases, which results in more packets in flight. If the TCP window is too small to accommodate, the sender scales back the speed at which it sends the packets before it exhausts the window. This becomes even more important when using jumbo frames.

{{%/notice%}}

{{%notice note%}}

Utilizing parallel sessions can help improve throughput numbers when using load balancing features such as LACP bonded links, MLAG switches or ECMP routing. In these traffic load balancing features, flows are normally hashed using the source and destination IP address and port. This means that a single flow always gets hashed to the same physical link and path. To test the full utilization of the traffic path, use multiple IP addresses and ports for the client and server connections. You should add the throughput results for each concurrent connection together to get the total bandwidth of the infrastructure. The `-P` option creates multiple sessions with varying source ports which, depending on the traffic hashing algorithm, can result in greater throughput results.

{{%/notice%}}

Run a 200 Mbps UDP test:

    iperf3 -c <dst-ip> -u -i 1 -b 200M

{{%notice note%}}

When testing with UDP, you can use the `-b` modifier to set a target throughput rate. Use `-b 0` for an unlimited bandwidth target. For UDP, without setting this value the throughput values might be very low.

{{%/notice%}}

{{%notice note%}}

Many client/server NIC cards perform TCP checksum/header offloading. This means that the NIC itself does these calculations. But for UDP, the software performs the header processing. As a result, performance numbers between UDP and TCP might not be consistent.

{{%/notice%}}

#### Optimizations

iPerf3 features many optimizations that work well with modern server hardware. It also has new features to improve how to measure statistics.

Run the test for 2 seconds before collecting results, to allow for TCP slowstart to finish. The `-O` flag sets the Omit mode to a 2 second delay, and the -i flag sets a ½ second report interval.

    iperf3 -c <dst-ip> -O 2 -i 0.5

Using the `-Z` flag enables the Zero Copy mode, which uses the `sendfile()` system call. This uses much less CPU to put the data on the PCI bus.

    iperf3 -c <dst-ip> -Z

Output the results in JSON format using the `-J` flag for easy parsing by most coding languages. This output prints after the entire test finishes running.

    iperf3 -c <dst-ip> -J 

Set the CPU affinity for the sender `(-A 2)` or the sender, receiver `(-A 2,3)`, where the core numbering starts at 0. This has the same effect as running `numactl -C 4 iperf3`.

    iperf3 -c <dst-ip> -A 2,3 

{{%notice note%}}

Using granular interval reporting counters can help provide greater information when examining why a specific throughput test is slow.

{{%/notice%}}

{{%notice note%}}

It is not necessary to use `-A x,y` if you are using the `-P` flag. The `-P` flag creates multiple connections and the server side appears to balance the threads across all available cores.

{{%/notice%}}

#### Considerations

As identified in the notes above, iPerf can give a vastly varied set of results depending on the settings. However, iPerf has some issues that make it difficult to use for performance testing on modern networks. Factors that matter in testing:

- TCP window size, controlled using the -w flag
- TCP vs UDP procotol, controlled using the -u modifier
- Target throughput rate, controlled using the -b modifier
- CPU utilization, controlled using the -Z modifier and the -A
    modifier
- Data time sets used for average calculations, controlled using -O
    modifier
- Concurrent connections on port, controlled using the -P modifier

By default iPerf uses TCP/UDP port 5201/5001 (depending on version) for ports during transfer. This does not work too well for ECMP testing. Specifying the `-P` flag tells iPerf to spawn multiple client threads, where the source port uses 5201 as well as a series of ephemeral ports. But when using this method, it is also normal to see a lot of these messages: `bind failed: Address already in use`.

### iPerf (version 2)

When installing iPerf from the distribution's repository, it is most likely version 2. This is a rather old version, and is no longer maintained.

#### Multicast

One unique feature of iPerf2 to take a look at is the ability to send multicast traffic. Here are the client and server commands to use:

    iperf -c 224.0.0.1 -u -b 512k  #source
    iperf -B 224.0.0.1 -su         #receiver

This causes the server to listen on a group address, meaning it sends an IGMP report to the connected network device. On the client side, be sure to create a static route for the multicast range, with a next hop toward the network devices under test (let\'s assume this is out from eth1).

    ip route add 224.0.0.0/4 dev eth1

#### Considerations

The results are inconsistent for UDP above 2Gbps. NVIDIA recommends using `nuttcp` or iPerf3 for high speed UDP testing. However, it is acceptable for testing networks if you keep the traffic rate below 2Gbps. Above that, the statistics are completely unreliable. Therefore, this article is not going to cover this as a viable performance test tool.

### nuttcp

This tool evolved over the past 30 years, and has several useful features. It supports rate limiting, multiple parallel streams and timer based execution. It also includes IPv6, IPv4 multicast and the ability to set parameters, such as TCP MSS or TOS/DSCP bits.

Looking at the application's help file, it is easy to see that this tool has a lot of unique functionality. One thing to understand is there are client (transmitter/receiver) and server entities. You can control the server settings from the client command, for such things as TCP window size. Server processes automatically fork into the background and run until an error condition occurs or something kills them. The examples below demonstrate some of the basics.

#### Server Commands

Start the server on the default port (5000):

    nuttcp -S

Start server on the default port for IPv6:

    nuttcp -s -6

Start server on port 5003:

    nuttcp -S -P 5003

#### Transmitter Commands

Run a 10 second test, giving results every second:

    nuttcp -i 1 <server>

Running longer tests require the `-T` flag, where you can specify duration like this:

    -T30 = 30 sec, -T1m = 1 min, and -T1h = 1 hr

Run a 10 second test, setting the transmitter/receiver window as well as the server receive/transmit window size to 32KB. You can also set the window in megabytes (-w5m) or Gigabytes (-w5g):

    nuttcp -w32 -ws32 <server>

The default traffic uses TCP, but you can run it as UDP with 8192 byte datagrams (default):

    nuttcp -u <server>

Run a 10 second UDP test at 50Mbps, and report throughput and packet loss:

    nuttcp -u -R50m <server>

Run a 10 second UDP test with 1200 byte datagrams:

    nuttcp -u -l1200 <server>

#### Receiver Commands

Run a 10 second test in reverse (server → client), giving results every 1 second:

    nuttcp -r -i 1 <server>

#### Special Features

##### UDP Burst Mode

Starting with version 6.2.8, `nuttcp` includes a *burst mode* for UDP, which is useful for finding network paths constrained a lack of buffering. To do this, set an instantaneous data rate with optional packet burst. Specify the rates in Kbps (-R100), Mbps (-R5m), Gbps (-R5g) or PPS (-R1000p). The burst is just a count of packets.

Send 300 Mbps of UDP at an instantaneous rate in bursts of 20 packets for 5 seconds:

    nuttcp -u -Ri300m/20 -i 1 -T5 <server>

This test might show a small amount of loss. If you increase the burst size at the same instantaneous rate, it also increases the stress to the network buffering. This progressively shows more loss as the transit device overflows its buffers.

On 10GbE network with 9000 byte MTU, you can send 8972 byte UDP datagrams at an instantaneous rate of 300 Mbps, and bursting at 100 packets. This should be lossless:

    nuttcp -l8972 -T30 -u -w4m -Ri300m/100 -i1 <server>

Again, increasing the burst value and retesting eventually shows where buffer exhaustion happens in the network:

##### 10G UDP Testing

`nuttcp` might the best tool for high speed UDP testing. It took very little effort to create a full 10 Gbps traffic flow using UDP, but it requires jumbo MTU size packets (9K):

    nuttcp -l8972 -T30 -u -w4m -Ru -i1 <server>

##### CPU Affinity

One of the newer features introduced in version 7.1 is CPU affinity. This allows the user to specify on which core to execute the process.

Sending multiple streams, you can use CPU affinity binding to make sure both processes do not end up on the same CPU core. Be sure to start the servers on the intended destination ports. Also, using the statistics output identifier helps to label the results with an *s1* or *s2*:

    nuttcp -i1 -xc 2/2 -Is1 -u -Ru -l8972 -w4m -p 5500 <server> & \
    nuttcp -i1 -xc 3/3 -Is2 -u -Ru -l8972 -w4m -p 5501 <server>

### Bandwidth Controller (bwctl)

This tool is a wrapper for iPerf2, iPerf3 and `nuttcp`. The documentation for this wrapper is available {{<exlink url="https://fasterdata.es.net/performance-testing/network-troubleshooting-tools/nuttcp/" text="here">}}.

The advantage of using `bwctl` is that it is a centralized bandwidth testing tool that utilizes all the tools listed above to provide bandwidth test results. You can read the {{<exlink url="http://docs.perfsonar.net/install_debian" text="installation guide here">}}.

### Ostinato

Ostinato is an open source tool for generating packets. It operates primarily from a GUI, but is {{<exlink url="http://ostinato.org/" text="easily installed">}} in a Linux desktop environment.

Although there is no CLI, it does have a {{<exlink url="https://apiguide.ostinato.org/start.html" text="Python API">}} that you can use to generate packets.

## Cumulus Linux Switch Outputs

When performing bandwidth testing, it is valuable to cross reference the results from the testing tool against various outputs on the Cumulus Linux switch.

### Traffic Services on the Switch

Throughput levels might change based on what services you apply to the traffic. Ideally, all traffic should be hardware switched through the switch ASIC. But certain services applied to the traffic require punting the traffic from the ASIC to the switch CPU. Because the switch CPU is slower at processing and forwarding packets, the throughput might suffer from these features. Some features that might cause software processing of packets are:

- Encapsulation methodologies
- GRE
- NAT
- PBR

It is also important to look at what general features get applied to the traffic:

- Layer 2 vs. layer 3 switching
- Netfilter ACLs for traffic

### Troubleshooting Output

You should examine these two outputs to verify the throughput:

- cl-netstat
- ethtool -S swp*X*
<!-- vale off -->
#### cl-netstat
<!-- vale on -->
This command is a wrapper for the interface counters provided in Linux. The output of `ip -s link show up` prints counters of all TX and RX packets. But these native Linux commands have no way to clear counters. The `cl-netstat` command adds this functionality, and can track individual connections under controlled environments. The example below shows the results of an iPerf3 test run between a client and server through the Cumulus Linux switch:

##### Client iPerf3 Results

    root@CLIENT:~# iperf3 -c 10.1.1.100
    Connecting to host 10.1.1.100, port 5201
    [  4] local 10.1.2.100 port 53984 connected to 10.1.1.100 port 5201
    [ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
    [  4]   0.00-1.00   sec   980 MBytes  8.22 Gbits/sec    0   5.17 MBytes       
    ...   
    [  4]   9.00-10.00  sec   951 MBytes  7.98 Gbits/sec    0   5.17 MBytes       
    - - - - - - - - - - - - - - - - - - - - - - - - -
    [ ID] Interval           Transfer     Bandwidth       Retr
    [  4]   0.00-10.00  sec  9.32 GBytes  8.01 Gbits/sec    0             sender
    [  4]   0.00-10.00  sec  9.29 GBytes  7.98 Gbits/sec                  receiver
<!-- vale off -->
##### cl-netstat Results
<!-- vale on -->
    cumulus@switch:~$ sudo cl-netstat   
    Kernel Interface table
    Iface      MTU    Met    RX_OK    RX_ERR    RX_DRP    RX_OVR    TX_OK    TX_ERR    TX_DRP    TX_OVR  Flg
    -------  -----  -----  -------  --------  --------  --------  -------  --------  --------  --------  -----
    swp13     1500      0    62622         0         0         0  6904270         0         0         0  BMRU
    swp14     1500      0  6904271         0         0         0    62623         0         0         0  BMRU

In the above example, you can see that traffic has successfully flowed between swp13 and swp14 without dropping any packets.
<!-- vale off -->
#### ethtool -S
<!-- vale on -->
Similarly, you can use the output of `ethtool -S` to cross reference the output obtained from `cl-netstat`.

    cumulus@switch:~$ sudo ethtool -S swp13
    NIC statistics:
         HwIfInOctets: 5583156718
         HwIfInUcastPkts: 5140969
         HwIfInBcastPkts: 14
         HwIfInMcastPkts: 9272
         HwIfOutOctets: 210229661164
         HwIfOutUcastPkts: 139033950
         HwIfOutMcastPkts: 17657
         HwIfOutBcastPkts: 8556
         HwIfInDiscards: 0
         HwIfInL3Drops: 0
         HwIfInBufferDrops: 0
         HwIfInAclDrops: 63
         HwIfInDot3LengthErrors: 0
         HwIfInErrors: 0
         SoftInErrors: 0
         SoftInDrops: 0
         SoftInFrameErrors: 0
         HwIfOutDiscards: 0
         HwIfOutErrors: 0
         HwIfOutQDrops: 0
         HwIfOutNonQDrops: 0

    cumulus@switch:~$ sudo ethtool -S swp14
    NIC statistics:
         HwIfInOctets: 210229250162
         HwIfInUcastPkts: 139051524 
         HwIfInBcastPkts: 5 
         HwIfInMcastPkts: 9230 
         HwIfOutOctets: 5583641007 
         HwIfOutUcastPkts: 5124014 
         HwIfOutMcastPkts: 17875 
         HwIfOutBcastPkts: 8711 
         HwIfInDiscards: 0 
         HwIfInL3Drops: 0 
         HwIfInBufferDrops: 0 
         HwIfInAclDrops: 54 
         HwIfInDot3LengthErrors: 0 
         HwIfInErrors: 0 
         SoftInErrors: 0 
         SoftInDrops: 0 
         SoftInFrameErrors: 0
         HwIfOutDiscards: 0
         HwIfOutErrors: 0
         HwIfOutQDrops: 0
         HwIfOutNonQDrops: 0 

The counters in `ethtool` are much larger than the output of `cl-netstat` because you cannot clear the `ethtool` counters. The key output to examine is to verify whether errors in receive or transmit are increasing.

The directionality of the counters matters as well. Drops on ingress via the HwIfIn prefix indicate that traffic rate on receive is too fast. This generally indicates a bursty traffic or choke points further along the traffic path. Drops on egress via the HwIfOut prefix indicate a many-to-one problem, where multiple RX interfaces are trying to send traffic out a single TX interface. This is not always a bad result, as it indicates full bandwidth utilization by the interface.

## RX Errors

If the counters under RX\_ERR are increasing during the bandwidth test, there might be problems with packet forwarding through the switch. Here are some previously written articles that address this scenario:

- {{<link title="RX Error Counters and Slow Throughput Performance">}}
- {{<link url="Understanding-CPU-Usage-on-Cumulus-Linux">}}
