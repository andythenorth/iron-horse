# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="hofman",
        base_numeric_id=10880,
        name="2-6-2+2-6-2 Hofman",
        tractive_effort_coefficient=0.27,  # dibble for game balance
        power=750,
        base_track_type_name="NG",
        intro_year=1940,
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=15, vehicle_length=3, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=SteamEnginePoweredUnit, weight=30, vehicle_length=4, spriterow_num=1
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=15, vehicle_length=3, spriterow_num=2
    )

    return consist_cabbage
