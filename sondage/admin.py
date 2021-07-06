from django.contrib import admin
from .models import *


@admin.register(Typ_sondage)
class Admin_Typ_sondage(admin.ModelAdmin):
    list_display = ('Sondage_desc', 'actif')
    list_filter = ('Sondage_desc',)


@admin.register(Exploitation_sondage)
class Admin_Exploitation_sondage(admin.ModelAdmin):
    list_display = ('Formulaire', 'Titre_minier', 'Typ_sondage', 'Inters_u_mesr_id', 'Typ_sondage_autre',
                    'Grille_maille_desc', 'Metrage', 'Intervalle', 'Intersection', 'Teneur')
    list_filter = ('Metrage',)


@admin.register(Exploration_sondage)
class Admin_Exploration_sondage(admin.ModelAdmin):
    list_display = ('Formulaire', 'Titre_minier', 'Typ_sondage', 'Inters_u_mesr_id', 'Typ_sondage_autre',
                    'Grille_maille_desc', 'Metrage', 'Intervalle', 'Intersection', 'Teneur')
    list_filter = ('Metrage',)

