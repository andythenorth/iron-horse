from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33120,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33140,
        gen=2,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33160,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33180,
        gen=3,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33200,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33220,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33240,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="2_axle_running_gear_only_alt_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=33260,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_alt_32px",
    )

    result.append(model_def)

    return result
