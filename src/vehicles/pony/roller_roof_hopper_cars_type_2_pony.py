from train.producer import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge -----------------------------------------------------------------

    model_def = ModelDef(
        schema_name="MineralCoveredHopperCarRollerRoofType2",
        base_numeric_id=24610,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_16px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MineralCoveredHopperCarRollerRoofType2",
        base_numeric_id=24630,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MineralCoveredHopperCarRollerRoofType2",
        base_numeric_id=22950,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_16px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="MineralCoveredHopperCarRollerRoofType2",
        base_numeric_id=27920,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="FreightCarUnit", chassis="2_axle_gapped_greebled_24px"
    )

    result.append(model_def)

    return result
