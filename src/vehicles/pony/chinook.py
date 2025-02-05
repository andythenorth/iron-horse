from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="chinook",
        base_numeric_id=120,
        name="Chinook",
        subrole="super_heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2900,
        },
        gen=4,
        fixed_run_cost_points=118,  # minor run cost bonus as default algorithm makes run cost too high
        caboose_family="railfreight_1",
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "RAILFREIGHT_RED_STRIPE", "SWOOSH"],
        default_livery_extra_docs_examples=[
            ("COLOUR_PALE_GREEN", "COLOUR_GREY"),
            ("COLOUR_BLUE", "COLOUR_GREY"),
        ],
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="DieselEngineUnit", weight=80, vehicle_length=6, spriterow_num=0
    )

    model_type_factory.define_unit(
        class_name="DieselEngineUnit", weight=80, vehicle_length=6, spriterow_num=1
    )

    model_type_factory.define_description("""I send these out in twos.""")
    model_type_factory.define_foamer_facts(
        """BR Class 20, uprated EE 8CSVT prime mover"""
    )

    result.append(model_type_factory)

    model_type_factory = model_type_factory.begin_clone(
        base_numeric_id=34900, unit_repeats=[1, 0]
    )

    # JFDI, the single unit should randomly reverse, the default 2-unit version should not, so hax
    model_type_factory.kwargs["random_reverse"] = True

    model_type_factory.complete_clone()

    result.append(model_type_factory)

    return result
