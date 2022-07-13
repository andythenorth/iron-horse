from train import DumpCarScrapMetalConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    # gen 2 start eh?
    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=14130,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=14140,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=14150,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13220,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13230,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13240,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13250,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=8610,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13270,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13280,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")

    # no gen 6A?

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13300,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=13310,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
