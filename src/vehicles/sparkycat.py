from train import EngineConsist, ElectroDieselEngineUnit

consist = EngineConsist(id='sparkycat',
                        base_numeric_id=160,
                        title='SparkyCat [ElectroDiesel]',
                        power=1850,
                        speed=110,
                        type_base_buy_cost_points=60,  # dibble buy cost for game balance
                        gen=6,
                        power_by_railtype={'RAIL': 1850, 'ELRL': 3700})

consist.add_unit(type=ElectroDieselEngineUnit,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
