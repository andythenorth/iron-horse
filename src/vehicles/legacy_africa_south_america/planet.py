# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="planet",
        base_numeric_id=360,
        name="Planet",
        base_track_type_name="NG",
        power=500,
        intro_year=1950,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=40, vehicle_length=4, rel_spriterow_index=0
    )

    return consist_cabbage
