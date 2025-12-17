from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="resistance",
        base_numeric_id=20990,
        name="Resistance",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "OHLE": 5200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        gen=5,
        intro_year_offset=-4,  # earlier than the IRL introduction of this never-built train...
        extended_vehicle_life=True,
        pantograph_type="z-shaped-double",
        liveries=[
            "CLASSIC_LINES",
            "RAILFREIGHT_RED_STRIPE",
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY", # coal
            "LOWER_LINES",
            "CONVENTIONAL_WISDOM",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ElectricEngineUnit",
        weight=120,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""A hard-charging bag of bones.""")
    model_def.define_foamer_facts(
        """Proposed BR Class 88, derived from Class 58 design"""
    )

    result.append(model_def)

    return result
