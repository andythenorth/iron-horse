# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="patagonia",
        base_numeric_id=9370,
        name="Patagonia",
        base_track_type_name="NG",
        power=500,
        intro_year=1960,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=20, vehicle_length=7, capacity=35, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=20, vehicle_length=7, capacity=35, spriterow_num=1
    )

    return consist_cabbage
