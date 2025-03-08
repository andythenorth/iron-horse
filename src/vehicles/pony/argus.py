from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="argus",
        base_numeric_id=21780,
        name="Argus",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 1300,
        },
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=3,
        intro_year_offset=4,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit", weight=67, vehicle_length=6, rel_spriterow_index=0
    )

    model_def.define_description("""Zoooom.""")
    model_def.define_foamer_facts("""SR CC1/CC2, BR Class 71""")

    result.append(model_def)

    return result
