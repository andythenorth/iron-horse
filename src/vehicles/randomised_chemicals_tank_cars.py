from train import TankCarChemicalsRandomisedConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8330,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8350,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8360,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8370,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8380,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8460,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8390,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8400,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8410,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = TankCarChemicalsRandomisedConsist(
        roster_id="pony",
        base_numeric_id=8420,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
