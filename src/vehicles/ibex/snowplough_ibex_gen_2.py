from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="SnowploughEngineConsist",
        id="snowplough_ibex_gen_2",
        base_numeric_id=9020,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    consist_factory.define_unit(
        class_name="SnowploughUnit", weight=50, vehicle_length=4
    )

    consist_factory.define_description("""""")
    consist_factory.define_foamer_facts("""""")

    result.append(consist_factory)

    return result
