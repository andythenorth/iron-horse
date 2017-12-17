from train import EngineConsist, DieselEngineUnit
# GE Shovelnose - meter gauge ish
consist = EngineConsist(id='cooper',
                        base_numeric_id=1440,
                        title='Cooper [Diesel]',
                        power=1000,
                        track_type='NG',
                        speed=55,
                        intro_date=1949)

consist.add_unit(type=DieselEngineUnit,
                 weight=85,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
