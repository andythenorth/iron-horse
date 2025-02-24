# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="kwa_falls",
        base_numeric_id=11010,
        name="2-8-2 Kwa Falls",
        power=1800,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1945,
    )

    consist_cabbage.add_unit(
        type=SteamEnginePoweredUnit, weight=100, vehicle_length=7, rel_spriterow_index=0
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, rel_spriterow_index=1
    )

    return consist_cabbage
