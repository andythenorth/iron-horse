from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="evolution",
        base_numeric_id=14010,
        name="Evolution",
        role="heavy_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2950,
        },
        random_reverse=True,
        gen=6,
        intro_year_offset=-2,
        fixed_run_cost_points=70,  # give a bonus so this can be a genuine mixed-traffic engine
        additional_liveries=["FREIGHTLINER_GBRF"],
        default_livery_extra_docs_examples=[("COLOUR_BLUE", "COLOUR_WHITE")],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=112,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = """I've put new engines in some Resilients, we might get another fifty years out of them."""
    consist.foamer_facts = """BR Class 47, Brush Class 57, original TTD UU '47'"""

    return consist
