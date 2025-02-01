from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="traxx_e_494",
        base_numeric_id=34700,
        name="Captrain Italia E.494 Traxx 3 LM",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-1,
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

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=105, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """ """
    consist_factory.foamer_facts = """Captrain Italia E.494 Traxx 3 FS 140 DC Last Mile"""

    return consist_factory
