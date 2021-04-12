from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="d_train",
        base_numeric_id=5670,
        name="D-Train",
        role="pax_railbus",
        role_child_branch_num=1,
        power=180,
        gen=6,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=18,
        chassis="2_axle_filled_24px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    )

    consist.description = """ """
    consist.foamer_facts = """ """

    return consist
