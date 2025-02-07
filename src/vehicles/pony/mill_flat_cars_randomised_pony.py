from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=32650,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        intro_year_offset=20,  # these are pushed right back to line up with standard gauge versions
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=32780,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27900,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27910,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27920,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27930,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27940,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27950,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27960,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27970,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarMillRandomisedConsist",
        base_numeric_id=27980,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_1cc_filled_32px"
    )

    result.append(model_def)

    return result
