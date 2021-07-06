from django.contrib import admin
from .models import *


@admin.register(Typ_analyse)
class Admin_Typ_analyse(admin.ModelAdmin):
    list_display = ('Analyse_desc', 'actif')
    list_filter = ('Analyse_desc',)


@admin.register(Exploitation_analyse)
class Admin_Exploitation_analyse(admin.ModelAdmin):
    list_display = ('Formulaire', 'Titre_minier', 'Typ_analyse', 'Pays', 'Typ_analyse_autre', 'Typ_analyse_autre', 'Nom_laboratoire')
    list_filter = ('Nom_laboratoire',)


@admin.register(Exploration_analyse)
class Admin_Exploration_analyse(admin.ModelAdmin):
    list_display = ('Formulaire', 'Titre_minier', 'Typ_analyse', 'Pays', 'Typ_analyse_autre', 'Typ_analyse_autre', 'Nom_laboratoire')
    list_filter = ('Nom_laboratoire',)

