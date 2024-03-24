from train import MailEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = MailEngineMetroConsist(
        roster_id=roster_id,
        id="wandle",
        base_numeric_id=1900,
        name="Wandle",
        role="mail_metro",
        role_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        gen=2,
        sprites_complete=True,
    )

    consist.add_unit(
        type=MetroUnit,
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=27,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist.description = """Is the underground a sanctuary? Refuge for the lost."""
    consist.foamer_facts = """London Underground R Stock"""

    return consist
