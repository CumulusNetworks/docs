---
title: Credentials and Profiles
author: NVIDIA
weight: 640
toc: 4
---

This section describes how to create and modify two types of profiles: access profiles and agent configuration profiles. Access profiles store user authentications credentials. Agent configuration profiles specify settings for a NetQ agent running on a switch. Both types of profiles must be applied to a switch for the changes to take effect. 

## Access Profiles

Authentication credentials are stored in access profiles which can be assigned to individual switches. You can create credentials with either basic (SSH username/password) or SSH (public/private key) authentication. This section describes how to create, edit, and delete access profiles. After you create a profile, {{<link title="Switch Management/#attach-an-access-profile-to-a-switch" text="attach it to individual switches">}} so that you can perform upgrades on those switches. 

{{<notice note>}}
By default, NVIDIA supplies two access profiles: Netq-Default and Nvl4-Default (for NVLink devices). NVIDIA strongly recommends creating new access profiles or updating the default profiles with unique credentials. 

You cannot delete default profiles.
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

8. (Optional) {{<link title="Switch Management/#attach-an-access-profile-to-a-switch" text="Attach the profile to a switch">}} so that you can perform upgrades.

{{</tab>}}

{{<tab "Basic Authentication">}}

Be sure to use credentials for an account that has permission to configure switches.

{{<notice tip>}}

The default credentials for Cumulus Linux have changed from *cumulus/CumulusLinux!* to *cumulus/cumulus* for releases 4.2 and later. For details, read [Cumulus Linux User Accounts]({{<ref "cumulus-linux-53/System-Configuration/Authentication-Authorization-and-Accounting/User-Accounts">}}).

{{</notice>}}

4. Enter a username and password.

5. Click **Create**, then confirm.

6. (Optional) To verify that the new profile is listed among available profiles, select **View profiles** from the Access Profiles card.

7. (Optional) {{<link title="Switch Management/#attach-an-access-profile-to-a-switch" text="Attach the profile to a switch">}} so that you can perform upgrades.

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

1. Open the LCM dashboard.

2. On the Access Profiles card, select **View profiles**.

3. Select the checkbox next to the profile you'd like to edit. Then select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} **Edit** above the table.

4. Make your edits, then click **Update**.

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

Any profile that is assigned to a switch can't be deleted. You must {{<link title="Switch Management/#attach-an-access-profile-to-a-switch" text="attach a different profile to the switch">}} first. Note that *Netq-Default* and *Nvl4-Default* can't be deleted. 

{{<tabs "TabID247" >}}

{{<tab "NetQ UI" >}}

1. On the Access Profiles card, select **View profiles**.

2. From the list of profiles, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} **Delete** in the profile's row. 

{{<figure src="/images/netq/delete-profile-450.png" alt="" width="600">}}

The delete icon only appears next to custom profiles that are not already attached to a switch.

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
credential_profile_3 Nvl4-Default             BASIC                           admin            **************   1                                    Fri Feb  3 19:18:26 2023
5a2eead7344fb91218bc
dec29b12c66ebef0d806
659b20e8805e4ff629bc
23e
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

## Agent Configuration Profiles

You can customize configuration profiles for NetQ agents running on switches. When you create a configuration profile, you can adjust the following agent settings:

- The VRF the NetQ agent uses to communicate with the NetQ server
- Whether WJH is enabled or disabled
- The agent log level
- The agent CPU limit

The default NetQ agent configuration profile sets the VRF to `mgmt`, the log level to `info`, the WJH status to disabled, and the CPU limit to disabled.
### Create Configuration Profiles

{{<tabs "TabID281">}}

{{<tab "NetQ UI">}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**.

2. Select **NetQ agent configurations**.

3. On the NetQ agent configurations card, select **Add config**.

4. Enter a profile name and choose the settings from the options presented in the UI. Select **Advanced** to set values for the log level and CPU limit:

{{<figure src="/images/netq/lcm-switch-agentconfig-profile-480.png" alt="card displaying agent configuration profile settings" height="450" width="450">}}

5. Enter your NetQ CLI {{<link url="Install-NetQ-CLI/#configure-the-netq-cli" text="authentication keys">}} and select **Add**.

{{%notice note%}}
If you use an in-band interface to manage your switch, you must use the CLI to create NetQ agent configuration profiles using the `inband-interface` option.
{{%/notice%}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Configure a NetQ agent configuration profile using the CLI with the `netq lcm add netq-config config-profile-name` command. If you manage the switch using an in-band interface, you must specify the interface name using the `inband-interface` option:

```
cumulus@netq-server:~$ netq lcm add netq-config config-profile-name <text-profile-name> access-key <text-access-key> secret-key <text-secret-key> [cpu-limit <text-cpu-limit>] [log-level error | log-level warn | log-level info | log-level debug] [vrf default | vrf mgmt | vrf <text-config-vrf>] [wjh enable | wjh disable] [inband-interface <text-interface-name>]
```

{{</tab>}}

{{</tabs>}}

### Apply Configuration Profiles

After you create an agent configuration profile, you must apply the profile to a switch to update the agent settings.

1. Run a {{<link url="Switch-Management/#switch-discovery" text="switch discovery">}}.

2. Select a switch from the **Discovered with NetQ** category and select **Change config**.

{{<figure src="/images/netq/lcm-switch-discovery-configure-configprofile-48.png" alt="card displaying discovered switch and change configuration option" height="450" width="450">}}

3. Select a configuration profile, then click **Next**.

4. Specify which NetQ agent version you want to run on the switch, then click **Next**.

5. Click **Install** to begin the pre-check process. After the pre-checks are successful, NetQ applies the configuration profile and installs the agent version you specified.