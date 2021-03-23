#!/usr/bin/env python3

import docraptor

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = 'fWcmD4BTI53tDaGKF2u9'

doc = """<tables>
<table name="Open Issues in 3.1.0">
<tr>
<th> Issue ID </th>
<th> Description </th>
<th> Affects </th>
<th> Fixed </th>
</tr>
<tr>
<td>2555854</td>
<td>CLI: Upgrade to NetQ 3.1.0 using the CLI fails due to an authentication issue. To work around this issue, run the {{netq bootstrap master upgrade}} command as usual, then use the Admin UI to complete the upgrade at _https://&lt;netq-appl-vm-hostname-or-ipaddr&gt;:8443_.</td>
<td>3.0.0-3.3.1</td>
<td></td>
</tr>
</table>
</tables>
"""

create_response = doc_api.create_doc({
                    "test": True,                                                   # test documents are free but watermarked
                    "document_content": doc,
                    "name": "test.xls",
                    "document_type": "xls",                                         # pdf or xls or xlsx
                })

file = open("test.xls", "wb")
file.write(create_response)
file.close