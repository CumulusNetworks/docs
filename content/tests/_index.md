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

## Img

### External Image
{{<img src="https://s3.amazonaws.com/cms.ipressroom.com/219/files/20149/544a0d86f6091d6699000060_NVLogo_2D/NVLogo_2D_362acb00-8e1b-476b-9662-9fe138a4a920-prv.jpg" external="true" >}}

## Figure

### Inline Figure

This is some text around {{< figure src="/images/cumulus-linux/acl-legend.png" >}} a figure

### Figure Size

{{< figure src="/images/cumulus-linux/acl-legend.png" height="100" width="100" >}}

### Figure Link

{{< figure src="/images/cumulus-linux/acl-legend.png" link="http://nvidia.com" >}}

### Figure Alt

{{< figure src="/images/cumulus-linux/acl-legend.png" alt="blah blah" >}}

### Figure Caption

{{< figure src="/images/cumulus-linux/acl-legend.png" caption="blah blah" >}}
## Img

### Src and no Src

{{< img src="/images/cumulus-linux/acl-legend.png" >}}  
{{< img "/images/cumulus-linux/acl-legend.png" >}}

### Alt, Height, Width

{{< img src="/images/cumulus-linux/acl-legend.png" width="50px" height="50px" alt="blah" >}}  

## Link

### Remote URL

{{<link url="Managing-Cumulus-Linux-Disk-Images" text="remote license" >}}  
{{<link url="Managing-Cumulus-Linux-Disk-Images" >}}  
using markdown **{{<link url="Managing-Cumulus-Linux-Disk-Images" text="remote license" >}}** in a link

### Remote Title

{{<link title="Adding and Updating Packages" text="remote license" >}}  
{{<link title="Adding and Updating Packages" >}}  
markdown: **{{<link title="Adding and Updating Packages" >}}**

### Local URL

{{<link url="#figure" text="remote license" >}}  
markdown: **{{<link url="#figure" text="remote license" >}}**

### Local Title

{{<link url="#Figure Caption" text="remote license" >}}  
markdown: **{{<link url="#Figure Caption" text="remote license" >}}**

## Notice

### Note

{{% notice note %}}
this is a note
{{% /notice %}}

{{% notice note %}}
this is a note with **markdown**
{{% /notice %}}

{{% notice note %}}
this is a note with {{<link url="#Figure Caption" text="shortcode" >}}
{{% /notice %}}

### Tip

{{% notice tip %}}
this is a tip
{{% /notice %}}

{{% notice tip %}}
this is a tip with **markdown**
{{% /notice %}}

{{% notice tip %}}
this is a tip with {{<link url="#Figure Caption" text="shortcode" >}}
{{% /notice %}}

### Info

{{% notice info %}}
this is an info
{{% /notice %}}

{{% notice info %}}
this is an info with **markdown**
{{% /notice %}}

{{% notice info %}}
this is an info with {{<link url="#Figure Caption" text="shortcode" >}}
{{% /notice %}}

### Warning

{{% notice warning %}}
this is a warning
{{% /notice %}}

{{% notice warning %}}
this is a warning with **markdown**
{{% /notice %}}

{{% notice warning %}}
this is a warning with {{<link url="#Figure Caption" text="shortcode" >}}
{{% /notice %}}

## Tabs

### Standard

{{< tabs "10 ">}}

{{< tab "NCLU Commands ">}}
blah blah
{{< /tab >}}

{{< tab "vtysh Commands ">}}
argh argh
{{< /tab >}}

{{< /tabs >}}

### Markdown

{{< tabs "20 ">}}

{{< tab "NCLU Commands ">}}
{{<link url="#Figure Caption" text="shortcode" >}}
{{< /tab >}}

{{< tab "vtysh Commands ">}}
{{<link url="#Figure Caption" text="shortcode2" >}}
{{< /tab >}}

{{< /tabs >}}