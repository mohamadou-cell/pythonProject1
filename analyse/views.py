from django.shortcuts import render
from .models import *

def list_typ_analyse(request):
    conv_typ_analyse = Typ_analyse.objects.all()
    nbr_typ_analyse = conv_typ_analyse.count()

    contexte = {'conv_typ_analyse': conv_typ_analyse, 'nbr_typ_analyse': nbr_typ_analyse}

    return render(request, 'list_typ_analyse.html', contexte)

def list_exploitation_analyse(request):
    conv_exploitation_analyse = Exploitation_analyse.objects.all()
    nbr_exploitation_analyse = conv_exploitation_analyse.count()

    contexte = {'conv_exploitation_analyse': conv_exploitation_analyse, 'nbr_exploitation_analyse': nbr_exploitation_analyse}

    return render(request, 'list_exploitation_analyse.html', contexte)

def list_exploration_analyse(request):
    conv_exploration_analyse = Exploration_analyse.objects.all()
    nbr_exploration_analyse = conv_exploration_analyse.count()

    contexte = {'conv_exploration_analyse': conv_exploration_analyse, 'nbr_exploration_analyse': nbr_exploration_analyse}

    return render(request, 'list_exploration_analyse.html', contexte)
