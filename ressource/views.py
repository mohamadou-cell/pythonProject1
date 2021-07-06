from django.shortcuts import render
from .models import *

def list_typ_resrc_reserv(request):
    conv_typ_resrc_reserv = Typ_resrc_reserv.objects.all()
    nbr_typ_resrc_reserv = conv_typ_resrc_reserv.count()

    contexte = {'conv_typ_resrc_reserv': conv_typ_resrc_reserv, 'nbr_typ_resrc_reserv': nbr_typ_resrc_reserv}

    return render(request, 'list_typ_resrc_reserv.html', contexte)

def list_unite_mesr_minrlstn(request):
    conv_unite_mesr_minrlstn = Unite_mesr_minrlstn.objects.all()
    nbr_unite_mesr_minrlstn = conv_unite_mesr_minrlstn.count()

    contexte = {'conv_unite_mesr_minrlstn': conv_unite_mesr_minrlstn, 'nbr_unite_mesr_minrlstn': nbr_unite_mesr_minrlstn}

    return render(request, 'list_unite_mesr_minrlstn.html', contexte)

def list_unite_mesr_substnc(request):
    conv_unite_mesr_substnc = Unite_mesr_substnc.objects.all()
    nbr_unite_mesr_substnc = conv_unite_mesr_substnc.count()

    contexte = {'conv_unite_mesr_substnc': conv_unite_mesr_substnc, 'nbr_unite_mesr_substnc': nbr_unite_mesr_substnc}

    return render(request, 'list_unite_mesr_substnc.html', contexte)

def list_exploitatn_resrc_reserv(request):
    conv_exploitatn_resrc_reserv = Exploitatn_resrc_reserv.objects.all()
    nbr_exploitatn_resrc_reserv = conv_exploitatn_resrc_reserv.count()

    contexte = {'conv_exploitatn_resrc_reserv': conv_exploitatn_resrc_reserv, 'nbr_exploitatn_resrc_reserv': nbr_exploitatn_resrc_reserv}

    return render(request, 'list_exploitatn_resrc_reserv.html', contexte)

def list_exploratn_resrc_reserv(request):
    conv_exploratn_resrc_reserv = Exploratn_resrc_reserv.objects.all()
    nbr_exploratn_resrc_reserv = conv_exploratn_resrc_reserv.count()

    contexte = {'conv_exploratn_resrc_reserv': conv_exploratn_resrc_reserv, 'nbr_exploratn_resrc_reserv': nbr_exploratn_resrc_reserv}

    return render(request, 'list_exploratn_resrc_reserv.html', contexte)
