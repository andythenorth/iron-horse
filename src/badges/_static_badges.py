# badges can be predefined here, or created dynamically for specific vehicle models etc as needed
static_badges = {
    "power_source": {
        "name": "STR_POWER_SOURCE",
    },
    "power_source_cabbage": {
        "sublabels": {
            "dual_voltage": {},
            "electro_diesel": {},
        },
    },
    "ih_ruleset_flags": {
        "sublabels": {
            "report_as_pax_car": {},
            "report_as_mail_car": {},
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
        },
    },
    "ih_variants_cabbage": {
        "sublabels": {
            "purchase_level_1_has_more_nested_variants": {},
        }
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
            "restaurant_car": {"name": "STR_BADGE_ROLE_RESTAURANT_CAR"},
            "suburban_or_universal_railcar": {"name": "STR_BADGE_ROLE_SUBURBAN"},
            "universal": {"name": "STR_BADGE_ROLE_GENERAL_PURPOSE"},
            "very_high_speed": {"name": "STR_BADGE_ROLE_INTERCITY_EXPRESS"},
        },
    },
    "special_flags": {
        "name": "STR_BADGE_SPECIAL_FLAGS",
        "sublabels": {
            "tilt": {"name": "STR_BADGE_SPECIAL_FLAG_TILT"},
            "ih_lgv_capable": {},
            "ih_random_reverse": {},
        },
    },
    "ih_behaviour": {
        "name": "STR_BADGE_BEHAVIOUR",
        "sublabels": {
            "randomised_wagon": {"name": "STR_BADGE_BEHAVIOUR_RANDOMISED_WAGON"},
        },
    },
}
