from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- standard gauge ---------------------------------------------------------------

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=16960,
        gen=2,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17000,
        gen=2,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17070,
        gen=3,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17250,
        gen=3,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17400,
        gen=4,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17420,
        gen=4,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_32px",
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17440,
        gen=5,
        subtype="B",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_24px"
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="FlatCarDropCentreType2",
        base_numeric_id=17610,
        gen=5,
        subtype="C",
        sprites_complete=False,
    )

    model_def.add_unit_def(
        unit_cls_name="AutomobileCarAsymmetricUnit", # CABBAGE
        chassis="4_axle_running_gear_only_32px",
    )

    result.append(model_def)

    return result
