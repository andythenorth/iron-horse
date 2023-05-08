from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="stalwart",
        base_numeric_id=11440,
        name="Stalwart",
        role="ultra_heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "AC": 3800, # clear separation from Roarer?
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=-1,  # introduce earlier than gen epoch by design
        #additional_liveries=["BANGER_BLUE", "SWOOSH", "WHITE_STRIPE", "2CC", "RAILFREIGHT_RED_STRIPE",],
        additional_liveries=["BANGER_BLUE", "WHITE_STRIPE", "2CC", "RAILFREIGHT_RED_STRIPE",],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
        sprites_additional_liveries_potential=True, # unfinished livery with yellow stripe
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=115, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """They really pushed the boat out for this one."""
    )
    consist.foamer_facts = """Metropolitan-Vickers 46 Class exported from UK to New South Wales"""

    return consist
