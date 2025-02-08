from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="quietus",
        base_numeric_id=21800,
        name="Quietus",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=3,  # in its own line as it's no neat fit to either diesel or electric progression
        power_by_power_source={
            "DIESEL": 2750,  # it's enough
            "AC": 7200,  # yolo, class 99 with a bit of a nerf
        },  # based on the Stadler Eurodual, really quite high values for both diesel and el (also matches Newag Dragon, which the shape is taken from)
        tractive_effort_coefficient=0.375,  # assume slip control magic
        random_reverse=True,
        pantograph_type="z-shaped-double",
        gen=6,
        fixed_run_cost_points=640,  # run cost nerf for high power + dual mode
        intro_year_offset=2,  # introduce later than gen epoch by design
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="ElectroDieselEngineUnit",
        weight=136,
        vehicle_length=8,
        spriterow_num=0,
    )

    model_def.define_description(
        """It'll get there and back again, in any weather."""
    )
    model_def.define_foamer_facts(
        """GBRF Class 99, Stadler Eurodual, Newag Dragon, CAF Bitrac"""
    )

    result.append(model_def)

    return result
