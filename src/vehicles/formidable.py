from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='formidable',
                            base_numeric_id=5380,
                            name='Formidable',
                            role='heavy_freight',
                            role_child_branch_num=-2, # in the diesel branch, not electric
                            power=3500, # HP matched to equivalent gen pure diesels
                            power_by_railtype={'RAIL': 3500, 'ELRL': 8200}, # based on the Stadler Eurodual, really quite high values eh, notably el-power is insane high
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
