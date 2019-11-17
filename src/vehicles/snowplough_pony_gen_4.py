from train import SnowploughEngineConsist, SnowploughUnit

def main(roster):
    consist = SnowploughEngineConsist(roster=roster,
                                      id='snowplough_pony_gen_4',
                                      base_numeric_id=4000,
                                      name='Snowplough',
                                      gen=4,
                                      speed=50,
                                      joker=True,
                                      sprites_complete=True)

    consist.add_unit(type=SnowploughUnit,
                     weight=50,
                     vehicle_length=4)

    return consist
