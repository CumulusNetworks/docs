---
title: Unsigned Certificate Warning when Connecting to NetQ UI
author: NVIDIA
weight: 344
toc: 4
---

## Issue
<!-- vale off -->
When I try to connect to the NetQ UI to configure my on-premises setup, I get a warning from my browser that the certificate is untrusted.
<!-- vale on -->
## Environment

- NetQ 3.0.0 - 3.1.0

## Resolution

The NetQ UI ships with a self-signed certificate, which is why your browser issues a warning. You can avoid seeing this issue by installing your own signed certificate.

To use a custom certificate, you need the following:

- A valid X509 certificate.
- A private key file for the certificate.
- A DNS record name configured to access the NetQ UI. The FQDN should match the common name of the certificate. If you use a wild card in the common name &mdash; for example, if the common name of the certificate is _*.example.com_ &mdash; then the NetQ telemetry server should reside on a subdomain of that domain, accessible via a URL like _netq.example.com_.
- You must install and run NetQ. You can verify this by running the `netq show opta-health` command.

To install a custom certificate:

1. Log in to the NetQ telemetry server via SSH and copy your certificate and key file there.
1. Generate a Kubernetes secret called `netq-gui-ingress-tls` using following command:

       cumulus@netq-ts:~$ kubectl create secret tls netq-gui-ingress-tls \
           --namespace default \
           --key <name of your key file>.key \
           --cert <name of your cert file>.crt

1. Verify that you created the secret:

       cumulus@netq-ts:~$ kubectl get secret

       NAME                               TYPE                                  DATA   AGE
       netq-gui-ingress-tls               kubernetes.io/tls                     2      5s

1. Update the ingress rule file to install self signed certificates. Create a new file called `ingress.yaml` with following content. Make sure to replace `<your hostname>` with the FQDN of the NetQ server.

       apiVersion: extensions/v1beta1
       kind: Ingress
       metadata:
         annotations:
           kubernetes.io/ingress.class: "ingress-nginx"
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
         - host: <your hostname>
           http:
             paths:
             - backend:
                 serviceName: netq-gui
                 servicePort: 80
         tls:
         - hosts:
           - <your hostname>
           secretName: netq-gui-ingress-tls

1. Run the following command:

       cumulus@netq-ts:~$ kubectl apply -f ingress.yaml

   If your ingress rule is successfully configured, a message like the following appears:

       ingress.extensions/netq-gui-ingress-external configured

Your custom certificate should now be working. Verify it in the UI by visiting `https://<your hostname>` in your browser.
