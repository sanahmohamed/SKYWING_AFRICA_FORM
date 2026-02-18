# 🗄️ Microsoft SQL Server Setup Guide

## Step 1 — Install ODBC Driver (on your Windows PC)

Download and install from Microsoft:
👉 https://aka.ms/odbc17

Choose: **ODBC Driver 17 for SQL Server**

---

## Step 2 — Install Python packages

```bash
pip install mssql-django pyodbc
```

---

## Step 3 — Create the Database in SQL Server

Open **SQL Server Management Studio (SSMS)** and run:

```sql
CREATE DATABASE skywing_db;
```

---

## Step 4 — Edit settings.py with your credentials

Open `skywing_site/settings.py` and update:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'skywing_db',          # your database name
        'USER': 'sa',                  # your SQL Server username
        'PASSWORD': 'YourPassword',    # your SQL Server password
        'HOST': 'localhost',           # or your server IP
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes',
        },
    }
}
```

### Using Windows Authentication instead?
Replace the block above with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'skywing_db',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
            'extra_params': 'TrustServerCertificate=yes',
        },
    }
}
```

---

## Step 5 — Run Migrations

```bash
python manage.py migrate
```

Expected output:
```
Applying registration.0001_initial... OK
```

---

## Step 6 — Run the Server

```bash
python manage.py runserver
```

---

## ✅ Verify the table was created

In SSMS, run:
```sql
USE skywing_db;
SELECT * FROM registration_registration;
```

---

## Common Errors

| Error | Fix |
|-------|-----|
| `No module named mssql` | Run `pip install mssql-django` |
| `pyodbc.InterfaceError: No driver` | Install ODBC Driver 17 from Microsoft link above |
| `Login failed for user` | Check USER and PASSWORD in settings.py |
| `Cannot open database` | Make sure `skywing_db` exists in SQL Server |
| `TrustServerCertificate` error | Already handled in settings — make sure OPTIONS block is present |

