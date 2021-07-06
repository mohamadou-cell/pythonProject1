from django.contrib import admin
from .models import *


@admin.register(Produit)
class Admin_Produit(admin.ModelAdmin):
    list_display = ('Produit_id', 'Code_produit', 'Produit_desc', 'actif')
    list_filter = ('Produit_desc',)


@admin.register(Exportation)
class Admin_Exportation(admin.ModelAdmin):
    list_display = ('Exportation_id', 'Formulaire', 'Produit', 'Pays', 'Qte_vendu_pays', 'Val_produit')
    list_filter = ('Val_produit',)


@admin.register(Exportation_brut)
class Admin_Exportation_brut(admin.ModelAdmin):
    list_display = ('Exportation_id', 'Formulaire', 'Produit', 'Pays', 'Qte_vendu_pays', 'Val_produit')
    list_filter = ('Val_produit',)


