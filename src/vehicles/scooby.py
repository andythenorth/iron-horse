from train import EngineConsist, DieselRailcarMail

consist = EngineConsist(id='scooby',
                        base_numeric_id=3070,
                        title='Scooby [Diesel]',
                        power=420,
                        speed=75,
                        type_base_running_cost_points=-32,  # dibble running costs for game balance
                        intro_date=1955)  # explicit intro date by design

consist.add_unit(type=DieselRailcarMail,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 spriterow_num=3)

consist.add_model_variant(spritesheet_suffix=0)
