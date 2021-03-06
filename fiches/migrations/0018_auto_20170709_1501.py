# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import fiches.functions


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0017_case_createur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arbaletrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('focalisation', fiches.functions.IntegerRangeField(default=0)),
                ('couvert', fiches.functions.IntegerRangeField(default=0)),
                ('escalade', fiches.functions.IntegerRangeField(default=0)),
                ('coup_crit', fiches.functions.IntegerRangeField(default=0)),
                ('visee_prec', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('vigilance', fiches.functions.IntegerRangeField(default=0)),
                ('maitr_arba', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('equitation', fiches.functions.IntegerRangeField(default=0)),
                ('dissimulation', fiches.functions.IntegerRangeField(default=0)),
                ('as_du_tir', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('perso', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arbaletrier', to='fiches.Avant_garde')),
            ],
        ),
        migrations.CreateModel(
            name='Eclaireur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dissimulation', fiches.functions.IntegerRangeField(default=0)),
                ('vigilance', fiches.functions.IntegerRangeField(default=0)),
                ('oeil_aigle', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('vif', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('escalade', fiches.functions.IntegerRangeField(default=0)),
                ('equitation', fiches.functions.IntegerRangeField(default=0)),
                ('pistage', fiches.functions.IntegerRangeField(default=0)),
                ('deguisement', fiches.functions.IntegerRangeField(default=0)),
                ('vigilant', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('rx_eclairs', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('natation', fiches.functions.IntegerRangeField(default=0)),
                ('contorsion', fiches.functions.IntegerRangeField(default=0)),
                ('trap', fiches.functions.IntegerRangeField(default=0)),
                ('depl_silenc', fiches.functions.IntegerRangeField(default=0)),
                ('assassin', fiches.functions.IntegerRangeField(default=0)),
                ('maitr_anim', fiches.functions.IntegerRangeField(default=0)),
                ('art_silenc', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('rodeur', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('perso', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eclaireur', to='fiches.Avant_garde')),
            ],
        ),
        migrations.CreateModel(
            name='Sorcier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boule_feu', fiches.functions.IntegerRangeField(default=0)),
                ('trait_feu', fiches.functions.IntegerRangeField(default=0)),
                ('contresort', fiches.functions.IntegerRangeField(default=0)),
                ('nova_feu', fiches.functions.IntegerRangeField(default=0)),
                ('souffle_dragon', fiches.functions.IntegerRangeField(default=0)),
                ('bouclier_mana', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('portail', fiches.functions.IntegerRangeField(default=0)),
                ('pilier_feu', fiches.functions.IntegerRangeField(default=0)),
                ('explo_pyro', fiches.functions.IntegerRangeField(default=0)),
                ('transfert', fiches.functions.IntegerRangeField(default=0)),
                ('bouclier_feu', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('desamorcer_pieges', fiches.functions.IntegerRangeField(default=0)),
                ('enchant', fiches.functions.IntegerRangeField(default=0)),
                ('pluie_feu', fiches.functions.IntegerRangeField(default=0)),
                ('bombe_vivante', fiches.functions.IntegerRangeField(default=0)),
                ('annul_male', fiches.functions.IntegerRangeField(default=0)),
                ('ana_magique', fiches.functions.IntegerRangeField(default=0)),
                ('grand_sorcier', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('perso', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sorcier', to='fiches.Avant_garde')),
            ],
        ),
        migrations.AddField(
            model_name='fantassin',
            name='escalade',
            field=fiches.functions.IntegerRangeField(default=0),
        ),
    ]
