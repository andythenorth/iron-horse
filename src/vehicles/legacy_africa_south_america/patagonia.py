from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="patagonia",
        base_numeric_id=9370,
        name="Patagonia",
        base_track_type_name="NG",
        power=500,
        intro_year=1960,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=20, vehicle_length=7, capacity=35, spriterow_num=0
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=20, vehicle_length=7, capacity=35, spriterow_num=1
    )

    return consist
