from train import AutomobileCarConsist, AutomobileCar


def main():
    # --------------- pony ----------------------------------------------------------------------
    # no gen 1 or 2, straight to gen 3
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5750,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="3_axle_solid_express_24px")

    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5760,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_solid_express_32px")

    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5740,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_solid_express_24px")

    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5730,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_solid_express_32px")
    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5710,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_24px")

    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5720,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")

    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5770,
        gen=6,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_24px")

    consist = AutomobileCarConsist(
        roster_id="pony",
        base_numeric_id=5780,
        gen=6,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=AutomobileCar, chassis="4_axle_filled_greebled_32px")
