from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="xerxes",
        base_numeric_id=6760,
        name="0-6-0+0-6-0 Xerxes",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1450,
        },
        random_reverse=True,
        gen=1,
        intro_year_offset=20,  # introduce much later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=140,  # minor run cost bonus as default algorithm makes run cost too high
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="SteamEngineUnit",
        weight=49,
        vehicle_length=5,
        spriterow_num=0,
        repeat=2,
    )

    consist_factory.define_description("""Not much to say about these two.""")
    consist_factory.define_foamer_facts(
        """GWR pannier tanks, original TTD Kirby 'Paul'"""
    )

    result.append(consist_factory)

    return result
