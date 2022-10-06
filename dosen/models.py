from django.db import models 

# Create your models here.
class Dosen(models.Model):
    no = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100, null=True)
    fakultas = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media/',blank=True, null=True)
    

    def __str__(self):
        return self.no