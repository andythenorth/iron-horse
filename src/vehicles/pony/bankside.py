from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineMetroConsist",
        id="bankside",
        base_numeric_id=1920,
        name="Bankside",
        subrole="mail_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 1100,
        },
        gen=3,
        default_livery_extra_docs_examples=[("COLOUR_RED", "COLOUR_BLUE")],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=30,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_3",
        repeat=2,
    )

    model_def.define_description("""Is it the screech of brakes?""")
    model_def.define_foamer_facts("""London Underground S Stock""")

    result.append(model_def)

    return result
