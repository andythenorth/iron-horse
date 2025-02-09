from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="maelstrom",
        base_numeric_id=21050,
        name="Maelstrom",
        subrole="heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2200,  # keep in line with equivalent gen general purpose engines
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=115, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """Not enough people see it as a healthy horse, pulling a sturdy wagon."""
    )
    model_def.define_foamer_facts("""BR Class 41""")

    result.append(model_def)

    return result
