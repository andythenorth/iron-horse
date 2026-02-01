from train.model_def import ModelDef


def main(**kwargs):
    result = []

    # --------------- metro ---------------------------------------------------------------
    model_def = ModelDef(
        schema_name="PassengeMetroTrailerCar",
        base_numeric_id=260,
        gen=1,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
        cab_id="serpentine",
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=22,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengeMetroTrailerCar",
        base_numeric_id=860,
        gen=1,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
        cab_id="poplar",
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=24,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengeMetroTrailerCar",
        base_numeric_id=2150,
        gen=2,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
        cab_id="westbourne",
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=22,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengeMetroTrailerCar",
        base_numeric_id=5200,
        gen=2,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
        cab_id="hammersmith",
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=24,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengeMetroTrailerCar",
        base_numeric_id=15270,
        gen=3,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
        cab_id="fleet",
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=22,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    result.append(model_def)

    model_def = ModelDef(
        schema_name="PassengeMetroTrailerCar",
        base_numeric_id=15290,
        gen=3,
        subtype="U",
        base_track_type="METRO",
        sprites_complete=True,
        cab_id="canary",
    )

    model_def.add_unit_def(
        unit_cls_name="MetroUnit",
        weight=24,
        capacity=120,
        chassis="metro_low_floor_32px",
        tail_light="metro_32px_2",
        repeat=2,
    )

    result.append(model_def)

    return result
