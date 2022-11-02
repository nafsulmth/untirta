from django.shortcuts import render, redirect
from mahasiswa.models import Mahasiswa
from mahasiswa.forms import FormMahasiswa
from django.contrib import messages

# Create your views here.
def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()
    if request.method == "POST":
        mahasiswa.hapus()

    return redirect('/mahasiswa/')


def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form': form,
            'mahasiswa': mahasiswa,
        }
    return render(request, template, konteks)



def mahasiswa(request):

    konteks = {
        'student': Mahasiswa.objects.all()
    }    
    return render(request, 'mahasiswa.html', konteks)


def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil ditambahkan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-mahasiswa.html', konteks)