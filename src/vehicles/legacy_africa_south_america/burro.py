#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="burro",
        base_numeric_id=9130,
        name="0-4-2 Burro",
        power=650,
        intro_year=1850,
    )

    consist_cabbage.add_unit(type=SteamEngineUnit, weight=40, vehicle_length=6, spriterow_num=0)

    return consist_cabbage
