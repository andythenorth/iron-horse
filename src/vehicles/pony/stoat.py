from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="stoat",
        base_numeric_id=21480,
        name="Stoat",
        subrole="branch_freight",
        subrole_child_branch_num=-3,
        power_by_power_source={
            "AC": 1050,
        },
        speed=60,  # continues a long way into gen 3, so go faster
        random_reverse=True,
        pantograph_type="diamond-single",
        gen=2,
        intro_year_offset=3,  # introduce later than gen epoch by design
        extended_vehicle_life=True,
        fixed_run_cost_points=105,  # substantial cost bonus so it can make money
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["BANGER_BLUE", "INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.define_unit(
        class_name="ElectricEngineUnit", weight=54, vehicle_length=6, spriterow_num=0
    )

    consist_factory.define_description("""Nippy little bugger.""")
    consist_factory.define_foamer_facts(
        """NER ES1, Metropolitan Railway camel-back and box-cab locomotives, Westoe Colliery electrics, generic steeple-cab locomotives"""
    )

    result.append(consist_factory)

    return result
