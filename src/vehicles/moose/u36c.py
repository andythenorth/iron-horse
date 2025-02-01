from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="u36c",
        base_numeric_id=22030,
        name="U36C",
        subrole="super_heavy_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "DIESEL": 3600,  # first high HP diesel in this roster??
        },
        random_reverse=True,
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=160,
        vehicle_length=8,
    )

    consist_factory.description = """"""
    consist_factory.foamer_facts = (
        """"""
    )

    return consist_factory
