from train import (
    MailEngineExpressRailcarConsist,
    ElectricRailcarMailUnit,
)


def main(roster_id, **kwargs):
    consist = MailEngineExpressRailcarConsist(
        roster_id=roster_id,
        id="chronos",
        base_numeric_id=950,
        name="Chronos",
        role="express_mail_railcar",
        role_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={"AC": 2800},
        pantograph_type="z-shaped-single-with-base",
        gen=5,
        intro_year_offset=1,  # introduce later by design
        liveries="gen_5_and_6_mail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricRailcarMailUnit,
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    consist.description = """Time's courier swift. Chronos weaves through night and day. Posts haste, never late."""
    consist.foamer_facts = """BR Class 325 mail/parcels EMU"""

    return consist
