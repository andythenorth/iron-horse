from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_type_factory = ModelTypeFactory(
        class_name="MailExpressRailcarTrailerCarConsist",
        base_numeric_id=6350,
        gen=5,
        subtype="U",
        cab_id="chronos",
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="MailRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_type_factory)

    return result
