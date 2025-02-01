from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineCabControlCarConsist",
        id="driving_cab_panoramic_passenger_ng_pony_gen_4",
        base_numeric_id=23510,
        name="Panoramic Driving Trailer",
        subrole_child_branch_num=-2,  # driving cab cars are probably jokers?
        base_track_type_name="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="CabControlPaxCarUnit",
        weight=32,
        chassis="railcar_ng_32px",
        tail_light="railcar_32px_6",
        suppress_roof_sprite=True,
    )

    consist_factory.add_description("""For a view most spectacular.""")
    consist_factory.add_foamer_facts("""Generic panoramic coaches""")

    result.append(consist_factory)

    return result
