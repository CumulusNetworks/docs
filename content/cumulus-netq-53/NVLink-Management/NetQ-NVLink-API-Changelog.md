---
title: NetQ NVLink API Changelog
author: NVIDIA
weight: 355
toc: 3
---


## 5.2 NetQ NVLink REST API Changelog

<p><strong>Version 5.2.0</strong> (compared to 5.1.0). Breaking changes are indicated with ⚠️. For more information, see the {{<exlink url="http://docs.nvidia.com/networking-ethernet-software/netq-nvlink-api-520/" text="REST API in Swagger">}}.<br>

<table id="api-changelog" class="sortable">
<thead>
<tr>
<th data-type="string">Endpoint</th>
<th data-type="string">Change Summary</th>
<th data-type="string">Notes and Details</th>
</tr>
</thead>
<tbody>
<tr><td><code>POST /v1/bring-up</code></td><td><strong>Added</strong>: Request field <code>CertP12</code></td><td>Binary field for user-cert mode; description updated with cert-mode docs, request examples added, 404 error response removed</td></tr>

<tr><td><code>GET /v1/certificates</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns overview listing all certificate metadata</td></tr>
<tr><td><code>POST /v1/certificates/ca</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Uploads CA certificate in PEM format; rejected when cluster is in self-signed cert mode</td></tr>
<tr><td><code>GET /v1/certificates/ca</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves CA certificate metadata</td></tr>
<tr><td><code>POST /v1/certificates/server</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Uploads server TLS certificate and key in PEM format; supports <code>?force=true</code> override</td></tr>
<tr><td><code>GET /v1/certificates/server</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves server certificate metadata</td></tr>

<tr><td><code>GET /v1/compute-nodes</code></td><td><strong>Added</strong>: Response field <code>Sensors</code></td><td><code>ComputeNode</code> now includes <code>Sensors</code> of type <code>NodeSensorsMap</code>; new schemas <code>NodeSensor</code> and <code>NodeSensorsMap</code></td></tr>
<tr><td><code>GET /v1/compute-nodes</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>

<tr><td><code>GET /v1/compute-nodes/{id}</code></td><td><strong>Added</strong>: Response field <code>Sensors</code></td><td><code>ComputeNode</code> now includes <code>Sensors</code> of type <code>NodeSensorsMap</code>; new schemas <code>NodeSensor</code> and <code>NodeSensorsMap</code></td></tr>
<tr><td><code>PUT /v1/compute-nodes/{id}</code></td><td><strong>Added</strong>: Request/response field <code>Sensors</code></td><td><code>ComputeNode</code> schema extended with <code>Sensors</code> and <code>NodeSensorsMap</code></td></tr>
<tr><td><code>GET /v1/compute-nodes/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>PUT /v1/compute-nodes/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>

<tr><td><code>GET /v1/gpus</code></td><td><strong>Introduced</strong>: New filtered listing</td><td>Lists GPUs with filters on <code>deviceUID</code>, <code>chassisSerialNumber</code>, <code>slotID</code>, <code>trayIndex</code>, <code>hostID</code></td></tr>
<tr><td><code>GET /v1/gpus</code></td><td><strong>Changed</strong>: <code>GPU.DeviceUID</code> schema</td><td>Inlined <code>uint64</code> type and added JavaScript precision warning (was <code>$ref: uint64</code>)</td></tr>

<tr><td><code>GET /v1/gpus/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>PUT /v1/gpus/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>GET /v1/gpus/{id}</code></td><td><strong>Changed</strong>: <code>GPU.DeviceUID</code> schema</td><td>Inlined <code>uint64</code> type with JavaScript precision warning (was <code>$ref: uint64</code>)</td></tr>
<tr><td><code>PUT /v1/gpus/{id}</code></td><td><strong>Changed</strong>: <code>GPU.DeviceUID</code> schema</td><td>Inlined <code>uint64</code> type with JavaScript precision warning (was <code>$ref: uint64</code>)</td></tr>

<tr><td><code>POST /v1/images</code></td><td><strong>Added</strong>: Optional request field <code>ImageType</code></td><td>Extends <code>UploadImageRequest</code> with <code>ImageType</code></td></tr>
<tr><td><code>GET /v1/images</code></td><td><strong>Changed ⚠️</strong>: <code>ImageMetadata.imageType</code> enum</td><td>Enum values changed from uppercase <code>NVOS</code> to lowercase <code>nvos</code>; new value <code>cpld</code> added (breaking change)</td></tr>

<tr><td><code>GET /v1/kpi/compute-health</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns compute node health metrics time series </td></tr>
<tr><td><code>GET /v1/kpi/connection-state</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns connection state metrics time series </td></tr>
<tr><td><code>GET /v1/kpi/domain-health</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns domain health metrics time series </td></tr>
<tr><td><code>GET /v1/kpi/gpu-health</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns GPU health metrics time series </td></tr>
<tr><td><code>GET /v1/kpi/partition-health</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns partition health metrics time series </td></tr>
<tr><td><code>GET /v1/kpi/switch-node-health</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns switch node health metrics time series </td></tr>

<tr><td><code>GET /v1/kpis</code></td><td><strong>Changed</strong>: KPI enums and schema</td><td><code>KPIType</code> enum extended with <code>FW_VERSIONS</code>; <code>KPIResponse</code> schema gains <code>fw-versions</code> field</td></tr>

<tr><td><code>GET /v1/partitions</code></td><td><strong>Added</strong>: Query parameter <code>gpu-id-type</code></td><td>Enum values: <code>device-uuid</code>, <code>db-id</code>; new <code>GpuIdType</code> schema</td></tr>
<tr><td><code>POST /v1/partitions</code></td><td><strong>Added</strong>: Request support for <code>GPU-DeviceUUID</code></td><td>Partition members may use <code>uint64</code> device UUIDs in addition to GPU DB IDs</td></tr>
<tr><td><code>GET /v1/partitions/{id}</code></td><td><strong>Added</strong>: Query parameter <code>gpu-id-type</code></td><td>Enum values: <code>device-uuid</code>, <code>db-id</code></td></tr>
<tr><td><code>PUT /v1/partitions/{id}</code></td><td><strong>Added</strong>: Request support for <code>GPU-DeviceUUID</code></td><td>Partition members may use <code>uint64</code> device UUIDs in addition to GPU DB IDs</td></tr>

<tr><td><code>GET /v1/redfish</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Lists all Redfish endpoints</td></tr>
<tr><td><code>POST /v1/redfish</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Creates a new Redfish endpoint</td></tr>
<tr><td><code>GET /v1/redfish/{id}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Retrieves a specific Redfish endpoint</td></tr>
<tr><td><code>DELETE /v1/redfish/{id}</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Deletes a Redfish endpoint</td></tr>

<tr><td><code>GET /v1/switch-nodes</code></td><td><strong>Added</strong>: Response field <code>Sensors</code></td><td><code>SwitchNode</code> schema now includes <code>Sensors</code> of type <code>NodeSensorsMap</code></td></tr>
<tr><td><code>GET /v1/switch-nodes</code></td><td><strong>Added</strong>: Response field <code>FWVersions</code></td><td><code>SwitchNode</code> schema gains <code>FWVersions</code>; new <code>FWVersions</code> schema (ASIC, BIOS, BMC, CPLD1–4, EROT variants, FPGA, NVOS)</td></tr>
<tr><td><code>GET /v1/switch-nodes</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>

<tr><td><code>GET /v1/switch-nodes/{id}</code></td><td><strong>Added</strong>: Response field <code>Sensors</code></td><td><code>SwitchNode</code> schema includes <code>Sensors</code> of type <code>NodeSensorsMap</code></td></tr>
<tr><td><code>PUT /v1/switch-nodes/{id}</code></td><td><strong>Added</strong>: Request/response field <code>Sensors</code></td><td><code>SwitchNode</code> schema includes <code>Sensors</code> of type <code>NodeSensorsMap</code></td></tr>

<tr><td><code>GET /v1/switches</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>GET /v1/switches/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>PUT /v1/switches/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>

<tr><td><code>GET /v1/ports</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>GET /v1/ports/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>PUT /v1/ports/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>

<tr><td><code>GET /v1/switch-nodes/{id}</code></td><td><strong>Added</strong>: Response field <code>FWVersions</code></td><td><code>SwitchNode</code> schema includes <code>FWVersions</code>; new <code>FWVersions</code> schema (ASIC, BIOS, BMC, CPLD1–4, EROT variants, FPGA, NVOS)</td></tr>
<tr><td><code>PUT /v1/switch-nodes/{id}</code></td><td><strong>Added</strong>: Request/response field <code>FWVersions</code></td><td><code>SwitchNode</code> schema includes <code>FWVersions</code>; uses shared <code>FWVersions</code> schema</td></tr>
<tr><td><code>GET /v1/switch-nodes/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>
<tr><td><code>PUT /v1/switch-nodes/{id}</code></td><td><strong>Changed</strong>: ID-related schemas constraints</td><td><code>SlotID</code>, <code>TrayIndex</code>, <code>HostID</code> schemas now require minimum value 0</td></tr>

<tr><td><code>POST /v1/upgrade-switch</code></td><td><strong>Changed</strong>: Upgrade request schema</td><td>Added <code>UpgradeType</code> enum (<code>nvos</code>, <code>cpld</code>) to <code>CreateSwitchUpgradeRequest</code>; description updated from “NVOS image” to “NVOS/Firmware image”; CPLD upgrade examples added</td></tr>

<tr><td><code>GET /v1/validations/fw-versions</code></td><td><strong>Introduced</strong>: New endpoint</td><td>Returns firmware version validation results per domain </td></tr>

<tr><td><code>GET /v1/version</code></td><td><strong>Changed</strong>: API version</td><td>API version updated from 5.1.0 to 5.2.0</td></tr>

<tr><td><code>ALL nmx/v1/* (NVL endpoints)</code></td><td><strong>Added</strong>: Error schema metadata</td><td>Error schema extended with <code>x-go-type: liberr.Error</code> and <code>x-go-type-import</code> for Go code generation; no wire-format changes</td></tr>
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

