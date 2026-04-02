from django.shortcuts import render, get_object_or_404
from .models import Movie, Category

def home(request):
    return render(request, "movies/index.html")

def browse(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()

    q = request.GET.get("q")
    if q:
        movies = movies.filter(title__icontains=q)

    genre = request.GET.get("genre")
    if genre:
        movies = movies.filter(category_id=genre)

    sort = request.GET.get("sort")
    if sort == "oldest":
        movies = movies.order_by("release_date")
    elif sort == "title":
        movies = movies.order_by("title")
    else:
        movies = movies.order_by("-release_date")

    return render(request, "movies/browse.html", {"movies": movies, "categories": categories})

def watch(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, "movies/watch.html", {"movie": movie})
