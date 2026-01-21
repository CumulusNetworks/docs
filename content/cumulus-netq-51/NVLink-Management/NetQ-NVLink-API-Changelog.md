---
title: API Changelog
author: NVIDIA
weight: 355
toc: 3
---


<!--
## 5.1 NetQ for NVLink REST API Changelog

- Added API methods to download support packages and upgrade NVOS for all switches within an NVLink domain. Switch-level operations receive priority over domain-level operations.
   - Added `GET /domain`
   - Added `GET /domains/count`
   - Added `GET /domains/{id}`
   - Added `profileID` in the response body of the `PATCH /domains/{id}` endpoint
   - Added `profileID` in the response body of the `PUT /switch-nodes/{id}` endpoint
   - Updated `POST /upgrade-switch` to support NVOS upgrades at the domain level
   - Updated `POST /tech-support` to download logs at the domain level
 - Added a fault-tolerance mechanism that allows NVLink switches with at least two out-of-band management ports to maintain connectivity to NMX controller and telemetry services in case one port fails.
    - Added `GET /services/{id}/connection`
    - Added `GET /services/connection`
- Added `GET /version` to get NetQ version
-->
<p><strong>Version 5.1.0</strong> (compared to 5.0.0). Breaking changes are indicated with ⚠️. For more information, see the NetQ for NVLink Swagger documentation.<br>

<table id="api-changelog" class="sortable">
  <thead>
    <tr>
      <th data-type="string">Endpoint</th>
      <th data-type="string">Change Summary</th>
      <th data-type="string">Notes and Details</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>GET /compute-nodes</code></td><td><strong>Added</strong>: Optional query parameter <code>hostname</code></td><td>Enables filtering by node hostname</td></tr>
    <tr><td><code>GET /compute-nodes</code></td><td><strong>Added</strong>: Response property <code>/items/Hostname</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>GET /compute-nodes/count</code></td><td><strong>Added</strong>: Optional query parameter <code>hostname</code></td><td>Enables filtered count queries</td></tr>
    <tr><td><code>GET /compute-nodes/{id}</code></td><td><strong>Added</strong>: Response property <code>Hostname</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>PUT /compute-nodes/{id}</code></td><td><strong>Added</strong>: Response property <code>Hostname</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>GET /domains</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Provides domain listing</td></tr>
    <tr><td><code>GET /domains/count</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns domain count</td></tr>
    <tr><td><code>GET /domains/{id}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves domain details</td></tr>
    <tr><td><code>PATCH /domains/{id}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Updates domain properties. Use this endpoint to create an association between a domain and a profile ID. Then use the profile ID to access the switches within the domain.</td></tr>
    <tr><td><code>GET /partitions</code></td><td><strong>Changed ⚠️</strong>: Added <code>subschema #3</code> to <code>/items/Members</code> list</td><td>Schema update for 200 responses</td></tr>
    <tr><td><code>GET /partitions</code></td><td><strong>Changed ⚠️</strong>: Added enum value <code>DEVICE_UID_BASED</code> to <code>/items/Type</code></td><td>Expands partition type options</td></tr>
    <tr><td><code>GET /partitions</code></td><td><strong>Added</strong>: Response properties <code>/items/MultiCastGroupLimit</code>, <code>/items/ResiliencyMode</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>POST /partitions</code></td><td><strong>Added</strong>: Optional request properties <code>MultiCastGroupLimit</code>, <code>ResiliencyMode</code></td><td>Enhances partition configuration</td></tr>
    <tr><td><code>POST /partitions</code></td><td><strong>Changed</strong>: Added <code>subschema #3</code> to <code>Members</code> oneOf list</td><td>Schema expansion</td></tr>
    <tr><td><code>GET /partitions/{id}</code></td><td><strong>Changed ⚠️</strong>: Added <code>subschema #3</code> and enum <code>DEVICE_UID_BASED</code></td><td>Updated schema for ID lookup</td></tr>
    <tr><td><code>GET /partitions/{id}</code></td><td><strong>Added</strong>: Optional properties <code>MultiCastGroupLimit</code>, <code>ResiliencyMode</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>PUT /partitions/{id}</code></td><td><strong>Changed</strong>: Added <code>subschema #3</code> to request <code>Members</code></td><td>Aligns with POST schema</td></tr>
    <tr><td><code>GET /ports</code></td><td><strong>Added</strong>: Required properties <code>/items/LinkRateMbps</code>, <code>/items/PortAdminState</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>GET /ports/{id}</code></td><td><strong>Added</strong>: Required properties <code>LinkRateMbps</code>, <code>PortAdminState</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>PUT /ports/{id}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Supports port updates</td></tr>
    <tr><td><code>GET /services/connection</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Provides connection details</td></tr>
    <tr><td><code>GET /services/{id}/connection</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves connection by service ID</td></tr>
    <tr><td><code>GET /settings</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Lists current settings</td></tr>
    <tr><td><code>PATCH /settings</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Updates settings</td></tr>
    <tr><td><code>GET /settings/{name}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves a named setting</td></tr>
    <tr><td><code>DELETE /settings/{name}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Deletes a named setting</td></tr>
    <tr><td><code>GET /support-packages</code></td><td><strong>Added</strong>: Query parameter <code>domainIDs</code> and property <code>/items/domainID</code></td><td>Supports domain filtering</td></tr>
    <tr><td><code>GET /support-packages</code></td><td><strong>Added</strong>: Response 404 non-success status</td><td>New response code</td></tr>
    <tr><td><code>POST /support-packages</code></td><td><strong>Added</strong>: Optional request property <code>Domains</code>.Use the <code>profileID</code> from <code>PATCH /domains/{id}</code> or <code>PUT /switch-nodes{id}</code> to perform this request.</td><td>Adds domain linking</td></tr>
    <tr><td><code>POST /support-packages</code></td><td><strong>Changed</strong>: Property <code>Switches</code> became optional</td><td>Improved request flexibility</td></tr>
    <tr><td><code>POST /support-packages</code></td><td><strong>Added</strong>: Response 404 non-success status</td><td>New response code</td></tr>
    <tr><td><code>GET /switch-nodes</code></td><td><strong>Added</strong>: Optional query parameter <code>hostname</code></td><td>Enables hostname filtering</td></tr>
    <tr><td><code>GET /switch-nodes</code></td><td><strong>Added</strong>: Response properties <code>/items/AdminState</code>, <code>/items/Hostname</code>, <code>/items/ManagementIPs</code>, <code>/items/ProfileID</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>GET /switch-nodes/count</code></td><td><strong>Added</strong>: Optional query parameter <code>hostname</code></td><td>Enables filtered counts</td></tr>
    <tr><td><code>GET /switch-nodes/{id}</code></td><td><strong>Added</strong>: Response properties <code>AdminState</code>, <code>Hostname</code>, <code>ManagementIPs</code>, <code>ProfileID</code></td><td>Returned with status 200</td></tr>
    <tr><td><code>PUT /switch-nodes/{id}</code></td><td><strong>Changed ⚠️</strong>: Removed <code>subschema #1</code>, <code>#2</code> from request <code>anyOf</code></td><td>Breaking request body change</td></tr>
    <tr><td><code>PUT /switch-nodes/{id}</code></td><td><strong>Changed ⚠️</strong>: Changed request body type/format from <code>object</code>/"" to empty</td><td>Breaking request definition change</td></tr>
    <tr><td><code>PUT /switch-nodes/{id}</code></td><td><strong>Removed</strong>: Request properties <code>Description</code>, <code>Name</code></td><td>Streamlined payload</td></tr>
    <tr><td><code>PUT /switch-nodes/{id}</code></td><td><strong>Added</strong>: Request schemas <code>UpdateSwitchNodePayload</code>, <code>UpdateAdminStateRequest</code></td><td>Extended payload flexibility</td></tr>
    <tr><td><code>PUT /switch-nodes/{id}</code></td><td><strong>Added</strong>: Response properties <code>AdminState</code>, <code>Hostname</code>, <code>ManagementIPs</code>, <code>ProfileID</code></td><td>Returned with status 200. Use the endpoint fo modify </td></tr>
    <tr><td><code>PUT /switch-nodes/{id}</code></td><td><strong>Added</strong>: Success response 202</td><td>New accepted response code</td></tr>
    <tr><td><code>POST /upgrade-switch</code></td><td><strong>Added</strong>: Optional request property <code>Domains</code></td><td>Upgrades the OS of switches within a domain. Use the <code>profileID</code> from <code>PATCH /domains/{id}</code> or <code>PUT /switch-nodes{id}</code> to perform this request.</td></tr>
    <tr><td><code>POST /upgrade-switch</code></td><td><strong>Changed</strong>: Property <code>Switches</code> became optional</td><td>Improved request flexibility</td></tr>
    <tr><td><code>POST /upgrade-switch</code></td><td><strong>Added</strong>: Response 404 non-success status</td><td>Error handling addition</td></tr>
    <tr><td><code>GET /version</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves API version info</td></tr>
  </tbody>
</table>


<script>
(function () {
  function getCellValue(row, index) {
    return row.children[index].innerText || row.children[index].textContent;
  }

  function comparer(index, type, asc) {
    return function (a, b) {
      var v1 = getCellValue(asc ? a : b, index);
      var v2 = getCellValue(asc ? b : a, index);

      if (type === 'number') {
        v1 = parseFloat(v1) || 0;
        v2 = parseFloat(v2) || 0;
      } else {
        v1 = v1.toString().toLowerCase();
        v2 = v2.toString().toLowerCase();
      }

      if (v1 < v2) return -1;
      if (v1 > v2) return 1;
      return 0;
    };
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('table.sortable thead th').forEach(function (th) {
      th.style.cursor = 'pointer';
      th.addEventListener('click', function () {
        var table = th.closest('table');
        var tbody = table.tBodies[0];
        var index = Array.prototype.indexOf.call(th.parentNode.children, th);
        var type = th.getAttribute('data-type') || 'string';
        var asc = th.getAttribute('data-sort') !== 'asc'; // toggle

        // update sort direction attribute
        th.setAttribute('data-sort', asc ? 'asc' : 'desc');

        Array.from(tbody.querySelectorAll('tr'))
          .sort(comparer(index, type, asc))
          .forEach(function (tr) { tbody.appendChild(tr); });
      });
    });
  });
})();
</script>

