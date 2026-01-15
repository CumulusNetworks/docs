---
title: Sharing Images
author: NVIDIA
weight: 35
product: NVIDIA Air 2.0
---

Image sharing enables organizations to securely share custom OS images with other NVIDIA Air organizations.

## Overview

When you upload a custom image to NVIDIA Air, that image is private to your organization by default. To share an image with another organization, you generate a claim code that the target organization uses to copy the image to their organization.

Image share requests expire after 24 hours by default.

## Required Permissions

Image sharing requires specific roles assigned to your account:

| Action | Required Role | Scope |
|--------|---------------|-------|
| Share an image (create claim code) | `AIR_IMAGE_SHARER` | `air:image_sharing` |
| Claim a shared image | `AIR_IMAGE_UPLOADER` or `AIR_IMAGE_PUBLISHER` | `air:image_write` |

For information on how roles are assigned, see {{<link title="API Authentication">}}.

## Sharing an Image

To share an image with another organization:

1. Navigate to the **Images** page.
2. Locate the image you want to share.
3. Click the **Actions** menu (three dots) on the right side of the image row.
4. Select **Share Image**.
5. Enter the target organization.
6. Click **Share**.

{{<img src="/images/guides/nvidia-air-v2/ShareImageMenu.png" alt="Actions menu showing Share Image option">}}

After creating the share, you receive a **claim code**. Send this claim code to the target organization through a secure channel.

## Claiming a Shared Image

When another organization shares an image with you, they provide a claim code. To claim the shared image:

1. Navigate to the **Images** page.
2. Click the **Image Shares** dropdown button.
3. Select **Claim Image Share**.
4. Enter the claim code provided by the source organization.
5. Click **Claim**.

{{<img src="/images/guides/nvidia-air-v2/ClaimImageShare.png" alt="Image Shares dropdown with Claim Image Share option">}}

The image is copied to your organization.
