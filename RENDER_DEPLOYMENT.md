# 🚀 Deploy to Render — Step-by-Step Guide

## Prerequisites
- GitHub account
- Render account (free tier works)
- Your project code pushed to GitHub

---

## Step 1 — Push to GitHub

```bash
cd skywing_project
git init
git add .
git commit -m "Initial commit - Skywing registration app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/skywing-registration.git
git push -u origin main
```

---

## Step 2 — Create `build.sh` Script

Already included in your project. This file runs during deployment:
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Make it executable:
```bash
chmod +x build.sh
```

---

## Step 3 — Deploy on Render

### 3.1 Create New Web Service
1. Go to https://render.com
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select `skywing-registration` repository

### 3.2 Configure Web Service

| Setting | Value |
|---------|-------|
| **Name** | `skywing-registration` |
| **Region** | Choose closest to your users |
| **Branch** | `main` |
| **Root Directory** | (leave blank) |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn skywing_site.wsgi:application` |
| **Instance Type** | Free (or paid for production) |

### 3.3 Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"**

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.2` |
| `SECRET_KEY` | Generate a new one: https://djecrety.ir |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |

**For SQL Server (if using):**
| Key | Value |
|-----|-------|
| `DB_ENGINE` | `mssql` |
| `DB_NAME` | `skywing_db` |
| `DB_USER` | `your_username` |
| `DB_PASSWORD` | `your_password` |
| `DB_HOST` | `your_server.database.windows.net` |
| `DB_PORT` | `1433` |

### 3.4 Click **"Create Web Service"**

Render will:
1. Clone your repo
2. Run `build.sh` (install deps, collect static files, migrate)
3. Start the app with Gunicorn

---

## Step 4 — Verify Deployment

### Check Static Files
Once deployed, visit:
```
https://your-app-name.onrender.com/static/images/web_banner.jpg
```

You should see the banner image.

### Check the App
```
https://your-app-name.onrender.com/
```

---

## 🔧 Troubleshooting

### Issue: Static files (images, CSS) not loading

**Solution 1 — Verify collectstatic ran:**
Check Render build logs for:
```
Copying static files...
123 static files copied to '/opt/render/project/src/staticfiles'
```

**Solution 2 — Verify WhiteNoise is installed:**
```bash
pip install whitenoise
```

**Solution 3 — Check ALLOWED_HOSTS:**
In Render dashboard → Environment → Add:
```
ALLOWED_HOSTS=your-app-name.onrender.com
```

### Issue: Database errors

**For SQLite (development only):**
SQLite files don't persist on Render free tier. Use PostgreSQL or SQL Server.

**For SQL Server:**
1. Verify environment variables are set
2. Check firewall allows Render IPs
3. Enable "Allow Azure services" in SQL Server

### Issue: 500 Server Error

**Check logs:**
Render Dashboard → Logs tab

**Common fixes:**
- Set `DEBUG=False` in production
- Add your domain to `ALLOWED_HOSTS`
- Run migrations: `python manage.py migrate`

---

## 📝 Post-Deployment Checklist

- [ ] Static files loading correctly (logo, banner, etc.)
- [ ] Form submission works
- [ ] Database connections successful
- [ ] Admin panel accessible at `/admin/`
- [ ] Custom domain configured (if needed)
- [ ] SSL certificate active (automatic on Render)

---

## 🔄 Updating Your App

Every time you push to GitHub:
```bash
git add .
git commit -m "Your changes"
git push origin main
```

Render will automatically:
1. Detect the push
2. Rebuild the app
3. Redeploy with zero downtime

---

## 💰 Cost

**Free Tier:**
- 750 hours/month (enough for 1 app running 24/7)
- Apps sleep after 15 min of inactivity
- First request after sleep takes 30-60 seconds

**Paid ($7/month):**
- No sleeping
- Better performance
- Custom domains

---

## 🌐 Custom Domain (Optional)

1. Render Dashboard → Settings → Custom Domain
2. Add your domain: `www.skywing-africa.com`
3. Add DNS records from Render to your domain provider
4. SSL certificate auto-generated

---

## 🆘 Need Help?

- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Your error logs: Render Dashboard → Logs

