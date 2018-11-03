from train import EngineConsist, DieselEngineUnit
# for rest of stats, look up Krauss Maffei Brazil
consist = EngineConsist(id='krauss',
                        base_numeric_id=260,
                        name='Krauss',
                        base_track_type='NG',
                        power=3500,
                        type_base_buy_cost_points=-10,  # dibble buy cost for game balance
                        intro_date=1963)

consist.add_unit(type=DieselEngineUnit,
                 weight=150,
                 vehicle_length=8,
                 spriterow_num=0)
