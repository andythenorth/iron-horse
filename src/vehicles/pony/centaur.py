from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="centaur",
        base_numeric_id=17080,
        name="Centaur",
        subrole="express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        # red stripe? Teeside steelmaster?
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=[
            "VANILLA",
            "SWOOSH",
            "SWOOSH",
            "DB_SCHENKER",
            "SWOOSH",
            "RAILFREIGHT_TRIPLE_GREY",
            "RES",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_GREY", "COLOUR_YELLOW"),
            ("COLOUR_WHITE", "COLOUR_GREY"),
            ("COLOUR_GREY", "COLOUR_GREY"),
            ("COLOUR_PALE_GREEN", "COLOUR_PALE_GREEN"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_YELLOW", "COLOUR_YELLOW"),
        ],
        caboose_family="railfreight_2",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=90,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Technically, we're all half centaur.""")
    model_def.define_foamer_facts(
        """proposed BR Class 38 (Class 37 replacement), body shape derived from SNCF <i>Nez Cassés</i> ('broken nose') locomotive and originally proposed for BR Class 60; also Portugese CP Class 1930"""
    )

    result.append(model_def)

    return result
