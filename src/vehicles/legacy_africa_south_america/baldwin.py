#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="baldwin",
        base_numeric_id=9100,
        name="2-8-2 Baldwin",
        power=1600,
        base_track_type_name="NG",
        intro_year=1920,
    )

    consist_cabbage.add_unit(type=SteamEnginePoweredUnit, weight=70, vehicle_length=7, spriterow_num=0)

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=25, vehicle_length=4, spriterow_num=1
    )

    return consist_cabbage
