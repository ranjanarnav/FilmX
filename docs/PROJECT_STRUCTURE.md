# 📂 Project Structure — FilmX

This document explains the structure of the FilmX Django project.

---

# Root Directory

```
C:.
│ .gitignore
│ manage.py
│ README.md
│ requirements.txt
```

---

# 📁 media/

Stores uploaded content.

```
media/
├── movies/ # Uploaded movie video files
└── thumbnails/ # Uploaded movie thumbnails
```


⚠️ This folder is ignored in GitHub.

---

# 📁 movies/ (Main Application)

This is the main Django app responsible for movie functionality.

```
movies/
│ admin.py # Admin panel configuration
│ apps.py # App configuration
│ models.py # Database models
│ tests.py # Test cases
│ urls.py # App URLs
│ views.py # Business logic
│ init.py
```

---

# 📁 movies/migrations/

Stores database migration files.

```
migrations/
│ 0001_initial.py
│ init.py
```


These files define database structure.

---

# 📁 movies/static/movies/

Contains static frontend files.

```
static/
└── movies/
├── css/
│ style.css # Main stylesheet
│
├── images/ # Static images
│
└── js/
script.js # JavaScript logic
```

Used for:

- Styling
- Animations
- UI logic

---

# 📁 movies/templates/

Contains HTML templates.

```
templates/
│ base.html

└── movies/
browse.html
index.html
watch.html
```

Template roles:

| File        | Purpose       |
|-------------|---------------|
| base.html   | Base layout   |
| index.html  | Homepage      |
| browse.html | Movie listing |
| watch.html  | Video player  |

---

# 📁 NetFlix/ (Project Configuration)

Main Django project folder.

```
NetFlix/
│ asgi.py
│ settings.py
│ urls.py
│ wsgi.py
│ init.py
```


File roles:

| File        | Purpose               |
|-------------|-----------------------|
| settings.py | Project configuration |
| urls.py     | Main URL routing      |
| wsgi.py     | Deployment interface  |
| asgi.py     | Async interface       |

---

# 📄 manage.py

Main Django management script.

Used for:

- Running server
- Migrations
- Admin creation

Example commands:

```
python manage.py runserver  
python manage.py migrate  
python manage.py createsuperuser  
```

---

# 📄 requirements.txt

Contains project dependencies.

Used to install required packages.

---

# 📄 .gitignore

Prevents unnecessary files from being uploaded to GitHub.

Ignored items:

- db.sqlite3
- media/
- staticfiles/
- __pycache__/

---

# 📊 Application Flow

User Flow:

User → Homepage → Browse Movies → Watch Movie

Admin Flow:

Admin → Login → Add Category → Upload Movie → Save