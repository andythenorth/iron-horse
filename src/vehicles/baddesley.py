from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="baddesley",
        base_numeric_id=6760,
        name="0-4-0+0-4-0 Baddesley",
        role="branch_freight",
        role_child_branch_num=-1,
        power=1000,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=3,
        intro_year_offset=-8,  # introduce earlier than gen epoch by design
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=65, vehicle_length=6, spriterow_num=0)

    consist.description = """."""
    consist.foamer_facts = """GARRATT"""

    return consist
