from train import EngineConsist, CabbageDVTUnit, DrivingCabUnitPax


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="auto_coach_pony_gen_2",
        base_numeric_id=4690,
        name="Auto Coach",
        role='heavy_express',
        role_child_branch_num=2,
        gen=2,
        power=50,
        sprites_complete=False,
    )

    consist.add_unit(
        type=CabbageDVTUnit,
        weight=32,
        chassis="jacobs_solid_express_20px",
    )

    consist.add_unit(
        type=DrivingCabUnitPax,
        weight=32,
        chassis="jacobs_solid_express_20px",
    )

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
