from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='flanders_storm',
                        base_numeric_id=1740,
                        name='Flanders Storm',
                        role='heavy_freight_2',
                        power=6400,
                        # dibble for game balance, assume super-slip control
                        tractive_effort_coefficient=0.4,
                        random_reverse=True,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        gen=5,
                        pantograph_type='z-shaped-double',
                        intro_date_offset=5)  # introduce later than gen epoch by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=120,
                 vehicle_length=8,
                 spriterow_num=0)
