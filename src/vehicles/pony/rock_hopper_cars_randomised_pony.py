from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------
    # !!! see also gen 4A quarry hopper combos
    """
    model_def = ModelDef(
        schema_name="HopperCarRockRandomised",
        base_numeric_id=29180,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_16px")

    result.append(model_def)
    """
    model_def = ModelDef(
        schema_name="HopperCarRockRandomised",
        base_numeric_id=31290,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarRockRandomised",
        base_numeric_id=31340,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarRockRandomised",
        base_numeric_id=29690,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_24px")

    result.append(model_def)

    model_def = ModelDef(
        schema_name="HopperCarRockRandomised",
        base_numeric_id=29650,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    model_def.add_unit_def(unit_cls_name="FreightCarUnit", chassis="empty_32px")

    result.append(model_def)

    return result
