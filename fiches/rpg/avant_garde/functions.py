from fiches.rpg.avant_garde.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% GENERAL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
def calcul_base(perso_id):
    perso = Avant_garde.objects.get(pk=perso_id)
    force = perso.force
    endu = perso.endu
    perce = perso.perce
    agi = perso.agi
    intell = perso.intell
    charisme = perso.charisme
    force_men = perso.force_men
    pv_max = perso.pv_max
    cap_combat = perso.cap_combat
    cap_tir = perso.cap_tir
    if perso.race == 'n':
        pv_max = min(pv_max + 1, 10)
        force = min(force + 1, 10)
        endu = min(endu + 1, 10)
        agi = max(agi - 2, 0)
    elif perso.race == 'e':
        agi = min(agi + 1, 10)
        cap_tir = min(cap_tir + 1, 10)
        perce = min(perce + 1, 10)
        pv_max = max(pv_max - 1, 0)
        endu = max(endu - 1, 0)
    if 10 in perso.avants:
        pv_max = min(pv_max + 1, 10)
    if 19 in perso.avants:
        intell = min(intell + 3, 10)
    if 21 in perso.desavants:
        pv_max = max(pv_max - 1, 0)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FANTASSIN %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_fant(perso_id):
    fantassin = Fantassin.objects.get(pk=perso_id)
    perso = fantassin.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    if fantassin.athle_resi == 2:
        force = min(force + 1, 10)
    elif fantassin.athle_resi == 3:
        endu = min(endu + 1, 10)
    if fantassin.epe_craned == 2:
        cap_combat = min(cap_combat + 1, 10)
    elif fantassin.epe_craned == 3:
        pv_max = min(pv_max + 2, 10)
    if fantassin.feroce_impla == 2:
        force = min(force + 1, 10)
        cap_combat = min(cap_combat + 1, 10)
    elif fantassin.feroce_impla == 3:
        endu = min(endu + 1, 10)
        pv_max = min(pv_max + 2, 10)
    if perso.niveau >= 3:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 4:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        force_men = min(force_men + 1, 10)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% APOTHCAIRE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_apo(perso_id):
    apo = Apothicaire.objects.get(pk=perso_id)
    perso = apo.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    if perso.niveau >= 1:
        intell = min(intell + 1, 10)
    if perso.niveau >= 2:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 3:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 4:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        force_men = min(force_men + 1, 10)
    if apo.guerisseur:
        intell = min(intell + 1, 10)
    if apo.scalpel_fioles == 2:
        intell = min(intell + 1, 10)
        apo.chirurgie = min(apo.chirurgie + 30, 100)
    elif apo.scalpel_fioles == 3:
        cap_tir = min(cap_tir + 1, 10)
    if apo.guerisseur_enfum == 2:
        intell = min(intell + 1, 10)
        force_men = min(force_men+ 1, 10)
    if apo.guerisseur_enfum == 3:
        cap_tir = min(cap_tir + 1, 10)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% APOTHCAIRE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_arba(perso_id):
    arba = Arbaletrier.objects.get(pk=perso_id)
    perso = arba.perso
    if perso.niveau >= 3:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        force_men = min(force_men + 1, 10)
