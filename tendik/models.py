from django.db import models

# Create your models here.
class Tendik(models.Model):
    no = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.no