from train import DumpCarScrapMetalConsist, FreightCar


def main():
    # --------------- pony NG ----------------------------------------------------------------------
    # gen 2 start eh?
    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19070,
        gen=2,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19090,
        gen=3,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")

    """ # restore in next version
    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19110,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_ng_16px")
    """
    # --------------- pony ----------------------------------------------------------------------
    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19130,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19150,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19170,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19190,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19210,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_16px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19230,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_greebled_24px")

    consist = DumpCarScrapMetalConsist(
        roster_id="pony",
        base_numeric_id=19250,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_greebled_32px")
