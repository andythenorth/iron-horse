from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="dynamo",
        base_numeric_id=20970,
        name="Dynamo",
        subrole="express",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "AC": 1900,  # matches or better than equivalent gen steam engines
        },
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        intro_year_offset=5,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=180,  # substantial cost bonus for balance against same-era steam engines
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=[],
        default_livery_extra_docs_examples=[
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_PINK"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="ElectricEngineUnit", weight=92, vehicle_length=8, spriterow_num=0
    )

    consist_factory.add_description("""Nowt to fuss about with this one.""")
    consist_factory.add_foamer_facts(
        """SR CC1/CC2 locomotives, English Electric Class EP01 exported from UK to Poland"""
    )

    result.append(consist_factory)

    return result
