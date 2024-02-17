from train import AlignmentCarConsist, AlignmentCar


def main(roster_id):
    # --------------- standard gauge ---------------------------------------------------------------

    consist = AlignmentCarConsist(
        roster_id=roster_id,
        base_numeric_id=9060,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AlignmentCar, vehicle_length=4, chassis="2_axle_solid_express_16px"
    )

    consist = AlignmentCarConsist(
        roster_id=roster_id,
        base_numeric_id=9070,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AlignmentCar, vehicle_length=6, chassis="4_axle_solid_express_24px"
    )

    consist = AlignmentCarConsist(
        roster_id=roster_id,
        base_numeric_id=9080,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(
        type=AlignmentCar, vehicle_length=8, chassis="4_axle_solid_express_32px"
    )
