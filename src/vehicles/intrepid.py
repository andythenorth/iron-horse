from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="intrepid",
        base_numeric_id=4810,
        name="Intrepid",
        role="heavy_express",
        role_child_branch_num=-2,  # -ve because Joker
        power=2200,
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=40,  # give a bonus so this can be a genuine mixed-traffic engine
        intro_date_offset=6,  # let's be later for this one
        default_livery_extra_docs_examples=[("COLOUR_GREEN", "COLOUR_WHITE")],
        sprites_complete=True,
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
