from django.contrib import admin
from .models import *

@admin.register(Typ_alteration)
class Admin_Typ_alteration(admin.ModelAdmin):
    list_display=('Typ_alteration_desc', 'actif')
    list_filter=('Typ_alteration_desc',)

@admin.register(Alteration)
class Admin_Alteration(admin.ModelAdmin):
    list_display=('Formulaire', 'Titre_minier', 'Typ_alteration', 'Mineral', 'Alteration_yn', 'Mineral_desc')
    list_filter=('Mineral_desc',)

@admin.register(Alteration_mineral_rel)
class Admin_Alteration_mineral_rel(admin.ModelAdmin):
    list_display=('Typ_alteration', 'Mineral')
    list_filter=('Typ_alteration',)

@admin.register(Mineral)
class Admin_Mineral(admin.ModelAdmin):
    list_display=('Mineral_desc', 'actif')
    list_filter=('Mineral_desc',)
