from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="booster",
        base_numeric_id=21760,
        name="Booster",
        subrole="branch_express",
        subrole_child_branch_num=2,
        power_by_power_source={"DIESEL": 600, "AC": 1600},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=4,
        intro_year_offset=7,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectroDieselEngineUnit",
        weight=70,
        vehicle_length=6,
        spriterow_num=0,
    )

    consist_factory.add_description(
        """I've rebuilt some of the Argus fleet to be more handy. Now we're sucking diesel."""
    )
    consist_factory.add_foamer_facts("""BR Class 71/74, Class 73""")

    return consist_factory
