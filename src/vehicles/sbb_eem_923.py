from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sbb_eem_923",
        base_numeric_id=13950,
        name="SBB Eem 923",
        role="branch_express",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 750,
            "AC": 2000,
        },  # IRL 400 HP at rail for diesel modes, but gets a bump for gameplay
        random_reverse=True,
        gen=5,
        pantograph_type="diamond-double",
        intro_year_offset=10,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit, weight=105, vehicle_length=6, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """DR E 21 51"""

    return consist
