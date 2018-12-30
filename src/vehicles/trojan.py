from train import EngineConsist, DieselEngineUnit

# deprecated Dec 2018 - replace with Ultra Shoebox
# this might cause a monoculture of Ultra Shoeboxes, which might be boring?

consist = EngineConsist(id='trojan',
                        base_numeric_id=780,
                        name='Trojan',
                        role='branch_freight',
                        power=1600,
                        random_reverse=True,
                        joker=True,
                        gen=6,
                        intro_date_offset=+5,
                        sprites_complete=False)

consist.add_unit(type=DieselEngineUnit,
                 weight=74,
                 vehicle_length=6,
                 spriterow_num=0)
