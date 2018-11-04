from train import EngineConsist, ElectricEngineUnit

consist = EngineConsist(id='ge289a',
                        base_numeric_id=1460,
                        name='GE 289a Boxcab',
                        power=1200,
                        base_track_type='NG',
                        intro_date=1922)

consist.add_unit(type=ElectricEngineUnit,
                 weight=64,
                 vehicle_length=6,
                 spriterow_num=0)
