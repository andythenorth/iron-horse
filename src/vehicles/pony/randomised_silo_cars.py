from train import SiloCarRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = SiloCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17450,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = SiloCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17470,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = SiloCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17490,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = SiloCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17510,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = SiloCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17530,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = SiloCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17550,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
