from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="PassengerEngineCabControlCarConsist",
        id="driving_cab_passenger_pony_gen_4",
        base_numeric_id=20040,
        name="Driving Trailer",
        subrole_child_branch_num=-1,  # driving cab cars are probably jokers?
        gen=4,
        intro_year_offset=16,  # a lot later, very short lived, replaced by gen 5 quickly
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="CabControlPaxCarUnit", weight=32, chassis="railcar_32px"
    )

    model_def.define_description(
        """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    )
    model_def.define_foamer_facts(
        """BR MK2 Driving Brake Standard Open (DBSO) with added generator"""
    )

    result.append(model_def)

    return result
