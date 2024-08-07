from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="phoenix",
        base_numeric_id=21120,
        name="Phoenix",
        role="express",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        fixed_run_cost_points=42,  # give a huge bonus so this can be a genuine mixed-traffic engine
        random_reverse=True,
        gen=5,
        # red stripe? Teeside steelmaster?
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "RAILFREIGHT_TRIPLE_GREY",
            "RAILFREIGHT_TRIPLE_GREY_COAL",
            "SWOOSH",
            "DB_SCHENKER",
            "LOADHAUL",
            "SWOOSH",
            "BANGER_BLUE",
        ],
        default_livery_extra_docs_examples=[("COLOUR_DARK_BLUE", "COLOUR_WHITE")],
        caboose_family="railfreight_2",
        decor_spriterow_num=8,
        show_decor_in_purchase_for_variants=[2, 3],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=110, vehicle_length=8, spriterow_num=0
    )

    consist.description = """We made these by uprating the Growler engine.  New paint too, don't spoil it."""
    consist.foamer_facts = """refurbished BR Class 37, with new alternator and uprated engine (per 2,000hp 37292)"""

    return consist
