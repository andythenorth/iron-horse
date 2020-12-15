from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='quietus',
                            base_numeric_id=5370,
                            name='Quietus',
                            role='very_heavy_freight',
                            role_child_branch_num=-2, # in the diesel branch, not electric
                            power=4500, # HP matched to equivalent gen pure diesels
                            power_by_railtype={'RAIL': 4500, 'ELRL': 6800}, # based on the CAF Bitrac, really quite high values for both diesel and el
                            random_reverse=True,
                            pantograph_type='z-shaped-double',
                            gen=6,
                            intro_date_offset=10,  # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=ElectroDieselEngineUnit,
                     weight=95,
                     vehicle_length=8,
                     spriterow_num=0)

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
