from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="SnowploughEngineConsist",
        id="snowplough_pony_gen_2",
        base_numeric_id=25130,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=True,
    )

    consist_factory.add_unit(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    consist_factory.add_description(
        """Does it ever snow here?  I wouldn't say, but these are waiting just in case."""
    )
    consist_factory.add_foamer_facts("""LNER / BR Independent Snowploughs""")

    return consist_factory
