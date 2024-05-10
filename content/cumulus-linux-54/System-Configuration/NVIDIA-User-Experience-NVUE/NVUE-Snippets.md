---
title: NVUE Snippets
author: NVIDIA
weight: 123
toc: 3
---
NVUE supports both traditional snippets and flexible snippets:
- Use traditional snippets to add configuration to the `/etc/network/interfaces`, `/etc/frr/frr.conf`, `/etc/frr/daemons`, `/etc/cumulus/switchd.conf`, `/etc/cumulus/datapath/traffic.conf` or `/etc/ssh/sshd_config` files.
- Use flexible snippets to manage any other text file on the system.

Cumulus Linux stores all snippets in the `/system/config/snippet` directory.

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

## Traditional Snippets

Use traditional snippets if you configure Cumulus Linux with NVUE commands, then want to configure a feature that does not yet support the NVUE Object Model. You create a snippet in `yaml` format, then add the configuration to the file with the `nv config patch` command.

{{%notice note%}}
The `nv config patch` command requires you to use the fully qualified path name to the snippet `.yaml` file; for example you cannot use `./` with the `nv config patch` command.
{{%/notice%}}
<!-- vale off -->
### /etc/frr/frr.conf Snippets
<!-- vale on -->

#### Example 1: Top Level Configuration

NVUE does not support configuring BGP to peer across the default route. The following example configures BGP to peer across the default route from the default VRF:

1. Create a `.yaml` file with the following traditional snippet:

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
   !---- CUE snippets ----
   ip nht resolve-via-default
   ```

#### Example 2: Nested Configuration

NVUE does not support configuring EVPN route targets using auto derived values from RFC 8365. The following example configures BGP to enable RFC 8365 derived router targets:

1. Create a `.yaml` file with the following traditional snippet:

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
   !---- CUE snippets ----
   router bgp 65517 vrf default
   address-family l2vpn evpn
   autort rfc8365-compatible
   ```

The traditional snippets for FRR write content to the `/etc/frr/frr.conf` file. When you apply the configuration and snippet with the `nv config apply` command, the FRR service goes through and reads in the `/etc/frr/frr.conf` file.

#### Example 3: EVPN Multihoming FRR Debugging

NVUE does not support configuring FRR debugging for EVPN multihoming. The following example configures FRR debugging:

1. Create a `.yaml` file and add the following traditional snippet:

   ```
   cumulus@switch:~$ sudo nano mh_debug_snippet.yaml
   - set:
       system:
         config:
           snippet:
             frr.conf: |
               debug bgp evpn mh es
               debug bgp evpn mh route
               debug bgp zebra
               debug zebra evpn mh es
               debug zebra evpn mh mac
               debug zebra evpn mh neigh
               debug zebra evpn mh nh
               debug zebra vxlan
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch mh_debug_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists in the `/etc/frr/frr.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/frr/frr.conf
   ...
   !---- NVUE snippets ----
   debug bgp evpn mh es
   debug bgp evpn mh route
   debug bgp zebra
   debug zebra evpn mh es
   debug zebra evpn mh mac
   debug zebra evpn mh neigh
   debug zebra evpn mh nh
   debug zebra vxlan
   ```

The traditional snippets for FRR write content to the `/etc/frr/frr.conf` file. When you apply the configuration and snippet with the `nv config apply` command, the FRR service goes through and reads in the `/etc/frr/frr.conf` file.

### /etc/network/interfaces Snippets

#### MLAG Timers Example

NVUE supports configuring only one of the {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#set-clagctl-timers" text="MLAG service timeouts">}} (initDelay). The following example configures the MLAG peer timeout to 400 seconds:

1. Create a `.yaml` file and add the following traditional snippet:

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

1. Create a `.yaml` file and add the following traditional snippet:

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
<!-- vale off -->
### /etc/cumulus/switchd.conf Snippets
<!-- vale on -->
NVUE does not provide options to configure link flap detection settings. The following example configures the link flap window to 10 seconds and the link flap threshold to 5 seconds:

1. Create a `.yaml` file and add the following traditional snippet:

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
<!--
### /etc/frr/daemons Snippets

You can create a traditional snippet to enable or disable all the FRR protocol daemons:

1. Create a `.yaml` file and add the following traditional snippet:

   ```
   cumulus@switch:~$ sudo nano frr_daemons_snippet.yaml
   - set:
       system:
         config:
           snippet:
             frr-daemons: |
               bgpd=yes
               ospfd=yes
               isisd=yes
               ospf6d=yes
               vtysh_enable=yes
               bgpd_options="   -M snmp -A 127.0.0.1"
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch frr_daemons_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the beginning of the `/etc/frr/daemons` file:

  ```
  cumulus@switch:~$ sudo cat /etc/frr/daemons
  bgpd=yes
  ospfd=yes
  ospf6d=yes
  isisd=yes
  ...
  vtysh_enable=yes
  zebra_options="  -M cumulus_mlag -M snmp -A 127.0.0.1 -s 90000000"
  bgpd_options="   -M snmp -A 127.0.0.1"
  ospfd_options="  -M snmp -A 127.0.0.1"
  ```

You can also control additional FRR protocol daemon related configuration by creating an `frr-daemons-append` snippet:

```
cumulus@switch:~$ sudo nano frr_daemons_append_snippet.yaml
- set:
    system:
      config:
        snippet:
          frr-daemons-append: |
            MAX_FDS=1024
            FRR_NO_ROOT="yes"
```
-->
### /etc/cumulus/datapath/traffic.conf Snippets

To add data path configuration for the Cumulus Linux `switchd` module that NVUE does not yet support, create a `traffic.conf` snippet.

The following example creates a file called `traffic_conf_snippet.yaml` and enables the resilient hash setting.

1. Create a `.yaml` file and add the following traditional snippet:

   ```
   cumulus@switch:~$ sudo nano traffic_conf_snippet.yaml
   - set:
       system:
         config:
           snippet:
             traffic.conf: |
               resilient_hash_enable = TRUE
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch traffic_conf_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the end of the `/etc/cumulus/datapath/traffic.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
   ...
   !---- NVUE snippets ----
   resilient_hash_enable = TRUE
   ```
<!--
### /etc/ssh/sshd_config Snippets

To add SSH daemon configuration for the Cumulus Linux SSH service that NVUE does not yet support, create a `sshd_config` snippet; for example:

1. Create a `.yaml` file and add the following traditional snippet:

   ```
   cumulus@switch:~$ sudo nano sshd_config_snippet.yaml
   - set:
       system:
         config:
           snippet:
             sshd_config: |
               PermitRootLogin yes
               X11Forwarding yes
               Match User anoncvs
                  X11Forwarding no
                  AllowTcpForwarding no
                  ForceCommand cvs server
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch sshd_config_snippet.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify that the configuration exists at the beginning of the `/etc/ssh/sshd_config` file:

   ```
   cumulus@switch:~$ sudo cat /etc/ssh/sshd_config
   ```
-->
## Flexible Snippets

Flexible snippets are an extension of traditional snippets that let you manage any text file on the system. You can add content to an existing text file or create a new text file, then add content. Cumulus Linux runs flexible snippets as root. 

Flexible snippets do *not* support:
- Binary files.
- Symbolic links.
- More than 1MB of content.
- More than one flexible snippet in the same destination file.

{{%notice warning%}}

Use caution when creating flexible snippets:
- If you configure flexible snippets incorrectly, they might impact switch functionality. For example, even though flexible snippet validation allows you to only add textual content, Cumulus Linux does not prevent you from creating a flexible snippet that adds to sensitive text files, such as `/boot/grub.cfg` and `/etc/fstab`  or add corrupt contents. Such snippets might render the box unusable or create a potential security vulnerability (the NVUE service (`nvued`) runs with superuser privileges).
- Do not add flexible snippets to configuration files that NVUE already controls, such as the `/etc/hosts`, `/etc/ntp.conf`, or `/etc/ptp4l.conf` files. Cumulus Linux does not prevent you from creating and applying a flexible snippet to these files and does not show warnings or errors. Cumulus Linux might accept the snippet content without adding it in the file. For a list of the files that NVUE manages, refer to {{<link url="NVUE-CLI/#configuration-files-that-nvue-manages" text="Configuration Files that NVUE Manages">}}.
- Do not manually update configuration files to which you add flexible snippets.

{{%/notice%}}

To create flexible snippets:

1. Create a file in `yaml` format and add each flexible snippet you want to apply in the format shown below. NVUE appends the flexible snippet at the end of an existing file. If the file does not exist, NVUE creates the file, then adds the content.

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

    - You can only set the umast permissions to a new file that you create. Adding the `permissions:` line is optional. The default umask persmissions are 644.
    - You can add a service with an action, such as `start`, `restart`, or `stop`. Adding the `services:` lines is optional; however, if you add the `service:` line, you must specify at least one service.

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch <filename>.yaml>
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

4. Verify the patched configuration.

{{%notice note%}}
The `nv config patch` command requires you to use the fully qualified path name to the snippet `.yaml` file; for example you cannot use `./` with the `nv config patch` command.
{{%/notice%}}

### Flexible Snippet Examples

The following example flexible snippet called `crontab-flex-snippet` appends the single line `@daily /opt/utils/run-backup.sh` to the existing `/etc/crontab` file, then restarts the `cron` service.

```
cumulus@leaf01:mgmt:~$ sudo nano crontab-flex-snippet.yaml
- set:
    system:
      config:
        snippet:
          crontab-flex-snippet:
            file: "/etc/crontab"
            content: |
              @daily /opt/utils/run-backup.sh
            services:
              schedule:
                service: cron
                action: restart
```

The following example flexible snippet called `apt-flex-snippet` creates a new file `/etc/apt/sources.list.d/microsoft-prod.list` with 0644 permissions and adds multi-line text:

```
- set:
    system:
      config:
        snippet:
          apt-flexible-snippet:
            file: "/etc/apt/sources.list.d/microsoft-prod.list"
            content: |
              # Adding Microsoft SQL Server Sources
              deb [arch=amd64] https://packages.microsoft.com/debian/10/prod buster main
            permissions: "0644"
```

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
