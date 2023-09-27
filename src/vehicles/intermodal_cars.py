from train import IntermodalCarConsist, IntermodalCar


def main():
    # --------------- pony ng ----------------------------------------------------------------------
    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=13000,
        gen=4,
        subtype="U",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_ng_16px")

    # --------------- pony ----------------------------------------------------------------------
    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=12920,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="2_axle_filled_16px")

    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=12930,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_gapped_24px")

    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=12750,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_gapped_32px")

    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=12760,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="2_axle_1cc_filled_16px")

    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=12770,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_1cc_filled_24px")

    consist = IntermodalCarConsist(
        roster_id="pony",
        base_numeric_id=12780,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=IntermodalCar, chassis="4_axle_1cc_filled_32px")
