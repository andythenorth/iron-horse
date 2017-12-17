from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='slug',
                        base_numeric_id=1000,
                        title='Slug [Diesel]',
                        power=1700,
                        speed=90,
                        gen=5)

consist.add_unit(type=DieselEngineUnit,
                 weight=110,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
