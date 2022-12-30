from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="merlion",
        base_numeric_id=15420,
        name="Merlion",
        role="freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        tractive_effort_coefficient=0.29,
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's be a littler earlier for this one
        caboose_family="railfreight_1",
        # add railfreight triple grey
        additional_liveries=["WHITE_STRIPE", "RAILFREIGHT_RED_STRIPE", "DUTCH"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=105,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = (
        """I don't like the looks of it right much, but I suppose it will do."""
    )
    consist.foamer_facts = """BR Class 31, uprated EE 12CSVT prime mover"""

    return consist
