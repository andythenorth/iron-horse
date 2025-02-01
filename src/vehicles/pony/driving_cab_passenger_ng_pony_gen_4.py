from train import ConsistFactory


def main(roster_id, **kwargs):
    consist_factory = ConsistFactory(
        class_name="PassengerEngineCabControlCarConsist",
        roster_id=roster_id,
        id="driving_cab_passenger_ng_pony_gen_4",
        base_numeric_id=23260,
        name="Driving Trailer",
        subrole_child_branch_num=-1,  # driving cab cars are probably jokers?
        base_track_type_name="NG",
        gen=4,
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="CabControlPaxCarUnit", weight=32, chassis="4_axle_ng_32px"
    )

    consist_factory.description = (
        """Now, a driving cab for the smaller trains. But not for goats."""
    )
    consist_factory.foamer_facts = (
        """KiwiRail SRV driving cab conversion of British Rail MK2 carriage"""
    )

    return consist_factory
