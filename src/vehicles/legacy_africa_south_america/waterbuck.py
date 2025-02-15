#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="waterbuck",
        base_numeric_id=11060,
        name="Waterbuck",
        power_by_power_source={
            "DIESEL": 2200,
        },
        base_track_type_name="NG",
        intro_year=1990,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=120, vehicle_length=8, spriterow_num=0
    )

    return consist_cabbage
