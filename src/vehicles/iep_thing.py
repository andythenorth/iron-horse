from train import PassengerHSTCabEngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = PassengerHSTCabEngineConsist(
        roster_id=roster_id,
        id="iep_thing",
        base_numeric_id=5390,
        name="Double Tide IEP",
        role="hst",  # quite a specific role, may or may not scale to other rosters
        role_child_branch_num=2,
        power=4500,
        power_by_railtype={"RAIL": 4500, "ELRL": 8000},
        intro_date_offset=-10,  # let's be a little bit earlier for this one - keep match to HST coaches
        gen=6,
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit,
        weight=70,
        vehicle_length=8,
        effect_offsets=[(0, 1), (0, -1)],  # double the smoke eh?
        spriterow_num=0,
        tail_light="hst_32px_1",
    )

    consist.description = """"""
    consist.foamer_facts = """"""

    return consist
