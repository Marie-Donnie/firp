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
        pv_max = pv_max + 1
        force = min(force + 1, 10)
        endu = min(endu + 1, 10)
        agi = max(agi - 2, 0)
    elif perso.race == 'e':
        agi = min(agi + 1, 10)
        cap_tir = min(cap_tir + 1, 10)
        perce = min(perce + 1, 10)
        pv_max = max(pv_max - 1, 0)
        endu = max(endu - 1, 0)
    if 10 in perso.avants.all():
        pv_max = pv_max + 1
    if 19 in perso.avants.all():
        intell = min(intell + 3, 10)
    if 21 in perso.desavants.all():
        pv_max = max(pv_max - 1, 0)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FANTASSIN %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_fantassin(perso_id):
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
        pv_max = pv_max + 2
    if fantassin.feroce_impla == 2:
        force = min(force + 1, 10)
        cap_combat = min(cap_combat + 1, 10)
    elif fantassin.feroce_impla == 3:
        endu = min(endu + 1, 10)
        pv_max = pv_max + 2
    if perso.niveau >= 3:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 4:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        force_men = min(force_men + 1, 10)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% APOTHCAIRE %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_apothicaire(perso_id):
    apo = Apothicaire.objects.get(pk=perso_id)
    perso = apo.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    chirurgie = apo.chirurgie
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
        chirurgie = min(apo.chirurgie + 30, 100)
    elif apo.scalpel_fioles == 3:
        cap_tir = min(cap_tir + 1, 10)
    if apo.guerisseur_enfum == 2:
        intell = min(intell + 1, 10)
        force_men = min(force_men+ 1, 10)
    if apo.guerisseur_enfum == 3:
        cap_tir = min(cap_tir + 1, 10)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir, chirurgie


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% ARBALETRIER %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_arbaletrier(perso_id):
    arba = Arbaletrier.objects.get(pk=perso_id)
    perso = arba.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    if perso.niveau >= 2:
        cap_tir = min(cap_tir + 1, 10)
    if perso.niveau >= 3:
        force_men = min(force_men + 1, 10)
        cap_tir = min(cap_tir + 1, 10)
    if perso.niveau >= 5:
        force_men = min(force_men + 1, 10)
        cap_tir = min(cap_tir + 1, 10)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% ECLAIREUR %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_eclaireur(perso_id):
    ecl = Eclaireur.objects.get(pk=perso_id)
    perso = ecl.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    if perso.niveau >= 2:
        if (ecl.aigle_vif == 2):
            perce = min(perce + 1, 10)
        elif (ecl.aigle_vif == 3):
            agi = min(agi + 1, 10)
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 3:
        if (ecl.vigilant_rx == 2):
            perce = min(perce + 1, 10)
        elif (ecl.vigilant_rx == 3):
            agi = min(agi + 1, 10)
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 4:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        if (ecl.silen_rodeur == 2):
            cap_combat = min(cap_combat + 1, 10)
            cap_tir = min(cap_tir + 1, 10)
            agi = min(agi + 1, 10)
        elif (ecl.silen_rodeur == 3):
            agi = min(agi + 1, 10)
            perce = min(perce + 2, 10)
        force_men = min(force_men + 1, 10)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% SORCIER %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_sorcier(perso_id):
    sorcier = Sorcier.objects.get(pk=perso_id)
    perso = sorcier.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    mana = 0
    if perso.niveau >= 2:
        intell = min(intell + 1, 10)
    if perso.niveau >= 3:
        intell = min(intell + 1, 10)
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 4:
        intell = min(intell + 1, 10)
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        intell = min(intell + 1, 10)
        force_men = min(force_men + 1, 10)
        mana += 100

    mana += intell * 10

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir, mana


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RABATTEUR %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

def calcul_rabatteur(perso_id):
    raba = Rabatteur.objects.get(pk=perso_id)
    perso = raba.perso
    force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir = calcul_base(perso.id)
    if perso.niveau >= 2:
        if (raba.gachette_vif == 2):
            cap_tir = min(cap_tir + 1, 10)
        elif (raba.gachette_vif == 3):
            agi = min(agi + 1, 10)
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 3:
        if (raba.gachette_rx == 2):
            cap_tir = min(cap_tir + 1, 10)
        elif (raba.gachette_rx == 3):
            agi = min(agi + 1, 10)
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 4:
        force_men = min(force_men + 1, 10)
    if perso.niveau >= 5:
        if (raba.fusillade_solitaire == 2):
            cap_tir = min(cap_tir + 2, 10)
            perce = min(perce + 1, 10)
        elif (raba.fusillade_solitaire == 3):
            agi = min(agi + 2, 10)
            endu = min(endu +1, 10)
        force_men = min(force_men + 1, 10)

    return force, endu, perce, agi, intell, charisme, force_men, pv_max, cap_combat, cap_tir
