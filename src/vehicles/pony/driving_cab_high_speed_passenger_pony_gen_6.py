from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="PassengerEngineCabControlCarConsist",
        id="driving_cab_high_speed_passenger_pony_gen_6",
        base_numeric_id=19920,
        name="High Speed Driving Trailer",
        subrole_child_branch_num=-3,  # driving cab cars are probably jokers?
        gen=6,
        lgv_capable=True,  # for lolz
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="CabControlPaxCarUnit", weight=32, chassis="railcar_32px"
    )

    model_def.define_description(
        """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    )
    model_def.define_foamer_facts(
        """CAF MK5A Driving Trailer (DT) with added generator"""
    )

    result.append(model_def)

    return result
