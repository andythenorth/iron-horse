# deprecated
from train import ModelTypeFactory


def main(**kwargs):
    result = []

    model_type_factory = ModelTypeFactory(
        class_name="EngineConsist",
        id="decapod",
        base_numeric_id=26080,
        name="0-10-0 Decapod",
        subrole="branch_express",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 650,
        },
        gen=2,
        intro_year_offset=7,  # let's be a little bit later for this one
        tractive_effort_coefficient=0.2,
        fixed_run_cost_points=120,  # substantial cost bonus so it can make money
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE"],
        sprites_complete=True,
    )

    model_type_factory.define_unit(
        class_name="SteamEngineUnit", weight=54, vehicle_length=6, spriterow_num=0
    )

    model_type_factory.define_description(
        """Don't know what they were thinking, but they asked me to build it. Well, it's done."""
    )
    model_type_factory.define_foamer_facts("""GER Class A55 <i>Decapod</i>""")

    result.append(model_type_factory)

    return result
