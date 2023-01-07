from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="intrepid",
        base_numeric_id=13850,
        name="Intrepid",
        role="heavy_express",
        role_child_branch_num=-1,  # -ve because Joker
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=40,  # give a bonus so this can be a genuine mixed-traffic engine
        intro_year_offset=6,  # let's be later for this one
        default_livery_extra_docs_examples=[("COLOUR_GREEN", "COLOUR_WHITE")],
        caboose_family="railfreight_1",
        # add triple grey railfreight
        additional_liveries=["LARGE_LOGO", "RAILFREIGHT_RED_STRIPE"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=115,  # bonus over Wyvern
        vehicle_length=8,
        spriterow_num=0,
    )

    consist.description = """These are a bit duff, but they're a bit lighter than a Wyvern so we'll give em a go."""
    consist.foamer_facts = """BR Class 47, prime mover downrated for reliability"""

    return consist
