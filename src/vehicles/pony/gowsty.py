from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="MailEngineRailcarConsist",
        id="gowsty",
        base_numeric_id=21320,
        name="Gowsty",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 280,
        },
        gen=3,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    model_type_factory.define_unit(
        class_name="DieselRailcarMailUnit",
        weight=30,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    model_type_factory.define_description(
        """A modern way to move mail and other parcels."""
    )
    model_type_factory.define_foamer_facts("""LNER / Armstrong-Whitworth Railcars""")

    result.append(model_type_factory)

    return result
