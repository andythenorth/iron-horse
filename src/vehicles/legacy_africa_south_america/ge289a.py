# from train import foo


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="ge289a",
        base_numeric_id=10500,
        name="GE 289a Boxcab",
        power=1200,
        base_track_type_name="NG",
        intro_year=1922,
    )

    consist_cabbage.add_unit(
        type=ElectricEngineUnit, weight=64, vehicle_length=6, rel_spriterow_index=0
    )

    return consist_cabbage
