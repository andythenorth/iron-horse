from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="revolution",
        base_numeric_id=21610,
        name="Revolution",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2250,  # lol, same as Shredder eh?
            "AC": 5400,  # higher HP than Screamer, but heavier so similar HP / ton
        },
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        fixed_run_cost_points=470,  # run cost nerf for bi-mode flexibility + high el-power
        intro_year_offset=-2,  # introduce earlier than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # banger blue?
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=95,
        vehicle_length=8,
        spriterow_num=0,
    )

    model_def.define_description(
        """Bobby-dazzlers these are. How they fit it all in amazes me."""
    )
    model_def.define_foamer_facts("""Vossloh Euro Dual (DRS Class 88, ROG Class 93)""")

    result.append(model_def)

    return result
