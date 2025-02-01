from train import CoveredHopperCarRandomisedConsist, FreightCar


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # gen 2 start

    consist_factory = CoveredHopperCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17240,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = CoveredHopperCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=17250,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = CoveredHopperCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35830,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="empty_16px")

    result.append(consist_factory)

    consist_factory = CoveredHopperCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35840,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = CoveredHopperCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35860,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="empty_24px")

    result.append(consist_factory)

    consist_factory = CoveredHopperCarRandomisedConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=35870,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist_factory.add_unit(type=FreightCar, chassis="empty_32px")

    result.append(consist_factory)

    return result
