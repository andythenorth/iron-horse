from train import PassengerEngineCabControlCarConsist, CabControlPaxCarUnit


def main(roster_id, **kwargs):
    consist = PassengerEngineCabControlCarConsist(
        roster_id=roster_id,
        id="driving_cab_panoramic_passenger_ng_pony_gen_4",
        base_numeric_id=23510,
        name="Panoramic Driving Trailer",
        role_child_branch_num=-2,  # driving cab cars are probably jokers?
        base_track_type_name="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    consist.add_unit(
        type=CabControlPaxCarUnit,
        weight=32,
        chassis="railcar_ng_32px",
        tail_light="railcar_32px_6",
        suppress_roof_sprite=True,
    )

    consist.description = """For a view most spectacular."""
    consist.foamer_facts = """Generic panoramic coaches"""

    return consist
