---
title: NetQ NVLink API Changelog
author: NVIDIA
weight: 355
toc: 3
---


## 5.3 NetQ NVLink REST API Changelog
<p><strong>Version 5.3.0</strong> (compared to 5.2.0). Breaking changes are indicated with ⚠️. For more information, see the {{<exlink url="http://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-530/" text="REST API in Swagger">}}.<br>
<table id="api-changelog" class="sortable">
<thead><tr><th data-type="string">Endpoint</th><th data-type="string">Change Summary</th><th data-type="string">Notes and Details</th></tr></thead>
<tbody>
<tr><td><code>PUT /v1/certificates/ca</code></td><td><strong>Added</strong>: New endpoint to rotate CA certificate</td><td>Replaces the stored CA certificate synchronously. Southbound picks up the new CA on its next natural reconnect or after a subsequent server or switch certificate rotation.</td></tr>
<tr><td><code>PUT /v1/certificates/server</code></td><td><strong>Added</strong>: New endpoint to rotate server certificate</td><td>Creates an asynchronous operation to rotate the server (southbound) TLS certificate. The optional <code>Reconnect</code> query parameter, when set to <code>true</code>, immediately activates the new certificate and drops and re-establishes managed-service connections.</td></tr>
<tr><td><code>PUT /v1/certificates/switches</code></td><td><strong>Added</strong>: New endpoint to rotate switch certificates</td><td>Creates an asynchronous operation to rotate TLS certificates on one or more managed switches. Requires a <code>CertP12</code> bundle in a multipart/form-data request. Returns <code>422</code> if a specified switch address is not currently managed.</td></tr>
<tr><td><code>DELETE /v1/chassis/{id}</code></td><td><strong>Added</strong>: New endpoint to delete a chassis</td><td>Synchronously deletes the chassis and cascades the deletion to its compute nodes, switch nodes, switches, GPUs, ports, and partitions in a single transaction.</td></tr>
<tr><td><code>DELETE /v1/compute-nodes/{id}</code></td><td><strong>Added</strong>: New endpoint to delete a compute node</td><td>Synchronously deletes the compute node and its GPUs and ports in a single transaction. Returns <code>409</code> if any of the node's GPUs is a member of an active partition; detach or delete the partition first.</td></tr>
<tr><td><code>DELETE /v1/domains/{id}</code></td><td><strong>Added</strong>: New endpoint to delete a domain</td><td>Asynchronously deletes the domain and all related entities (chassis, switch nodes, compute nodes, switches, GPUs, ports, partitions) and associated NMX services. Track progress via <code>GET /v1/operations/{operationId}</code>.</td></tr>
<tr><td><code>DELETE /v1/switch-nodes/{id}</code></td><td><strong>Added</strong>: New endpoint to delete a switch node</td><td>Synchronously deletes the switch node and its switches and ports in a single transaction.</td></tr>
<tr><td><code>GET /v1/chassis</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br><strong>Added</strong>: <code>chassisSerialNumber</code> query filter</td><td>The <code>pagination</code> parameter (offset/limit object) has been removed. Clients that relied on it must be updated. Use the new <code>chassisSerialNumber</code> parameter to filter results by chassis serial number.</td></tr>
<tr><td><code>GET /v1/compute-nodes</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br><strong>Added</strong>: <code>chassisSerialNumber</code>, <code>slotID</code>, <code>trayIndex</code>, <code>hostID</code> query filters</td><td>The <code>pagination</code> parameter has been removed. Clients that relied on it must be updated. New location-based query filters allow narrowing results by chassis, slot, tray, and host.</td></tr>
<tr><td><code>GET /v1/domains</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br><strong>Added</strong>: <code>controlPlaneState</code> query filter</td><td>The <code>pagination</code> parameter has been removed. Clients that relied on it must be updated. Use the new <code>controlPlaneState</code> parameter to filter domains by their control plane state.</td></tr>
<tr><td><code>GET /v1/gpus</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br>⚠️ <strong>Changed</strong>: <code>deviceUID</code> parameter type from <code>uint64</code> to <code>HexOrDecimalUint64</code><br><strong>Added</strong>: <code>systemUID</code> query filter</td><td>The <code>pagination</code> parameter has been removed. The <code>deviceUID</code> filter now accepts a decimal number or a hex string with <code>0x</code> prefix (e.g., <code>0x1A2B3C</code>); clients passing plain integer values must update to the new string format. A new <code>systemUID</code> filter allows filtering by node unique identifier.</td></tr>
<tr><td><code>GET /v1/ports</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br><strong>Added</strong>: <code>portUID</code>, <code>portType</code>, <code>chassisSerialNumber</code>, <code>slotID</code>, <code>trayIndex</code>, <code>hostID</code> query filters</td><td>The <code>pagination</code> parameter has been removed. Clients that relied on it must be updated. New filters allow querying ports by UID, type, and physical location.</td></tr>
<tr><td><code>GET /v1/switch-nodes</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br><strong>Added</strong>: <code>chassisSerialNumber</code>, <code>slotID</code>, <code>trayIndex</code>, <code>hostID</code> query filters</td><td>The <code>pagination</code> parameter has been removed. Clients that relied on it must be updated. New location-based query filters allow narrowing results by chassis, slot, tray, and host.</td></tr>
<tr><td><code>GET /v1/switches</code></td><td>⚠️ <strong>Removed</strong>: <code>pagination</code> query parameter<br>⚠️ <strong>Changed</strong>: <code>deviceUID</code> parameter type from <code>uint64</code> to <code>HexOrDecimalUint64</code><br><strong>Added</strong>: <code>deviceUID</code>, <code>systemUID</code>, <code>chassisSerialNumber</code>, <code>slotID</code>, <code>trayIndex</code>, <code>hostID</code> query filters</td><td>The <code>pagination</code> parameter has been removed. The new <code>deviceUID</code> filter accepts a decimal number or a hex string with <code>0x</code> prefix (e.g., <code>0x1A2B3C</code>). Additional location-based filters and a <code>systemUID</code> filter are also new.</td></tr>
<tr><td><code>GET /v1/compute-nodes</code><br><code>GET /v1/compute-nodes/{id}</code><br><code>GET /v1/switch-nodes</code><br><code>GET /v1/switch-nodes/{id}</code></td><td>⚠️ <strong>Changed</strong>: Response field <code>NodeSensor.URI</code> renamed to <code>NodeSensor.ID</code></td><td>The sensor identifier field in the <code>NodeSensor</code> schema was renamed from <code>URI</code> to <code>ID</code>. Clients that read sensor data from compute node or switch node responses must update field references from <code>URI</code> to <code>ID</code>.</td></tr>
<tr><td><code>GET /v1/services</code></td><td>⚠️ <strong>Changed</strong>: <code>address</code> query filter type from IPv4-only to IPv4 or hostname<br><strong>Changed</strong>: Response field <code>NmxService.Address</code> type from IPv4-only to IPv4 or hostname</td><td>The <code>address</code> filter and the <code>NmxService.Address</code> response field now use the broader <code>Address</code> schema (IPv4 or hostname). Previously, only IPv4 addresses were accepted.</td></tr>
<tr><td><code>POST /v1/services</code></td><td>⚠️ <strong>Changed</strong>: Request field <code>ServiceConnectionInformation.Address</code> type from IPv4-only to IPv4 or hostname</td><td><code>AddNmxServiceRequest.ServiceConnectionInformation.Address</code> now uses the <code>Address</code> schema (IPv4 or hostname). Services can now be registered using a hostname. Clients passing IPv4 values are unaffected.</td></tr>
<tr><td><code>POST /v1/certificates/server</code></td><td><strong>Added</strong>: <code>403</code> error response</td><td>The endpoint now returns <code>403 Forbidden</code> when the upload is rejected due to the current system configuration or policy (for example, when operating in self-signed cert-mode).</td></tr>
<tr><td><code>PATCH /v1/switch-profiles/{id}</code></td><td><strong>Changed</strong>: Request body is now required</td><td>The request body was previously optional. It is now required. A <code>PATCH</code> request must always include a body with at least one field to update (<code>Name</code>, <code>Username</code>, or <code>Password</code>).</td></tr>
</tbody>
</table>
<script>
(function() {
  const table = document.getElementById("api-changelog");
  if (!table) return;
  const headers = table.querySelectorAll("thead th");
  headers.forEach((header, index) => {
    let ascending = true;
    header.style.cursor = "pointer";
    header.addEventListener("click", () => {
      const tbody = table.querySelector("tbody");
      const rows = Array.from(tbody.querySelectorAll("tr"));
      const type = header.getAttribute("data-type") || "string";
      rows.sort((a, b) => {
        const aText = a.querySelectorAll("td")[index]?.innerText || "";
        const bText = b.querySelectorAll("td")[index]?.innerText || "";
        if (type === "number") {
          return ascending ? parseFloat(aText) - parseFloat(bText) : parseFloat(bText) - parseFloat(aText);
        }
        return ascending ? aText.localeCompare(bText) : bText.localeCompare(aText);
      });
      rows.forEach(row => tbody.appendChild(row));
      ascending = !ascending;
    });
  });
})();
</script>

