---
title: Cumulus Linux Support File
author: NVIDIA
weight: 707
toc: 4
---

Cumulus Linux generates support files called `cl-support` whenever issues are detected. 

This file is used to aid in troubleshooting customer issues. The Cumulus Networks global support staff often requests customers to provide this file when they open support tickets. 

The `cl-support` file is located in the `/var/support` directory and is named `cl_support_xxx.txz`.

There are three ways `cl-support` is generated:

- If `switchd` or any other process generates a core file (located in `/var/support/core`), then the `cl-support` file is generated.
- After the first failure of one of the following monitored services since the switch was rebooted or power cycled:
    - clagd
    - frr
    - openvswitch-vtep
    - portwd
    - ptmd
    - rdnbrd
    - switchd
    - vxrd
    - vxsnd
- A `cl-support` file can be triggered by issuing the `cl-support` command.

  {{%notice info%}}
  
You should only run this command at the direction of a  member of the Cumulus Networks support staff.

{{%/notice%}}

If you need to copy the `cl-support` file off of the switch to a remote host for collection, use `scp`:

    cumulus@switch:~$ scp /var/support/ username@myserver:/path/

<!--
## Comments

- 
    
    <div id="comment_360001082774">
    
    <div class="comment-avatar">
    
    ![Avatar](https://secure.gravatar.com/avatar/f9c71f2b72c801a44aa89c7eb001d3f7?default=https%3A%2F%2Fassets.zendesk.com%2Fhc%2Fassets%2Fdefault_avatar.png&r=g)
    
    </div>
    
    <div class="comment-container">
    
    **Nicolas Piatto** <span class="comment-published">November 28, 2018
    14:38</span>
    
    <div class="comment-body markdown">
    
    Is there an better way ( than a dirty cron job ) to exec cl-support
    every N hour ? ( a bit like what Arista is doing by default  
    )  
    During tshoot, there is often a miss in collecting a show
    tech-support prior to take action like power cycle ( :p ) and you
    loose the ability to dig deeper afterward. Getting at least N hour
    old show-tech could help
    
    </div>
    
    <span class="comment-actions"> <span class="dropdown">
    <span class="dropdown-toggle" data-aria-label="Comment actions" data-aria-haspopup="true">Comment
    actions</span> <span class="dropdown-menu" data-role="menu">
    </span> </span>
    </span>
    
    </div>
    
    </div>

- 
    
    <div id="comment_360001074153">
    
    <div class="comment-avatar comment-avatar-agent">
    
    ![Avatar](https://secure.gravatar.com/avatar/b61be1b80ad2fbce08b75ec5590cc508?default=https%3A%2F%2Fassets.zendesk.com%2Fhc%2Fassets%2Fdefault_avatar.png&r=g)
    
    </div>
    
    <div class="comment-container">
    
    **Dave Olson** <span class="comment-published">November 29, 2018
    02:08</span>
    
    <div class="comment-body markdown">
    
    Nicolas; it's a bad idea to run cl-support when it's not needed,
    because it can cause problems just by being run.
    
    There are many ways to monitor CL on a switch, that don't involve
    running cl-support. And of course, there's netq.
    
    </div>
-->
