# badges can be predefined here, or created dynamically for specific vehicle models etc as needed
static_badges = {
    "power_source": {
        "name": "STR_POWER_SOURCE",
        "sublabels": {
            "dual_voltage": {},
            "electro_diesel": {},
        },
    },
    "ih_wagon_subtype": {
        # "name": "STR_BADGE_WAGON_LENGTH",
        "sublabels": {
            "a": {},  # {"name": "STR_BADGE_WAGON_LENGTH_SMALL"},
            "b": {},  # {"name": "STR_BADGE_WAGON_LENGTH_MEDIUM"},
            "c": {},  # {"name": "STR_BADGE_WAGON_LENGTH_LARGE"},
            "d": {},  # {"name": "STR_BADGE_WAGON_LENGTH_TWIN"},
            "u": {},  # {"name": "STR_EMPTY"},
            "z": {},  # CABBAGE 3/8 temp
        },
    },
    "ih_gen": {
        "name": "STR_BADGE_GEN",
        "sublabels": {
            "1": {"name": "STR_BADGE_GEN_1"},
            "2": {"name": "STR_BADGE_GEN_2"},
            "3": {"name": "STR_BADGE_GEN_3"},
            "4": {"name": "STR_BADGE_GEN_4"},
            "5": {"name": "STR_BADGE_GEN_5"},
            "6": {"name": "STR_BADGE_GEN_6"},
        },
    },
    "role": {
        "name": "STR_BADGE_ROLE",
        "sublabels": {
            "driving_cab": {"name": "STR_BADGE_ROLE_DRIVING_CAB"},
            "express": {"name": "STR_BADGE_ROLE_EXPRESS"},
            "freight": {"name": "STR_BADGE_ROLE_FREIGHT"},
            "gronk": {"name": "STR_BADGE_ROLE_GRONK"},
            "high_power_railcar": {"name": "STR_BADGE_ROLE_EXPRESS"},
            "lolz": {"name": "STR_BADGE_ROLE_LOLZ"},
            "metro": {"name": "STR_BADGE_ROLE_METRO"},
            "metro_freight": {"name": "STR_BADGE_ROLE_METRO_FREIGHT"},
            "suburban_or_universal_railcar": {"name": "STR_BADGE_ROLE_SUBURBAN"},
            "universal": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE"},
            "very_high_speed": {"name": "STR_BADGE_ROLE_INTERCITY_EXPRESS"},
        },
    },
    # note that we namespace `ih_behaviour` intentionally;
    # I considered just `behaviour`,
    # but I don't want to deal with de-conflicting other people's interpretations of that
    # badges are cheap
    "ih_behaviour": {
        "name": "STR_BADGE_BEHAVIOUR",
        "sublabels": {
            "caboose": {"name": "STR_BADGE_BEHAVIOUR_CABOOSE"},
            "driving_cab": {"name": "STR_BADGE_BEHAVIOUR_DRIVING_CAB"},
            "lgv_capable": {"name": "STR_BADGE_BEHAVIOUR_LGV_CAPABLE"},
            "provides_easter_egg_haulage_speed_bonus": {},
            "restaurant_car": {"name": "STR_BADGE_BEHAVIOUR_RESTAURANT_CAR"},
            "random_reverse": {},
            "randomised_wagon": {"name": "STR_BADGE_BEHAVIOUR_RANDOMISED_WAGON"},
            "receives_easter_egg_haulage_speed_bonus": {
                "name": "STR_BADGE_BEHAVIOUR_EASTER_EGG_HAULAGE_SPEED_BONUS"
            },
            "tilt": {"name": "STR_BADGE_BEHAVIOUR_TILT"},
        },
    },
    # many ih_formation_ruleset badges are provided by catalogues, but a handful must be provided even for rosters that don't contain any vehicles using the relevant badge
    "ih_formation_ruleset": {
        "sublabels": {
            "vehicle_reports_as/looks_like_pax_brake_car" : {},
            "vehicle_reports_as/restaurant_car": {},
        },
    },
}
