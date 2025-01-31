from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineRailcarConsist",
        roster_id=roster_id,
        id="gowsty",
        base_numeric_id=21320,
        name="Gowsty",
        subrole="mail_railcar",
        subrole_child_branch_num=2,
        power_by_power_source={
            "DIESEL": 280,
        },
        gen=3,
        sprites_complete=True,
        intro_year_offset=-5,
    )  # introduce early by design

    consist_factory.add_unit(
        class_name="DieselRailcarMailUnit",
        weight=30,
        chassis="railcar_32px",
        tail_light="railcar_32px_1",
    )

    consist_factory.description = """A modern way to move mail and other parcels."""
    consist_factory.foamer_facts = """LNER / Armstrong-Whitworth Railcars"""

    return consist_factory
