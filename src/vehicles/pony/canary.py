from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineMetroConsist",
        base_id="canary",
        base_numeric_id=960,
        name="Canary",
        subrole="pax_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 1100,
        },
        base_track_type_name="METRO",
        gen=3,
        sprites_complete=True,
    )

    # should be 4 short units, not 2 long but eh
    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=36,
        capacity=200,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_3",
        repeat=2,
    )

    model_def.define_description("""Do Mondays go on slow-time?""")
    model_def.define_foamer_facts("""London Underground S Stock""")

    result.append(model_def)

    return result
