#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="americano",
        base_numeric_id=9060,
        name="4-4-0 Americano",
        power=1000,
        intro_year=1850,
    )

    consist_cabbage.add_unit(type=SteamEngineUnit, weight=52, vehicle_length=5, spriterow_num=0)

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, spriterow_num=1
    )

    return consist_cabbage
