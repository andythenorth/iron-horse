from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="PassengerEngineExpressRailcar",
        model_id="turbulent",
        base_numeric_id=15320,
        name="Turbulent",
        subrole="express_pax_railcar",
        subrole_child_branch_num=-1,  # joker to hide them from simplified mode
        power_by_power_source={
            "DIESEL": 1200,
        },
        gen=4,
        intro_year_offset=1,  # introduce later by design
        livery_group_name="CABBAGE_RAILCAR",  # override default liveries from gestalt
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselExpressRailcarPaxUnit",
        weight=50,
        chassis="railcar_32px",
        tail_light="railcar_32px_3",
        repeat=2,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """BR Class 124 DMU, using turbine from SNCF Class T 1000 ETG Turbotrain"""
    )

    result.append(model_def)

    return result
