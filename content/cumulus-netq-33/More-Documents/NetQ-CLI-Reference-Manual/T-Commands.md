---
title: T through Z Commands
author: Cumulus Networks
weight: 1107
toc: 3
right_toc_levels: 2
pdfhidden: true
draft: true
---
This topic includes all commands that begin with `netq t*`, `netq u*`, `netq v*`, `netq w*`, `netq x*`, `netq y*`, and `netq z*`.

## netq trace

    <ip>   :  IPv4 or v6 address (no mask)
    <mac>  :  MAC address

- - -

--------------------------


## Configuration Commands

All of the NetQ configuration commands begin with netq config.
They are described here in alphabetical order by component group:
Add-on Configuration Commands
Agent Configuration Commands
Parser
Server
Telemetry Server

### Add-on Configuration Commands

netq config (add|del) addons
Installs or removes all additional software components available with a given release. [in a particular directory?]
Syntax
netq config add addons
netq config del addons
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
	None
Run From
	Telemetry server, leaf, spine, host?
Command History
	
Release
Description
1.0
Introduced

Usage Guidelines
Sample Usage
Related Commands




### NetQ Agent Configuration Commands

netq config (add|del) agent (stats|sensors)
Installs or removes [Starts or stops? Enables or disables?] collection of statistics or sensor measurements by NetQ Agent on [all or specific node?].
Syntax
	netq config add agent stats
	netq config del agent stats
netq config add agent sensors
neq config del agent sensors
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
	None
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Starting statistical collection on agent node [check to see if it is running?]
cumulus@ts:~$ netq config add agent stats
Related Commands
Netq config add agent docker-monitor
Netq config add agent loglevel
Netq config add agent kubernetes-monitor

netq config add agent docker-monitor
Installs [Starts? Enables?] the Docker monitoring service on [all or specific node?].
Syntax
	netq config add agent docker-monitor [poll-period <text-duration-period>]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
poll-period
The amount of time to monitor a docker container for statistics collection. The <text-duration-period> value must be specified in [seconds, minutes, hours?]
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Set the monitoring duration of a docker container to one hour
cumulus@ts:~$ netq config add agent docker-monitor poll-period 3600
Related Commands
netq config add agent addons
netq config add agent loglevel
netq config add agent kubernetes-monitor

netq config add agent loglevel
Specifies the level of detail to display in the [system] log file[s?].
Syntax
	netq config add agent loglevel [debug|info|warning|error]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
debug
Display errors, warnings, and informational events the system receives or generates.
info
Display only informational events
warning
Display warnings and informational events
error
Display xxx
Run From
	Telemetry server, leaf, spine, host?
JSON Output
	Not applicable
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	If no level is specified, the xxx level is used by default.
Changing the logging level takes place immediately, but prior content is not removed. 
[add definition of errors, warnings and info--what is the criteria/differentiation between…]
Sample Usage
	Set the display level of the [system?] log file to capture xxx
cumulus@ts:~$ netq config add agent loglevel warning
Related Commands
netq config add agent addons
netq config add agent docker-monitor
netq config add agent kubernetes-monitor

netq config add agent kubernetes-monitor
Installs [Starts? Enables?] the Kubernetes monitoring service on [all or specific node?].
Syntax
	netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments	
poll-period
The amount of time to monitor a kubernetes container for statistics collection. The <text-duration-period> value must be specified in [seconds, minutes, hours?]
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Set the monitoring duration of a kubernetes container to one hour
cumulus@ts:~$ netq config add agent kubernetes-monitor poll-period 3600
Related Commands
netq config add agent addons
netq config add agent docker-monitor
netq config add agent loglevel

Parser Configuration Commands
Server Configuration Commands
Telemetry Server Configuration Commands



AGENT NOTIFIER COMMANDS

 netq config (add|del) experimental
   netq config (add|del) agent (stats|sensors)
   netq config reload parser
   netq config show server [json]
   netq config add server <ip-server>|<text-server-name> [port <1025-65535>] [vrf <text-vrf>]
   netq config add server <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  [vrf <text-vrf>]
   netq config del server
   netq config (start|stop|status|restart) agent
   netq config add agent loglevel [debug|info|warning|error]
   netq config del agent loglevel
   netq config show agent [kubernetes-monitor|loglevel|stats|sensors|frr-monitor|wjh|wjh-threshold|cpu-limit] [json]


   netq config (add|del) experimental
   netq config (add|del) addons
   netq config (add|del) agent (stats|sensors)
   netq config reload parser

   netq config show server [json]
   netq config add server <ip-server>|<text-server-name> [port <1025-65535>] [vrf <text-vrf>]
   netq config add server <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  [vrf <text-vrf>]
   netq config del server

   netq config (start|stop|status|restart) agent
   netq config add agent loglevel [debug|info|warning|error]
   netq config del agent loglevel
   netq config show agent [kubernetes-monitor|docker-monitor|loglevel|stats|sensors] [json]




   netq <hostname> show stp topology [around <text-time>] [json]
