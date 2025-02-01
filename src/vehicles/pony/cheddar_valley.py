from train import ConsistFactory


def main(**kwargs):
    result = []

    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="cheddar_valley",
        base_numeric_id=21300,
        name="Cheddar Valley",
        subrole="super_heavy_freight",
        subrole_child_branch_num=3,
        power_by_power_source={
            "DIESEL": 4200,
        },
        # dibble for game balance, assume super-slip control
        tractive_effort_coefficient=0.4,
        random_reverse=True,
        intro_year_offset=3,  # let's be a little bit later for this one
        gen=5,
        fixed_run_cost_points=210,  # unrealism: run cost nerf for being so high-powered
        # unfinished EWS livery exists, but eh
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["YEOMAN", "DB_SCHENKER", "FREIGHTLINER_GBRF", "ARC"],
        default_livery_extra_docs_examples=[
            ("COLOUR_WHITE", "COLOUR_GREEN"),
            ("COLOUR_ORANGE", "COLOUR_RED"),
        ],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="DieselEngineUnit",
        weight=125,
        vehicle_length=8,
        effect_offsets=[(1, 0)],
        spriterow_num=0,
    )

    consist_factory.add_description(
        """I shipped these in from overseas.  Pull you backwards through a wall this one will.  Right proper engine."""
    )
    consist_factory.add_foamer_facts(
        """GMD  / EMD Class 59, uprated GMD / EMD 710 series prime mover"""
    )

    result.append(consist_factory)

    return result
