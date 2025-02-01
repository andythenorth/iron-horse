from train import EngineConsist, DieselEngineUnit


def main(**kwargs):  # for rest of stats, look up Chinese CKD8G
    consist = EngineConsist(
        id="roca", base_numeric_id=9440, name="Roca", power=3000, intro_year=1990
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=30, vehicle_length=8, spriterow_num=0
    )

    return consist
