from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="grid",
        base_numeric_id=12390,
        name="Grid",
        role="super_heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        intro_year_offset=-10,  # let's be a little bit earlier for this one
        gen=5,
        caboose_family="railfreight_1",
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE", "RAILFREIGHT_TRIPLE_GREY"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    consist.description = """These aren't bad at all."""
    consist.foamer_facts = """BR Class 56"""

    return consist
