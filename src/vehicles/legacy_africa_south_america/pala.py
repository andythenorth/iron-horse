#from train import foo 


def main(**kwargs):  # standard gauge GE Shovelnose
    consist_cabbage = ModelDefFoo(
        id="pala", base_numeric_id=9360, name="Pala", power=1200, intro_year=1955
    )

    consist_cabbage.add_unit(
        type=DieselEngineUnit, weight=105, vehicle_length=7, spriterow_num=0
    )

    return consist_cabbage
