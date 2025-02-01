# coding=utf-8

from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    # for rest of stats, look up GE Evolution
    consist = EngineConsist(
        id="evolucao",
        base_numeric_id=9240,
        name="Evolução",
        power=4400,
        intro_year=1995,
    )

    consist.add_unit(
        type=DieselEngineUnit, weight=40, vehicle_length=8, spriterow_num=0
    )

    return consist
