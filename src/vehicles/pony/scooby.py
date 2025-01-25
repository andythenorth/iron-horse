from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster_id, **kwargs):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="scooby",
        base_numeric_id=21430,
        name="Scooby",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 420,
        },
        gen=4,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    consist.add_unit(
        type=DieselRailcarMailUnit,
        weight=37,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist.description = """A more modern way to move mail and other parcels."""
    consist.foamer_facts = """BR Class 128/130"""

    return consist
