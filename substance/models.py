from django.db import models
from alteration.models import *
from analyse.models import *
from localisation.models import *
from minier.models import *
from produit.models import *
from rapport.models import *
from ressource.models import *
from sondage.models import *



class Substance(models.Model):
    Substance_desc = models.CharField(max_length=10, null=False, blank=False)
    actif = models.CharField(max_length=10, null=False, blank=False)

class Extraction(models.Model):
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
    Substance = models.ForeignKey(max_length=10, null=False, blank=False)
    Qte_brut = models.CharField(max_length=10, null=False, blank=False)
    Cout_production = models.CharField(max_length=10, null=False, blank=False)
    Qte_transform = models.CharField(max_length=10, null=False, blank=False)
    Autres_min = models.CharField(max_length=10, null=False, blank=False)

class Extraction_brut(models.Model):
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
    Substance = models.ForeignKey(max_length=10, null=False, blank=False)
    Qte_brut = models.CharField(max_length=10, null=False, blank=False)
    Cout_production = models.CharField(max_length=10, null=False, blank=False)
    Qte_transform = models.CharField(max_length=10, null=False, blank=False)

class Titre_substance_rel(models.Model):
    Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
    Substance = models.ForeignKey(max_length=10, null=False, blank=False)
    Commune = models.ForeignKey(max_length=10, null=False, blank=False)
    Autres_subst = models.CharField(max_length=10, null=False, blank=False)

class Benefic_typ(models.Model):
    Benefic_typ_desc = models.CharField(max_length=10, null=False, blank=False)

