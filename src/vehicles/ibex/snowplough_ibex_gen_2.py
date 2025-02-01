from train import SnowploughEngineConsist


def main(roster_id, **kwargs):
    consist = SnowploughEngineConsist(
        roster_id=roster_id,
        id="snowplough_ibex_gen_2",
        base_numeric_id=9020,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    consist.add_unit(class_name="SnowploughUnit", weight=50, vehicle_length=4)

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
