from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="dryth",
        base_numeric_id=4880,
        name="Dryth",
        subrole="ultra_heavy_freight",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "AC": 2900,
        },
        speed=75,  # continues a long way into gen 4, so go faster
        gen=3,
        pantograph_type="diamond-single",
        intro_year_offset=8,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit",
        weight=70,
        vehicle_length=6,
        spriterow_num=0,
        repeat=2,
    )

    consist_factory.description = (
        """He paws fiercely, rejoicing in his strength, and charges into the fray."""
    )
    consist_factory.foamer_facts = (
        """SR CC1/CC2 locomotives, English Electric export boxcab locomotives"""
    )

    consist_factory.add_clone(base_numeric_id=34930, clone_units=[1, 0])

    return consist_factory
