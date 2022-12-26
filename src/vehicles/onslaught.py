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
            "DIESEL": 3300,
        },
        random_reverse=True,
        gen=5,
        speed=125,  # Onslaught not replaced, but has gen 6 speeds
        intro_year_offset=-8,  # let's be really early with this one to give a mail engine matching Blaze HST intro year
        fixed_run_cost_points=300,  # give a small malus to this one (balancing eh?)
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        additional_liveries=["RAILFREIGHT_TRIPLE_GREY"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Aye I do like these. Right loud too."""
    consist.foamer_facts = (
        """BR Class 50, proposed English Electric / BR Class 51 <i>Super Deltic</i>"""
    )

    return consist
