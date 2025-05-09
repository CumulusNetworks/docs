---
title: NVUE Format Reference
author: NVIDIA
weight: 1855
toc: 3
---

The NVUE openAPI schema references the `format` keyword, which takes a string that represents the format of valid input for a given property (such as `format: ipv4`, `format: float`, and so on). This section lists the formats that the schema uses and validates, and provides valid examples.

## Reserved Names

NVUE reserves the following names:

```
"auto"
"none"
"null"
"any"
"all"
```

NVUE uses the reserved names for special purposes:
- Interface names
- Instance names
- Item names
- Generic names
- Profile names
- Bridge names
- VRF names

### user-name

Usernames for system accounts.

**Valid Format:**
- Must start with a letter or underscore (_)
- Can contain letters, digits, underscores, or dashes
- Can end with a dollar sign ($)
- Maximum length: 32 characters
- Cannot be a reserved name (auto, none, null, any, all)

**Valid Examples:**

```
"john_doe"
"user123"
"admin-user"
"system_user$"
"_service"
```

### key-string

SSH public keys.

**Valid Format:**

- Must be a base64 encoded string
- Must be properly formatted base64

### command

Command strings for authorization.

**Valid Format:**

- Must not contain any of the following special characters:
  - `|` (pipe)
  - `&` (ampersand)
  - `;` (semicolon)
  - `(` (left parenthesis)
  - `)` (right parenthesis)
  - `<` (less than)
  - `>` (greater than)
  - `'` (single quote)
  - `"` (double quote)
  - `$` (dollar sign)
  - `\` (backslash)
  - `#` (hash)
  - `*` (asterisk)
  - `?` (question mark)
- Cannot be a reserved name

**Valid Examples:**

```
"ls"
"show interfaces"
"configure terminal"
"ping 10.10.10.2"
```

### clock-date

Date format for system clock.

**Valid Format:**
- Format: YYYY-MM-DD
- Year must be between 1970 and 2037
- Month: 01-12 or 1-12
- Day: 01-31 or 1-31

**Valid Examples:**

```
"2024-03-15"
"1970-01-01"
"2037-12-31"
"2024-3-5"
```

### clock-time

Time format for system clock.

**Valid Format:**
- Format: HH:MM:SS
- Hours: 00-23
- Minutes: 00-59
- Seconds: 00-59

**Valid Examples:**
```
"00:00:00"
"23:59:59"
"12:30:45"
"09:05:01"
```

### mss-format

TCP MSS format.

**Valid Input Format:**
- Must be a string
- Either a single number or a range
- Range format: "start-end"
- Values must be less than MAX_TCP_MSS (65535)
- Range end must be greater than start

**Valid Examples:**

```
"536"
"536-65535"
"128"
"1000-2000"
```

### rate-limit

Rate limit values.

**Valid Format:**
- Format: number/unit
- Units: second, min, hour
- Maximum values:
  - second: 1,000,000
  - min: 60,000,000
  - hour: 3,600,000,000

**Valid Examples:**

```
"1000/second"
"50000/min"
"1000000/hour"
"100/second"
```

### secret-string

Secret strings.

**Valid Format:**
- Non-empty string
- Cannot contain spaces

**Valid Examples:**

```
"secret123"
"mySecretKey"
"password123!@#"
```

### bond-swp-name

Bond and switch port names.

**Valid Format:**
- Must be either a valid switch port name (swp) or bond name
- Cannot be a reserved name
- Cannot be a VXLAN interface name

**Valid Examples:**

```
"swp1"
"swp1s1"
"bond0"
"bond1"
```

### interval

Sample interval values.

**Valid Format:**
- Must be an integer
- Must be a multiple of 10

**Valid Examples:**

```
10
20
100
1000
```

### repo-url

Repository URLs.

**Valid Format:**
- HTTP/HTTPS URLs
- Copy/File paths
- Must follow proper URL format for HTTP/HTTPS
- File/Copy paths cannot contain any of the following special characters:
  - `\` (backslash)
  - `/` (forward slash)
  - `:` (colon)
  - `*` (asterisk)
  - `?` (question mark)
  - `"` (double quote)
  - `<` (less than)
  - `>` (greater than)
  - `|` (pipe)

**Valid Examples:**

```
"http://www.example.com"
"https://apps.example.com/repos/"
"file:/home/apt/debian"
"copy:/var/lib/apt/archive"
```

### repo-dist

Repository distribution names.

**Valid Format:**
- Alphanumeric characters
- Can contain hyphens (-) and underscores (_)
- Cannot contain any other special characters

**Valid Examples:**

```
"stable"
"main"
"ubuntu-20-04"
"debian_bullseye"
```

### repo-pool

Repository pool names.

**Valid Format:**
- Alphanumeric characters
- Can contain hyphens (-) and underscores (_)
- Cannot contain any other special characters

**Valid Examples:**

```
"main"
"contrib"
"non-free"
"universe_multiverse"
```

### transceiver-name

Transceiver interface names.

**Valid Format:**
- Must be a valid switch port name (swp)
- Must match NOS patterns for transceiver types
- Can be a range of interfaces

**Valid Examples:**

```
"swp1"
"swp1s1"
"swp1-4"
"swp1,2"
```

### interface-name

The `interface-name` format supports various types of network interface names.

**Valid Interface Types**

- Switch Port (swp)
- Ethernet (eth)
- Subinterface (sub)
- Switch Virtual Interface (svi)
- Loopback (lo)
- Bond interfaces
- NOS-specific interface types

**Valid Examples**

```
# Switch Ports
swp1
swp1s1
swp1L1
swp1L1s1

# Ethernet
eth1
eth2

# Subinterfaces
eth1.1
eth1.1.1
bond1.1

# Switch Virtual Interfaces
vlan1
vlan1-v0
vrrp4-1-1
vrrp6-1-1

# Loopback
lo

# Bond interfaces
bond1
bond_1
bond1_1
```

**Rules**

1. Switch Port (swp) names:
   - Must start with "sw"
   - Followed by module number (optional)
   - Followed by "p" and port number
   - Optionally followed by "s" and breakout number
   - Optionally followed by "L" for logical ports

2. Ethernet (eth) names:
   - Must start with "eth"
   - Followed by a number

3. Subinterface names:
   - Must start with a letter
   - Can contain letters, numbers, and underscores
   - Must have at least one dot (.) followed by a number
   - Can have multiple dot-separated numbers

4. Switch Virtual Interface (svi) names:
   - Must start with "vlan" followed by a number or name
   - Optionally followed by "-v0"
   - Or must be a VRRP interface name (vrrp4/vrrp6-number-number)

5. Loopback names:
   - Must be exactly `lo`.

6. Bond interface names:
   - Must start with a letter
   - Can contain letters, numbers, and underscores
   - Cannot match patterns of other interface types
   - Cannot be a reserved name

7. General rules:
   - Names cannot be `reserved` words (auto, none, null, any, all)
   - Names cannot start with reserved prefixes (sw, eth, vlan, ib, fnm, vrrp)
   - Names cannot match the pattern "lo" followed by a number (reserved for future use)

### Interface Name Range Support

The `interface-name` format also supports specifying a range of interfaces using a special syntax. When you specify a range, each interface name in the range must be valid according to the rules above.

**Valid Range Examples**

```
# Switch Port Ranges
swp1-3 # Expands to: swp1, swp2, swp3
swp1,2,3 # Expands to: swp1, swp2, swp3
swp1-3,5 # Expands to: swp1, swp2, swp3, swp5
swp1-3,5,7 # Expands to: swp1, swp2, swp3, swp5, swp7
swp1s1-3 # Expands to: swp1s1, swp1s2, swp1s3
swp1s1,2,3 # Expands to: swp1s1, swp1s2, swp1s3
swp1L1-3 # Expands to: swp1L1, swp1L2, swp1L3
swp1L1,2,3 # Expands to: swp1L1, swp1L2, swp1L3
swp1L1s1-3 # Expands to: swp1L1s1, swp1L1s2, swp1L1s3
swp1L1s1,2,3 # Expands to: swp1L1s1, swp1L1s2, swp1L1s3

# Ethernet Ranges
eth1-3 # Expands to: eth1, eth2, eth3

# Bond Ranges
bond1-3 # Expands to: bond1, bond2, bond3
```

**Range Rules**

1. You specify a range format with a hyphen (-) between start and end numbers.
2. The start number must be less than the end number.
3. Only the numeric portion of the interface name can be part of the range.
4. All expanded interface names must be valid according to their respective interface type rules.
5. Cannot mix different interface types in a single range.
6. The non-numeric parts of the interface name must be identical for all interfaces in the range.

### Network Address Formats

#### ipv4

IPv4 address format.

**Valid Input Format:**
- Must be a string
- Four octets separated by dots
- Each octet must be between 0 and 255
- No leading zeros allowed
- No spaces allowed

**Valid Examples:**

```
"192.168.1.1"
"10.10.10.4"
"172.16.254.1"
```

#### ipv4-unicast

IPv4 unicast address format.

**Valid Input Format:**
- Must be a valid IPv4 address
- First octet must not be between 224 and 239 (multicast range)

**Valid Examples:**

```
"192.168.1.1"
"10.10.10.4"
"172.16.254.1"
```

#### ipv4-multicast

IPv4 multicast address format.

**Valid Input Format:**
- Must be a valid IPv4 address
- First octet must be between 224 and 239

**Valid Examples:**

```
"224.0.0.1"
"239.255.255.250"
"230.0.0.1"
```

#### ipv4-prefix

IPv4 address with prefix length.

**Valid Input Format:**
- Must be a string
- Format: "ipv4_address/prefix_length"
- Prefix length must be between 0 and 32

**Valid Examples:**

```
"192.168.1.0/24"
"10.0.0.0/8"
"172.16.0.0/12"
```

#### ipv4-sub-prefix

IPv4 subnet address with prefix length.

**Valid Input Format:**
- Must be a string
- Format: "network_address/prefix_length"
- Must be a valid network address (not a host address)
- Prefix length must be between 0 and 32

**Valid Examples:**

```
"192.168.1.0/24"
"10.0.0.0/8"
"172.16.0.0/12"
```
<!-- vale off -->
#### ipv6-prefix

IPv6 address with prefix length.

**Valid Input Format:**
- Must be a string.
- Format: "ipv6_address/prefix_length"
- Prefix length must be between 0 and 128

**Valid Examples:**

```
"2001:db8::/32"
"2001:db8:85a3::8a2e:370:7334/64"
"fe80::/10"
```

#### ipv4-netmask

IPv4 address with netmask.

**Valid Input Format:**
- Must be a string.
- Format: "ipv4_address/netmask"
- Both parts must be valid IPv4 addresses

**Valid Examples:**

```
"192.168.1.0/255.255.255.0"
"10.0.0.0/255.0.0.0"
```

#### ipv6-netmask

IPv6 address with netmask.

**Valid Input Format:**
- Must be a string
- Format: "ipv6_address/netmask"
- Both parts must be valid IPv6 addresses
<!-- vale off -->
**Valid Examples:**

```
"2001:db8::/ffff:ffff::"
"2001:db8:85a3::8a2e:370:7334/ffff:ffff:ffff:ffff::"
```

### MAC and Related Addresses

#### mac

MAC address format.

**Valid Input Format:**
- Must be a string
- Format: "XX:XX:XX:XX:XX:XX"
- Each X must be a hexadecimal digit (0-9, A-F, a-f)

**Valid Examples:**

```
"00:11:22:33:44:55"
"AA:BB:CC:DD:EE:FF"
"aa:bb:cc:dd:ee:ff"
```

#### clock-id

PTP clock ID format.

**Valid Input Format:**
- Must be a string
- Format: "XX:XX:XX:XX:XX:XX:XX:XX"
- Each X must be a hexadecimal digit (0-9, A-F, a-f)

**Valid Examples:**

```
"00:11:22:33:44:55:66:77"
"AA:BB:CC:DD:EE:FF:00:11"
```

#### es-identifier

Ethernet Segment Identifier format.

**Valid Input Format:**
- Must be a string
- Format: "XX:XX:XX:XX:XX:XX:XX:XX:XX:XX"
- Each X must be a hexadecimal digit (0-9, A-F, a-f)

**Valid Examples:**

```
"00:11:22:33:44:55:66:77:88:99"
"AA:BB:CC:DD:EE:FF:00:11:22:33"
```

#### segment-identifier

Ethernet Segment Identifier format (Type-0).

**Valid Input Format:**
- Must be a string
- Format: "00:XX:XX:XX:XX:XX:XX:XX:XX:XX"
- Must start with "00:"
- Each X must be a hexadecimal digit (0-9, A-F, a-f)

**Valid Examples:**

```
"00:11:22:33:44:55:66:77:88:99"
"00:AA:BB:CC:DD:EE:FF:00:11:22"
```

### BGP Related Formats

#### route-distinguisher

Route distinguisher format.

**Valid Input Format:**
- Must be a string
- Three types supported:
  1. Type 0: "ASN:NN" (2-byte ASN:4-byte number)
  2. Type 1: "IP:NN" (4-byte IP:2-byte number)
  3. Type 2: "ASN:NN" (4-byte ASN:2-byte number)

**Valid Examples:**

```
"65000:1"
"192.168.1.1:1"
"98765654:99"
```

#### route-target

Route target format.

**Valid Input Format:**
- Must be a string.
- Three types supported:
  1. "ASN:NN" (2-byte ASN:4-byte number)
  2. "IP:NN" (4-byte IP:2-byte number)
  3. "ASN:NN" (4-byte ASN:2-byte number)

**Valid Examples:**

```
"65000:1"
"192.168.1.1:1"
"65000:99999999"
```

#### well-known-community

Well-known BGP community values.

**Valid Input Format:**
- Must be one of:
  - "local-as"
  - "no-advertise"
  - "no-export"
  - "internet"
  - "additive"

#### community

BGP community format.

**Valid Input Format:**
- Must be a string
- Format: "NN:NN"
- Each NN must be a 16-bit number (0-65535)

**Valid Examples:**

```
"65000:1"
"100:1"
"65535:65535"
```

#### large-community

BGP large community format.

**Valid Input Format:**
- Must be a string
- Format: "NN:NN:NN"
- Each NN must be a 32-bit number

**Valid Examples:**

```
"65000:1:1"
"100:1:1"
"4294967295:4294967295:4294967295"
```

#### bgp-regex

BGP regex pattern format.

**Valid Input Format:**
- Must be a string
- Can contain digits, underscores, colons, dots, and special regex characters
- Cannot start with '*'
- Must contain at least one special character
- Cannot contain certain invalid regex patterns

**Valid Examples:**

```
"^[0-9]+$"
```

### Other Network Formats

#### ip-port-range

IP port range format.

**Valid Input Format:**
- Must be a string
- Format: "start-end"
- Both numbers must be 16-bit (0-65535)
- Start must be less than or equal to end

**Valid Examples:**

```
"1-65535"
"80-443"
"1024-2048"
```

#### vlan-range

VVLAN range format.

**Valid Input Format:**
- Must be a string
- Format: "start-end"
- Both numbers must be between 1-4095
- Start must be less than or equal to end

**Valid Examples:**

```
"1-4095"
"100-200"
"1000-2000"
```

#### asn-range

ASN range format.

**Valid Input Format:**
- Must be a string
- Comma-separated list of numbers
- Each number must be a valid ASN (0-4294967295)

**Valid Examples:**

```
"65000,65001"
"65000,65001,65002"
"4294967295"
```

#### evpn-route

EVPN route format.

**Valid Input Format:**
- Must be a string
- Format varies by route type (1-5)
- Type 1: [RD]:[1]:[ethtag]:[esi]:[ip]:[frag-id]
- Type 2: [RD]:[2]:[ethtag]:[mac] or [RD]:[2]:[ethtag]:[mac]:[ip]
- Type 3: [RD]:[3]:[ethtag]:[ip]
- Type 4: [RD]:[4]:[esi]:[ip]
- Type 5: [RD]:[5]:[ethtag]:[prefix]

**Valid Examples:**

```
"[27.0.0.3:2]:[1]:[0]:[03:44:38:39:ff:ff:01:00:00:01]:[::]:[0]"
"[27.0.0.3:2]:[2]:[0]:[00:02:00:00:00:07]"
"[27.0.0.3:10]:[3]:[0]:[27.0.0.3]"
"[27.0.0.5:3]:[4]:[03:44:38:39:ff:ff:01:00:00:01]:[27.0.0.5]"
"[27.0.0.21:15]:[5]:[0]:[83.2.1.0/24]"
```

### System and Command Formats

#### command-path

Command path format.

**Valid Input Format:**
- Must be a string
- Path components separated by '/'
- Cannot start with '//'
- Cannot contain spaces
- Cannot contain consecutive '//'

**Valid Examples:**

```
"/interface"
"/interface/*/"
"/interface/link"
```

### General Name and ID Formats

#### json-pointer

JSON pointer format.

**Valid Input Format:**
- Must be a valid JSON pointer string
- Must follow JSON pointer syntax rules

**Valid Examples:**

```
"/foo/bar"
"/foo/0"
"/foo/bar/baz"
```

#### integer

Integer format.

**Valid Input Format:**
- Must be a valid integer or integer range
- Can use range expansion syntax.

**Valid Examples:**

```
123
"1-5"
"1,2,3"
```

#### number

Numerical value format.

**Valid Input Format:**

Must be a valid integer or floating-point number.

**Valid Examples:**

```
"123"
123.45
-123
"-123.45"
```

#### float

Floating-point number format.

**Valid Input Format:**

Must be a valid integer or floating-point number.

**Valid Examples:**

```
"123"
123.45
-123
"-123.45"
```

#### oid

OID (Object Identifier) format.

**Valid Input Format:**
- Must be a string
- Must start and end with a digit
- Can contain digits and dots
- No consecutive dots allowed

**Valid Examples:**

```
"1.2.3.4"
"1.3.6.1.2.1"
"1.2.3.4.5"
```

#### snmp-branch

SNMP MIB tree branch format.

**Valid Input Format:**
- Must be a string
- Must start with optional dot
- Must start and end with a digit
- Can contain digits and dots
- No consecutive dots allowed

**Valid Examples:**

```
"1.2.3"
".1.2.3"
"1.2.3.4"
```

#### instance-name

Generic instance name format.

**Valid Input Format:**
- Must be a string
- Must start with a letter
- Can contain letters, numbers, and underscores
- Cannot be a reserved name

**Valid Examples:**

```
"instance1"
"my_instance"
"test123"
```

#### item-name

Generic item name format.

**Valid Input Format:**
- Must be a string
- Must start with a letter or number
- Can contain letters, numbers, underscores, and hyphens
- Cannot be a reserved name

**Valid Examples:**

```
"item1"
"my-item"
"test_123"
```

#### generic-name

Generic name format.

**Valid Input Format:**
- Must be a string
- Must start with a letter
- Can contain letters, numbers, underscores, and hyphens
- Cannot be a reserved name

**Valid Examples:**

```
"name1"
"my-name"
"test_123"
```

#### bridge-name

Bridge name format.

**Valid Input Format:**
- Must follow instance-name format rules
- Must start with a letter
- Can contain letters, numbers, and underscores
- Cannot be a reserved name

**Valid Examples:**

```
"bridge1"
"my_bridge"
"test123"
```

#### vrf-name

VRF name format.

**Valid Input Format:**
- Must follow generic-name format rules
- Must start with a letter
- Can contain letters, numbers, underscores, and hyphens
- Cannot be a reserved name

**Valid Examples:**

```
"vrf1"
"my-vrf"
"test_123"
```

#### ptp-port-id

PTP port ID format.

**Valid Input Format:**

- Must be a string
- Format: "clock-id-port-number"
- clock-id must be valid clock ID format
- port-number must be 2 bytes in hex format

**Valid Examples:**

```
"00:11:22:33:44:55:66:77-01:02"
"AA:BB:CC:DD:EE:FF:00:11-02:03"
```

#### sequence-id

PTP sequence ID format.

**Valid Input Format:**
- Must be a string
- Format: "start-end"
- start must be 8-bit (0-255)
- end must be 32-bit (0-4294967295)

**Valid Examples:**

```
"1-65535"
"0-4294967295"
"100-200"
```

#### integer-id

Integer ID format.

**Valid Input Format:**
- Must be a string
- Must be a positive integer
- Cannot start with 0 (zero)

**Valid Examples:**

```
"1"
"123"
"999999"
```

#### profile-name

Profile name format.

**Valid Input Format:**
- Must be a string
- Must start with a letter
- Can contain letters, numbers, underscores, and hyphens
- Cannot be a reserved name

**Valid Examples:**

```
"profile1"
"my-profile"
"test_123"
```

#### idn-hostname

Internationalized domain name hostname format.

**Valid Input Format:**
- Must be a string
- Must follow IDN hostname rules
- Must be properly encoded
- Cannot contain invalid characters

**Valid Examples:**

```
"example.com"
"test.example.com"
```
