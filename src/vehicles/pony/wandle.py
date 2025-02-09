from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineMetroConsist",
        base_id="wandle",
        base_numeric_id=1900,
        name="Wandle",
        subrole="mail_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        base_track_type_name="METRO",
        gen=2,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MetroUnit",
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=27,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    model_def.define_description(
        """Is the underground a sanctuary? Refuge for the lost."""
    )
    model_def.define_foamer_facts("""London Underground R Stock""")

    result.append(model_def)

    return result
