from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="MailExpressRailcarTrailerCar",
        base_numeric_id=6350,
        gen=5,
        subtype="U",
        cab_id="chronos",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="MailRailcarTrailerCar",
        chassis="4_axle_solid_express_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    result.append(model_def)

    return result
