from train import SnowploughEngineConsist, SnowploughUnit


def main(roster_id):
    consist = SnowploughEngineConsist(
        roster_id=roster_id,
        id="snowplough_ibex_gen_2",
        base_numeric_id=9020,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    consist.add_unit(type=SnowploughUnit, weight=50, vehicle_length=4)

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
