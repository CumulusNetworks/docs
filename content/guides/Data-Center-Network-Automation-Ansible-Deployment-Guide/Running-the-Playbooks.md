---
title: Running the Playbooks
author: NVIDIA
weight: 50
product: Technical Guides
imgData: guides
---
<style>
  .scroll{
    height: 500px;
    overflow-y: auto;
  }
</style>

## Enable the NVUE API

Cumulus Linux 5.5 and earlier disables the NVUE REST API by default. If you want to use any of the object specific modules or the `api` module, you need to enable the NVUE REST API with the following commands on the switch:

```
cumulus@switch:~$ sudo ln -s /etc/nginx/sites-{available,enabled}/nvue.conf 

cumulus@switch:~$ sudo sed -i 's/listen localhost:8765 ssl;/listen \[::\]:8765 ipv6only=off ssl;/g' /etc/nginx/sites-available/nvue.conf 

cumulus@switch:~$ sudo systemctl restart nginx
```

You can find a sample playbook that enables the NVUE REST API across all of the switches {{<exlink url="https://gitlab.com/nvidia-networking/systems-engineering/nvue/-/blob/main/examples/playbooks/enable-nvue-api.yml" text="here">}}. Download the file and run it against the switches.
 
```
cumulus@oob-management:~$ curl -o enable-nvue-api.yml https://gitlab.com/nvidia-networking/systems-engineering/nvue/-/raw/main/examples/playbooks/enable-nvue-api.yml

cumulus@oob-management:~$ curl -o hosts https://gitlab.com/nvidia-networking/systems-engineering/nvue/-/raw/main/examples/hosts

cumulus@oob-management:~$ ansible-playbook enable-nvue-api.yml -i hosts   
```

## Sample Playbooks
You can find additional example playbooks and host files in the `<collections_directory>/nvidia/nvue/examples` directory or in the git repository {{<exlink url="https://gitlab.com/nvidia-networking/systems-engineering/nvue/-/tree/main/examples/playbooks" text="here">}}.

```
cumulus@oob-management:~$ ls ~/.ansible/collections/ansible_collections/nvidia/nvue/examples/

collections  host_vars  hosts  playbooks
```

You can run any of the sample playbooks in the `playbooks` directory.

```
cumulus@oob-management:~$ ls ~/.ansible/collections/ansible_collections/nvidia/nvue/examples/playbooks

api.yml                      gather-config-multiple.yml
bridge.yml                   gather-config.yml
command.yml                  interface.yml
evpn-multihoming-leaf01.yml  revision.yml
evpn-symmetric-leaf01.yml    static-vxlan-leaf01.yml
```

The `gather-config.yml` uses the high-level `api` module to fetch the root configuration and the object-level `interface` module to fetch interface configuration.

```
cumulus@oob-management:~$ cd ~/.ansible/collections/ansible_collections/nvidia/nvue/examples/
cumulus@oob-management:~$ cat playbooks/gather-config.yml

- name: NVUE API
  hosts: cumulus
  connection: ansible.netcommon.httpapi
  gather_facts: false
  vars:
    ansible_network_os: nvidia.nvue.httpapi
    ansible_httpapi_port: 8765
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false

  tasks:
    - name: Get the current config
      nvidia.nvue.api:
        operation: get
      register: output

    - name: Print current config
      ansible.builtin.debug:
        msg: "{{ output }}"

    - name: Get the current interface config
      nvidia.nvue.interface:
        state: gathered
      register: interface

    - name: Print current interface
      ansible.builtin.debug:
        msg: "{{ interface }}"
```

Run the playbook. Optionally, you can add the `-v` parameter to increase verbosity of the playbook execution.

<div class="scroll">

```
cumulus@oob-management:~$ ansible-playbook playbooks/gather-config.yml -i hosts  

Sample Output:
[WARNING]: running playbook inside collection nvidia.nvue

PLAY [NVUE API] *****************************************************************

TASK [Get the current config] *****************************************************************
ok: [cumulus]

TASK [Print current config] *****************************************************************
ok: [cumulus] => {
    "msg": {
        "changed": false,
        "failed": false,
        "message": {
            "acl": {},
            "bridge": {
                "domain": {
                    "br_default": {
                        "ageing": 1800,
                        "encap": "802.1Q",
                        "mac-address": "auto",
                        "multicast": {
                            "snooping": {
                                "enable": "on",
                                "querier": {
                                    "enable": "off"
                                }
                            }
                        },
                        "stp": {
                            "priority": 32768,
                            "state": {
                                "up": {}
                            }
                        },
                        "type": "vlan-aware",
                        "untagged": 1,
                        "vlan": {
                            "10": {
                                "multicast": {
                                    "snooping": {
                                        "querier": {
                                            "source-ip": "0.0.0.0"
                                        }
                                    }
                                },
                                "ptp": {
                                    "enable": "off"
                                },
                                "vni": {
                                    "10": {
                                        "flooding": {
                                            "enable": "auto"
                                        },
                                        "mac-learning": "auto"
                                    }
                                }
                            }
                        },
                        "vlan-vni-offset": 0
                    }
                }
            },
            "evpn": {
                "enable": "off"
            },
            "header": {
                "model": "VX",
                "nvue-api-version": "nvue_v1",
                "rev-id": 1.0,
                "version": "Cumulus Linux 5.5.0"
            },
            "interface": {
                "eth0": {
                    "acl": {},
                    "ip": {
                        "address": {
                            "dhcp": {}
                        },
                        "gateway": {},
                        "ipv4": {
                            "forward": "off"
                        },
                        "ipv6": {
                            "enable": "on",
                            "forward": "off"
                        },
                        "vrf": "mgmt"
                    },
                    "link": {
                        "auto-negotiate": "on",
                        "duplex": "full",
                        "fec": "auto",
                        "mtu": 9216,
                        "speed": "auto",
                        "state": {
                            "up": {}
                        }
                    },
                    "type": "eth"
                },
                "lo": {
                    "ip": {
                        "address": {},
                        "igmp": {
                            "enable": "off"
                        },
                        "ipv4": {
                            "forward": "on"
                        },
                        "ipv6": {
                            "enable": "on",
                            "forward": "on"
                        },
                        "vrf": "default"
                    },
                    "router": {
                        "adaptive-routing": {
                            "enable": "off"
                        },
                        "ospf": {
                            "enable": "off"
                        },
                        "ospf6": {
                            "enable": "off"
                        },
                        "pim": {
                            "enable": "off"
                        }
                    },
                    "type": "loopback"
                }
            },
            "mlag": {
                "enable": "off"
            },
            "nve": {
                "vxlan": {
                    "enable": "off"
                }
            },
            "qos": {
                "advance-buffer-config": {
                    "default-global": {
                        "egress-lossy-buffer": {
                            "multicast-switch-priority": {
                                "0": {
                                    "service-pool": "0"
                                },
                                "1": {
                                    "service-pool": "0"
                                },
                                "2": {
                                    "service-pool": "0"
                                },
                                "3": {
                                    "service-pool": "0"
                                },
                                "4": {
                                    "service-pool": "0"
                                },
                                "5": {
                                    "service-pool": "0"
                                },
                                "6": {
                                    "service-pool": "0"
                                },
                                "7": {
                                    "service-pool": "0"
                                }
                            },
                            "traffic-class": {
                                "0": {
                                    "service-pool": "0"
                                },
                                "1": {
                                    "service-pool": "0"
                                },
                                "2": {
                                    "service-pool": "0"
                                },
                                "3": {
                                    "service-pool": "0"
                                },
                                "4": {
                                    "service-pool": "0"
                                },
                                "5": {
                                    "service-pool": "0"
                                },
                                "6": {
                                    "service-pool": "0"
                                },
                                "7": {
                                    "service-pool": "0"
                                }
                            }
                        },
                        "egress-pool": {
                            "0": {
                                "memory-percent": 100,
                                "mode": "dynamic"
                            }
                        },
                        "ingress-lossy-buffer": {
                            "priority-group": {
                                "bulk": {
                                    "service-pool": "0",
                                    "switch-priority": {
                                        "0": {},
                                        "1": {},
                                        "2": {},
                                        "3": {},
                                        "4": {},
                                        "5": {},
                                        "6": {},
                                        "7": {}
                                    }
                                }
                            }
                        },
                        "ingress-pool": {
                            "0": {
                                "memory-percent": 100,
                                "mode": "dynamic"
                            }
                        }
                    }
                },
                "congestion-control": {
                    "default-global": {
                        "traffic-class": {
                            "0": {
                                "ecn": "enable",
                                "max-threshold": 1500000,
                                "min-threshold": 150000,
                                "probability": 100,
                                "red": "disable"
                            }
                        }
                    }
                },
                "egress-queue-mapping": {
                    "default-global": {
                        "switch-priority": {
                            "0": {
                                "traffic-class": 0
                            },
                            "1": {
                                "traffic-class": 1
                            },
                            "2": {
                                "traffic-class": 2
                            },
                            "3": {
                                "traffic-class": 3
                            },
                            "4": {
                                "traffic-class": 4
                            },
                            "5": {
                                "traffic-class": 5
                            },
                            "6": {
                                "traffic-class": 6
                            },
                            "7": {
                                "traffic-class": 7
                            }
                        }
                    }
                },
                "egress-scheduler": {
                    "default-global": {
                        "traffic-class": {
                            "0": {
                                "bw-percent": 12,
                                "mode": "dwrr"
                            },
                            "1": {
                                "bw-percent": 13,
                                "mode": "dwrr"
                            },
                            "2": {
                                "bw-percent": 12,
                                "mode": "dwrr"
                            },
                            "3": {
                                "bw-percent": 13,
                                "mode": "dwrr"
                            },
                            "4": {
                                "bw-percent": 12,
                                "mode": "dwrr"
                            },
                            "5": {
                                "bw-percent": 13,
                                "mode": "dwrr"
                            },
                            "6": {
                                "bw-percent": 12,
                                "mode": "dwrr"
                            },
                            "7": {
                                "bw-percent": 13,
                                "mode": "dwrr"
                            }
                        }
                    }
                },
                "egress-shaper": {},
                "link-pause": {},
                "mapping": {
                    "default-global": {
                        "pcp": {
                            "0": {
                                "switch-priority": 0
                            },
                            "1": {
                                "switch-priority": 1
                            },
                            "2": {
                                "switch-priority": 2
                            },
                            "3": {
                                "switch-priority": 3
                            },
                            "4": {
                                "switch-priority": 4
                            },
                            "5": {
                                "switch-priority": 5
                            },
                            "6": {
                                "switch-priority": 6
                            },
                            "7": {
                                "switch-priority": 7
                            }
                        },
                        "port-default-sp": 0,
                        "trust": "l2"
                    }
                },
                "pfc": {},
                "remark": {
                    "default-global": {}
                },
                "roce": {
                    "enable": "off"
                },
                "traffic-pool": {
                    "default-lossy": {
                        "memory-percent": 100,
                        "switch-priority": {
                            "0": {},
                            "1": {},
                            "2": {},
                            "3": {},
                            "4": {},
                            "5": {},
                            "6": {},
                            "7": {}
                        }
                    }
                }
            },
            "router": {
                "adaptive-routing": {
                    "enable": "off"
                },
                "bgp": {
                    "enable": "off"
                },
                "igmp": {
                    "enable": "off"
                },
                "nexthop": {
                    "group": {}
                },
                "ospf": {
                    "enable": "off"
                },
                "ospf6": {
                    "enable": "off"
                },
                "pbr": {
                    "enable": "off"
                },
                "pim": {
                    "enable": "off"
                },
                "policy": {
                    "as-path-list": {},
                    "community-list": {},
                    "ext-community-list": {},
                    "large-community-list": {},
                    "prefix-list": {},
                    "route-map": {}
                },
                "ptm": {
                    "enable": "off"
                },
                "vrr": {
                    "enable": "off"
                },
                "vrrp": {
                    "enable": "off"
                }
            },
            "service": {
                "dhcp-relay": {},
                "dhcp-relay6": {},
                "dhcp-server": {},
                "dhcp-server6": {},
                "dns": {},
                "lldp": {
                    "dot1-tlv": "off",
                    "lldp-med-inventory-tlv": "off",
                    "mode": "default",
                    "tx-hold-multiplier": 4,
                    "tx-interval": 30
                },
                "ntp": {},
                "ptp": {
                    "1": {
                        "acceptable-master": {},
                        "domain": 0,
                        "enable": "off",
                        "ip-dscp": 46,
                        "logging-level": "info",
                        "monitor": {
                            "max-offset-threshold": 50,
                            "max-timestamp-entries": 100,
                            "max-violation-log-entries": 4,
                            "max-violation-log-sets": 2,
                            "min-offset-threshold": -50,
                            "path-delay-threshold": 200,
                            "violation-log-interval": 1
                        },
                        "priority1": 128,
                        "priority2": 128,
                        "profile": {
                            "default-1588": {
                                "announce-interval": 1,
                                "announce-timeout": 3,
                                "delay-mechanism": "end-to-end",
                                "delay-req-interval": 0,
                                "domain": 0,
                                "priority1": 128,
                                "priority2": 128,
                                "profile-type": "ieee-1588",
                                "sync-interval": 0,
                                "transport": "ipv4"
                            },
                            "default-itu-8275-1": {
                                "announce-interval": -3,
                                "announce-timeout": 3,
                                "delay-mechanism": "end-to-end",
                                "delay-req-interval": -4,
                                "domain": 24,
                                "local-priority": 128,
                                "priority1": 128,
                                "priority2": 128,
                                "profile-type": "itu-g-8275-1",
                                "sync-interval": -4,
                                "transport": "802.3"
                            },
                            "default-itu-8275-2": {
                                "announce-interval": 0,
                                "announce-timeout": 3,
                                "delay-mechanism": "end-to-end",
                                "delay-req-interval": -6,
                                "domain": 44,
                                "local-priority": 128,
                                "priority1": 128,
                                "priority2": 128,
                                "profile-type": "itu-g-8275-2",
                                "sync-interval": -6,
                                "transport": "ipv4"
                            }
                        },
                        "unicast-master": {}
                    }
                },
                "snmp-server": {
                    "enable": "off"
                },
                "synce": {
                    "enable": "off"
                },
                "syslog": {}
            },
            "system": {
                "aaa": {
                    "authentication-order": {},
                    "tacacs": {
                        "enable": "off"
                    },
                    "user": {}
                },
                "acl": {
                    "mode": "atomic"
                },
                "config": {
                    "apply": {
                        "ignore": {},
                        "overwrite": "all"
                    },
                    "auto-save": {
                        "enable": "off"
                    },
                    "snippet": {}
                },
                "control-plane": {
                    "acl": {},
                    "policer": {},
                    "trap": {}
                },
                "counter": {
                    "polling-interval": {
                        "logical-interface": 5,
                        "physical-interface": 2
                    }
                },
                "forwarding": {
                    "ecmp-hash": {
                        "destination-ip": "on",
                        "destination-port": "on",
                        "gtp-teid": "off",
                        "ingress-interface": "off",
                        "inner-destination-ip": "off",
                        "inner-destination-port": "off",
                        "inner-ip-protocol": "off",
                        "inner-ipv6-label": "off",
                        "inner-source-ip": "off",
                        "inner-source-port": "off",
                        "ip-protocol": "on",
                        "ipv6-label": "on",
                        "source-ip": "on",
                        "source-port": "on"
                    },
                    "host-route-preference": "route",
                    "lag-hash": {
                        "destination-ip": "on",
                        "destination-mac": "on",
                        "destination-port": "on",
                        "ether-type": "on",
                        "gtp-teid": "off",
                        "ip-protocol": "on",
                        "source-ip": "on",
                        "source-mac": "on",
                        "source-port": "on",
                        "vlan": "on"
                    },
                    "programming": {
                        "log-level": "info"
                    }
                },
                "global": {
                    "anycast-id": "none",
                    "anycast-mac": "none",
                    "fabric-id": 1,
                    "fabric-mac": "none",
                    "l3svd": {
                        "enable": "off"
                    },
                    "reserved": {
                        "routing-table": {
                            "pbr": {
                                "begin": 10000,
                                "end": 4294966272
                            }
                        },
                        "vlan": {
                            "internal": {
                                "range": "3725-3999"
                            },
                            "l3-vni-vlan": {
                                "begin": 4000,
                                "end": 4064
                            }
                        }
                    },
                    "system-mac": "auto"
                },
                "hostname": "cumulus",
                "port-mirror": {
                    "session": {}
                },
                "reboot": {
                    "mode": "cold"
                },
                "wjh": {
                    "enable": "off"
                }
            },
            "vrf": {
                "default": {
                    "evpn": {
                        "enable": "off"
                    },
                    "loopback": {
                        "ip": {
                            "address": {
                                "127.0.0.1/8": {},
                                "::1/128": {}
                            }
                        }
                    },
                    "ptp": {
                        "enable": "on"
                    },
                    "router": {
                        "bgp": {
                            "enable": "off"
                        },
                        "nexthop-tracking": {},
                        "ospf": {
                            "enable": "off"
                        },
                        "ospf6": {
                            "enable": "off"
                        },
                        "pim": {
                            "enable": "off"
                        },
                        "rib": {},
                        "static": {}
                    },
                    "table": "auto"
                },
                "mgmt": {
                    "evpn": {
                        "enable": "off"
                    },
                    "loopback": {
                        "ip": {
                            "address": {
                                "127.0.0.1/8": {},
                                "::1/128": {}
                            }
                        }
                    },
                    "ptp": {
                        "enable": "on"
                    },
                    "router": {
                        "bgp": {
                            "enable": "off"
                        },
                        "nexthop-tracking": {},
                        "ospf": {
                            "enable": "off"
                        },
                        "ospf6": {
                            "enable": "off"
                        },
                        "rib": {},
                        "static": {}
                    },
                    "table": "auto"
                }
            }
        }
    }
}

TASK [Get the current interface config] *****************************************************************
ok: [cumulus]

TASK [Print current interface] *****************************************************************
ok: [cumulus] => {
    "msg": {
        "changed": false,
        "failed": false,
        "message": {
            "eth0": {
                "acl": {},
                "ip": {
                    "address": {
                        "dhcp": {}
                    },
                    "gateway": {},
                    "ipv4": {
                        "forward": "off"
                    },
                    "ipv6": {
                        "enable": "on",
                        "forward": "off"
                    },
                    "vrf": "mgmt"
                },
                "link": {
                    "auto-negotiate": "on",
                    "duplex": "full",
                    "fec": "auto",
                    "mtu": 9216,
                    "speed": "auto",
                    "state": {
                        "up": {}
                    }
                },
                "type": "eth"
            },
            "lo": {
                "ip": {
                    "address": {},
                    "igmp": {
                        "enable": "off"
                    },
                    "ipv4": {
                        "forward": "on"
                    },
                    "ipv6": {
                        "enable": "on",
                        "forward": "on"
                    },
                    "vrf": "default"
                },
                "router": {
                    "adaptive-routing": {
                        "enable": "off"
                    },
                    "ospf": {
                        "enable": "off"
                    },
                    "ospf6": {
                        "enable": "off"
                    },
                    "pim": {
                        "enable": "off"
                    }
                },
                "type": "loopback"
            }
        }
    }
}

PLAY RECAP *****************************************************************
cumulus                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

</div>

## Resources

- {{<exlink url="https://gitlab.com/nvidia-networking/systems-engineering/nvue/-/tree/main/examples/playbooks" text="NVUE modules on Gitlab">}}
- {{<exlink url="https://galaxy.ansible.com/nvidia/nvue" text="NVUE modules on Galaxy">}}
- {{<exlink url="https://console.redhat.com/ansible/automation-hub/repo/published/nvidia/nvue/" text="NVUE modules on Automation Hub">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/Data-Center-Network-Automation-Quick-Start-Guide/" text="Data Center Network Automation Quick Start Guide">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/production-ready-automation/" text="Production Ready Automation Guide">}}
- {{<exlink url="https://developer.nvidia.com/blog/automating-data-center-networks-with-nvidia-cumulus-linux/" text="Automating Data Center Networks with NVIDIA Cumulus Linux">}}