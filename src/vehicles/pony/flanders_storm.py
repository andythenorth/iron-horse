from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="flanders_storm",
        base_numeric_id=25150,
        name="Flanders Storm",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 6200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        caboose_family="railfreight_2",
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "RAILFREIGHT_TRIPLE_GREY", "DB_SCHENKER"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=120, vehicle_length=8, rel_spriterow_index=0
    )

    model_def.define_description(
        """This is a right proper engine.  Does work enough for two."""
    )
    model_def.define_foamer_facts("""BR Class 92""")

    result.append(model_def)

    return result
