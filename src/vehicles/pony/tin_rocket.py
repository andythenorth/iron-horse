from train import PassengerEngineRailcarConsist, DieselRailcarPaxUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineRailcarConsist(
        roster_id=roster_id,
        id="tin_rocket",
        base_numeric_id=21160,
        name="Tin Rocket",
        subrole="pax_railcar",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 400,
        },
        gen=5,
        sprites_complete=True,
        # introduce early by design
        intro_year_offset=-5,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=40,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist.description = (
        """Fast quiet trains for a new era. No more rattling Slammers."""
    )
    consist.foamer_facts = """BR Class 153/155/156/158 <i>Sprinters</i>"""

    return consist
