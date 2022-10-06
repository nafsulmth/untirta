from django.shortcuts import render
from mahasiswa.models import Mahasiswa
# Create your views here.
def mahasiswa(request):
    context = {
        'student': Mahasiswa.objects.all()
        
    }
    return render(request,"mahasiswa.html", context)