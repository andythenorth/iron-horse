from train import PassengerEngineRailbusConsist, DieselRailcarPaxUnit


def main(roster_id):
    consist = PassengerEngineRailbusConsist(
        roster_id=roster_id,
        id="zipper",
        base_numeric_id=5670,
        name="Zipper",
        role="pax_railbus",
        role_child_branch_num=1,
        power=280,
        gen=6,
        sprites_complete=False,
    )

    consist.add_unit(
        type=DieselRailcarPaxUnit,
        weight=25,
        chassis="railbus_lwb_24px",
        tail_light="railcar_24px_1", # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    )

    consist.description = """ """
    consist.foamer_facts = """ """

    return consist
