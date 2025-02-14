from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist_cabbage = EngineConsist(
        id="gazelle",
        base_numeric_id=11070,
        name="Gazelle",
        power_by_power_source={
            "DIESEL": 1800,
        },
        base_track_type_name="NG",
        intro_year=1975,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=90, vehicle_length=7, spriterow_num=0
    )

    return consist_cabbage
