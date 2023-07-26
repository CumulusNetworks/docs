---
title: Gathering Ansible Facts on Cumulus Linux
author: NVIDIA
weight: 322
toc: 4
---

This article outlines the process for using {{<exlink url="http://www.ansible.com/home" text="Ansible">}} in a lab environment to gather information (which Ansible calls facts) about a Cumulus Linux switch, where Ansible runs on a physical server or in a virtual machine on the same network as the switch.

## Requirements

- A Cumulus Linux switch
- A host running Ansible
- {{<link url="Set-up-a-Basic-Ansible-Lab" text="Set up a basic Ansible lab">}}, or have an understanding of and past experience with Ansible

## How to Gather Facts from the CLI

1. Make sure the hostname is in DNS. Ping the DNS hostname of the Cumulus Linux switch:

        user at server in ~
        $ ping sw1
        PING sw1 (192.168.100.11) 56(84) bytes of data.
        64 bytes from sw1 (192.168.100.11): icmp_req=1 ttl=64 time=0.197 ms
        64 bytes from sw1 (192.168.100.11): icmp_req=2 ttl=64 time=0.163 ms
        ^C
        --- sw1 ping statistics ---
        2 packets transmitted, 2 received, 0% packet loss, time 1000ms
        rtt min/avg/max/mdev = 0.163/0.180/0.197/0.017 ms
        user at server in ~
        $

2. Use the {{<exlink url="https://docs.ansible.com/ansible/latest/collections/ansible/builtin/setup_module.html" text="Ansible setup command">}}, where sw1 is the DNS name of your switch1, where `-m` means which module you are selecting to run, `--ask-pass` prompts you for the password (most automation environments {{<exlink url="https://wiki.archlinux.org/index.php/SSH_Keys#Simple_method" text="utilize SSH keys for authentication">}} instead of passwords), `-vvvv` gives you all the debugs (it is not needed but does help you troubleshoot) and `-u root` makes the user root instead of your username to the host device running Ansible.

        ansible sw1 -m setup --ask-pass -vvvv -u root

3. Ansible connects to the switch utilizing the provided user (in this case, root) and the provided password. This should be the exact same way a user would connect to the switch via SSH. If able to connect, Ansible runs the setup module and gather facts about the Cumulus switch.
<!-- vale off -->
## What Facts Are Gathered?
<!-- vale on -->
Ansible gathers many facts. This article uses a DNI et-7448bf model running Cumulus Linux 2.0.1 as the example setup. Some facts highlighted here are important for writing a playbook. You can find the entire results of the setup command {{<link url="#example-ansible_facts" text="below">}}.

The version of Cumulus Linux.

- What does the setup command return?

    ```
     "ansible_lsb": {
    "description": "2.0.1-fffbbda-201403232243-final",
     "id": "\"Cumulus Networks\"",
     "major_release": "2",
     "release": "2.0.1"
     },
    ```

- An example utilizing the variable:  

      - name: install image file (installs to opposite slot)
         command: /usr/cumulus/bin/cl-img-install -f http://192.168.100.1/{{ image }}
         when: ansible_lsb.release not in image

The above task in a playbook can use any fact gathered in the setup command (run automatically on any playbook unless purposelessly turned off). This example utilizes the `ansible_lsb.release` variable obtained in setup and compares it to the example playbook's specific variable of `{{image}}`. This playbook would upgrade the switch for this task utilizing the [cl-img-install]({{<ref "/cumulus-linux-43/Installation-Management/Managing-Cumulus-Linux-Disk-Images" >}}) command. {{<exlink url="https://docs.ansible.com/ansible/latest/user_guide/playbooks_conditionals.html" text="Creating a conditional statement">}} utilizing "when:" keeps you from wasting time installing unless the image given by the user running this playbook was different than the image currently running on the switch `{{ansible_lsb.release}}`.

### The Hostname

- What does the setup command return?

    ```
     "ansible_hostname": "sw1",
    ```

- An example utilizing the variable:  

      - name: configure MOTD with version # for user
         lineinfile: dest=/etc/motd regexp='^sw.*bin$' line='{{ ansible_hostname }} - running version {{ image }}' backrefs=yes
         register: result

This example utilizes the hostname as well as the internal variable `{{image}}`, which is not returned by the Ansible setup gathering the facts. The above task updates the MOTD on the Cumulus Linux switch with the current hostname and what image the switch is running. An example is: `sw1 - running version CumulusLinux-2.0.1-powerpc.bin`.

### The Management MAC Address

- What does the setup command return?

        "ansible_eth0": { 
          "active": true, 
          "device": "eth0", 
          "ipv4": {
            "address": "192.168.100.11",
            "netmask": "255.255.255.0",
            "network": "192.168.100.0" 
          },
           "ipv6": [ 
            {
            "address": "fe80::4638:39ff:fe00:3410", 
            "prefix": "64", 
            "scope": "link"
           }
           ],
           "macaddress": "44:38:39:00:34:10",
           "mtu": 1500,
           "promisc": false,
           "type": "ether"
         },

- An example utilizing the variable:  

      - name: writing report to /var/log/mac-script.log
         shell: "echo {{ansible_hostname}}: Script Completed Successfully at {{ansible_date_time.time}} - Version {{ansible_lsb.release}} MAC for eth0 is {{ansible_etho.macaddress}} >> /tmp/upgrade-script.log"
         delegate_to: 127.0.0.1

Example output for this task is `"sw1: Script Completed Successfully at 18:53:24 - Version 2.0.1 MAC for eth0 is 44:38:39:00:34:10"`. The script above outputs that text to a file it creates called `upgrade-script.log`, located in the `/tmp/` directory.

## Example Ansible Facts

{{<expand "ansible_facts">}}
```
sw1 | success >> {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "192.168.100.11"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::4638:39ff:fe00:3410"
        ],
        "ansible_architecture": "ppc",
        "ansible_bios_date": "NA",
        "ansible_bios_version": "NA",
        "ansible_cmdline": {
            "active": "1",
            "console": "ttyS0,115200"
        },
        "ansible_date_time": {
            "date": "2014-04-23",
            "day": "23",
            "epoch": "1398279204",
            "hour": "18",
            "iso8601": "2014-04-23T18:53:24Z",
            "iso8601_micro": "2014-04-23T18:53:24.063644Z",
            "minute": "53",
            "month": "04",
            "second": "24",
            "time": "18:53:24",
            "tz": "UTC",
            "tz_offset": "+0000",
            "year": "2014"
        },
        "ansible_default_ipv4": {
            "address": "192.168.100.11",
            "alias": "eth0",
            "gateway": "192.168.100.1",
            "interface": "eth0",
            "macaddress": "44:38:39:00:34:10",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "192.168.100.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_devices": {
            "mmcblk0": {
                "holders": [],
                "host": "",
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "scheduler_mode": "cfq",
                "sectors": "16039936",
                "sectorsize": "512",
                "size": "7.65 GB",
                "support_discard": "0",
                "vendor": null
            },
            "mtdblock0": {
                "holders": [],
                "host": "",
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "scheduler_mode": "cfq",
                "sectors": "252672",
                "sectorsize": "512",
                "size": "123.38 MB",
                "support_discard": "0",
                "vendor": null
            },
            "mtdblock1": {
                "holders": [],
                "host": "",
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "scheduler_mode": "cfq",
                "sectors": "8192",
                "sectorsize": "512",
                "size": "4.00 MB",
                "support_discard": "0",
                "vendor": null
            },
            "mtdblock2": {
                "holders": [],
                "host": "",
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "scheduler_mode": "cfq",
                "sectors": "256",
                "sectorsize": "512",
                "size": "128.00 KB",
                "support_discard": "0",
                "vendor": null
            },
            "mtdblock3": {
                "holders": [],
                "host": "",
                "model": null,
                "partitions": {},
                "removable": "0",
                "rotational": "0",
                "scheduler_mode": "cfq",
                "sectors": "1024",
                "sectorsize": "512",
                "size": "512.00 KB",
                "support_discard": "0",
                "vendor": null
            }
        },
        "ansible_distribution": "Debian",
        "ansible_distribution_release": "NA",
        "ansible_distribution_version": "7.4",
        "ansible_domain": "",
        "ansible_env": {
            "HOME": "/root",
            "LANG": "C",
            "LANGUAGE": "C",
            "LC_ALL": "C",
            "LC_CTYPE": "en_US.UTF-8",
            "LOGNAME": "root",
            "MAIL": "/var/mail/root",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11",
            "PWD": "/root",
            "SHELL": "/bin/bash",
            "SHLVL": "1",
            "SSH_CLIENT": "192.168.100.1 38058 22",
            "SSH_CONNECTION": "192.168.100.1 38058 192.168.100.11 22",
            "SSH_TTY": "/dev/pts/0",
            "TERM": "xterm",
            "USER": "root",
            "VTYSH_PAGER": "/bin/cat",
            "_": "/bin/sh"
        },
        "ansible_eth0": {
            "active": true,
            "device": "eth0",
            "ipv4": {
                "address": "192.168.100.11",
                "netmask": "255.255.255.0",
                "network": "192.168.100.0"
            },
            "ipv6": [
                {
                    "address": "fe80::4638:39ff:fe00:3410",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "44:38:39:00:34:10",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_form_factor": "NA",
        "ansible_fqdn": "sw1",
        "ansible_hostname": "sw1",
        "ansible_interfaces": [
            "swp13",
            "swp38",
            "swp24",
            "swp8",
            "swp9",
            "swp2",
            "swp3",
            "swp1",
            "swp6",
            "swp7",
            "swp4",
            "swp5",
            "swp18",
            "swp19",
            "swp30",
            "swp31",
            "swp36",
            "swp37",
            "swp34",
            "swp35",
            "swp10",
            "lo",
            "swp12",
            "swp39",
            "swp14",
            "swp15",
            "swp16",
            "swp17",
            "eth0",
            "swp32",
            "swp33",
            "swp50",
            "swp51",
            "swp21",
            "swp20",
            "swp23",
            "swp22",
            "swp25",
            "swp52",
            "swp27",
            "swp26",
            "swp29",
            "swp28",
            "swp49",
            "swp48",
            "swp11",
            "swp43",
            "swp42",
            "swp41",
            "swp40",
            "swp47",
            "swp46",
            "swp45",
            "swp44"
        ],
        "ansible_kernel": "3.2.46-1+deb7u1+cl2+1",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "ipv4": {
                "address": "127.0.0.1",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 16436,
            "promisc": false,
            "type": "loopback"
        },
        "ansible_lsb": {
            "description": "2.0.1-fffbbda-201403232243-final",
            "id": "\"Cumulus Networks\"",
            "major_release": "2",
            "release": "2.0.1"
        },
        "ansible_machine": "ppc",
        "ansible_memfree_mb": 1811,
        "ansible_memtotal_mb": 1961,
        "ansible_mounts": [
            {
                "device": "/dev/sysroot1",
                "fstype": "squashfs",
                "mount": "/mnt/root-ro",
                "options": "ro,relatime",
                "size_available": 0,
                "size_total": 83230720
            },
            {
                "device": "/dev/mmcblk0p3",
                "fstype": "ext2",
                "mount": "/mnt/root-rw",
                "options": "rw,noatime,errors=continue",
                "size_available": 6939443200,
                "size_total": 7418720256
            },
            {
                "device": "/dev/persist",
                "fstype": "ext2",
                "mount": "/mnt/persist",
                "options": "rw,relatime,errors=continue",
                "size_available": 123028480,
                "size_total": 129945600
            }
        ],
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_processor": [],
        "ansible_processor_cores": 1,
        "ansible_processor_count": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 1,
        "ansible_product_name": "dni,et-7448bf",
        "ansible_product_serial": "NA",
        "ansible_product_uuid": "NA",
        "ansible_product_version": "NA",
        "ansible_python_version": "2.7.3",
        "ansible_selinux": false,
        "ansible_ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBALQOYdH7nWkblxn+Q5G4S/oSsfQF2JDJClr0Da3HydfDxfRH3Rsi9qarKnSIxSvxoUjK7LYjDfYZBFnINCPdGVXBaUMu0LrcOMYb3q+uanE7sf4awL4OuQzApsE9si08YM7uokJ3VLqLzHXRd+TnnQx+PtCiAoNYRlkEGo/Jz8FbAAAAFQCObjJN+ewzVInFqcDYj3q3KnDE+QAAAIEAg3Z5xWeWrSTljRQn2d6F7SSwQuZfzvoSS3lqAEC6+xXfJVLh+lDYALRIdorB20AMDCbZh+MQW8/bWmrwCz20JI2Nq5o1aFqzlOMWPa/YdVUMGoSoJ9vmZBYWlKuq568OJ058xgLJTmtEGiuNMyJSlp7+IIxwaID9GuS1WgoNyzgAAACAfqAW8w8wWYeOt/7b2Lh8NHflhrbB0eEyhPmlgEog+dYeoLFM3nojKY4siJgNUKIqF32Gp4EPpZklXaXA8PLQfwimYBDdYDj3yYq2WKjUxPNnkcsf/tBDcdEWiAp3cBmoMO4RUlRZumo+kkRcvHWVa0tlAjEcHwFsMNPaNpWoyWE=",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBB8NV6cTbEcEy0fDOAXnBJpnv8L3UOZdyC4i3IWwR/EPXoHHK5uGHyKzCg+irF0X/n/AtuIwCCEHdXn02tLIwkw=",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDPZRLZA4slhDzBUrO3xvF7zWCD5JeSYFJPCGfKm9zoCkc75cR7mbXimc0Wle8naYcLANZzyMmd98n7oPi/Ort8Rary8agjoLBOR8r/1b8jHDuTu19Xq02RnFrlsCsR+nbq7OPtXLUSaDL4osQq6tlX2MgmiWjshZhuQ7yg/12LbPDduiSAfQjWWzNDO+BruCmxAg70Czxu5XQwjXOzY6rkF2ZXqF3bTntJHTe0KzRHGdqvOA4/JfRkPmDpOdSYTr4e1dSancNdGZEl4lBdlKF/ZYUr26RMJfEWpyvcUARElah+L1CkqGDSyjosYvGnFWnsioTx3Qg/GgZ6OW4xdOFD",
        "ansible_swapfree_mb": 0,
        "ansible_swaptotal_mb": 0,
        "ansible_swp1": {
            "active": false,
            "device": "swp1",
            "macaddress": "44:38:39:00:34:11",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp10": {
            "active": false,
            "device": "swp10",
            "macaddress": "44:38:39:00:34:1a",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp11": {
            "active": false,
            "device": "swp11",
            "macaddress": "44:38:39:00:34:1b",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp12": {
            "active": false,
            "device": "swp12",
            "macaddress": "44:38:39:00:34:1c",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp13": {
            "active": false,
            "device": "swp13",
            "macaddress": "44:38:39:00:34:1d",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp14": {
            "active": false,
            "device": "swp14",
            "macaddress": "44:38:39:00:34:1e",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp15": {
            "active": false,
            "device": "swp15",
            "macaddress": "44:38:39:00:34:1f",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp16": {
            "active": false,
            "device": "swp16",
            "macaddress": "44:38:39:00:34:20",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp17": {
            "active": false,
            "device": "swp17",
            "macaddress": "44:38:39:00:34:21",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp18": {
            "active": false,
            "device": "swp18",
            "macaddress": "44:38:39:00:34:22",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp19": {
            "active": false,
            "device": "swp19",
            "macaddress": "44:38:39:00:34:23",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp2": {
            "active": false,
            "device": "swp2",
            "macaddress": "44:38:39:00:34:12",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp20": {
            "active": false,
            "device": "swp20",
            "macaddress": "44:38:39:00:34:24",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp21": {
            "active": false,
            "device": "swp21",
            "macaddress": "44:38:39:00:34:25",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp22": {
            "active": false,
            "device": "swp22",
            "macaddress": "44:38:39:00:34:26",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp23": {
            "active": false,
            "device": "swp23",
            "macaddress": "44:38:39:00:34:27",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp24": {
            "active": false,
            "device": "swp24",
            "macaddress": "44:38:39:00:34:28",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp25": {
            "active": false,
            "device": "swp25",
            "macaddress": "44:38:39:00:34:29",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp26": {
            "active": false,
            "device": "swp26",
            "macaddress": "44:38:39:00:34:2a",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp27": {
            "active": false,
            "device": "swp27",
            "macaddress": "44:38:39:00:34:2b",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp28": {
            "active": false,
            "device": "swp28",
            "macaddress": "44:38:39:00:34:2c",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp29": {
            "active": false,
            "device": "swp29",
            "macaddress": "44:38:39:00:34:2d",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp3": {
            "active": false,
            "device": "swp3",
            "macaddress": "44:38:39:00:34:13",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp30": {
            "active": false,
            "device": "swp30",
            "macaddress": "44:38:39:00:34:2e",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp31": {
            "active": false,
            "device": "swp31",
            "macaddress": "44:38:39:00:34:2f",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp32": {
            "active": false,
            "device": "swp32",
            "macaddress": "44:38:39:00:34:30",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp33": {
            "active": false,
            "device": "swp33",
            "macaddress": "44:38:39:00:34:31",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp34": {
            "active": false,
            "device": "swp34",
            "macaddress": "44:38:39:00:34:32",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp35": {
            "active": false,
            "device": "swp35",
            "macaddress": "44:38:39:00:34:33",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp36": {
            "active": false,
            "device": "swp36",
            "macaddress": "44:38:39:00:34:34",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp37": {
            "active": false,
            "device": "swp37",
            "macaddress": "44:38:39:00:34:35",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp38": {
            "active": false,
            "device": "swp38",
            "macaddress": "44:38:39:00:34:36",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp39": {
            "active": false,
            "device": "swp39",
            "macaddress": "44:38:39:00:34:37",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp4": {
            "active": false,
            "device": "swp4",
            "macaddress": "44:38:39:00:34:14",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp40": {
            "active": false,
            "device": "swp40",
            "macaddress": "44:38:39:00:34:38",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp41": {
            "active": false,
            "device": "swp41",
            "macaddress": "44:38:39:00:34:39",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp42": {
            "active": false,
            "device": "swp42",
            "macaddress": "44:38:39:00:34:3a",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp43": {
            "active": false,
            "device": "swp43",
            "macaddress": "44:38:39:00:34:3b",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp44": {
            "active": false,
            "device": "swp44",
            "macaddress": "44:38:39:00:34:3c",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp45": {
            "active": false,
            "device": "swp45",
            "macaddress": "44:38:39:00:34:3d",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp46": {
            "active": false,
            "device": "swp46",
            "macaddress": "44:38:39:00:34:3e",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp47": {
            "active": false,
            "device": "swp47",
            "macaddress": "44:38:39:00:34:3f",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp48": {
            "active": false,
            "device": "swp48",
            "macaddress": "44:38:39:00:34:40",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp49": {
            "active": false,
            "device": "swp49",
            "macaddress": "44:38:39:00:34:41",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp5": {
            "active": false,
            "device": "swp5",
            "macaddress": "44:38:39:00:34:15",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp50": {
            "active": false,
            "device": "swp50",
            "macaddress": "44:38:39:00:34:45",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp51": {
            "active": false,
            "device": "swp51",
            "macaddress": "44:38:39:00:34:49",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp52": {
            "active": false,
            "device": "swp52",
            "macaddress": "44:38:39:00:34:4d",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp6": {
            "active": false,
            "device": "swp6",
            "macaddress": "44:38:39:00:34:16",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp7": {
            "active": false,
            "device": "swp7",
            "macaddress": "44:38:39:00:34:17",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp8": {
            "active": false,
            "device": "swp8",
            "macaddress": "44:38:39:00:34:18",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_swp9": {
            "active": false,
            "device": "swp9",
            "macaddress": "44:38:39:00:34:19",
            "mtu": 1500,
            "promisc": false,
            "type": "ether"
        },
        "ansible_system": "Linux",
        "ansible_system_vendor": "dni",
        "ansible_user_id": "root",
        "ansible_userspace_bits": "32"
    },
    "changed": false
}
```

{{</expand>}}
