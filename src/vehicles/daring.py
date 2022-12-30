from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="daring",
        base_numeric_id=13960,
        name="Daring",
        role="express",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1750,
        },
        fixed_run_cost_points=116,  # give a small bonus so this can be a genuine mixed-traffic engine
        random_reverse=True,
        gen=4,
        intro_year_offset=1,  # let's be a littler later for this one
        default_livery_extra_docs_examples=[("COLOUR_GREEN", "COLOUR_WHITE")],
        caboose_family="gwr_1",
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=75,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = """Fast and light, right good."""
    consist.foamer_facts = """BR Class 35 <i>Hymek</i>"""

    return consist
