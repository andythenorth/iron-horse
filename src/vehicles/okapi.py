from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='okapi',
                        base_numeric_id=1960,
                        title='Okapi [Diesel]',
                        power=1850,
                        track_type='NG',
                        speed=65,
                        type_base_running_cost_points=-2,  # dibble running costs for game balance
                        intro_date=1958)

consist.add_unit(type=DieselEngineUnit,
                 weight=100,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
