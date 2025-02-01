from train import MailExpressRailcarTrailerCarConsist, MailRailcarTrailerCar


def main(roster_id, **kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = MailExpressRailcarTrailerCarConsist(
        roster_id=roster_id,
        roster_id_providing_module=kwargs["roster_id_providing_module"],
        base_numeric_id=6350,
        gen=5,
        subtype="U",
        cab_id="chronos",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        type=MailRailcarTrailerCar,
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(consist_factory)

    return result
