from train import EngineConsist, ElectricEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="cyclone",
        base_numeric_id=27870,
        name="Cyclone",
        role="express",
        role_child_branch_num=-2,
        power_by_power_source={
            "AC": 2200,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="z-shaped-single",
        intro_year_offset=4,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "SWOOSH", "DB_SCHENKER", "INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_YELLOW"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=92, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Nippy as a whippet, eats miles like hot dinners. Proper electric workhorse, that one."""
    consist.foamer_facts = """Austrian Federal Railways (ÖBB) 1163 class"""

    return consist
