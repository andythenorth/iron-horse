from train import ModelTypeFactory


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------
    """

    model_def =ModelTypeFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=34300,
        gen=3,
        intro_year_offset=20,  # let's be a little bit later for this one
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_16px")

    result.append(model_def)


    model_def =ModelTypeFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=32850,
        gen=3,
        intro_year_offset=20,  # let's be a little bit later for this one
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=False,
    )

    model_def.define_unit(class_name="FreightCar", chassis="4_axle_ng_24px")

    result.append(model_def)
   """
    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelTypeFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=20280,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="2_axle_gapped_16px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=22980,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_24px"
    )

    result.append(model_def)

    model_def = ModelTypeFactory(
        class_name="HopperCarAggregateConsistType3",
        base_numeric_id=20300,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="FreightCar", chassis="4_axle_filled_32px"
    )

    result.append(model_def)

    return result
