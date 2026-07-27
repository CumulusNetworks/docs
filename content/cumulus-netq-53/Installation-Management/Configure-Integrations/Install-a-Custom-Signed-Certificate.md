---
title: Install a Custom Signed Certificate
author: NVIDIA
weight: 395
toc: 3
---

When you first log in to the NetQ UI as part of an on-premises deployment, your browser will display a warning indicating that the default certificate is not trusted. You can avoid this warning by installing your own custom-signed certificate using the steps outlined on this page. The self-signed certificate is sufficient for non-production environments or cloud deployments.


## Prerequisites

You need the following items to perform the certificate installation:

- A valid X.509 certificate containing a Subject Alternative Name (SAN) attribute. The SAN must include the DNS name used to access the NetQ UI, for example, `DNS:netq.example.com`. Modern browsers validate the SAN field; the Common Name alone is not sufficient.
- A private key file for the certificate.
- A DNS record name configured to access the NetQ UI. The DNS record must resolve to a NetQ gateway, node, VIP, or load balancer IP that is reachable from the client browser. For lab validation, a local `/etc/hosts` entry can be used. Do not use a Kubernetes ClusterIP for external browser access unless the client can route to the cluster network.
  - The FQDN must match a DNS entry in the certificate's Subject Alternative Name (SAN). If you use a wildcard SAN (for example, `DNS:*.example.com`) the NetQ UI hostname must be a valid subdomain of that wildcard, such as `netq.example.com`.
- The certificate must be issued by a CA trusted by the client or browser. If you use an internal or lab CA, install the CA root or intermediate certificate on the client machine; otherwise, the browser may still show a trust warning.
- A functioning and healthy NetQ instance. You can verify this by running the `netq show opta-health` command.

## Install a Certificate Using kubectl

1. Log in to the NetQ VM via SSH and copy your certificate and key files there.

2. Generate a Kubernetes secret called `netq-gateway-tls` in the `netq-gateway` namespace:

    ```
    nvidia@netq-ts:~$ kubectl create secret tls netq-gateway-tls \
          --namespace netq-gateway \
          --key <name of your key file>.key \
          --cert <name of your cert file>.crt
    ```

3. Verify that you created the secret successfully:

    ```
    nvidia@netq-ts:~$ kubectl get secret -n netq-gateway | grep netq-gateway-tls
    NAME                  TYPE                DATA   AGE
    netq-gateway-tls      kubernetes.io/tls   2      5s
    ```

4. Verify that the certificate served by the gateway has the expected issuer and SAN:

    ```
    openssl s_client -connect <your-hostname>:443 \
      -servername <your-hostname> -showcerts </dev/null 2>/dev/null \
    | openssl x509 -noout -issuer -subject -dates -ext subjectAltName
    ```

    Confirm that the Subject Alternative Name contains `DNS:<your-hostname>`.

5. Create a new file called `ingress.yaml` and add the following content. Replace `<your-hostname>` with the FQDN of the NetQ VM (for example, `netq.cumulus.com`):

    ```
    apiVersion: gateway.networking.k8s.io/v1
    kind: HTTPRoute
    metadata:
      name: netq-gui-httproute-external
      namespace: netq-eth
    spec:
      parentRefs:
        - name: netq-gateway
          namespace: netq-gateway
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

6. Apply the new route:

    ```
    nvidia@netq-ts:~$ kubectl apply -f ingress.yaml
    httproute.gateway.networking.k8s.io/netq-gui-httproute-external configured
    ```

Your custom certificate should now be working. Verify this by opening the NetQ UI at `https://<your-hostname>/netq-gui/` in your browser.

## Update an Existing Certificate

If you already have a certificate installed and want to change or update it, delete the existing TLS secret before following the steps in this section:

```
kubectl delete secret netq-gateway-tls --namespace netq-gateway
```

If this secret is managed by cert-manager, deleting only the secret might not be sufficient, because cert-manager can recreate it. Check whether a Certificate resource manages the secret:

```
kubectl get certificate -n netq-gateway
```
If a Certificate resource exists for this secret, delete the Certificate resource first, then delete the secret:

```
kubectl delete certificate netq-gateway-tls-certificate --namespace netq-gateway
kubectl delete secret netq-gateway-tls --namespace netq-gateway
```

## Troubleshooting

If the UI loads but the browser still displays a certificate warning, check the following:

- The certificate SAN contains the exact hostname used in the browser.
- The hostname resolves to a client-reachable NetQ gateway, node, or VIP IP.
- The issuing CA is trusted by the client or browser.
