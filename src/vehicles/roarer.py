from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='roarer',
                        base_numeric_id=2230,
                        title='Roarer [Electric]',
                        power=3200,
                        speed=110,
                        type_base_buy_cost_points=30,  # dibble buy cost for game balance
                        gen=4)

consist.add_unit(type=ElectricEngineUnit,
                 weight=80,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
