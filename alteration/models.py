from django.db import models
from substance.models import *
from analyse.models import *
from localisation.models import *
from minier.models import *
from produit.models import *
from rapport.models import *
from ressource.models import *
from sondage.models import *


class Typ_alteration(models.Model):
  Typ_alteration_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Alteration(models.Model):
  Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_alteration = models.ForeignKey(max_length=10, null=False, blank=False)
  Mineral = models.ForeignKey(max_length=10, null=False, blank=False)
  Alteration_yn = models.CharField(max_length=10, null=False, blank=False)
  Mineral_desc = models.CharField(max_length=10, null=False, blank=False)

class Alteration_mineral_rel(models.Model):
    Typ_alteration = models.ForeignKey(max_length=10, null=False, blank=False)
    Mineral = models.ForeignKey(max_length=10, null=False, blank=False)

class Mineral(models.Model):
    Mineral_desc = models.CharField(max_length=10, null=False, blank=False)
    actif = models.CharField(max_length=10, null=False, blank=False)


