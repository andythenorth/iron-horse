from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="onslaught",
        base_numeric_id=4290,
        name="Onslaught",
        role="heavy_express",
        role_child_branch_num=3,
        power=3300,
        random_reverse=True,
        gen=5,
        intro_date_offset=-8,  # let's be really early with this one to give a mail engine matching Blaze HST intro date
        fixed_run_cost_points=300,  # give a small malus to this one (balancing eh?)
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        # alternative_cc_livery="RAILFREIGHT_TRIPLE_GREY",  # unfinished
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=100, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Aye I do like these. Right loud too."""
    consist.foamer_facts = (
        """BR Class 50, proposed English Electric / BR Class 51 <i>Super Deltic</i>"""
    )

    return consist
