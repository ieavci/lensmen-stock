from django.urls import path
from . import views

"""
http://127.0.0.1:8000/
http://127.0.0.1:8000/home
http://127.0.0.1:8000/photos
http://127.0.0.1:8000/photos/1
"""

urlpatterns=[
    path('', views.home, name='home'),
    path('home', views.home),
    path('photos', views.photos, name='photos'),
    path('kategori/<int:id>', views.kategori, name='kategori'),
    path('photos/<int:id>', views.photo_story, name='story'),
    path('about_us', views.about_us,name='about_us'),
    
]