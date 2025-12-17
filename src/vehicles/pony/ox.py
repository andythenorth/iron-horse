from train.producer import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        schema_name="SimpleEngine",
        model_id="ox",
        base_numeric_id=31400,
        name="2-6-2 Ox",
        subrole="branch_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "STEAM": 800,
        },
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        random_reverse=True,
        gen=2,
        intro_year_offset=-5,  # more earlier trains are good eh?
        liveries=["STOCK_STANDARD", "FREIGHT_BLACK", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        unit_cls_name="SteamEnginePoweredUnit",
        weight=70,
        vehicle_length=6,
        rel_spriterow_index=0,
    )

    model_def.define_description("""""")
    model_def.define_foamer_facts(
        """"""
    )  # SOME SORT OF LNER 0-6-2t, but as 2-6-2t https://www.lner.info/locos/N/n10.php

    result.append(model_def)

    return result
