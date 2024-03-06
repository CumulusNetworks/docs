---
title: help
author: NVIDIA
weight: 1103
toc: 3
right_toc_levels: 1
pdfhidden: true
type: nojsscroll
---

## netq help

Displays the syntax for all commands or ones containing a particular keyword, a list of all commands and options, or a summary of command formatting.

### Syntax

```
netq help [<text-keywords>]
netq help list
netq help verbose
```

### Required Arguments

| Argument | Value | Description |
| ---- | ---- | ---- |
| list | NA | Display all NetQ commands in the terminal window |
| verbose | NA | Display NetQ command formatting rules |

### Options

| Option | Value | Description |
| ---- | ---- | ---- |
| NA | \<text-keywords\> | Display syntax for commands with these keywords |

### Sample Usage

<!--need updated example-->

Display syntax for all commands with the `agent` keyword:

```
cumulus@switch:~$ netq agent help OR netq help agent
Commands:
    netq check agents [label <text-label-name> | hostnames <text-list-hostnames>] [include <agent-number-range-list> | exclude <agent-number-range-list>] [around <text-time>] [json]
    netq show unit-tests agent [json]
    netq config (add|del) agent (stats|sensors)
```

Display the NetQ command format rules:

```
cumulus@netq-ts:~$ netq help verbose

netq commands have the following format:
    netq [<hostname>] action object [options]

[] denotes an optional parameter or keyword
<> denotes a parameter to be specified such as an IP prefix, addr etc.

Hitting the TAB key will automatically show the available options.
Partial keywords are also accepted; e.g.: 'netq show ip ro 4.0.0.1'.
...
```

### Related Commands

None
