from train import EngineConsist, ElectricEngineUnit


def main(**kwargs):
    consist = EngineConsist(
        id="v8",
        base_numeric_id=9450,
        name="V8 2-C+C-2",
        power=4000,
        intro_year=1949,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=160, vehicle_length=8, spriterow_num=0
    )

    return consist
