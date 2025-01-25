from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineRailcarConsist(
        roster_id=roster_id,
        id="breeze",
        base_numeric_id=21850,
        name="Breeze",
        subrole="pax_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "AC": 520,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=5,
        sprites_complete=True,
        intro_year_offset=-3,  # introduce early by design
    )

    consist.add_unit(
        type=ElectricRailcarPaxUnit,
        weight=38,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
    )

    consist.description = """So Swiftly Home"""
    consist.foamer_facts = """BR Class 319, Class 455"""

    return consist
