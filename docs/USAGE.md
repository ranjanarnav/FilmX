# 🎬 FilmX Usage Guide

This document explains how to use the FilmX movie streaming platform, including how to manage movies using the Django admin panel.

---

# 🧑‍💼 Admin Usage

All movie content is managed through the Django Admin Panel.

Open:

http://127.0.0.1:8000/admin/

Login using your admin credentials.

---

# 📂 Step 1 — Create Categories

Before uploading movies, create categories.

Go to:

Movies → Category → Add Category

Fill:

- Category Name  
  Example:
  - Action
  - Comedy
  - Horror
  - Sci-Fi
  - Drama

Click:

Save

Categories will now be available when uploading movies.

---

# 🎬 Step 2 — Upload Movies

Go to:

Movies → Movie → Add Movie

Fill the following fields:

## Required Fields

### 🎞 Movie Name

Enter the movie title.

Example:

Avengers: Endgame

---

### 📝 Description

Add movie description.

Example:

A group of superheroes unite to defeat a powerful enemy.

---

### 🖼 Thumbnail

Upload movie poster image.

Recommended:

- Format: JPG or PNG
- Size: 500×750 pixels
- High-quality poster image

---

### 🎬 Movie File

Upload video file.

Supported formats:

- .mp4 (Recommended)
- .mkv
- .webm

Best format:

MP4 (H.264)

---

### 🎭 Category

Select category created earlier.

Example:

Action

---

Click:

Save

Your movie will now appear on the website.

---

# 🔍 Search Movies

Users can search movies using the search bar.

Search supports:

- Movie name
- Partial matches

Example searches:

Avengers  
Spider  
Batman  

Matching results will appear automatically.

---

# 🎥 Watching Movies

Users can:

1. Open the website homepage
2. Browse available movies
3. Click on movie thumbnail
4. Open movie detail page
5. Click play
6. Start watching video

Movies stream directly in the browser.

---

# 🧹 Managing Movies

Admins can edit or delete movies.

To edit:

Movies → Movie → Select Movie → Edit → Save

To delete:

Movies → Movie → Select Movie → Delete

---

# 📁 Media Storage

Uploaded files are stored inside:

media/

Typical structure:

media/
├── thumbnails/
├── movies/

Do NOT upload media files to GitHub.

They are ignored using `.gitignore`.

---

# ⚠️ Important Notes

- Always create categories before movies
- Use optimized video files
- Keep thumbnails lightweight
- Avoid very large files in development

---

# 🧪 Example Workflow

Typical admin workflow:

1. Create Category → Action  
2. Upload Movie → John Wick  
3. Upload Thumbnail  
4. Upload Video  
5. Select Category  
6. Save  
7. Movie appears on homepage  

---

# 👨‍💻 User Workflow

Typical user workflow:

1. Open homepage  
2. Browse movies  
3. Search movie  
4. Select movie  
5. Click play  
6. Watch movie  

---

# 🔮 Future Usage Improvements

Possible future features:

- User login system
- Watch history
- Favorites list
- Movie ratings
- Recommendations
- Subscriptions