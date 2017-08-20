# coding=utf-8

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
        mois = u"Janvier"
    elif value == 2:
        mois = u"Février"
    elif value == 3:
        mois = u"Mars"
    elif value == 4:
        mois = u"Avril"
    elif value == 5:
        mois = u"Mai"
    elif value == 6:
        mois = u"Juin"
    elif value == 7:
        mois = u"Juillet"
    elif value == 8:
        mois = u"Août"
    elif value == 9:
        mois = u"Septembre"
    elif value == 10:
        mois = u"Octobre"
    elif value == 11:
        mois = u"Novembre"
    elif value == 12:
        mois = u"Décembre"
    else:
        mois = u"No"
    return mois
