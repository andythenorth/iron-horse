from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="sdp40f",
        base_numeric_id=22040,
        name="sdp40f",
        subrole="heavy_express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "DIESEL": 2800, # nerfed to account for HEP
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
