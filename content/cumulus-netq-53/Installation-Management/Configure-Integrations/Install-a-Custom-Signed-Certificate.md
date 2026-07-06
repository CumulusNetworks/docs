---
title: Install a Custom Signed Certificate
author: NVIDIA
weight: 395
toc: 3
---

When you first log in to the NetQ UI as part of an on-premises deployment, your browser will display a warning indicating that the default certificate is not trusted. You can avoid this warning by installing your own, custom-signed certificate using the steps outlined on this page. The self-signed certificate is sufficient for non-production environments or cloud deployments. 

{{%notice note%}}
The steps outlined in this section apply to NetQ version 5.2.1 or later. For earlier versions, refer to the {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-51/Installation-Management/Configure-Integrations/Install-a-Custom-Signed-Certificate/" text="previous version of this guide">}}.
{{%/notice%}}
{{%notice note%}}
If you already have a certificate installed and want to change or update it, run `kubectl delete secret netq-gateway-tls \--namespace kgateway-system` before following the steps in this section.
{{%/notice%}}
You need the following items to perform the certificate installation:

- A valid X509 certificate, containing a Subject Alternative Name (SAN) attribute.
- A private key file for the certificate.
- A DNS record name configured to access the NetQ UI. The FQDN should match the common name of the certificate. If you use a wild card in the common name &mdash; for example, if the common name of the certificate is _*.example.com_ &mdash; then the NetQ telemetry server should reside on a subdomain of that domain, accessible via a URL like _netq.example.com_.
- A functioning and healthy NetQ instance.You can verify this by running the `netq show opta-health` command.

## Install a Certificate using the NetQ CLI

{{<tabs "Install Cert">}}

{{<tab "NetQ CLI">}}

1. Log in to the NetQ VM via SSH and copy your certificate and key file there.

2. Generate a Kubernetes secret called `netq-gateway-tls` in the `kgateway-system` namespace:

    ```
    nvidia@netq-ts:~$ kubectl create secret tls netq-gateway-tls \
        --namespace netq-infra \
        --key <name of your key file>.key \
        --cert <name of your cert file>.crt
    ```
3. Verify that you created the secret successfully:

    ```
    nvidia@netq-ts:~$ kubectl get secret -n kgateway-system | grep netq-gateway-tls

    NAME                               TYPE                                  DATA   AGE
    netq-gateway-tls                   kubernetes.io/tls                     2      5s
    ```

4. Update the ingress rule file to install self-signed certificates.

    1. Create a new file called `ingress.yaml`.

    2. Copy and add the following content to the file. Replace `<your-hostname>` with the FQDN of the NetQ VM.

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: netq-gui-httproute-external
  namespace: netq-eth
spec:
  parentRefs:
    - name: netq-gateway
      namespace: kgateway-system
      sectionName: https
  hostnames:
    - <your-hostname>
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: netq-gui
          port: 80
      timeouts:
        request: 3600s
        backendRequest: 3600s
```


5. Apply the new rule:

```
nvidia@netq-ts:~$ kubectl apply -f ingress.yaml

httproute.gateway.networking.k8s.io/netq-gui-httproute-external configured
```
The message above appears if your ingress rule is successfully configured.

 
{{</tab>}}

{{</tabs>}}

Your custom certificate should now be working. Verify this by opening the NetQ UI at `https://<your-hostname>/netq-gui/` in your browser.