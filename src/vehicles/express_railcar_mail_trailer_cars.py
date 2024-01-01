from train import MailExpressRailcarTrailerCarConsist, MailRailcarTrailerCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = MailExpressRailcarTrailerCarConsist(
        roster_id="pony",
        base_numeric_id=4900,
        gen=5,
        subtype="U",
        cab_id="chronos",
        sprites_complete=False,
    )

    consist.add_unit(
        type=MailRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )
