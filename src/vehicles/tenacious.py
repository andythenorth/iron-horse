from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="tenacious",
        base_numeric_id=15440,
        name="Tenacious",
        role="heavy_express",
        role_child_branch_num=-1,  # -ve because Joker
        replacement_consist_id="resilient",  # this Joker ends with Resilient
        power_by_power_source={
            "DIESEL": 2150,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=150,  # give a small bonus so this can be a genuine mixed-traffic engine
        default_livery_extra_docs_examples=[
            ("COLOUR_GREEN", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        caboose_family="gwr_1",
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=80,  # significant bonus over other of same power band
        vehicle_length=8,
        spriterow_num=0,
    )

    consist.description = """It's rapid, sprightly, and formidable all at once."""
    consist.foamer_facts = """BR Class 42/43 <i>Warship</i>"""

    return consist
