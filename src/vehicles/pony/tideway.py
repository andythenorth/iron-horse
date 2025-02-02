from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="MailEngineMetroConsist",
        id="tideway",
        base_numeric_id=2200,
        name="Tideway",
        subrole="mail_metro",
        subrole_child_branch_num=1,
        power_by_power_source={
            "METRO": 1050,
        },
        gen=3,
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="MetroUnit",
        weight=29,
        # set capacity for freight; mail will be automatically calculated
        capacity=30,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    consist_factory.define_description("""Do they whisper occasionally?""")
    consist_factory.define_foamer_facts("""London Underground 1996 Stock""")

    result.append(consist_factory)

    return result
