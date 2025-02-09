from train import ModelDef, AlignmentCar


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="AlignmentCarConsist",
        base_numeric_id=9060,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name=AlignmentCar, vehicle_length=4, chassis="2_axle_solid_express_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AlignmentCarConsist",
        base_numeric_id=9070,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name=AlignmentCar, vehicle_length=6, chassis="4_axle_solid_express_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="AlignmentCarConsist",
        base_numeric_id=9080,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name=AlignmentCar, vehicle_length=8, chassis="4_axle_solid_express_32px"
    )

    result.append(model_def)

    return result
