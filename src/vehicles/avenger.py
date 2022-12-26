from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="avenger",
        base_numeric_id=13900,
        name="Avenger",
        role="ultra_heavy_express",
        role_child_branch_num=1,
        power_by_power_source={
            "AC": 5800,
        },
        random_reverse=True,
        gen=5,
        speed=125,  # Shredder not replaced, but has gen 6 speeds
        pantograph_type="z-shaped-single",
        intro_year_offset=-2,  # introduce slightly earlier than gen epoch by design
        additional_liveries=["GNER", "RAILFREIGHT_TRIPLE_GREY"],
        default_livery_extra_docs_examples=[
            ("COLOUR_BLUE", "COLOUR_WHITE"),
            ("COLOUR_ORANGE", "COLOUR_WHITE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=100, vehicle_length=8, spriterow_num=0
    )

    consist.description = """Daft as a brush if you ask me.  Or mad as a badger.  Goes like stink off a shovel though."""
    consist.foamer_facts = """BR Class 89"""

    return consist
