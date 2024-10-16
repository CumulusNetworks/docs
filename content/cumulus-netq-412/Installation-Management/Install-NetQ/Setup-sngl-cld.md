---
title: Set Up Your Virtual Machine for a Single Cloud Server
author: NVIDIA
weight: 226
toc: 5
bookhidden: true
---
Follow these steps to set up and configure your VM on a single server in a cloud deployment.

- - -

## System Requirements

Verify that your system meets the VM requirements.

| Resource | Minimum Requirements |
| --- | :--- |
| Processor | 4 virtual CPUs |
| Memory | 8 GB RAM |
| Local disk storage | 64 GB|
| Network interface speed | 1 Gb NIC |
| Hypervisor | KVM/QCOW (QEMU Copy on Write) image for servers running Ubuntu;<br> VMware ESXi™ 6.5 or later (OVA image) for servers running Cumulus Linux or Ubuntu  | 


## Port Requirements

Confirm that the required ports are open for communications. The OPTA must be able to initiate HTTPS connections (destination TCP port 443) to the netq.nvidia.com domain (*.netq.nvidia.com). You must also open the following ports on your NetQ OPTA:

| Port or Protocol Number | Protocol | Component Access |
| --- | --- | --- |
|4	|IP Protocol|	Calico networking (IP-in-IP Protocol)|
|22	|TCP|	SSH|
|80	|TCP|	nginx|
|179	|TCP|	Calico networking (BGP)|
|443	|TCP|	NetQ UI|
|2379	|TCP|	etcd datastore|
|4789	|UDP|	Calico networking (VxLAN)|
|5000	|TCP|	Docker registry|
|6443	|TCP|	kube-apiserver|
|30001	|TCP|	DPU communication|
|31980	|TCP|	NetQ Agent communication|
|31982	|TCP|	NetQ Agent SSL communication|
|32708	|TCP|	API Gateway|

## Installation and Configuration

1. Download the NetQ image.

    a. Log in to your {{<exlink url="https://nvid.nvidia.com/" text="NVIDIA Application Hub">}} account.<br>
    b. Select **NVIDIA Licensing Portal**.<br>
    c. Select **Software Downloads** from the menu.<br>
    d. Click **Product Family** and select **NetQ**.<br>
    e. For deployments using KVM, download the **NetQ SW 4.11 KVM Cloud** image. For deployments using VMware, download the **NetQ SW 4.11 VMware Cloud** image.<br>
    f. If prompted, read the license agreement and proceed with the download.<br>

{{%notice note%}}
NVIDIA employees can download NetQ directly from the {{<exlink url="http://ui.licensing.nvidia.com/" text="NVIDIA Licensing Portal">}}.
{{%/notice%}}

2. Open your hypervisor and configure your VM. You can use the following examples for reference or use your own hypervisor instructions.
<!--undo these shortcodes-->
- {{<netq-install/vm-setup hypervisor="kvm" deployment="cloud" version="4.11">}}
- {{<netq-install/vm-setup hypervisor="vmware" deployment="cloud" version="4.11">}}

3. Log in to the VM and change the password.

Use the default credentials to log in the first time:

- Username: cumulus
- Password: cumulus

```
$ ssh cumulus@<ipaddr>
Warning: Permanently added '<ipaddr>' (ECDSA) to the list of known hosts.
Ubuntu 20.04 LTS
cumulus@<ipaddr>'s password:
You are required to change your password immediately (root enforced)
System information as of Thu Dec  3 21:35:42 UTC 2020
System load:  0.09              Processes:           120
Usage of /:   8.1% of 61.86GB   Users logged in:     0
Memory usage: 5%                IP address for eth0: <ipaddr>
Swap usage:   0%
WARNING: Your password has expired.
You must change your password now and login again!
Changing password for cumulus.
(current) UNIX password: cumulus
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Connection to <ipaddr> closed.
```
Log in again with your new password.

```
$ ssh cumulus@<ipaddr>
Warning: Permanently added '<ipaddr>' (ECDSA) to the list of known hosts.
Ubuntu 20.04 LTS
cumulus@<ipaddr>'s password:
  System information as of Thu Dec  3 21:35:59 UTC 2020
  System load:  0.07              Processes:           121
  Usage of /:   8.1% of 61.86GB   Users logged in:     0
  Memory usage: 5%                IP address for eth0: <ipaddr>
  Swap usage:   0%
Last login: Thu Dec  3 21:35:43 2020 from <local-ipaddr>
cumulus@ubuntu:~$
```

4. Verify that the platform is ready for installation. Fix any errors before installing the NetQ software.

```
cumulus@hostname:~$ sudo opta-check-cloud
```

5. Change the hostname for the VM from the default value.

The default hostname for the NetQ virtual machines is *ubuntu*. Change the hostname to fit your naming conventions while meeting Internet and Kubernetes naming standards.

{{<notice tip>}}
Kubernetes requires hostnames to be composed of a sequence of labels concatenated with dots. For example, “en.wikipedia.org” is a hostname. Each label must be from 1 to 63 characters long. The entire hostname, including the delimiting dots, has a maximum of 253 ASCII characters.<br>
<br>
The Internet standards (RFCs) for protocols specify that labels may contain only the ASCII letters a through z (in lower case), the digits 0 through 9, and the hyphen-minus character ('-').
{{</notice>}}

Use the following command:

```
cumulus@hostname:~$ sudo hostnamectl set-hostname NEW_HOSTNAME
```
Add the same NEW_HOSTNAME value to **/etc/hosts** on your VM for the localhost entry. For example:

```
127.0.0.1 localhost NEW_HOSTNAME
```

6. Install and activate the NetQ software using the CLI:

Run the following command on your NetQ cloud appliance with the `config-key` obtained from the email you received from NVIDIA titled *NetQ Access Link*. You can also obtain the configuration key {{<link title="Configure Premises" text="through the NetQ UI">}}.

```
cumulus@<hostname>:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-4.11.0-opta.tgz 
    config-key <your-config-key> 
    [proxy-host <proxy-hostname> proxy-port <proxy-port>]
```

<div class="notices note"><p></p><p>NetQ uses the 10.244.0.0/16 (<code>pod-ip-range</code>) and 10.96.0.0/16 (<code>service-ip-range</code>) networks for internal communication by default. If you are using these networks, you must override each range by specifying new subnets for these parameters in the install command:</p>
    <pre><div class="copy-code-img"><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/29-Copy-Paste/copy-paste-1.svg" width="20" height="20"></div>cumulus@hostname:~$ netq install opta standalone full interface eth0 bundle /mnt/installables/NetQ-4.11.0-opta.tgz config-key &lt;your-config-key&gt; pod-ip-range &lt;pod-ip-range&gt; service-ip-range &lt;service-ip-range&gt;</pre><p>You can specify the IP address of the server instead of the interface name using the <code>ip-addr &lt;address&gt;</code> argument:</p>
    <pre><div class="copy-code-img"><img src="https://icons.cumulusnetworks.com/01-Interface-Essential/29-Copy-Paste/copy-paste-1.svg" width="20" height="20"></div>cumulus@hostname:~$ netq install opta standalone full ip-addr &lt;ip-address&gt; bundle /mnt/installables/NetQ-4.11.0-opta.tgz config-key &lt;your-config-key&gt;</pre><p>If you change the server IP address or hostname after installing NetQ, you must reset the server with the <code>netq bootstrap reset keep-db</code> command and rerun the install command.</p>
    <p></p></div>
    
<div class="notices tip"><p>If this step fails for any reason, run <code>netq bootstrap reset</code> and then try again.</p></div>

## Verify Installation Status

To view the status of the installation, use the `netq show status [verbose]` command. The following example shows a successful installation:

```
State: Active
    Version: 4.11.0
    Installer Version: 4.11.0
    Installation Type: Standalone
    Activation Key: PKrgipMGEhVuZXRxLWVuZHBvaW50LWdhdGV3YXkYsagDIixUQmFLTUhzZU80RUdTL3pOT01uQ2lnRnrrUhTbXNPUGRXdnUwTVo5SEpBPTIHZGVmYXVsdDoHbmV0cWRldgz=
    Master SSH Public Key: a3NoLXJzYSBBQUFNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFEazliekZDblJUajkvOZ0hteXByTzZIb3Y2cVZBWFdsNVNtKzVrTXo3dmMrcFNZTGlOdWl1bEhZeUZZVDhSNmU3bFdqS3NrSE10bzArNFJsQVd6cnRvbVVzLzlLMzQ4M3pUMjVZQXpIU2N1ZVhBSE1TdZ0JyUkpXYUpTNjJ2RTkzcHBDVjBxWWJvUFo3aGpCY3ozb0VVWnRsU1lqQlZVdjhsVjBNN3JEWW52TXNGSURWLzJ2eks3K0x2N01XTG5aT054S09hdWZKZnVOT0R4YjFLbk1mN0JWK3hURUpLWW1mbTY1ckoyS1ArOEtFUllrr5TkF3bFVRTUdmT3daVNoZnpQajMwQ29CWDZZMzVST2hDNmhVVnN5OEkwdjVSV0tCbktrWk81MWlMSDAyZUpJbXJHUGdQa2s1SzhJdGRrQXZISVlTZ0RwRlpRb3Igcm9vdEBucXRzLTEwLTE4OC00NC0xNDc=
    Is Cloud: True
    
    Standalone Status:
    IP Address     Hostname       Role    Status
    -------------  -------------  ------  --------
    10.188.44.147  10.188.44.147  Role    Ready
    
    NetQ... Active
```
Run the `netq show opta-health` command to verify that all applications are operating properly. Allow at least 15 minutes for all applications to come up and report their status.

```
cumulus@hostname:~$ netq show opta-health
    Application                                            Status    Namespace      Restarts    Timestamp
    -----------------------------------------------------  --------  -------------  ----------  ------------------------
    cassandra-rc-0-w7h4z                                   READY     default        0           Fri Apr 10 16:08:38 2020
    cp-schema-registry-deploy-6bf5cbc8cc-vwcsx             READY     default        0           Fri Apr 10 16:08:38 2020
    kafka-broker-rc-0-p9r2l                                READY     default        0           Fri Apr 10 16:08:38 2020
    kafka-connect-deploy-7799bcb7b4-xdm5l                  READY     default        0           Fri Apr 10 16:08:38 2020
    netq-api-gateway-deploy-55996ff7c8-w4hrs               READY     default        0           Fri Apr 10 16:08:38 2020
    netq-app-address-deploy-66776ccc67-phpqk               READY     default        0           Fri Apr 10 16:08:38 2020
    netq-app-admin-oob-mgmt-server                         READY     default        0           Fri Apr 10 16:08:38 2020
    netq-app-bgp-deploy-7dd4c9d45b-j9bfr                   READY     default        0           Fri Apr 10 16:08:38 2020
    netq-app-clagsession-deploy-69564895b4-qhcpr           READY     default        0           Fri Apr 10 16:08:38 2020
    netq-app-configdiff-deploy-ff54c4cc4-7rz66             READY     default        0           Fri Apr 10 16:08:38 2020
    ...
```
{{%notice note%}}
If any of the applications or services display Status as DOWN after 30 minutes, open a support ticket and attach the output of the `opta-support` command.
{{%/notice%}}

After NetQ is installed, you can {{<link title="Access the NetQ UI" text="log in to NetQ">}} from your browser.