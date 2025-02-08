from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineMetroConsist",
        id="hammersmith",
        base_numeric_id=1890,
        name="Hammersmith",
        subrole="pax_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        gen=2,
        sprites_complete=True,
    )

    model_def.add_unit(
        class_name="MetroUnit",
        weight=36,
        capacity=160,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    model_def.define_description(
        """Do pigeons roost on rooftops? Do they watch us pass by?"""
    )
    model_def.define_foamer_facts("""London Underground R Stock""")

    result.append(model_def)

    return result
