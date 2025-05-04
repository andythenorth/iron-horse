from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    # no gen 2 for NG, straight to gen 3

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=24360,
        gen=3,
        subtype="A",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=25930,
        gen=3,
        subtype="B",
        base_track_type="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=25880,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=24470,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=23360,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=18060,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=30820,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="FarmCargoMixedCombos",
        base_numeric_id=31010,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
