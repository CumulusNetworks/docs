---
title: Test some shortcodes
author: Cumulus Networks
cascade: 
    draft: true
    version: "0.1"
---

This page will render shortcodes. If a shortcode fails, Hugo should fail.

## Exlink

### URL
{{<exlink url="Cumulusnetworks.com" >}}  

### URL + Text
{{<exlink url="Cumulusnetworks.com" text="cumulus site">}}

## Expand

### Plain text

{{< expand "Click to expand... "  >}}
This is some text inside an expand
{{< /expand >}}

### Markdown

{{< expand "Click to expand... "  >}}
This is some **markdown** inside an expand
{{< /expand >}} 

## Figure

### Inline Figure

This is some text around {{< figure src="/images/cumulus-linux/qinq-double-tagged-no-vxlan.png" >}} a figure

### Figure Size

{{< figure src="/images/cumulus-linux/qinq-double-tagged-no-vxlan.png" height="100" width="100" >}}

### Figure Link

{{< figure src="/images/cumulus-linux/qinq-double-tagged-no-vxlan.png" link="http://cumulusnetworks.com" >}}

### Figure Alt

{{< figure src="/images/cumulus-linux/qinq-double-tagged-no-vxlan.png" alt="blah blah" >}}

### Figure Caption

{{< figure src="/images/cumulus-linux/qinq-double-tagged-no-vxlan.png" caption="blah blah" >}}

### Broken Figure

{{< figure src="/images/cumulus-linux/qinq-double-tagged-no-vxlan-plumbis.png" alt="blah blah" >}}

## Link

### Remote URL
{{<link url="Managing-Cumulus-Linux-Disk-Images" text="remote license" >}}
### Remote Title
### Local URL
### Local Title