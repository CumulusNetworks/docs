---
title: Install a Custom Signed Certificate
author: NVIDIA
weight: 395
toc: 3
---

When you first log in to the NetQ UI as part of an on-premises deployment, your browser will display a warning indicating that the default certificate is not trusted. You can avoid this warning by installing your own, custom-signed certificate using the steps outlined on this page. The self-signed certificate is sufficient for non-production environments or cloud deployments. 

{{<notice info>}}
Custom-signed certificates are supported in NetQ 5.0.1. The steps as outlined in this section are not supported in NetQ 5.0.0.
{{</notice>}}
{{%notice note%}}
If you already have a certificate installed and want to change or update it, run the `kubectl delete secret netq-gui-ingress-tls [name] --namespace default` command before following the steps outlined in this section. After making your updates, restart nginx with the `kubectl delete pod -l app.kubernetes.io/name=ingress-nginx --namespace ingress-nginx` command.
{{%/notice%}}

You need the following items to perform the certificate installation:

- A valid X509 certificate, containing a Subject Alternative Name (SAN) attribute.
- A private key file for the certificate.
- A DNS record name configured to access the NetQ UI.

  The FQDN should match the common name of the certificate. If you use a wild card in the common name &mdash; for example, if the common name of the certificate is _*.example.com_ &mdash; then the NetQ telemetry server should reside on a subdomain of that domain, accessible via a URL like _netq.example.com_.
- A functioning and healthy NetQ instance.

  You can verify this by running the `netq show opta-health` command.

## Install a Certificate using the NetQ CLI

{{<tabs "Install Cert">}}

{{<tab "NetQ CLI">}}

1. Log in to the NetQ VM via SSH and copy your certificate and key file there.

2. Generate a Kubernetes secret called `netq-gui-ingress-tls`:

    ```
    nvidia@netq-ts:~$ kubectl create secret tls netq-gui-ingress-tls \
        --namespace netq-infra \
        --key <name of your key file>.key \
        --cert <name of your cert file>.crt
    ```

3. Verify that you created the secret successfully:

    ```
    nvidia@netq-ts:~$ kubectl get secret -n netq-infra | grep netq-gui-ingress-tls

    NAME                               TYPE                                  DATA   AGE
    netq-gui-ingress-tls               kubernetes.io/tls                     2      5s
    ```

4. Update the ingress rule file to install self-signed certificates.

    1. Create a new file called `ingress.yaml`

    2. Copy and add the following content to the file. Replace `<your-hostname>` with the FQDN of the NetQ VM.

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kong-dp-kong-proxy
  namespace: netq-infra
  annotations:
    nginx.ingress.kubernetes.io/ssl-passthrough: "false"
spec:
  ingressClassName: ingress-nginx-class
  rules:
  - host: <your-hostname>
    http:
      paths:
      - path: /(api/netq|netq|netq-gui|nmx).*
        pathType: ImplementationSpecific
        backend:
          service:
            name: kong-dp-kong-proxy
            port:
              number: 8443
  tls:
  - hosts:
    - <your-hostname>
    secretName: netq-gui-ingress-tls
```


5. Apply the new rule:

    ```
    nvidia@netq-ts:~$ kubectl apply -f ingress.yaml
    ingress.extensions/netq-gui-ingress-external configured
    ```
    
    The message above appears if your ingress rule is successfully configured.

 
{{</tab>}}

{{</tabs>}}

Your custom certificate should now be working. Verify this by opening the NetQ UI at `https://<your-hostname>/netq-gui/` in your browser.