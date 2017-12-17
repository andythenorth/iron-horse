from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='toaster',
                        base_numeric_id=990,
                        title='Toaster [Diesel]',
                        power=4200,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        speed=110,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        gen=6)

consist.add_unit(type=DieselEngineUnit,
                 weight=140,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
