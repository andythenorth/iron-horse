from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="trient",
        base_numeric_id=9030,
        name="Trient",
        role="super_heavy_freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 4050,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=3,  # let's be a little bit later for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_GREEN"),
            ("COLOUR_ORANGE", "COLOUR_RED"),
        ],
        requires_high_clearance=True,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=125,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = """CABBAGE."""
    consist.foamer_facts = (
        """CABBAGE - GMD  / EMD Class 59, uprated GMD / EMD 710 series prime mover"""
    )

    return consist
