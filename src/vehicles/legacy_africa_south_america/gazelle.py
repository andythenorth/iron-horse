# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
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
        type=DieselEngineUnit, weight=90, vehicle_length=7, rel_spriterow_index=0
    )

    return consist_cabbage
