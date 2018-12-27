from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='peasweep',
                        base_numeric_id=1750,
                        name='Peasweep',
                        role='heavy_freight_2',
                        power=3700,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        gen=4,
                        pantograph_type='diamond-double',
                        intro_date_offset=-13,  # introduce earlier than gen epoch by design
                        sprites_complete=True)

consist.add_unit(type=ElectricEngineUnit,
                 weight=75,
                 vehicle_length=6,
                 spriterow_num=0,
                 repeat=2)
