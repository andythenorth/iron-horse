#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="pequeno",
        base_numeric_id=9390,
        name="0-4-0 Pequeno",
        power=350,
        base_track_type_name="NG",
        intro_year=1865,
    )

    consist_cabbage.add_unit(type=SteamEnginePoweredUnit, weight=40, vehicle_length=4, spriterow_num=0)

    return consist_cabbage
