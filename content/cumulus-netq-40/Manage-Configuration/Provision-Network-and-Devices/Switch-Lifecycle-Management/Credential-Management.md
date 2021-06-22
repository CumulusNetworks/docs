---
title: Manage Switch Credentials
author: NVIDIA
weight: 640
toc: 4
---
Switch access credentials are needed for performing installations and upgrades of software. You can choose between basic authentication (SSH username/password) and SSH (Public/Private key) authentication. These credentials apply to all switches. If some of your switches have alternate access credentials, you must change them or modify the credential information before attempting installations or upgrades with the lifecycle management feature.

## Specify Switch Credentials

Switch access credentials are not specified by default. You must add these.

To specify access credentials:

{{<tabs "TabID15">}}

{{<tab "NetQ UI">}}

1. Open the LCM dashboard.

2. Click the *Click here to add Switch access* link on the Access card.

    {{<figure src="/images/netq/lcm-access-card-no-auth-300.png" width="200">}}

3. Select the authentication method you want to use; **SSH** or **Basic Authentication**. Basic authentication is selected by default.

{{<tabs "TabID183">}}

{{<tab "Basic Authentication">}}

Be sure to use credentials for a user account that has permission to configure switches.

{{<notice tip>}}

The default credentials for Cumulus Linux have changed from *cumulus/CumulusLinux!* to *cumulus/cumulus* for releases 4.2 and later. For details, read [Cumulus Linux User Accounts]({{<ref "cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts">}}).

{{</notice>}}

1. Enter a username.

2. Enter a password.

    {{<img src="/images/netq/lcm-access-create-dialog-300.png" width="250">}}

3. Click **Save**.

    The Access card now indicates your credential configuration.

    {{<figure src="/images/netq/lcm-access-configured-300.png" width="200">}}

{{</tab>}}

{{<tab "SSH">}}

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH key method.
{{</notice>}}

1. Create a pair of SSH private and public keys.

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where the SSH key pair was generated for each switch

3. Copy the SSH *private* key into the entry field in the Create Switch Access card.

    {{<figure src="/images/netq/lcm-access-create-SSH-300.png" width="250">}}

    {{<notice note>}}
For security, your private key is stored in an encrypted format, and only provided to internal processes while encrypted.
    {{</notice>}}

The Access card now indicates your credential configuration.

{{<figure src="/images/netq/lcm-access-ssh-configured-300.png" width="200">}}

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To configure basic authentication, run:

```
cumulus@switch:~$ netq lcm add credentials username cumulus password cumulus
```

{{<notice tip>}}

The default credentials for Cumulus Linux have changed from *cumulus/CumulusLinux!* to *cumulus/cumulus* for releases 4.2 and later. For details, read [Cumulus Linux User Accounts]({{<ref "cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts">}}).

{{</notice>}}

To configure SSH authentication using a public/private key:

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH Key method.
{{</notice>}}

1. If the keys do not yet exist, create a pair of SSH private and public keys.

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where the SSH key pair was generated for each switch

3. Add these credentials to the switch.

    ```
    cumulus@switch:~$ netq lcm add credentials ssh-key PUBLIC_SSH_KEY
    ```

{{</tab>}}

{{</tabs>}}

## View Switch Credentials

You can view the type of credentials being used to access your switches in the NetQ UI. You can view the details of the credentials using the NetQ CLI.

{{<tabs "TabID133" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Access card, either **Basic** or **SSH** is indicated.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To see the credentials, run `netq lcm show credentials`.

If an SSH key is used for the credentials, the public key is displayed in the command output:

```
cumulus@switch:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
SSH              MY-SSH-KEY                                       Tue Apr 28 19:08:52 2020
```

If a username and password is used for the credentials, the username is displayed in the command output but the password is masked:

```
cumulus@switch:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
BASIC                           cumulus          **************   Tue Apr 28 19:10:27 2020
```

{{</tab>}}

{{</tabs>}}

## Modify Switch Credentials

You can modify your switch access credentials at any time. You can change between authentication methods or change values for either method.

To change your access credentials:

{{<tabs "TabID175" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Access card, click the *Click here to change access mode* link in the center of the card.

3. Select the authentication method you want to use; **SSH** or **Basic Authentication**. Basic authentication is selected by default.

4. Based on your selection:

    - **Basic**: Enter a new username and/or password
    - **SSH**: Copy and paste a new SSH private key

<div style="padding-left: 18px;">
{{<notice tip>}}
Refer to {{<link title="#Specify Switch Credentials" text="Specify Switch Credentials">}} for details.
{{</notice>}}
</div>

5. Click **Save**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To change the basic authentication credentials, run the add credentials command with the new username and/or password. This example changes the password for the cumulus account created above:

```
cumulus@switch:~$ netq lcm add credentials username cumulus password Admin#123
```

To configure SSH authentication using a public/private key:

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH Key method.
{{</notice>}}

1. If the new keys do not yet exist, create a pair of SSH private and public keys.

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where the SSH key pair was generated for each switch

3. Add these new credentials to the switch.

    ```
    cumulus@switch:~$ netq lcm add credentials ssh-key PUBLIC_SSH_KEY
    ```

{{</tab>}}

{{</tabs>}}

## Remove Switch Credentials

You can remove the access credentials for switches using the NetQ CLI. Note that without valid credentials, you cannot upgrade your switches.

To remove the credentials, run `netq lcm del credentials`. Verify they are removed by running `netq lcm show credentials`.
