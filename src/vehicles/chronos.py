from train import (
    MailEngineExpressRailcarConsist,
    ElectricRailcarMailUnit,
)


def main(roster_id):
    consist = MailEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="chronos",
        base_numeric_id=6400,
        name="Chronos",
        role="express_mail_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={"AC": 2800},
        pantograph_type="z-shaped-single-with-base",
        gen=5,
        intro_year_offset=1,  # introduce later by design
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricRailcarMailUnit,
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2
    )

    consist.description = """She was like a bird for speed, an arrow for directness."""
    consist.foamer_facts = """BR Class 325 mail/parcels EMU"""

    return consist
