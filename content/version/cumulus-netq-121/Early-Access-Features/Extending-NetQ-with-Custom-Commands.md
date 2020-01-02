---
title: Extending NetQ with Custom Commands
author: Cumulus Networks
weight: 75
aliases:
 - /display/NETQ121/Extending+NetQ+with+Custom+Commands
 - /pages/viewpage.action?pageId=8356588
pageID: 8356588
product: Cumulus NetQ
version: 1.2.1
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
---
NetQ provides the ability to codify playbooks and extend NetQ with
custom commands for use cases specific to your network.

The summary of steps required to do this is a follows:

  - The extensions must be written in [Python](https://www.python.org)
    or [Cython](http://cython.org).

  - The commands need to be added must use `network doctopt`.

  - The .py file (or the compiled .so if using Cython) is now copied to
    /usr/lib/python2.7/dist-packages/netq\_apps/modules/addons.

  - Enable the add-ons with the `netq config add addons` command

  - Check that your command works by typing `netq <TAB>`

## Sample File with Custom Command</span>

To help you get started, here is the Hello World of NetQ command
extension:

    '''
    hello: A netq app hello world module
    Usage:
       netq hello [json]
    Options:
       hello                          : Hello world experimental
    '''
    import json
    from netq_apps.modules import NetqModule, RC_SUCCESS, RC_FAIL
    app = NetqModule()
    
    @app.route('hello')
    def cli_hello_world(cli, netq):
        '''My very own hello'''
        jsonify = cli.get('json')
        if jsonify:
           print json.dumps({'greeting': 'Hello World'})
        else:
           print 'Hello World'
        return RC_SUCCESS

Let's break down each part of the code.

### Command Specification With Help</span>

The lines at the start of the file within the triple quotes (''')
constitute what is called the *docstring* of the file or module.
`network-docopt`, the Python library that builds the command parser for
NetQ, uses the information provided in the *docstring*. Specifically,
everything between **Usage** and **Options** is considered a command
specification. In this case, `netq hello` is the only command specified
in the file. The command MUST start with the word `netq`. Every `netq`
command follows the following structure:

    netq [<hostname>] <verb> <object> <filters>

For example, here is the sample for `show vlan`:

    netq [<hostname>] show vlan [<1-4096>] [around <text-time>] [json] 

The *\<hostname\>* option is used to filter results to just the
specified host; hostname can also be a regular expression. The
*\<verb\>* is *show*, the *\<object\>* is *vlan* and the remaining
parameters are filters to viewing the data.

For example, if you wanted to extend hello world by passing an optional
greeting, modify the usage to be:

    netq hello <text-greeting>

`network-docopt` understands a few parameter types and validates them
before passing them to your code. Some common ones are:

  - **\<hostname\>**: A host known to NetQ

  - **\<remote-interface\>**: An interface on the specified host known
    to NetQ

  - **\<text\>**: Any free text, but has to be a single word or
    delimited within quotes

  - **\<ip\>**, **\<ip/prefixlen\>**: IPv4 or IPv6 address, with prefix
    length in the second case

  - **\<ipv4\>**, **\<ipv4/prefixlen\>**: IPv4 address, with prefix
    length in the second case

  - **\<ipv6\>**, **\<ipv6/prefixlen\>**: IPv6 address, with prefix
    length in the second case

  - **\<wildcard\>**: All the remaining text

  - Valid number range: Such as **\<1-4096\>** to limit the allowed
    range

So in the VLAN example above, specifying a VLAN value outside the 1-4096
range results in an error, with command unknown and a help message
indicating that you need to specify a value between 1 and 4096. For
hosts and interfaces used with *\<hostname\>* and
*\<remote-interface\>*, NetQ automatically provides tab completion.

To display meaningful help associated with a keyword, add the help for
the command via the **Options** section. In the example code above, the
object *hello* has the help text "Hello world experimental". This text
is displayed when the user types `netq <TAB>`, as shown in the following
example:

    cumulus@switch:~$ netq 
    <hostname> : Type first char of netq host for dynamic completion
    check : Perform fabric-wide checks
    config : Configuration
    example : Show examples of usage and workflow
    hello : Hello world experimental
    help : Show usage info
    resolve : Annotate input with names and interesting info
    show : Show fabric-wide info about specified object
    trace : Control Path Trace
    cumulus@torc-11:mgmt-vrf:~$ netq

{{%notice note%}}

Any help you provide here overrides the help provided for the keyword by
a module loaded previously.

{{%/notice%}}

### Associating the Command with the Function</span>

After configuring the command, you need to associate or *bind* that
command with the function to be called when a user runs the command.
This is done by using decorators to functions similar to how other CLI
builders or web servers work.

First, create an instance of the class `NetqModule()` called *app*. Then
associate the function to the appropriate command via the decorator
`@app.route`. As shown in the example above, the function
`cli_hello_world()` is decorated to indicate that it is the function to
call for the command `hello`. The function takes two parameters: *cli*
and *netq*. Usage of these parameters is discussed in the next section.

Keep in mind the following when matching the command to the function:

  - If a prior binding has already been assigned to a command, the newer
    binding will fail. By default, modules in the core NetQ code take
    precedence over early access modules, which take precedence over the
    modules defined in addons directory.

  - The command string can be as small as possible. For example, the
    commands `netq hello json` and `netq hello` can be handled by
    different functions or by the same function. The NetQ command parser
    does a longest match first to determine which of the competing
    functions is assigned to execute a command. The command parser
    supports up to three string matches. In other words, `show ip
    address` is supported, but `show ip address json` is not. Such
    longer command strings bound to a function either silently fail or a
    shorter string version is matched.

### Using the cli and netq Parameters</span>

The function that is called to execute a command expects to received two
parameters, *cli* and *netq*, in the order shown in the example above.

*cli* is a dictionary containing the parameters provided by the user on
the command line. *netq* contains the timestamps provided by the user,
if any. Any other object within NetQ can be ignored. The timestamps are
provided to query NetQ objects around a specific time or in a time
window.

The example shows how to extract the value provided by the user at the
command line from *cli*. Since *json* is a keyword, getting the key
*json* from *cli* lets you to determine if the user specified *json* at
the command line or not. If the user did not specify *json* at the
command line, `cli.get('json')` returns *None*, whereas if the user did
specify *json*, then `cli.get('json')` returns the string "json". Thus,
if the user wants to specify a parameter along with a keyword, for
example, as shown in `netq show macs [vlan <1-4096>]`, then the value of
the VLAN to search for a MAC address can be found using
`cli.get('<1-4096>')`, not via `cli.get('vlan')`.

### Return Values</span>

The function returns either *RC\_SUCCESS* if successful or *RC\_FAIL* if
not. The code snippet shows how to import these values from the standard
NetQ libraries.

## Querying the NetQ Database</span>

While the code snippet above was sufficient to illustrate the general
skeleton, if you want to extend the commands, you typically will want to
add meaningful functionality such as querying the database and
displaying some more meaningful information. For example, consider a new
command called `show ip-routes`, which displays the route information
available in the database, but with a different set of fields than shown
via `show ip routes`. The code to do so is shown below.

    """
    routes.py: NetQ app module for processing IPv4/v6 routes
    Usage:
       netq <hostname> show myroutes [vrf <vrf>] [json]
    Options:
       myroutes                               : IPv4/v6 routes
    """
    from __future__ import absolute_import
    from collections import OrderedDict
     
    from netq_apps.modules import NetqModule, RC_SUCCESS
    from netq_apps.cmd.netq import netq_show
     
    from netq_lib.orm.redisdb.models import Route
     
    app = NetqModule()
     
    @app.route('show myroutes')
    @netq_show
    def cli_show_myroutes(cli, netq, context):
        '''MY very own show routes'''
        hostname = cli.get('<hostname>') or '*'
        vrf = cli.get('<vrf>') or '*'
        context.col_sizes = [16, 8, 32, 26, 16]
        entries = Route.query.filter(timestamp=netq.start_time,
                                     endtimestamp=netq.end_time,
                                     hostname=hostname, vrf=vrf)
        for entry in entries:
            out = OrderedDict()
            if isinstance(entry, tuple):
                route = entry[0]
            else:
                route = entry
            if not route.nexthops:
                route.nexthops = [['None', 'Local']]
            nexthops = ', '.join(
                '%s: %s' % (nh[0], nh[1]) if nh[0] != 'None' else '%s' % nh[1]
                for nh in sorted(route.nexthops)
            )
     
            out['Hostname'] = route.hostname
            out['Protocol'] = route.protocol
            out['Prefix'] = route.prefix
            out['Nexthops'] = nexthops
            out['Last Changed'] = route.timestamp
            yield out

Much of this code is similar to the hello world example, but the new
items are discussed below.

### The Imports</span>

There are two additional imports, one for *netq\_show* and the other for
*Route*.

#### netq\_show</span>

*netq\_show* is the decorator that takes care of wrapping the output in
a format native to NetQ. For example, it generates the JSON for you
automatically, so that you don't have to write a JSON output generator
just to support JSON and you don't have to worry about supporting the
tabular format, displaying rotten nodes in a different color and so on.
All you have to do is generate output in the form of an `OrderedDict`
and `yield` for every entry. The `OrderedDict` ensures that the columns
are displayed in the order provided in the code. The column headers are
generated from the dictionary key, as are the JSON keys.

By wrapping the code with the *netq\_show*, all these display
complexities are covered for you.

#### Route</span>

*Route* is the database object that holds all the pertinent information
about a route. Its contents are defined in the
`/usr/lib/python2.7/dist-packages/netq_lib/orm/redisdb/models.py` file.
There are other database objects defined in the file, but this example
only involves the *Route* object.

### The Function Handler</span>

The function that satisfies the command `show myroutes` is
*cli\_show\_myroutes*, and because of the decorator, takes an additional
input parameter, *context*. It's mainly used to pass things between the
main NetQ command module and the specific modules, such as this one.
This particular case uses the *context* to update the column sizes to be
used in the display.

### The Query Functions</span>

The meat of the code is the query. Objects are queried using the model
of *\<object\>.query.\<query function\>. T*his particular example uses
*filter* as the query function, as shown by the `Route.query.filter()`
call. The filter function produces output filtered by the parameters
specified in the keyword arguments passed. For example, the *hostname*
keyword argument restricts the results returned by the query function to
only those on the specified host. The list of keys that can be specified
for an object are listed under the object's definition in the
aforementioned `models.py` file under the function `key_fmt()`. A look
at that function for the *Route* object shows that the key fields are:
hostname, prefix, route type, routing table id, ipv4/v6 route and, If
the entry is originated on this node, the protocol that added this route
and the VRF name qualifier. The values returned include all the key
fields plus the fields shown in the `val_fmt()` function for the object.

The other useful query functions are:

  - `query.get()`: which returns just the first element matching the
    parameters specified.

  - `query.latest()`: which returns the latest element matching the
    parameters specified, and does not take any time parameters.

  - `query.count()`: which returns a count of the matching elements
    instead of the elements themselves.

The filter query functions return an iterator and thus is lazy about
retrieving data from the back end. You can stop whenever you want in the
iteration. `query.get()` and `query.latest()` both return a single
object of the type the query is on while `query.count()` returns an
integer.

## Debugging</span>

Inevitably when writing code, coding errors need to be debugged and the
fixes tried again. When a module doesn't load or returns an error, it is
reported in the `netqd.log`, usually kept under `/var/log` (unless you
modified the location). Deploying the module on one node doesn't mean it
is automatically available on all nodes. You must copy it to all the
required nodes.

To reload the modules after making fixes, run the command `netq config
reload parser`.

## Caveats</span>

This feature is an early access feature, and must be treated as such.
There may be obscure failures which will require Cumulus Networks
engineering intervention to investigate. Finally, please save the
modules you write. If you reinstall the `netq-apps` package, your
modules may get overwritten when you install the new package. One of the
next releases of NetQ should provide the ability to store these modules
under `/usr/local/lib`, to keep them from being affected by package
management.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
