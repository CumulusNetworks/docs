---
title: Troubleshoot Layer 1
author: NVIDIA
weight: 1025
toc: 3
---

This chapter describes how to troubleshoot layer 1 issues that can affect the modules connecting a switch to a network.

## Background

Before we describe various troubleshooting methods, it's helpful to understand some background information.

### Specifications

The following specifications are useful in understanding and troubleshooting layer 1 problems:

- {{<exlink url="https://standards.ieee.org/standard/802_3-2018.html" text="IEEE 802.3 specifications">}} define the technologies and link characteristics of the various types and speeds of Ethernet technologies.
- {{<exlink url="https://www.snia.org/technology-communities/sff/specifications" text="SFF MSA specifications">}} define the specifics of the hardware construction and implementations of features of the SFP and QSFP modules themselves.

### Form Factors

Modern Ethernet modules come in one of two form factors:

- Small Form factor Pluggables (SFP)
- Quad Small Form factor Pluggables (QSFP)

Each contains an EEPROM with information about the module's capabilities, and various groups of required or optional  registers to query or control aspects of the module when needed. The main values are decoded in the output from the `ethtool -m <swp>` command.

The memory locations for the various fields in the EEPROM and the common registers are defined in the SFF/MSA specifications:

- SFP: {{<exlink url="https://members.snia.org/document/dl/25916" text="SFF-8472">}}: *Management Interface for SFP+* (PDF)
- QSFP: {{<exlink url="https://members.snia.org/document/dl/26418" text="SFF-8636">}} *Management Interface for 4-lane Modules and Cables* (PDF)

Identifiers used in the first byte of the module memory map:

- 0x03: SFP/SFP+/SFP28 - One 10G or 25G lane - Small Formfactor Pluggable
- 0x0d: QSFP+ - Four 10G lanes - Quad SFP (40G total)
- 0x11: QSFP28 - Four 25G or 50G lanes (100G or 200G total) - Quad SFP with 25G or 50G lanes
- 0x18: QSFP-DD - Eight 50G lanes (400G total) - Quad SFP with a recessed extra card-edge connector to enable 8 lanes of 50G

### Encoding

There are two parts of high-speed Ethernet that are grouped under *encoding* in the output from the `ethtool -m <swp>` command:

- The way to represent bits on the wire or optical fiber:
  - NRZ (also known as PAM2): Has two voltage (or laser) levels signifying a 0 and 1. Negative voltage level = 0, positive voltage = 1. Used on all Ethernet technologies below lane speeds of 50Gbps.

  {{<figure src="/images/cumulus-linux/L1ts-NRZ-eyes.jpg" width="600">}}

  - PAM4 encoding: Has four signal level signifying two bits (00,01,10,11). These level are much closer together than the levels in NRZ/PAM2, so signal integrity is an even greater concern. PAM4 encoding is used on 50G lanes.

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

On the ASIC, the 40G, 100G and 200G SerDes devices are 4 lanes; 400G SerDes uses 8 lanes. So an SFP port is actually one lane on a four lane SerDes. Depending on the platform design, this sometimes affects how SFP ports can be configured and broken out.

Combining these two ideas, port speeds are created using the following formulas:

| Port Speed | Number of Lanes |
| ---------- | --------------- |
| 1G | One 10G or 25G lane clocked at 1G. Or, on a 1G fixed copper switch, a 1G lane. |
| 10G | One 10G lane. |
| 25G | One 25G lane. |
| 40G | Four 10G lanes. |
| 50G | Two 25G lanes or one 50G lane. |
| 100G | Four 25G lanes (100G SR4/CR4) or two 50G lanes (100G CR2). |
| 200G | Four 50G lanes. |
| 400G | Eight 50G lanes. |

## Active and Passive Modules and Cables

From the point of view of the port, modules and cables can be classified as either *active* or *passive*.

Active cables and modules contain transmitters that regenerate the bit signals over the cable. All optical modules are active. 10/100/1000BaseT and 10GBaseT are active modules and contain an onboard PHY that handles the BaseT autonegotiation and TX/RX to the remote BaseT device. For active modules, the port only has to provide a TX signal with a base level of power to the module, and the module uses the power it receives on the port power bus to regenerate the signal to the remote side.

Although some copper cable assemblies are active, they are extremely rare.

Passive cables (copper DACs) directly connect the port side of the module to the copper twinax media on the other side of the module in the assembly. The port TX lines provides the power to drive the signal to the remote end. The port goes through a training sequence with the remote end port to tune the power TX and RX parameters to optimize the received signal and ensure correct clock and data recovery at each RX end.

## Compliance Codes, Ethernet Type, Ethmode Type, Interface Type

These four terms essentially mean the same thing: the type of Ethernet technology that the module implements.

In order for the port to know the characteristics of the module that is inserted, the SFP or QSFP module EEPROMs have a standardized set of data to describe the module characteristics. These values appear in the output of `ethtool -m <swp>`.

The compliance codes describe the type of Ethernet technology the module implements. Examples include 1000Base-T, 10GBase-SR, 10GBase-CR, 40GBase-SR4 and 100GBase-CR4.

The last part of the compliance code specifies the Ethernet technology and the number of lanes used:

- \-T: Twisted pair.
- CR: Copper twinax (passive DAC). CR4 uses a bundle of 4 twinax cables for 4 lanes, CR2 uses 2 cables, CR uses 1.
- SR: Optical short range. SR4 uses a bundle of 4 fibers for 4 lanes.
- LR: Optical long range. LR4 uses 4 wavelengths over one fiber pair to transmit 4 lanes over long distances (kilometers).
- xWDM (SWDM, CWDM, DWDM): Optical wavelength multiplexed technologies (various). Multiple lanes are transmitted by different wavelengths.

An active module with a passive module compliance code and vice versa would cause the port to be set up incorrectly and may affect signal integrity.

Some modules have vendor specific coding, are older, or are using a proprietary vendor technology that is not listed in the standards. As a result, they are not recognized by default and need to be overridden to the correct compliance code.  On Mellanox platforms, the port firmware has known and support modules hardcoded to the correct compliance code. On Broadcom platforms, the `/usr/share/cumulus/portwd.conf` file contains known overrides for certain modules. On Broadcom platforms, the user can also create an override file in `/etc/cumulus/portwd.conf` to specify that a module is best represented by a particular compliance code.

The override file uses the vendor OUI (preferred) or the vendor name, plus the vendor PN (all from the module EEPROM) to specify the correct override compliance code of the module. For example:

```
[cables]
44:7c:7f,C41MF=40g-sr4
DELL EMC,C41MF=40g-sr4
```

## Digital Optical Monitoring (DOM)

DOM is an optional capability that vendors can implement on their optical transceivers to display to the user various useful measurements about the optical power. The values are generally reliable within a 10% tolerance. A value of *0.0000* generally indicates the value is not implemented by the vendor.

The most useful DOM values when troubleshooting a problem link are:

- RX optical power (receiver signal average optical power)
- TX optical power (laser output power)  

The location of DOM fields are standardized, so if DOM capability is present on a module, the values are displayed in the output of `ethtool -m <swp>`.

For each DOM value there can be thresholds to mark a high or low *warning* or an *alarm* when the value exceeds that threshold.

Generally, an alarm value indicates the level required for the signal to be within the vendor's design tolerance, and the warning level is a little bit closer to expected norms.

When a warning or alarm is triggered, the flag flips from *Off* to *On*. Reading that value with `ethtool -m` or NVIDIA NetQ (or some other monitoring software) resets this flag back to *Off*.

## Autonegotiation

The definition of autonegotiation (or autoneg) has changed slightly with each new Ethernet speed and technology. As a result, there are 3 different types of autoneg (IEEE 802.3 clauses 28, 37, 73), which apply to various Ethernet technologies that Cumulus Linux supports:

- 10/100/1000/10GBASE-T (twisted pair, clause 28): The original Ethernet autoneg, which negotiates speed and duplex (full/half) and flow control (link pause) on full-duplex. Mandatory for 1G/10G data rates.
- 1000BASE-X (optical, clause 37): Detects unidirectional link (no RX on one side) and signal to bring the port down; this avoids blackholing traffic.
- 40G/100G/25G/50G/200G/400GBASE-CR (DAC, clause 73): Negotiates speed, performs link training to improve BER and negotiates FEC.

Note that many Ethernet technologies used in Cumulus Linux switches do not have autoneg capability. Notably:

- All 10G links do not have autonegotiation. However, there is an autoneg for backplane links, but these links do not exist on Cumulus Linux switch ports.
- All optical links except 1G optical do not have autonegotiation.  

Thus, only about half of all modern link types even support autoneg, leading to much confusion regarding whether to enable or disable autoneg.

The next three subsections provide guidance on when and how to enable autonegotiation.

### Ethernet Link Types and Autonegotiation

1000BASE-T and 10GBASE-T fixed copper ports require autonegotiation for 1G and 10G speeds. This is the default setting and cannot be disabled for 1G speeds. Disabling autoneg on these ports requires setting the speed to 100Mbps or 10Mbps and the correct {{<link url="Switch-Port-Attributes/#port-speed-and-duplex-mode" text="duplex">}} setting.

1000BASE-T SFPs have an onboard PHY that does the autonegotiation automatically on the RJ45 side without involving the port. Do not change the default autoneg setting on these ports; on Mellanox switches, autoneg is *ON* while on Broadcom switches, autoneg is *OFF*.

For 1000BASE-X, autonegotiation is highly recommended on 1G optical links to detect unidirectional link failures.

For all other optical modules, there is no autonegotiation on any optical links except for 1000BASE-X.

For 10G DACs, there is no autonegotiation.

For DAC cables on speeds higher than 25G, autonegotiation is unnecessary, but is useful because it can improve signal integrity by link training. It also negotiates speed and FEC, but this is less useful since the neighbor speed and FEC is usually known.

On Broadcom platforms, when autonegotiation is enabled, the output of `l1-show` displays the local advertised autonegotiation capabilities and the remote advertised autonegotiation capabilities, provided the link is up.

### General Autonegotiation Guidance

- When autoneg is supported on an Ethernet type, both sides of the link must be configured with the same autoneg setting.
- Cumulus Linux sets a default for autoneg and/or speed, duplex and FEC for each port based on the ASIC and port speed. On Mellanox platforms running Cumulus Linux, autoneg defaults to *ON*. On Broadcom platforms running Cumulus Linux, autoneg and FEC default to *OFF*, and the maximum speed for the port as defined in `ports.conf`.
- If autoneg is *OFF* &mdash; which is called force mode &mdash; then speed, duplex and FEC must also be specified if a non-default value for the port is desired. If autoneg is *ON*, then speed, duplex and FEC should not be specified. The only exception to this is for 1000BASE-X optical interfaces, where speed is *1000* and autoneg is *ON* in order to get unidirectional link detection.
- If autoneg is enabled on a link type that does not support autoneg, the port enters *autodetect* mode (see the {{<link url="#autodetect" text="next section">}}) to try and determine the most likely speed and FEC settings to bring the link up. This feature is usually successful, but if the link does not come up, it may be necessary to disable autoneg and set these link settings manually.
- There is no concept of autoneg of MTU. To change the MTU from the default setting, {{<link url="Switch-Port-Attributes/#mtu" text="configure it explicitly">}}.
- Generally, the duplex setting can be ignored except on 10M/100M links. The default is *Full*. Although you can configure it, it has no option except *Full* on speeds higher than 1G and is autonegotiated on 1000BASE-T links.

### Autodetect

As a result of the confusion about when autoneg applies to a link type, many Ethernet software vendors, including Cumulus Linux, allow autoneg ON to be configured on every interface type. When autonegotiation is *ON*, but is not supported on a link type, the port software tries to determine the most likely link settings to bring the link up. Cumulus Linux calls this feature *autodetect*, but it is not directly configurable.

When autonegotiation is enabled on a port, the behavior is as follows:

- On Mellanox platforms, when autoneg is *ON*, the port is always in autodetect mode. The port steps through a list of possible autoneg, speed and FEC settings for the port and module combination until the link comes up. The default configuration is autoneg *ON*, which essentially means *autodetect on* for Mellanox switches.
- On Broadcom platforms, if autoneg is available on the Ethernet type, it is enabled. On Ethernet types that do not support autoneg, Cumulus Linux treats autoneg as *autodetect*. At the port hardware level it sets:
  - Autoneg to OFF.
  - Speed to the max speed defined in `ports.conf`.
  - FEC to RS on 100G, FEC BaseR on 25G, and OFF everywhere else.

Autodetect is a local feature. The neighbor is assumed to either be configured with autoneg off and speed, duplex and FEC set manually, or using some equivalent algorithm to determine the correct speed, duplex and FEC settings.

To see the user configured settings for autoneg, speed, duplex and FEC versus the actual operational state on the port hardware, use the `l1-show` command.

{{%notice note%}}

The autodetect feature is usually successful, but if the link does not come up, it may be necessary to disable autonegotiation and configure the link settings manually.  

{{%/notice%}}

## FEC

Forward Error Correction (FEC) is an algorithm used to correct bit errors along a medium. FEC encodes the data stream so that the remote device can correct a certain number of bit errors by decoding the stream.

The target IEEE bit error rate (BER) is 10<sup>-12</sup>. At 25G lane speeds and above, this may not be achievable without error correction, depending on the media type and length. See {{<link url="Switch-Port-Attributes">}} for a more detailed discussion of FEC requirements for certain cable types.

Both sides of a link must have the same FEC encoding algorithm enabled for the link to come up. If both sides are showing signal lock, but no carrier and/or local RX faults, there could be an autoneg mismatch or FEC mismatch in the configuration.

### FEC Encoding Algorithms and Settings

- The Reed-Solomon RS-FEC(528,514) algorithm adds 14 bits of encoding information to a 514 bit stream. It replaces and uses the same amount of overhead in the 64B/66B encoding, so that the bit rate is not affected. It can correct 7 bit errors in a 514 bit stream. RS(528,514) is used in 25G lanes (for example, 25G and 100G interfaces).
- The Reed-Solomon RS-FEC(544,514) algorithm adds 30 bits of overhead to correct 14 bit errors per 514 bits. It is used on 50G lanes, hence, 200G, 400G and 100G CR2 interfaces.
- Base-R (also known as FireCode/FC) FEC adds 32 bits per 32 blocks of 64B/66B to correct XX bits per 2048 bits. It replaces one bit per block, so it uses the same amount of overhead as 64B/66 encoding. It is used in 25G interfaces only. The algorithm executes faster than the RS-FEC algorithm, so latency is reduced. Both RS-FEC and Base-R FEC are implemented in hardware.
- None/Off: FEC is optional and is often useful on 25G and 50G lanes. On 25G lanes (including 100G and 2x50G cables), if the cable quality is good enough to achieve a BER of 10<sup>-12</sup> without FEC, then there is no reason to enable it.  10G/40G links should never require FEC. If a 10G/40G link has errors, replace the cable. None/Off is the default setting on Broadcom switches since autoneg *OFF* is the default setting.
- Auto: FEC can be autonegotiated between 2 devices. When autoneg is *ON*, the default FEC setting is *auto* to enable FEC capability information to be sent and received with the neighbor and the port FEC active/operational setting is set to the result of the negotiation. *Auto* is the default setting on Mellanox switches since autoneg *ON* is the default setting.

In some cases, the configured value may be different than the operational value. In such cases, the `l1-show` command displays both values. For example:

- Configured: Auto, Operational: RS.  
- Configured: RS, but link is down, so Operational is: None/Off

## Signal Integrity

The goal of Ethernet protocols and technologies is to enable the bits generated on one side of a link to be received correctly on the other side. The next two sections provide information as to what might be happening on the link level when the link is down or bits are not being received correctly.

### Link State: RX Power, Signal Detection, Signal Lock, Carrier, RX Fault

Various characteristics show the state of a link. All characteristics may not be available to display on all platforms.

- RX power: On optical modules with DOM capabilities enabled, the module shows the power level of the received signal. Note that a module can receive a signal with plenty of power, but still not be able to recover the data from a signal because it is distorted.
- Signal detected: A signal is received from the remote device on the port itself.
- Signal lock: The local port receiver is locked onto a good signal that is received from the remote side.
- Carrier detected: Both ends of the link are able to understand the data being sent to them. The link should be up on both sides.
- RX fault (None, Local, Remote or Local/Remote): The local end or the remote end is alerting that it is not receiving and/or understanding a good signal and bit stream. A Local fault indicates the local end does not have RX lock or cannot understand the data sent to it. A Remote fault indicates that the local end can understand the RX signal and bit stream, but the remote end is sending alerts over a working path for which it has no RX lock or it cannot understand the data sent to it.

{{%notice tip%}}

If both sides are showing signal lock, but not carrier, it could be there is an autoneg mismatch or FEC mismatch in the configuration.

{{%/notice%}}

### Eyes

When a 1 or a 0 bit is transmitted across a link, it is represented on the electrical side of the port as either a high voltage level or a low voltage level, respectively. If an oscilloscope is attached to those leads, as the bit stream is transmitted across it, the transitions between one and zero would form a pattern in the shape of an eye.

{{<figure src="/images/cumulus-linux/L1ts-NRZ-eyes.jpg" width="600">}}

The farther the distance between the 1 and 0, the more open the eye appears. The better &mdash; that is, more open &mdash; the eye is, the less likely it is for a bit to be misread. When a bit is misread, it causes a bit-error, which would result in an FCS error on the entire packet being received. A lower eye measurement generally translates to a larger bit-error rate (BER). FEC can correct bit errors up to a point.

Eyes are not measured on fixed copper ports. Nor are they measured when a link is down.

Each hardware vendor implements some quantitative measurement of eyes and some kind of qualitative measurement.

On a Mellanox switch, the eyes are assigned a height in mV and a grade. As a rule of thumb for speeds below 100G (NRZ encoding), when the grade goes below 4000, the error rate or stability of the link may be negatively impacted.  

On a Broadcom switch, the eyes are assigned a value for up, down, left, right (U,D,L,R) measurements from the center of the eye. As a rule of thumb, when the up or down measurement goes below *100* or the left/right measurement goes below *150*, the error rate or stability of the link may be negatively impacted.

Note that these rules of thumb are only an indicator when troubleshooting a problem link. A link may have no stability problems with a measurement below these values, and FEC may correct all errors presented on such a link. For some interface types, FEC is required for the very reason to remove errors up to BER levels that are expected on the media.

For lanes speeds above 50G (200G- and 400G-capable ports), the link uses PAM4 encoding, which has 3 eyes stacked on top of each other and therefore much smaller eye measurements. The rules of thumb mentioned above do not apply.

## l1-show Command

Because Linux Ethernet tools do not have a unified approach to the various vendor driver implementations and areas that affect layer 1, the `l1-show` command was added to Cumulus Linux versions 3.7.7 and 4.0.0 in order to show all layer 1 aspects of a Cumulus Linux port and link.

```
cumulus@switch:~$ sudo l1-show PORTLIST
```

### l1-show Output

Here is the output from a 25G DAC link on a Mellanox switch:

```
cumulus@switch:~$ sudo l1-show swp43
Port:  swp43
  Module Info
      Vendor Name: Mellanox               PN: MCP2M00-A003
      Identifier: 0x03 (SFP)              Type: 25g-cr
  Configured State
      Admin: Admin Up     Speed: 25G      MTU: 9216
      Autoneg: Off                        FEC: Off
  Operational State
      Link Status: Kernel: Up             Hardware: Up
      Speed: Kernel: 25G                  Hardware: 25G
      Autoneg: Off                        FEC: Off
      TX Power (mW): None
      RX Power (mW): None
      Topo File Neighbor: mlx-switch-1, swp43
      LLDP Neighbor:      mlx-switch-1, swp43
  Port Hardware State:
      Rx Fault: None                      Carrier Detect: yes
      Rx Signal: Detect: Y                Signal Lock: Y
      Ethmode Type: 25g-cr                Interface Type: CR
      Speed: 25G                          Autoneg: Off
      MDIX: ForcedNormal, Normal          FEC: Off
      Local Advrtsd: None                 Remote Advrtsd: None
      Eyes: L: 281, R: 296, U: 118, D: 118
```

Here is the Mellanox 2410 switch on the other side of the link:

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

The output is organized into the following sections:

- Module Info: Shows the basic information about the module, according to the module EEPROM.
- Configured State: Shows the configuration information of the port as defined in the kernel.
- Operational State: Shows the high level details of the actual link status of the port in the hardware and kernel.
- Port Hardware State: Shows the low level port information from the port on the switch ASIC.

#### Module Information

The vendor name, vendor part number, identifier (Q/SFP type), and type (compliance codes) are read from the vendor EEPROM. If a compliance code override is being applied on a Broadcom platform, it is noted here. See {{<link url="#compliance-codes-ethernet-type-ethmode-type-interface-type" text="Compliance Codes, Ethernet Type, Ethmode Type, Interface type">}} above for an explanation.

```
  Module Info
      Vendor Name: Mellanox               PN: MCP2M00-A003
      Identifier: 0x03 (SFP)              Type: 25g-cr
```

#### Configured State

The configured state reflects the configuration that has been applied to the kernel via `ifupdown2` or NCLU. The `switchd` daemon translates the kernel state to the platform hardware state and keeps them in sync.

```
  Configured State
      Admin: Admin Up     Speed: 25G      MTU: 9216
      Autoneg: On                         FEC: Auto
```

#### Operational State

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

- Link Status and Speed: Normally the kernel state and hardware state should match, unless the link is in some unstable or transitory state.
- Autoneg/Autodetect: See the discussion in the {{<link url="#autonegotiation" text="Autonegotiation">}} section above for more information about the meaning of these values.
- FEC: The operational state of FEC on the link. See the discussion in the {{<link url="#fec" text="FEC">}} section above for more information about the meaning of these values.
- TX Power/RX Power: These values are read from the module DOM to indicate the optical power strength measured on the module if the module implements the feature. Sometimes both are supported, sometimes only RX, sometimes neither. This is not applicable to DAC and twisted pair interfaces.
- Topo File Neighbor: If the `/etc/ptm.d/topology.dot` file is populated, the entry matching this interface is shown.
- LLDP Neighbor: If the `lldpd` daemon is running and LLDP data is received from the neighbor, the neighbor information is shown here.

#### Port Hardware State

The port hardware state shows additional low level port information. Since different hardware vendors have different approaches to how the port information is organized, the output varies between vendors.

Here is the output on Mellanox platforms:

```
  Port Hardware State:
      Compliance Code: 100GBASE-CR4 or 25GBASE-CR CA-L
      Cable Type: Passive copper cable
      Speed: 25G                          Autodetect: Enabled
      Eyes: 79                            Grade: 5451
      Troubleshooting Info: No issue was observed.
```

Here is the output on Broadcom platforms:

```
  Port Hardware State:
      Rx Fault: None                      Carrier Detect: yes
      Rx Signal: Detect: Y                Signal Lock: Y
      Ethmode Type: 25g-cr                Interface Type: CR
      Speed: 25G                          Autoneg: Off
      MDIX: ForcedNormal, Normal          FEC: Off
      Local Advrtsd: None                 Remote Advrtsd: None
      Eyes: L: 281, R: 296, U: 118, D: 118
```

See the discussions in the {{<link url="#fec" text="FEC">}}, {{<link url="#autonegotiation" text="Autonegotiation">}} and {{<link url="#signal-integrity" text="Signal Integrity">}} sections above for more details about each value.

The Mellanox port firmware automatically troubleshoots link problems and displays items of concern in the Troubleshooting Info section of this output.

## Troubleshoot Layer 1 Problems

This section contains a troubleshooting methodology and checklist for helping you resolve layer 1 issues for modules whether or not they are on the {{<exlink url="https://cumulusnetworks.com/hcl" text="Cumulus Linux HCL">}}.

Layer 1 problems can be classified as follows:

- Link down
- Link flapping
- Errors on link (not drops - drops are a layer 2/layer 3 switching issue)
- Signal integrity issues
- MTU size mismatch
- I2C issues
- High power module issues

### Link Is Down or Flapping

A down or flapping link can exhibit any of the following symptoms:

- `ip link show <swp>` returns `<NO-CARRIER,BROADCAST,MULTICAST,UP>` when it should return something like `<BROADCAST,MULTICAST,UP,LOWER_UP>`
- `ip link show` changing every second or two indicates the link is flapping up/down
- `ethtool -S <swp>` returns HwIfInErrors
- `cl-netstat` returns RX_ERR
- No LLDP data is received, or it is flapping
- `l1-show` returns `Link Status: Kernel: Down` and `Hardware: Down` for the operational state.

The first thing you need to do is run `l1-show <swp>` on both ends of the link, if possible. The output contains all the pertinent information to help troubleshoot the link.

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

#### Troubleshoot Module Info

- Does the module vendor name and vendor PN match the module that you believe is installed? That is, are you looking at the right link? Is the right module installed?
- Does the module type match the technology that you believe the link is? For example, if you have a 100G DAC installed, do you see *Type: 100G-CR4*?  
- Do both sides agree on the technology being used?

#### Troubleshoot Configured State

- Admin: Is the link *Admin Up*?
- Speed: Is the configured speed correct?
- MTU: Does the MTU match on both sides? Note that an MTU mismatch won't prevent the link from coming up, but it does affect traffic forwarding.
- Autoneg: Does this match what is expected? See the {{<link url="#autonegotiation" text="Autonegotiation">}} section above for details.
- FEC: Is the FEC setting correct? See the {{<link url="#fec" text="FEC">}} section above for details.

#### General Troubleshooting Steps

1. Collect `l1-show <swp>` for the module on both ends of the link. If `l1-show` is not supported, then collect a cl-support on both sides with the module installed and admin up - any troubleshooting and bug filing will need some base information.
   - The files that you will be using the most: Support/ethtool.module, Support/portmap, Support/portstat, Support/port.all, Support/ethtool.fec, Support/ethtool.link
     - Identify the module with the issue in `ethtool.module`. Search the internet for the value in the *Vendor PN* field and get the vendor's data sheet.
     - Get the hardware port mapping from portmap. You must have this to find the correct lines in portstat and portmap
     - Find the hardware port entry in portstat and port.all (using portmap table)
     - Find the transceiver type that this module is claimed to be by the manufacturer (See 1.b. Google 'Vendor PN')
2. Verify correct transceiver codes in these places:
   - `ethtool -m <swp>`: The `Transceiver type` field that has the text *Ethernet* should identify the vendor's programmed type and the type of module the datasheet states. Note that 10G and 40G DACs often do not use this field.
   - Find the transceiver in the map of transceiver types to see if the next items match:
   - Check the `Interface` column in the `portstat` file. It should match the value in the `Transceiver type` field when you run `ethtool -m`.
   - `/cumulus/switchd/config/interface/<swp>/interface_mode` should match the `interface_mode` in the map table.
   - `/cumulus/switchd/config/interface/<swp>/ethtool_mode` should match the `ethtool_mode` in the map table.
   - if not correct, try an override in `/etc/cumulus/portwd.conf`.  For now, search Zendesk on how.  TODO:  quick guide to an override file
3. Verify RX and TX: Note that `l1-show` provides all this information:

        `ethtool -m <swp>`  DOM output good (if supported, only applies to optical modules not copper). This tells if the module thinks it is RX/TX

        SFP:
                Optical diagnostics support               : Yes
                Laser bias current                        : 17.122 mA
                Laser output power                        : 0.2205 mW / -6.57 dBm  <-- TX is good for 1G Base-SX
                Receiver signal average optical power     : 0.2193 mW / -6.59 dBm  <-- RX is in similar range of TX

        QSFP:
                Alarm/warning flags implemented           : Yes
                Laser tx bias current (Channel 1)         : 7.680 mA
                Laser tx bias current (Channel 2)         : 7.808 mA
                Laser tx bias current (Channel 3)         : 7.680 mA
                Laser tx bias current (Channel 4)         : 7.744 mA
                Transmit avg optical power (Channel 1)    : 0.7671 mW / -1.15 dBm  <-- is around 0.1 to 1.0 mW depending on optic type
                Transmit avg optical power (Channel 2)    : 0.8118 mW / -0.91 dBm
                Transmit avg optical power (Channel 3)    : 0.7866 mW / -1.04 dBm
                Transmit avg optical power (Channel 4)    : 0.8269 mW / -0.83 dBm
                Rcvr signal avg optical power(Channel 1)  : 0.0001 mW / -40.00 dBm  <-- This means no light is RX'd. Bad
                Rcvr signal avg optical power(Channel 2)  : 0.0001 mW / -40.00 dBm  <--
                Rcvr signal avg optical power(Channel 3)  : 0.0001 mW / -40.00 dBm  <--
                Rcvr signal avg optical power(Channel 4)  : 0.0001 mW / -40.00 dBm  <--  

        - Hardware link up: l1-show:  Operational State: Link Status: Hardware   This is the Broadcom or Mellanox ASIC status of the link:  If down, then the link is down at the ASIC level 
        - Signal Detected Information:  l1-show: Port Hardware State section.:  This will show signal status, Lock status and Fault Status (See Note 1 below) as well as Eye info or Link Grade info if the link is up.
        - `ethtool <swp>`:  Link detected: yes. This should be properly synced from the ASIC status.  If it is mismatched, then it is likely a bug.
4. Verify there are no basic setting mismatches (speed, duplex, autoneg). Check both sides and ensure they match.
   - Check the settings in `/etc/network/interfaces`.
   - Check speed/duplex and autoneg columns under Operational State in the `l1-show` output. The values should match on both sides.
   - Check the speed, duplex and autonegotiation values in `ethtool <swp>` (Support/ethtool.link). This is less reliable, since you can enable autoneg on links that don't support it and the ASIC should do the right thing. See {{<link url="Switch-Port-Attributes/#interface-configuration-recommendations-for-broadcom-platforms" text="Interface Recommendations">}} for more information.
5. Check FEC settings are correct and match on both sides for 100G and 25G: `ethtool --show-fec` (Support/ethtool.fec)   See: What the FEC? and the {{<link url="Switch-Port-Attributes/#fec" text="FEC">}} section of the Switch Port Attributes topic.
6. Loopback tests: Move the modules and connect dut1-dut1 and dut2-dut2. See if one switch works, then perform steps 1-4 on each side. If it works one way, try to isolate the issue to one module/port/platform/configuration.
7. Try a different module of the same type; the current module could be bad.
8. Try a different module of different type - preferably one that is supported on the {{<exlink url="https://cumulusnetworks.com/hcl" text="Cumulus Linux HCL">}}.

### Fault(Local) and Fault(Remote) Errors

Fault(Remote) applies to 10G speeds and above. It means the local module sees a signal from the remote module, but the remote module doesn't report any signal from the local module. This could be due to one or more of the following issues:

- The local device isn't transmitting.
- The remote is broken on the RX side.
- The fiber/copper path to the remote is broken.

Fault(Local) indicates that the local module does not see any signal from the remote. Again, this applies to 10G and above speeds only. This could be due to one or more of the following issues:

- The remote device isn't transmitting.
- The local device is broken on the RX side.
- The fiber/copper path from the remote is broken.

For optical modules:

- If the local or remote device isn't transmitting, and the modules support DOM, you can try to eliminate the issue by checking the transmit power levels on the local device in the output from `ethtool -m`. If it is 'zero' or 0.0001 then the module may be disabled, or doesn't have the correct power settings enabled
- If either device is broken on the RX side, and the module supports DOM, you can check the receive power levels on the remote in the output from `ethtool -m`.
- If the path to or from the remote is broken, try different cables to find which cable/connector is bad. If changing the cable doesn't work, then swap the modules one at a time.

For copper DACs, since they don't support DOM, you can try different cables.

### I2C Problems

When modules disappear or you see `smbus` or `i2c` errors in the log, sometimes a module or group of modules is wrecking the I2C bus, which is the bus where Cumulus Linux communicates with module EEPROMs as well as with fans and temperature sensors.

This requires a bit of detective work, and worst case a binary search of removing half the cables at a time until you find the right cable. The bad cable may wreck communications with another working cable on the bus. You should contact the NVIDIA Networking Global Support Services team for help.

### Module High Power Problems

Some modules require higher power signals and bits to be set for them to be enabled. One symptom of this may be 0.0001mw transmit power, when power is expected.

This takes some platform and EEPROM detective work, and usually is seen once on newer platforms before it is fixed. You should contact the NVIDIA Networking Global Support Services team for help.

For example, here is the `l1-show` output for an AOC (on swp6) with failed RX on lane 3:

```
  Port:  swp6
  Module Info
      Vendor Name: XXXXX                  PN: AOC-XXXX
      Identifier: 0x0d (QSFP+)            Type: 40g-sr4
  Configured State
      Admin: Admin Up     Speed: 40G      MTU: 9216
      Autoneg: Off                        FEC: Off
  Operational State
      Link Status: Kernel: Down           Hardware: Down
      Speed: Kernel: 40G                  Hardware: 40G
      Autoneg: Off                        FEC: None (down)
      TX Power (mW): [1.1645, 1.171, 1.1155, 1.0945]
      RX Power (mW): [0.159, 0.1732, 0.153, 0.0067]  <- Low power on lane 3
      Topo File Neighbor: switch_1, swp6
      LLDP Neighbor:      None, None
  Port Hardware State:
      Rx Fault: Local                     Carrier Detect: no
      Rx Signal: Detect: YYYY             Signal Lock: YYYN  <- No signal lock on lane 3
      Ethmode Type: 40g-sr4               Interface Type: SR4
      Speed: 40G                          Autoneg: Off
      MDIX: ForcedNormal, Normal          FEC: Off
      Local Advrtsd: None                 Remote Advrtsd: None
      Eyes: L: 357, R: 326, U: 211, D: 219, L: 328, R: 312, U: 206, D: 211,
            L: 359, R: 343, U: 211, D: 200, L: 0, R: 0, U: 0, D: 0 <- No valid eye on lane 3
```

Here is the `l1-show` output for an AOC with failed lanes 0 and 1. Note that signal lock is bouncing, and sometimes shows *Y*:

```
Port:  swp8
  Module Info
      Vendor Name: XXXX                   PN: AOC-XXXX
      Identifier: 0x0d (QSFP+)            Type: 40g-sr4
  Configured State
      Admin: Admin Up     Speed: 40G      MTU: 9216
      Autoneg: Off                        FEC: Off
  Operational State
      Link Status: Kernel: Down           Hardware: Down
      Speed: Kernel: 40G                  Hardware: 40G
      Autoneg: Off                        FEC: None (down)
      TX Power (mW): [1.1762, 1.1827, 1.1272, 1.1062]
      RX Power (mW): [0.0001, 0.0001, 0.5255, 0.64]  <-- Low power on lanes 0,1
      Topo File Neighbor: switch_2, swp10
      LLDP Neighbor:      None, None
  Port Hardware State:
      Rx Fault: Local                     Carrier Detect: no
      Rx Signal: Detect: YYYY             Signal Lock: YNYY  <- No lock on lane 1 at moment of capture
      Ethmode Type: 40g-sr4               Interface Type: SR4
      Speed: 40G                          Autoneg: Off
      MDIX: ForcedNormal, Normal          FEC: Off
      Local Advrtsd: None                 Remote Advrtsd: None
      Eyes: L: 0, R: 0, U: 0, D: 0, L: 0, R: 0, U: 0, D: 0,  <-- No valid eyes on lanes 0,1
            L: 359, R: 359, U: 214, D: 226, L: 359, R: 359, U: 243, D: 264
```

---

```
cumulus@mlx-2410-53:mgmt:~$ sudo ethtool -m swp10
	Identifier                                : 0x03 (SFP)
	Extended identifier                       : 0x04 (GBIC/SFP defined by 2-wire interface ID)
	Connector                                 : 0x07 (LC)
	Transceiver codes                         : 0x10 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00
	Transceiver type                          : 10G Ethernet: 10G Base-SR
	Encoding                                  : 0x06 (64B/66B)
	BR, Nominal                               : 10300MBd
	Rate identifier                           : 0x00 (unspecified)
	Length (SMF,km)                           : 0km
	Length (SMF)                              : 0m
	Length (50um)                             : 80m
	Length (62.5um)                           : 30m
	Length (Copper)                           : 0m
	Length (OM3)                              : 300m
	Laser wavelength                          : 850nm
	Vendor name                               : FINISAR CORP.
	Vendor OUI                                : 00:90:65
	Vendor PN                                 : FTLX8574D3BCL
	Vendor rev                                : A
	Option values                             : 0x00 0x1a
	Option                                    : RX_LOS implemented
	Option                                    : TX_FAULT implemented
	Option                                    : TX_DISABLE implemented
	BR margin, max                            : 0%
	BR margin, min                            : 0%
	Vendor SN                                 : UWK0UTZ
	Date code                                 : 161217
	Optical diagnostics support               : Yes
	Laser bias current                        : 8.546 mA
	Laser output power                        : 0.5268 mW / -2.78 dBm
	Receiver signal average optical power     : 0.5426 mW / -2.66 dBm
	Module temperature                        : 28.77 degrees C / 83.79 degrees F
	Module voltage                            : 3.3050 V
	Alarm/warning flags implemented           : Yes
	Laser bias current high alarm             : Off
	Laser bias current low alarm              : Off
	Laser bias current high warning           : Off
	Laser bias current low warning            : Off
	Laser output power high alarm             : Off
	Laser output power low alarm              : Off
	Laser output power high warning           : Off
	Laser output power low warning            : Off
	Module temperature high alarm             : Off
	Module temperature low alarm              : Off
	Module temperature high warning           : Off
	Module temperature low warning            : Off
	Module voltage high alarm                 : Off
	Module voltage low alarm                  : Off
	Module voltage high warning               : Off
	Module voltage low warning                : Off
	Laser rx power high alarm                 : Off
	Laser rx power low alarm                  : Off
	Laser rx power high warning               : Off
	Laser rx power low warning                : Off
	Laser bias current high alarm threshold   : 13.000 mA
	Laser bias current low alarm threshold    : 4.000 mA
	Laser bias current high warning threshold : 12.500 mA
	Laser bias current low warning threshold  : 5.000 mA
	Laser output power high alarm threshold   : 1.0000 mW / 0.00 dBm
	Laser output power low alarm threshold    : 0.2512 mW / -6.00 dBm
	Laser output power high warning threshold : 0.7943 mW / -1.00 dBm
	Laser output power low warning threshold  : 0.3162 mW / -5.00 dBm
	Module temperature high alarm threshold   : 78.00 degrees C / 172.40 degrees F
	Module temperature low alarm threshold    : -13.00 degrees C / 8.60 degrees F
	Module temperature high warning threshold : 73.00 degrees C / 163.40 degrees F
	Module temperature low warning threshold  : -8.00 degrees C / 17.60 degrees F
	Module voltage high alarm threshold       : 3.7000 V
	Module voltage low alarm threshold        : 2.9000 V
	Module voltage high warning threshold     : 3.6000 V
	Module voltage low warning threshold      : 3.0000 V
	Laser rx power high alarm threshold       : 1.0000 mW / 0.00 dBm
	Laser rx power low alarm threshold        : 0.0100 mW / -20.00 dBm
	Laser rx power high warning threshold     : 0.7943 mW / -1.00 dBm
	Laser rx power low warning threshold      : 0.0158 mW / -18.01 dBm
cumulus@mlx-2410-53:mgmt:~$
```

