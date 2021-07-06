from django.contrib import admin
from .models import *


@admin.register(Pays)
class Admin_Pays(admin.ModelAdmin):
    list_display = ('Pays_cd', 'nom_pays', 'actif')
    list_filter = ('Pays_cd',)


@admin.register(Region)
class Admin_Region(admin.ModelAdmin):
    list_display = ('region_cd', 'nom_region')
    list_filter = ('region_cd',)


@admin.register(Departement)
class Admin_Departement(admin.ModelAdmin):
    list_display = ('Region', 'nom_departement')
    list_filter = ('nom_departement',)

@admin.register(Commune)
class Admin_Commune(admin.ModelAdmin):
    list_display = ('Departement', 'nom_commune')
    list_filter = ('nom_commune',)
