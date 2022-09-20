from django.shortcuts import render

# Create your views here.
def prodi9(request):
    judul = ["Nama: Nafsul Muthmainnah", "NIM: 2225210037", "Kelas: 3A", "Domisili: Pandeglang, Banten", "Hobi: Membaca dan Menulis", "Instagram: https://instagram.com/nafsulmth/", "LinkedIn: https://www.linkedin.com/in/nafsul-mutmainah-42377a24a/"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexprofil.html', konteks)