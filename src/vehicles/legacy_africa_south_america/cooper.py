from train import EngineConsist, DieselEngineUnit


def main(**kwargs):  # GE Shovelnose - meter gauge ish
    consist_cabbage = EngineConsist(
        id="cooper",
        base_numeric_id=10480,
        name="Cooper",
        power_by_power_source={
            "DIESEL": 1000,
        },
        base_track_type_name="NG",
        intro_year=1949,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=85, vehicle_length=7, spriterow_num=0
    )

    return consist_cabbage
