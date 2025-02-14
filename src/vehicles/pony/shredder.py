from train.factory import ModelDef


def main(**kwargs):
    result = []

    model_def = ModelDef(
        class_name="EngineConsist",
        base_id="shredder",
        base_numeric_id=21350,
        name="Shredder",  # Griffon and Shredder names are wrong way round, but seems to suit the shapes so eh, leave it :)
        subrole="express",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2150,  # intended for short mail / supplies trains
        },
        random_reverse=True,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,
        intro_year_offset=7,  # introduce later than gen epoch by design
        additional_liveries=["SWOOSH", "SWOOSH", "SWOOSH"],
        sprites_complete=True,
    )

    model_def.add_unit_def(
        class_name="DieselEngineUnit", weight=76, vehicle_length=8, spriterow_num=0
    )

    model_def.define_description(
        """I'm not saying I hate em. But they're not much to love are they?"""
    )
    model_def.define_foamer_facts("""EMD JT42HW-HS (Class 67)""")

    result.append(model_def)

    return result
