from train import ConsistFactory


def main(**kwargs):
    consist_factory = ConsistFactory(
        class_name="EngineConsist",
        id="tyrconnell",
        base_numeric_id=930,
        name="4-8-0 Tyrconnell",
        subrole="universal",
        subrole_child_branch_num=-4,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 900,
        },
        tractive_effort_coefficient=0.28,
        gen=2,
        intro_year_offset=-5,  # introduce early eh
        random_reverse=False,
        # note that livery names are metadata only and can repeat for different spriterows
        # additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=True,
    )

    consist_factory.add_unit(
        class_name="SteamEngineUnit", weight=45, vehicle_length=5, spriterow_num=0
    )

    consist_factory.add_unit(
        class_name="SteamEngineTenderUnit", weight=19, vehicle_length=3, spriterow_num=1
    )

    consist_factory.description = """A titan from the North. Steadfast and stout."""
    consist_factory.foamer_facts = (
        """Londonderry and Lough Swilly Railway Company 4-8-0 locomotives"""
    )

    return consist_factory
