from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="hawkinge",
        base_numeric_id=6410,
        name="4-8-2 Hawkinge",
        role="super_heavy_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 2350,
        },
        tractive_effort_coefficient=0.25,
        gen=3,
        intro_year_offset=5,  # introduce later than gen epoch by design
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=124,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=32, vehicle_length=4, spriterow_num=1
    )

    consist.description = """Mr. Bulleid designed these. Do you like 'em?"""
    consist.foamer_facts = (
        """SR Merchant Navy / West Country / Battle of Britain classes"""
    )

    return consist
