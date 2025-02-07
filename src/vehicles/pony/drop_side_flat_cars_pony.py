from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30130,
        gen=1,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30700,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30820,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30520,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    # no gen 2A, gen 1A continues in pony

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30530,
        gen=2,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="3_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30540,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30580,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30630,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30590,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30510,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30880,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_gapped_32px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30840,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_filled_greebled_alt_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="FlatCarDropSideConsist",
        base_numeric_id=30910,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_greebled_32px"
    )

    result.append(model_def)

    return result
