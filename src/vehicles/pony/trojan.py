from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="trojan",
        base_numeric_id=21450,
        name="Trojan",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=6,  # introduce later than gen epoch by design
        liveries=["CONVENTIONAL_WISDOM", "BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=95,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Steel yourself, this one's on the move.""")
    model_def.define_foamer_facts(
        """GEC Stephenson steel mill locomotives, Alco RSD-1 export switcher"""
    )

    result.append(model_def)

    return result
