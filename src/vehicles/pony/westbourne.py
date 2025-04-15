from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineMetro",
        model_id="westbourne",
        base_numeric_id=360,
        name="Westbourne",
        subrole="pax_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 850,
        },
        base_track_type="METRO",
        gen=2,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=33,
        capacity=160,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    model_def.define_description("""Does the public want what the public gets?""")
    model_def.define_foamer_facts("""London Underground 1938/1949 Stock""")

    result.append(model_def)

    return result
