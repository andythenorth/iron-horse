from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineMetroConsist",
        base_id="ravensbourne",
        base_numeric_id=1910,
        name="Ravensbourne",
        subrole="mail_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=24,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    model_def.define_description("""Is that lamp light blinking?""")
    model_def.define_foamer_facts("""Metropolitan Railway electric multiple units""")

    result.append(model_def)

    return result
