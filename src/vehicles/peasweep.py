from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='peasweep',
                        base_numeric_id=1750,
                        name='Peasweep',
                        role='heavy_freight_2',
                        power=3600,
                        type_base_buy_cost_points=40,  # dibble buy cost for game balance
                        type_base_running_cost_points=-5,  # dibble run cost for game balance
                        joker=True, # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        gen=4,
                        intro_date_offset=-13) # introduce earlier than gen epoch by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=75,
                 vehicle_length=6,
                 spriterow_num=0,
                 repeat=2)

