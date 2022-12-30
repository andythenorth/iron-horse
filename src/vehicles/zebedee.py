from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="zebedee",
        base_numeric_id=13990,
        name="Zebedee",
        role="super_heavy_express",
        role_child_branch_num=-3,  # it's a joker, tried it as super heavy express 1, the power progression and dates are all wrong for that
        power_by_power_source={
            "AC": 4000,
        },
        random_reverse=True,
        gen=4,
        pantograph_type="z-shaped-double",
        intro_year_offset=9,  # introduce much later than gen epoch by design
        additional_liveries=[],
        default_livery_extra_docs_examples=[("COLOUR_BLUE", "COLOUR_WHITE")],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=82, vehicle_length=8, spriterow_num=0
    )

    consist.description = """These were heavy on the track, but we had em back and fitted extra springs."""
    consist.foamer_facts = """BR Class 87, Class 86"""

    return consist
