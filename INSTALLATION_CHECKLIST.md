# Taiga YunoHost App - Pre-Installation Checklist

## ⚠️ CRITICAL: Before Testing

### 1. Update SHA256 Checksums
The current checksums in `manifest.toml` are placeholders. You MUST update them:

```bash
# Get backend checksum
curl -sL https://github.com/taigaio/taiga-back/archive/refs/tags/6.7.0.tar.gz | sha256sum

# Get frontend checksum  
curl -sL https://github.com/taigaio/taiga-front/archive/refs/tags/6.7.0.tar.gz | sha256sum
```

Then update in `manifest.toml`:
- `[resources.sources.main]` sha256
- `[resources.sources.front]` sha256

### 2. System Requirements
- **Minimum RAM:** 512MB (1GB recommended)
- **Disk Space:** ~500MB for app + data
- **YunoHost Version:** >= 11.2
- **Required Services:** PostgreSQL, Redis, RabbitMQ (auto-installed)

### 3. Test Installation Commands

```bash
# Install from local directory
sudo yunohost app install ./taiga_ynh --force

# Or from GitHub (once ready)
sudo yunohost app install https://github.com/unedeplus/taiga_ynh
```

## ✅ Compliance Checklist

### Manifest (manifest.toml)
- [x] Uses `packaging_format = 2`
- [x] Includes `[upstream]` section with all required fields
- [x] Includes `[integration]` section with resource estimates
- [x] Defines all required resources (sources, system_user, install_dir, data_dir, ports, database, apt)
- [x] Has proper install questions (domain, path, init_main_permission, admin, password)
- [x] Multi-instance support enabled
- [ ] **TODO:** Update real SHA256 checksums for sources

### Scripts
- [x] All scripts source `/usr/share/yunohost/helpers`
- [x] All scripts use `ynh_script_progression` for progress tracking
- [x] Install script properly uses YunoHost helpers
- [x] Remove script cleans up all resources
- [x] Backup script backs up all necessary data
- [x] Restore script properly restores all components
- [x] Upgrade script handles version migrations
- [x] Change_url script updates all configurations
- [x] Scripts use proper variable names ($app, $install_dir, $data_dir, etc.)

### Configuration Templates
- [x] nginx.conf uses `__VARIABLE__` syntax
- [x] systemd service files use `__VARIABLE__` syntax
- [x] Taiga backend config (local.py) properly templated
- [x] Taiga frontend config (conf.json) properly templated
- [x] Proper permissions set on sensitive files

### File Structure
- [x] Follows standard YunoHost app structure
- [x] All required scripts present (install, remove, backup, restore, upgrade, change_url)
- [x] Configuration templates in conf/ directory
- [x] Documentation in doc/ directory
- [x] tests.toml defines basic tests

### Security & Best Practices
- [x] Systemd services use sandboxing options
- [x] Sensitive credentials stored in settings (not hardcoded)
- [x] Proper file permissions (750 for dirs, 600 for sensitive configs)
- [x] Services run as dedicated system user
- [x] Database credentials randomly generated
- [x] RabbitMQ credentials randomly generated

### Features
- [x] Multi-instance support
- [x] Backup/restore functionality
- [x] URL change support
- [x] WebSocket support (for real-time events)
- [x] Celery workers for background tasks
- [x] Proper logging configuration
- [ ] LDAP integration (not applicable - Taiga doesn't support LDAP)
- [ ] SSO integration (not applicable - would require custom development)

## 🧪 Testing Procedure

### 1. Basic Installation Test
```bash
# Install
sudo yunohost app install ./taiga_ynh -a "domain=example.com&path=/taiga&admin=admin&password=SecurePass123"

# Verify services are running
sudo systemctl status taiga
sudo systemctl status taiga-celery

# Check logs
sudo journalctl -u taiga -n 50
sudo journalctl -u taiga-celery -n 50

# Access the app
curl -I https://example.com/taiga/
```

### 2. Backup Test
```bash
# Create backup
sudo yunohost backup create --apps taiga

# List backups
sudo yunohost backup list

# Verify backup contents
sudo tar -tzf /home/yunohost.backup/archives/BACKUP_NAME.tar
```

### 3. Restore Test
```bash
# Remove app
sudo yunohost app remove taiga

# Restore from backup
sudo yunohost backup restore BACKUP_NAME --apps taiga

# Verify restored app works
curl -I https://example.com/taiga/
```

### 4. Upgrade Test
```bash
# Make a minor change to trigger upgrade
# (e.g., edit version in manifest.toml to 6.7.0~ynh2)

# Run upgrade
sudo yunohost app upgrade taiga --file ./taiga_ynh

# Verify app still works
curl -I https://example.com/taiga/
```

### 5. Change URL Test
```bash
# Change path
sudo yunohost app change-url taiga --new-path /project-management

# Verify new URL works
curl -I https://example.com/project-management/

# Change domain (if you have another domain)
sudo yunohost app change-url taiga --new-domain newdomain.com
```

### 6. Multi-instance Test
```bash
# Install second instance
sudo yunohost app install ./taiga_ynh -a "domain=example.com&path=/taiga2&admin=admin&password=SecurePass123"

# Verify both instances work independently
curl -I https://example.com/taiga/
curl -I https://example.com/taiga2/
```

## 🐛 Common Issues & Solutions

### Issue: Build fails during frontend compilation
**Solution:** Ensure sufficient RAM (>512MB) and swap space

### Issue: Services fail to start
**Solution:** Check logs: `journalctl -u taiga -n 100`

### Issue: Database connection errors
**Solution:** Verify PostgreSQL is running: `systemctl status postgresql`

### Issue: RabbitMQ errors
**Solution:** Check RabbitMQ status: `systemctl status rabbitmq-server`

### Issue: 502 Bad Gateway
**Solution:** 
1. Check if Taiga service is running: `systemctl status taiga`
2. Verify port is correct in settings
3. Check nginx logs: `/var/log/nginx/`

## 📝 Next Steps

After successful testing:

1. **Update checksums** in manifest.toml with real values
2. **Test on a clean YunoHost instance** (not your main server)
3. **Document any special configuration** needed
4. **Submit to YunoHost Apps** organization when stable
5. **Set up CI/CD** for automated testing
6. **Monitor feedback** and iterate

## 📚 Additional Resources

- [YunoHost Packaging Documentation](https://doc.yunohost.org/en/dev/packaging/)
- [Taiga Installation Documentation](https://docs.taiga.io/setup-production.html)
- [YunoHost Apps CI](https://ci-apps.yunohost.org/)
- [YunoHost Forum](https://forum.yunohost.org/)
