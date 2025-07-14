---
title: Validate Overall Network Health
author: NVIDIA
weight: 800
toc: 3
---

The Validation Summary card in the NetQ UI lets you view the overall health of your network at a glance, giving you a high-level understanding of how well your network is operating. 

## View Key Metrics of Network Health

The Validation Summary card displays high-level results each category of validation and indicates whether the most recently run validation passed, failed, or did not run.

{{<figure src="/images/netq/validation-summary-415.png" width="750">}}

Select **View details** in the bottom-right corner to view a more detailed summary, with a list of the individual tests comprising a single validation and whether those tests passed or failed.

{{<figure src="/images/netq/val-summary-full-415.png" width="1000">}}


From this view, you can select **View details** on a specific validation to view a comprehensive list of all the validations that NetQ ran for that particular protocol or service, or you can run a new validation by selecting **Re-run**.

The following dashboard displays the results from BGP validations from the past 24 hours. 

 - Use the dropdown menus in the side navigation to limit or expand the time range of the data displayed. 
 - From here, you can also choose whether to display all validation results, or only on-demand or scheduled validations.
 - Select **Re-run** to run a new, on-demand validation.


{{<figure src="/images/netq/bgp-validation-415.png" width="1000">}}

