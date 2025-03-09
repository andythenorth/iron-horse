from train import PassengerEngineBase, MetroUnit


def main(**kwargs):
    model_def = PassengerEngineBase(
        id="riachuelo",
        base_numeric_id=10510,
        name="Riachuelo",
        power=600,
        intro_year=1900,
    )

    # should be 4 units not 2
    model_def.add_unit(
        type=MetroUnit, weight=40, vehicle_length=8, capacity=120, rel_spriterow_index=0
    )

    model_def.add_unit(
        type=MetroUnit, weight=40, vehicle_length=8, capacity=120, rel_spriterow_index=1
    )

    return model_def
