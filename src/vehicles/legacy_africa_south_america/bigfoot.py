from train import EngineConsist, DieselEngineUnit


def main(**kwargs):  # roughly an SAR 91-000 class
    consist_cabbage = EngineConsist(
        id="bigfoot",
        base_numeric_id=10660,
        name="Bigfoot",
        power=900,
        base_track_type_name="NG",
        intro_year=1970,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=50, vehicle_length=5, spriterow_num=0
    )

    return consist_cabbage
