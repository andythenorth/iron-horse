from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="fs_e636",
        base_numeric_id=140,
        name="FS E.636",
        role="heavy_express",
        role_child_branch_num=-2,
        power_by_power_source={"DC": 2800},
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    # !!! these are only 60 foot long IRL so 2x 4/8 units

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=4, spriterow_num=0, repeat=2
    )

    consist.description = """ """
    consist.foamer_facts = """FS E.636"""

    return consist
