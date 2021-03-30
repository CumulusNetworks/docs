---
title: TDR Cable Diagnostics
author: NVIDIA
weight: 433
---
Cumulus Linux 3.7.9 and later provides the Time Domain Reflectometer (TDR) cable diagnostic tool, which enables you to isolate cable faults on unshielded twisted pair (UTP) cable runs.

{{%notice note%}}

- TDR is supported on the EdgeCore AS4610 switch.
- In Cumulus Linux 3.7.12 and later, TDR is also supported on the Dell N3248PXE switch.
- Pluggable modules are not supported.

{{%/notice%}}

## Run Cable Diagnostics

Cumulus Linux TDR runs, checks, and reports on the status of the cable diagnostic circuitry for specified ports.

{{%notice warning%}}

Running TDR is disruptive to an active link; If the link is up on an enabled port when you start diagnostics, the link is brought down, then brought back up when the diagnostics are complete.

{{%/notice%}}

{{%notice note%}}

To obtain the most accurate results, make sure that auto-negotiation is enabled on both the switch port and the link partner (for fixed copper ports, auto-negotiation is enabled by default in Cumulus Linux and cannot be disabled).

{{%/notice%}}

To run cable diagnostics and report results, issue the `cl-tdr <port-list>` command. You must have root permissions to run the command. Because the test is disruptive, a warning message displays and you are prompted to continue.

The following example command runs cable diagnostics on swp39:

```
cumulus@switch:~$ sudo cl-tdr swp39

Time Domain Reflectometer (TDR) diagnostics tests are disruptive.
When TDR is run on an interface, it will cause the interface to
go down momentarily during the test. The interface will be restarted
at the conclusion of the test.

The following interfaces may be affected:
swp39

Are you sure you want to continue? [yes/NO]yes
swp39 current results @ 2019-08-05 09:37:53 EDT
      cable(4 pairs)
      pair A Ok, length 15 meters (+/-10)  
      pair B Ok, length 15 meters (+/-10)
      pair C Ok, length 17 meters (+/-10)
      pair D Ok, length 13 meters (+/-10)
```

## Command Options

The `cl-tdr` command includes several options, described below:

| Option<img width=300/> | Description <img width=600/>|
|------------------------|-----------------------------|
| `-h` | Displays this list of command options. |
| `-d <delay>` | The delay in seconds between diagnostics on different ports when you run the command on multiple ports. You can specify 0 through 30 seconds. The default is 2 seconds. |
| `-j` | Displays diagnostic results in JSON format. |
| `-y` | Proceeds automatically without the warning or prompt. |

## Example Commands

The following command runs diagnostics on ports swp39, swp40, and swp32 and sets the delay to one second:

```
cumulus@switch:~$  sudo cl-tdr swp39-40,swp32 -d 1
```

The following command example runs diagnostics on swp39 and reports the results in json format:

```
cumulus@switch:~$  sudo cl-tdr swp39 -j
```

The following command runs diagnostics on ports swp39 and swp40 without displaying the warning or prompting to continue:

```
cumulus@switch:~$   sudo cl-tdr swp39-40 -y
```

## Understanding Diagnostic Results

The TDR tool reports diagnostic test results per pair for each port. For example:

```
 swp39 current results @ 2019-08-05 09:37:53 EDT
      cable(4 pairs)
      pair A Ok, length 15 meters (+/-10)  
      pair B Ok, length 15 meters (+/-10)
      pair C Ok, length 17 meters (+/-10)
      pair D Ok, length 13 meters (+/-10)
```

Possible cable pair states are as follows:

| State| Description|
|------|------------|
| `Ok` | No cable fault is detected. |
| `Open` | A lack of continuity is detected between the pins at each end of the cable. |
| `Short` | A short-circuit is detected on the cable. |
| `Open/Short` | Either a lack of continuity between the pins at each end of the cable or a short-circuit is detected on the cable. |
| `Crosstalk` | A signal transmitted on one pair is interfering with and degrading the transmission on another pair. |
| `Unknown` | An unknown issue is detected. |

Per pair cable faults are detected within plus or minus 5 meters. Good cable accuracy is detected within plus or minus 10 meters.

## Cable Diagnostic Logs

Cable diagnostic results are also logged to the `/var/log/switchd.log` file. For example:

```
2019-08-05T10:02:30.691513-04:00 act-4610p-53 switchd[3037]: hal_bcm_port.c:3495 swp39 Enhanced Cable Diagnostics (TDR) started
2019-08-05T10:02:31.466523-04:00 act-4610p-53 switchd[3037]: hal_bcm_port.c:3446 swp39 TDR state=Ok npairs=4 +/- 10
2019-08-05T10:02:31.468735-04:00 act-4610p-53 switchd[3037]: hal_bcm_port.c:3449 swp39 TDR pair A state=Ok len=17
2019-08-05T10:02:31.471958-04:00 act-4610p-53 switchd[3037]: hal_bcm_port.c:3453 swp39 TDR pair B state=Ok len=18
2019-08-05T10:02:31.475047-04:00 act-4610p-53 switchd[3037]: hal_bcm_port.c:3457 swp39 TDR pair C state=Ok len=18
2019-08-05T10:02:31.477109-04:00 act-4610p-53 switchd[3037]: hal_bcm_port.c:3461 swp39 TDR pair D state=Ok len=15
```
