from train import EngineConsist, DieselEngineUnit


def main(roster_id, **kwargs):
    consist = EngineConsist(
        roster_id=roster_id,
        id="shredder",
        base_numeric_id=21350,
        name="Shredder",  # Griffon and Shredder names are wrong way round, but seems to suit the shapes so eh, leave it :)
        role="express",
        role_child_branch_num=1,
        power_by_power_source={
            "DIESEL": 2150,  # intended for short mail / supplies trains
        },
        random_reverse=True,
        fixed_run_cost_points=120,  # give a bonus so this can be a genuine mixed-traffic engine
        gen=5,
        intro_year_offset=7,  # introduce later than gen epoch by design
        additional_liveries=["SWOOSH", "SWOOSH", "SWOOSH"],
        sprites_complete=True,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=76, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """I'm not saying I hate em. But they're not much to love are they?"""
    )
    consist.foamer_facts = """EMD JT42HW-HS (Class 67)"""

    return consist
