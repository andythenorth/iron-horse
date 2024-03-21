from train import MailEngineMetroConsist, MetroUnit


def main(roster_id, **kwargs):
    consist = MailEngineMetroConsist(
        roster_id=roster_id,
        id="tideway",
        base_numeric_id=2200,
        name="Tideway",
        role="mail_metro",
        role_child_branch_num=1,
        power_by_power_source={
            "METRO": 1050,
        },
        gen=3,
        default_livery_extra_docs_examples=[("COLOUR_RED", "COLOUR_BLUE")],
        sprites_complete=False,
    )

    consist.add_unit(
        type=MetroUnit,
        weight=29,
        # set capacity for freight; mail will be automatically calculated
        capacity=30,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist.description = """Do they whisper occasionally?"""
    consist.foamer_facts = """London Underground 1996 Stock"""

    return consist
