from train import SnowploughEngineConsist


def main(roster_id, **kwargs):
    consist_factory = SnowploughEngineConsist(
        roster_id=roster_id,
        id="snowplough_ibex_gen_2",
        base_numeric_id=9020,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    consist_factory.add_unit(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    consist_factory.description = """"""
    consist_factory.foamer_facts = """"""

    return consist_factory
