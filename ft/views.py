from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judul = ["Jurusan Teknik Elektro", "Jurusan Teknik Industri", "Jurusan Teknik Kimia", "Jurusan Teknik Mesin", "Jurusan Teknik Metalurgi", "Jurusan Teknik Sipil"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexft.html', konteks)