from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='baby_boat',
                        base_numeric_id=1590,
                        title='Baby Boat [Diesel]',
                        power=1800,
                        speed=75,
                        intro_date=1978)

consist.add_unit(type=DieselEngineUnit,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
