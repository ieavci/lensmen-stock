from django.shortcuts import render
from .models import Category, Photo
"""category_list=['Sokak','Savaş','Doğa','Hayvan']
photo_list=[

    {
        'id':1,
        'foto_adi':'fotoğraf 1',
        'foto_aciklama':'fotoğraf açıklama',
        'foto_veri':'1.jpeg',
        'anasayfa':False,
    },
    {
        'id':2,
        'foto_adi':'fotoğraf 2',
        'foto_aciklama':'fotoğraf açıklama',
        'foto_veri':'2.jpg',        
        'anasayfa':True,
    },
    {
        'id':3,
        'foto_adi':'fotoğraf 3',
        'foto_aciklama':'fotoğraf açıklama',
        'foto_veri':'3.jpg',
        'anasayfa':True,
    },
    {
        'id':4,
        'foto_adi':'fotoğraf 4',
        'foto_aciklama':'fotoğraf açıklama',
        'foto_veri':'4.jpg',
        'anasayfa':False,
    },
]
"""
# Create your views here.

def home(requset):
    data={
        'categories':Category.objects.all(),           #category_list içindeki elemanlar için veri oluşturma
        'photos':Photo.objects.filter(anasayfa=True)    
    }
    return render(requset,'index.html',data)

def photos(requset):
    data={
       'categories':Category.objects.all(),       
       'photos':Photo.objects.all()    
    }
    return render(requset,'photos.html',data)
def kategori(requset,id):
    category = Category.objects.get(id=id)
    photos = Photo.objects.filter(category=category)
    
    data={
        'categories':Category.objects.all(),
        'category': category,
        'photos': photos,
         
        }
    return render(requset,'kategori.html',data)
def photo_story(requset,id):
    data={
              
        'photo':Photo.objects.get(id=id)
    }
    return render(requset,'story.html',data)
def about_us(requset):  
    
    return render(requset,'about_us.html')

