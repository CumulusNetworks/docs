---
title: Cumulus User Experience - CUE
author: NVIDIA
weight: 115
toc: 3
---
CUE is a command line interface for Cumulus Linux.

TALK ABOUT OBJECT MODEL HERE

## Command Line Basics

BLABLABLA

### Command Line Structure

The CUE command line has a flat structure as opposed to a modal structure. This means that you can run all commands from the primary prompt instead of only in a specific mode.

### Command Syntax

CUE commands all begin with `cl` and fall into one of three syntax categories: configuration (set and unset), monitoring (show), and configuration management (config).

`cl set [options] <attribute>` and `cl unset [options] <attribute>`
`cl show [options] <attribute>`
`cl config <command> [options]`

### Command Completion

As you enter commands, you can get help with the valid keywords or options using the Tab key. For example, using Tab completion with `cl set` displays the possible objects for the command, and returns you to the command prompt to complete the command.

```
cumulus@switch:~$ cl set check <<press Tab>>
ridge     interface  nve        router     vrf
evpn       mlag       platform   system

cumulus@switch:~$ cl set
```

### Command Help

As you enter commands, you can get help with command syntax by entering `-h` or `--help` at various points within a command entry. For example, to find out what options are available for `cl set interface`, enter `cl set -h` or `cl set --help`.

```
cumulus@switch:~$ cl set interface -h
Usage:
cl set interface [options] <interface-id> ...

Description:
  Interfaces

Identifiers:
  <interface-id>    Interface

Revision Options:
  --rev <revision>  The revision id to operate on
  --pending         Alias of '--rev=pending'
  --applied         Alias of '--rev=applied'
  --startup         Alias of '--rev=startup'
  --running         Alias of '--rev=running'

General Options:
  -h, --help        Show help.
```

### Command History

The CLI stores commands issued within a session, which enables you to review and rerun commands that have already been run. At the command prompt, press the Up Arrow and Down Arrow keys to move back and forth through the list of commands previously entered. When you have found a given command, you can run the command by pressing Enter, just as you would if you had entered it manually. Optionally you can modify the command before you run it.

## Command Categories

While the CLI has a flat structure, the commands can be conceptually grouped into three functional categories:

- Configuration Commands
- Monitoring Commands
- Configuration Management Commands

### Configuration Commands

The CUE configuration commands modify switch configuration. You can set and unset configuration options.

The `cl set` commands are grouped into the following. Each command group includes subcommands.

cl set router [options] [<attribute> ...]
cl set platform [options] [<attribute> ...]
cl set bridge [options] [<attribute> ...]
cl set mlag [options] [<attribute> ...]
cl set evpn [options] [<attribute> ...]
cl set interface [options] <interface-id> ...
cl set system [options] [<attribute> ...]
cl set vrf [options] <vrf-id> ...
cl set nve [options] [<attribute> ...]

### Monitoring Commands

The CUE monitoring commands show various parts of the network configuration. For example, you can show the complete network configuration or BGP status. The monitoring commands are grouped into the following. Each command group includes subcommands.

cl show router [options] [<attribute> ...]
cl show platform [options] [<attribute> ...]
cl show bridge [options] [<attribute> ...]
cl show mlag [options] [<attribute> ...]
cl show evpn [options] [<attribute> ...]
cl show interface [options] [<interface-id> ...]
cl show system [options] [<attribute> ...]
cl show vrf [options] [<vrf-id> ...]
cl show nve [options] [<attribute> ...]

### Configuration Management Commands

The CUE configuration management commands manage and apply configurations.

| Command | Description |
| ------- | ----------- |
| cl config apply [options] [<revision>] | Applies the running configuration. The configuration is applied but not saved and does not persist after a reboot.|
| cl config save [options] | Saves the running configuration. The configuration persists after a reboot. |
| cl config replace [options] <cue-file> | Replaces the pending configuration with the specified file. |
| cl config detach [options] | Detaches the configuration from the current pending revision. |
| cl config diff [options] [(<revision>|--empty)] [<revision>] | Shows differences between two configuration revisions. |
| cl config patch [options] <cue-file> | Updates the pending revision with a configuration in a specified YAML file. |

To see the full set of CUE commands, run `cl list-commands`.
