from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="vulcan",
        base_numeric_id=4930,
        name="Vulcan",
        role="heavy_express",
        role_child_branch_num=-3,
        power=2750,
        random_reverse=True,
        gen=4,
        intro_date_offset=1,  # introduce later than gen epoch by design
        fixed_run_cost_points=240,  # give a serious malus to this one (balancing eh?)
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_DARK_GREEN", "COLOUR_ORANGE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit,
        weight=105,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
    )

    consist.description = (
        """These aren't bad at all. Clever electronics they tell me."""
    )
    consist.foamer_facts = """English Electric DP2 prototype"""

    return consist
