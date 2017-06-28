from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fiches.rpg.avant_garde.forms import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@login_required
def creer_base(request):
    utilisateur = request.user
    if (utilisateur.has_perm('fiche.add_avant_garde')):
        if request.method == 'POST':
            form = Avant_GardeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = Avant_GardeForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/global_form.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire une fiche de l'avant-garde.")


@login_required
def creer_apothicaire(request, base_id):
    utilisateur = request.user
    if (utilisateur.has_perm('fiche.add_avant_garde')):
        if request.method == 'POST':
            data = request.POST.dict()
            data['nom'] = 'Avant garde'
            form = FicheForm(data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(form.errors)
        else:
            form = Avant_gardeForm()

        context = {'form': form}

        return render(request, 'global_form.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire une fiche de l'avant-garde.")


def persos_ag(request):
    fiches_list = Avant_garde.objects.order_by('nom', 'prenom')

    paginator = Paginator(fiches_list, 20)
    page = request.GET.get('page')
    try:
        fiches = paginator.page(page)
    # if page not an integer, display first page of results
    except PageNotAnInteger:
        fiches = paginator.page(1)
    # if page is out of range, display the last page of results
    except EmptyPage:
        fiches = paginator.page(paginator.num_pages)

    context = {'fiches': fiches}

    return render(request, 'rpg/avant_garde/personnages.html', context)
