from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineMetroConsist",
        id="serpentine",
        base_numeric_id=460,
        name="Serpentine",
        subrole="pax_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 550,
        },
        gen=1,
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="MetroUnit",
        weight=33,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    model_def.define_description(
        """Does the money feel good? Do you like your life well."""
    )
    model_def.define_foamer_facts(
        """London Underground 'Gate' Stock, Standard Stock"""
    )

    result.append(model_def)

    return result
