from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        id="dover",
        base_numeric_id=21150,
        name="Dover",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 540,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        use_3_unit_sets=True,
        gen=4,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="ElectricRailcarMailUnit",
        weight=35,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist_factory.add_description(
        """A useful motor van for mail and express freight."""
    )
    consist_factory.add_foamer_facts("""BR Class 419 MLV, Class 489 GLV""")

    return consist_factory
