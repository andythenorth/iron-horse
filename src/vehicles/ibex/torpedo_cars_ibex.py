from train import TorpedoCarConsist, TorpedoCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        base_numeric_id=390,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        base_numeric_id=490,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        base_numeric_id=90,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        base_numeric_id=310,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)
