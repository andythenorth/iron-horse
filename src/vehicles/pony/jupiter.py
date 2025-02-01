from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        id="jupiter",
        base_numeric_id=21840,
        name="Jupiter",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 680,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        use_3_unit_sets=True,
        gen=5,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="ElectricRailcarMailUnit",
        weight=35,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist_factory.description = (
        """A new generation of mail and express freight haulage."""
    )
    consist_factory.foamer_facts = """BR Class 302, BR Class 325"""

    return consist_factory
