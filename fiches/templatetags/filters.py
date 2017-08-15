from django import template
from datetime import datetime

register = template.Library()


@register.filter
def prix(value):
    p_or = value // 10000
    reste = value % 10000
    p_argent = reste // 100
    reste = reste % 100
    p_cuivre = reste
    return p_or, p_argent, p_cuivre


@register.filter
def p_or(value):
    p_or = value // 10000
    return p_or


@register.filter
def p_argent(value):
    reste = value % 10000
    p_argent = reste // 100
    return p_argent


@register.filter
def p_cuivre(value):
    reste = value % 10000
    reste = reste % 100
    p_cuivre = reste
    return p_cuivre


@register.filter
def kilos(value):
    return value // 1000


@register.filter
def grammes(value):
    return value % 1000


@register.filter
def pourcent(value, arg):
    return (value * 100) / arg


@register.filter
def age(value):
    year = datetime.now().year
    return year - 1980 - value

@register.filter
def mois(value):
    if value == 1:
        mois = "Janvier"
    elif value == 2:
        mois = "Février"
    elif value == 3:
        mois = "Mars"
    elif value == 4:
        mois = "Avril"
    elif value == 5:
        mois = "Mai"
    elif value == 6:
        mois = "Juin"
    elif value == 7:
        mois = "Juillet"
    elif value == 8:
        mois = "Août"
    elif value == 9:
        mois = "Septembre"
    elif value == 10:
        mois = "Octobre"
    elif value == 11:
        mois = "Novembre"
    elif value == 12:
        mois = "Décembre"
    else:
        mois = "No"
    return mois
