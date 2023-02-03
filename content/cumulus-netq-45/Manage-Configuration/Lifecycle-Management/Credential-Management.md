---
title: Credentials and Profiles
author: NVIDIA
weight: 640
toc: 4
---

Authentication credentials are stored in access profiles which can be assigned to individual switches. You can create credentials with either basic (SSH username/password) or SSH (public/private key) authentication. This section describes how to create, edit, and delete access profiles, as well as how to assign profiles to individual switches. 

{{<notice note>}}
By default, NVIDIA supplies two access profiles: Netq-default and Nvl4-Default. NVIDIA strongly recommends creating new access profiles with unique credentials. You cannot edit or delete default profiles.
{{</notice>}}

## Create an Access Profile

{{<tabs "TabID14">}}

{{<tab "NetQ UI">}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu. Under **Admin**, select **Manage switches**.

2. On the Access Profiles card, select **Add profile**.

3. Enter a name for the profile, then select the authentication method you want to use: **SSH** or **Basic**

{{<tabs "TabID183">}}

{{<tab "SSH">}}

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH key method.
{{</notice>}}

4. Create a pair of SSH private and public keys:

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

5. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where you generated the SSH key pair for each switch

6. Copy the SSH *private* key into the entry field:

    {{<figure src="/images/netq/ssh-access-profile-450.png" alt="card displaying field for ssh private key" width="300">}}

    {{<notice note>}}
For security, your private key is stored in an encrypted format, and only provided to internal processes while encrypted.
    {{</notice>}}

7. (Optional) To verify that the new profile is listed among available profiles, select **View profiles** from the Access Profiles card.

{{</tab>}}

{{<tab "Basic Authentication">}}

Be sure to use credentials for an account that has permission to configure switches.

{{<notice tip>}}

The default credentials for Cumulus Linux have changed from *cumulus/CumulusLinux!* to *cumulus/cumulus* for releases 4.2 and later. For details, read [Cumulus Linux User Accounts]({{<ref "cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts">}}).

{{</notice>}}

4. Enter a username and password.

5. Click **Create**, then confirm.

6. (Optional) To verify that the new profile is listed among available profiles, select **View profiles** from the Access Profiles card.

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "NetQ CLI">}}

<!--

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
    - Run `ssh-copy-id USER@<switch_ip>` on the server where you generated the SSH key pair for each switch

3. Add these credentials to the switch.

    ```
    cumulus@switch:~$ netq lcm add credentials ssh-key PUBLIC_SSH_KEY
    ```
-->
{{</tab>}}

{{</tabs>}}

## Edit Access Profiles

Note that Netq-default and Nvl4-Default cannot be edited.

{{<tabs "TabID175" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Access Profiles card, select **View profiles**.

3. Select the checkbox next to the profile you'd like to edit. Then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} Edit above the table.

4. Make you edits, then click **Update**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

<!-->

To change the basic authentication credentials, run the add credentials command with the new username and/or password. This example changes the password for the cumulus account created above:

```
cumulus@switch:~$ netq lcm add credentials username cumulus password Admin#123
```

To configure SSH authentication using a public/private key:

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH Key method.
{{</notice>}}

1. If the new keys do not yet exist, create a pair of SSH private and public keys:

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where you generated the SSH key pair for each switch

3. Add these new credentials to the switch:

    ```
    cumulus@switch:~$ netq lcm add credentials ssh-key PUBLIC_SSH_KEY
    ```

-->

{{</tab>}}

{{</tabs>}}

## Delete Access Profiles

Any profile that is currently assigned to a switch cannot be removed. You must assign a different profile to the switch before it's able to be deleted. Note that *Netq-default* and *Nvl4-Default* cannot be deleted. 

{{<tabs "TabID247" >}}

{{<tab "NetQ UI" >}}

1. On the Access Profiles card, select **View profiles**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

1. Run `netq lcm del credentials`. 

2. Verify their removal by running `netq lcm show credentials`.

{{</tab>}}

{{</tabs>}}

## View Access Profiles

You can view the type of credentials used to access your switches in the NetQ UI. You can view the details of the credentials using the NetQ CLI.

{{<tabs "TabID133" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Access Profiles card, select **View profiles**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

<!--

To see the credentials, run `netq lcm show credentials`.

If you use an SSH key for the credentials, the public key appears in the command output:

```
cumulus@switch:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
SSH              MY-SSH-KEY                                       Tue Apr 28 19:08:52 2020
```

If you use a username and password for the credentials, the username appears in the command output with the password masked:

```
cumulus@switch:~$ netq lcm show credentials
Type             SSH Key        Username         Password         Last Changed
---------------- -------------- ---------------- ---------------- -------------------------
BASIC                           cumulus          **************   Tue Apr 28 19:10:27 2020
```
-->
{{</tab>}}

{{</tabs>}}
