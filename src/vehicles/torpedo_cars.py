from train import TorpedoCarConsist, TorpedoCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = TorpedoCarConsist(
        roster_id="pony",
        base_numeric_id=4060,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id="pony",
        base_numeric_id=4070,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id="pony",
        base_numeric_id=4080,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id="pony",
        base_numeric_id=4090,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    # no gen 6 for Pony, enough is enough
