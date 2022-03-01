---
title: NVUE Snippets
author: NVIDIA
weight: 123
toc: 3
---
NVUE supports both snippets and flexible snippets:
- Use snippets to add configuration to either the `/etc/frr/frr.conf` or `/etc/network/interfaces` file.
- Use flexible snippets to manage any other text file on the system.

## Snippets

Use snippets if you configure Cumulus Linux with NVUE commands, then want to configure a feature that does not yet support the NVUE Object Model. You create a snippet in `yaml` format and add the configuration to either the `/etc/frr/frr.conf` or `/etc/network/interfaces` file.
<!-- vale off -->
### /etc/frr/frr.conf Snippets
<!-- vale on -->
NVUE does not support configuring BGP to peer across the default route. The following example configures BGP to peer across the default route from the default VRF:

1. Create a `.yaml` file with the following snippet:

   ```
   cumulus@switch:~$ sudo nano ./bgp_snippet.yaml
   - set:
       system:
         config:
           snippet:
             frr.conf: |
               ip nht resolve-via-default
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch ./bgp_snippet.yaml
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

### /etc/network/interfaces Snippets

#### Configure MLAG Timers

NVUE supports configuring only one of the {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#set-clagctl-timers" text="MLAG service timeouts">}} (initDelay). The following example configures the MLAG peer timeout to 400 seconds:

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano ./mlag_snippet.yaml
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
   cumulus@switch:~$ nv config patch ./mlag_snippet.yaml
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

#### Configure a Traditional Bridge

NVUE does not support configuring traditional bridges. The following example configures a traditional bridge called `br0` with the IP address 11.0.0.10/24. swp1, swp2 are members of the bridge.

1. Create a `.yaml` file and add the following snippet:

   ```
   cumulus@switch:~$ sudo nano ./bridge_snippet.yaml
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
   cumulus@switch:~$ nv config patch ./bridge_snippet.yaml
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
   - set:
       system:
        config:
          snippet:
            <snippet-name>:
              file: "<filename>"
              permissions: "<umask-permissions>"
              content: |
                # This is my content 
   ```

    You can only set the umast permissions to a new file that you create. Adding the `permissions:` line is optional. The default umask persmissions are 644.

   The following example creates two snippets called `mysnippet1` and `mysnippet2` in a file called `./flexible-snippets.yaml`.
   - `mysnippet1` creates the `/etc/file1` file, changes the umask permissions to 0600, and adds the content `# This is my content`.
   - `mysnippet2` adds `# This is my content` to the `/etc/file2` file that exists on the system.

   ```
   cumulus@switch:~$ sudo nano ./flexible-snippets.yaml
   - set:
       system:
        config:
          snippet:
            mysnippet1:
              file: "/etc/file1"
              permissions: "0600"
              content: |
                # This is my content 
            mysnippet2:
              file: "/etc/file2"
              content: |
                # This is my content        
   ```

2. Run the following command to patch the configuration:

   ```
   cumulus@switch:~$ nv config patch ./flexible-snippets.yaml
   ```

3. Run the `nv config apply` command to apply the configuration:

   ```
   cumulus@switch:~$ nv config apply
   ```

NVUE appends the flexible snippet at the end of an existing file. If the file does not exist, NVUE creates the file and adds the content.
