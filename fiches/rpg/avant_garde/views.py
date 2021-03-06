
import os

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
                if save_it.classe == 1:
                    fantassin = Fantassin.objects.select_related().filter(perso = save_it.id)
                    if fantassin:
                        return redirect('afficher_fantassin', classe_id=fantassin.first().id)
                elif save_it.classe == 2:
                    arbaletrier = Arbaletrier.objects.select_related().filter(perso = save_it.id)
                    if arbaletrier:
                        return redirect('afficher_arbaletrier', classe_id=arbaletrier.first().id)
                elif save_it.classe == 3:
                    eclaireur = Eclaireur.objects.select_related().filter(perso = save_it.id)
                    if eclaireur:
                        return redirect('afficher_eclaireur', classe_id=eclaireur.first().id)
                elif save_it.classe == 4:
                    apothicaire = Apothicaire.objects.select_related().filter(perso = save_it.id)
                    if apothicaire:
                        return redirect('afficher_apothicaire', classe_id=apothicaire.first().id)
                elif save_it.classe == 5:
                    sorcier = Sorcier.objects.select_related().filter(perso = save_it.id)
                    if sorcier:
                        return redirect('afficher_sorcier', classe_id=sorcier.first().id)
                elif save_it.classe == 6:
                    rabatteur = Rabatteur.objects.select_related().filter(perso = save_it.id)
                    if rabatteur:
                        return redirect('afficher_rabatteur', classe_id=rabatteur.first().id)
                return redirect('detail_perso', perso_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = Avant_GardeForm(instance=base)

        avantages = Avantages.objects.all()
        desavantages = Desavantages.objects.all()
        campagnes = Campagne.objects.all()
        context = {'form': form, 'avantages': avantages,
                   'desavantages': desavantages, 'campagnes': campagnes}
        return render(request, 'rpg/avant_garde/global_form.html', context)

    else:
        return HttpResponse("Vous ne pouvez pas editer cette fiche de l'avant-garde.")


#@permission_required('fiches.allie', raise_exception=True)
def persos_ag(request):
    fiches_list = Avant_garde.objects.order_by('-pj', 'nom', 'prenom')

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


#@permission_required('fiches.allie', raise_exception=True)
def detail_perso(request, perso_id):
    fiche = get_object_or_404(Avant_garde, pk=perso_id)
    utilisateur = request.user
    context = {'fiche': fiche, 'utilisateur': utilisateur}

    return render(request, 'rpg/avant_garde/personnage.html', context)


#@permission_required('fiches.allie', raise_exception=True)
def presentation(request):
    context = {}
    return render(request, 'rpg/avant_garde/presentation.html', context)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CLASSES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CREATION %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

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
                save_it = form.save()
                return redirect('afficher_fantassin', classe_id=save_it.id)
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
                save_it = form.save()
                return redirect('afficher_arbaletrier', classe_id=save_it.id)
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
                save_it = form.save()
                return redirect('afficher_eclaireur', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = EclaireurForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/eclaireur.html', context)
    else:
        return HttpResponse("La classe eclaireur ne correspond pas a celle du personnage.")


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
                save_it = form.save()
                return redirect('afficher_apothicaire', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ApothicaireForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/apothicaire.html', context)
    else:
        return HttpResponse("La classe apothicaire ne correspond pas a celle du personnage.")


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
                save_it = form.save()
                return redirect('afficher_sorcier', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = SorcierForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/sorcier.html', context)
    else:
        return HttpResponse("La classe sorcier ne correspond pas a celle du personnage.")


@permission_required('fiches.fdg', raise_exception=True)
def creer_rabatteur(request, perso_id):
    utilisateur = request.user
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if (utilisateur == perso.createur) and (perso.classe == 6):
        if request.method == 'POST':
            data = request.POST.copy()
            data['perso'] = perso.id
            form = RabatteurForm(data)
            if form.is_valid():
                save_it = form.save()
                return redirect('afficher_rabatteur', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = RabatteurForm()

        context = {'form': form}

        return render(request, 'rpg/avant_garde/rabatteur.html', context)
    else:
        return HttpResponse("La classe rabatteur ne correspond pas a celle du personnage.")


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
                save_it = form.save()
                return redirect('afficher_fantassin', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = FantassinForm(instance=fantassin)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/fantassin.html', context)

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
                save_it = form.save()
                return redirect('afficher_arbaletrier', classe_id=save_it.id)
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
                save_it = form.save()
                return redirect('afficher_eclaireur', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = EclaireurForm(instance=eclaireur)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/eclaireur.html', context)

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
                save_it = form.save()
                return redirect('afficher_apothicaire', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = ApothicaireForm(instance=apothicaire)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/apothicaire.html', context)

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
                save_it = form.save()
                return redirect('afficher_sorcier', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = SorcierForm(instance=sorcier)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/sorcier.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")

@permission_required('fiches.fdg', raise_exception=True)
def edit_rabatteur(request, perso_id):
    rabatteur = Rabatteur.objects.get(pk=perso_id)
    utilisateur = request.user
    if utilisateur == rabatteur.perso.createur or is_admin(utilisateur):
        if request.method == 'POST':
            data = request.POST.copy()
            data['createur'] = User.objects.get(username=utilisateur).id
            data['perso'] = rabatteur.perso.id
            form = RabatteurForm(data, request.FILES, instance=rabatteur)
            if form.is_valid():
                save_it = form.save()
                return redirect('afficher_rabatteur', classe_id=save_it.id)
            else:
                print(form.errors)
        else:
            form = RabatteurForm(instance=rabatteur)

        context = {'form': form}

        return render(request, 'rpg/avant_garde/rabatteur.html', context)

    else:

        return HttpResponse("Vous ne pouvez pas editer ce personnage.")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% AFFICHAGE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

#@permission_required('fiches.allie', raise_exception=True)
def afficher_fantassin(request, classe_id):
    classe = get_object_or_404(Fantassin, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_fantassin(classe.id)
    utilisateur = request.user
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir,
               'utilisateur': utilisateur }

    return render(request, 'rpg/avant_garde/display_fantassin.html', context)


#@permission_required('fiches.allie', raise_exception=True)
def afficher_apothicaire(request, classe_id):
    classe = get_object_or_404(Apothicaire, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir, chirurgie = calcul_apothicaire(classe_id)
    utilisateur = request.user
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir, 'chirurgie': chirurgie,
               'utilisateur': utilisateur }

    return render(request, 'rpg/avant_garde/display_apothicaire.html', context)


#@permission_required('fiches.allie', raise_exception=True)
def afficher_arbaletrier(request, classe_id):
    classe = get_object_or_404(Arbaletrier, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_arbaletrier(classe_id)
    utilisateur = request.user
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir,
               'utilisateur': utilisateur }

    return render(request, 'rpg/avant_garde/display_arbaletrier.html', context)


#@permission_required('fiches.allie', raise_exception=True)
def afficher_eclaireur(request, classe_id):
    classe = get_object_or_404(Eclaireur, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_eclaireur(classe_id)
    utilisateur = request.user
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir,
               'utilisateur': utilisateur }

    return render(request, 'rpg/avant_garde/display_eclaireur.html', context)


#@permission_required('fiches.allie', raise_exception=True)
def afficher_sorcier(request, classe_id):
    classe = get_object_or_404(Sorcier, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir, mana = calcul_sorcier(classe_id)
    utilisateur = request.user
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir, 'mana': mana,
               'utilisateur': utilisateur }

    return render(request, 'rpg/avant_garde/display_sorcier.html', context)


#@permission_required('fiches.allie', raise_exception=True)
def afficher_rabatteur(request, classe_id):
    classe = get_object_or_404(Rabatteur, pk=classe_id)
    perso = classe.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_rabatteur(classe.id)
    utilisateur = request.user
    context = {'fiche': perso, 'classe': classe, 'force': force,
               'endu': endu, 'perce': perce, 'agi': agi, 'intell': intell,
               'charisme': charisme, 'force_men': force_men, 'pv_max': pv_max,
               'cap_combat': cap_combat, 'cap_tir': cap_tir,
               'utilisateur': utilisateur }

    return render(request, 'rpg/avant_garde/display_rabatteur.html', context)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% SUPPRESSION %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

@permission_required('fiches.fdg', raise_exception=True)
def delete_fiche(request, classe, classe_id):
    classe = int(classe)
    if classe == 1:
        classe = get_object_or_404(Fantassin, pk=classe_id)
        perso = classe.perso
    elif classe == 2:
        classe = get_object_or_404(Arbaletrier, pk=classe_id)
        perso = classe.perso
    elif classe == 3:
        classe = get_object_or_404(Eclaireur, pk=classe_id)
        perso = classe.perso
    elif classe == 4:
        classe = get_object_or_404(Apothicaire, pk=classe_id)
        perso = classe.perso
    elif classe == 5:
        classe = get_object_or_404(Sorcier, pk=classe_id)
        perso = classe.perso
    elif classe == 6:
        classe = get_object_or_404(Rabatteur, pk=classe_id)
        perso = classe.perso
    else:
        print(classe, classe_id)
    if request.user == perso.createur:
        context = {'fiche': perso}
        if request.method == 'POST':
            path = "%s/" % (settings.MEDIA_ROOT)
            fichier = os.path.join(path, perso.image.name)
            if perso.image.name != "images/site/no-image.png":
                os.remove(fichier)
            classe.delete()
            perso.delete()
            return render(request, 'fiches/fiche_supprimee.html', context)
        else:
            return render(request, 'fiches/confirmation_suppression.html', context)
    else:
        return HttpResponse("Vous ne pouvez pas supprimer cette fiche.")


@permission_required('fiches.fdg', raise_exception=True)
def update_pv(request, perso_id, valeur):
    perso = get_object_or_404(Avant_garde, pk=perso_id)
    if request.user.id == perso.createur.id or request.user.has_perm('fiches.admin'):
        if request.method == 'POST':
            # update the values of the cell number
            if int(valeur) < 1 or int(valeur) > perso.pv_max:
                return HttpResponse(status=406)
            perso.pv = valeur
            perso.save(update_fields=['pv'])
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=403)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FONCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def is_admin(user):
    return user.groups.filter(name='Admin').exists()
