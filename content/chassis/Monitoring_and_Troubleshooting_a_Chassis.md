---
title: Monitoring and Troubleshooting a Chassis
author: Cumulus Networks
weight: 17
aliases:
 - /display/CHASSIS/Monitoring+and+Troubleshooting+a+Chassis
 - /pages/viewpage.action?pageId=7113871
pageID: 7113871
product: Cumulus Chassis
version: '1.0'
imgData: chassis
siteSlug: chassis
---
Typically you use [standard
methods](/display/CHASSIS/Monitoring+and+Troubleshooting) to monitor and
troubleshoot the chassis. However, some commands work a little
differently and there are some chassis-specific commands you can
utilize. Those differences are discussed in this chapter.

## <span>Using the sensors Command</span>

The `sensors` command displays data from all the sensors in the chassis.
The bmcd daemon gathers this data from the local node, remote nodes, and
for Backpack chassis, the attached BMC and CMM. Data for every sensor in
the chassis is available on every card.

Data that applies to the whole chassis, such as fan speeds, is prefixed
with `chassis`:

    ...
     
    chassis:Fan14Front-virtual-0
    Adapter: Virtual device
    Fan14 Front: 7200 RPM
     
    ... 

Otherwise, data is gathered for each specific line card and fabric card:

    ...
     
    fc301:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc202:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.0°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc701:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc701 lm75b_temp:  +25.0°C  
     
    fc201:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc201 lm75c_temp:  +27.0°C  
     
    ...

{{%notice note%}}

Cumulus Linux has read-only access to sensor information. Cumulus Linux
can still see temperature, PSU status and so forth, but it can’t change
any settings. You need to change these settings directly through the
BMC.

{{%/notice%}}

### <span>Example sensors Output</span>

Here is the complete output, which is about 1200 lines long:

Click to see output of the sensors command...

    cumulus@omp-800-fc402:~$ sensors
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
     
    jc42-i2c-0-19
    Adapter: SMBus I801 adapter at f000
    temp1:        +23.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    jc42-i2c-0-1a
    Adapter: SMBus I801 adapter at f000
    temp1:        +23.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan14Front-virtual-0
    Adapter: Virtual device
    Fan14 Front: 7200 RPM
     
    lc102:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc102 lm75b_temp:  +30.0°C  
     
    lc301:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc301 lm75b_temp:  +25.0°C  
     
    lc102:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +28.0°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc302:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc302:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc302 lm75b_temp:  +29.0°C  
     
    lc401:asic_temp-virtual-0
    Adapter: Virtual device
    lc401 asic_temp:  +37.0°C  
     
    lc802:cpu_temp-virtual-0
    Adapter: Virtual device
    lc802 cpu_temp:  +19.0°C  
     
    lc401:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc602:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc602 lm75a_temp:  +20.0°C  
     
    lc302:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +27.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc301:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc301:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc202:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.0°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc701:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc701 lm75b_temp:  +25.0°C  
     
    fc201:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc201 lm75c_temp:  +27.0°C  
     
    chassis:Fan10Front-virtual-0
    Adapter: Virtual device
    Fan10 Front: 7000 RPM
     
    lc701:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc701 lm75a_temp:  +20.0°C  
     
    lc702:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +22.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +22.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc401:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc401 lm75d_temp:  +21.0°C  
     
    fc401:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
     
    chassis:Fan11Rear-virtual-0
    Adapter: Virtual device
    Fan11 Rear:  7100 RPM
     
    lc502:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +27.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc102:asic_temp-virtual-0
    Adapter: Virtual device
    lc102 asic_temp:  +43.0°C  
     
    lc501:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc501 lm75d_temp:  +21.0°C  
     
    lc801:asic_temp-virtual-0
    Adapter: Virtual device
    lc801 asic_temp:  +38.0°C  
     
    lc402:cpu_temp-virtual-0
    Adapter: Virtual device
    lc402 cpu_temp:  +17.0°C  
     
    fc201:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc201 lm75b_temp:  +27.0°C  
     
    fc302:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc302 lm75d_temp:  +22.0°C  
     
    lc602:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc602 lm75d_temp:  +25.0°C  
     
    lc401:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +15.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +14.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +14.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc301:asic_temp-virtual-0
    Adapter: Virtual device
    fc301 asic_temp:  +42.0°C  
     
    lc102:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +28.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc302:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc302 lm75a_temp:  +21.0°C  
     
    fc202:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc202 lm75b_temp:  +28.0°C  
     
    lc302:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc201:asic_temp-virtual-0
    Adapter: Virtual device
    lc201 asic_temp:  +37.0°C  
     
    lc201:cpu_temp-virtual-0
    Adapter: Virtual device
    lc201 cpu_temp:  +17.0°C  
     
    chassis:Fan1Rear-virtual-0
    Adapter: Virtual device
    Fan1 Rear:   7100 RPM
     
    lc701:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc202:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +27.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan7Front-virtual-0
    Adapter: Virtual device
    Fan7 Front:  7100 RPM
     
    lc302:asic_temp-virtual-0
    Adapter: Virtual device
    lc302 asic_temp:  +37.0°C  
     
    chassis:Fan4Front-virtual-0
    Adapter: Virtual device
    Fan4 Front:  7000 RPM
     
    lc702:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc702 lm75c_temp:  +27.0°C  
     
    lc202:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc202 lm75d_temp:  +24.0°C  
     
    lc301:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc301 lm75a_temp:  +20.0°C  
     
    lc601:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc601 lm75c_temp:  +28.0°C  
     
    lc101:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +25.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc102:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc102 lm75c_temp:  +26.0°C  
     
    lc401:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc502:cpu_temp-virtual-0
    Adapter: Virtual device
    lc502 cpu_temp:  +17.0°C  
     
    lc702:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc702 lm75b_temp:  +28.0°C  
     
    lc301:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc301 lm75d_temp:  +21.0°C  
     
    lc301:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc601:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc601 lm75d_temp:  +21.0°C  
     
    fc301:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc402:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +27.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc302:cpu_temp-virtual-0
    Adapter: Virtual device
    fc302 cpu_temp:  +17.0°C  
     
    lc302:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +26.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc602:cpu_temp-virtual-0
    Adapter: Virtual device
    lc602 cpu_temp:  +21.0°C  
     
    fc202:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc202 lm75a_temp:  +20.0°C  
     
    chassis:Fan5Front-virtual-0
    Adapter: Virtual device
    Fan5 Front:  7100 RPM
     
    lc301:asic_temp-virtual-0
    Adapter: Virtual device
    lc301 asic_temp:  +38.0°C  
     
    lc202:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
     
    chassis:Fan14Rear-virtual-0
    Adapter: Virtual device
    Fan14 Rear:  7200 RPM
     
    fc302:asic_temp-virtual-0
    Adapter: Virtual device
    fc302 asic_temp:  +43.0°C  
     
    lc802:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc802 lm75c_temp:  +27.0°C  
     
    lc201:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc702:cpu_temp-virtual-0
    Adapter: Virtual device
    lc702 cpu_temp:  +21.0°C  
     
    lc701:cpu_temp-virtual-0
    Adapter: Virtual device
    lc701 cpu_temp:  +19.0°C  
     
    lc101:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +23.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc701:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc701 lm75d_temp:  +21.0°C  
     
    chassis:Fan12Rear-virtual-0
    Adapter: Virtual device
    Fan12 Rear:  7000 RPM
     
    lc102:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc402:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +25.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc202:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc202 lm75a_temp:  +20.0°C  
     
    lc401:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc401 lm75c_temp:  +28.0°C  
     
    fc101:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc101 lm75a_temp:  +20.0°C  
     
    chassis:Fan8Front-virtual-0
    Adapter: Virtual device
    Fan8 Front:  7100 RPM
     
    lc502:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc502 lm75a_temp:  +19.0°C  
     
    chassis:Fan13Rear-virtual-0
    Adapter: Virtual device
    Fan13 Rear:  7000 RPM
     
    lc601:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +23.0°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan7Rear-virtual-0
    Adapter: Virtual device
    Fan7 Rear:   7100 RPM
     
    lc201:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc501:cpu_temp-virtual-0
    Adapter: Virtual device
    lc501 cpu_temp:  +17.0°C  
     
    fc302:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc302 lm75c_temp:  +28.0°C  
     
    fc202:cpu_temp-virtual-0
    Adapter: Virtual device
    fc202 cpu_temp:  +17.0°C  
     
    lc401:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc401 lm75b_temp:  +25.0°C  
     
    lc602:asic_temp-virtual-0
    Adapter: Virtual device
    lc602 asic_temp:  +38.0°C  
     
    lc802:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc802 lm75b_temp:  +29.0°C  
     
    fc202:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc202 lm75d_temp:  +21.0°C  
     
    lc802:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc802 lm75a_temp:  +20.0°C  
     
    lc501:asic_temp-virtual-0
    Adapter: Virtual device
    lc501 asic_temp:  +37.0°C  
     
    lc302:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc302 lm75d_temp:  +25.0°C  
     
    lc402:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc402 lm75d_temp:  +25.0°C  
     
    fc101:asic_temp-virtual-0
    Adapter: Virtual device
    fc101 asic_temp:  +41.0°C  
     
    fc102:asic_temp-virtual-0
    Adapter: Virtual device
    fc102 asic_temp:  +40.0°C  
     
    lc101:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc101 lm75a_temp:  +20.0°C  
     
    lc201:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc201:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc201 lm75d_temp:  +21.0°C  
     
    lc402:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc302:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc302 lm75c_temp:  +25.0°C  
     
    chassis:Fan15Front-virtual-0
    Adapter: Virtual device
    Fan15 Front: 7100 RPM
     
    lc401:cpu_temp-virtual-0
    Adapter: Virtual device
    lc401 cpu_temp:  +14.0°C  
     
    lc801:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc801 lm75a_temp:  +20.0°C  
     
    fc201:asic_temp-virtual-0
    Adapter: Virtual device
    fc201 asic_temp:  +43.0°C  
     
    fc401:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc401 lm75a_temp:  +24.0°C  
     
    lc801:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc801 lm75d_temp:  +22.0°C  
     
    lc102:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc102 lm75d_temp:  +27.0°C  
     
    lc702:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc702 lm75d_temp:  +25.0°C  
     
    fc402:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc402 lm75c_temp:  +29.0°C  
     
    lc101:asic_temp-virtual-0
    Adapter: Virtual device
    lc101 asic_temp:  +41.0°C  
     
    lc101:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc101 lm75d_temp:  +22.0°C  
     
    lc501:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc301:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +23.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc401:cpu_temp-virtual-0
    Adapter: Virtual device
    fc401 cpu_temp:  +18.0°C  
     
    lc301:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc301 lm75c_temp:  +27.0°C  
     
    fc301:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc301 lm75c_temp:  +29.0°C  
     
    lc202:asic_temp-virtual-0
    Adapter: Virtual device
    lc202 asic_temp:  +38.0°C  
     
    lc502:asic_temp-virtual-0
    Adapter: Virtual device
    lc502 asic_temp:  +38.0°C  
     
    lc801:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc801 lm75b_temp:  +26.0°C  
     
    fc102:cpu_temp-virtual-0
    Adapter: Virtual device
    fc102 cpu_temp:  +18.0°C  
     
    fc101:cpu_temp-virtual-0
    Adapter: Virtual device
    fc101 cpu_temp:  +18.0°C  
     
    lc301:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc602:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +25.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc101:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc101 lm75d_temp:  +21.0°C  
     
    fc202:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +21.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc401:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc401 lm75d_temp:  +25.0°C  
     
    lc602:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +28.0°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc501:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc501 lm75a_temp:  +20.0°C  
     
    fc202:asic_temp-virtual-0
    Adapter: Virtual device
    fc202 asic_temp:  +44.0°C  
     
    fc401:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc401 lm75b_temp:  +32.0°C  
     
    fc202:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc502:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc502 lm75d_temp:  +25.0°C  
     
    chassis:Fan16Front-virtual-0
    Adapter: Virtual device
    Fan16 Front: 7100 RPM
     
    chassis:Fan4Rear-virtual-0
    Adapter: Virtual device
    Fan4 Rear:   7000 RPM
     
    fc402:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc402 lm75b_temp:  +30.0°C  
     
    chassis:Fan15Rear-virtual-0
    Adapter: Virtual device
    Fan15 Rear:  7000 RPM
     
    fc102:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc301:cpu_temp-virtual-0
    Adapter: Virtual device
    fc301 cpu_temp:  +19.0°C  
     
    chassis:Fan9Front-virtual-0
    Adapter: Virtual device
    Fan9 Front:  7000 RPM
     
    lc601:cpu_temp-virtual-0
    Adapter: Virtual device
    lc601 cpu_temp:  +20.0°C  
     
    lc801:cpu_temp-virtual-0
    Adapter: Virtual device
    lc801 cpu_temp:  +16.0°C  
     
    fc101:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc101 lm75c_temp:  +26.0°C  
     
    lc101:cpu_temp-virtual-0
    Adapter: Virtual device
    lc101 cpu_temp:  +19.0°C  
     
    lc602:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +21.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc101:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc701:asic_temp-virtual-0
    Adapter: Virtual device
    lc701 asic_temp:  +39.0°C  
     
    lc702:asic_temp-virtual-0
    Adapter: Virtual device
    lc702 asic_temp:  +39.0°C  
     
    chassis:Fan2Rear-virtual-0
    Adapter: Virtual device
    Fan2 Rear:   7000 RPM
     
    fc402:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc402 lm75d_temp:  +23.0°C  
     
    lc501:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +15.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +15.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc102:jc42_i2c_0_19-virtual-0Adapter: Virtual device
    temp1:        +22.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc201:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc201 lm75d_temp:  +21.0°C  
     
    lc102:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc102 lm75a_temp:  +20.0°C  
     
    lc802:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +28.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc201:cpu_temp-virtual-0
    Adapter: Virtual device
    fc201 cpu_temp:  +17.0°C  
     
    fc402:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc402 lm75a_temp:  +22.0°C  
     
    lc802:asic_temp-virtual-0
    Adapter: Virtual device
    lc802 asic_temp:  +39.0°C  
     
    fc201:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc201 lm75a_temp:  +20.0°C  
     
    fc102:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc102 lm75d_temp:  +21.0°C  
     
    fc402:asic_temp-virtual-0
    Adapter: Virtual device
    fc402 asic_temp:  +41.0°C  
     
    fc301:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc301 lm75b_temp:  +29.0°C  
     
    fc202:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc202 lm75c_temp:  +26.0°C  
     
    lc702:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc702 lm75a_temp:  +20.0°C  
     
    lc402:asic_temp-virtual-0
    Adapter: Virtual device
    lc402 asic_temp:  +40.0°C  
     
    lc201:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc201 lm75a_temp:  +19.0°C  
     
    chassis:Fan2Front-virtual-0
    Adapter: Virtual device
    Fan2 Front:  7000 RPM
     
    lc801:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc801 lm75c_temp:  +28.0°C  
     
    fc101:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc302:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc302 lm75a_temp:  +19.0°C  
     
    fc402:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +23.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc802:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc501:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +23.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan6Rear-virtual-0
    Adapter: Virtual device
    Fan6 Rear:   7200 RPM
     
    fc401:lm75c_temp-virtual-0
    Adapter: Virtual device
    fc401 lm75c_temp:  +31.0°C  
     
    lc501:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc501 lm75c_temp:  +27.0°C  
     
    lc401:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc401 lm75a_temp:  +20.0°C  
     
    fc301:lm75d_temp-virtual-0
    Adapter: Virtual device
    fc301 lm75d_temp:  +22.0°C  
     
    fc302:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan9Rear-virtual-0
    Adapter: Virtual device
    Fan9 Rear:   7000 RPM
     
    chassis:Fan6Front-virtual-0
    Adapter: Virtual device
    Fan6 Front:  7100 RPM
     
    lc202:cpu_temp-virtual-0
    Adapter: Virtual device
    lc202 cpu_temp:  +20.0°C  
     
    lc802:lm75d_temp-virtual-0
    Adapter: Virtual device
    lc802 lm75d_temp:  +26.0°C  
     
    fc201:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +22.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc301:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc301 lm75a_temp:  +23.0°C  
     
    fc101:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc101 lm75b_temp:  +28.0°C  
     
    lc601:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc601 lm75a_temp:  +20.0°C  
     
    lc201:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc201 lm75b_temp:  +25.0°C  
     
    chassis:Fan12Front-virtual-0
    Adapter: Virtual device
    Fan12 Front: 7000 RPM
     
    lc601:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc601 lm75b_temp:  +26.0°C  
     
    fc402:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc801:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +15.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +15.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc802:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +27.0°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc302:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc302 lm75b_temp:  +27.0°C  
     
    lc202:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc202 lm75b_temp:  +27.0°C  
     
    fc302:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +22.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc301:cpu_temp-virtual-0
    Adapter: Virtual device
    lc301 cpu_temp:  +17.0°C  
     
    fc402:cpu_temp-virtual-0
    Adapter: Virtual device
    fc402 cpu_temp:  +17.0°C  
     
    lc502:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc502 lm75c_temp:  +26.0°C  
     
    lc102:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc102 lm75c_temp:  +26.0°C  
     
    lc601:asic_temp-virtual-0
    Adapter: Virtual device
    lc601 asic_temp:  +37.0°C  
     
    lc602:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc602 lm75c_temp:  +26.0°C  
     
    fc201:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +16.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +18.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    chassis:Fan11Front-virtual-0
    Adapter: Virtual device
    Fan11 Front: 7200 RPM
     
    chassis:Fan3Rear-virtual-0
    Adapter: Virtual device
    Fan3 Rear:   7100 RPM
     
    lc701:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc701 lm75c_temp:  +28.0°C  
     
    chassis:Fan5Rear-virtual-0
    Adapter: Virtual device
    Fan5 Rear:   7000 RPM
     
    lc202:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc202 lm75c_temp:  +25.0°C  
     
    lc101:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc101 lm75b_temp:  +26.0°C  
     
    lc701:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc401:asic_temp-virtual-0
    Adapter: Virtual device
    fc401 asic_temp:  +47.0°C  
     
    lc702:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +28.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc101:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +21.5°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc601:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc402:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +23.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan1Front-virtual-0
    Adapter: Virtual device
    Fan1 Front:  7100 RPM
     
    lc502:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +17.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc801:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +23.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc602:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc602 lm75b_temp:  +29.0°C  
     
    lc101:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc101 lm75c_temp:  +29.0°C  
     
    lc502:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc502 lm75b_temp:  +27.0°C  
     
    chassis:Fan10Rear-virtual-0
    Adapter: Virtual device
    Fan10 Rear:  6900 RPM
     
    chassis:Fan13Front-virtual-0
    Adapter: Virtual device
    Fan13 Front: 7100 RPM
     
    lc302:cpu_temp-virtual-0
    Adapter: Virtual device
    lc302 cpu_temp:  +21.0°C  
     
    lc501:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc501 lm75b_temp:  +26.0°C  
     
    lc402:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc402 lm75c_temp:  +25.0°C  
     
    fc102:lm75a_temp-virtual-0
    Adapter: Virtual device
    fc102 lm75a_temp:  +21.0°C  
     
    chassis:Fan8Rear-virtual-0
    Adapter: Virtual device
    Fan8 Rear:   7100 RPM
     
    fc201:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc102:lm75b_temp-virtual-0
    Adapter: Virtual device
    fc102 lm75b_temp:  +28.0°C  
     
    lc702:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +26.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc701:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
     
    lc601:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +24.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc202:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +26.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc402:lm75a_temp-virtual-0
    Adapter: Virtual device
    lc402 lm75a_temp:  +20.0°C  
     
    chassis:Fan16Rear-virtual-0
    Adapter: Virtual device
    Fan16 Rear:  7000 RPM
     
    lc402:lm75b_temp-virtual-0
    Adapter: Virtual device
    lc402 lm75b_temp:  +27.0°C  
     
    lc201:lm75c_temp-virtual-0
    Adapter: Virtual device
    lc201 lm75c_temp:  +27.0°C  
     
    lc801:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +23.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    fc401:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +25.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    chassis:Fan3Front-virtual-0
    Adapter: Virtual device
    Fan3 Front:  7100 RPM
    lc502:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +25.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc102:cpu_temp-virtual-0
    Adapter: Virtual device
    lc102 cpu_temp:  +19.0°C  
     
    fc401:jc42_i2c_0_19-virtual-0
    Adapter: Virtual device
    temp1:        +25.2°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
     
    lc101:coretemp_isa_0000-virtual-0
    Adapter: Virtual device
    Core 0:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 1:       +20.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 2:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
    Core 3:       +19.0°C  (high = +98.0°C, crit = +98.0°C)
     
    fc102:jc42_i2c_0_1a-virtual-0
    Adapter: Virtual device
    temp1:        +22.8°C  (low  =  +5.0°C)
                           (high = +90.0°C, hyst = +90.0°C)
                           (crit = +95.0°C, hyst = +95.0°C)
    cumulus@omp-800-fc402:~$ 

### <span>About the bmcd Service</span>

The main purpose of the `bmcd` service is to distribute the sensor
information among all of the cards in a chassis so that every card sees
every sensor. If you are having trouble getting information from the
`sensors` command, check the status of the `bmcd` service using the
`systemctl` command:

    cumulus@omp-800-fc402:~$ systemctl status bmcd.service
    ● bmcd.service - BMC Interface Daemon
       Loaded: loaded (/lib/systemd/system/bmcd.service; enabled)
       Active: active (running) since Wed 2018-01-24 02:10:36 UTC; 2 weeks 2 days ago
     Main PID: 1288 (bmcd)
       CGroup: /system.slice/bmcd.service
               └─1288 /usr/bin/python /usr/sbin/bmcd

## <span>Generating the cl-support Script</span>

If you're submitting a ticket to the Cumulus Networks support team for
an issue with the chassis, you can generate the `cl-support` script for
a specific node in the chassis by specifying the IPv6 address of the
node in the `cl-chassis` command:

    cumulus@omp-800-fc402:~$ sudo cl-chassis <IPv6> cl-support

{{%notice tip%}}

You must use `sudo` when running the `cl-chassis` command as the
*cumulus* user.

{{%/notice%}}

Or you can generate the script for all the nodes in the chassis:

    cumulus@omp-800-fc402:~$ sudo cl-chassis all cl-support
    ********************************************************************************
    lc101
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc102
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc101
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc401
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc402
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc702
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc701
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc602
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc601
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc401
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc301
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc302
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc201
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc402
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc302
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc301
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc202
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc501
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc201
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc502
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc801
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    lc802
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc202
    SUCCESS!
    ********************************************************************************
    ********************************************************************************
    fc102
    SUCCESS!
    ********************************************************************************
    cumulus@omp-800-fc402:~$
