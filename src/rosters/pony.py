from roster import Roster

from vehicles import ares
from vehicles import athena
from vehicles import bean_feast
from vehicles import blackthorn
from vehicles import blaze
from vehicles import boar_cat
from vehicles import braf
from vehicles import breeze
from vehicles import brenner_cab
from vehicles import brenner_middle
from vehicles import carrack
from vehicles import cheddar_valley
from vehicles import cheese_bug
from vehicles import chimera
from vehicles import chinook
from vehicles import deasil
from vehicles import dover
from vehicles import dragon
from vehicles import driving_cab_pony_gen_5
from vehicles import driving_cab_pony_gen_6
from vehicles import fleet
from vehicles import flanders_storm
from vehicles import flindermouse
from vehicles import fury
from vehicles import geronimo
from vehicles import girt_licker
from vehicles import goliath
from vehicles import gosling_blast
from vehicles import gowsty
from vehicles import grid
from vehicles import griffon
from vehicles import gronk
from vehicles import growler
from vehicles import gwynt
from vehicles import haar
from vehicles import happy_train
from vehicles import helm_wind_cab
from vehicles import helm_wind_middle
from vehicles import hercules
from vehicles import hurly_burly
from vehicles import jupiter
from vehicles import kelpie
from vehicles import lark
from vehicles import lemon
from vehicles import little_bear
from vehicles import longwater
from vehicles import mail_rail
from vehicles import merrylegs
from vehicles import moor_gallop
from vehicles import mumble
from vehicles import peasweep
from vehicles import pegasus
from vehicles import phoenix
from vehicles import pikel
from vehicles import pinhorse
from vehicles import plastic_postbox
from vehicles import proper_job
from vehicles import pylon
from vehicles import revolution
from vehicles import roarer
from vehicles import saxon
from vehicles import scooby
from vehicles import scorcher
from vehicles import screamer
from vehicles import serpentine
from vehicles import shoebox
from vehicles import shredder
from vehicles import sizzler
from vehicles import slammer
from vehicles import slug
from vehicles import snapper
from vehicles import snowplough_pony_gen_4
from vehicles import spinner
from vehicles import stoat
from vehicles import super_shoebox
from vehicles import tencendur
from vehicles import thunderbird
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import tyburn
from vehicles import ultra_shoebox
from vehicles import upcountry
from vehicles import westbourne
from vehicles import workish
from vehicles import wyvern
from vehicles import zeus
from vehicles import zorro

# migration note; see also render_docs as it may already have methods for getting the tech tree in generation order
print('roster engines list should be refactored to use order from role_group_mapping combined with engine generation')

roster = Roster(id = 'pony',
                numeric_id = 1,
                # ELRL, ELNG is mapped to RAIL, NG etc
                # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
                intro_dates = {'RAIL': [1860, 1900, 1930, 1960, 1990, 2020],
                               'METRO': [1900, 1950, 2000],
                               'NG': [1860, 1905, 1950, 2000]},
                # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
                # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
                # NG is Corsican-style 1000mm, native brit NG is not a thing for gameplay
                speeds = {'RAIL': {'standard': [45, 45, 60, 75, 87, 96], # gen 5 and 6 forced down by design, really fast freight is imbalanced
                                   'express': [60, 75, 90, 105, 115, 125], # smaller steps in gen 5 and 6, balances against faster HSTs
                                   'hst': [0, 0, 0, 0, 125, 140], # only gen 5 and 6 HST provided
                                   'very_high_speed': [0, 0, 0, 0, 140, 186]},
                          'METRO': {'standard': [45, 55, 65]}, # no express for metro in Pony
                          'NG': {'standard': [45, 45, 55, 65], # NG standard/express all same in Pony, balanced against trams, RVs
                                 'express': [45, 45, 55, 65]}},

                # capacity factor per generation, will be multiplied by vehicle length
                freight_car_capacity_per_unit_length =  {'RAIL': [4, 4, 5, 5.5, 6, 6],
                                                         'NG': [3, 3, 4, 4]},
                pax_car_capacity_per_unit_length =  {'RAIL': [3, 4, 5, 5, 6, 6],
                                                     'NG': [3, 4, 5, 6]},
                # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
                train_car_weight_factors = [0.5, 0.5, 0.5, 0.48, 0.44, 0.44],

                engines = [# branch express
                           lark,
                           merrylegs,
                           proper_job,
                           stoat,
                           pinhorse,
                           shoebox,
                           super_shoebox,
                           ultra_shoebox,
                           # express
                           spinner,
                           carrack,
                           tencendur,
                           kelpie,
                           griffon,
                           shredder,
                           wyvern,
                           thunderbird,
                           revolution,
                           upcountry,
                           pegasus,
                           dragon,
                           hurly_burly,
                           moor_gallop,
                           roarer,
                           fury,
                           screamer,
                           sizzler,
                           # driving cab cars
                           driving_cab_pony_gen_5,
                           driving_cab_pony_gen_6,
                           # branch freight
                           saxon,
                           little_bear,
                           hercules,
                           goliath,
                           # freight
                           gwynt,
                           braf,
                           haar,
                           growler,
                           slug,
                           phoenix,
                           girt_licker,
                           lemon,
                           chinook,
                           grid,
                           blackthorn,
                           cheddar_valley,
                           chimera,
                           flindermouse,
                           peasweep,
                           flanders_storm,
                           gosling_blast,
                           # joker engines / snowploughs
                           gronk,
                           snowplough_pony_gen_4,
                           # diesel railcars
                           deasil,
                           slammer,
                           tin_rocket,
                           happy_train,
                           gowsty,
                           scooby,
                           plastic_postbox,
                           mail_rail,
                           # electric railcars
                           athena,
                           geronimo,
                           breeze,
                           zeus,
                           ares,
                           dover,
                           jupiter,
                           pylon,
                           # brit high speed pax
                           blaze,
                           scorcher,
                           helm_wind_cab,
                           helm_wind_middle,
                           brenner_cab,
                           brenner_middle,
                           # metro
                           serpentine,
                           westbourne,
                           fleet,
                           longwater,
                           tyburn,
                           tideway,
                           # ng engines
                           cheese_bug,
                           bean_feast,
                           pikel,
                           boar_cat,
                           # ng railcars
                           mumble,
                           snapper,
                           workish,
                           zorro])
