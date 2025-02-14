from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineCabControlCarConsist",
        base_id="driving_cab_passenger_ng_pony_gen_4",
        base_numeric_id=23260,
        name="Driving Trailer",
        subrole_child_branch_num=-1,  # driving cab cars are probably jokers?
        base_track_type_name="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="CabControlPaxCarUnit", weight=32, chassis="4_axle_ng_32px"
    )

    model_def.define_description(
        """Now, a driving cab for the smaller trains. But not for goats."""
    )
    model_def.define_foamer_facts(
        """KiwiRail SRV driving cab conversion of British Rail MK2 carriage"""
    )

    result.append(model_def)

    return result
