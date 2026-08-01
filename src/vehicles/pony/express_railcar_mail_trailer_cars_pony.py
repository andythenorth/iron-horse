from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MailExpressRailcarTrailerCar",
        base_numeric_id=6350,
        gen=5,
        subtype="U",
        cab_id="chronos",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="MailRailcarTrailerCarUnit",
        chassis="4_axle_solid_pax_mail_32px",
        repeat=2,
    )

    result.append(model_def)

    return result
