from django.db import models
from alteration.models import *
from analyse.models import *
from localisation.models import *
from minier.models import *
from produit.models import *
from rapport.models import *
from ressource.models import *
from substance.models import *


class Typ_sondage(models.Model):
    Sondage_desc = models.CharField(max_length=10, null=False, blank=False)
    actif = models.CharField(max_length=10, null=False, blank=False)

class Exploitation_sondage(models.Model):
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False, on_delete=models.CASCADE)
    Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False, on_delete=models.CASCADE)
    Typ_sondage = models.ForeignKey(max_length=10, null=False, blank=False, on_delete=models.CASCADE)
    Inters_u_mesr_id = models.CharField(max_length=10, null=False, blank=False)
    Typ_sondage_autre = models.CharField(max_length=10, null=False, blank=False)
    Grille_maille_desc = models.CharField(max_length=10, null=False, blank=False)
    Metrage = models.CharField(max_length=10, null=False, blank=False)
    Intervalle = models.CharField(max_length=10, null=False, blank=False)
    Intersection = models.CharField(max_length=10, null=False, blank=False)
    Teneur = models.CharField(max_length=10, null=False, blank=False)

class Exploration_sondage(models.Model):
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False, on_delete=models.CASCADE)
    Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False, on_delete=models.CASCADE)
    Typ_sondage = models.ForeignKey(max_length=10, null=False, blank=False, on_delete=models.CASCADE)
    Inters_u_mesr_id = models.CharField(max_length=10, null=False, blank=False)
    Typ_sondage_autre = models.CharField(max_length=10, null=False, blank=False)
    Grille_maille_desc = models.CharField(max_length=10, null=False, blank=False)
    Metrage = models.CharField(max_length=10, null=False, blank=False)
    Intervalle = models.CharField(max_length=10, null=False, blank=False)
    Intersection = models.CharField(max_length=10, null=False, blank=False)
    Teneur = models.CharField(max_length=10, null=False, blank=False)

