from django.contrib import admin
from .models import *


@admin.register(Typ_rapport)
class Admin_Typ_rapport(admin.ModelAdmin):
    list_display = ('Nm_typ_rapport')
    list_filter = ('Nm_typ_rapport',)


@admin.register(Rapport)
class Admin_Rapport(admin.ModelAdmin):
    list_display = ('Rapport_nom', 'Rapport_annuel', 'Rapport_trimestriel', 'Rapport_entreprise', 'Rapport_actif', 'Rapport_excel')
    list_filter = ('Rapport_excel',)


@admin.register(Liste_rapport)
class Admin_Liste_rapport(admin.ModelAdmin):
    list_display = ('Typ_rapport', 'Rapport', 'Nm_rpt_executable', 'Rapport_titre', 'Rapport_desc')
    list_filter = ('Rapport_desc',)

