from django.db import models
from alteration.models import *
from analyse.models import *
from localisation.models import *
from minier.models import *
from produit.models import *
from substance.models import *
from ressource.models import *
from sondage.models import *


class Typ_rapport(models.Model):
  Nm_typ_rapport = models.CharField(max_length=10, null=False, blank=False)

class Rapport(models.Model):
  Rapport_nom = models.CharField(max_length=10, null=False, blank= False)
  Rapport_annuel = models.CharField(max_length=10, null=False, blank=False)
  Rapport_trimestriel = models.CharField(max_length=10, null=False, blank=False)
  Rapport_entreprise = models.CharField(max_length=10, null=False, blank=False)
  Rapport_actif = models.CharField(max_length=10, null=False, blank=False)
  Rapport_excel = models.CharField(max_length=10, null=False, blank=False)

class Liste_rapport(models.Model):
  Typ_rapport = models.ForeignKey(max_length=10, null=False, blank=False)
  Rapport = models.ForeignKey(max_length=10, null=False, blank=False)
  Nm_rpt_executable = models.CharField(max_length=10, null=False, blank=False)
  Rapport_titre = models.CharField(max_length=10, null=False, blank=False)
  Rapport_desc = models.CharField(max_length=10, null=False, blank=False)

