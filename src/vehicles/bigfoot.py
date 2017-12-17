from train import EngineConsist, DieselEngineUnit
# roughly an SAR 91-000 class
consist = EngineConsist(id='bigfoot',
                        base_numeric_id=1620,
                        title='Bigfoot [Diesel]',
                        power=900,
                        track_type='NG',
                        speed=70,
                        type_base_buy_cost_points=-5,  # dibble buy cost for game balance
                        type_base_running_cost_points=-10,  # dibble running costs for game balance
                        intro_date=1970)

consist.add_unit(type=DieselEngineUnit,
                 weight=50,
                 vehicle_length=5,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
