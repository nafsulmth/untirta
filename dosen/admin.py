from django.contrib import admin
from dosen.models import Dosen
# Register your models here.

class DosenAdmin(admin.ModelAdmin):
    list_display = ['no', 'nip', 'nama', 'jabatan', 'fakultas', 'email', 'foto']
    search_fields = ['nip', 'nama']


admin.site.register(Dosen, DosenAdmin)