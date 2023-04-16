from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="hercules",
        base_numeric_id=380,
        name="0-6-0 Hercules",
        role="freight",
        role_child_branch_num=2,
        power_by_power_source={
            "STEAM": 1100,
        },
        tractive_effort_coefficient=0.24,
        gen=1,
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=59, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    consist.description = (
        """Cheap to build, cheap to run.  I'll take a dozen at once."""
    )
    consist.foamer_facts = (
        """GWR 2301 Dean Goods Class, generic 0-6-0 freight locomotives"""
    )

    return consist
