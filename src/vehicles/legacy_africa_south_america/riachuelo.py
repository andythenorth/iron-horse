from train import PassengerEngineConsist, MetroUnit


def main(**kwargs):
    consist_cabbage = PassengerEngineConsist(
        id="riachuelo",
        base_numeric_id=10510,
        name="Riachuelo",
        power=600,
        intro_year=1900,
    )

    # should be 4 units not 2
    consist_cabbage.add_unit(
        type=MetroUnit, weight=40, vehicle_length=8, capacity=120, spriterow_num=0
    )

    consist_cabbage.add_unit(
        type=MetroUnit, weight=40, vehicle_length=8, capacity=120, spriterow_num=1
    )

    return consist_cabbage
