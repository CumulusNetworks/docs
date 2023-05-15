---
title: Install a Custom Signed Certificate
author: NVIDIA
weight: 395
toc: 3
---

The NetQ UI ships with a self-signed certificate that is sufficient for non-production environments or cloud deployments. For on-premises deployments, however, you receive a warning from your browser that this default certificate is not trusted when you first log in to the NetQ UI. You can avoid this by installing your own signed certificate.

{{%notice note%}}
If you already have a certificate installed and want to change or update it, run the `kubectl delete secret netq-gui-ingress-tls [name] --namespace default` command.
{{%/notice%}}

You need the following items to perform the certificate installation:

- A valid X509 certificate.
- A private key file for the certificate.
- A DNS record name configured to access the NetQ UI.

  The FQDN should match the common name of the certificate. If you use a wild card in the common name &mdash; for example, if the common name of the certificate is _*.example.com_ &mdash; then the NetQ telemetry server should reside on a subdomain of that domain, accessible via a URL like _netq.example.com_.
- A functioning and healthy NetQ instance.

  You can verify this by running the `netq show opta-health` command.

## Install a Certificate using the NetQ CLI

{{<tabs "Install Cert">}}

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
       apiVersion: networking.k8s.io/v1
       kind: Ingress
       metadata:
         annotations:
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
        ingressClassName: ingress-nginx-class
        rules:
        - host: <your-hostname>
          http:
             paths:
              - path: /
              pathType: Prefix
              backend:
                service:
                 name: netq-gui
                 port: 
                  number: 80
              path: /
              pathType: Prefix
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
    
    A message like the one above appears if your ingress rule is successfully configured.

1. Configure the NetQ API to use the new certificate.

    Edit the `netq-swagger-ingress-external` service:

      ```
      kubectl edit ingress netq-swagger-ingress-external
      ```

    Add the `tls:` section in the `spec:` stanza, referencing your configured hostname and the `netq-gui-ingress-tls` secretName:

      ```
      spec:
      rules:
      - host: <hostname>
        http:
        paths:
        - backend:
          serviceName: swagger-ui
          servicePort: 8080
          path: /swagger(/|$)(.*)
      tls:
      - hosts:
        - <hostname>
        secretName: netq-gui-ingress-tls
      ```

    After saving your changes, delete the current swagger-ui pod to restart the service:

      ```
      cumulus@netq-ts:~$ kubectl delete pod -l app=swagger-ui
      pod "swagger-ui-deploy-69cfff7b45-cj6r6" deleted
      ```

{{</tab>}}

{{</tabs>}}

Your custom certificate should now be working. Verify this by opening the NetQ UI at `https://<your-hostname-or-ipaddr>` in your browser.

