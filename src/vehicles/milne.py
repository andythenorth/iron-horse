from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='milne',
                        base_numeric_id=2050,
                        title='4-8-2 Milne [Steam]',
                        power=600,
                        track_type='NG',
                        speed=55,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        type_base_running_cost_points=-15,  # dibble running costs for game balance
                        reversible=True,
                        intro_date=1910)

consist.add_unit(type=SteamEngineUnit,
                 weight=50,
                 vehicle_length=7,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)