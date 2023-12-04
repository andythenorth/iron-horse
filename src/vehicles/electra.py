from train import (
    MailEngineExpressRailcarConsist,
    ElectricRailcarMailUnit,
)


def main(roster_id):
    consist = MailEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="electra",
        base_numeric_id=11080,
        name="Electra", # or RedStar?
        role="express_mail_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={"AC": 1120},
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
    )

    consist.description = """She was like a bird for speed, an arrow for directness."""
    consist.foamer_facts = (
        """BR Class 325"""
    )

    return consist
