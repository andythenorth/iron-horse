from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="keen",
        base_numeric_id=470,
        name="0-6-0+0-6-0 Keen",
        subrole="heavy_freight",
        subrole_child_branch_num=-1,
        power_by_power_source={
            "STEAM": 1800,
        },
        random_reverse=True,
        gen=3,
        intro_year_offset=-13,  # introduce much earlier than gen epoch by design
        fixed_run_cost_points=240,  # adjust to match similar engines of same gen
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit",
        weight=58,
        vehicle_length=5,
        spriterow_num=0,
        repeat=2,
    )

    consist_factory.description = """Gallop apace, you fiery-footed steeds."""
    consist_factory.foamer_facts = (
        """18in Hunslet tanks, Austerity tanks, LNER J94 Class"""
    )

    return consist_factory
