from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="PassengerEngineMetroConsist",
        id="poplar",
        base_numeric_id=1930,
        name="Poplar",
        subrole="pax_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="MetroUnit",
        weight=36,
        capacity=120,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    model_def.define_description(
        """Do dreams fade in the dawn? Lost in the city's waking."""
    )
    model_def.define_foamer_facts(
        """Metropolitan Railway electric multiple units"""
    )

    result.append(model_def)

    return result
