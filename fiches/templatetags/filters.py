from django import template

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
