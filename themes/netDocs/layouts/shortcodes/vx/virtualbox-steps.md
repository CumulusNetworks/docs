<ol>
<li>Open the VirtualBox application and select <strong>Import Appliance</strong> from the <strong>File</strong> menu.</li>
<li>Browse for the OVA disk image you downloaded, click the <strong>Open</strong> button, then click <strong>Continue</strong>.</li>
<li>In the Appliance settings, change the name of the VM to <code>leaf01</code>, then click <strong>Import</strong> to begin the import process.
<p><img src="/images/cumulus-vx/VirtualBox-review.png" > </p></li>
<li>In the VirtualBox Manager window, right click the <code>leaf01</code> VM, then select <strong>Clone</strong>.</li>
<li>Change the name of the VM to <code>leaf02</code>, then click <strong>Continue</strong>.</li>
<li>Select <strong>Full Clone</strong> and click <strong>Clone</strong>.</li>
<li>Repeat steps 6 through 8 to create <code>spine01</code>.</li>
</ol>
