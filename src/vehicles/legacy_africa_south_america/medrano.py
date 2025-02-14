from train import PassengerEngineConsist, MetroUnit


def main(**kwargs):
    consist_cabbage = PassengerEngineConsist(
        id="medrano",
        base_numeric_id=10530,
        name="Medrano",
        power=1100,
        intro_year=2000,
    )

    # should be 4 units, not 2
    consist_cabbage.add_unit(
        type=MetroUnit, weight=30, vehicle_length=8, capacity=200, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=MetroUnit, weight=30, vehicle_length=8, capacity=200, spriterow_num=1
    )

    return consist_cabbage
