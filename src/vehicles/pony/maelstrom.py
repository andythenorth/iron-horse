from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="maelstrom",
        base_numeric_id=21050,
        name="Maelstrom",
        subrole="heavy_freight",
        subrole_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2200,  # keep in line with equivalent gen general purpose engines
        },
        random_reverse=True,
        gen=4,
        intro_year_offset=-2,  # let's not have everything turn up in 1960
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["SWOOSH", "BANGER_BLUE", "SWOOSH"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="DieselEngineUnit", weight=115, vehicle_length=8, spriterow_num=0
    )

    consist_factory.define_description(
        """Not enough people see it as a healthy horse, pulling a sturdy wagon."""
    )
    consist_factory.define_foamer_facts("""BR Class 41""")

    result.append(consist_factory)

    return result
