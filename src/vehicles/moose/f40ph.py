from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="f40ph",
        base_numeric_id=22010,
        name="F40PH",
        subrole="branch_express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 1800,
        },
        random_reverse=True,
        fixed_run_cost_points=140,  # substantial cost bonus as a mixed traffic engine
        gen=4,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        sprites_complete=False,
    )

    model_type_factory.define_unit(
        class_name="DieselEngineUnit", weight=110, vehicle_length=6, spriterow_num=0
    )

    model_type_factory.define_description("""""")
    model_type_factory.define_foamer_facts("""""")

    result.append(model_type_factory)

    return result
