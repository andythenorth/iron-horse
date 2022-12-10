from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cheddar_valley",
        base_numeric_id=9260,
        name="Cheddar Valley",
        role="super_heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 4050,  # 750hp steps Vanguard -> Grid -> Cheddar Valley
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=3,  # let's be a little bit later for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        alternative_liveries=["YEOMAN"],
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_GREEN"),
            ("COLOUR_ORANGE", "COLOUR_RED"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=125,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = """I shipped these in from overseas.  Pull you backwards through a wall this one will.  Right proper engine."""
    consist.foamer_facts = (
        """GMD  / EMD Class 59, uprated GMD / EMD 710 series prime mover"""
    )

    return consist
