from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="xerxes",
        base_numeric_id=2180,
        name="0-6-0+0-6-0 Xerxes",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1450,
        },
        random_reverse=True,
        gen=1,
        intro_year_offset=20,  # introduce much later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=140,  # minor run cost bonus as default algorithm makes run cost too high
        # note that livery names are metadata only and can repeat for different spriterows
        liveries=["VANILLA", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="SteamEnginePoweredUnit",
        weight=49,
        vehicle_length=5,
        rel_spriterow_index=0,
        repeat=2,
    )

    model_def.define_description("""Not much to say about these two.""")
    model_def.define_foamer_facts("""GWR pannier tanks, original TTD Kirby 'Paul'""")

    result.append(model_def)

    return result
