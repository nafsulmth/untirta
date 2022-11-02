from django.shortcuts import render
from tendik.models import Tendik
from tendik.forms import FormTendik
# Create your views here.
def tendik(request):
    context = {
        'student': Tendik.objects.all()
        
    }
    return render(request,"tendik.html", context)
def tambah_tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data berhasil ditambahkan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tendik.html', konteks)
    else:
        form = FormTendik()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-tendik.html', konteks)
