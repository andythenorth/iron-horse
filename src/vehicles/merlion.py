from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="merlion",
        base_numeric_id=15420,
        name="Merlion",
        role="freight",
        role_child_branch_num=-1,
        power=1750,
        tractive_effort_coefficient=0.29,
        random_reverse=True,
        gen=4,
        intro_date_offset=-2,  # let's be a littler earlier for this one
        force_caboose_families={
            "caboose_car": "pony_railfreight_1",
            "goods_caboose_car": "pony_railfreight_1",
        },
        alternative_cc_livery="RAILFREIGHT_RED_STRIPE",
        sprites_complete=True,
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
