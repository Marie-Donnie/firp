from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fiches.rpg.avant_garde.forms import *
from fiches.rpg.avant_garde.models import *
from fiches.rpg.avant_garde.functions import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% AVANT-GARDE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
@permission_required('fiches.fdg', raise_exception=True)
def creer_base(request):
    utilisateur = request.user
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
    campagnes = Campagne.objects.all()
    context = {'form': form, 'avantages': avantages,
               'desavantages': desavantages, 'campagnes': campagnes}
    return render(request, 'rpg/avant_garde/global_form.html', context)


@permission_required('fiches.fdg', raise_exception=True)
def editer_base(request, base_id):
    base = Avant_garde.objects.get(pk=base_id)
    utilisateur = request.user
    if utilisateur == base.createur or is_admin(utilisateur):
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


def presentation(request):
    context = {}
    return render(request, 'rpg/avant_garde/presentation.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CLASSES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CREATION %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def creer_apothicaire(request, perso_id):
    utilisateur = request.user
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if (utilisateur == perso.createur) and (perso.classe == 4):
        if request.method == 'POST':
            data = request.POST.copy()
            data['perso'] = perso.id
            form = ApothicaireForm(data)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=perso_id)
            else:
                print(form.errors)
        else:
            form = ApothicaireForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/apothicaire.html', context)
    else:
        return HttpResponse("La classe apothicaire ne correspond pas a celle du personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def creer_fantassin(request, perso_id):
    utilisateur = request.user
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if (utilisateur == perso.createur) and (perso.classe == 1):
        if request.method == 'POST':
            data = request.POST.copy()
            data['perso'] = perso.id
            form = FantassinForm(data)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=perso_id)
            else:
                print(form.errors)
        else:
            form = FantassinForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/fantassin.html', context)
    else:
        return HttpResponse("La classe fantassin ne correspond pas a celle du personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def creer_arbaletrier(request, perso_id):
    utilisateur = request.user
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if (utilisateur == perso.createur) and (perso.classe == 2):
        if request.method == 'POST':
            data = request.POST.copy()
            data['perso'] = perso.id
            form = ArbaletrierForm(data)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=perso_id)
            else:
                print(form.errors)
        else:
            form = ArbaletrierForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/arbaletrier.html', context)
    else:
        return HttpResponse("La classe arbaletrier ne correspond pas a celle du personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def creer_eclaireur(request, perso_id):
    utilisateur = request.user
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if (utilisateur == perso.createur) and (perso.classe == 3):
        if request.method == 'POST':
            data = request.POST.copy()
            data['perso'] = perso.id
            form = EclaireurForm(data)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=perso_id)
            else:
                print(form.errors)
        else:
            form = EclaireurForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/eclaireur.html', context)
    else:
        return HttpResponse("La classe eclaireur ne correspond pas a celle du personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def creer_sorcier(request, perso_id):
    utilisateur = request.user
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if (utilisateur == perso.createur) and (perso.classe == 5):
        if request.method == 'POST':
            data = request.POST.copy()
            data['perso'] = perso.id
            form = SorcierForm(data)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=perso_id)
            else:
                print(form.errors)
        else:
            form = SorcierForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/sorcier.html', context)
    else:
        return HttpResponse("La classe sorcier ne correspond pas a celle du personnage.")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% EDITION %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def edit_fantassin(request, perso_id):
    fantassin = Fantassin.objects.get(pk=perso_id)
    utilisateur = request.user
    if utilisateur == fantassin.perso.createur or is_admin(utilisateur):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            data['perso'] = fantassin.perso.id
            form = FantassinForm(data, request.FILES, instance=fantassin)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=fantassin.perso.id)
            else:
                print(form.errors)
        else:
            form = FantassinForm(instance=fantassin)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/fantassin.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def edit_apothicaire(request, perso_id):
    apothicaire = Apothicaire.objects.get(pk=perso_id)
    utilisateur = request.user
    if utilisateur == apothicaire.perso.createur or is_admin(utilisateur):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            data['perso'] = apothicaire.perso.id
            form = ApothicaireForm(data, request.FILES, instance=apothicaire)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=apothicaire.perso.id)
            else:
                print(form.errors)
        else:
            form = ApothicaireForm(instance=apothicaire)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/apothicaire.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def edit_arbaletrier(request, perso_id):
    arbaletrier = Arbaletrier.objects.get(pk=perso_id)
    utilisateur = request.user
    if utilisateur == arbaletrier.perso.createur or is_admin(utilisateur):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            data['perso'] = arbaletrier.perso.id
            form = ArbaletrierForm(data, request.FILES, instance=arbaletrier)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=arbaletrier.perso.id)
            else:
                print(form.errors)
        else:
            form = ArbaletrierForm(instance=arbaletrier)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/arbaletrier.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def edit_eclaireur(request, perso_id):
    eclaireur = Eclaireur.objects.get(pk=perso_id)
    utilisateur = request.user
    if utilisateur == eclaireur.perso.createur or is_admin(utilisateur):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            data['perso'] = eclaireur.perso.id
            form = EclaireurForm(data, request.FILES, instance=eclaireur)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=eclaireur.perso.id)
            else:
                print(form.errors)
        else:
            form = EclaireurForm(instance=eclaireur)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/eclaireur.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def edit_sorcier(request, perso_id):
    sorcier = Sorcier.objects.get(pk=perso_id)
    utilisateur = request.user
    if utilisateur == sorcier.perso.createur or is_admin(utilisateur):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            data['perso'] = sorcier.perso.id
            form = SorcierForm(data, request.FILES, instance=sorcier)
            if form.is_valid():
                form.save()
                return redirect('detail_perso', perso_id=sorcier.perso.id)
            else:
                print(form.errors)
        else:
            form = SorcierForm(instance=sorcier)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/sorcier.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% AFFICHAGE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def afficher_fantassin(request, classe_id):

    classe = get_object_or_404(Fantassin, pk=classe_id)

    perso = classe.perso

    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_fantassin(classe.id)
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir}

    return render(request, 'rpg/avant_garde/display_fantassin.html', context)

def afficher_apothicaire(request, classe_id):
    classe = get_object_or_404(Apothicaire, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_apothicaire(classe_id)
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir}

    return render(request, 'rpg/avant_garde/display_apothicaire.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FONCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def is_admin(user):
    return user.groups.filter(name='Admin').exists()
