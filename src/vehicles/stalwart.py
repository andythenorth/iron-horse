from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="stalwart",
        base_numeric_id=11440,
        name="Stalwart",
        role="ultra_heavy_express",
        role_child_branch_num=-1,
        power_by_power_source={
            "AC": 4000,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=6,  # introduce later than gen epoch by design
        # banger blue
        additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=110, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """"""

    return consist
