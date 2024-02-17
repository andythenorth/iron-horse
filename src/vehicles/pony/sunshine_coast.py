from train import PassengerEngineExpressRailcarConsist, ElectricExpressRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="sunshine_coast",
        base_numeric_id=4130,
        name="Sunshine Coast",
        role="express_pax_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "AC": 1900,
        },
        pantograph_type="z-shaped-single-with-base",
        gen=4,
        intro_year_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricExpressRailcarPaxUnit,
        weight=45,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist.description = (
        """Better three hours too soon than a minute too late."""  # Shakespeare
    )
    consist.foamer_facts = """BR Class 309 <i>Clacton Express</i>, BR 4-REP"""

    return consist
