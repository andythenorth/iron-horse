# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="ndemi",
        base_numeric_id=11110,
        name="4-8-0 Ndemi",
        power=1700,
        base_track_type_name="NG",
        intro_year=1887,
    )

    consist_cabbage.add_unit(
        type=SteamEnginePoweredUnit, weight=75, vehicle_length=8, rel_spriterow_index=0
    )

    consist_cabbage.add_unit(
        type=SteamEngineTenderUnit, weight=35, vehicle_length=4, rel_spriterow_index=1
    )

    return consist_cabbage
