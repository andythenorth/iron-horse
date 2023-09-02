from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="onslaught",
        base_numeric_id=13330,
        name="Onslaught",
        role="super_heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        gen=5,
        speed=125,  # Onslaught not replaced, but has gen 6 speeds
        intro_year_offset=-8,  # let's be really early with this one to give a mail engine matching Blaze HST intro year
        # additional_liveries=["BANGER_BLUE", "LARGE_LOGO", "FANCY_BLUE", "INTERCITY_RASPBERRY_RIPPLE", "RAILFREIGHT_TRIPLE_GREY", "DUTCH"],
        additional_liveries=["BANGER_BLUE"],
        decor_spriterow_num=7,
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # more?
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Aye I do like these. Right loud too."""
    consist.foamer_facts = (
        """BR Class 50, proposed English Electric / BR Class 51 <i>Super Deltic</i>"""
    )

    return consist
