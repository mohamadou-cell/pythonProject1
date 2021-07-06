from django.db import models
from alteration.models import *
from analyse.models import *
from localisation.models import *
from substance.models import *
from produit.models import *
from rapport.models import *
from ressource.models import *
from sondage.models import *



class Nature_titre_minier(models.Model):
  Nature_tminier_cd = models.CharField(max_length=10, null=False, blank=False)
  nom_nature = models.CharField(max_length=10, null=False, blank=False)

class Titre_minier(models.Model):
  Entreprise = models.ForeignKey(max_length=10, null=False, blank=False)
  Num_titre_minier = models.CharField(max_length=10, null=False, blank=False)
  Nom_perimetre = models.CharField(max_length=10, null=False, blank=False)

class Exploratn_details(models.Model):
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
  Exploratn_details_id = models.CharField(max_length=10, null=False, blank=False)
  Nbr_tranchee = models.CharField(max_length=10, null=False, blank=False)
  Nbr_prosp_avance = models.CharField(max_length=10, null=False, blank=False)
  Nbr_prosp_prelmnr = models.CharField(max_length=10, null=False, blank=False)
  Da_saprolit_oxyd = models.CharField(max_length=10, null=False, blank=False)
  Da_saprok = models.CharField(max_length=10, null=False, blank=False)
  Da_roche_saine = models.CharField(max_length=10, null=False, blank=False)
  Da_autre_ind = models.CharField(max_length=10, null=False, blank=False)
  Da_autre_desc = models.CharField(max_length=10, null=False, blank=False)
  Ah_silicificatn = models.CharField(max_length=10, null=False, blank=False)
  Ah_albitisatn = models.CharField(max_length=10, null=False, blank=False)
  Ah_sericitisatn = models.CharField(max_length=10, null=False, blank=False)
  Ah_silicecarbonage = models.CharField(max_length=10, null=False, blank=False)
  Ah_saprolit_oxyd = models.CharField(max_length=10, null=False, blank=False)
  Ah_autre_ind = models.CharField(max_length=10, null=False, blank=False)
  Ah_autre_desc = models.CharField(max_length=10, null=False, blank=False)
  As_sulfur = models.CharField(max_length=10, null=False, blank=False)
  As_pyrite = models.CharField(max_length=10, null=False, blank=False)
  As_calcopyrite = models.CharField(max_length=10, null=False, blank=False)
  As_arsenopyrite = models.CharField(max_length=10, null=False, blank=False)
  As_pyrothite = models.CharField(max_length=10, null=False, blank=False)
  As_autre_ind = models.CharField(max_length=10, null=False, blank=False)
  As_autre_desc = models.CharField(max_length=10, null=False, blank=False)

class Tranchee(models.Model):
  Entreprise = models.ForeignKey(max_length=10, null=False, blank=False)
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Tranchee_desc = models.CharField(max_length=10, null=False, blank=False)
  Longueur = models.CharField(max_length=10, null=False, blank=False)
  Profondeur = models.CharField(max_length=10, null=False, blank=False)
  Faibl_intervalle = models.CharField(max_length=10, null=False, blank=False)
  Faibl_intersectn = models.CharField(max_length=10, null=False, blank=False)
  Faibl_u_mesr_id = models.CharField(max_length=10, null=False, blank=False)
  Moyen_intervalle = models.CharField(max_length=10, null=False, blank=False)
  Moyen_intersection = models.CharField(max_length=10, null=False, blank=False)
  Moyen_u_mesr_id = models.CharField(max_length=10, null=False, blank=False)
  Elev_intervalle = models.CharField(max_length=10, null=False, blank=False)
  Elev_intersectn = models.CharField(max_length=10, null=False, blank=False)
  Elev_u_mesr_id = models.CharField(max_length=10, null=False, blank=False)

class Typ_geophysique(models.Model):
  Typ_geophysique_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Geophysique(models.Model):
  Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_geophysique = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_geochimie_autre = models.CharField(max_length=10, null=False, blank=False)
  Nbr_ligne = models.CharField(max_length=10, null=False, blank=False)
  Superficie_km2 = models.CharField(max_length=10, null=False, blank=False)
  Altitude_vol = models.CharField(max_length=10, null=False, blank=False)
  Distance_lign_vol = models.CharField(max_length=10, null=False, blank=False)
  Magnetique = models.CharField(max_length=10, null=False, blank=False)
  Radiometrique = models.CharField(max_length=10, null=False, blank=False)
  electromagnetiq = models.CharField(max_length=10, null=False, blank=False)

class Typ_geochimie(models.Model):
  Typ_geochimie_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Typ_cartgrph(models.Model):
  Typ_cartgrph_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Cartographie(models.Model):
  Formulaire = models.ForeignKey(max_length=10, null = False, blank= False)
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_cartgrph = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_cartgrph_autre = models.CharField(max_length=10, null=False, blank=False)
  Echelle = models.CharField(max_length=10, null=False, blank=False)
  Grille_maille = models.CharField(max_length=10, null=False, blank=False)
  Prctg_affleurmnt = models.CharField(max_length=10, null=False, blank=False)
  Surface_km2 = models.CharField(max_length=10, null=False, blank=False)


