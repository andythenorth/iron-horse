from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="super_stentor",
        base_numeric_id=15780,
        name="Super Stentor",
        role="super_heavy_freight",
        role_child_branch_num=-2,  # Joker eh
        power_by_power_source={
            "DIESEL": 4550,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=2,  # let's be a little bit later for this one
        gen=6,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        # schenker?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=129,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = """Make Stentor great again."""
    consist.foamer_facts = """Re-engineered and uprated class 60."""

    return consist
