from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineMetroConsist",
        id="longwater",
        base_numeric_id=290,
        name="Longwater",
        subrole="mail_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 550,
        },
        gen=1,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="MetroUnit",
        weight=29,
        # set capacity for freight; mail will be automatically calculated
        capacity=24,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist_factory.description = """Do they bury themselves? Hidden from society?"""
    consist_factory.foamer_facts = """London Underground 'Gate' Stock, Standard Stock"""

    return consist_factory
