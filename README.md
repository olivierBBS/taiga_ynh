# Taiga for YunoHost

[![Integration level](https://dash.yunohost.org/integration/taiga.svg)](https://ci-apps.yunohost.org/ci/apps/taiga/) ![Working status](https://ci-apps.yunohost.org/ci/badges/taiga.status.svg) ![Maintenance status](https://ci-apps.yunohost.org/ci/badges/taiga.maintain.svg)

[![Install Taiga with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=taiga)

*[Read this README in other languages.](./ALL_README.md)*

> *This package allows you to install Taiga quickly and simply on a YunoHost server.*  
> *If you don't have YunoHost, please consult [the guide](https://yunohost.org/install) to learn how to install it.*

## Overview

Taiga is a free and open-source project management platform for agile developers, designers and project managers who want a simple, beautiful tool that makes work truly enjoyable.

**Shipped version:** 6.7.0~ynh1

**Demo:** https://tree.taiga.io/discover

## Screenshots

![Taiga Screenshot](./doc/screenshots/taiga-screenshot.png)

## Documentation and resources

* Official app website: <https://taiga.io/>
* Official user documentation: <https://docs.taiga.io/>
* Official admin documentation: <https://docs.taiga.io/>
* Upstream app code repository: <https://github.com/taigaio>
* YunoHost Store: <https://apps.yunohost.org/app/taiga>
* Report a bug: <https://github.com/unedeplus/taiga_ynh/issues>

## Developer info

### Package structure

This package follows YunoHost packaging v2 guidelines:

- `manifest.toml`: App metadata, installation questions, and resource definitions
- `scripts/`: Bash scripts for installation, removal, upgrade, backup, restore, and URL changes
- `conf/`: Configuration file templates (NGINX, systemd, Taiga settings)
- `doc/`: Documentation files

### Important notes

**Before testing:**
1. You need to update the SHA256 checksums in `manifest.toml` for the actual Taiga 6.7.0 releases
2. Ensure your YunoHost instance has sufficient resources (at least 512MB RAM recommended)
3. PostgreSQL, Redis, and RabbitMQ will be automatically configured

**Features:**
- ✅ Multi-instance support
- ✅ Full backup/restore functionality
- ✅ URL change support
- ✅ Systemd service management
- ✅ Nginx reverse proxy configuration
- ✅ PostgreSQL database
- ✅ Redis caching
- ✅ RabbitMQ for async tasks
- ✅ Celery workers for background jobs
- ⚠️ LDAP integration: Not implemented (Taiga doesn't natively support LDAP)
- ⚠️ SSO integration: Not implemented (would require custom development)

### Installation

```bash
yunohost app install https://github.com/unedeplus/taiga_ynh
```

### Testing

This package uses YunoHost's CI testing framework. Tests are defined in `tests.toml`.

To test locally:
```bash
# Run package check
package_check taiga_ynh/

# Or use YunoHost's test system
yunohost app install taiga_ynh/ --force
```

### Updating checksums

To get the correct SHA256 checksums for the sources:

```bash
# Backend
curl -L https://github.com/taigaio/taiga-back/archive/refs/tags/6.7.0.tar.gz | sha256sum

# Frontend
curl -L https://github.com/taigaio/taiga-front/archive/refs/tags/6.7.0.tar.gz | sha256sum
```

Then update the values in `manifest.toml` under `[resources.sources.main]` and `[resources.sources.front]`.

### Known issues and limitations

- Email configuration is set to console backend by default (logs to console). Configure SMTP in the Django settings for real emails.
- WebSocket connections for real-time updates require proper reverse proxy configuration (included).
- Large file uploads may require adjusting `client_max_body_size` in NGINX.
- Resource-intensive during installation due to building the frontend.

### References

- [YunoHost packaging documentation](https://doc.yunohost.org/en/dev/packaging/)
- [YunoHost app helpers v2.1](https://doc.yunohost.org/en/dev/packaging/scripts/helpers_v2.1)
- [Taiga documentation](https://docs.taiga.io/)
- [Example YunoHost apps](https://github.com/YunoHost-Apps)

## License

This package is distributed under AGPL-3.0-or-later license (same as Taiga).

**Taiga:** https://github.com/taigaio
