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
            "express": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE_EXPRESS"},
            "express_railcar": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE_EXPRESS"},
            "freight": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE_FREIGHT"},
            "gronk": {"name": "STR_BADGE_ROLE_GRONK"},
            "high_power_railcar": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE_EXPRESS"},
            "hst": {"name": "STR_BADGE_ROLE_INTERCITY_EXPRESS"},
            "lolz": {"name": "STR_BADGE_ROLE_LOLZ"},
            "mail_railcar": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE"},
            "metro": {"name": "STR_BADGE_ROLE_METRO"},
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
            "provides_easter_egg_haulage_speed_bonus": {},
            "restaurant_car": {"name": "STR_BADGE_BEHAVIOUR_RESTAURANT_CAR"},
            "randomised_wagon": {"name": "STR_BADGE_BEHAVIOUR_RANDOMISED_WAGON"},
            "receives_easter_egg_haulage_speed_bonus": {
                "name": "STR_BADGE_BEHAVIOUR_EASTER_EGG_HAULAGE_SPEED_BONUS"
            },
            "tilt": {"name": "STR_BADGE_SPECIAL_FLAG_TILT"},
            "lgv_capable": {},
            "random_reverse": {},
        },
    },
}
