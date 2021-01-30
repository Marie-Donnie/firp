from django.db import models
from datetime import datetime


import yaml
import math


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class IntegerRangeField(models.SmallIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.SmallIntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


class Shops:
    sv = {'shoemakers': 150,
          'butchers': 1200,
          'furriers': 250,
          'fishmongers': 1200,
          'maidservants': 250,
          'beer_sellers': 1400,
          'tailors': 250,
          'buckle_makers': 1400,
          'barbers': 350,
          'plasterers': 1400,
          'jewelers': 400,
          'spice_merchants': 1400,
          'taverns_restaurants': 400,
          'blacksmiths': 1500,
          'old_clothes': 400,
          'painters': 1500,
          'pastrycooks': 500,
          'licensed_doctors': 1700,
          'masons': 500,
          'roofers': 1800,
          'carpenters': 550,
          'locksmiths': 1900,
          'weavers': 600,
          'bathers': 1900,
          'chandlers': 700,
          'ropemakers': 1900,
          'mercers': 700,
          'inns': 2000,
          'coopers': 700,
          'tanners': 2000,
          'bakers': 800,
          'copyists': 2000,
          'watercarriers': 850,
          'sculptors': 2000,
          'scabbardmakers': 850,
          'rugmakers': 2000,
          'wine_sellers': 900,
          'harness_makers': 2000,
          'hatmakers': 950,
          'bleachers': 2100,
          'saddlers': 1000,
          'hay_merchants': 2300,
          'chicken_butchers': 1000,
          'cutlers': 2300,
          'pursemakers': 1100,
          'glovemakers': 2400,
          'woodsellers': 2400,
          'woodcarvers': 2400,
          'magic_shops': 2800,
          'booksellers': 6300,
          'bookbinders': 3000,
          'illuminators': 3900,
          'doctors': 350}

    def count_specific_shops(self, shop, citizens):

        return citizens / self.sv[shop]

    def count_shops(self, citizens):
        result = dict()
        for (key, value) in self.sv.items():
            div = citizens / value
            print(div)
            result[key] = truncate(div, 2)
        return result


def read_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


# TEST FUNCTIONS
# import functions
# yaml = functions.read_yaml("yaml/weather.yml")
# functions.get_season(yaml, "ete")
# functions.get_temperatures(yaml, "ete")
# functions.get_temperature(yaml, "ete", "minimum")

def get_season(yaml, saison):
    return yaml[saison]


def get_temperatures(yaml, saison):
    return get_season(yaml, saison)['temperature']


def get_temperature(yaml, saison, param):
    return get_temperatures(yaml, saison)[param]


def get_ciel(yaml, saison):
    return get_season(yaml, saison)['ciel']


def get_vent(yaml, saison):
    return get_season(yaml, saison)['vent']


def get_humidite(yaml, saison):
    return get_season(yaml, saison)['humidite']
