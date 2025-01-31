from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="MailEngineMetroConsist",
        roster_id=roster_id,
        id="ravensbourne",
        base_numeric_id=1910,
        name="Ravensbourne",
        subrole="mail_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="MetroUnit",
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=24,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist_factory.description = """Is that lamp light blinking?"""
    consist_factory.foamer_facts = """Metropolitan Railway electric multiple units"""

    return consist_factory
