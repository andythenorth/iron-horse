from roster import Roster

from vehicles import apt_thing
from vehicles import bean_feast
from vehicles import bertha
from vehicles import boar_cat
from vehicles import braf
from vehicles import chaplin
from vehicles import cheddar_valley
from vehicles import cheese_bug
from vehicles import chimera
from vehicles import chinook
from vehicles import deasil
from vehicles import dragon
from vehicles import express_tank
from vehicles import faun
from vehicles import fleet
from vehicles import flanders_storm
from vehicles import flindermouse
from vehicles import freight_tank
from vehicles import gowsty
from vehicles import growler
from vehicles import haar
from vehicles import happy_train
from vehicles import high_flyer
from vehicles import hurly_burly
from vehicles import lemon
from vehicles import little_bear
from vehicles import longwater
from vehicles import mail_rail
from vehicles import moor_gallop
from vehicles import mumble
from vehicles import northcock
from vehicles import peasweep
from vehicles import pendolino_thing
from vehicles import pikel
from vehicles import phoenix
from vehicles import plastic_postbox
from vehicles import ramsbottom
from vehicles import roarer
from vehicles import scooby
from vehicles import screamer
from vehicles import serpentine
from vehicles import shoebox
from vehicles import sizzler
from vehicles import slammer
from vehicles import slug
from vehicles import snapper
from vehicles import standard
from vehicles import suburban
from vehicles import super_shoebox
from vehicles import thunderbird
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import turtle
from vehicles import tyburn
from vehicles import ultra_shoebox
from vehicles import velaro_thing
from vehicles import westbourne

roster = Roster(id = 'pony',
                numeric_id = 1,
                # ELRL, ELNG is mapped to RAIL, NG etc
                # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
                intro_dates = {'RAIL': [1860, 1900, 1930, 1960, 1990, 2020],
                               'METRO': [1900, 1950, 2000],
                               'NG': [1860, 1905, 1950, 2000]},
                # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
                # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
                speeds = {'RAIL': {'standard': [45, 45, 60, 75, 87, 100], # gen 5 and 6 forced down by design, really fast freight is imbalanced
                                   'express': [60, 75, 90, 105, 120, 135], # 135 is for a reason, can't remember what :P
                                   'very_high_speed': [0, 0, 0, 140, 170, 200]},
                          'METRO': {'standard': [45, 55, 65]}, # no express for metro in Pony
                          'NG': {'standard': [35, 35, 45, 55], # NG standard/express all same in Pony
                                 'express': [35, 35, 45, 55]}},

                # capacity factor per generation, will be multiplied by vehicle length
                freight_car_capacity_per_unit_length =  {'RAIL': [4, 4, 5, 5.5, 6, 6],
                                                         'NG': [3, 3, 4, 4]},
                # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
                freight_car_weight_factors = [0.5, 0.5, 0.5, 0.48, 0.44, 0.44],

                engines = [chaplin,
                           ramsbottom,
                           standard,
                           suburban,
                           braf,
                           high_flyer,
                           bertha,
                           hurly_burly,
                           flindermouse,
                           express_tank,
                           freight_tank,
                           haar,
                           northcock,
                           lemon,
                           moor_gallop,
                           peasweep,
                           shoebox,
                           little_bear,
                           growler,
                           dragon,
                           chinook,
                           roarer,
                           super_shoebox,
                           faun,
                           slug,
                           thunderbird,
                           cheddar_valley,
                           screamer,
                           flanders_storm,
                           ultra_shoebox,
                           phoenix,
                           turtle,
                           chimera,
                           sizzler,
                           deasil,
                           slammer,
                           tin_rocket,
                           happy_train,
                           gowsty,
                           scooby,
                           plastic_postbox,
                           mail_rail,
                           apt_thing,
                           pendolino_thing,
                           velaro_thing,
                           # brit extras
                           serpentine,
                           westbourne,
                           fleet,
                           longwater,
                           tyburn,
                           tideway,
                           # brit ng
                           cheese_bug,
                           bean_feast,
                           pikel,
                           boar_cat,
                           mumble,
                           snapper])