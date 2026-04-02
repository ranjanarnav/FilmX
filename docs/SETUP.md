# ⚙️ FilmX Setup Guide

This guide explains how to install and run the FilmX Django movie streaming project locally.

Follow each step carefully.

---

# 📋 Requirements

Before running this project, make sure you have:

- Python 3.9 or higher
- pip (Python package manager)
- Git (optional but recommended)

Check Python version:

```
python --version
```

---

# 📥 Step 1 — Download Project

Option 1 — Clone using Git:

```
git clone https://github.com/ranjanarnav/FilmX.git
```

cd FilmX

Option 2 — Download ZIP:

1. Click "Code"
2. Click "Download ZIP"
3. Extract the folder
4. Open terminal inside project folder

---

# 📦 Step 2 — Install Dependencies

Install required packages:

```
pip install -r requirements.txt
```

This installs Django and required libraries.

---

# 🗃 Step 3 — Apply Database Migrations

Run:

```
python manage.py makemigrations
```
```
python manage.py migrate
```

This will create the database structure.

---

# 👤 Step 4 — Create Admin User

Create superuser:

```
python manage.py createsuperuser
```

Enter:

Username:
Email:
Password:

This account will be used to access admin panel.

---

# ▶️ Step 5 — Run Development Server

Start server:

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

Your FilmX website should now be running.

---

# 🔐 Step 6 — Access Admin Panel

Open:

```
http://127.0.0.1:8000/admin/
```

Login using:

- Username
- Password

You can now:

- Create categories
- Upload movies
- Manage content

---

# 📁 Media Setup

If media folder does not exist, create:

```
media/
```

Inside media folder, Django will store:

- Movie thumbnails
- Movie video files

Example:

media/
├── thumbnails/
├── movies/

Do NOT upload media files to GitHub.

---

# 📂 Static Files Setup (Optional)

If running in production:

```
python manage.py collectstatic
```

This will create:

staticfiles/

Used for deployment only.

---

# 🧪 Verify Installation

If setup is successful:

- Homepage loads
- Admin panel works
- Movies can be uploaded
- Videos can be played

---

# ❗ Common Issues & Fixes

## Issue: ModuleNotFoundError

Fix:

```
pip install -r requirements.txt
```

---

## Issue: Database error

Fix:

Delete:

`db.sqlite3`

Then run:

```
python manage.py migrate
```

---

## Issue: Media not loading

Check:

settings.py contains:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

---

# 🧹 After Setup — Next Steps

Once setup is complete:

1. Create Categories
2. Upload Movies
3. Upload Thumbnails
4. Test Video Playback

For usage instructions:

➡️ See **USAGE.md**

---

# 🚀 Running in Production (Future)

For production deployment, you may use:

- Gunicorn
- Nginx
- VPS hosting
- Cloud storage for media

Production setup guide can be added later.

---

# 🧠 Developer Notes

Default Database:

`SQLite`

Admin Access:

```
/admin/
```

Main App:

`movies`

---

# ✅ Setup Complete

If everything runs successfully, FilmX is ready to use.