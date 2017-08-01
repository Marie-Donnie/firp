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
    pv = perso.pv
    cap_combat = perso.cap_combat
    cap_tir = perso.cap_tir
    if perso.race == 'n':
        pv = min(pv + 1, 10)
        force = min(force + 1, 10)
        endu = min(endu + 1, 10)
        agi = max(agi - 2, 0)
    elif perso.race == 'e':
        agi = min(agi + 1, 10)
        cap_tir = min(cap_tir + 1, 10)
        perce = min(perce + 1, 10)
        pv = max(pv - 1, 0)
        endu = max(endu - 1, 0)
