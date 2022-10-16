from train import PieceGoodsCarRandomisedConsist, FreightCar


def main():
    # --------------- pony NG -------------------------------------------------------------------

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15850,
        gen=1,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15820,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=15800,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # --------------- pony ----------------------------------------------------------------------

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17080,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    # no new type A for gen 2, gen 1 type A continues

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17090,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17100,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17110,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17120,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_16px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17130,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17180,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17140,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17150,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17160,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_24px")

    consist = PieceGoodsCarRandomisedConsist(
        roster_id="pony",
        base_numeric_id=17170,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="empty_32px")
