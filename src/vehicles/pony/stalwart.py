from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="stalwart",
        base_numeric_id=21380,
        name="Stalwart",
        subrole="ultra_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "AC": 3800,  # clear separation from Roarer?
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=-1,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        # additional_liveries=["BANGER_BLUE", "SWOOSH", "WHITE_STRIPE", "SWOOSH", "RAILFREIGHT_RED_STRIPE",],
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[
            "BANGER_BLUE",
            "WHITE_STRIPE",
            "SWOOSH",
            "RAILFREIGHT_RED_STRIPE",
        ],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # unfinished livery with yellow stripe
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=115, vehicle_length=8, spriterow_num=0
    )

    consist_factory.description = """They really pushed the boat out for this one."""
    consist_factory.foamer_facts = (
        """Metropolitan-Vickers 46 Class exported from UK to New South Wales"""
    )

    return consist_factory
