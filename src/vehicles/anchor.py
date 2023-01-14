from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="anchor",
        base_numeric_id=12010,
        name="Anchor",
        role="freight",
        role_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 1700,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=6,  # introduce later than gen epoch by design
        additional_liveries=[],
        default_livery_extra_docs_examples=[
            ("COLOUR_YELLOW", "COLOUR_GREY"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = """"""
    consist.foamer_facts = """Hunslet bo-bo locomotives for BSC Scunthorpe works"""

    return consist
