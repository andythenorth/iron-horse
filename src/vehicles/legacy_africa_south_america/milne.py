#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="milne",
        base_numeric_id=11090,
        name="4-8-2 Milne",
        power=600,
        base_track_type_name="NG",
        random_reverse=True,
        intro_year=1910,
    )

    consist_cabbage.add_unit(type=SteamEngineUnit, weight=50, vehicle_length=7, spriterow_num=0)

    return consist_cabbage
