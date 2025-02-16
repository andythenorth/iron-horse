# from train import foo


def main(**kwargs):  # for rest of stats, look up Krauss Maffei Brazil
    consist_cabbage = ModelDefFoo(
        id="krauss",
        base_numeric_id=9300,
        name="Krauss",
        base_track_type_name="NG",
        power_by_power_source={
            "DIESEL": 3500,
        },
        intro_year=1963,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=150, vehicle_length=8, spriterow_num=0
    )

    return consist_cabbage
