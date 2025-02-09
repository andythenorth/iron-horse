from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="dragon",
        base_numeric_id=21070,
        name="Dragon",
        subrole="super_heavy_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2750,
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=1,  # introduce later than gen epoch by design
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_YELLOW"),
        ],
        caboose_family="gwr_1",
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit",
        weight=99,
        vehicle_length=8,
        effect_offsets=[(-1, 0), (1, 0)],  # double the smoke eh?
        spriterow_num=0,
    )

    model_def.define_description("""A right big fast diesel hydraulic this one is.""")
    model_def.define_foamer_facts("""BR Class 52 <i>Western</i>""")

    result.append(model_def)

    return result
