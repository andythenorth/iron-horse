# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="pacifico",
        base_numeric_id=9350,
        name="4-6-2 Pacifico",
        power=1800,
        intro_year=1910,
    )

    consist_cabbage.add_unit(
        type=SteamEnginePoweredUnit, weight=90, vehicle_length=7, rel_spriterow_index=0
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=40, vehicle_length=5, rel_spriterow_index=1
    )

    return consist_cabbage
