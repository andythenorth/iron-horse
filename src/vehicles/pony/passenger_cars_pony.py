from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=23740,
        gen=1,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=23680,
        gen=1,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=22410,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=22430,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=22450,
        gen=3,
        subtype="C",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_32px")

    result.append(model_def)

    # no gen 4A NG coach

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=22470,
        gen=4,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=22490,
        gen=4,
        subtype="C",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="4_axle_ng_32px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=23010,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="3_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=20840,
        gen=1,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18210,
        gen=1,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="6_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18190,
        gen=2,
        subtype="A",
        livery_group_name="gen_2_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="3_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18230,
        gen=2,
        subtype="B",
        livery_group_name="gen_2_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18250,
        gen=2,
        subtype="C",
        livery_group_name="gen_2_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="6_axle_solid_express_32px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18270,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="PaxCarUnit", chassis="3_axle_solid_express_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18290,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18310,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18330,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=18680,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=19080,
        gen=5,
        subtype="B",
        livery_group_name="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="PassengerCar",
        base_numeric_id=19100,
        gen=5,
        subtype="C",
        livery_group_name="gen_5_and_6_pax_liveries",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="PaxCarUnit", chassis="4_axle_solid_pax_mail_32px"
    )

    result.append(model_def)

    return result
