from train import EngineConsist, ElectricEngineUnit


def main(**kwargs):
    consist_cabbage = EngineConsist(
        id="ge289a",
        base_numeric_id=10500,
        name="GE 289a Boxcab",
        power=1200,
        base_track_type_name="NG",
        intro_year=1922,
    )

    consist_cabbage.add_unit(
        type=ElectricEngineUnit, weight=64, vehicle_length=6, spriterow_num=0
    )

    return consist_cabbage
