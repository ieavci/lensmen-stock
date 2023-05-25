from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name
    
    

class Photo(models.Model):
    foto_adi = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    foto_adi = models.CharField(max_length=100)
    foto_aciklama = models.TextField()
    foto_veri = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)

    def str(self):
        return self.foto_adi   
    
    

"""class Category(models.Model):
    name = models.CharField(max_length=100)
    


class Photo(models.Model):
    foto_adi = models.CharField(max_length=100)
    foto_aciklama = models.TextField()
    foto_veri = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
   
"""

    
