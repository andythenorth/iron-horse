from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="onslaught",
        base_numeric_id=21470,
        name="Onslaught",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=-8,  # let's be really early with this one to give a mail engine matching Blaze HST intro year
        # additional_liveries=["BANGER_BLUE", "LARGE_LOGO", "SWOOSH", "INTERCITY_RASPBERRY_RIPPLE", "RAILFREIGHT_TRIPLE_GREY", "DUTCH_1986"],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "DB_SCHENKER"],
        decor_spriterow_num=8,
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # more?
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit", weight=100, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """Aye I do like these. Right loud too."""
    consist_factory.foamer_facts = (
        """BR Class 50, proposed English Electric / BR Class 51 <i>Super Deltic</i>"""
    )

    return consist_factory
