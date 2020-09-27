from train import PassengerVeryHighSpeedCabEngineConsist, ElectricHighSpeedPaxUnit


def main(roster_id):
    consist = PassengerVeryHighSpeedCabEngineConsist(roster_id=roster_id,
                                                     id='brenner_cab',
                                                     base_numeric_id=130,
                                                     name='Brenner Cab',
                                                     role='very_high_speed',
                                                     role_child_branch_num=1,
                                                     dual_headed=True,
                                                     power=3000,
                                                     gen=6,
                                                     intro_date_offset=-3,  # introduce earlier than gen epoch by design
                                                     sprites_complete=True)

    consist.add_unit(type=ElectricHighSpeedPaxUnit,
                     weight=52,
                     spriterow_num=0,
                     chassis='4_axle_solid_express_32px',
                     tail_light='very_high_speed_32px_2')

    consist.description = """"""
    consist.cite = """Dr. Constance Speed"""
    consist.foamer_facts = """Alstom Class 390 <i>Pendolino</i>."""

    return consist
