from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="haar",
        base_numeric_id=1880,
        name="0-8-0 Haar",
        subrole="freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "STEAM": 1500,
        },
        tractive_effort_coefficient=0.24,
        gen=3,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["FREIGHT_BLACK"],
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="SteamEngineUnit", weight=70, vehicle_length=5, spriterow_num=0
    )

    model_type_factory.define_unit(
        class_name="SteamEngineTenderUnit", weight=40, vehicle_length=3, spriterow_num=1
    )

    model_type_factory.define_description(
        """This is right ugly, but the shed likes them. Easy to maintain. They'll do."""
    )
    model_type_factory.define_foamer_facts("""SR Q1 Class, LMS Class 7F""")

    result.append(model_type_factory)

    return result
