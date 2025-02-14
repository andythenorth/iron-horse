from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist_cabbage = EngineConsist(
        id="big_boat",
        base_numeric_id=10640,
        name="Big Boat",
        power=4500,
        # dibble up TE, modern diesels can cheat adhesion using wheel slip
        tractive_effort_coefficient=0.35,
        intro_year=1985,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=190, vehicle_length=8, spriterow_num=0
    )

    # I tried the Big Boat with a long-hood forward random variant, but it looked bad, removed it.

    return consist_cabbage
