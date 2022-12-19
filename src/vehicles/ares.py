from train import MailEngineRailcarConsist, ElectricRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(
        roster_id=roster_id,
        id="ares",
        base_numeric_id=11170,
        name="Ares",
        role="mail_railcar",
        role_child_branch_num=2,
        power_by_power_source={
            "AC": 400,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        # use_3_unit_sets=True, # Ares only 2 unit sets, varies from other Pony mail railcars
        gen=3,
        sprites_complete=False,
        intro_year_offset=-3,
    )  # introduce early by design

    consist.add_unit(
        type=ElectricRailcarMailUnit,
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist.description = """A handy parcels car."""
    consist.foamer_facts = """LNER <i>Tyneside Electrics</i>"""

    return consist
