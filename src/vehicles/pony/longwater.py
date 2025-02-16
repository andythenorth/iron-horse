from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineMetro",
        model_type_id="longwater",
        base_numeric_id=290,
        name="Longwater",
        subrole="mail_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 550,
        },
        base_track_type_name="METRO",
        gen=1,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=29,
        # set capacity for freight; mail will be automatically calculated
        capacity=24,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    model_def.define_description("""Do they bury themselves? Hidden from society?""")
    model_def.define_foamer_facts("""London Underground 'Gate' Stock, Standard Stock""")

    result.append(model_def)

    return result
