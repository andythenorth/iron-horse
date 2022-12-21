import global_constants

from roster import Roster

from vehicles import ares
from vehicles import athena

# one auto coach only as autoreplace can't handle mixed cargo articulated consists
from vehicles import auto_coach_pony_gen_2
from vehicles import argus
from vehicles import arrow
from vehicles import avenger
from vehicles import bean_feast
from vehicles import blackthorn
from vehicles import blaze
from vehicles import blind_smuir
from vehicles import boar_cat
from vehicles import bone
from vehicles import booster
from vehicles import braf
from vehicles import breeze
from vehicles import brenner_cab
from vehicles import brenner_middle_mail
from vehicles import brenner_middle_passenger
from vehicles import bright_country
from vehicles import buffalo
from vehicles import captain_steel
from vehicles import cargo_sprinter
from vehicles import carrack

# from vehicles import challenger # for NA roster
from vehicles import cheddar_valley
from vehicles import cheese_bug
from vehicles import chinook
from vehicles import chuggypig
from vehicles import clipper
from vehicles import daring
from vehicles import deasil
from vehicles import decapod
from vehicles import defiant
from vehicles import diablo
from vehicles import doubletide
from vehicles import dover
from vehicles import dragon
from vehicles import dreadnought
from vehicles import driving_cab_mail_pony_gen_5
from vehicles import driving_cab_mail_pony_gen_6
from vehicles import driving_cab_passenger_pony_gen_4
from vehicles import driving_cab_passenger_pony_gen_5
from vehicles import driving_cab_passenger_pony_gen_6
from vehicles import esk
from vehicles import evolution
from vehicles import falcon
from vehicles import firebird
from vehicles import fleet
from vehicles import flanders_storm
from vehicles import flindermouse
from vehicles import foxhound
from vehicles import fury
from vehicles import gargouille
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
from vehicles import hawkinge
from vehicles import hector
from vehicles import helm_wind_cab
from vehicles import helm_wind_middle_mail
from vehicles import helm_wind_middle_passenger
from vehicles import hercules
from vehicles import high_flyer
from vehicles import highlander
from vehicles import hurly_burly
from vehicles import intrepid
from vehicles import jupiter
from vehicles import kelpie
from vehicles import lamia
from vehicles import lark
from vehicles import lemon
from vehicles import little_bear
from vehicles import longwater
from vehicles import lynx
from vehicles import mainstay
from vehicles import maximillian
from vehicles import magnum_70
from vehicles import merlion
from vehicles import merrylegs
from vehicles import moor_gallop
from vehicles import mumble
from vehicles import nimbus
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
from vehicles import quietus
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
from vehicles import skipper
from vehicles import slammer
from vehicles import slug
from vehicles import snapper
from vehicles import snowplough_pony_gen_2
from vehicles import spinner
from vehicles import stag
from vehicles import stentor
from vehicles import stoat
from vehicles import streamer
from vehicles import strongbow
from vehicles import sunshine_coast
from vehicles import super_shoebox
from vehicles import super_stentor
from vehicles import swift
from vehicles import tenacious
from vehicles import tencendur
from vehicles import thor
from vehicles import thunderer
from vehicles import tideway
from vehicles import tin_rocket
from vehicles import toaster
from vehicles import tornado
from vehicles import triton
from vehicles import tyburn
from vehicles import ultra_shoebox
from vehicles import vanguard
from vehicles import vigilant
from vehicles import viking
from vehicles import vulcan
from vehicles import westbourne
from vehicles import withershins
from vehicles import workish
from vehicles import wyvern
from vehicles import xerxes
from vehicles import yillen
from vehicles import zebedee
from vehicles import zest
from vehicles import zeus
from vehicles import zipper
from vehicles import zorro


def main():
    return Roster(
        id="pony",
        numeric_id=1,
        # note that the grf name is Iron Horse, as the pony roster was released for many years under that name, and changing it would needlessly confuse players
        # but to avoid overloading the word 'horse', which is widely used in src, we continue using 'pony' as the roster id
        grf_name="iron-horse",
        grfid=r"CA\12\1F",
        str_grf_name="Iron Horse",
        # ELRL, ELNG is mapped to RAIL, NG etc
        # default intro dates per generation, can be over-ridden if needed by setting intro_year kw on consist
        intro_years={
            "RAIL": [1860, 1900, 1930, 1960, 1990, 2020],
            "METRO": [1900, 1950, 2000],
            "NG": [1860, 1905, 1950, 2000],
        },
        # default speeds per generation, can be over-ridden if needed by setting speed kw arg on consist
        # speeds roughly same as RH trucks of same era + 5mph or so, and a bit higher at the top end (back and forth on this many times eh?),
        # NG is Corsican-style 1000mm, native brit NG is not a thing for gameplay
        speeds={
            "RAIL": {
                # gen 5 and 6 held down by design, really fast freight is imbalanced
                "standard": [
                    45,
                    45,
                    60,
                    75,
                    87,
                    87,
                ],
                # match standard, except gen 6
                "suburban": [45, 45, 60, 75, 87, 99],
                # smaller steps in gen 5 and 6, balances against faster HSTs
                "express": [
                    60,
                    75,
                    90,
                    105,
                    115,
                    125,
                ],
                "hst": [0, 0, 0, 112, 125, 125],
                "hst_on_lgv": [0, 0, 0, 112, 125, 140],
                "very_high_speed": [0, 0, 0, 0, 125, 125],
                "very_high_speed_on_lgv": [0, 0, 0, 0, 140, 186],
            },
            "METRO": {
                "standard": [45, 55, 65]
                # only standard for metro in Pony
            },
            "NG": {
                "standard": [
                    45,
                    45,
                    55,
                    65,
                ],
                # NG standard/suburban/express same in Pony, balanced against trams, RVs
                # suburban has to be provided as the mail railcar expects it, just copying it in is easiest solution
                "suburban": [45, 45, 55, 65],
                # suburban has to be provided as the coaches/mail vans etc expect it, just copying it in is easiest solution
                "express": [45, 45, 55, 65],
            },
        },
        # capacity factor per generation, will be multiplied by vehicle length
        freight_car_capacity_per_unit_length={
            "RAIL": [4, 4, 5, 5.5, 6, 6.5],
            "NG": [3, 3, 4, 4],
        },
        pax_car_capacity_per_unit_length={
            "RAIL": [3, 3.75, 4.5, 5.25, 6, 6],
            "NG": [3, 5, 5, 6],
        },
        pax_car_capacity_types={
            "default": {
                "multiplier": 1,
                "loading_speed_multiplier": 1,
            },
            "high_capacity": {
                "multiplier": 1.5,
                "loading_speed_multiplier": 1.75,
            },
            # very specifically tuned multiplier against a single pony vehicle
            "autocoach_combine": {
                "multiplier": 2.7,
                "loading_speed_multiplier": 1.75,
            },
            "restaurant": {
                "multiplier": 0.45,
                "loading_speed_multiplier": 1,
            },
        },
        # freight car weight factor varies slightly by gen, reflecting modern cars with lighter weight
        train_car_weight_factors=[0.5, 0.5, 0.5, 0.48, 0.44, 0.40],
        # specify lists of cc2 colours, and an option to remap all the cc1 to a specific other cc (allowing multiple input colours to map to one result)
        livery_presets={
            "FREIGHTLINER_GBRF": {
                # note the remap to yellow, allowing 1cc wagons to be whatever player chooses
                "remap_to_cc": "COLOUR_YELLOW",
                "docs_image_input_cc": [
                    ("COLOUR_YELLOW", "COLOUR_PALE_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_DARK_GREEN"),
                    ("COLOUR_ORANGE", "COLOUR_GREEN"),
                    ("COLOUR_CREAM", "COLOUR_MAUVE"),
                ],
            },
            "RAILFREIGHT_RED_STRIPE": {
                # don't match the stripe options to triple grey, it was tried and the blue just doesn't look good
                # green and purple were allowed as they're vivid and it's by player request
                "remap_to_cc": "COLOUR_GREY",
                "docs_image_input_cc": [
                    ("COLOUR_GREY", "COLOUR_RED"),
                    ("COLOUR_YELLOW", "COLOUR_PINK"),
                    ("COLOUR_GREY", "COLOUR_PURPLE"),
                    ("COLOUR_WHITE", "COLOUR_GREEN"),
                ],
            },
            "RAILFREIGHT_TRIPLE_GREY": {
                # note the remap to white, to provide lightest of the triple greys as cc1
                "remap_to_cc": "COLOUR_WHITE",
                "docs_image_input_cc": [
                    ("COLOUR_GREY", "COLOUR_RED"),
                    ("COLOUR_YELLOW", "COLOUR_BLUE"),
                    ("COLOUR_BROWN", "COLOUR_DARK_BLUE"),
                    ("COLOUR_GREY", "COLOUR_PURPLE"),
                    ("COLOUR_WHITE", "COLOUR_GREEN"),
                ],
            },
            "YEOMAN": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_BLUE", "COLOUR_GREY"),
                    ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
                    ("COLOUR_RED", "COLOUR_GREY"),
                    ("COLOUR_ORANGE", "COLOUR_WHITE"),
                ],
            },
            "CABBAGE_1": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_WHITE"),
                    ("COLOUR_GREY", "COLOUR_YELLOW"),
                ],
            },
            "CABBAGE_2": {
                "remap_to_cc": None,
                "docs_image_input_cc": [
                    ("COLOUR_RED", "COLOUR_LIGHT_BLUE"),
                ],
            },
        },
        # empty dicts currently, but could hold remaps, docs image colours etc if needed
        default_pax_liveries = [{}, {}],
        suburban_pax_liveries = [{"forced_livery_num":1}, {"forced_livery_num":0}],
        default_mail_liveries = [{"forced_livery_num":3}, {"forced_livery_num":0}, {"forced_livery_num":1}, {"forced_livery_num":2}],
        diesel_railcar_mail_liveries = [{"forced_livery_num":2}, {"forced_livery_num":0}, {"forced_livery_num":1}, {"forced_livery_num":3}],
        electric_railcar_mail_liveries = [{"forced_livery_num":3}, {"forced_livery_num":0}, {"forced_livery_num":1}, {"forced_livery_num":2}],
        # this list is manually maintained deliberately, even though it could be mostly automated using tech tree
        engines=[
            # challenger, # for NA roster
            # branch express
            lark,
            merrylegs,
            decapod,
            proper_job,
            stag,
            kelpie,
            foxhound,
            griffon,
            lynx,
            pinhorse,
            argus,
            booster,
            tornado,
            # express (electro-diesels with non-standard position in power/length tree)
            shoebox,
            super_shoebox,
            ultra_shoebox,
            # express
            reliance,
            spinner,
            carrack,
            tencendur,
            daring,
            shredder,
            thunderer,
            swift,
            strongbow,
            arrow,
            wyvern,
            tenacious,
            intrepid,
            vanguard,
            resilient,
            evolution,  # out of normal order so that the names read 'Evolution', 'Revolution' (usually jokers come after the tech tree version not before)
            revolution,
            pegasus,
            streamer,
            hawkinge,
            dragon,
            vulcan,
            falcon,
            onslaught,
            dreadnought,
            relentless,
            hurly_burly,
            moor_gallop,
            roarer,
            fury,
            hector,
            zebedee,
            screamer,
            nimbus,
            avenger,
            sizzler,
            # driving cab cars
            driving_cab_passenger_pony_gen_4,
            driving_cab_passenger_pony_gen_5,
            driving_cab_passenger_pony_gen_6,
            driving_cab_mail_pony_gen_5,
            driving_cab_mail_pony_gen_6,
            # branch freight
            buffalo,
            saxon,
            little_bear,
            captain_steel,
            goliath,
            stoat,
            zest,
            # freight
            hercules,
            braf,
            diablo,
            haar,
            growler,
            merlion,
            slug,
            viking,
            phoenix,
            xerxes,
            vigilant,
            blind_smuir,
            mainstay,
            yillen,
            doubletide,
            girt_licker,
            lemon,
            esk,
            chinook,
            withershins,
            grid,
            bone,
            blackthorn,
            defiant,
            quietus,
            cheddar_valley,
            stentor,
            highlander,
            super_stentor,
            toaster,
            flindermouse,
            peasweep,
            flanders_storm,
            triton,
            # joker engines / snowploughs
            grub,
            lamia,
            gronk,
            chuggypig,
            magnum_70,
            snowplough_pony_gen_2,
            # cargo sprinter
            cargo_sprinter,
            # auto-coach (only one as autoreplace can't handle mixed cargo articulated consists)
            auto_coach_pony_gen_2,
            # railbuses
            clipper,
            skipper,
            zipper,
            # diesel railcars
            deasil,
            slammer,
            tin_rocket,
            happy_train,
            gowsty,
            scooby,
            plastic_postbox,
            # electric railcars
            athena,
            geronimo,
            breeze,
            zeus,
            ares,
            dover,
            jupiter,
            pylon,
            # express electric railcars
            high_flyer,
            sunshine_coast,
            olympic,
            bright_country,
            # brit high speed pax
            firebird,
            blaze,
            scorcher,
            helm_wind_cab,
            helm_wind_middle_passenger,
            helm_wind_middle_mail,
            brenner_cab,
            brenner_middle_passenger,
            brenner_middle_mail,
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
            thor,
            pikel,
            boar_cat,
            gargouille,
            maximillian,
            # ng railcars
            mumble,
            snapper,
            workish,
            zorro,
        ],
    )
