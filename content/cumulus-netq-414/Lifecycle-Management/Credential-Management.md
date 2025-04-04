---
title: Credentials and Profiles
author: NVIDIA
weight: 640
toc: 4
---

You must have switch access credentials to install and upgrade software on a switch. These user authentication credentials are stored in NetQ as access profiles. The profiles must be applied to a switch before you can upgrade or install software. 

## Access Profiles

Authentication credentials are stored in access profiles which can be assigned to individual switches. You can create credentials with either basic (SSH username/password) or SSH (public/private key) authentication. This section describes how to create, edit, and delete access profiles. After you create a profile, attach it to individual switches so that you can perform upgrades on those switches. 

{{<notice note>}}
By default, NVIDIA supplies an access profile called <i>Netq-Default</i>. You must create a new access profile or update the default profile with unique credentials to perform upgrades and other lifecycle management tasks. 

You cannot delete the default profile.
{{</notice>}}

### Create Access Profiles

{{<tabs "TabID14">}}

{{<tab "NetQ UI">}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**.

2. On the Access Profiles card, select **Add profile**.

3. Enter a name for the profile, then select the authentication method you want to use: **SSH** or **Basic**

{{<tabs "TabID183">}}

{{<tab "SSH">}}

{{%notice info%}}
The SSH user must have sudoer permission to configure switches when using the SSH key method. To provide sudo access to the SSH user on a switch, create a file in the `/etc/sudoers.d/` directory with the following content. Replace `<USER>` with the SSH access profile username:

```
“<USER>” ALL=(ALL) NOPASSWD: ALL
```
{{%/notice%}}

4. Create a pair of SSH private and public keys on the NetQ appliance:

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```
When prompted, hit the enter/return key.

5. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where you generated the SSH key pair for each switch

6. Copy the SSH *private* key into the entry field:

    {{<figure src="/images/netq/ssh-access-profile-450.png" alt="card displaying field for ssh private key" width="300">}}

    {{<notice note>}}
For security, your private key is stored in an encrypted format, and only provided to internal processes while encrypted.
    {{</notice>}}

7. (Optional) To verify that the new profile is listed among available profiles, select **View profiles** from the Access Profiles card.

8. (Optional) Attach the profile to a switch so that you can perform upgrades.

{{</tab>}}

{{<tab "Basic Authentication">}}

4. Enter a username and password.

5. Click **Create**, then confirm.

6. (Optional) To verify that the new profile is listed among available profiles, select **View profiles** from the Access Profiles card.

7. (Optional) Attach the profile to a switch so that you can perform upgrades.

{{</tab>}}

{{</tabs>}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To configure basic authentication, run:

```
cumulus@netq-server:~$ netq lcm add credentials profile_name NEWPROFILE username cumulus password cumulus
```
Specify a unique name for the configuration after `profile_name`. 

{{<notice tip>}}

The default credentials for Cumulus Linux have changed from *cumulus/CumulusLinux!* to *cumulus/cumulus* for releases 4.2 and later. For details, read [Cumulus Linux User Accounts]({{<ref "cumulus-linux-43/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts">}}).

{{</notice>}}

To configure SSH authentication using a public/private key:

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH key method.
{{</notice>}}

1. If the keys do not yet exist, create a pair of SSH private and public keys on the NetQ appliance.

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```
When prompted, hit the enter/return key.

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where you generated the SSH key pair for each switch
<br>
<br>
3. Add these credentials to the switch. Specify a unique name for the configuration after `profile_name`. 

    ```
    cumulus@netq-server:~$ netq lcm add credentials profile_name NEWPROFILE username <USERNAME> ssh-key PUBLIC_SSH_KEY
    ```

{{</tab>}}

{{</tabs>}}

### Edit Access Profiles

{{<tabs "TabID175" >}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**.

2. On the Access Profiles card, select **View profiles**.

3. Select the the profile you'd like to edit. Then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} **Edit** above the table.

4. Make your changes, then click **Update**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

The syntax for editing access profiles is:

```
cumulus@netq-server:~$ netq lcm edit credentials 
    profile_id <text-switch-profile-id> 
    [profile_name <text-switch-profile-name>] 
    [auth-type <text-switch-auth-type>] 
    [username <text-switch-username>] 
    [password <text-switch-password> | ssh-key <text-ssh-key>]
```
Run `netq lcm show credentials` to obtain the profile ID. See the {{<link title="lcm/#netq-lcm-edit-credentials" text="command line reference">}} for further details.

To configure SSH authentication using a public/private key (requires sudoer permission):

1. If the new keys do not yet exist, create a pair of SSH private and public keys:

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy the SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where you generated the SSH key pair for each switch
<br>
<br>
3. Add these new credentials to the switch:

    ```
    cumulus@netq-server:~$ netq lcm edit credentials ssh-key PUBLIC_SSH_KEY
    ```

{{</tab>}}

{{</tabs>}}

### Delete Access Profiles

You cannot delete a profile that is currently attached to a switch. You must attach a different profile to the switch first. Note that you cannot delete the *Netq-Default* profile (but you can edit it). 

{{<tabs "TabID247" >}}

{{<tab "NetQ UI" >}}

1. On the Access Profiles card, select **View profiles**.

2. From the list of profiles, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} **Delete** in the profile's row. 

{{<figure src="/images/netq/access-profile-del-490.png" alt="" width="700">}}

The delete icon only appears next to custom profiles that are not attached to a switch.

3. Select **Remove**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

1. Run `netq lcm show credentials`. Identify the profiles you'd like to delete and copy their identifiers from the Profile ID column. The following example deletes the n-1000 profile:

```
cumulus@netq-server:~$ netq lcm show credentials
Profile ID           Profile Name             Type             SSH Key        Username         Password         Number of switches                   Last Changed
-------------------- ------------------------ ---------------- -------------- ---------------- ---------------- ------------------------------------ -------------------------
credential_profile_d Netq-Default             BASIC                           cumulus          **************   11                                   Fri Feb  3 18:20:33 2023
9e875bd2e6784617b304
c20090ce28ff2bb46a4b
9bf23cda98f1bdf91128
5c9
credential_profile_3 n-1000                   BASIC                           admin            **************   0                                    Fri Feb  3 21:49:10 2023
eddab251bddea9653df7
cd1be0fc123c5d7a42f8
18b68134e42858e54a9c
289
```

2. Run `netq lcm del credentials profile_ids <text-credential-profile-ids>`:

```
cumulus@netq-server:~$ netq lcm del credentials profile_ids credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289
```

3. Verify that the profile is deleted with `netq lcm show credentials`.

{{</tab>}}

{{</tabs>}}

### View Access Profiles

You can view the type of credentials used to access your switches in the NetQ UI. You can view the details of the credentials using the NetQ CLI.

{{<tabs "TabID133" >}}

{{<tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. On the Access Profiles card, select **View profiles**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To view a list of access profiles and their associated credentials, run `netq lcm show credentials`.

If you use an SSH key for the credentials, the public key appears in the command output.

If you use a username and password for the credentials, the username appears in the command output with the password masked.

{{</tab>}}

{{</tabs>}}

## Attach an Access Profile to a Switch

NetQ uses access profiles to store user authentications credentials. After creating an access profile from your credentials, you can attach a profile to one or multiple switches.

{{<tabs "TabID85" >}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**. On the Switches card, select **Manage**.

2. The table displays a list of switches. The **Access type** column specifies whether the type of authentication is basic or SSH. The **Profile name** column displays the access profile that is assigned to the switch.

Select the switches to which you'd like to assign access profiles, then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/04-Login-Logout/login-key-1.svg" height="18" width="18">}} **Manage access profile** above the table: 

{{<figure src="/images/netq/manage-access-profile-450.png" alt="" width="500" height="375">}}

3. Select the profile from the list, then click **Apply**. If the profile you want to use isn't listed, select **Add new profile** and follow the steps to create an access profile.

4. Select **Ok** on the confirmation dialog. The updated access profiles are now reflected in the **Profile name** column.


{{</tab>}}

{{<tab "NetQ CLI" >}}

The command syntax to attach a profile to a switch is:

```
netq lcm attach credentials 
    profile_id <text-switch-profile-id> 
    hostnames <text-switch-hostnames>
```

1. Run `netq lcm show credentials` to display a list of access profiles. Note the profile ID that you'd like to assign to a switch.

2. Run `netq lcm show switches` to display a list of switches. Note the hostname of the switch(es) you'd like to attach a profile to.

3. Next, attach the credentials to the switch:

```
netq lcm attach credentials profile_id credential_profile_3eddab251bddea9653df7cd1be0fc123c5d7a42f818b68134e42858e54a9c289 hostnames tor-1,tor-2
Attached profile to switch(es).
```

4. Run `netq lcm show switches` and verify the change in the credential profile column.

{{</tab>}}

{{</tabs>}}

## Reassign or Detach an Access Profile

Detaching a profile from a switch restores it to the default access profile, Netq-Default.

{{<tabs "TabID110" >}}

{{<tab "NetQ UI" >}}

1. On the Switches card, click **Manage**.

2. From the table of switches, locate the switch whose access profile you'd like to manage. Hover over the access type column and select **Manage access**:

{{<figure src="/images/netq/detach-manage-access-450.png" alt="" width="500" height="270">}}

3. To assign a different access profile to the switch, select it from the list. To detach the access profile, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18"/> **Detach**.

{{<figure src="/images/netq/manage-access-profile-spine-450.png" alt="" width="500" height="450">}}

After you detach the profile from the switch, NetQ reassigns it to the Netq-Default profile.

{{</tab>}}

{{<tab "NetQ CLI" >}}

The syntax for the detach command is `netq lcm detach credentials hostname <text-switch-hostname>`.

1. To obtain a list of hostnames, run `netq lcm show switches`.

2. Detach the access profile and specify the hostname. The following example detaches spine-1 from its assigned access profile:

```
cumulus@switch:~$ netq lcm detach credentials hostname spine-1
Detached profile from switch.
```

3. Run `netq lcm show switches` and verify the change in the credential profile column.

{{</tab>}}

{{</tabs>}}