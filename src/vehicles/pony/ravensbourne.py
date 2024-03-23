from train import MailEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = MailEngineMetroConsist(
        roster_id=roster_id,
        id="ravensbourne",
        base_numeric_id=1910,
        name="Ravensbourne",
        role="mail_metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 600,
        },
        gen=1,
        sprites_complete=True,
    )

    consist.add_unit(
        type=MetroUnit,
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=24,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist.description = """Is that lamp light blinking?"""
    consist.foamer_facts = """Metropolitan Railway electric multiple units"""

    return consist
