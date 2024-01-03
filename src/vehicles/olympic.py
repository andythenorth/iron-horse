from train import PassengerEngineExpressRailcarConsist, ElectricExpressRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="olympic",
        base_numeric_id=900,
        name="Olympic",
        role="express_pax_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "AC": 2400,
        },
        pantograph_type="z-shaped-single-with-base",
        gen=5,
        intro_year_offset=1,  # introduce later by design
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricExpressRailcarPaxUnit,
        weight=46,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist.description = """Faster with control. Always faster. Always control."""
    consist.foamer_facts = """BR Class 442 <i>Wessex Express</i>"""

    return consist
