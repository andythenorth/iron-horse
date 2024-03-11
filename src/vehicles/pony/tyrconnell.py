from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tyrconnell",
        base_numeric_id=930,
        name="4-8-0 Tyrconnell",
        role="universal",
        role_child_branch_num=-4,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 900,
        },
        tractive_effort_coefficient=0.28,
        gen=2,
        intro_year_offset=-5,  # introduce early eh
        random_reverse=False,
        # note that livery names are metadata only and can repeat for different spriterows
        # additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist.add_unit(type=SteamEngineUnit, weight=45, vehicle_length=5, spriterow_num=0)

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=19, vehicle_length=3, spriterow_num=1
    )

    consist.description = """A titan from the North. Steadfast and stout."""
    consist.foamer_facts = (
        """Londonderry and Lough Swilly Railway Company 4-8-0 locomotives"""
    )

    return consist
