from roster import Roster

from vehicles import aberdare
from vehicles import am9_thing
from vehicles import apt_thing
from vehicles import badger
from vehicles import bertha
from vehicles import chaplin
from vehicles import chinook
from vehicles import collett
from vehicles import donegal
from vehicles import electra
from vehicles import express_tank
from vehicles import fleet
from vehicles import growler
from vehicles import high_flyer
from vehicles import hudswell
from vehicles import lemon
from vehicles import longwater
from vehicles import northcock
from vehicles import pendolino_thing
from vehicles import plastic_postbox
from vehicles import ramsbottom
from vehicles import raven
from vehicles import roarer
from vehicles import scooby
from vehicles import serpentine
from vehicles import shoebox
from vehicles import slammer
from vehicles import slug
from vehicles import sparkycat
from vehicles import standard
from vehicles import stewart
from vehicles import suburban
from vehicles import super_shoebox
from vehicles import thunderbird
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import toaster
from vehicles import tug
from vehicles import turtle
from vehicles import tyburn
from vehicles import velaro_thing
from vehicles import walker
from vehicles import westbourne
from vehicles import wizzo

roster = Roster(id = 'pony',
                numeric_id = 1,
                # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
                intro_dates = [1860, 1900, 1930, 1960, 1990, 2020],
                # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
                # speeds are roughly matched to RH trucks of same era + 5mph or so (back and forth on this many times eh?)
                speeds = {'RAIL': {'freight': [45, 45, 60, 75, 90, 100],
                                   'fast_freight': [65, 80, 95, 110, 110, 110],
                                   'pax_mail': [65, 80, 95, 110, 125, 140]},
                          'NG': {'freight': [75, 110],
                                 'fast_freight': [55, 55],
                                 'pax_mail': [55, 55]}},
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
                           wizzo,
                           roarer,
                           super_shoebox,
                           slug,
                           tug,
                           thunderbird,
                           badger,
                           sparkycat,
                           toaster,
                           turtle,
                           slammer,
                           tin_rocket,
                           scooby,
                           plastic_postbox,
                           am9_thing,
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
