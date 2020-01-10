---
title: Writing Guidelines
author: Cumulus Networks
weight: 220
siteSlug: contributor-guide
---
When we create our user documentation, we strive to provide easy-to-read, concise content with illustrations when useful. When you are editing existing or creating new content for Cumulus Networks technical user documentation, please follow these general guidelines.

## Organization and Content

- Cumulus is not a stuffy company so use a more casual, conversational writing style to match
    - Good: The first step in providing feedback on the Cumulus Networks documentation is to decide what level of input you want to provide.
    - Not so good: A user must first determine the complexity of the input he or she plans to submit for inclusion in the Cumulus Networks technical documentation.
- Use an active rather than passive voice
    - Good: An administrator backs up our network configuration on a regular basis.
    - Not so good: Our network configuration will be backed up by an administrator on a regular basis.
- Write content focused on a user's task, describing what they need to know, what needs to be done, and why it is important
    - Good: This topology allows you to build networks of varying size using nodes of different port counts and/or by increasing the tiers.
    - Not so good: This topology is used throughout this guide.
- Provide examples and graphical images to clarify your content
    - Good: {{<figure src="/images/netq/alarms-perf-rating.png" width="350">}}
    - Not so good: {{<figure src="/images/uploads/osi-model-bad-art.png" width="400">}}
- Chunk large topics and procedures into smaller sections
    - Good: {{<figure src="/images/uploads/contrib-gde-chunks-good.png" width="200">}}
    - Not so good: {{<figure src="/images/uploads/contrib-gde-chunks-bad.png" width="200">}}
- Use shorter and simpler sentences whenever possible
    - Good: You can submit new paragraphs, images, sections and whole topics for inclusion into the documentation.
    - Not so good: You can submit new paragraphs for a given topic, images to explain new concepts, sections that add explanation, and whole topics describing a new feature or capability for inclusion into the documentation.

## Word Usage

- Use common words and industry terms; explain new terms
    - Good: The NCLU wrapper utility called `net` is capable of configuring layer 2 and layer 3 features of the networking stack, installing ACLs and VXLANs, restoring configuration files, as well as providing monitoring and troubleshooting functionality for these features.
    - Not so good: `net` is capable of configuring various networking features like monitoring and troubleshooting.
- Use concise words that do not have multiple meanings or nuances
    - Good: To configure the switch, perform the following steps.
    - Not so good: To configure the switch, execute the following steps.
- Avoid extraneous words or phrases
    - Good: Click **Card** to select and open a card.
    - Not so good: Click the card icon in order to select a card to open.
- Avoid using contractions
    - Good: Do not reboot the switch.
    - Not so good: Don't reboot the switch.
- Check your spelling and grammar
    - Use the checker available with your editor when available
- Use title caps, capitalizing the first word of the title, heading, all nouns, adjectives and verbs. Avoid punctuation.
    - Good: Configure VRF Route Leaking
    - Not so good: Configuring a switch -- Vrf route Leaking

All edits and new content are reviewed by the Cumulus Networks documentation team before publication, so if you are not sure about particular style issues, leave it to us.
