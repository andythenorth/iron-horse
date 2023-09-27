from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="maelstrom",
        base_numeric_id=9440,
        name="Maelstrom",
        role="heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2200,  # keep in line with equivalent gen general purpose engines
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        additional_liveries=["SWOOSH_LESS", "BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=115, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """Not enough people see it as a healthy horse, pulling a sturdy wagon."""
    )
    consist.foamer_facts = """BR Class 41"""

    return consist
