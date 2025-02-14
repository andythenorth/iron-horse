from train import EngineConsist, DieselEngineUnit


def main(**kwargs):
    consist_cabbage = EngineConsist(
        id="savannah_slammer",
        base_numeric_id=10580,
        name="Savannah Slammer",
        power=500,
        intro_year=1980,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=65, vehicle_length=8, capacity=65, spriterow_num=0
    )

    return consist_cabbage
