from django.shortcuts import render
from .models import *

def list_typ_sondage(request):
    conv_typ_sondage = Typ_sondage.objects.all()
    nbr_typ_sondage = conv_typ_sondage.count()

    contexte = {'conv_typ_sondage': conv_typ_sondage, 'nbr_typ_sondage': nbr_typ_sondage}

    return render(request, 'list_typ_sondage.html', contexte)

def list_exploitation_sondage(request):
    conv_exploitation_sondage = Exploitation_sondage.objects.all()
    nbr_exploitation_sondage = conv_exploitation_sondage.count()

    contexte = {'conv_exploitation_sondage': conv_exploitation_sondage, 'nbr_exploitation_sondage': nbr_exploitation_sondage}

    return render(request, 'list_exploitation_sondage.html', contexte)

def list_exploration_sondage(request):
    conv_exploration_sondage = Exploration_sondage.objects.all()
    nbr_exploration_sondage = conv_exploration_sondage.count()

    contexte = {'conv_exploration_sondage': conv_exploration_sondage, 'nbr_exploration_sondage': nbr_exploration_sondage}

    return render(request, 'list_exploration_sondage.html', contexte)
