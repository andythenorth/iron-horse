from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="lemon",
        base_numeric_id=270,
        name="4-8-0 Lemon",
        role="super_heavy_freight",
        role_child_branch_num=1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power_by_power_source={
            "STEAM": 2400,
        },
        speed=75,  # for lolz
        tractive_effort_coefficient=0.29,
        gen=3,
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=115,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=50, vehicle_length=4, spriterow_num=1
    )

    consist.description = """I'm not saying I'm the best engine builder in the business, but I'd be in the top one."""
    consist.foamer_facts = (
        """proposed LMS 'Lemon 4-8-0' freight locomotive, BR Standard Class 9F"""
    )

    return consist
