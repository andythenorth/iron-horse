from train.model_def import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="thunderer",
        base_numeric_id=4830,
        name="4-6-0 Thunderer",  # shorter 2-6-0 version was tried, but doesn't fit a power band gap in the mixed traffic roster
        subrole="heavy_express",
        subrole_child_branch_num=-1,
        # this Joker ends with Intrepid, long-lived
        power_by_power_source={
            "STEAM": 1500,  # slightly less than the Swift (and lighter engine)
        },
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=140,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=2,
        intro_year_offset=10,  # introduce later than gen epoch by design
        liveries=["STOCK_STANDARD", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=82,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEngineTenderUnit",
        weight=30,
        vehicle_length=4,
        rel_spriterow_index=1,
    )

    model_def.define_description(
        """Bit of an odd beast this one.  It's quite happy on passengers and mail or you can put it on freight.  Right long-lived too."""
    )
    model_def.define_foamer_facts(
        """GWR 2900 <i>Saint</i> Class, GWR 4000 <i>Star</i> Class"""
    )

    result.append(model_def)

    return result
