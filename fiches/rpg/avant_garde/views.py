from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fiches.rpg.avant_garde.forms import *
from fiches.rpg.avant_garde.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@login_required
def creer_base(request):
    utilisateur = request.user
    if (utilisateur.has_perm('fiche.add_avant_garde')):
        if request.method == 'POST':
            data = request.POST.copy()
            if not 'avants' in data:
                data['avants'] = Avantages.objects.get(pk=1)
            if not 'desavants' in data:
                data['desavants'] = Desavantages.objects.get(pk=1)
            data['createur'] = User.objects.get(username=utilisateur).id
            form = Avant_GardeForm(data, request.FILES)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_perso', perso_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = Avant_GardeForm()

        avantages = Avantages.objects.all()
        desavantages = Desavantages.objects.all()
        context = {'form': form, 'avantages': avantages,
                   'desavantages': desavantages}
        return render(request, 'rpg/avant_garde/global_form.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas faire une fiche de l'avant-garde.")


@login_required
def editer_base(request, base_id):
    base = Avant_garde.objects.get(pk=base_id)
    utilisateur = request.user
    if utilisateur == base.createur:
        if request.method == 'POST':
            data = request.POST.copy()
            if not 'avants' in data:
                data['avants'] = Avantages.objects.get(pk=1)
            if not 'desavants' in data:
                data['desavants'] = Desavantages.objects.get(pk=1)
            data['createur'] = User.objects.get(username=utilisateur).id
            form = Avant_GardeForm(data, request.FILES, instance=base)
            if form.is_valid():
                save_it = form.save()
                return redirect('detail_perso', perso_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = Avant_GardeForm(instance=base)

        avantages = Avantages.objects.all()
        desavantages = Desavantages.objects.all()
        context = {'form': form, 'avantages': avantages,
                   'desavantages': desavantages}
        print(base.avants)
        return render(request, 'rpg/avant_garde/global_form.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas editer cette fiche de l'avant-garde.")


@login_required
def creer_apothicaire(request, ag_id):
    utilisateur = request.user
    if (utilisateur.has_perm('fiche.add_avant_garde')):
        perso = get_object_or_404(Avant_garde, pk=ag_id)
        if (perso.classe == 4):
            if request.method == 'POST':
                data = request.POST.copy()
                data['perso'] = perso.id
                form = ApothicaireForm(data)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/')
                else:
                    print(form.errors)
            else:
                form = ApothicaireForm()

            context = {'form': form}

            return render(request, 'rpg/avant_garde/apothicaire.html', context)
        else:
            return HttpResponse("La classe apothicaire ne correspond pas a celle du personnage.")

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


def detail_perso(request, perso_id):
    fiche = get_object_or_404(Avant_garde, pk=perso_id)

    context = {'fiche': fiche}

    return render(request, 'rpg/avant_garde/personnage.html', context)
