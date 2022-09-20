from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = ["Program Studi Administrasi Publik", "Program Studi Ilmu Komunikasi", "Program Studi Ilmu Pemerintahan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfisip.html', konteks)