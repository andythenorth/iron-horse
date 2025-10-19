from train.producer import ModelDef


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
        liveries=[
            "RIDEWELL",
            "BANGER_BLUE",
            "SHOW_PONY",
            "LOWER_LINES",
            "STOCK_STANDARD",
            "RAILFREIGHT_TRIPLE_GREY",
            "MAIL_BY_RAIL",
        ],
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
