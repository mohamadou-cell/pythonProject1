from django.db import models
from alteration.models import *
from analyse.models import *
from localisation.models import *
from minier.models import *
from substance.models import *
from rapport.models import *
from ressource.models import *
from sondage.models import *


class Produit(models.Model):
    Produit_id = models.CharField(max_length=10, null=False, blank=False)
    Code_produit = models.CharField(max_length=10, null=False, blank=False)
    Produit_desc = models.CharField(max_length=10, null=False, blank=False)
    actif = models.CharField(max_length=10, null=False, blank=False)

class Exportation(models.Model):
    Exportation_id = models.CharField(max_length=10, null=False, blank=False)
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
    Produit = models.ForeignKey(max_length=10, null=False, blank=False)
    Pays = models.ForeignKey(max_length=10, null=False, blank=False)
    Qte_vendu_pays = models.CharField(max_length=10, null=False, blank=False)
    Val_produit = models.CharField(max_length=10, null=False, blank=False)

class Exportation_brut(models.Model):
    Exportation_id = models.CharField(max_length=10, null=False, blank=False)
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
    Produit= models.ForeignKey(max_length=10, null=False, blank=False)
    Pays = models.ForeignKey(max_length=10, null=False, blank=False)
    Qte_vendu_pays = models.CharField(max_length=10, null=False, blank=False)
    Val_produit = models.CharField(max_length=10, null=False, blank=False)

