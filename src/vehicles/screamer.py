from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='screamer',
                        base_numeric_id=450,
                        name='Screamer',
                        role='express_2',
                        power=5000,
                        type_base_buy_cost_points=71,  # dibble buy cost for game balance
                        random_reverse=True,
                        intro_date=1995)  # explicit intro date by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=85,
                 vehicle_length=8,
                 spriterow_num=0)

