from train import SnowploughEngineConsist, SnowploughUnit


def main(roster_id):
    consist = SnowploughEngineConsist(
        roster_id=roster_id,
        id="snowplough_pony_gen_2",
        base_numeric_id=4000,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=True,
    )

    consist.add_unit(type=SnowploughUnit, weight=50, vehicle_length=4)

    consist.description = """Does it ever snow here?  I wouldn't say, but these are waiting just in case."""
    consist.foamer_facts = """LNER / BR Independent Snowploughs"""

    return consist
