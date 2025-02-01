from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineExpressRailcarConsist",
        id="high_flyer",
        base_numeric_id=4120,
        name="High Flyer",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "AC": 1600,
        },
        pantograph_type="diamond-single-with-base",
        gen=3,
        intro_year_offset=2,  # introduce later by design
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricExpressRailcarPaxUnit",
        weight=48,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist_factory.add_description("""All Pullman Electric Express.""")
    consist_factory.add_foamer_facts("""SR 5-BEL <i>Brighton Belle</i>""")

    return consist_factory
