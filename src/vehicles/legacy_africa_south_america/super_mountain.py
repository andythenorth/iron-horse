#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="super_mountain",
        base_numeric_id=9550,
        name="4-8-4 Super Mountain",
        power=2100,
        intro_year=1935,
    )

    consist_cabbage.add_unit(
        type=SteamEngineUnit, weight=110, vehicle_length=8, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=60, vehicle_length=6, spriterow_num=1
    )

    return consist_cabbage
