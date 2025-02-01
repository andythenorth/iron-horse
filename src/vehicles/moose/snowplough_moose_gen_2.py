from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="SnowploughEngineConsist",
        id="snowplough_moose_gen_2",
        base_numeric_id=34890,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    consist_factory.add_unit(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    consist_factory.description = """MOOSE."""
    consist_factory.foamer_facts = """MOOSE"""

    return consist_factory
