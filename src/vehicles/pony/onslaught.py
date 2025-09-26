from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="SimpleEngine",
        model_id="onslaught",
        base_numeric_id=21470,
        name="Onslaught",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 3450,
        },
        random_reverse=True,
        gen=5,
        intro_year_offset=-8,  # let's be really early with this one to give a mail engine matching Blaze HST intro year
        # additional_liveries=["BANGER_BLUE", "SUPERGRAPHIC", "VANILLA", "INTERCITY_RASPBERRY_RIPPLE", "RAILFREIGHT_TRIPLE_GREY", "DUTCH"],
        liveries=["CLASSIC_LINES", "BANGER_BLUE", "DB_SCHENKER"],
        decor_spriterow_num=8,
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=100,
        vehicle_length=8,
        rel_spriterow_index=0,
    )

    model_def.define_description("""Aye I do like these. Right loud too.""")
    model_def.define_foamer_facts(
        """BR Class 50, proposed English Electric / BR Class 51 <i>Super Deltic</i>"""
    )

    result.append(model_def)

    return result
