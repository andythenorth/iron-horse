from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        roster_id=roster_id,
        id="ares",
        base_numeric_id=20810,
        name="Ares",
        subrole="mail_railcar",
        subrole_child_branch_num=3,
        power_by_power_source={
            "AC": 400,
        },
        pantograph_type="diamond-single-with-base",
        easter_egg_haulage_speed_bonus=True,
        # use_3_unit_sets=True, # Ares only 2 unit sets, varies from other Pony mail railcars
        gen=3,
        sprites_complete=True,
        intro_year_offset=-3,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="ElectricRailcarMailUnit",
        weight=28,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist_factory.description = """A handy parcels car."""
    consist_factory.foamer_facts = """LNER <i>Tyneside Electrics</i>"""

    return consist_factory
