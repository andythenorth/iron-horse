from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        id="scooby",
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

    consist_factory.add_unit(
        class_name="DieselRailcarMailUnit",
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist_factory.add_description(
        """A more modern way to move mail and other parcels."""
    )
    consist_factory.add_foamer_facts("""BR Class 128/130""")

    return consist_factory
