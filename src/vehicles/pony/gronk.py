from train import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        id="gronk",
        base_numeric_id=21490,
        name="Gronk",
        subrole="gronk",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "DIESEL": 400,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=4,
        intro_year_offset=-9,  # introduce much earlier than gen epoch by design
        extended_vehicle_life=True,  # extended vehicle life for all gronks eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "DB_SCHENKER", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=55, vehicle_length=4, spriterow_num=0
    )

    model_def.define_description(
        """The universal shunter.  Goes everywhere&hellip;slowly."""
    )
    model_def.define_foamer_facts("""BR Class 08/09""")

    result.append(model_def)

    model_def = model_def.begin_clone(base_numeric_id=990, unit_repeats=[1])

    # this is a JFDI thing, the 2-unit version varies sprites per unit position, which is generally supported
    # but the *buy menu* compositor does not support that as of Jan 2024, so hax
    model_def.unit_defs[0].spriterow_num = 1
    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=55, vehicle_length=4, spriterow_num=0
    )

    # JFDI, the single unit should randomly reverse, the 2-unit version should not, so hax
    model_def.kwargs["random_reverse"] = False

    model_def.complete_clone()

    result.append(model_def)

    return result
