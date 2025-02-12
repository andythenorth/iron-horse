from train import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25330,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=24090,
        gen=1,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25000,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25010,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=26690,
        gen=3,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_32px")

    result.append(model_def)

    # no gen 4A NG coach

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34220,
        gen=4,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25550,
        gen=4,
        subtype="C",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_ng_32px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34620,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="2_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34630,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=30410,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="6_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34640,
        gen=2,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="2_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34650,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=30420,
        gen=2,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="6_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34660,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="3_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34670,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=30430,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=34680,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25300,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25310,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCarConsist",
        base_numeric_id=25320,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCar", chassis="4_axle_solid_express_32px")

    result.append(model_def)

    return result
