from roster import Roster

from vehicles import ares
from vehicles import athena
from vehicles import auto_coach_pony_gen_2
from vehicles import avenger
from vehicles import bean_feast
from vehicles import blackthorn
from vehicles import blaze
from vehicles import blind_smuir
from vehicles import boar_cat
from vehicles import bone
from vehicles import braf
from vehicles import breeze
from vehicles import brenner_cab
from vehicles import brenner_middle
from vehicles import bright_country
from vehicles import buffalo
from vehicles import carrack
#from vehicles import challenger # for NA roster
from vehicles import cheddar_valley
from vehicles import cheese_bug
from vehicles import chinook
from vehicles import deasil
from vehicles import diablo
from vehicles import dover
from vehicles import dragon
from vehicles import driving_cab_pony_gen_5
from vehicles import driving_cab_pony_gen_6
from vehicles import endeavour
from vehicles import esk
from vehicles import evolution
from vehicles import firebird
from vehicles import fleet
from vehicles import flanders_storm
from vehicles import flindermouse
from vehicles import fury
from vehicles import geronimo
from vehicles import girt_licker
from vehicles import goliath
from vehicles import gowsty
from vehicles import grid
from vehicles import griffon
from vehicles import gronk
from vehicles import growler
from vehicles import grub
from vehicles import haar
from vehicles import happy_train
from vehicles import helm_wind_cab
from vehicles import helm_wind_middle
from vehicles import hercules
from vehicles import high_flyer
from vehicles import hurly_burly
from vehicles import intrepid
from vehicles import jupiter
from vehicles import kelpie
from vehicles import lamia
from vehicles import lark
from vehicles import lemon
from vehicles import little_bear
from vehicles import longwater
from vehicles import mail_rail
from vehicles import magnum_70
from vehicles import merlion
from vehicles import merrylegs
from vehicles import moor_gallop
from vehicles import mumble
from vehicles import olympic
from vehicles import onslaught
from vehicles import peasweep
from vehicles import pegasus
from vehicles import phoenix
from vehicles import pikel
from vehicles import pinhorse
from vehicles import plastic_postbox
from vehicles import proper_job
from vehicles import pylon
from vehicles import relentless
from vehicles import reliance
from vehicles import resilient
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
from vehicles import snowplough_pony_gen_2
from vehicles import spinner
from vehicles import stoat
from vehicles import streamer
from vehicles import strongbow
from vehicles import sunshine_coast
from vehicles import super_shoebox
from vehicles import swift
from vehicles import tencendur
from vehicles import thunderer
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import toaster
from vehicles import triton
from vehicles import tyburn
from vehicles import ultra_shoebox
from vehicles import vanguard
from vehicles import vigilant
from vehicles import viking
from vehicles import vulcan
from vehicles import westbourne
from vehicles import workish
from vehicles import wyvern
from vehicles import zebedee
from vehicles import zeus
from vehicles import zorro


def main(disabled=False):
    # migration note; see also render_docs as it may already have methods for getting the tech tree in generation order
    print('roster engines list should be refactored to use order from role_group_mapping combined with engine generation')
    roster = Roster(id = 'pony',
                    numeric_id = 1,
                    # ELRL, ELNG is mapped to RAIL, NG etc
                    # default intro dates per generation, can be over-ridden if needed by setting intro_date kw on consist
                    intro_dates = {'RAIL': [1860, 1900, 1930, 1960, 1990, 2020],
                                   'METRO': [1900, 1950, 2000],
                                   'NG': [1860, 1905, 1950, 2000]
                                   },
                    # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
                    # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
                    # NG is Corsican-style 1000mm, native brit NG is not a thing for gameplay
                    speeds = {'RAIL': {'standard': [45, 45, 60, 75, 87, 87], # gen 5 and 6 held down by design, really fast freight is imbalanced
                                       'railcar': [45, 45, 60, 75, 87, 99], # match standard, except gen 6
                                       'express': [60, 75, 90, 105, 115, 125], # smaller steps in gen 5 and 6, balances against faster HSTs
                                       'hst': [0, 0, 0, 112, 125, 140], # only gen 4, 5 and 6 HST provided
                                       'very_high_speed': [0, 0, 0, 0, 140, 186]
                                       },
                              'METRO': {'standard': [45, 55, 65]
                                        # no express for metro in Pony
                                        },
                              'NG': {'standard': [45, 45, 55, 65], # NG standard/railcar/express all same in Pony, balanced against trams, RVs
                                     'railcar': [45, 45, 55, 65],
                                     'express': [45, 45, 55, 65]}
                                     },

                    # capacity factor per generation, will be multiplied by vehicle length
                    freight_car_capacity_per_unit_length =  {'RAIL': [4, 4, 5, 5.5, 6, 6.5],
                                                             'NG': [3, 3, 4, 4]
                                                             },
                    pax_car_capacity_per_unit_length =  {'RAIL': [3, 4, 5, 5, 6, 6],
                                                         'NG': [3, 4, 5, 6]
                                                         },
                    # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
                    train_car_weight_factors = [0.5, 0.5, 0.5, 0.48, 0.44, 0.40],

                    # specify lists of cc1 and not_cc2 colours, and an option to remap all the cc1 to a specific other cc (allowing multiple input colours to map to one result)
                    livery_presets = {'EWS': {'cc1': ['COLOUR_PINK'],
                                              'not_cc2': [],
                                              'remap_to_cc': None,
                                              'docs_image_input_cc': [('COLOUR_PINK', 'COLOUR_YELLOW')]
                                              },
                                      'FREIGHTLINER_GBRF': {'cc1': ['COLOUR_PALE_GREEN', 'COLOUR_GREEN', 'COLOUR_DARK_GREEN', 'COLOUR_MAUVE'], # includes GBRF
                                                       'not_cc2': [],
                                                       'remap_to_cc': None,
                                                       'docs_image_input_cc': [('COLOUR_PALE_GREEN', 'COLOUR_YELLOW'), ('COLOUR_DARK_GREEN', 'COLOUR_ORANGE'), ('COLOUR_GREEN', 'COLOUR_ORANGE'), ('COLOUR_MAUVE', 'COLOUR_CREAM')]
                                                       },
                                      # red stripe cc1 chosen to give nice wagon colour options
                                      'RAILFREIGHT_RED_STRIPE': {'cc1': ['COLOUR_GREY', 'COLOUR_BROWN', 'COLOUR_YELLOW', 'COLOUR_ORANGE'], # not white, too limiting for other liveries
                                                                 'not_cc2': ['COLOUR_GREY', 'COLOUR_BROWN', 'COLOUR_YELLOW', 'COLOUR_ORANGE', 'COLOUR_WHITE'], # do ban white though, looks bad as lower stripe
                                                                 'remap_to_cc': 'COLOUR_GREY',
                                                                 'docs_image_input_cc': [('COLOUR_GREY', 'COLOUR_RED'), ('COLOUR_BROWN', 'COLOUR_PINK')]
                                                                 },
                                       # triple grey cc1 chosen to give nice wagon colour options
                                       # notcc2 chosen for (a) ensuring contrast of sector symbol (b) also happens to enable dutch yellow/grey livery
                                       # note the remap to white, to provide lightest of the triple greys as cc1
                                      'RAILFREIGHT_TRIPLE_GREY': {'cc1': ['COLOUR_GREY', 'COLOUR_BROWN', 'COLOUR_YELLOW', 'COLOUR_ORANGE'], # not white, too limiting for other liveries
                                                                  'not_cc2': ['COLOUR_GREY', 'COLOUR_BROWN', 'COLOUR_YELLOW', 'COLOUR_ORANGE', 'COLOUR_WHITE'], # do ban white though, looks bad with sector logo
                                                                  'remap_to_cc': 'COLOUR_WHITE',
                                                                  'docs_image_input_cc': [('COLOUR_GREY', 'COLOUR_RED'), ('COLOUR_YELLOW', 'COLOUR_BLUE'), ('COLOUR_BROWN', 'COLOUR_DARK_BLUE')],
                                                                  },
                                      'YEOMAN': {'cc1': ['COLOUR_GREY', 'COLOUR_WHITE'],
                                                 'not_cc2': [],
                                                 'remap_to_cc': None,
                                                 'docs_image_input_cc': [('COLOUR_GREY', 'COLOUR_BLUE'), ('COLOUR_WHITE', 'COLOUR_DARK_BLUE')]
                                                 }
                                      },

                    engines = [# branch express
                               # challenger, # for NA roster
                               lark,
                               merrylegs,
                               proper_job,
                               stoat,
                               pinhorse,
                               shoebox,
                               super_shoebox,
                               ultra_shoebox,
                               # express
                               reliance,
                               kelpie,
                               griffon,
                               spinner,
                               carrack,
                               tencendur,
                               merlion,
                               shredder,
                               thunderer,
                               swift,
                               strongbow,
                               streamer,
                               wyvern,
                               intrepid,
                               vanguard,
                               resilient,
                               evolution, # out of normal order so that the names read 'Evolution', 'Revolution' (usually jokers come after the tech tree version not before)
                               revolution,
                               pegasus,
                               dragon,
                               vulcan,
                               onslaught,
                               relentless,
                               hurly_burly,
                               moor_gallop,
                               roarer,
                               fury,
                               zebedee,
                               screamer,
                               avenger,
                               sizzler,
                               # driving cab cars
                               driving_cab_pony_gen_5,
                               driving_cab_pony_gen_6,
                               # branch freight
                               buffalo,
                               saxon,
                               little_bear,
                               goliath,
                               # freight
                               hercules,
                               braf,
                               diablo,
                               haar,
                               viking,
                               growler,
                               slug,
                               phoenix,
                               vigilant,
                               blind_smuir,
                               girt_licker,
                               lemon,
                               esk,
                               chinook,
                               grid,
                               bone,
                               blackthorn,
                               endeavour,
                               cheddar_valley,
                               toaster,
                               flindermouse,
                               peasweep,
                               flanders_storm,
                               triton,
                               # joker engines / snowploughs
                               grub,
                               lamia,
                               gronk,
                               magnum_70,
                               snowplough_pony_gen_2,
                               # auto-coaches
                               # auto_coach_pony_gen_2,
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
                               # luxury electric railcars
                               high_flyer,
                               sunshine_coast,
                               olympic,
                               bright_country,
                               # brit high speed pax
                               firebird,
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
                               zorro
                               ])
    roster.register(disabled=disabled)
