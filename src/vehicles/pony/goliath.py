from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="goliath",
        base_numeric_id=21230,
        name="Goliath",
        subrole="branch_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1650,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=5,
        intro_year_offset=2,  # introduce later than gen epoch by design
        liveries=["LOWER_LINES", "STOCK_STANDARD", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=71,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description("""It gets the job done either way.""")
    model_def.define_foamer_facts("""YEC <i>Janus</i>, Corus <i>Trojan</i>""")

    result.append(model_def)

    return result
