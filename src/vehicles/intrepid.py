from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="intrepid",
        base_numeric_id=4810,
        name="Intrepid",
        role="heavy_express",
        role_child_branch_num=-1,  # -ve because Joker
        power=2200,
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=40,  # give a bonus so this can be a genuine mixed-traffic engine
        intro_date_offset=2,  # let's be a tiny bit later for this one
        default_livery_extra_docs_examples=[("COLOUR_GREEN", "COLOUR_WHITE")],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=115,  # bonus over Wyvern
        vehicle_length=8,
        spriterow_num=0,
    )

    consist.description = """They've put a non-standard hydraulic transmission in these, but they're a bit lighter than a Wyvern so we'll give em a go."""
    consist.foamer_facts = """BR Class 35 <i>Hymek</i>, Brush <i>Falcon</i> prototype and BRCW <i>Lion</i> prototype"""

    return consist
