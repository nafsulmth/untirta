from django.db import models


# Create your models here
class Mahasiswa(models.Model):
    no = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    ttl = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media/',blank=True, null=True)
    

    def __str__(self):
        return self.no