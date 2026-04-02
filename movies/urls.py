from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Landing page
    path('browse/', views.browse, name='browse'),      # Browse movies
    path('watch/<int:movie_id>/', views.watch, name='watch'),  # Watch movie
]
