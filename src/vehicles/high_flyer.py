from train import PassengerEngineExpressRailcarConsist, ElectricExpressRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="high_flyer",
        base_numeric_id=13260,
        name="High Flyer",
        role="express_pax_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power=840,
        pantograph_type="diamond-single-with-base",
        gen=3,
        intro_year_offset=2,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricExpressRailcarPaxUnit,
        weight=48,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist.description = """All Pullman Electric Express."""
    consist.foamer_facts = """SR 5-BEL <i>Brighton Belle</i>"""

    return consist
