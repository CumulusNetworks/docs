---
title: Network Switch Port LED and Status LED Guidelines
author: NVIDIA
weight: 1030
toc: 4
---
Data centers today have a large number of network switches manufactured by different hardware vendors running network operating systems from different providers. This section provides a set of guidelines for how network port and status LEDs appear on the front panel of a network switch. This provides you with a standard way to identify the state of a switch and its ports by looking at its front panel, irrespective of the hardware vendor or NOS.

## Network Port LEDs

A network port LED indicates the state of the link, such as link UP or Tx/Rx activity. Here are the requirements for these LEDs:

- **Number of LEDs per port** - Ports that cannot be split; for example, 1G ports must have 1 LED per port. Ports that can be split have 1 LED per split port. For example, a 40G port that you can split into 4 10G ports has 4 LEDs, one per split port.
- **Location** - A port LED must be placed right above the port. This prevents the LEDs from being hidden by drooping cables. If the port can be split, the LED for each split port must also be placed above the port. The LEDs must be evenly spaced and be inside the edges of the ports to prevent confusion.
- **Port Number Label** - The port number must be printed in white on the switch front panel directly under the corresponding LED.
- **Colors** - As network port technology improves with smaller ports and higher speeds, having different colors for different types of ports or speeds is confusing. Focus on providing a simple set of indications that show basic information about the port. Green and amber colors must be used on the LED to differentiate between good and bad states. These colors are commonly found on network port LEDs and are easy to implement on future switches.
- **Signaling** - The table below shows the information you can convey with port LEDs.
    - **Max Speed** indicates the maximum speed at which the port can be run. For a 10G port, if the port speed is 10G, then it is running at its maximum speed. If the 10G port is running at 1G speed, then it is running at a *lower speed*.
    - **Physical Link Up/Down** displays layer 2 link status.
    <!-- vale off -->
    - **Beaconing** provides a way for you to identify a particular link. You can *beacon* that port from a remote location so the network operator has visual indication for that port.
    <!-- vale on -->
    - **Fault** can also be considered a form of beaconing. Both try to draw attention towards the port.
    - **Blinking amber** implies a blink rate of 33ms. *Slow blinking amber* indicates a blink rate of 500ms, with a 50% on and off duty cycle. For example, a slow blinking amber LED is amber for 500 ms and then off for 500ms.
<!-- vale off -->
    | Activity            | Max Speed indication | Lower Speed Indication |
    | ------------------- | -------------------- | ---------------------- |
    | Physical Link Down  | Off                  | Off                    |
    | Physical Link UP    | Solid Green          | Solid Amber            |
    | Link Tx/Rx Activity | Blinking Green       | Blinking Amber         |
    | Beaconing          | Slow Blinking Amber  | Slow Blinking Amber    |
    | Fault               | Slow Blinking Amber  | Slow Blinking Amber    |
<!-- vale on -->
## Status LEDs

A set of status LEDs are typically located on one side of a network switch. The status LEDs provide a visual indication on what is physically wrong with the network switch. Typical LEDs on the front panel are for PSUs (power supply units), fans, and system. Locator LEDs are also found on the front panel of a switch. Each component that has an LED is known as a *unit* below.

- **Number of LEDs per unit** - Each unit must have only 1 LED.
- **Location** - All units must have their LEDs on the right-hand side of the switch after the physical ports.
- **Unit label** - The label must be printed on the front panel directly above the LED.
- **Colors** - Provide a simple set of indications that show basic information about the unit. The following section has more information about the indications, but colors are standardized on green and amber. These colors are universally found on all status LEDs.
- **Defined LED** - Every network switch must have LEDs for the following:

  - PSU
  - Fans
  - System LED
  - Locator LED

- **PSU LEDs** - Each PSU must have its own LED. PSU faults are difficult to debug. If you know which PSU is faulty, you can quickly check if it is powered up correctly and, if that fault persists, replace the PSU.

    | Unit Activity                       | Indication          |
    | ----------------------------------- | ------------------- |
    | Installed and power OK              | Solid Green         |
    | Installed, but no power             | Slow Blinking Amber |
    | Installed, powered, but has faults. | Slow Blinking Amber |

- **Fan LED** - A network switch might have multiple fan trays (3 through 6). It is difficult to put an LED for each fan tray on the front panel given the limited real estate. The recommendation is one LED for all fans.

    | Unit Activity                 | Indication          |
    | ----------------------------- | ------------------- |
    | All fans running OK           | Solid Green         |
    | Fault on any one of the fans. | Slow Blinking Amber |

- **System LED** - A network switch must have a system LED that indicates the general state of a switch. This state can be of hardware, software, or both. It is up to the individual switch NOS to decide what this LED indicates. However, the LED can have only the following indications:

    | Unit Activity | Indication          |
    | ------------- | ------------------- |
    | All OK        | Solid Green         |
    | Not OK        | Slow Blinking Amber |

- **Locator LED** - The locator LED helps locate a particular switch in a data center full of switches. The LED must have a different color and predefined location. It must be located at the top right corner on the front panel of the switch and its color must be blue.

    | Unit Activity   | Indication    |
    | --------------- | ------------- |
    | Locate enabled  | Blinking Blue |
    | Locate disabled | Off           |
