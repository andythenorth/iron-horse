from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_type_id="swift",
        base_numeric_id=230,
        name="4-4-2 Swift",
        subrole="heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1550,
        },
        tractive_effort_coefficient=0.18,
        gen=2,
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "BANGER_BLUE"],
        cabbage_new_livery_system=True,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=80,
        vehicle_length=6,
        spriterow_num=0,
    )

    model_def.add_unit_def(
        class_name="SteamEngineTenderUnit", weight=35, vehicle_length=4, spriterow_num=1
    )

    model_def.define_description(
        """Eh it's the right big engine I said they needed. Mr. Raven helped me out a treat with this one."""
    )
    model_def.define_foamer_facts("""GNR Class C1, Class C2 <i>Klondike</i>""")

    result.append(model_def)

    return result
