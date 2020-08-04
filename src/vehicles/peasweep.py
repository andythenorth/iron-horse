from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='peasweep',
                            base_numeric_id=1750,
                            name='Peasweep',
                            role='heavy_freight',
                            role_child_branch_num=2,
                            power=3700,
                            gen=4,
                            pantograph_type='diamond-double',
                            intro_date_offset=-13,  # introduce earlier than gen epoch by design
                            sprites_complete=True)

    consist.add_unit(type=ElectricEngineUnit,
                     weight=75,
                     vehicle_length=6,
                     spriterow_num=0,
                     repeat=2)

    consist.foamer_facts = """LNER EM1 (BR Class 76)."""

    return consist
