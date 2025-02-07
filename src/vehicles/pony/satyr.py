from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_def = ModelTypeFactory(
        class_name="EngineConsist",
        id="satyr",
        base_numeric_id=31010,
        name="4-6-4 Satyr",
        subrole="express",
        subrole_child_branch_num=-2,
        power_by_power_source={
            "STEAM": 1450,
        },
        tractive_effort_coefficient=0.24,
        random_reverse=True,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "SWOOSH", "FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_def.define_unit(
        class_name="SteamEngineUnit", weight=90, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description("""Bob on.""")
    model_def.define_foamer_facts(
        """LB&SCR L Class, L&YR Hughes <i>Dreadnought tanks</i>"""
    )

    result.append(model_def)

    return result
