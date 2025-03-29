from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="shearwater",
        base_numeric_id=15230,
        name="0-6-0 Shearwater",
        subrole="freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1250,
        },
        speed=60, # bumped to last 2 generations
        tractive_effort_coefficient=0.24,
        gen=2,
        intro_year_offset=5,  # let's be a little bit later for this one
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "FREIGHT_BLACK"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=65,
        vehicle_length=5,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=31, vehicle_length=3, rel_spriterow_index=1
    )

    model_def.define_description(
        """"""
    )
    model_def.define_foamer_facts("""NER Class C 0-6-0 (LNER J21)""") # ACTUALLY GWR 2251 CABBAGE, LNER J36 (NBR Class C)

    result.append(model_def)

    return result
