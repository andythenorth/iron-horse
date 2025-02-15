from train.factory import ModelDef


def main(**kwargs):
    result = []

    # --------------- narrow gauge -----------------------------------------------------------------

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=32810,
        gen=2,
        subtype="A",
        base_track_type_name="NG",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=32830,
        gen=3,
        subtype="A",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_sparse_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=17570,
        gen=3,
        subtype="B",
        base_track_type_name="NG",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_ng_sparse_24px")

    result.append(model_def)

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=25780,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=27850,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="3_axle_filled_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=25800,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="4_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=19270,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(class_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=19290,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=19310,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_gapped_greebled_alt_32px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=19330,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_gapped_greebled_alt_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=19350,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        class_name="TankCarAcidType2",
        base_numeric_id=19370,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="FreightCarUnit", chassis="4_axle_gapped_greebled_alt_32px"
    )

    result.append(model_def)

    return result
