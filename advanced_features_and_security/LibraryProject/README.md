# Django Permissions and Groups Setup

## Overview
This project implements a permissions and groups system in Django to control access to the Document model.

## Custom Permissions
- `can_view`: Allows viewing documents.
- `can_create`: Allows creating documents.
- `can_edit`: Allows editing documents.
- `can_delete`: Allows deleting documents.

## User Groups
- **Editors**: Can create and edit documents.
- **Viewers**: Can only view documents.
- **Admins**: Can perform all actions (view, create, edit, delete).

## Usage
- Assign users to appropriate groups via the Django admin site.
- Use the `@permission_required` decorator in views to enforce permissions.