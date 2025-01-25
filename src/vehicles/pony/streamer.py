from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="streamer",
        base_numeric_id=4840,
        name="4-6-4 Streamer",
        subrole="super_heavy_express",
        subrole_child_branch_num=-1,  # -ve because Joker
        power_by_power_source={
            "STEAM": 2300,
        },
        tractive_effort_coefficient=0.18,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=3,
        intro_year_offset=4,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_GREEN", "COLOUR_DARK_GREEN"),
            ("COLOUR_GREY", "COLOUR_WHITE"),
            ("COLOUR_WHITE", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=111,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (-2, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.add_unit(
        type=SteamEngineTenderUnit, weight=39, vehicle_length=4, spriterow_num=1
    )

    consist.description = (
        """Mr. Gresley did these. I'm sure he knows what he's doing."""
    )
    consist.foamer_facts = """LNER W1 'Hush Hush'"""

    return consist
