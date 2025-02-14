from train.train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="MailEngineRailcarConsist",
        base_id="scooby",
        base_numeric_id=21430,
        name="Scooby",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 420,
        },
        gen=4,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    model_def.add_unit_def(
        class_name="DieselRailcarMailUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    model_def.define_description(
        """A more modern way to move mail and other parcels."""
    )
    model_def.define_foamer_facts("""BR Class 128/130""")

    result.append(model_def)

    return result
