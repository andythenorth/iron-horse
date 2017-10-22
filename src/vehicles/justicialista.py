from train import EngineConsist, DieselLoco

consist = EngineConsist(id='justicialista',
                        base_numeric_id=250,
                        title='Justicialista [Diesel]',
                        power=5880,  # yes, really, it's high powered
                        speed=85,
                        intro_date=1955)

consist.add_unit(type=DieselLoco,
                 weight=114,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_unit(type=DieselLoco,
                 weight=114,
                 vehicle_length=8,
                 spriterow_num=1)

consist.add_model_variant(spritesheet_suffix=0)
