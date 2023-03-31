from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="stentor",
        base_numeric_id=14420,
        name="Stentor",
        role="super_heavy_freight",
        role_child_branch_num=-2,  # Joker eh
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=-2,  # let's be a little bit earlier for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        caboose_family="railfreight_2",
        additional_liveries=["RAILFREIGHT_TRIPLE_GREY"],
        sprites_complete=True,
        sprites_additional_liveries_needed=True, # copy livery from Super Stentor?
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=128,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist.description = """This one is loud, and packed with technology."""
    consist.foamer_facts = """BR Class 60 design mockups"""

    return consist
