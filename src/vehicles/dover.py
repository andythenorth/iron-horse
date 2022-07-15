from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="dover",
        base_numeric_id=9740,
        name="Dover",
        role="mail_railcar",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 540,
        },
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        use_3_unit_sets=True,
        gen=4,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    consist.add_unit(
        type=ElectricRailcarMailUnit,
        weight=35,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist.description = """A useful motor van for mail and express freight."""
    consist.foamer_facts = """BR Class 419 MLV, Class 489 GLV"""

    return consist
