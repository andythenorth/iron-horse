from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='estados',
                        base_numeric_id=190,
                        name='Estados Boxcab',
                        power=1450,
                        intro_date=1925)

consist.add_unit(type=ElectricEngineUnit,
                 weight=90,
                 vehicle_length=6,
                 spriterow_num=0)
