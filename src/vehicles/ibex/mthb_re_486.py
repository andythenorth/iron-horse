from train import EngineConsist, ElectricEngineUnit

# !! based on MittelThurgauBahn MThB Re486 of 2000 - sold to SBB Cargo Re481, see also DB cargo 145
# !! actually a predecessor of Traxx


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="mthb_re_486",
        base_numeric_id=8970,
        name="MTHB Re 486",
        role="super_heavy_freight",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 5600,
            "DC": 5600,
        },
        random_reverse=True,
        gen=5,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
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

    consist.description = """ """
    consist.foamer_facts = """MTHB Re 486 (precursor to Traxx)"""

    return consist
