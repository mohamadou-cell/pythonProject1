from django.contrib import admin
from .models import *


@admin.register(Typ_resrc_reserv)
class Admin_Typ_resrc_reserv(admin.ModelAdmin):
    list_display = ('Resrc_reserv_desc', 'actif')
    list_filter = ('Resrc_reserv_desc',)


@admin.register(Unite_mesr_minrlstn)
class Admin_Unite_mesr_minrlstn(admin.ModelAdmin):
    list_display = ('Unite_mesr_desc', 'actif')
    list_filter = ('Unite_mesr_desc',)


@admin.register(Unite_mesr_substnc)
class Admin_Unite_mesr_substnc(admin.ModelAdmin):
    list_display = ('Unite_mesr_desc', 'actif')
    list_filter = ('Unite_mesr_desc',)

@admin.register(Exploitatn_resrc_reserv)
class Admin_Exploitatn_resrc_reserv(admin.ModelAdmin):
    list_display = ('Entreprise', 'Titre_minier', 'Produit', 'Typ_resrc_reserv', 'Typ_resrc_reserv_autre',
                    'Tonnage', 'Unite_mesr', 'Unite_mesr_autre', 'Teneur', 'Teneur_coupure', 'Autre_substances')
    list_filter = ('Autre_substances',)

@admin.register(Exploratn_resrc_reserv)
class Admin_Exploratn_resrc_reserv(admin.ModelAdmin):
    list_display = ('Entreprise', 'Titre_minier', 'Produit', 'Typ_resrc_reserv', 'Typ_resrc_reserv_autre',
                    'Tonnage', 'Unite_mesr', 'Unite_mesr_autre', 'Teneur', 'Teneur_coupure', 'Autre_substances')
    list_filter = ('Autre_substances',)

