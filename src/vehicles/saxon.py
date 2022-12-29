from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="saxon",
        base_numeric_id=10370,
        name="0-8-0 Saxon",
        role="branch_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1000,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=3,
        intro_year_offset=-8,  # introduce earlier than gen epoch by design
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=False,
    )

    consist.add_unit(type=SteamEngineUnit, weight=65, vehicle_length=6, spriterow_num=0)

    consist.description = """I didn't do these, we've shipped them in. On ships like. On the sea. They pull well mind you."""
    consist.foamer_facts = """SR Z class, SR USA class (USATC S100 Class)"""

    return consist
