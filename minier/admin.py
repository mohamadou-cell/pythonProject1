from django.contrib import admin
from .models import *


@admin.register(Nature_titre_minier)
class Admin_Nature_titre_minier(admin.ModelAdmin):
    list_display = ('Nature_tminier_cd', 'nom_nature')
    list_filter = ('Nature_tminier_cd',)


@admin.register(Titre_minier)
class Admin_Titre_minier(admin.ModelAdmin):
    list_display = ('Entreprise', 'Num_titre_minier', 'Nom_perimetre')
    list_filter = ('Nom_perimetre',)


@admin.register(Exploratn_details)
class Admin_Exploratn_details(admin.ModelAdmin):
    list_display = ('Titre_minier', 'Formulaire', 'Exploratn_details_id', 'Nbr_tranchee', 'Nbr_prosp_avance', 'Nbr_prosp_prelmnr', 'Da_saprolit_oxyd', 'Da_saprok', 'Da_roche_saine', 'Da_autre_ind', 'Da_autre_desc', 'Ah_silicificatn',
                    'Ah_albitisatn', 'Ah_sericitisatn', 'Ah_silicecarbonage', 'Ah_saprolit_oxyd', 'Ah_autre_ind', 'Ah_autre_desc', 'As_sulfur', 'As_pyrite', 'As_calcopyrite', 'As_arsenopyrite', 'As_pyrothite', 'As_autre_ind', 'As_autre_desc')
    list_filter = ('As_autre_desc',)


@admin.register(Tranchee)
class Admin_Tranchee(admin.ModelAdmin):
    list_display = ('Entreprise', 'Titre_minier', 'Tranchee_desc', 'Longueur', 'Profondeur', 'Faibl_intervalle', 'Faibl_intersectn',
                    'Faibl_u_mesr_id', 'Moyen_intervalle', 'Moyen_intersection', 'Moyen_u_mesr_id', 'Elev_intervalle', 'Elev_intersectn', 'Elev_u_mesr_id')
    list_filter = ('Tranchee_desc',)

@admin.register(Typ_geophysique)
class Admin_Typ_geophysique(admin.ModelAdmin):
    list_display = ('Typ_geophysique_desc', 'actif')
    list_filter = ('Typ_geophysique_desc',)

@admin.register(Geophysique)
class Admin_Geophysique(admin.ModelAdmin):
    list_display = ('Entreprise', 'Titre_minier', 'Typ_geophysique', 'Typ_geochimie_autre', 'Nbr_ligne',
                    'Superficie_km2', 'Altitude_vol', 'Distance_lign_vol', 'Magnetique', 'Radiometrique', 'electromagnetiq')
    list_filter = ('Magnetique',)

@admin.register(Typ_geochimie)
class Admin_Typ_geochimie(admin.ModelAdmin):
    list_display = ('Typ_geochimie_desc', 'actif')
    list_filter = ('Typ_geochimie_desc',)

@admin.register(Typ_cartgrph)
class Admin_Typ_cartgrph(admin.ModelAdmin):
    list_display = ('Typ_cartgrph_desc', 'actif')
    list_filter = ('Typ_cartgrph_desc',)

@admin.register(Cartographie)
class Admin_Cartographie(admin.ModelAdmin):
    list_display = ('Entreprise', 'Titre_minier', 'Typ_cartgrph', 'Typ_cartgrph_autre', 'Echelle',
                    'Grille_maille', 'Prctg_affleurmnt', 'Surface_km2')
    list_filter = ('Grille_maille',)

