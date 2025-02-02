from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="tincans",
        base_numeric_id=370,
        name="Tincans",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "AC": 6200,  # match to Resistance
        },
        # dibble for game balance, assume some slip control
        tractive_effort_coefficient=0.34,
        gen=5,
        intro_year_offset=-13,  # introduce earlier than gen epoch by design
        extended_vehicle_life=True,
        pantograph_type="z-shaped-single",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="ElectricEngineUnit",
        weight=70,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    consist_factory.define_description(
        """“I would not wish any companion in the world but you.”"""
    )
    consist_factory.define_foamer_facts(
        """Polish PKP EU07 (derived from UK Class 83 design)"""
    )

    consist_factory.add_clone(base_numeric_id=34950, clone_units=[1, 0])

    result.append(consist_factory)

    consist_factory = consist_factory.clone(base_numeric_id=34950)

    result.append(consist_factory)

    return result
