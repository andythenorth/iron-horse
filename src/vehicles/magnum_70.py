from train import EngineConsist, BatteryHybridEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="magnum_70",
        base_numeric_id=14000,
        name="Magnum 70",
        role="gronk!",
        role_child_branch_num=-2,
        power_by_power_source={
            "BATTERY_HYBRID": 500,
        },
        speed=35,
        # dibble TE up for game balance, assume low gearing or something
        tractive_effort_coefficient=0.375,
        fixed_run_cost_points=100,  # substantial cost bonus so it can make money
        random_reverse=True,
        gen=6,
        intro_year_offset=-6,  # introduce earlier than gen epoch by design
        vehicle_life=60,  # extended vehicle life for all gronks eh
        # banger blue?  some kind of industrial 'extra 'yellow'?
        additional_liveries=[],
        sprites_complete=False,
    )

    consist.add_unit(
        type=BatteryHybridEngineUnit, weight=70, vehicle_length=4, spriterow_num=0
    )

    consist.description = """Even Gronks don't last forever."""
    consist.foamer_facts = """Clayton CB40/CBD80/CBD90"""

    return consist
