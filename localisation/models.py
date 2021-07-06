from django.db import models
from alteration.models import *
from analyse.models import *
from substance.models import *
from minier.models import *
from produit.models import *
from rapport.models import *
from ressource.models import *
from sondage.models import *


class Pays(models.Model):
  Pays_cd = models.CharField(max_length=10, null=False, blank=False)
  nom_pays = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Region(models.Model):
  region_cd = models.CharField(max_length=10, null=False, blank=False)
  nom_region = models.CharField(max_length=10, null=False, blank=False)

class Departement(models.Model):
  Region = models.ForeignKey(Region, on_delete = models.CASCADE)
  nom_departement = models.CharField(max_length=10, null=False, blank=False)

class Commune(models.Model):
  Departement = models.ForeignKey(Departement, on_delete = models.CASCADE)
  nom_commune = models.CharField(max_length=10, null=False, blank=False)






