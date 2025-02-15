#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="kessler",
        base_numeric_id=11030,
        name="0-4-2 Kessler",
        power=450,
        base_track_type_name="NG",
        random_reverse=True,
        intro_year=1860,
    )

    consist_cabbage.add_unit(type=SteamEngineUnit, weight=25, vehicle_length=5, spriterow_num=0)

    return consist_cabbage
