from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineMetroConsist",
        base_id="fleet",
        base_numeric_id=210,
        name="Fleet",
        subrole="pax_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 1050,
        },
        base_track_type_name="METRO",
        gen=3,
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_RED"),
            ("COLOUR_RED", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    # should be 4 short units, not 2 long but eh
    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=33,
        capacity=200,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    model_def.define_description("""Was the train door jammed? Was the time right?""")
    model_def.define_foamer_facts("""London Underground 1996 Stock""")

    result.append(model_def)

    return result
