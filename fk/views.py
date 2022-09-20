from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["Prodi Kedokteran", "Prodi Keperawatan S1", "Prodi Keperawatan D3", "Prodi S1 Gizi", "Prodi Ilmu Keolahragaan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfk.html', konteks)