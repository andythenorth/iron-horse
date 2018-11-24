from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='flindermouse',
                        base_numeric_id=790,
                        name='Flindermouse',
                        role='heavy_freight_2',
                        power=1100,
                        joker=True,  # this engine doesn't fit the set roster pattern, by design it's to mix things up
                        gen=3,
                        pantograph_type='diamond-double',
                        intro_date_offset=-20)  # introduce earlier than gen epoch by design

consist.add_unit(type=ElectricEngineUnit,
                 weight=65,
                 vehicle_length=6,
                 spriterow_num=0)
