from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="relentless",
        base_numeric_id=4400,
        name="Relentless",
        role="heavy_express",
        role_child_branch_num=3,
        power=3950,  # slightly more than standard progression, to enable higher speed to be reach quickly
        random_reverse=True,
        gen=6,
        intro_date_offset=-7,  # let's be earlier on this to keep the mail up with the HSTs etc
        fixed_run_cost_points=300,  # give a small malus to this one (balancing eh?)
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=95, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Solid piece of kit these."""
    consist.foamer_facts = (
        """Newag Griffin, Bombardier Traxx 2, Stadler Euro 4001, Siemens EuroRunner"""
    )

    return consist
