---
title: CLI Configuration
author: NVIDIA
weight: 290
toc: 3
---
Cumulus Linux provides several options to configure the CLI; you can set a CLI session timeout, and enable and configure the pager.

## Set the CLI Session Timeout

To reduce the window of opportunity for unauthorized user access to an unattended CLI session on the switch, or to end an inactive session and release the resources associated with it, set the CLI session to exit after a certain amount of idle time.

{{< tabs "15 ">}}
{{< tab "NVUE Command ">}}

Run the `nv set system cli inactive-timeout <seconds>` command. You can set the CLI session timeout to a value between 0 and 86400 minutes. The default value is 0 (disabled).

```
cumulus@switch:~$ nv set system cli inactive-timeout 300
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Command ">}}

In the `/etc/profile.d/nvue_cli.sh` file, add the `TMOUT` value in seconds:

```
cumulus@switch:~$ sudo nano /etc/profile.d/nvue_cli.sh
...
readonly TMOUT=18000
export TMOUT
```

{{< /tab >}}
{{< /tabs >}}

To show the configured CLI session timeout, run the command:

```
cumulus@switch:~$ nv show system cli 

```

## Configure the CLI Pager

The CLI pager enables you to view the contents of a file or the output of a command one page at a time in the terminal window, using the up and down arrow keys or the space bar.

To configure the CLI pager, set the pager state and the pager options.

- You can set the pager state to `enabled`, `disabled`, or `auto`. The default value is `auto`.
- You can set the pager options to `more`, `less`, or `vim`. The default value is `less`.

{{< tabs "48 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system cli pagination state enabled
cumulus@switch:~$ nv set system cli pagination pager more
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Command ">}}

Edit the `NVUE_PAGINATE` and the `NVUE_PAGER` values in the `/etc/profile.d/nvue_cli.sh` file.

```
cumulus@switch:~$ sudo nano /etc/profile.d/nvue_cli.sh
...
export NVUE_PAGINATE=on
export NVUE_PAGER=more
```

{{< /tab >}}
{{< /tabs >}}

## Show CLI Settings

To show the current CLI settings, run the `nv show system cli` command:

```
cumulus@switch:~$ nv show system cli
                  applied
----------------  -------
inactive-timeout  12000  
pagination               
  state           enabled
  pager           more
```

To show the configured pager options only, run the `nv show system cli pagination` command:

```
cumulus@switch:~$ nv show system cli pagination
       applied
-----  -------
state  enabled
pager  more
```
