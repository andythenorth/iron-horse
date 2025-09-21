from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="westrail",
        base_numeric_id=23000,
        name="Westrail",
        subrole="freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
            "OHLE": 3450,
        },
        pantograph_type="z-shaped-single",
        # no random reverse
        gen=5,
        intro_year_offset=6,  # introduce later than gen epoch by design
        liveries=["VANILLA", "BANGER_BLUE", "SWOOSH", "SWOOSH", "INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    model_def.add_unit_def(
        class_name="ElectroDieselEngineUnit",
        weight=98,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """Westrail P Class"""  # https://en.wikipedia.org/wiki/Westrail_P_class
    )

    result.append(model_def)

    return result
