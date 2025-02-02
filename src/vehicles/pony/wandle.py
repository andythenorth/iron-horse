from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="MailEngineMetroConsist",
        id="wandle",
        base_numeric_id=1900,
        name="Wandle",
        subrole="mail_metro",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "METRO": 900,
        },
        gen=2,
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="MetroUnit",
        weight=32,
        # set capacity for freight; mail will be automatically calculated
        capacity=27,
        chassis="metro_heavy_32px",
        tail_light="metro_32px_1",
        repeat=2,
    )

    consist_factory.define_description(
        """Is the underground a sanctuary? Refuge for the lost."""
    )
    consist_factory.define_foamer_facts("""London Underground R Stock""")

    result.append(consist_factory)

    return result
