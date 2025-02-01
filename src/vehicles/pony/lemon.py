from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="lemon",
        base_numeric_id=270,
        name="4-8-0 Lemon",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,  # child branch 1 empty, for tech tree drawing reasons (blackthorn and quietus in branch -1)
        power_by_power_source={
            "STEAM": 2400,
        },
        speed=75,  # for lolz
        tractive_effort_coefficient=0.29,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=115,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=50, vehicle_length=4, spriterow_num=1
    )

    consist_factory.add_description(
        """I'm not saying I'm the best engine builder in the business, but I'd be in the top one."""
    )
    consist_factory.add_foamer_facts(
        """proposed LMS 'Lemon 4-8-0' freight locomotive, BR Standard Class 9F"""
    )

    return consist_factory
