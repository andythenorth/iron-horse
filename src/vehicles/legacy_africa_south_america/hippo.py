#from train import foo 


def main(**kwargs):
    consist_cabbage = ModelDefFoo(
        id="hippo",
        base_numeric_id=10910,
        name="Hippo",
        power=3600,
        base_track_type_name="NG",
        intro_year=1975,
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=130, vehicle_length=8, spriterow_num=0
    )

    return consist_cabbage
