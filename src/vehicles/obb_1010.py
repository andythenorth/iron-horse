from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="obb_1010",
        base_numeric_id=10790,
        name="OBB 1010",
        role="super_heavy_express",
        role_child_branch_num=2,
        power=5300,
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_date_offset=9,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """ """
    )
    consist.foamer_facts = """OBB 1010"""

    return consist
