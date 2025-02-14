from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="yillen",
        base_numeric_id=6370,
        name="Yillen",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's be a little earlier for this one
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    # 2 separate units so that buy menu has reversed cabs
    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=67, vehicle_length=5, spriterow_num=0
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=67, vehicle_length=5, spriterow_num=1
    )

    model_def.define_description("""The universe is asymmetric. And so are these.""")
    model_def.define_foamer_facts("""BR Class 15, BR Class 16""")

    result.append(model_def)

    return result
