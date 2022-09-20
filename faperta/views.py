from django.shortcuts import render

# Create your views here.
def prodi1(request):
    judul = ["Program Studi Agribisnis", "Program Studi Agroekoteknologi", "Program Studi Ilmu Perikanan", "Program Studi Teknologi Pangan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfaperta.html', konteks)