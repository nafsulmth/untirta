from django.shortcuts import render
from dosen.models import Dosen
# Create your views here.
def dosen(request):
    context = {
        'lecturer': Dosen.objects.all()
        
    }
    return render(request,"dosen.html", context)