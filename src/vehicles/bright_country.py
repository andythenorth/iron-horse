from train import (
    PassengerEngineExpressRailcarConsist,
    ElectroDieselExpressRailcarPaxUnit,
)


def main(roster_id):
    consist = PassengerEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="bright_country",
        base_numeric_id=12840,
        name="Bright Country",
        role="express_pax_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={"DIESEL": 620, "AC": 1240},
        pantograph_type="z-shaped-single-with-base",
        lgv_capable=True,
        gen=6,
        intro_year_offset=1,  # introduce later by design
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselExpressRailcarPaxUnit,
        weight=51,  # penalty compared to previous gen due to diesel engines
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist.description = """She was like a bird for speed, an arrow for directness."""
    consist.foamer_facts = (
        """BR Class 442 <i>Wessex Express</i> (electro-diesel conversion)"""
    )

    return consist
