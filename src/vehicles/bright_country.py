from train import PassengerEngineLuxuryRailcarConsist, ElectroDieselLuxuryRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineLuxuryRailcarConsist(
        roster_id=roster_id,
        id="bright_country",
        base_numeric_id=3800,
        name="Bright Country",
        role="luxury_pax_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power=1240,
        power_by_railtype={"RAIL": 620, "ELRL": 1240},
        pantograph_type="z-shaped-single-with-base",
        gen=6,
        intro_date_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselLuxuryRailcarPaxUnit,
        weight=51,  # penalty compared to previous gen due to diesel engines
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist.description = """She was like a bird for speed, an arrow for directness."""
    consist.foamer_facts = (
        """BR Class 442 <i>Wessex Express</i> (electro-diesel conversion)"""
    )

    return consist
