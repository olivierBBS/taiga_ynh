# Taiga YunoHost App: Licensing & Publishing Guide

## 1. Licensing & Permissions

### Is it allowed to host this on a public GitHub?
**Yes, absolutely.**

*   **Taiga's License:** Taiga (the software itself) is licensed under the **MPL 2.0 (Mozilla Public License 2.0)**. This is a permissive open-source license that explicitly allows you to:
    *   Use the software for any purpose (including commercial).
    *   Modify the software.
    *   Distribute the software.
    *   Host it on your own server (Self-Hosting).

*   **Your Repository's License:** Your YunoHost package scripts are licensed under **AGPL-3.0** (GNU Affero General Public License v3.0). This is the standard and recommended license for YunoHost applications. It ensures that improvements to the packaging scripts remain open source.

### Does the Taiga Team allow this?
**Yes.** The Taiga team actively supports the open-source community. They provide the source code specifically so people can self-host it. Creating a YunoHost package (which makes self-hosting easier) is exactly the kind of community contribution open-source projects encourage.

*Note: You are packaging the "Community Edition" of Taiga. As long as you don't claim to be the official "Taiga Cloud" service or violate their trademark (e.g., by pretending to be the company Taiga.io), you are in the clear.*

---

## 2. How to Add to the YunoHost Catalog

Getting your app into the official YunoHost catalog allows other users to install it easily via the Web Admin interface.

### Step 1: Final Validation (Quality Assurance)
Before submitting, ensure the app meets the quality standards:
1.  **Install/Remove:** Verify `install` and `remove` work cleanly (no leftover files/databases).
2.  **Upgrade:** Verify that `upgrade` works (e.g., bumping the version number in `manifest.toml` and running an upgrade).
3.  **Backup/Restore:** Verify you can backup the app and restore it successfully (we just fixed this!).
4.  **CI/CD:** YunoHost has an automated testing tool called `package_check`.

### Step 2: Run Package Check
You can run the YunoHost CI tools locally or rely on their infrastructure later.
To test locally (if you have `yunohost-dev` tools installed):
```bash
yunohost app check https://github.com/olivierBBS/taiga_ynh/tree/main
```
*This will run a series of automated tests (install, backup, restore, remove, etc.) and give you a score (Level 0 to Level 8).*

### Step 3: Submit to the YunoHost Community
Once your app is working well:

1.  **Publish on the Forum:**
    *   Create a new topic in the [YunoHost Forum > Apps > Apps in progress](https://forum.yunohost.org/c/apps/apps-in-progress/16).
    *   Title it "[New App] Taiga - Project Management Platform".
    *   Describe the app and ask for testers.

2.  **Request Inclusion in the Catalog:**
    *   The official list of apps is maintained in the `apps` repository.
    *   Once you have positive feedback from testers, you can ask the YunoHost apps team (on the forum or Matrix chat) to include it in the community list.
    *   They will review your code (checking for security, best practices, and license compliance).

### Step 4: Maintenance
Once accepted:
*   You become the **Maintainer**.
*   When Taiga releases a new version (e.g., 6.8.0), you will need to:
    1.  Update the version in `manifest.toml`.
    2.  Update the `conf.json` or `local.py` if Taiga changed configuration requirements.
    3.  Test the upgrade.
    4.  Push the changes to your repo.

## Summary
You are doing great work! This package is a valuable contribution to the YunoHost ecosystem. The licensing is correct, and the path to publishing is open.

**Next Immediate Step:**
Finish verifying the installation at the root path (`/`) as discussed. Once that works, you are ready to announce it on the YunoHost forum!
