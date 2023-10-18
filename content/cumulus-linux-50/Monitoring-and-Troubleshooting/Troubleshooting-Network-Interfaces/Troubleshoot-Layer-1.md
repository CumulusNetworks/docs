---
title: Troubleshoot Layer 1
author: NVIDIA
weight: 1095
toc: 3
---

This chapter describes how to troubleshoot layer 1 issues that can affect the port modules connecting a switch to a network.

## High Speed Ethernet Technologies

### Specifications

The following specifications are useful in understanding and troubleshooting layer 1 problems:

- {{<exlink url="https://standards.ieee.org/standard/802_3-2018.html" text="IEEE 802.3 specifications">}} define the technologies and link characteristics of the various types and speeds of Ethernet technologies.
- {{<exlink url="https://www.snia.org/technology-communities/sff/specifications" text="SFF MSA specifications">}} define the specifics of the hardware construction and implementations of features of the SFP and QSFP modules themselves.

### Form Factors

Modern Ethernet modules come in one of two form factors:

- Small Form factor Pluggables (SFP)
- Quad Small Form factor Pluggables (QSFP)

Each form factor contains an EEPROM with information about the capabilities of the module and various groups of required or optional registers to query or control aspects of the module when needed. The output from the `ethtool -m <swp>` command decodes the main values.

The SFF/MSA specifications define the memory locations for the fields in the EEPROM and the common registers:

- SFP: {{<exlink url="https://members.snia.org/document/dl/25916" text="SFF-8472">}}: *Management Interface for SFP+* (PDF)
- QSFP: {{<exlink url="https://members.snia.org/document/dl/26418" text="SFF-8636">}} *Management Interface for 4-lane Modules and Cables* (PDF)

Identifiers used in the first byte of the module memory map:
<!-- vale off -->
- 0x03: SFP/SFP+/SFP28 - One 10G or 25G lane - Small Form factor Pluggable
- 0x0d: QSFP+ - Four 10G lanes - Quad SFP (40G total)
- 0x11: QSFP28 - Four 25G or 50G lanes (100G or 200G total) - Quad SFP with 25G or 50G lanes
- 0x18: QSFP-DD - Eight 50G lanes (400G total) - Quad SFP with a recessed extra card-edge connector to enable 8 lanes of 50G
<!-- vale on -->
### Encoding

Two parts of high-speed Ethernet are under *encoding* in the output from the `ethtool -m <swp>` command:

- The way to represent bits on the wire or optical fiber:
  - NRZ (also known as PAM2) has two voltage (or laser) levels signifying a 0 and 1. Negative voltage level = 0, positive voltage = 1. Used on all Ethernet technologies below lane speeds of 50Gbps.

  {{<figure src="/images/cumulus-linux/L1ts-NRZ-eyes.jpg" width="600">}}

  - PAM4 encoding has four signal levels signifying two bits (00,01,10,11). These levels are much closer together than the levels in NRZ/PAM2, so signal integrity is an even greater concern. PAM4 encoding is used on 50G lanes.

  {{<figure src="/images/cumulus-linux/L1ts-PAM4-eyes.jpg">}}

- The way the bits are joined together into a *frame* to be able to facilitate functions like clock recovery and error checking and correction:
  - 64B/66B: Two control bits with a 1/0 transition are added to the front of a 64 bit frame to ensure that the clock  can sync every 66 bits.
  - RS-FEC encoding (528,514) or (544,514): Uses 14 or 30 bits to enable correction of bit errors on the receive side (see the {{<link url="#fec" text="FEC">}} section below).
  - BaseR FEC encoding: Steals a bit in the 64B/66B control word to re-encode and add a smaller level of error correction than RS-FEC.

The relationship between lane speed and encoding methods is described in this table:

| Lane Speed | Encoding |
| ---------- | -------- |
| 10G | Uses 64B/66B framing then encoded in NRZ &mdash; actually 10.3125 Gbps on the wire. |
| 25G | Uses 64B/66B framing then encoded in NRZ &mdash; actually 25.78125 Gbps on the wire. Can also use RS-FEC (528,514) or Base-R FEC. |
| 50G | Uses PAM4 encoding and RS-FEC (544,514). |

The SerDes (Serial/Deserializer) is the component in the port that converts byte data to and from a set of bit streams (lanes), where:

- SFP ports use 1 lane
- QSFP ports use 4 lanes
- QSFP-DD ports use 8 lanes

On the ASIC, the 40G, 100G and 200G SerDes devices are 4 lanes; 400G SerDes uses 8 lanes. So an SFP port is actually one lane on a four lane SerDes. Depending on the platform design, this sometimes affects how you can configure and break out SFP ports.

Port speeds are created using the following formulas:

| Port Speed | Number of Lanes |
| ---------- | --------------- |
| 1G | One 10G or 25G lane clocked at 1G. Or, on a 1G fixed copper switch, a 1G lane. |
| 10G | One 10G lane. |
| 25G | One 25G lane. |
| 40G | Four 10G lanes. |
| 50G | Two 25G lanes (NRZ) or one 50G lane (PAM4). |
| 100G | Four 25G lanes (100G-SR4/CR4 NRZ) or two 50G lanes (100G-CR2 PAM4). |
| 200G | Four 50G lanes. |
| 400G | Eight 50G lanes. |

### Active and Passive Modules and Cables

From the point of view of the port, modules and cables can be classified as either *active* or *passive*.

Active cables and modules contain transmitters that regenerate the bit signals over the cable. All optical modules are active. 10/100/1000BaseT and 10GBaseT are active modules and contain an onboard PHY that handles the BaseT auto-negotiation and TX/RX to the remote BaseT device. For active modules, the port only has to provide a TX signal with a base level of power to the module and the module uses the power it receives on the port power bus to regenerate the signal to the remote side.

Although some copper cable assemblies are active, they are extremely rare.

Passive cables (copper DACs) connect the port side of the module directly to the copper twinax media on the other side of the module in the assembly. The port TX lines provide the power to drive the signal to the remote end. The port goes through a training sequence with the remote end port to tune the power TX and RX parameters to optimize the received signal and ensure correct clock and data recovery at each RX end.

### Compliance Codes, Ethernet Type, Ethmode Type, Interface Type

Compliance codes, Ethernet type, Ethmode type, and interface type are all terms for the type of Ethernet technology that the module implements.

For the port to know the characteristics of the module that is inserted, the SFP or QSFP module EEPROMs have a standardized set of data to describe the module characteristics. These values appear in the output of `ethtool -m <swp>`.

The compliance codes describe the type of Ethernet technology the module implements, such as 1000Base-T, 10GBase-SR, 10GBase-CR, 40GBase-SR4, and 100GBase-CR4.

The first part of the compliance code gives the full line rate speed of the technology. The last part of the compliance code specifies the Ethernet technology and the number of lanes used:

- \-T: Twisted pair.
- CR: Copper twinax (passive DAC). CR4 uses a bundle of 4 twinax cables for 4 lanes, CR2 uses 2 cables, CR uses 1.
- SR: Optical short range. SR4 uses a bundle of 4 fibers for 4 lanes.
- LR: Optical long range. LR4 uses 4 wavelengths over one fiber pair to transmit 4 lanes over long distances (kilometers).
- xWDM (SWDM, CWDM, DWDM): Optical wavelength multiplexed technologies (various). Multiple lanes are transmitted by different wavelengths.

An active module with a passive module compliance code or a passive module with an active module compliance code causes the port to be set up incorrectly and may affect signal integrity.

Some modules have vendor specific coding, are older, or use a proprietary vendor technology that is not listed in the standards. As a result, they are not recognized by default and need to be overridden to the correct compliance code. On NVIDIA switches, the port firmware automatically overrides certain supported modules to the correct compliance code.

### Digital Diagnostic Monitoring/Digital Optical Monitoring (DDM/DOM)

DDM/DOM is an optional capability that vendors can implement on their optical transceivers to display measurements about the optical power. The values are generally reliable within a 10% tolerance. A value of *0.0000* generally indicates the value is not implemented by the vendor.

The most useful DDM/DOM values when troubleshooting a problem link are:

- RX optical power (receiver signal average optical power)
- TX optical power (laser output power)  

The location of DDM/DOM fields are standardized. If DDM/DOM capability is present on a module, the values are displayed in the output of `ethtool -m <swp>`.

For each DDM/DOM value there can be thresholds to mark a high or low *warning* or an *alarm* when the value exceeds that threshold.

An alarm value indicates the level required for the signal to be within the vendor's design tolerance, and the warning level is a little bit closer to expected norms.

When a warning or alarm is triggered, the flag flips from *Off* to *On*. Reading that value with `ethtool -m` or NVIDIA NetQ (or some other monitoring software) resets this flag back to *Off* after it is read.

## Auto-negotiation

There are 3 different types of auto-negotiation (IEEE 802.3 clauses 28, 37, 73), which apply to various Ethernet technologies that Cumulus Linux supports:

- 10/100/1000/10GBASE-T (twisted pair, clause 28): The original Ethernet auto-negotiation, which negotiates speed and duplex (full/half), and flow control (link pause) on full-duplex. Mandatory for 1G/10G data rates over twisted pair.
- 1000BASE-X (optical, clause 37): Detects unidirectional link conditions (no RX on one side). If a unidirectional link condition occurs, clause 37 auto-negotiation signals the port to bring the link down; this avoids blackholing traffic.
- 40G/100G/25G/50G/200G/400GBASE-CR (DAC, clause 73): Negotiates speed, performs link training to improve the bit error rate (BER), and negotiates FEC.

Many Ethernet technologies used in Cumulus Linux switches do not have auto-negotiation capability:

- No 10G DAC or optical link has auto-negotiation; only 10GBASE-T and backplane links have auto-negotiation standards. Backplane links do not exist on Cumulus Linux switch ports.
- No optical links, except 1G optical, have auto-negotiation.  

Only about half of all modern link types support auto-negotiation. The next subsections provide guidance on when and how to enable auto-negotiation.

### Ethernet Link Types and Auto-negotiation

1000BASE-T and 10GBASE-T fixed copper ports require auto-negotiation for 1G and 10G speeds. This is the default setting; you cannot disable auto-negotiation for 1G speeds. Disabling auto-negotiation on these ports requires setting the speed to 100Mbps or 10Mbps and the correct {{<link url="Switch-Port-Attributes/#port-speed-and-duplex-mode" text="duplex">}} setting.

1000BASE-T SFPs have an onboard PHY that performs auto-negotiation automatically on the RJ45 side without involving the port. Do not change the default auto-negotiation setting on these ports; on NVIDIA switches, auto-negotiation is *ON*.

For 1000BASE-X, auto-negotiation is highly recommended on 1G optical links to detect unidirectional link failures.

For all other optical modules except for 1000BASE-X, there is no auto-negotiation standard.

For 10G DACs, there is no auto-negotiation.

For DAC cables on speeds higher than 25G, auto-negotiation is unnecessary, but is useful because it can improve signal integrity by link training. It also negotiates speed and FEC, which is less useful because the neighbor speed and FEC is usually known.

### General Auto-negotiation Guidance

- When auto-negotiation is supported on an Ethernet type, both sides of the link must be configured with the same auto-negotiation setting.
- Cumulus Linux sets a default for auto-negotiation and speed, duplex, and FEC for each port based on the ASIC and port speed. On NVIDIA platforms running Cumulus Linux, auto-negotiation defaults to *ON*.
- If auto-negotiation is *OFF* &mdash; which is called force mode &mdash; then speed, duplex and FEC must also be specified if a non-default value for the port is desired. If auto-negotiation is *ON*, then speed, duplex and FEC should not be specified. The only exception to this is for 1000BASE-X optical interfaces, where speed is *1000* and auto-negotiation is *ON* to get unidirectional link detection.
- If auto-negotiation is enabled on a link type that does not support auto-negotiation, the port enters *autodetect* mode (see the {{<link url="#autodetect" text="next section">}}) to determine the most likely speed and FEC settings to bring the link up. This feature is usually successful, but if the link does not come up, it might be necessary to disable auto-negotiation and set these link settings manually.
- There is no concept of auto-negotiation of MTU. To change the MTU from the default setting, {{<link url="Switch-Port-Attributes/#mtu" text="configure it explicitly">}}.
- Generally, you can ignore the duplex setting, except on 10M/100M links. The default is *Full*. Although you can configure the duplex setting, it has no option except *Full* on speeds higher than 1G and is auto-negotiated on 1000BASE-T links.

### Autodetect

As a result of the confusion about when auto-negotiation applies to a link type, many Ethernet software vendors, including Cumulus Linux, allow auto-negotiation ON to be configured on every interface type. When auto-negotiation is *ON*, but is not supported on a link type, the port software tries to determine the most likely link settings to bring the link up. Cumulus Linux calls this feature *autodetect*, but it is not directly configurable.

When auto-negotiation is enabled on a port, the behavior is as follows:

- When auto-negotiation is *ON*, the port is always in autodetect mode. The port steps through a list of possible auto-negotiation, speed and FEC settings for the port and module combination until the link comes up. The default configuration is auto-negotiation *ON*.

Autodetect is a local feature. The neighbor is assumed to either be configured with auto-negotiation off and speed, duplex, and FEC set manually, or using some equivalent algorithm to determine the correct speed, duplex, and FEC settings.

To see the user configured settings for auto-negotiation, speed, duplex and FEC compared to the actual operational state on the port hardware, use the `l1-show` command.

{{%notice note%}}
The autodetect feature is usually successful, but if the link does not come up, disable auto-negotiation and configure the link settings manually.  
{{%/notice%}}

## FEC

Forward Error Correction (FEC) is an algorithm used to correct bit errors along a medium. FEC encodes the data stream so that the remote device can correct a certain number of bit errors by decoding the stream.

The target IEEE bit error rate (BER) in high-speed Ethernet is 10<sup>-12</sup>. At 25G lane speeds and above, this might not be achievable without error correction, depending on the media type and length. See {{<link url="Switch-Port-Attributes/#fec">}} for a more detailed discussion of FEC requirements for certain cable types.

{{%notice note%}}
Both sides of a link must have the same FEC encoding algorithm enabled for the link to come up. If both sides appear to have a working signal path but the link is down, there might be an auto-negotiation mismatch or FEC mismatch in the configuration.
{{%/notice%}}

### FEC Encoding Algorithms and Settings

- The Reed-Solomon RS-FEC(528,514) algorithm adds 14 bits of encoding information to a 514 bit stream. It replaces and uses the same amount of overhead in the 64B/66B encoding so that the bit rate is not affected. The algorithm can correct 7 bit errors in a 514 bit stream. RS(528,514) is used on 25G (NRZ) lanes, including 25G, 50G-CR2, and 100G-SR4/CR4 interfaces.
- The Reed-Solomon RS-FEC(544,514) algorithm adds 30 bits of overhead to correct 14+ bit errors per 514 bits. FEC RS is required on 50G (PAM4) lanes; all 200G, 400G, 100G-CR2 and 50G-CR interfaces.
- Base-R (also known as FireCode/FC) FEC adds 32 bits per 32 blocks of 64B/66B to correct 11 bits per 2048 bits. It replaces one bit per block, so it uses the same amount of overhead as 64B/66B encoding. It is used in 25G interfaces only. The algorithm executes faster than the RS-FEC algorithm, so latency is reduced. Both RS-FEC and Base-R FEC are implemented in hardware.
- None/Off: FEC is optional and is often useful on 25G lanes, which includes 100G-SR4/CR4 and 50G-CR2 links. If the cable quality is good enough to achieve a BER of 10<sup>-12</sup> without FEC, then there is no reason to enable it. 10G/40G links should never require FEC. If a 10G/40G link has errors, replace the cable or module that is causing the error.
- Auto: FEC can be auto-negotiated between 2 devices. When auto-negotiation is *ON*, the default FEC setting is *auto* to enable FEC capability information to be sent and received with the neighbor. The port FEC active/operational setting is set to the result of the negotiation. *Auto* is the default setting on NVIDIA switches (auto-negotiation *ON* is the default setting).
- If auto-negotiation is disabled on 100G and 25G interfaces, you must set FEC to *OFF**, RS, or BaseR to match the neighbor. The FEC default setting of *auto* does not link up when auto-negotiation is disabled.

In some cases, the configured value might be different than the operational value. In such cases, the `l1-show` command displays both values. For example:

- Configured: Auto, Operational: RS.  
- Configured: RS, but link is down, so Operational is: None/Off

## Signal Integrity

The goal of Ethernet protocols and technologies is to enable the bits generated on one side of a link to be received correctly on the other side. The next two sections provide information about what might be happening on the link level when the link is down or bits are not received correctly.

### Link State: RX Power, Signal Detection, Signal Lock, Carrier Detection, RX Fault

Various characteristics show the state of a link. All characteristics might not be available to display on all platforms.

- RX power: On optical modules with DDM/DOM capabilities, the module shows the power level of the received signal. Note that a module can receive a signal with plenty of power, but still not be able to recover the data from a signal because it is distorted.
- Signal detected: A signal is received from the remote device on the local port receiver.
- Signal lock: The local port receiver is locked onto a good signal that is received from the remote side.
- Carrier detected: Both ends of the link are able to understand the data being sent to them. The link should be up on both sides.
- RX fault (None, Local, Remote or Local/Remote): The local end or the remote end is alerting that it is not receiving and/or understanding a good signal and bit stream.
  - Local fault indicates the local end does not have signal lock or cannot understand the data sent to it on its RX path.
  - Remote fault indicates that the local end RX path has signal lock and can understand the bit stream from the neighbor, but the remote neighbor is sending alerts over that working path indicating that it has no signal lock or cannot understand the data sent to it over its own RX path.

### Eyes

When a 1 or a 0 bit is transmitted across a link, it is represented on the electrical side of the port as either a high voltage level or a low voltage level. If an oscilloscope is attached to those leads, as the bit stream is transmitted across it, the transitions between 1 and 0 form a pattern in the shape of an eye.

{{<figure src="/images/cumulus-linux/L1ts-NRZ-eyes.jpg" width="600">}}

The farther the distance between the 1 and 0, the more open the eye appears. The more open the eye is, the less likely it is for a bit to be misread. When a bit is misread, it causes a bit-error, which results in an FCS error on the entire packet being received. A lower eye measurement generally translates to a larger bit error rate (BER). FEC can correct bit errors up to a point.

Eyes are not measured on fixed copper ports and are not measured when a link is down.

Each hardware vendor implements some quantitative measurement of eyes and some kind of qualitative measurement.

On an NVIDIA switch, the eyes are assigned a height in mV and a grade. For speeds below 100G (NRZ encoding), when the grade goes below 4000, the error rate or stability of the link might be negatively impacted.  

A link might have no stability problems with a measurement below these values, and FEC might correct all errors presented on such a link. For some interface types, FEC is required to remove errors up to BER levels that are expected on the media.

For 50G lanes (200G- and 400G-capable ports), the link uses PAM4 encoding, which has 3 eyes stacked on top of each other and therefore much smaller eye measurements. FEC is required on these links.

## l1-show Command

Because Linux Ethernet tools do not have a unified approach to the various vendor driver implementations and areas that affect layer 1, Cumulus Linux uses the `l1-show` command to show all layer 1 aspects of a Cumulus Linux port and link.

You must run the `l1-show` command as root. The syntax for the command is:

```
cumulus@switch:~$ sudo l1-show PORTLIST
```

Here is the output from the NVIDIA SN2410 switch on the other side of the same link:

```
cumulus@2410-switch:~$ sudo l1-show swp43
Port:  swp43
  Module Info
      Vendor Name: Mellanox               PN: MCP2M00-A003
      Identifier: 0x03 (SFP)              Type: 25g-cr
  Configured State
      Admin: Admin Up     Speed: 25G      MTU: 9216
      Autoneg: On                         FEC: Auto
  Operational State
      Link Status: Kernel: Up             Hardware: Up
      Speed: Kernel: 25G                  Hardware: 25G
      Autoneg: On (Autodetect enabld)     FEC: None
      TX Power (mW): None
      RX Power (mW): None
      Topo File Neighbor: bcm-switch-1, swp43
      LLDP Neighbor:      bcm-switch-1, swp43
  Port Hardware State:
      Compliance Code: 100GBASE-CR4 or 25GBASE-CR CA-L
      Cable Type: Passive copper cable
      Speed: 25G                          Autodetect: Enabled
      Eyes: 79                            Grade: 5451
      Troubleshooting Info: No issue was observed.
```

The output is in the following sections:

- Module Info: Shows basic information about the module, according to the module EEPROM.
- Configured State: Shows configuration information of the port, as defined in the kernel.
- Operational State: Shows high level details of the actual link status of the port in the hardware and kernel.
- Port Hardware State: Shows low level port information from the port on the switch ASIC.

## Module Information

The vendor name, vendor part number, identifier (QSFP/SFP type), and type (compliance codes) comes from the vendor EEPROM. See {{<link url="#compliance-codes-ethernet-type-ethmode-type-interface-type" text="Compliance Codes, Ethernet Type, Ethmode Type, Interface type">}} above for an explanation.

```
Module Info
    Vendor Name: Mellanox               PN: MCP2M00-A003
    Identifier: 0x03 (SFP)              Type: 25g-cr
```

### Configured State

The configured state reflects the configuration you apply to the kernel with `ifupdown2`. The `switchd` daemon translates the kernel state to the platform hardware state and keeps them in sync.

```
Configured State
    Admin: Admin Up     Speed: 25G      MTU: 9216
    Autoneg: On                         FEC: Auto
```

- `Admin state`:  
  - *Admin Up* means the kernel has enabled the port with NVUE, `ifupdown2`, or temporarily with `ip set line <swp> up`.
  - *Admin Down* means the kernel has disabled the port.
- `Speed`:  
  - The configured speed in the kernel.  
  - The maximum speed is in the `/etc/cumulus/ports.conf` file.
  - You can lower the speed with NVUE or `ifupdown2`.
  - If you enable auto-negotiation, this output displays the negotiated or auto-detected speed.
- `MTU`: The configured MTU setting in the kernel.
- `Autoneg`: The configured auto-negotiation state in the kernel. See {{<link url="#auto-negotiation" text="Auto-negotiation">}} for more information.
- `FEC`: The configured state of FEC in the kernel. See {{<link url="#fec" text="FEC">}}, above for more information.

### Operational State

The operational state shows the current state of the link in the kernel and in the switch hardware.

```
  Operational State
      Link Status: Kernel: Up             Hardware: Up
      Speed: Kernel: 25G                  Hardware: 25G
      Autoneg: On (Autodetect enabld)     FEC: None
      TX Power (mW): None
      RX Power (mW): None
      Topo File Neighbor: switch-1, swp43
      LLDP Neighbor:      switch-1, swp43
```

- `Link Status` and `Speed`: The kernel state and hardware state matches, unless the link is in some unstable or transitory state.
- `Autoneg` and `Autodetect`: See {{<link url="#auto-negotiation" text="Auto-negotiation">}} above for more information.
- `FEC`: The operational state of FEC on the link. See {{<link url="#fec" text="FEC">}} above for more information.
- `TX Power` and `RX Power`: These values come from the module DDM/DOM fields to indicate the optical power strength measured on the module if the module implements the feature. The switch supports, both, only RX, or neither. This does not apply to DAC and twisted pair interfaces.
- `Topo File Neighbor`: If you populate the `/etc/ptm.d/topology.dot` file and the `ptmd` daemon is active, the entry matching this interface shows.
- `LLDP Neighbor`: If the `lldpd` daemon is running and the switch receives LLDP data from the neighbor, the neighbor information shows here.

### Port Hardware State

The port hardware state shows additional low level port information. The output varies between vendors.

Here is the output on NVIDIA platforms:

```
  Port Hardware State:
      Compliance Code: 100GBASE-CR4 or 25GBASE-CR CA-L
      Cable Type: Passive copper cable
      Speed: 25G                          Autodetect: Enabled
      Eyes: 79                            Grade: 5451
      Troubleshooting Info: No issue was observed.
```

The NVIDIA port firmware automatically troubleshoots link problems and displays items of concern in the *Troubleshooting Info* section of this output.

See {{<link url="#fec" text="FEC">}}, {{<link url="#auto-negotiation" text="Auto-negotiation">}} and {{<link url="#signal-integrity" text="Signal Integrity">}} above for more details.

## Troubleshoot Layer 1 Problems

This section provides a troubleshooting process and checklist to help resolve layer 1 issues for modules.

The root cause of a layer 1 problem falls into one of these three categories:

- Configuration issues: A misconfiguration on one neighbor or the other, or a configuration mismatch between the neighbors.
- Hardware issues: Failures in fiber patches or modules and, on rare occasions, a QSFP or SFP port.
- Switch driver errors in handling a particular module type. These errors are rare and you can usually work around them.

To resolve a layer 1 problem, follow these steps:

- {{<link url="#classify-the-layer-1-problem" text="Characterize and classify">}} the problem.
- Design a test that best displays the lowest level indicator of that problem behavior. The hierarchy view of `l1-show` is often the best tool to find this indicator.
- Make changes based on the problem type that leads toward isolating the root cause of the failure. Use the test to track progress.
  - Identify if the issue is likely a configuration issue or a hardware issue. If unclear, start with configuration first.
  - For configuration issues, ensure the configuration on both ends of the link matches the guidance in this guide and in {{<link url="Switch-Port-Attributes" text="Switch Port Attributes">}}.
  - For hardware issues, isolate the faulty component by methodically moving and replacing components as described in {{<link url="#isolate-faulty-hardware" text="Isolate Faulty Hardware">}} below.
- After you isolate the root cause, make the changes permanent to resolve the problem. For faulty hardware, replace the failed component.

### Classify the Layer 1 Problem

You can classify layer 1 problems as follows:

- {{<link url="#troubleshoot-down-or-flapping-links" text="Link down or flapping">}}
- {{<link url="#troubleshoot-physical-errors-on-a-link" text="Physical errors on link">}}; these are not the same as *drops*, which are layer 2 or layer 3 switching issues
- {{<link url="#troubleshoot-signal-integrity-issues" text="Signal integrity issues">}}, which manifest as errors, link down or link flapping
- {{<link url="#troubleshoot-mtu-size-mismatches" text="MTU size mismatches">}}
- {{<link url="#troubleshoot-high-power-module-issues" text="High power module issues">}}
- {{<link url="#troubleshoot-i2c-issues" text="I2C issues">}}

See the sections below for specific guidance for each problem type.

### Isolate Faulty Hardware

When you suspect that one of the components in a link is faulty, use the following approach to determine which component is faulty.

First, identify the faulty behavior at the lowest level possible, then design a test that best displays that behavior. Use the hierarchy output of `l1-show` to find the best indicator. Here are some examples of tests you can use:

- No RX power: Examine the *RX power* in the *Operational State* section of the `l1-show` output.
- Remote side is sending *RX Faults*: Check the *Troubleshooting info* for *neighbor is sending remote faults*.
- Errors on link when FEC is not required: Examine the *HwIfInErrors* counters in `ethtool -S <swp>` to see if they are incrementing over time.

Try swapping the modules and fibers to determine which component is bad:

- Swap the DAC, AOC or fiber patch cables along the path with known good cables. Does the test indicate that the symptoms change?
- Swap the modules between the local and remote. Does the test indicate the symptoms move with the module or stay on the same neighbor?
- Loopback tests: Move one of the modules to the neighbor and connect the two modules back-to-back in the same switch, ideally with the same cable. What does the test indicate now? Now, move both modules to the other side and repeat. Try to isolate the issue to a single fiber, module, port, platform or configuration.
- Replace each module one at a time with a different module of the same type; the current module could be bad.
- Replace each module with a different module from a different vendor. Use a module that the Cumulus Linux switch supports. Check the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}}.

## Troubleshoot Down or Flapping Links

A down or flapping link can exhibit any or all the following symptoms:

- `l1-show` returns *Link Status: Kernel: Down* and *Hardware: Down* for the operational state.
- `ip link show <swp>` returns *<NO-CARRIER,BROADCAST,MULTICAST,UP>*. An *up* link returns something like *<BROADCAST,MULTICAST,UP,LOWER_UP>*.
- `ip link show` changes every second or two, indicating the link is flapping up or down.
- Log messages in `/var/log/linkstate` indicate the carrier is flapping up or down.
- The switch does not receive any LLDP data, or the link is flapping.

To begin troubleshooting, examine the output of `l1-show` on both ends of the link if possible. The output contains all the pertinent information to help troubleshoot the link.

```
cumulus@switch~$ sudo l1-show swp10
Port:  swp10
  Module Info
      Vendor Name: FINISAR CORP.          PN: FTLX8574D3BCL
      Identifier: 0x03 (SFP)              Type: 10g-sr
  Configured State
      Admin: Admin Up     Speed: 10G      MTU: 9216
      Autoneg: On                         FEC: Auto
  Operational State
      Link Status: Kernel: Up             Hardware: Up
      Speed: Kernel: 10G                  Hardware: 10G
      Autoneg: On (Autodetect enabld)     FEC: None
      TX Power (mW): [0.5267]
      RX Power (mW): [0.5427]
      Topo File Neighbor: qct-ix8-51, swp3
      LLDP Neighbor:      qct-ix8-51, swp3
  Port Hardware State:
      Compliance Code: 10G Base-SR
      Cable Type: Optical Module (separated)
      Speed: 10G                          Autodetect: Enabled
      Eyes: 411                           Grade: 41609
      Troubleshooting Info: No issue was observed.
```

Working from top to bottom of the `l1-show` output on both sides of the link, ask the questions listed below.

### Examine Module Information

```
Module Info
    Vendor Name: FINISAR CORP.          PN: FTLX8574D3BCL
    Identifier: 0x03 (SFP)              Type: 10g-sr
```

- Does the module vendor name and vendor part number match the module that connects to the switch? Is this port the correct port with the link problem? Is the right module installed?
- Does the module type match the technology for this link? For example, if there is a 100G DAC, is this value *Type: 100G-CR4*? See {{<link url="#compliance-codes-ethernet-type-ethmode-type-interface-type" text="Compliance Codes, Ethernet Type, Ethmode Type, Interface Type">}} for more information.
- Does the device at the remote end recognize the module as the same Ethernet type that the local switch recognizes? Vendor outputs differ. If the remote device is not a Cumulus Linux device, consult the vendor documentation to determine how to display the Ethernet type for the installed module.

### Examine Configured State

```
Configured State
    Admin: Admin Up     Speed: 10G      MTU: 9216
    Autoneg: On                         FEC: Auto
```

- `Admin`: Is the link *Admin Up*? Is the link configured and enabled?
- `Speed`: Is the configured speed correct? Does it match the configured speed on the remote side?
- `MTU`: Does the MTU match on both sides? Note that an MTU mismatch does not prevent the link from coming up, but it does affect traffic forwarding.
- `Autoneg`: Does this setting match the configuration and is it what you expect? See {{<link url="#auto-negotiation" text="Auto-negotiation">}}.
- `FEC`: Is the FEC setting correctly configured? See {{<link url="#fec" text="FEC">}}.

### Examine Operational State

```
Operational State
    Link Status: Kernel: Up             Hardware: Up
    Speed: Kernel: 10G                  Hardware: 10G
    Autoneg: On (Autodetect enabld)     FEC: None
    TX Power (mW): [0.5267]
    RX Power (mW): [0.5427]
    Topo File Neighbor: qct-ix8-51, swp3
    LLDP Neighbor:      qct-ix8-51, swp3
```

- `Link status` (Kernel and Hardware): What is the current state of both?  
  - Normally these values should be in sync.
  - When troubleshooting a link down issue, one or both of these values is *down* (usually both).
  - In a link flapping issue, one or both of these values might change every second or less, so the output of this field might not represent the value in the next moment in time.
- `Speed` (Kernel and Hardware): Does the operational speed match the configured speed?
  - When the link is up, the kernel and hardware operational values should be in sync with each other and the configured speed.
  - When the link is down and auto-negotiation is on, the kernel value is *Unknown!* because the hardware does not synchronize to a speed.
  - When the link is down and auto-negotiation is off, the kernel speed displays the configured value. The *Hardware* field shows various values, depending on implementation of the particular hardware interface.
- `Autoneg` and `Autodetect`: Normally the operational value matches the configured value. This is informational only, but it is useful to know if `autodetect` is on. See {{<link url="#auto-negotiation" text="auto-negotiation">}} and {{<link url="#autodetect" text="autodetect">}}.
- `FEC`: This field is only useful for informational purposes. It displays the actual FEC only when the link is up.
  - When the link is down, the operational FEC is *None*.
  - When the link is up, this field shows the actual FEC value working on the link.
- `TX Power` and `RX Power` (optical modules only): If the module supports laser power DDM/DOM, are these values in working ranges?
  - Check the *Laser send power high/low alarm* and *Laser receive power high/low warning* thresholds in the output of `ethtool -m <swp>` to see what the expected low and high values are.
  - A short range module should send in the range of 0.6 and 1.0 mW and should work with receive power in the range of > 0.05 mW.
  - Long range optical modules have TX power above 1.0 mW.
  - When in doubt, consult the technical specifications for the particular module.
  - A value of *0.0000* or *0.0* indicates that the module does not support DDM/DOM TX or RX power, or the module is not transmitting or receiving a signal.
    - If the TX Power is *0.0000* or *0.0*, then either the module does not support TX DDM/DOM or the module lasers are off for some reason.
    - If the RX Power is *0.0000* or *0.0*, then either the module does not support RX DDM/DOM or the module receivers are not receiving a signal.
    - A value of *0.0001* indicates that the module supports DDM/DOM, but the module is not receiving or transmitting a signal.
      - If the TX Power is *0.0001*, then the module lasers are likely disabled for some reason.
      - If the RX Power is *0.0001*, then the module receivers are not receiving a signal.
    - On a QSFP module, check the value for each of the four lanes. Sometimes only one lane is failing and the entire link is down as a result.
- `Topo File Neighbor`: If you configure a `ptmd` topology file on the switch, you can identify the link neighbor you expect.
- `LLDP Neighbor`: Does this match the expected neighbor and port?
  - This value is the neighbor and port that LLDP reports.
  - If the link is down, this value is normally blank.

### Examine Port Hardware State

The following values come from the NVIDIA port firmware:

```
Port Hardware State:
    Compliance Code: 25GBASE-CR CA-S
    Cable Type: Passive copper cable
    Speed: N/A                          Autodetect: Enabled
    Eyes: 0                             Grade: 0
    Troubleshooting Info: Auto-negotiation no partner detected.
```

- `Compliance Code`:
  - Does the interface type recognized by the firmware match the type of module installed? Does the firmware correctly recognize the module type?
- `Cable Type`: Does the cable type that the firmware recognizes match the installed cable type?
- `Speed`:
  - Does the speed match the expected speed?
  - If auto-negotiation is on and the link is down, *N/A* or a speed you do not expect displays.
- `Autodetect`:
  - If *Enabled*, the link algorithm might be failing with the neighbor.  
  - Try disabling auto-negotiation and setting a forced speed.  
  - See {{<link url="#auto-negotiation" text="auto-negotiation">}} and {{<link url="#autodetect" text="autodetect">}} for more guidance.
- `Eyes` and `Grade`:  
  - If the link is not up, all zeros display.  
  - If the link is up, the RX eye (mV) and grade values display.  
  - See {{<link url="#eyes" text="Eyes">}} for more information.
- `Troubleshooting Info`:
  - What does the firmware assess as the problem? Although this information is at the end of the output, this is sometimes the first place to look for basic guidance.
  - Examples:
    - `The port is closed by command. Please check that the interface is enabled.` Configure the port so it is *Admin Up*.
    - `The cable is unplugged.` The firmware does not detect a module. Check to see if a module is in this port, or reseat the module.
    - `Auto-negotiation no partner detected.` The link is down because it does not see the neighbor. This is not very helpful to determine the cause alone.
      - Check the configurations on both sides for an auto-negotiation or FEC configuration mismatch.
      - If the link is a fiber link and the module supports RX/TX Power DDM/DOM, check the *RX Power* and *TX Power* values in the *Operational State* output of `l1-show` to help determine which component fails.
      - Follow the steps in {{<link url="#isolate-faulty-hardware" text="Isolate Faulty Hardware">}}; use this value or the *RX/TX Power* DDM/DOM value as the test.
    - `Force Mode no partner detected.` Auto-negotiation or autodetect is off, link is down because it does not see the neighbor. This is not very helpful to determine the cause alone.
      - Check the configurations on both sides for a speed, auto-negotiation, or FEC configuration mismatch.
      - If the link is a fiber link and the module supports RX/TX Power DDM/DOM, check the *RX Power* and *TX Power* values in the *Operational State* output of `l1-show` to help determine which component fails.
      - Follow the steps in {{<link url="#isolate-faulty-hardware" text="Isolate Faulty Hardware">}}; use this value or the *RX/TX Power* DDM/DOM value as the test.
    - `Neighbor is sending remote faults`. This end of the link is receiving data from the neighbor, but the neighbor is not receiving recognizable data from the local port. See *RX Fault* in {{<link url="#signal-integrity" text="Signal Integrity">}} above for details. The local device is not transmitting, the remote receiver is not receiving recognizable data or is receiving broken data.

### RX Signal Failure Examples

Here is the output from `l1-show` for an AOC (on swp6) with failed RX on lane 3. Because an AOC is an integrated fiber assembly, you must replace the entire assembly.

```
  Port:  swp6
  Module Info
      Vendor Name: XXXXX                  PN: AOC-XXXX
      Identifier: 0x0d (QSFP+)            Type: 40g-sr4
  Configured State
      Admin: Admin Up     Speed: 40G      MTU: 9216
      Autoneg: Off                        FEC: Off
  Operational State
      Link Status: Kernel: Down           Hardware: Down <=Link is down, Kernel and Hardware
      Speed: Kernel: 40G                  Hardware: 40G
      Autoneg: Off                        FEC: None (down)
      TX Power (mW): [1.1645, 1.171, 1.1155, 1.0945]
      RX Power (mW): [0.159, 0.1732, 0.153, 0.0067]  <=Low power on lane 3
      Topo File Neighbor: switch_1, swp6
      LLDP Neighbor:      None, None
  Port Hardware State:
      Rx Fault: Local  <=Local RX Failed  Carrier Detect: no <=No bi-directional communication
      Rx Signal: Detect: YYYY             Signal Lock: YYYN  <=No signal lock on lane 3
      Ethmode Type: 40g-sr4               Interface Type: SR4
      Speed: 40G                          Autoneg: Off
      MDIX: ForcedNormal, Normal          FEC: Off
      Local Advrtsd: None                 Remote Advrtsd: None
      Eyes: L: 357, R: 326, U: 211, D: 219, L: 328, R: 312, U: 206, D: 211,
            L: 359, R: 343, U: 211, D: 200, L: 0, R: 0, U: 0, D: 0 <= No valid eye on lane 3
```

Here is the `l1-show` output for an AOC with failed lanes 0 and 1. Note that signal lock is bouncing, and sometimes shows *Y*. You must replace the AOC.

```
Port:  swp8
  Module Info
      Vendor Name: XXXX                   PN: AOC-XXXX
      Identifier: 0x0d (QSFP+)            Type: 40g-sr4
  Configured State
      Admin: Admin Up     Speed: 40G      MTU: 9216
      Autoneg: Off                        FEC: Off
  Operational State
      Link Status: Kernel: Down           Hardware: Down <=Link is down, Kernel and Hardware
      Speed: Kernel: 40G                  Hardware: 40G
      Autoneg: Off                        FEC: None (down)
      TX Power (mW): [1.1762, 1.1827, 1.1272, 1.1062]
      RX Power (mW): [0.0001, 0.0001, 0.5255, 0.64]  <=Low power on lanes 0,1
      Topo File Neighbor: switch_2, swp10
      LLDP Neighbor:      None, None
  Port Hardware State:
      Rx Fault: Local  <=Local RX Failed  Carrier Detect: no <=No bi-directional communication
      Rx Signal: Detect: YYYY             Signal Lock: YNYY  <=No lock on lane 1 at moment of capture
      Ethmode Type: 40g-sr4               Interface Type: SR4
      Speed: 40G                          Autoneg: Off
      MDIX: ForcedNormal, Normal          FEC: Off
      Local Advrtsd: None                 Remote Advrtsd: None
      Eyes: L: 0, R: 0, U: 0, D: 0, L: 0, R: 0, U: 0, D: 0,  <=No valid eyes on lanes 0,1
            L: 359, R: 359, U: 214, D: 226, L: 359, R: 359, U: 243, D: 264
```

## Troubleshoot Physical Errors on a Link

Physical errors on a link occur if you have signal integrity issues or you do not configure the required FEC type on a particular module or cable type.  

The target bit error rate (BER) in high-speed Ethernet is 10<sup>-12</sup>. When BER exceeds this value, either configure the correct FEC setting or replace a marginal module, cable, or fiber patch. If the resulting BER on a link with correctly configured FEC is still unacceptable, you need to replace one of the hardware components in the link to resolve the errors.

See {{<link url="#fec" text="FEC">}} and {{<link url="#troubleshoot-signal-integrity-issues" text="Troubleshoot Signal Integrity Issues">}} for more details.

To see error counters for a port, run the `ethtool -S <swp> | grep Errors` command. If FEC is on, these counters only count errors that FEC does not correct.

On NVIDIA switches, to see the bit error count that FEC corrects on a link, run the `sudo l1-show <swp> --pcs-errors` command.

Because errors can occur during link up and down transitions, it is best to check error counters over a period of time to ensure they are incrementing regularly instead of displaying stale counts from when the link last transitions up or down. The `/var/log/linkstate` log files show historical link up and link down transitions on a switch.

## Troubleshoot Signal Integrity Issues

Signal integrity issues are often a root cause of different types of symptoms:

- If the signal integrity is very poor or non-existent, the link stays down.
- If the signal integrity is too marginal, the link might flap with or without FEC on.
- If the signal integrity is marginal, the link might display physical error counts. Depending on the link speed and cable type, the module or cable can have some margin of error in signal integrity. In these cases, use FEC to correct errors to reach the target IEEE bit error rate (BER) of 10<sup>-12</sup> on the link. See {{<link url="#fec" text="FEC">}} for guidance.

  If FEC is on and the bit stream does not recover acceptably, the link stays down. If the signal integrity is marginal, but bad enough that FEC cannot correct an acceptable rate of errors, the link flaps when FEC signals a restart of the link to attempt to restore an acceptable bit stream.  

To see error counters for a port, run the `ethtool -S <swp> | grep Errors` command. If FEC is on, these counters only count errors that FEC does not correct.

To see counts of bit errors that FEC corrects on a link, run the `sudo l1-show <swp> --pcs-errors` command.

Signal integrity issues are physical issues and usually, you must replace some hardware component in the link to fix the link. Follow the steps in {{<link url="#isolate-faulty-hardware" text="Isolate Faulty Hardware">}} to isolate and replace the failed hardware component.

On rare occasions, if the switch does not recognize a module correctly and is the wrong type (active instead of passive), it can cause a signal integrity issue.

See {{<link url="#active-and-passive-modules-and-cables" text="Active and Passive Modules and Cables">}}, {{<link url="#compliance-codes-ethernet-type-ethmode-type-interface-type" text="Compliance Codes, Ethernet Type, Ethmode Type, Interface Type">}} and {{<link url="#examine-module-information" text="Examine Module Information">}} for more details.

## Troubleshoot MTU Size Mismatches

Usually there is an MTU size mismatch when higher layer protocols like OSPF adjacencies fail or you lose non-fragmentable packets. Generally, an MTU settings mismatch does not affect link operational status.

To troubleshoot a suspected MTU problem, review the *Configured State* section in the output of `l1-show`:

```
Configured State
    Admin: Admin Up     Speed: 10G      MTU: 9216 <===
    Autoneg: On                         FEC: Auto
```

- Compare the MTU configuration with that of the neighbor. Do they match?
- Note that different vendors sometimes have different interpretations on the MTU value and might vary by a few bytes from another vendor. Research the vendor documentation to determine if you need to adjust this value in the configuration to match a neighbor.

## Troubleshoot High Power Module Issues

The SFF specifications allow for modules of different power consumption levels along with a request and grant procedure to enable higher levels.

An SFP module can have 3 different power classes:

1. 1.0W
1. 1.5W
1. 2.0W

Cumulus Linux enables power class 2 (1.5W) by default. All Cumulus Linux switches support 1.5W across all SFP ports simultaneously.

A QSFP module can have 8 different power classes:

1. 1.5W
1. 2.0W
1. 2.5W
1. 3.5W
1. 4.0W
1. 4.5W
1. 5.0W
1. 10.0W

*Low power mode* is power class 1 (1.5W). This is the state during initial boot.  

After hardware initialization, Cumulus Linux enables *normal power mode* on QSFP modules by default &mdash; power classes 2-4, 2.0W to 3.5W.

All Cumulus Linux switches support 3.5W across all QSFP ports simultaneously.

Some modules require *high power modes* for driving long distance lasers. Power classes 5-8 &mdash; 4.0W, 4.5W, 5.0W, 10.0W &mdash; are high power modes. If a module needs a high power mode, it can request it, which the switch grants if the port supports it.

To determine if a switch supports higher power modes, consult the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}} and the hardware manufacturer specifications for power limitations for a switch.

NVIDIA switches vary in their support of high power modules. For example, on some NVIDIA Spectrum 1 switches, only the first and last two QSFP ports support up to QSFP power class 6 (4.5W) and only the first and last two SFP ports support SFP power class 3 (2.0W) modules. Other Spectrum 1 switches do not support high power ports at all. Consult the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}} and the hardware manufacturer specifications for exact details of which ports support high power modules.

The total bus power rating is the default power rating per port type (SFP: 1.5W, QSFP: 3.5W) multiplied by the number of ports of each type present on the bus.

To see the requested and enabled status for high power module, review the output of `sudo ethtool -m`. The following output is from a device of power class between 1 and 4 (1.5W to 3.5W). The module does not request a high power class or the switch does not enable it.

```
cumulus@switch:mgmt:~# sudo ethtool -m swp53
        Identifier                                : 0x11 (QSFP28)
        Extended identifier                       : 0x00
        Extended identifier description           : 1.5W max. Power consumption <= ignore for high power modules
        Extended identifier description           : No CDR in TX, No CDR in RX
        Extended identifier description           : High Power Class (> 3.5 W) not enabled <= high power mode not requested or enabled
```

The following is the output from a power class 7 (5.0W) module. The module is requesting power class 7, but the  switch does not support or enable it. The switch only supports power class 6 on this port.

```
cumulus@switch:mgmt:~# sudo ethtool -m swp49
[sudo] password for cumulus:
       Identifier                                : 0x11 (QSFP28)
       Extended identifier                       : 0xcf
       Extended identifier description           : 3.5W max. Power consumption  <= ignore for high power modules
       Extended identifier description           : CDR present in TX, CDR present in RX
       Extended identifier description           : 5.0W max. Power consumption,  High Power Class (> 3.5 W) not enabled <= Request 5.0W, not enabled
 
```

The following is the output from a power class 6 (4.5W) module. The module is requesting power class 6 and the switch enables it.

```
cumulus@switch:mgmt:~# sudo ethtool -m swp3
        Identifier                                : 0x11 (QSFP28)
        Extended identifier                       : 0xce
        Extended identifier description           : 3.5W max. Power consumption <= ignore for high power modules
        Extended identifier description           : CDR present in TX, CDR present in RX
        Extended identifier description           : 4.5W max. Power consumption,  High Power Class (> 3.5 W) enabled <= Request 4.5W, enabled
```

## Troubleshoot I2C issues

Ethernet switches contain multiple I2C buses set up for the switch CPU to communicate low speed control information with the port modules, fans, and power supplies within the system.

On rare occasions, a port module with a defective I2C component or firmware can fail and lock up one or more I2C buses. Depending on the particular hardware design of a switch and the way in which the failure occurs, different symptoms of this failure display. Often traffic continues to work for a while in this failed condition, but sometimes the failure can cause modules to be incorrectly configured, resulting in link failures or increased error rates on a link. In the worst case, the switch reboots or locks up.

Because I2C issues are in the low speed control circuitry of a module, high speed traffic rates do not affect the data side of the module. Software bugs in Cumulus Linux do not cause these issues.

When the I2C bus has issues or lockups, installed port modules might no longer show up in the output of `sudo l1-show <swp>` or `sudo ethtool -m <swp>`. A significant number of `smbus` or `i2c` or `EEPROM read` errors might be present in `/var/log/syslog`. After one module locks up the bus, some or all the other modules then exhibit problems, making it nearly impossible to tell which module is causing the failure.  

Failed I2C components or defective designs in port modules cause an overwhelming number of I2C lockups. Low priced vendor modules cause most failures, but even high price, high quality modules can fail, only with much lower incidence; they have a higher MTBF rating. If you suspect an I2C issue, first look at the installed modules that are not on the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}}. The Cumulus Linux HCL includes modules that work in Cumulus Linux switches, which also have a solid track record in customer networks.

You might resolve the issue if you remove each port module one by one until the problem clears; this might indicate which module causes the failure. However, often the bus blocks in a way that requires a reboot or power cycle to clear the I2C failure. Clearing the failure in one of these ways works for a while, but when the conditions are right again, hours, days or months later, the marginal I2C component might fail again and lock up the switch.

In the worst situations, a switch might have multiple bad or marginal I2C modules from the same vendor batch, making it difficult to determine which module or modules are bad.

Because I2C problems can be very pernicious, often showing up again much later after the problem clears, deal with them quickly and forcefully.

To verify that an I2C failure is occurring, run `sudo tail -F /var/log/syslog` and look for `smbus` or `i2c` or `EEPROM read` errors that continue to appear or appear in bursts.

Based on the failure scenario when tyou discover the issue, choose when to address this issue; immediately or during a maintenance window.

- If traffic or the switch operates negatively and you cannot route traffic through a redundant network, you must do something immediately.
- If you can route traffic around the failing switch, allowing troubleshooting to proceed on the failed switch, proceed to reroute traffic to find an appropriate time to troubleshoot the failing switch.
- To troubleshoot the failure and restore the switch to working, use the following options according to the urgency of the situation:
  - Remove port modules one-by-one to see if the condition clears. This provides low probability of clearing the I2C failure, but possibly provides lower impact to traffic. If successful, this approach might reveal the problem module.
  - Restart `switchd` by running the `sudo systemctl reset-failed ; sudo systemctl restart switchd` command. Verify the condition clears after the restart completes. This provides a medium probability of clearing the I2C failure and a medium impact to traffic. It does not provide a way to discover which module failed.
  - Reboot the switch and verify the condition clears after the reboot completes. This provides a high probability of clearing the I2C failure, but also a high impact to traffic. It does not provide a way to discover which module failed.
  - Power cycle the switch and verify the condition clears after the reboot completes. This provides a very high probability of clearing the I2C failure, but also a very high impact to traffic. It does not provide a way to discover which module failed.
  - If the I2C failure recurs soon after a power cycle, you need to combine a binary strategy of removing half the modules at a time and power cycling.
  - If after removing all the modules, and power cycling, the I2C errors are still occurring, the next step is to remove each power supply and fan one by one between power cycles to see if one of those devices is blocking the I2C bus.
  - If you remove all modules and each power supply and you test the fan independently, and the I2C failures are still occurring, then the final step is to replace the switch.
  
If the switch is operational again due to one of the above methods, but you have not identified the module that caused, try the following approach:

- If there is a history in the `syslog` files of occasional errors on one module in advance of the failure, remove or replace that module first.
- If there are modules from vendors not on the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}}, seek to replace those modules with high priority.
- Replace any module that has caused problems in the past.
- Replace all modules in the switch.

If needed, contact the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Enterprise Support team">}} for additional help.
