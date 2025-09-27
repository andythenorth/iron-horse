from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="stalwart",
        base_numeric_id=21380,
        name="Stalwart",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "OHLE": 3800,  # clear separation from Roarer?
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=-1,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        liveries=[
            "STOCK_STANDARD",
            "BANGER_BLUE",
            "CLASSIC_LINES",
            "VANILLA",
            "RAILFREIGHT_RED_STRIPE",
        ],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="ElectricEngineUnit",
        weight=115,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""They really pushed the boat out for this one.""")
    model_def.define_foamer_facts(
        """Metropolitan-Vickers 46 Class exported from UK to New South Wales"""
    )

    result.append(model_def)

    return result
