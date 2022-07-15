from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="gowsty",
        base_numeric_id=10800,
        name="Gowsty",
        role="mail_railcar",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 280,
        },
        gen=3,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    consist.add_unit(
        type=DieselRailcarMailUnit,
        weight=30,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist.description = """A modern way to move mail and other parcels."""
    consist.foamer_facts = """LNER / Armstrong-Whitworth Railcars"""

    return consist
