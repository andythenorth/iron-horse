from train import PassengerEngineRailcarConsist, ElectricRailcarPaxUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineRailcarConsist(
        roster_id=roster_id,
        id="emu_ibex_4",
        base_numeric_id=34530,
        name="SBB RABDe 12/12",
        role="pax_railcar",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 320,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        gen=4,
        sprites_complete=False,
        # intro_year_offset=-3,
    )

    consist.add_unit(
        type=ElectricRailcarPaxUnit,
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist.description = """ """
    consist.foamer_facts = """SBB RABDe 12/12"""

    return consist
