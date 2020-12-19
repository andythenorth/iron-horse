from train import MailEngineRailcarConsist, ElectroDieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="pylon",
        base_numeric_id=2120,
        name="Pylon",
        role="mail_railcar",
        role_child_branch_num=2,
        power=820,
        power_by_railtype={"RAIL": 700, "ELRL": 820},
        pantograph_type="z-shaped-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        use_3_unit_sets=True,
        gen=6,
        sprites_complete=True,
        intro_date_offset=-3,
    )  # introduce early by design

    consist.add_unit(
        type=ElectroDieselRailcarMailUnit,
        weight=36,
        chassis="railcar_32px",
        tail_light="railcar_32px_2",
    )

    consist.description = """The last word in mail-by-rail."""
    consist.foamer_facts = """Orion Class 769 <i>FLEX</i>"""

    return consist
