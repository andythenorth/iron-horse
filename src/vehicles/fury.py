from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="fury",
        base_numeric_id=11220,
        name="Fury",
        role="super_heavy_express",
        role_child_branch_num=-4,
        power_by_power_source={
            "AC": 3600, # supposed to be mid-powered, but maintains same hp/speed ratio of previous gen, or it will be too nerfed for 125mph
        },
        random_reverse=True,
        gen=5,
        speed=125, # Fury not replaced, but has gen 6 speeds
        pantograph_type="z-shaped-double",
        intro_year_offset=1,  # introduce later than gen epoch by design
        # intercity, railfreight?
        additional_liveries=["SWOOSH", "FREIGHTLINER_GBRF", "RES"],
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=82, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """Rebuilt the Roarers. Very sound these are, last a long time they will."""
    )
    consist.foamer_facts = """rebuilt BR 'AL' Classes 81-85"""

    return consist
