from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
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

    model_def.add_unit(
        class_name="CabControlPaxCarUnit",
        weight=32,
        chassis="railcar_ng_32px",
        tail_light="railcar_32px_6",
        suppress_roof_sprite=True,
    )

    model_def.define_description("""For a view most spectacular.""")
    model_def.define_foamer_facts("""Generic panoramic coaches""")

    result.append(model_def)

    return result
