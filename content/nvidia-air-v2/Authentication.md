---
title: API Authentication
author: NVIDIA
weight: 25
product: NVIDIA Air 2.0
---

NVIDIA Air uses NGC API keys for authenticating API requests. This page covers Air-specific authentication details. For general information about NGC API keys, see the {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#ngc-api-keys" text="NGC API Keys documentation">}}.

For the full API reference, see the {{<exlink url="https://air-ngc.nvidia.com/api/docs/" text="NVIDIA Air API documentation">}}.

## API Key Types

NGC supports two types of API keys:

| Key Type | Use Case | Lifecycle |
|----------|----------|-----------|
| **Personal Key** | Individual development, testing | Tied to user account |
| **Service Key** | Automation, CI/CD pipelines | Tied to NGC org (not a user) |

For most Air API usage, a Personal Key is sufficient. Use Service Keys when you need automation that shouldn't depend on an individual user's account.

### Generating API Keys

To generate an API key:
- **Personal Key**: See {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#generating-a-personal-api-key" text="Generating a Personal API Key">}}
- **Service Key**: See {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#generating-a-service-api-key" text="Generating a Service API Key">}}

When generating a key, select **NVIDIA Air** from the services list to grant Air API access.

## Using API Keys

Include your API key in the `Authorization` header:

```bash
curl -X GET "https://api.air-ngc.nvidia.com/api/v3/simulations/" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Roles and Scopes

Air uses a role-based access control system managed through NGC. The Air API checks **scopes** to authorize requests. How you get scopes depends on the key type:

- **Personal API Keys**: You assign **roles** to users in NGC. Air automatically derives scopes from those roles.
- **Service Keys**: You assign **scopes** directly when creating the key, giving you fine-grained control.

### Roles

Roles are assigned to users in your NGC organization and apply to Personal API Keys. To manage user roles, see {{<exlink url="https://docs.nvidia.com/ngc/latest/ngc-user-guide.html#updating-user-roles" text="Updating User Roles">}} in the NGC documentation.

| Role | Description |
|------|-------------|
| `air` | Standard Air user with full simulation access |
| `air-admin` | Administrative access to all Air resources |
| `air-demo-manager` | Can manage Demo Marketplace content |
| `air-image-uploader` | Can upload custom images |
| `air-image-publisher` | Can publish images for public availability |
| `air-image-sharer` | Can create cross-org image sharing links |
| `air-instructor` | Can create and manage training sessions |

### Scopes

Scopes are the permissions that the Air API checks to authorize requests. For Personal API Keys, scopes are derived from assigned roles. For Service Keys, you select scopes directly when generating the key.

| Scope | Description |
|-------|-------------|
| `air:access` | Basic platform access (required for all users) |
| `air:simulation_read` | Read simulation details, nodes, interfaces, services |
| `air:simulation_create` | Create simulations via import, clone, or UI |
| `air:simulation_edit` | Modify simulation properties and topology |
| `air:simulation_delete` | Delete simulations |
| `air:simulation_start_stop` | Start and stop simulations |
| `air:image_read` | View published and org images |
| `air:image_write` | Upload and edit images |
| `air:image_publish` | Publish images for public availability (not restricted to any org) |
| `air:image_sharing` | Create cross-org image share links |
| `air:marketplace_demo_read` | View and interact with marketplace demos |
| `air:marketplace_demo_write` | Create and edit marketplace demos |
| `air:marketplace_demo_publish` | Publish demos to the marketplace |
| `air:training_instructor` | Create and manage training sessions |

### Role to Scope Mapping

The standard `air` role grants these scopes:
- `air:access`
- `air:simulation_read`
- `air:simulation_create`
- `air:simulation_edit`
- `air:simulation_delete`
- `air:simulation_start_stop`
- `air:image_read`

Additional roles grant additional scopes as indicated by their names.
