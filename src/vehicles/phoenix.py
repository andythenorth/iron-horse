from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="phoenix",
        base_numeric_id=9200,
        name="Phoenix",
        role="freight",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2100,  # really it's just a livery upgrade
        },
        random_reverse=True,
        gen=6,
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """The Slugs were right knackered, so we've put a new engine in to make this."""
    )
    consist.foamer_facts = """Class 37, re-engineered with new prime mover"""

    return consist
