from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="PassengerEngineCabControlCarConsist",
        id="driving_cab_high_speed_passenger_pony_gen_5",
        base_numeric_id=19900,
        name="High Speed Driving Trailer",
        subrole_child_branch_num=-2,  # driving cab cars are probably jokers?
        gen=5,
        lgv_capable=True,  # for lolz
        liveries="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="CabControlPaxCarUnit", weight=32, chassis="railcar_32px"
    )

    consist_factory.add_description(
        """Front or back of a train, up to you. Supplies hotel power for the coaches, so your main loco has more power for traction. Clever idea we had eh?"""
    )
    consist_factory.add_foamer_facts(
        """proposed BR MK5 Driving Trailer (DT) with added generator"""
    )

    result.append(consist_factory)

    return result
