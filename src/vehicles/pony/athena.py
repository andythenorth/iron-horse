from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineRailcarConsist(
        roster_id=roster_id,
        id="athena",
        base_numeric_id=20030,
        name="Athena",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 320,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=3,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    consist.add_unit(
        type=ElectricRailcarPaxUnit,
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist.description = """World's Greatest Suburban Electric"""
    consist.foamer_facts = """LNER <i>Tyneside Electrics</i>"""

    return consist
