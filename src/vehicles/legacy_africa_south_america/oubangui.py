#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="oubangui",
        base_numeric_id=11050,
        name="2-6-6-2 Oubangui",
        power=1500,
        base_track_type_name="NG",
        intro_year=1920,
    )

    consist_cabbage.add_unit(type=SteamEnginePoweredUnit, weight=90, vehicle_length=8, spriterow_num=0)

    return consist_cabbage
