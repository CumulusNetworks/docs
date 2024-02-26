---
title: NVUE Snippets
author: NVIDIA
weight: 123
toc: 3
---
NVUE supports both snippets and flexible snippets:
- Use snippets to add configuration to the `/etc/frr/frr.conf`, `/etc/network/interfaces`, or `/etc/cumulus/switchd.conf` file.
- Use flexible snippets to manage any other text file on the system.

{{%notice note%}}
- A snippet configures a single parameter associated with a specific configuration file.
- You can only set or unset a snippet; you cannot modify, partially update, or change a snippet.
- Setting the snippet value replaces any existing snippet value.
- Cumulus Linux supports only one snippet for a configuration file.
- Only certain configuration files support a snippet.
- NVUE does not parse or validate the snippet content and does not validate the resulting file after you apply the snippet.
- PATCH is only the method of applying snippets and does not refer to any snippet capabilities.
- As NVUE supports more features and introduces new syntax, snippets and flexible snippets become invalid. **Before** you upgrade Cumulus Linux to a new release, review the {{<link url="Whats-New" text="What's New">}} for new NVUE syntax and remove the snippet if NVUE introduces new syntax for the feature that the snippet configures.
{{%/notice%}}

## Snippets

Use snippets if you configure Cumulus Linux with NVUE commands, then want to configure a feature that does not yet support the NVUE Object Model. You create a snippet in `yaml` format, then add the configuration to the `/etc/frr/frr.conf`, `/etc/network/interfaces`, or `/etc/cumulus/switchd.conf` file with the `nv config patch` command.

{{%notice note%}}
The `nv config patch` command requires you to use the fully qualified path name to the snippet `.yaml` file; for example you cannot use `./` with the `nv config patch` command.
{{%/notice%}}
<!-- vale off -->
### /etc/frr/frr.conf Snippets
<!-- vale on -->

#### Example 1: Top Level Configuration

NVUE does not support configuring BGP to peer across the default route. The following example configures BGP to peer across the default route from the default VRF:

1. Create a `.yaml` file with the following snippet:

   ```
   cumulus@switch:~$ sudo nano bgp_snippet.yaml
   - set:
       system:
         config:
           snippet:
             frr.conf: |
               ip nht resolve-via-default
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch bgp_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/frr/frr.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/frr/frr.conf
   ...
   ! end of router ospf block
   !---- NVUE snippets ----
   ip nht resolve-via-default
   ```

#### Example 2: Nested Configuration

NVUE does not support configuring EVPN route targets using auto derived values from RFC 8365. The following example configures BGP to enable RFC 8365 derived router targets:

1. Create a `.yaml` file with the following snippet:

   ```
   cumulus@switch:~$ sudo nano bgp_snippet.yaml
   - set:
       system:
         config:
           snippet:
             frr.conf: |
               router bgp 65517 vrf default
                 address-family l2vpn evpn
                   autort rfc8365-compatible
   ```

Make sure to use spaces not tabs; the parser expects spaces in yaml format.

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch bgp_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/frr/frr.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/frr/frr.conf
   ...
   ! end of router bgp 65517 vrf default
   !---- NVUE snippets ----
   router bgp 65517 vrf default
   address-family l2vpn evpn
   autort rfc8365-compatible
   ```

The snippets for FRR write content to the `/etc/frr/frr.conf` file. When you apply the configuration and snippet with the `nv config apply` command, the FRR service goes through and reads in the `/etc/frr/frr.conf` file.

### /etc/network/interfaces Snippets

#### MLAG Timers Example

NVUE supports configuring only one of the {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#set-clagctl-timers" text="MLAG service timeouts">}} (initDelay). The following example configures the MLAG peer timeout to 400 seconds:

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano mlag_snippet.yaml
   - set:
       system:
         config:
           snippet:
             ifupdown2_eni:
               peerlink.4094: |
                 clagd-args --peerTimeout 400
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch mlag_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists in the peerlink.4094 stanza of the `/etc/network/interfaces` file:

   ```
   cumulus@switch:~$ sudo cat /etc/network/interfaces
   ...
   auto peerlink.4094
   iface peerlink.4094
    clagd-args --peerTimeout 400
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
   ...
   ```

#### Traditional Bridge Example

NVUE does not support configuring traditional bridges. The following example configures a traditional bridge called `br0` with the IP address 11.0.0.10/24. swp1, swp2 are members of the bridge.

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano bridge_snippet.yaml
   - set:
       system:
        config:
          snippet:
            ifupdown2_eni:
              eni_stanzas: |
                auto br0
                iface br0
                  address 11.0.0.10/24
                  bridge-ports swp1 swp2
                  bridge-vlan-aware no
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch bridge_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/network/interfaces` file:

   ```
   cumulus@switch:~$ sudo cat /etc/network/interfaces
   ...
   auto br0
   iface br0
     address 11.0.0.10/24
     bridge-ports swp1 swp2
     bridge-vlan-aware no
   ```

### /etc/cumulus/switchd.conf Snippets

NVUE does not provide options to configure link flap detection settings. The following example configures the link flap window to 10 seconds and the link flap threshold to 5 seconds:

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano switchd_snippet.yaml
   - set:
       system:
         config:
           snippet:
             switchd.conf: |
               link_flap_window = 10
               link_flap_threshold = 5
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch switchd_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/cumulus/switchd.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/cumulus/switchd.conf
   !---- NVUE snippets ----
   link_flap_window = 10
   link_flap_threshold = 5
   ```

## Flexible Snippets

Flexible snippets are an extension of regular snippets that let you manage any text file on the system. You can add content to an existing text file or create a new text file and add content.

Flexible snippets do *not* support:
- Binary files.
- Symbolic links.
- More than 1MB of content.
- More than one flexible snippet in the same destination file.

{{%notice warning%}}
Cumulus Linux runs flexible snippets as root. Exercise caution when creating and editing flexible snippets.
{{%/notice%}}

To create flexible snippets:

1. Create a file in `yaml` format and add each flexible snippet you want to apply in the format shown below.

   ```
   cumulus@leaf01:mgmt:~$ sudo nano <filename>.yaml>
   - set:
       system:
        config:
          snippet:
            <snippet-name>:
              file: "<filename>"
              permissions: "<umask-permissions>"
              content: |
                # This is my content
              services:
                 <name>:
                   service: <service-name>
                   action: <action>
   ```

    NVUE appends the flexible snippet at the end of an existing file. If the file does not exist, NVUE creates the file and adds the content.

    - You can only set the umast permissions to a new file that you create. Adding the `permissions:` line is optional. The default umask persmissions are 644.
    - You can add a service with an action, such as start, restart, or stop. Adding the `services:` lines is optional.

## Remove a Snippet

To remove a traditional or flexible snippet, edit the snippet's `.yaml` file to change `set` to `unset`, then patch and apply the configuration. Alternatively, you can use the REST API DELETE and PATCH methods.

The following example removes the {{<link url="#etcnetworkinterfaces-snippets" text="MLAG timer traditional snippet">}} created above to configure the MLAG peer timeout:

1. Edit the `mlag_snippet.yaml` file to change `set` to `unset`:

   ```
   cumulus@switch:~$ sudo nano mlag_snippet.yaml
   - unset:
       system:
         config:
           snippet:
             ifupdown2_eni:
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch mlag_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the peer timeout parameter no longer exists in the `peerlink.4094` stanza of the `/etc/network/interfaces` file:

   ```
   cumulus@switch:~$ sudo cat /etc/network/interfaces
   ...
   auto peerlink.4094
   iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 180
   ...
   ```
