# Quick Installation Guide - Taiga on YunoHost

## Your Setup
- **GitHub Repository:** https://github.com/unedeplus/taiga_ynh
- **YunoHost Server:** https://192.168.1.170/yunohost/admin/
- **Local IP:** 192.168.1.170

---

## Option 1: Install via Web Admin (Recommended)

1. **Access your YunoHost admin panel:**
   - Go to: https://192.168.1.170/yunohost/admin/
   - Navigate to: **Applications** → **Install**

2. **Install from custom URL:**
   - Click on "Install custom app" or look for URL input
   - Enter: `https://github.com/unedeplus/taiga_ynh`
   - Click **Install**

3. **Fill installation form:**
   - **Domain:** Choose your domain (e.g., `192.168.1.170` or your actual domain)
   - **Path:** `/taiga` (or any path you prefer)
   - **Admin user:** Select a YunoHost user to be Taiga admin
   - **Password:** Set a strong password for Taiga admin
   - **Public access:** Choose "Visitors" for public or "All users" for private

4. **Wait for installation:**
   - Installation takes 10-20 minutes (building frontend)
   - Monitor progress in the web interface

---

## Option 2: Install via SSH/CLI

### Step 1: Connect to your server
```bash
ssh admin@192.168.1.170
# or
ssh root@192.168.1.170
```

### Step 2: Install the app
```bash
# Install from GitHub directly
sudo yunohost app install https://github.com/unedeplus/taiga_ynh

# You'll be prompted for:
# - Domain: 192.168.1.170 (or your domain)
# - Path: /taiga
# - Admin user: your_username
# - Password: ********
```

### Step 3: Or with inline arguments
```bash
sudo yunohost app install https://github.com/unedeplus/taiga_ynh \
  --args "domain=192.168.1.170&path=/taiga&admin=yourusername&password=YourSecurePassword123"
```

---

## Option 3: Install from Local Copy (Testing)

If you want to test modifications before pushing to GitHub:

### Step 1: Transfer the package to server
```bash
# From your local machine
cd /media/psychen/NEXTCLOUD-2/NEXTCLOUD-Psychen/VSCODE-FOLDER/

# Create a tarball (excluding git files)
tar -czf taiga_ynh.tar.gz \
  --exclude='.git' \
  --exclude='taiga_ynh' \
  --exclude='*.md' \
  -C 20251129-TAIGA-Yunohost-App \
  .

# Transfer to server
scp taiga_ynh.tar.gz admin@192.168.1.170:/tmp/
```

### Step 2: Install on server
```bash
# SSH to server
ssh admin@192.168.1.170

# Extract package
cd /tmp
mkdir -p taiga_ynh_install
tar -xzf taiga_ynh.tar.gz -C taiga_ynh_install/

# Install
sudo yunohost app install /tmp/taiga_ynh_install
```

---

## After Installation

### 1. Access Taiga
- URL: `https://192.168.1.170/taiga/` (or your domain)
- Login with the admin credentials you set during installation

### 2. Check Services Status
```bash
ssh admin@192.168.1.170

# Check Taiga services
sudo systemctl status taiga
sudo systemctl status taiga-celery

# Check logs
sudo journalctl -u taiga -n 50 --no-pager
sudo journalctl -u taiga-celery -n 50 --no-pager
```

### 3. Verify Installation
```bash
# Check app is installed
sudo yunohost app list | grep taiga

# Check app info
sudo yunohost app info taiga
```

---

## Troubleshooting

### Installation Fails
```bash
# Check installation logs
sudo cat /var/log/yunohost/categories/operation/operation_*.log | tail -100

# Or in web admin: Tools → Logs → Recent operations
```

### Services Not Running
```bash
# Restart services
sudo systemctl restart taiga
sudo systemctl restart taiga-celery

# Check detailed logs
sudo journalctl -u taiga -f
```

### Access Issues
```bash
# Check nginx configuration
sudo nginx -t
sudo systemctl reload nginx

# Check permissions
sudo yunohost app info taiga
```

### Database Issues
```bash
# Check PostgreSQL
sudo systemctl status postgresql
sudo -u postgres psql -c "\l" | grep taiga
```

---

## Next Steps After Installation

### Configure Email (Optional)
Edit the Django settings to add SMTP:
```bash
sudo nano /var/www/taiga/taiga-back/settings/local.py

# Add:
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.example.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "your-email@example.com"
# EMAIL_HOST_PASSWORD = "your-password"

# Restart service
sudo systemctl restart taiga
```

### Enable Public Registration (Optional)
```bash
sudo nano /var/www/taiga/taiga-back/settings/local.py

# Change:
# PUBLIC_REGISTER_ENABLED = True

sudo systemctl restart taiga
```

---

## Important Notes

✅ **Installation takes 10-20 minutes** - Frontend compilation is resource-intensive
✅ **Minimum 512MB RAM required** - 1GB recommended
✅ **First access may be slow** - Allow services to fully start
✅ **WebSocket support included** - Real-time updates work out of the box
✅ **Multi-instance supported** - You can install multiple Taiga instances

---

## Quick Commands Reference

```bash
# Install
sudo yunohost app install https://github.com/unedeplus/taiga_ynh

# Remove
sudo yunohost app remove taiga

# Backup
sudo yunohost backup create --apps taiga

# Restore
sudo yunohost backup restore BACKUP_NAME --apps taiga

# Upgrade
sudo yunohost app upgrade taiga

# Change URL
sudo yunohost app change-url taiga --new-path /new-path

# Logs
sudo journalctl -u taiga -f
```

---

**Ready to install!** All package validations passed. Choose your preferred installation method above.
