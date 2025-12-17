from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=34740,
        gen=2,
        subtype="B",
        livery_group_name="gen_2_motorail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="3_axle_solid_express_24px"
    )

    result.append(model_def)

    #     model_def = ModelDef(
    #         schema_name="AutomobileMotorailCar",
    #         base_numeric_id=38760,
    #         gen=2,
    #         subtype="C",
    #         sprites_complete=False,
    #     )
    #
    #     model_def.add_unit_def(
    #         schema_name="ExpressCarUnit", chassis="4_axle_solid_express_32px"
    #     )
    #
    #     result.append(model_def)
    #
    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=20820,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="3_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=18000,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=34420,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="2_axle_lwb_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=18010,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=36290,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_motorail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="2_axle_lwb_filled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="AutomobileMotorailCar",
        base_numeric_id=32780,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_motorail_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="ExpressCarUnit", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
