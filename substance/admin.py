from django.contrib import admin
from .models import *


@admin.register(Substance)
class Admin_Substance(admin.ModelAdmin):
    list_display = ('Substance_desc', 'actif')
    list_filter = ('Substance_desc',)


@admin.register(Extraction)
class Admin_Extraction(admin.ModelAdmin):
    list_display = ('Formulaire', 'Substance', 'Qte_brut', 'Cout_production', 'Qte_transform', 'Autres_min')
    list_filter = ('Qte_transform',)


@admin.register(Extraction_brut)
class Admin_Extraction_brut(admin.ModelAdmin):
    list_display = ('Formulaire', 'Substance', 'Qte_brut', 'Cout_production', 'Qte_transform')
    list_filter = ('Qte_transform',)

@admin.register(Titre_substance_rel)
class Admin_Titre_substance_rel(admin.ModelAdmin):
    list_display = ('Titre_minier', 'Substance', 'Commune', 'Autres_subst')
    list_filter = ('Autres_subst',)

@admin.register(Benefic_typ)
class Admin_Benefic_typ(admin.ModelAdmin):
    list_display = ('Benefic_typ_desc')
    list_filter = ('Benefic_typ_desc',)

