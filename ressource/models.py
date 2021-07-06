from django.db import models
from alteration.models import *
from analyse.models import *
from localisation.models import *
from minier.models import *
from produit.models import *
from rapport.models import *
from substance.models import *
from sondage.models import *


class Typ_resrc_reserv(models.Model):
  Resrc_reserv_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Unite_mesr_minrlstn(models.Model):
  Unite_mesr_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Unite_mesr_substnc(models.Model):
  Unite_mesr_desc = models.CharField(max_length=10, null=False, blank=False)
  actif = models.CharField(max_length=10, null=False, blank=False)

class Exploitatn_resrc_reserv(models.Model):
  Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Produit = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_resrc_reserv = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_resrc_reserv_autre = models.CharField(max_length=10, null=False, blank=False)
  Tonnage = models.CharField(max_length=10, null=False, blank=False)
  Unite_mesr = models.ForeignKey(max_length=10, null=False, blank=False)
  Unite_mesr_autre = models.CharField(max_length=10, null=False, blank=False)
  Teneur = models.CharField(max_length=10, null=False, blank=False)
  Teneur_coupure = models.CharField(max_length=10, null=False, blank=False)
  Autre_substances = models.CharField(max_length=10, null=False, blank=False)

class Exploratn_resrc_reserv(models.Model):
  Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
  Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
  Produit = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_resrc_reserv = models.ForeignKey(max_length=10, null=False, blank=False)
  Typ_resrc_reserv_autre = models.CharField(max_length=10, null=False, blank=False)
  Tonnage = models.CharField(max_length=10, null=False, blank=False)
  Unite_mesr = models.ForeignKey(max_length=10, null=False, blank=False)
  Unite_mesr_autre = models.CharField(max_length=10, null=False, blank=False)
  Teneur = models.CharField(max_length=10, null=False, blank=False)
  Teneur_coupure = models.CharField(max_length=10, null=False, blank=False)
  Autre_substances = models.CharField(max_length=10, null=False, blank=False)






