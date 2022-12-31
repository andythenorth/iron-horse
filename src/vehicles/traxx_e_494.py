from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="traxx_e_494",
        base_numeric_id=14870,
        name="Captrain Italia E.494 Traxx 3 LM",
        role="ultra_heavy_freight",
        role_child_branch_num=-1,
        # !! maybe add last mile diesel?  tends to not be useful on high HP electrics, but eh...?
        power_by_power_source={"DC": 7400, "DIESEL": 2000},
        random_reverse=True,
        gen=6,
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
    consist.foamer_facts = """Captrain Italia E.494 Traxx 3 FS 140 DC Last Mile"""

    return consist
