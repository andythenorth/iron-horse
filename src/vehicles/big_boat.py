from train import EngineConsist, DieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="big_boat",
        base_numeric_id=1600,
        name="Big Boat",
        power=4500,
        # dibble up TE, modern diesels can cheat adhesion using wheel slip
        tractive_effort_coefficient=0.35,
        intro_date=1985,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=190, vehicle_length=8, spriterow_num=0
    )

    # I tried the Big Boat with a long-hood forward random variant, but it looked bad, removed it.

    return consist
