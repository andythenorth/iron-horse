from train import EngineConsist, DieselEngineUnit
# standard gauge GE Shovelnose
consist = EngineConsist(id='pala',
                        base_numeric_id=320,
                        title='Pala [Diesel]',
                        power=1200,
                        speed=75,
                        intro_date=1955)

consist.add_unit(type=DieselEngineUnit,
                 weight=105,
                 vehicle_length=7,
                 spriterow_num=0)

