from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineRailcarConsist",
        id="breeze",
        base_numeric_id=21850,
        name="Breeze",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 520,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=5,
        sprites_complete=True,
        intro_year_offset=-3,  # introduce early by design
    )

    consist_factory.add_unit(
        class_name="ElectricRailcarPaxUnit",
        weight=38,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist_factory.add_description("""So Swiftly Home""")
    consist_factory.add_foamer_facts("""BR Class 319, Class 455""")

    return consist_factory
