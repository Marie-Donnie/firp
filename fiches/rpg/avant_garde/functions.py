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
