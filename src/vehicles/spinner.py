from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="spinner",
        base_numeric_id=480,
        name="4-2-2 Spinner",
        role="express",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 950,
        },
        tractive_effort_coefficient=0.12,
        fixed_run_cost_points=160,  # minor cost bonus so it can make money
        gen=1,
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=48, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=3, spriterow_num=1
    )

    consist.description = """I told them they need a big engine, not big wheels.  But they pay the piper, so they call the tune.  It does go fast, I'll give it that."""
    consist.foamer_facts = (
        """Midland Railway 115 Class <i>Spinner</i>, GNR <i>Stirling Single</i>"""
    )

    return consist
