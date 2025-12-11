# Investigation Summary: Taiga on YunoHost

## Current Status
The installation fails during the database migration step (`python manage.py migrate`).

## The Error
```
psycopg2.OperationalError: connection to server at "127.0.0.1", port 5432 failed: FATAL:  password authentication failed for user "taiga"
```
This error indicates that the application is attempting to connect to PostgreSQL via TCP/IP on `127.0.0.1`. However, the authentication fails, likely because the `taiga` database user is configured to use `peer` or `md5` authentication over Unix Domain Sockets, not TCP/IP.

## Configuration vs. Reality
1.  **Intended Configuration**: We are configuring Django to use Unix Domain Sockets.
    *   File: `conf/local.py`
    *   Setting: `"HOST": "/var/run/postgresql"`
    *   Setting: `"PORT": ""`

2.  **Verified on Disk**:
    *   Debug logs confirm that `local.py` is generated correctly on the server with the settings above.

3.  **Runtime Behavior**:
    *   Despite the config file explicitly setting the socket path, the error message proves that `psycopg2` is trying to connect to `127.0.0.1`.
    *   **Root Cause Found**: `manage.py` defaults to `settings.common` if `DJANGO_SETTINGS_MODULE` is not set. `settings.common` defaults to `127.0.0.1`. The `scripts/install` script was not setting this environment variable when calling `manage.py`.

## Debugging Findings
1.  **`psql` Connectivity (Confirmed)**:
    *   We injected a `psql` command into the install script.
    *   **Result**: Success. The `taiga` user can connect to the database using the generated password via the `/var/run/postgresql` socket. This rules out issues with the database creation or user permissions.

2.  **Python/Django Debugging (Confirmed)**:
    *   We injected a Python script to print the loaded Django settings and environment variables.
    *   **Result**: When `settings.local` is explicitly loaded, the configuration is correct (`HOST: /var/run/postgresql`) and `psycopg2` can connect via socket.
    *   **Conclusion**: The issue is not with the settings file or the environment, but with *which* settings file Django is loading during `manage.py` execution.

## Resolution
We have modified `scripts/install` and `scripts/upgrade` to explicitly set `DJANGO_SETTINGS_MODULE=settings.local` for all `manage.py` calls.

## New Issue: Missing Dependency
After fixing the settings loading, the installation failed with:
```
django.core.cache.backends.base.InvalidCacheBackendError: Could not find backend 'django_redis.cache.RedisCache': No module named 'django_redis'
```
This indicates that `django-redis` is required by `settings.local` but is not installed by default. We have added `django-redis` to the pip install commands in `scripts/install` and `scripts/upgrade`.

## Next Steps
Ask the user to run the installation again to verify the fix.
