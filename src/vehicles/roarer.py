from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="roarer",
        base_numeric_id=11270,
        name="Roarer",
        role="super_heavy_express",
        role_child_branch_num=3,
        power_by_power_source={
            "AC": 3000,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=3,  # introduce later than gen epoch by design
        # banger blue
        additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=80, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """They're right loud these are, but we've got the power right up on em too."""
    )
    consist.foamer_facts = """BR 'AL' Classes 81-85"""

    return consist
