from train import SnowploughEngineConsist, SnowploughUnit


def main(roster_id, **kwargs):
    consist = SnowploughEngineConsist(
        roster_id=roster_id,
        id="snowplough_moose_gen_2",
        base_numeric_id=9000,
        name="Snowplough",
        gen=2,
        speed=75,
        sprites_complete=False,
    )

    consist.add_unit(type=SnowploughUnit, weight=50, vehicle_length=4)

    consist.description = """MOOSE."""
    consist.foamer_facts = """MOOSE"""

    return consist
