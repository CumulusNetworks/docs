---
title: Network Switch Port LED and Status LED Guidelines
author: Cumulus Networks
weight: 415
aliases:
 - /display/DOCS/Network+Switch+Port+LED+and+Status+LED+Guidelines
 - /pages/viewpage.action?pageId=8366316
product: Cumulus Linux
version: '4.0'
---
Data centers today have a large number of network switches manufactured by different hardware vendors running network operating systems (NOS) from different providers. This chapter provides a set of guidelines for how network port and status LEDs should appear on the front panel of a network switch. This provides a network operator with a standard way to identify the state of a switch and its ports by looking at its front panel, irrespective of the hardware vendor or NOS.

## Network Port LEDs

A network port LED indicates the state of the link, such as link UP or Tx/Rx activity. Here are the requirements for these LEDs:

- **Number of LEDs per port** — Ports that cannot be split; for example, 1G ports must have 1 LED per port. Ports that can be split should have 1 LED per split port. So a 40G port that can be split into 4 10G ports has 4 LEDs, one per split port.
- **Location** — A port LED should be placed right above the port. This prevents the LEDs from being hidden by drooping cables. If the port can be split, the LED for each split port should also be placed above the port. The LEDs should be evenly spaced and be inside the edges of the ports to prevent confusion.
- **Port Number Label** — The port number must be printed in white on the switch front panel directly under the corresponding LED.
- **Colors** — As network port technology improves with smaller ports and higher speeds, having different colors for different types of ports or speeds is confusing. The focus should be on giving a network operator a simple set of indications that provide the operator with basic information about the port. Hence, green and amber colors must be used on the LED to differentiate between good and bad states. These colors are commonly found on network port LEDs and should be easy to implement on future switches.
- **Signaling** — The table below indicates the information that can be conveyed via port LEDs and how it should be done.
    - **Max Speed** indicates the maximum speed at which the port can be run. For a 10G port, if the port speed is 10G, then it is running at its maximum speed. If the 10G port is running at 1G speed then its running at a *lower speed*.
    - **Physical Link Up/Down** displays layer 2 link status.
    - **Beaconing** provides a way for a network operator to identify a particular link. The administrator can *beacon* that port from a remote location so the network operator has visual indication for that port.
    - **Fault** can also be considered a form of beaconing or vice versa. Both try to draw attention of the network operator towards the port, thus they are signaled the same way.
    - **Blinking amber** implies a blink rate of 33ms. *Slow blinking amber* indicates a blink rate of 500ms, with a 50% on/off duty cycle. In other words, a slow blinking amber LED is amber for 500 ms and then off for 500ms.

    | Activity            | Max Speed indication | Lower Speed Indication |
    | ------------------- | -------------------- | ---------------------- |
    | Physical Link Down  | Off                  | Off                    |
    | Physical Link UP    | Solid Green          | Solid Amber            |
    | Link Tx/Rx Activity | Blinking Green       | Blinking Amber         |
    | Beaconing           | Slow Blinking Amber  | Slow Blinking Amber    |
    | Fault               | Slow Blinking Amber  | Slow Blinking Amber    |

## Status LEDs

A set of status LEDs are typically located on one side of a network switch. The status LEDs provide a visual indication on what is physically wrong with the network switch. Typical LEDs on the front panel are for PSUs (power supply units), fans and system. Locator LEDs are also found on the front panel of a switch. Each component that has an LED is known as a *unit* below.

- **Number of LEDs per unit** — Each unit should have only 1 LED.
- **Location** — All units should have their LEDs on the right-hand side of the switch after the physical ports.
- **Unit label** — The label should be printed on the front panel directly above the LED.
- **Colors** — The focus should be on giving a network operator a simple set of indications that provide basic information about the unit. The following section has more information about the indications, but colors are standardized on green and amber. These colors are universally found on all status LEDs and should be easy to implement on future switches.
- **Defined LED** — Every network switch must have LEDs for the following:
      - PSU
      - Fans
      - System LED
      - Locator LED
- **PSU LEDs** — Each PSU must have its own LED. PSU faults are difficult to debug. If a network operator knows which PSU is faulty, he or she can quickly check if it is powered up correctly and, if that fault persists, replace the PSU.

    | Unit Activity                       | Indication          |
    | ----------------------------------- | ------------------- |
    | Installed and power OK              | Solid Green         |
    | Installed, but no power             | Slow Blinking Amber |
    | Installed, powered, but has faults. | Slow Blinking Amber |

- **Fan LED** — A network switch may have multiple fan trays (3 - 6). It is difficult to put an LED for each fan tray on the front panel, given the limited real estate. Hence, the recommendation is one LED for all fans.

    | Unit Activity                 | Indication          |
    | ----------------------------- | ------------------- |
    | All fans running OK           | Solid Green         |
    | Fault on any one of the fans. | Slow Blinking Amber |

- **System LED** — A network switch must have a system LED that indicates the general state of a switch. This state could be of hardware, software, or both. It is up to the individual switch NOS to decide what this LED indicates. But the LED can have only the following indications:

    | Unit Activity | Indication          |
    | ------------- | ------------------- |
    | All OK        | Solid Green         |
    | Not OK        | Slow Blinking Amber |

- **Locator LED** — The locator LED helps locate a particular switch in a data center full of switches. Thus, it should have a different color and predefined location. It must be located at the top right corner on the front panel of the switch and its color must be blue.

    | Unit Activity   | Indication    |
    | --------------- | ------------- |
    | Locate enabled  | Blinking Blue |
    | Locate disabled | Off           |

## Locate a Switch

Cumulus Linux supports the locator LED functionality for identifying a switch, by blinking a single LED on a specified network port, on the following switches:

- Celestica Seastone
- Dell Z9100-ON
- Edgecore AS7712-32X
- Penguin Arctica 3200C
- Quanta QuantaMesh BMS T4048-IX2
- Supermicro SSE-C3632S

To use the locator LED functionality, run:

```
cumulus@switch:~$ ethtool -p --identify PORT_NAME TIME
```

In the example above, `INTERFACE_NAME` should be replaced with the name of the port, and `TIME` should be replaced with the length of time, in seconds, that the port LED should blink.

{{%notice note%}}

This functionality is only supported on swp\* ports, not eth\* management interfaces.

{{%/notice%}}

## Caveats and Errata

### Dell-N3048EP-ON LED Colors at Low Speeds

Across all 48 ports on a Dell-N3048EP-ON switch, if the link speed of a device is 10Mbps, the link light does not come on and only the activity light is seen. Traffic does work properly at this speed.

{{%notice note%}}

Cumulus Linux does not support 10M speeds.

{{%/notice%}}

If you set the ports to 100M, the link lights for ports 1-46 are orange, while the lights for ports 47 and 48 are green.

When all of the ports are set to 1G, all the link lights are green.

### EdgeCore Minipack-AS8000 Port LED Blink State

The port LED blink state that indicates link activity is not implemented; the ports only have ON/OFF states.
