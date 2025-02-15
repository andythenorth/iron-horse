#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="albertine",
        base_numeric_id=11080,
        name="4-4-2 Albertine",
        power=1200,
        tractive_effort_coefficient=0.19,
        base_track_type_name="NG",
        intro_year=1885,
    )

    consist_cabbage.add_unit(type=SteamEnginePoweredUnit, weight=45, vehicle_length=7, spriterow_num=0)

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=30, vehicle_length=4, spriterow_num=1
    )

    return consist_cabbage
