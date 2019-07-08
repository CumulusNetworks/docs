---
title: Markdown Guide
author: Daniel Cawley
weight: 1
siteSlug: Writing_Guide
---

## Second Level Header

### Third Level Header

#### Fourth Level Header

##### Fifth Level Header

The template adds the title in a level-one header by default, start all content
with level two headers.

## Numbered and Bulleted Lists

- The - character signifies a bulleted list
- Round Bullets are enabled by default
- The _*_ character may also be used, we will use - by default
  - Nested lists are supported
  - They will render with a,b,c
    - Only second level nesting currently supported
  - As in paragraphs, you can continue to add text onto the next line in
  markdown
- A new line followed by a - signifies a new list item

1. Numbered lists are supported as well
2. Very simple and self explanatory
  1. Nested lists also supported
  2. Will display as 1,2,3,
3. Nested ul (bulleted list) will display differently
  - Bullets
  - Are Displayed

## Inline Styling

Use two asterisks to bold any text

**This text will be bold (strong) in the rendered html**

Use one to italicize any text

*This text will be italicized in the rendered text*

Underscores may also be used in the place of asterisks, however the Cumulus
Standard will be the **

The ~ character can be used for strike throughs

~~This text will have a strikethrough~~


### Code Blocks and Syntax

Use three backticks to signify a code block


```
Formatter.prototype.removeSideandTopBar = function(){
$ = this.$
$("div[id = 'ht-loader']").remove()
$('#ht-headerbar').remove()
$('#ht-sidebar').remove()
$('#ht-breadcrumb').remove()
$('#ht-sidebar-dragbar').remove()
$("div[class = 'section section-1']").has('p.expand-control-text').remove()
}
```

inline code can be added with single backticks

**Example** Run `git checkout -b dev` to add a new branch

#### Syntax Highlight

To be continuted...
