from django.db import models
from alteration.models import *
from substance.models import *
from localisation.models import *
from minier.models import *
from produit.models import *
from rapport.models import *
from ressource.models import *
from sondage.models import *


class Typ_analyse(models.Model):
    Analyse_desc = models.CharField(max_length=10, null=False, blank=False)
    actif = models.CharField(max_length=10, null=False, blank=False)

class Exploitation_analyse(models.Model):
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
    Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
    Typ_analyse = models.ForeignKey(max_length=10, null=False, blank=False)
    Pays = models.ForeignKey(max_length=10, null=False, blank=False)
    Typ_analyse_autre = models.CharField(max_length=10, null=False, blank=False)
    Typ_analyse_autre = models.CharField(max_length=10, null=False, blank=False)
    Nom_laboratoire = models.CharField(max_length=10, null=False, blank=False)

class Exploration_analyse(models.Model):
    Formulaire = models.ForeignKey(max_length=10, null=False, blank=False)
    Titre_minier = models.ForeignKey(max_length=10, null=False, blank=False)
    Typ_analyse = models.ForeignKey(max_length=10, null=False, blank=False)
    Pays = models.ForeignKey(max_length=10, null=False, blank=False)
    Typ_analyse_autre = models.CharField(max_length=10, null=False, blank=False)
    Typ_analyse_autre = models.CharField(max_length=10, null=False, blank=False)
    Nom_laboratoire = models.CharField(max_length=10, null=False, blank=False)


