# Fix: ModuleNotFoundError: No module named 'mssql'

## The Problem
The `mssql-django` package is not installed in your virtual environment.

## The Fix — Run these commands ONE BY ONE in your terminal:

### Step 1 — Make sure your venv is activated
```
C:\skywing_registration_django\venv\Scripts\activate
```
You should see `(venv)` at the start of your prompt.

### Step 2 — Install the required packages
```
pip install mssql-django
pip install pyodbc
```

### Step 3 — Verify installation
```
pip show mssql-django
```
You should see version info if installed correctly.

### Step 4 — Now run migrations
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## If pip install fails (SSL or network error):
```
pip install mssql-django --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

## If ODBC Driver error appears after install:
Download and install ODBC Driver 17 from:
https://aka.ms/odbc17
