from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="intrepid",
        base_numeric_id=21520,
        name="Intrepid",
        subrole="heavy_express",
        subrole_child_branch_num=-1,  # -ve because Joker
        power_by_power_source={
            "DIESEL": 2200,
        },
        random_reverse=True,
        gen=4,
        fixed_run_cost_points=40,  # give a bonus so this can be a genuine mixed-traffic engine
        intro_year_offset=6,  # let's be later for this one
        extended_vehicle_life=True,
        default_livery_extra_docs_examples=[("COLOUR_GREEN", "COLOUR_WHITE")],
        caboose_family="railfreight_1",
        # add triple grey railfreight
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["LARGE_LOGO", "RAILFREIGHT_RED_STRIPE"],
        sprites_complete=True,
        sprites_additional_liveries_potential=True,  # triple grey railfreight?
    )

    consist_factory.define_unit(
        class_name="DieselEngineUnit",
        weight=100,  # bonus over Wyvern, less than IRL as HP is nerfed
        vehicle_length=8,
        spriterow_num=0,
    )

    consist_factory.define_description(
        """These are a bit duff, but they're a bit lighter than a Wyvern so we'll give em a go."""
    )
    consist_factory.define_foamer_facts(
        """BR Class 47, prime mover downrated for reliability"""
    )

    result.append(consist_factory)

    return result
