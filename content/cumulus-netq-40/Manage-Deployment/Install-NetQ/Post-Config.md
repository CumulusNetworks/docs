---
title: Post Installation Configuration Options
author: NVIDIA
weight: 395
toc: 3
---

This topic describes how to configure deployment options that you can perform only after you finish installing or upgrading NetQ.

## Install a Custom Signed Certificate

The NetQ UI ships with a self-signed certificate that is sufficient for non-production environments or cloud deployments. For on-premises deployments, however, you receive a warning from your browser that this default certificate is not trusted when you first log in to the NetQ UI. You can avoid this by installing your own signed certificate.

You need the following items to perform the certificate installation:

- A valid X509 certificate.
- A private key file for the certificate.
- A DNS record name configured to access the NetQ UI.

  The FQDN should match the common name of the certificate. If you use a wild card in the common name &mdash; for example, if the common name of the certificate is _*.example.com_ &mdash; then the NetQ telemetry server should reside on a subdomain of that domain, accessible via a URL like _netq.example.com_.
- NetQ is running.

  You can verify this by running the `netq show opta-health` command.

You can install a certificate using the Admin UI or the NetQ CLI.

{{<tabs "Install Cert">}}

{{<tab "NetQ UI">}}

1. Enter *https://\<hostname-or-ipaddr-of-netq-appliance-or-vm\>:8443* in your browser address bar to open the Admin UI.

2. From the Health page, click **Settings**.

    {{<figure src="/images/netq/adminui-settings-tab-cert-400.png" width="600">}}

3. Click **Edit**.

4. Enter the hostname, certificate and certificate key in the relevant fields.

5. Click **Lock**.

{{</tab>}}

{{<tab "NetQ CLI">}}

1. Log in to the NetQ On-premises Appliance or VM via SSH and copy your certificate and key file there.

1. Generate a Kubernetes secret called `netq-gui-ingress-tls`.

    ```
    cumulus@netq-ts:~$ kubectl create secret tls netq-gui-ingress-tls \
        --namespace default \
        --key <name of your key file>.key \
        --cert <name of your cert file>.crt
    ```

1. Verify that you created the secret successfully.

    ```
    cumulus@netq-ts:~$ kubectl get secret

    NAME                               TYPE                                  DATA   AGE
    netq-gui-ingress-tls               kubernetes.io/tls                     2      5s
    ```

1. Update the ingress rule file to install self-signed certificates.

    1. Create a new file called `ingress.yaml`.

    2. Copy and add this content to the file.

       ```
       apiVersion: extensions/v1beta1
       kind: Ingress
       metadata:
         annotations:
           kubernetes.io/ingress.class: "ingress-nginx"
           nginx.ingress.kubernetes.io/ssl-passthrough: "true"
           nginx.ingress.kubernetes.io/ssl-redirect: "true"
           nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
           nginx.ingress.kubernetes.io/proxy-connect-timeout: "3600"
           nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
           nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
           nginx.ingress.kubernetes.io/proxy-body-size: 10g
           nginx.ingress.kubernetes.io/proxy-request-buffering: "off"
         name: netq-gui-ingress-external
         namespace: default
       spec:
         rules:
         - host: <your-hostname>
           http:
             paths:
             - backend:
                 serviceName: netq-gui
                 servicePort: 80
         tls:
         - hosts:
           - <your-hostname>
           secretName: netq-gui-ingress-tls
        ```

    3. Replace `<your-hostname>` with the FQDN of the NetQ On-premises Appliance or VM.

1. Apply the new rule.

    ```
    cumulus@netq-ts:~$ kubectl apply -f ingress.yaml
    ingress.extensions/netq-gui-ingress-external configured
    ```
    
    A message like the one here appears if your ingress rule is successfully configured.

{{</tab>}}

{{</tabs>}}

Your custom certificate should now be working. Verify this by opening the NetQ UI at `https://<your-hostname-or-ipaddr>` in your browser.

## Update Your Cloud Activation Key

You use the cloud activation key (called the *config-key*) to access the cloud services, not the authorization keys you use for configuring the CLI. NVIDIA provides the key when you set up your premises.

On occasion, you might want to update your cloud service activation key. For example, if you mistyped the key during installation and now your existing key does not work, or you received a new key for your premises from NVIDIA.

Update the activation key using the Admin UI or NetQ CLI:

{{<tabs "Cloud Key">}}

{{<tab "Admin UI">}}

1. Open the Admin UI by entering *https://\<master-hostname-or-ipaddress\>:8443* in your browser address field.

2. Click **Settings**.

3. Click **Activation**.

4. Click **Edit**.

5. Enter your new configuration key in the designated entry field.

6. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI">}}

Run the following command on your standalone or master NetQ Cloud Appliance or VM replacing `text-opta-key` with your new key.

```
cumulus@<hostname>:~$ netq install standalone activate-job config-key <text-opta-key>
```

{{</tab>}}

{{</tabs>}}

## Add More Nodes to Your Server Cluster

Installation of NetQ with a server cluster sets up the master and two worker nodes. To expand your cluster to include up to a total of 10 nodes, use the Admin UI.

To add more worker nodes:

1. Prepare the nodes. Refer to the relevant server cluster instructions in {{<link title="Install the NetQ System">}}.

2. Open the Admin UI by entering *https://\<master-hostname-or-ipaddress\>:8443* in your browser address field.

    This opens the Health dashboard for NetQ.

3. Click **Cluster** to view your current configuration.

    {{<figure src="/images/netq/adminui-cluster-tab-400.png" width="700" caption="On-premises deployment">}}

    This opens the Cluster dashboard, with the details about each node in the cluster.

4. Click **Add Worker Node**.

5. Enter the *private* IP address of the node you want to add.

6. Click **Add**.

    Monitor the progress of the three jobs by clicking <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-circle-down.svg" height="18" width="18"/> next to the jobs.

    On completion, a card for the new node is added to the Cluster dashboard.

    If the addition fails for any reason, download the log file by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/>, run `netq bootstrap reset` on this new worker node, and then try again.

7. Repeat this process to add more worker nodes as needed.
