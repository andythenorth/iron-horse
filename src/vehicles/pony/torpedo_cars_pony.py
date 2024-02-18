from train import TorpedoCarConsist, TorpedoCar


def main(roster_id, **kwargs):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=4140,
        gen=2,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=4060,
        gen=3,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=4170,
        gen=4,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist = TorpedoCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=4090,
        gen=5,
        subtype="U",
        sprites_complete=True,
    )

    consist.add_unit(type=TorpedoCar, vehicle_length=3)

    consist.add_unit(type=TorpedoCar, vehicle_length=6)

    consist.add_unit(type=TorpedoCar, vehicle_length=3)
