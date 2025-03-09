# from train import foo


def main(**kwargs):
    model_def = ModelDefFoo(
        id="big_boat",
        base_numeric_id=10640,
        name="Big Boat",
        power=4500,
        # dibble up TE, modern diesels can cheat adhesion using wheel slip
        tractive_effort_coefficient=0.35,
        intro_year=1985,
    )

    model_def.add_unit(
        type=DieselEngineUnit, weight=190, vehicle_length=8, rel_spriterow_index=0
    )

    # I tried the Big Boat with a long-hood forward random variant, but it looked bad, removed it.

    return model_def
