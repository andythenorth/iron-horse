from train import ConsistFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    consist_factory = ConsistFactory(
        class_name="MailExpressRailcarTrailerCarConsist",
        base_numeric_id=6350,
        gen=5,
        subtype="U",
        cab_id="chronos",
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="MailRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(consist_factory)

    return result
