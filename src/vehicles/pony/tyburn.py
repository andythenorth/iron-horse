from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineMetroConsist",
        roster_id=roster_id,
        id="tyburn",
        base_numeric_id=2190,
        name="Tyburn",
        subrole="mail_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 850,
        },
        gen=2,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="MetroUnit",
        weight=29,
        # set capacity for freight; mail will be automatically calculated
        capacity=27,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist_factory.description = """Do moles live in holes underground? Can they be found?"""
    consist_factory.foamer_facts = """London Underground 1938/1949 Stock"""

    return consist_factory
