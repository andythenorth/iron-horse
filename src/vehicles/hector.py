from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="hector",
        base_numeric_id=14550,
        name="Hector",  # the name is because BR 86 222 and 86 223 reasons
        role="super_heavy_express",
        role_child_branch_num=3,
        power_by_power_source={
            "AC": 4040,  # such realism, per wikipedia-is-definitely-true
        },
        random_reverse=True,
        gen=6,
        pantograph_type="z-shaped-double",
        intro_year_offset=1,  # introduce later than gen epoch by design
        alternative_liveries=["FREIGHTLINER_GBRF"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_PALE_GREEN"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=83, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Life-extended the Fury, wasn't a big job. They just keep going on these do."""
    consist.foamer_facts = """BR Class 86"""

    return consist
