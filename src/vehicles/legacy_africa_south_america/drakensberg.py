#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="drakensberg",
        # !! This vehicle needs more than one id range due to length
        base_numeric_id=10840,
        name="4-8-2+2-8-4 Drakensberg",
        tractive_effort_coefficient=0.25,
        power=3000,
        base_track_type_name="NG",
        intro_year=1945,
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=4, spriterow_num=0
    )

    consist_cabbage.add_unit(type=SteamEngineUnit, weight=80, vehicle_length=6, spriterow_num=1)

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=65, vehicle_length=4, spriterow_num=2
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=45, vehicle_length=6, spriterow_num=3
    )

    return consist_cabbage
