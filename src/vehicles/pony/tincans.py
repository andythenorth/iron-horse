from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="tincans",
        base_numeric_id=370,
        name="Tincans",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "AC": 6200,  # match to Resistance
        },
        # dibble for game balance, assume some slip control
        tractive_effort_coefficient=0.34,
        gen=5,
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        pantograph_type="z-shaped-single",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=70,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    model_def.define_description(
        """“I would not wish any companion in the world but you.”"""
    )
    model_def.define_foamer_facts(
        """Polish PKP EU07 (derived from UK Class 83 design)"""
    )

    result.append(model_def)

    model_def = model_def.begin_clone(base_numeric_id=34950, unit_repeats=[1])

    model_def.complete_clone()

    result.append(model_def)

    return result
