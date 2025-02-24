from train import PassengerEngineBase, MetroUnit


def main(**kwargs):
    consist_cabbage = PassengerEngineBase(
        id="manzana",
        base_numeric_id=10520,
        name="Manzana",
        power_by_power_source={
            "METRO": 900,
        },
        intro_year=1950,
    )

    # should be 4 units not 2
    consist_cabbage.add_unit(
        type=MetroUnit, weight=40, vehicle_length=8, capacity=160, rel_spriterow_index=0
    )

    consist_cabbage.add_unit(
        type=MetroUnit, weight=40, vehicle_length=8, capacity=160, rel_spriterow_index=1
    )

    return consist_cabbage
