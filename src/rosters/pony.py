from roster import Roster

from vehicles import aberdare
from vehicles import apt_thing
from vehicles import bertha
from vehicles import chaplin
from vehicles import cheddar_valley
from vehicles import chimera
from vehicles import chinook
from vehicles import collett
from vehicles import donegal
from vehicles import dragon
from vehicles import electra
from vehicles import express_tank
from vehicles import fleet
from vehicles import growler
from vehicles import happy_train
from vehicles import high_flyer
from vehicles import hudswell
from vehicles import lemon
from vehicles import longwater
from vehicles import mail_rail
from vehicles import northcock
from vehicles import pendolino_thing
from vehicles import phoenix
from vehicles import plastic_postbox
from vehicles import ramsbottom
from vehicles import raven
from vehicles import roarer
from vehicles import scooby
from vehicles import screamer
from vehicles import serpentine
from vehicles import shoebox
from vehicles import sizzler
from vehicles import slammer
from vehicles import slug
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import super_shoebox
from vehicles import thunderbird
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import turtle
from vehicles import tyburn
from vehicles import ultra_shoebox
from vehicles import velaro_thing
from vehicles import walker
from vehicles import westbourne

roster = Roster(id = 'pony',
                numeric_id = 1,
                # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
                intro_dates = [1860, 1900, 1930, 1960, 1990, 2020],
                # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
                # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
                speeds = {'RAIL': {'standard': [45, 45, 60, 75, 90, 105],
                                   'express': [60, 75, 90, 105, 120, 135],
                                   'very_high_speed': [0, 0, 0, 140, 170, 200]},
                          'METRO': {'standard': [45, 45, 55, 65, 65]}, # no express for metro in Horse
                          'NG': {'standard': [50, 50, 50, 50, 50],
                                 'express': [55, 55]}},

                # capacity factor per generation, will be multiplied by vehicle length
                freight_car_capacity_per_unit_length =  {'RAIL': [5, 5, 5, 5, 5, 5],
                                                         'NG': [3, 3, 3, 3, 3, 3]},
                engines = [chaplin,
                           ramsbottom,
                           standard,
                           suburban,
                           aberdare,
                           bertha,
                           high_flyer,
                           raven,
                           express_tank,
                           collett,
                           lemon,
                           northcock,
                           electra,
                           shoebox,
                           growler,
                           chinook,
                           dragon,
                           roarer,
                           super_shoebox,
                           slug,
                           cheddar_valley,
                           thunderbird,
                           screamer,
                           ultra_shoebox,
                           phoenix,
                           chimera,
                           turtle,
                           sizzler,
                           slammer,
                           tin_rocket,
                           happy_train,
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
                           stewart,
                           hudswell,
                           donegal,
                           walker])